from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable

from .corpus import sha256_file


AGENT_AUDIT_FIELDS = [
    "split", "method", "query_id", "answerable", "status", "answer",
    "citations", "answer_grade_0_1_2", "citation_semantic_support",
    "abstention_correct", "audit_status", "reviewer_notes", "reviewed_at",
]
BENCHMARK_REVIEW_FIELDS = ["query_id", "decision", "notes", "reviewed_at"]
RUN_SPECS = {
    "dev/hybrid": ("dev", "hybrid", 17, "results/agent/dev/hybrid_traces.jsonl"),
    "test/dense": ("test", "dense", 7, "results/agent/test/dense_traces.jsonl"),
    "test/hybrid": ("test", "hybrid", 7, "results/agent/test/hybrid_traces.jsonl"),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def atomic_write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows({field: row.get(field, "") for field in fields} for row in rows)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def normalize_text(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def jaccard(left: str, right: str) -> float:
    a, b = set(normalize_text(left).split()), set(normalize_text(right).split())
    return len(a & b) / len(a | b) if a or b else 1.0


def automatic_benchmark_checks(root: Path, cases: list[dict[str, Any]], chunks: list[dict[str, Any]], manifest: dict[str, Any]) -> dict[str, Any]:
    chunk_by_id = {row["id"]: row for row in chunks}
    ids = [row.get("id") for row in cases]
    dev_ids = {row["id"] for row in cases if row.get("split") == "dev"}
    test_ids = {row["id"] for row in cases if row.get("split") == "test"}
    cross_duplicates = []
    for dev in (row for row in cases if row["split"] == "dev" and row["answerable"]):
        for test in (row for row in cases if row["split"] == "test" and row["answerable"]):
            same_answer = normalize_text(dev["gold_answer"]) == normalize_text(test["gold_answer"])
            near_duplicate = jaccard(dev["question"], test["question"]) >= 0.9 and jaccard(dev["gold_answer"], test["gold_answer"]) >= 0.9
            if same_answer or near_duplicate:
                cross_duplicates.append([dev["id"], test["id"]])

    per_case: dict[str, dict[str, Any]] = {}
    for case in cases:
        checks: dict[str, bool] = {
            "schema": isinstance(case.get("id"), str) and bool(case.get("question")) and case.get("split") in {"dev", "test"} and isinstance(case.get("answerable"), bool),
            "manual_status_pending": case.get("manual_audit_status") == "pending_review",
        }
        if case["answerable"]:
            gold_ids = case.get("gold_chunk_ids", [])
            resolved = [chunk_by_id.get(chunk_id) for chunk_id in gold_ids]
            checks.update({
                "gold_fields_present": bool(case.get("gold_answer")) and bool(case.get("gold_evidence")) and bool(gold_ids),
                "source_exists": any(chunk and chunk.get("source_id") == case.get("source") for chunk in resolved),
                "physical_page_valid": isinstance(case.get("physical_page"), int) and 1 <= case["physical_page"] <= manifest["physical_content_pages"],
                "gold_chunk_ids_exist": bool(resolved) and all(resolved),
                "evidence_in_declared_chunk_page": bool(resolved) and any(chunk and chunk["page"] == case["physical_page"] and chunk["source_id"] == case["source"] and case["gold_evidence"] in chunk["text"] for chunk in resolved),
            })
        else:
            checks.update({
                "no_fake_gold_fields": not any(key in case for key in ("gold_answer", "gold_evidence", "gold_chunk_ids")),
                "expected_abstention_present": case.get("expected_behavior") == "search_and_abstain" and bool(case.get("corpus_check")),
            })
        per_case[case["id"]] = {"automatic_check": "passed" if all(checks.values()) else "failed", "checks": checks}

    global_checks = {
        "total_24": len(cases) == 24,
        "split_17_dev_7_test": (len(dev_ids), len(test_ids)) == (17, 7),
        "answerability_counts": Counter((row["split"], row["answerable"]) for row in cases) == Counter({("dev", True): 15, ("dev", False): 2, ("test", True): 5, ("test", False): 2}),
        "unique_query_ids": len(ids) == len(set(ids)) == 24,
        "dev_test_disjoint": not (dev_ids & test_ids),
        "no_obvious_cross_split_duplicate": not cross_duplicates,
        "all_cases_pass": all(row["automatic_check"] == "passed" for row in per_case.values()),
        "manifest_page_count": manifest.get("physical_content_pages") == 51,
        "manifest_chunk_count": manifest.get("chunk_count") == len(chunks) == 191,
        "chunks_hash_matches_manifest": sha256_file(root / "artifacts" / "chunks.jsonl") == manifest.get("chunks_sha256"),
        "index_hash_matches_manifest": sha256_file(root / "artifacts" / "bge_vectors.f32") == manifest.get("index_sha256"),
        "embedding_contract": manifest.get("embedding_model") == "BAAI/bge-small-en-v1.5" and manifest.get("vector_dimension") == 384 and manifest.get("normalize_embeddings") is True,
    }
    source_path = Path(manifest["source_input"])
    global_checks["normalized_source_hash_matches_manifest"] = source_path.exists() and sha256_file(source_path) == manifest.get("source_normalized_sha256")
    passed = all(global_checks.values())
    return {
        "automatic_check": "passed" if passed else "failed",
        "global_checks": global_checks,
        "cross_split_duplicate_candidates": cross_duplicates,
        "per_case": per_case,
        "manual_review_status": "pending_review",
    }


def _contains_forbidden_payload_fields(value: Any) -> bool:
    if isinstance(value, dict):
        if set(value) & {"gold_answer", "gold_evidence", "expected_answer", "expected_behavior", "abstention_correct", "answer_grade"}:
            return True
        return any(_contains_forbidden_payload_fields(item) for item in value.values())
    if isinstance(value, list):
        return any(_contains_forbidden_payload_fields(item) for item in value)
    return False


def automatic_trace_checks(root: Path, cases: list[dict[str, Any]], chunks: list[dict[str, Any]], locked: dict[str, Any]) -> dict[str, Any]:
    case_by_id = {row["id"]: row for row in cases}
    chunk_by_id = {row["id"]: row for row in chunks}
    all_rows: list[tuple[str, int, dict[str, Any]]] = []
    per_trace: dict[str, dict[str, Any]] = {}
    run_checks: dict[str, dict[str, Any]] = {}
    for run, (split, method, expected_count, relative) in RUN_SPECS.items():
        path = root / relative
        traces = read_jsonl(path)
        expected_ids = {row["id"] for row in cases if row["split"] == split}
        actual_ids = [row.get("query_id") for row in traces]
        run_checks[run] = {
            "trace_file_exists": path.exists(),
            "execution_count": len(traces) == expected_count,
            "query_ids_match_benchmark": set(actual_ids) == expected_ids and len(actual_ids) == len(set(actual_ids)),
            "method_matches_run": all(row.get("retrieval_method") == method for row in traces),
            "split_matches_run": all(row.get("split") == split for row in traces),
        }
        for line_number, trace in enumerate(traces, 1):
            all_rows.append((run, line_number, trace))
            context = trace.get("final_context", [])
            context_ids = {row.get("id") for row in context}
            search_events = [event for event in trace.get("events", []) if event.get("event") == "search"]
            citation_pairs = re.findall(r"\[([a-f0-9]{32})\s*\|\s*page\s+(\d+)\]", trace.get("raw_model_answer", ""), flags=re.I)
            context_pages = {row.get("id"): row.get("page") for row in context}
            corpus_consistent = True
            for result in context:
                corpus = chunk_by_id.get(result.get("id"))
                if not corpus or any(result.get(key) != corpus.get(key) for key in ("source", "source_id", "page", "text")):
                    corpus_consistent = False
            serialized = json.dumps(trace, ensure_ascii=False)
            checks = {
                "query_id_and_split": trace.get("query_id") in case_by_id and case_by_id[trace["query_id"]]["split"] == split,
                "question_matches_benchmark": trace.get("query_id") in case_by_id and trace.get("question") == case_by_id[trace["query_id"]]["question"],
                "model_gpt_6_luna": trace.get("model") == "gpt-6-luna",
                "retrieval_method": trace.get("retrieval_method") == method,
                "exactly_one_tool_call": len(search_events) == 1,
                "tool_arguments_locked": bool(search_events) and search_events[0].get("arguments", {}).get("method") == method and search_events[0].get("arguments", {}).get("top_k") == 3,
                "top3_disclosure": 0 < len(context) <= 3 and len(search_events[0].get("results", [])) <= 3 if search_events else False,
                "citations_in_context": all(citation in context_ids for citation in trace.get("raw_model_citations", trace.get("citations", []))),
                "citation_pages_match_context": all(context_pages.get(chunk_id.lower()) == int(page) for chunk_id, page in citation_pairs),
                "final_context_ids_match": set(trace.get("final_context_ids", [])) == context_ids,
                "corpus_metadata_consistent": corpus_consistent,
                "no_gold_or_expected_payload_fields": not _contains_forbidden_payload_fields({"events": trace.get("events", []), "final_context": context}),
                "no_secret_or_local_path": not any(pattern in serialized for pattern in ("OPENAI_API_KEY", "sk-", "D:\\\\Coding", "C:\\\\Users")),
                "nonnegative_usage_latency_cost": all(isinstance(trace.get("usage", {}).get(key), int) and trace["usage"][key] >= 0 for key in ("input_tokens", "output_tokens", "total_tokens")) and isinstance(trace.get("latency_ms"), (int, float)) and trace["latency_ms"] >= 0 and isinstance(trace.get("estimated_api_cost_usd"), (int, float)) and trace["estimated_api_cost_usd"] >= 0,
                "token_and_cost_arithmetic": trace.get("usage", {}).get("total_tokens") == trace.get("usage", {}).get("input_tokens", 0) + trace.get("usage", {}).get("output_tokens", 0) and abs(trace.get("estimated_api_cost_usd", 0) - (trace.get("usage", {}).get("input_tokens", 0) * 0.10 / 1_000_000 + trace.get("usage", {}).get("output_tokens", 0) * 0.50 / 1_000_000)) < 1e-12,
                "answer_error_schema": isinstance(trace.get("answer"), str) and (trace.get("error") is None or isinstance(trace.get("error"), str)) and trace.get("status") in {"answered", "abstain", "error"},
            }
            per_trace[f"{run}:{trace.get('query_id')}"] = {"line": line_number, "automatic_check": "passed" if all(checks.values()) else "failed", "checks": checks}
    composite = [(run, trace.get("query_id")) for run, _, trace in all_rows]
    global_checks = {
        "exactly_31_executions": len(all_rows) == 31,
        "no_duplicate_execution": len(composite) == len(set(composite)),
        "all_runs_pass": all(all(values.values()) for values in run_checks.values()),
        "all_traces_pass": all(row["automatic_check"] == "passed" for row in per_trace.values()),
        "locked_method_unchanged": locked.get("locked") is True and locked.get("selected_method") == "hybrid" and locked.get("baseline_method") == "dense" and locked.get("candidate_top_k") == 10 and locked.get("final_context_k") == 3 and locked.get("rrf_k") == 60,
        "locked_manifest_hash_matches": sha256_file(root / "artifacts" / "corpus_manifest.json") == locked.get("corpus_manifest_sha256"),
        "test_not_used_before_lock": locked.get("test_metrics_seen_before_lock") is False and all(summary.get("split") == "dev" for summary in locked.get("dev_summaries", {}).values()),
        "total_cost_under_cap": sum(trace.get("estimated_api_cost_usd", 0) for _, _, trace in all_rows) < 1.0,
    }
    return {
        "automatic_check": "passed" if all(global_checks.values()) else "failed",
        "global_checks": global_checks,
        "run_checks": run_checks,
        "per_trace": per_trace,
        "summary": {
            "executions": len(all_rows),
            "successful": sum(trace.get("status") != "error" for _, _, trace in all_rows),
            "errors": sum(trace.get("status") == "error" for _, _, trace in all_rows),
            "input_tokens": sum(trace.get("usage", {}).get("input_tokens", 0) for _, _, trace in all_rows),
            "output_tokens": sum(trace.get("usage", {}).get("output_tokens", 0) for _, _, trace in all_rows),
            "estimated_cost_usd": sum(trace.get("estimated_api_cost_usd", 0) for _, _, trace in all_rows),
        },
    }


def evidence_context(text: str, evidence: str, radius: int = 180) -> str:
    start = text.find(evidence)
    if start < 0:
        return text[: radius * 2]
    left, right = max(0, start - radius), min(len(text), start + len(evidence) + radius)
    prefix = "…" if left else ""
    suffix = "…" if right < len(text) else ""
    return prefix + text[left:right] + suffix


def make_benchmark_packet(cases: list[dict[str, Any]], chunks: list[dict[str, Any]], checks: dict[str, Any]) -> str:
    chunk_by_id = {row["id"]: row for row in chunks}
    lines = [
        "# Manual benchmark review packet", "",
        "> All automatic checks are mechanical. Every checkbox below is intentionally blank and requires student review.", "",
    ]
    for case in cases:
        lines.extend([f"## {case['id']} — {case['split']} — {'answerable' if case['answerable'] else 'insufficient evidence'}", "", f"- **Question:** {case['question']}"])
        if case["answerable"]:
            chunk_id = case["gold_chunk_ids"][0]
            chunk = chunk_by_id[chunk_id]
            lines.extend([
                f"- **Gold answer:** {case['gold_answer']}",
                f"- **Source:** {case['source']}",
                f"- **Physical page:** {case['physical_page']}",
                f"- **Gold chunk ID:** `{chunk_id}`",
                f"- **Gold evidence:** {case['gold_evidence']}",
                "- **Evidence context:**",
                "", f"> {evidence_context(chunk['text'], case['gold_evidence']).replace(chr(10), ' ')}", "",
            ])
        else:
            lines.extend([
                "- **Expected behavior:** search and abstain when evidence remains insufficient.",
                f"- **Absence rationale:** {case['absence_reason']}",
                f"- **Corpus check procedure:** {case['corpus_check']}",
                "- **Source / page / gold chunk / evidence:** N/A by benchmark design.",
            ])
        automatic = checks["per_case"][case["id"]]
        lines.extend([
            f"- **Automatic check:** `{automatic['automatic_check']}` — " + ", ".join(f"{key}={str(value).lower()}" for key, value in automatic["checks"].items()),
            "", "Student checklist:", "",
            "- [ ] Question hợp lệ.",
            "- [ ] Gold answer / expected abstention đúng.",
            "- [ ] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.",
            "- [ ] Source/page đúng.",
            "- [ ] Không trùng hoặc rò rỉ dev/test.",
            "- **Ghi chú:** ________________________________________________", "",
        ])
    return "\n".join(lines) + "\n"


def _tokens(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", value.casefold()))


def make_agent_packet_and_hints(root: Path, cases: list[dict[str, Any]], trace_checks: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    case_by_id = {row["id"]: row for row in cases}
    lines = [
        "# Manual agent review packet", "",
        "> Gold fields below are shown only for post-execution human audit. Mechanical/AI hints are not official labels.", "",
    ]
    hints: list[dict[str, Any]] = []
    for run, (_, _, _, relative) in RUN_SPECS.items():
        for line_number, trace in enumerate(read_jsonl(root / relative), 1):
            case = case_by_id[trace["query_id"]]
            context_by_id = {row["id"]: row for row in trace["final_context"]}
            citations = trace.get("raw_model_citations", trace.get("citations", []))
            context_text = " ".join(row["text"] for row in trace["final_context"])
            answer_tokens = _tokens(trace.get("raw_model_answer", trace["answer"]))
            context_tokens = _tokens(context_text)
            overlap = len(answer_tokens & context_tokens) / len(answer_tokens) if answer_tokens else 0.0
            gold_recall = None
            if case["answerable"]:
                gold_tokens = _tokens(case["gold_answer"])
                gold_recall = len(gold_tokens & answer_tokens) / len(gold_tokens) if gold_tokens else 1.0
            hint = {
                "disclaimer": "AI/mechanical hints, not official labels",
                "run": run,
                "query_id": case["id"],
                "context_has_gold_evidence": trace.get("context_evidence"),
                "all_citation_ids_in_context": all(citation in context_by_id for citation in citations),
                "raw_abstention_detected": trace["status"] == "abstain",
                "answer_context_token_overlap": round(overlap, 4),
                "gold_answer_token_recall_hint": "" if gold_recall is None else round(gold_recall, 4),
                "missing_condition_warning": bool(gold_recall is not None and gold_recall < 0.5),
                "possible_unsupported_claim_warning": bool(trace["status"] == "answered" and overlap < 0.3),
            }
            hints.append(hint)
            lines.extend([
                f"## {run} · {case['id']}", "",
                f"- **Type:** {'answerable' if case['answerable'] else 'insufficient evidence'}",
                f"- **Question:** {case['question']}",
                f"- **Gold / expected behavior (post-run audit only):** {case.get('gold_answer', 'Search and abstain if evidence is insufficient.')}",
                f"- **Agent status:** `{trace['status']}`",
                f"- **Agent answer:** {trace['answer']}",
                f"- **Citation IDs:** {', '.join(f'`{value}`' for value in citations) if citations else 'none'}",
                f"- **Context contains strict gold evidence:** `{trace.get('context_evidence')}` (mechanical retrieval check)",
                f"- **Citation syntax/in-context check:** `{hint['all_citation_ids_in_context']}`",
                f"- **Raw abstention detected:** `{hint['raw_abstention_detected']}`",
                f"- **Tool-call count:** {sum(event.get('event') == 'search' for event in trace['events'])}",
                f"- **Usage:** input={trace['usage']['input_tokens']}, output={trace['usage']['output_tokens']}, total={trace['usage']['total_tokens']}",
                f"- **Latency / estimated cost:** {trace['latency_ms']:.3f} ms / ${trace['estimated_api_cost_usd']:.7f}",
                f"- **Original trace:** `{relative}:{line_number}`", "",
                "### Cited passages", "",
            ])
            if citations:
                for citation in citations:
                    row = context_by_id.get(citation)
                    if row:
                        lines.extend([f"**`{row['id']}` · rank {row['rank']} · page {row['page']} · {row['source']}**", "", row["text"], ""])
                    else:
                        lines.extend([f"`{citation}` — NOT FOUND IN FINAL CONTEXT", ""])
            else:
                lines.extend(["No citations emitted.", ""])
            lines.extend(["### Final context", ""])
            for row in trace["final_context"]:
                lines.extend([f"**Rank {row['rank']} · `{row['id']}` · page {row['page']} · {row['source']}**", "", row["text"], ""])
            lines.extend([
                "### Student fields", "",
                "- `answer_grade_0_1_2: ____`",
                "- `citation_semantic_support: ____`",
                "- `abstention_correct: ____`",
                "- `reviewer_reason: ____`", "",
            ])
    return "\n".join(lines) + "\n", hints


def prepare_audit_artifacts(root: Path, cases: list[dict[str, Any]], chunks: list[dict[str, Any]], manifest: dict[str, Any], locked: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    benchmark_checks = automatic_benchmark_checks(root, cases, chunks, manifest)
    trace_checks = automatic_trace_checks(root, cases, chunks, locked)
    (root / "results" / "automatic_benchmark_checks.json").write_text(json.dumps(benchmark_checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (root / "results" / "automatic_trace_checks.json").write_text(json.dumps(trace_checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manual = root / "results" / "manual"
    manual.mkdir(parents=True, exist_ok=True)
    (manual / "benchmark_review_packet.md").write_text(make_benchmark_packet(cases, chunks, benchmark_checks), encoding="utf-8")
    agent_packet, hints = make_agent_packet_and_hints(root, cases, trace_checks)
    (manual / "agent_review_packet.md").write_text(agent_packet, encoding="utf-8")
    hint_fields = list(hints[0]) if hints else ["disclaimer"]
    atomic_write_csv(manual / "ai_review_hints.csv", hints, hint_fields)
    benchmark_reviews = manual / "benchmark_reviews.csv"
    if not benchmark_reviews.exists():
        atomic_write_csv(benchmark_reviews, [], BENCHMARK_REVIEW_FIELDS)
    return benchmark_checks, trace_checks


def parse_bool(value: str) -> bool:
    normalized = value.strip().casefold()
    if normalized in {"true", "t", "yes", "y", "1"}:
        return True
    if normalized in {"false", "f", "no", "n", "0"}:
        return False
    raise ValueError("Enter true/false (or yes/no).")


def parse_support(value: str, expected: int) -> list[bool]:
    if expected == 0 and not value.strip():
        return []
    try:
        loaded = json.loads(value)
        if isinstance(loaded, bool):
            loaded = [loaded]
    except json.JSONDecodeError:
        loaded = [parse_bool(item) for item in value.split(",") if item.strip()]
    if not isinstance(loaded, list) or any(type(item) is not bool for item in loaded) or len(loaded) != expected:
        raise ValueError(f"Enter exactly {expected} booleans, e.g. {[True] * expected}")
    return loaded


def agent_review_complete(row: dict[str, str]) -> bool:
    if row.get("audit_status") != "reviewed":
        return False
    answerable = row.get("answerable", "").casefold() == "true"
    citations = [value for value in row.get("citations", "").split("|") if value]
    try:
        support = parse_support(row.get("citation_semantic_support", ""), len(citations))
        if answerable:
            return row.get("answer_grade_0_1_2") in {"0", "1", "2"} and row.get("abstention_correct", "") == "" and len(support) == len(citations)
        return row.get("answer_grade_0_1_2", "") == "" and row.get("abstention_correct", "").casefold() in {"true", "false"} and len(support) == len(citations)
    except ValueError:
        return False


def merge_agent_audit_rows(existing: list[dict[str, str]], generated: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key = {(row.get("split"), row.get("method"), row.get("query_id")): row for row in existing}
    merged = []
    for base in generated:
        old = by_key.get((base["split"], base["method"], base["query_id"]), {})
        for field in ("answer_grade_0_1_2", "citation_semantic_support", "abstention_correct", "audit_status", "reviewer_notes", "reviewed_at"):
            if old.get(field, "") != "":
                base[field] = old[field]
        merged.append(base)
    return merged


def manual_metrics_for_run(traces: list[dict[str, Any]], reviews: list[dict[str, str]]) -> dict[str, Any]:
    by_id = {row["query_id"]: row for row in reviews}
    reviewed = [trace for trace in traces if trace["query_id"] in by_id and agent_review_complete(by_id[trace["query_id"]])]
    result: dict[str, Any] = {"reviewer_completion": {"n": len(reviewed), "N": len(traces)}}
    if len(reviewed) != len(traces):
        result.update({
            "status": "pending manual review",
            "grounded_answer": "pending manual review",
            "semantic_citation_validity": "pending manual review",
            "correct_abstention": "pending manual review",
            "false_abstention": "pending manual review",
        })
        return result
    grades = Counter()
    semantic_n = semantic_N = correct_n = correct_N = false_n = false_N = 0
    for trace in traces:
        review = by_id[trace["query_id"]]
        support = parse_support(review["citation_semantic_support"], len([value for value in review.get("citations", "").split("|") if value]))
        semantic_n += sum(support)
        semantic_N += len(support)
        if trace["answerable"]:
            grades[review["answer_grade_0_1_2"]] += 1
            false_n += trace["status"] == "abstain"
            false_N += 1
        else:
            correct_n += parse_bool(review["abstention_correct"])
            correct_N += 1
    total_grades = sum(grades.values())
    result.update({
        "status": "complete",
        "grounded_answer": {"0": grades["0"], "1": grades["1"], "2": grades["2"], "N": total_grades, "mean": (grades["1"] + 2 * grades["2"]) / total_grades if total_grades else None},
        "semantic_citation_validity": {"n": semantic_n, "N": semantic_N},
        "correct_abstention": {"n": correct_n, "N": correct_N},
        "false_abstention": {"n": false_n, "N": false_N},
    })
    return result


def audit_status(root: Path, cases: list[dict[str, Any]]) -> dict[str, Any]:
    benchmark_rows = read_csv(root / "results" / "manual" / "benchmark_reviews.csv")
    benchmark_reviewed = {row["query_id"] for row in benchmark_rows if row.get("decision") in {"approve", "reject"}}
    agent_rows = read_csv(root / "results" / "manual" / "agent_audit.csv")
    agent_reviewed = sum(agent_review_complete(row) for row in agent_rows)
    return {
        "benchmark": {"reviewed": len(benchmark_reviewed), "total": len(cases), "pending": len(cases) - len(benchmark_reviewed), "output": "results/manual/benchmark_reviews.csv"},
        "agent": {"reviewed": agent_reviewed, "total": len(agent_rows), "pending": len(agent_rows) - agent_reviewed, "output": "results/manual/agent_audit.csv"},
        "next_commands": [
            "python scripts/lab.py audit benchmark",
            "python scripts/lab.py audit agent",
            "python scripts/lab.py audit status",
            "python scripts/lab.py aggregate",
        ],
    }


def run_benchmark_audit(root: Path, cases: list[dict[str, Any]], input_fn: Callable[[str], str] = input, output_fn: Callable[[str], None] = print) -> None:
    path = root / "results" / "manual" / "benchmark_reviews.csv"
    rows = read_csv(path)
    reviewed = {row["query_id"] for row in rows if row.get("decision") in {"approve", "reject"}}
    for case in cases:
        if case["id"] in reviewed:
            continue
        output_fn(f"\n{case['id']} [{case['split']}] {'answerable' if case['answerable'] else 'insufficient'}\nQuestion: {case['question']}\nExpected: {case.get('gold_answer', case.get('expected_behavior'))}\nPage: {case.get('physical_page', 'N/A')}\nEvidence: {case.get('gold_evidence', case.get('corpus_check'))}")
        choice = input_fn("Decision [a]pprove/[r]eject/[s]kip/[q]uit: ").strip().casefold()
        if choice == "q":
            break
        if choice == "s" or choice == "":
            continue
        if choice not in {"a", "r"}:
            output_fn("Invalid decision; case left pending.")
            continue
        notes = input_fn("Notes: ").strip()
        rows.append({"query_id": case["id"], "decision": "approve" if choice == "a" else "reject", "notes": notes, "reviewed_at": utc_now()})
        atomic_write_csv(path, rows, BENCHMARK_REVIEW_FIELDS)


def run_agent_audit(root: Path, traces: list[dict[str, Any]], input_fn: Callable[[str], str] = input, output_fn: Callable[[str], None] = print) -> None:
    path = root / "results" / "manual" / "agent_audit.csv"
    rows = read_csv(path)
    by_key = {(row["split"], row["method"], row["query_id"]): row for row in rows}
    for trace in traces:
        key = (trace["split"], trace["retrieval_method"], trace["query_id"])
        row = by_key[key]
        if agent_review_complete(row):
            continue
        output_fn(f"\n{trace['split']}/{trace['retrieval_method']} {trace['query_id']} [{trace['status']}]\nAnswer: {trace['answer']}")
        for citation in trace.get("citations", []):
            passage = next((item for item in trace["final_context"] if item["id"] == citation), None)
            output_fn(f"Citation {citation}: {passage['text'] if passage else 'NOT IN CONTEXT'}")
        action = input_fn("Review [e]nter/[s]kip/[q]uit: ").strip().casefold()
        if action == "q":
            break
        if action != "e":
            continue
        try:
            citations = trace.get("citations", [])
            if trace["answerable"]:
                grade = input_fn("answer_grade_0_1_2: ").strip()
                if grade not in {"0", "1", "2"}:
                    raise ValueError("Grade must be 0, 1, or 2")
                abstention = ""
            else:
                grade = ""
                abstention = str(parse_bool(input_fn("abstention_correct [true/false]: ").strip())).lower()
            support = parse_support(input_fn(f"citation_semantic_support ({len(citations)} booleans as JSON): ").strip(), len(citations))
            reason = input_fn("reviewer_reason: ").strip()
        except ValueError as exc:
            output_fn(f"Invalid review: {exc}; row left pending.")
            continue
        row.update({
            "answer_grade_0_1_2": grade,
            "citation_semantic_support": json.dumps(support),
            "abstention_correct": abstention,
            "audit_status": "reviewed",
            "reviewer_notes": reason,
            "reviewed_at": utc_now(),
        })
        atomic_write_csv(path, rows, AGENT_AUDIT_FIELDS)

