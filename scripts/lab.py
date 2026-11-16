from __future__ import annotations

import argparse
import hashlib
import json
import re
import socket
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentic_rag.agent import aggregate_agent, run_agent_split
from agentic_rag.audit import (
    AGENT_AUDIT_FIELDS,
    RUN_SPECS,
    atomic_write_csv,
    audit_status,
    manual_metrics_for_run,
    merge_agent_audit_rows,
    prepare_audit_artifacts,
    read_csv,
    read_jsonl,
    run_agent_audit,
    run_benchmark_audit,
)
from agentic_rag.benchmark import load_benchmark, prepare_benchmark, validate_benchmark
from agentic_rag.config import load_settings
from agentic_rag.corpus import build_chunks, load_chunks, load_pages, sha256_file, write_jsonl
from agentic_rag.embeddings import EmbeddingWorker, write_vectors
from agentic_rag.evaluation import choose_and_lock, run_retrieval
from agentic_rag.retrieval import RetrievalIndex


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def inspect_day6() -> dict[str, object]:
    settings = load_settings()
    d6 = settings.day6_root
    db_live = False
    try:
        with socket.create_connection(("127.0.0.1", 55433), timeout=1):
            db_live = True
    except OSError:
        pass
    result = {
        "day6_root": str(d6),
        "normalized_pages": str(settings.normalized_pages_path),
        "normalized_pages_exists": settings.normalized_pages_path.exists(),
        "pdf_exists": settings.day6_pdf_path.exists(),
        "persistent_chunk_file_found": False,
        "day6_backend": "PostgreSQL 16.16 + pgvector 0.8.7",
        "day6_table_and_strategy": settings.day6_collection,
        "day6_database_port_live": db_live,
        "day6_reported_counts": {"A": 309, "B": 191, "C": 191},
        "embedding_model": settings.embedding_model,
        "dimension": 384,
        "normalize_embeddings": True,
        "query_prefix": "Represent this sentence for searching relevant passages: ",
        "decision": "reuse read-only pgvector" if db_live else "rebuild a portable Day 7 exact-cosine index from Day 6 normalized pages and identical strategy-B chunking",
    }
    dump(settings.root / "artifacts" / "day6_inspection.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def build() -> dict[str, object]:
    settings = load_settings()
    pages = load_pages(settings.normalized_pages_path)
    chunks = build_chunks(pages)
    write_jsonl(settings.chunks_path, chunks)
    prepare_benchmark(settings.day6_root / "benchmark" / "questions.jsonl", chunks, settings.benchmark_path)
    chunk_hash = sha256_file(settings.chunks_path)
    existing = {}
    if settings.manifest_path.exists():
        existing = json.loads(settings.manifest_path.read_text(encoding="utf-8"))
    reused_vectors = bool(
        settings.vectors_path.exists()
        and existing.get("chunks_sha256") == chunk_hash
        and existing.get("embedding_model") == settings.embedding_model
        and existing.get("vector_dimension") == 384
    )
    if not reused_vectors:
        with EmbeddingWorker(settings.embedding_python, settings.root / "scripts" / "embedding_worker.py", settings.embedding_model) as worker:
            vectors = worker.embed([chunk["text"] for chunk in chunks], query=False)
            write_vectors(settings.vectors_path, vectors, worker.dimension)
    manifest = {
        "source_day6_root": str(settings.day6_root),
        "source_input": str(settings.normalized_pages_path),
        "source_pdf": str(settings.day6_pdf_path),
        "source_normalized_sha256": sha256_file(settings.normalized_pages_path),
        "physical_content_pages": len(pages),
        "chunk_count": len(chunks),
        "chunk_version": "day6_strategy_B_section_paragraph_aware_900_v1",
        "chunks_path": str(settings.chunks_path.relative_to(settings.root)),
        "chunks_sha256": chunk_hash,
        "embedding_model": settings.embedding_model,
        "embedding_revision": "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a",
        "vector_dimension": 384,
        "normalize_embeddings": True,
        "query_prefix": "Represent this sentence for searching relevant passages: ",
        "day6_backend": "PostgreSQL 16.16 + pgvector 0.8.7 (offline during Day 7 inspection)",
        "day6_collection": settings.day6_collection,
        "day7_backend": "portable float32 exact-cosine index",
        "index_path": str(settings.vectors_path.relative_to(settings.root)),
        "index_sha256": sha256_file(settings.vectors_path),
        "dense_and_bm25_same_corpus": True,
        "rebuild_reason": "Day 6 stored chunks/vectors only in pgvector; port 55433 was unavailable and no chunk export existed.",
        "embedding_cost_usd": 0,
    }
    dump(settings.manifest_path, manifest)
    print(json.dumps({**manifest, "vectors_reused": reused_vectors}, ensure_ascii=False, indent=2))
    return manifest


def open_index():
    settings = load_settings()
    chunks = load_chunks(settings.chunks_path)
    worker = EmbeddingWorker(settings.embedding_python, settings.root / "scripts" / "embedding_worker.py", settings.embedding_model)
    return settings, worker, RetrievalIndex(chunks, settings.vectors_path, worker, rrf_k=settings.rrf_k)


def retrieval(split: str, methods: list[str]) -> None:
    settings, worker, index = open_index()
    try:
        cases = load_benchmark(settings.benchmark_path)
        summaries = [run_retrieval(index, cases, method=method, split=split, output_dir=settings.root / "results" / "retrieval" / split, top_k=settings.final_context_k) for method in methods]
        print(json.dumps(summaries, indent=2))
    finally:
        worker.close()


def lock() -> None:
    settings = load_settings()
    locked = choose_and_lock(settings.root / "results" / "retrieval" / "dev", settings.root / "configs" / "locked_config.json", settings, sha256_file(settings.manifest_path))
    print(json.dumps(locked, indent=2))


def agent_run(split: str, methods: list[str]) -> None:
    settings, worker, index = open_index()
    try:
        cases = load_benchmark(settings.benchmark_path)
        summaries = []
        existing_cost = 0.0
        for trace_path in (settings.root / "results" / "agent").rglob("*_traces.jsonl"):
            for line in trace_path.read_text(encoding="utf-8").splitlines():
                if line:
                    existing_cost += json.loads(line).get("estimated_api_cost_usd", 0.0)
        for method in methods:
            remaining = settings.live_cost_cap_usd - existing_cost
            if remaining <= 0:
                raise RuntimeError(f"Live evaluation cost cap reached: {existing_cost:.6f} USD")
            output = settings.root / "results" / "agent" / split / f"{method}_traces.jsonl"
            summary = run_agent_split(index, cases, split=split, method=method, output=output, settings=settings, cost_budget_usd=remaining)
            summaries.append({"method": method, **summary})
            existing_cost += summary["estimated_cost_usd"]
        dump(settings.root / "results" / "agent" / split / "run_summary.json", summaries)
        print(json.dumps(summaries, indent=2))
    finally:
        worker.close()


def run_test(include_agent: bool) -> None:
    settings = load_settings()
    locked = json.loads((settings.root / "configs" / "locked_config.json").read_text(encoding="utf-8"))
    methods = list(dict.fromkeys(["dense", locked["selected_method"]]))
    retrieval("test", methods)
    if include_agent:
        agent_run("test", methods)


def update_report_manual_section(root: Path, outputs: dict[str, object], status: dict[str, object]) -> None:
    report = root / "report" / "individual" / "2A202603874_TrieuHaiDangTrinh.md"
    text = report.read_text(encoding="utf-8")
    benchmark = status["benchmark"]
    agent = status["agent"]
    lines = [
        "<!-- BEGIN GENERATED MANUAL EVALUATION -->",
        "### Manual semantic evaluation status (generated by `scripts/lab.py aggregate`)",
        "",
        f"- Benchmark review: {benchmark['reviewed']}/{benchmark['total']} reviewed; {benchmark['pending']} pending.",
        f"- Agent review: {agent['reviewed']}/{agent['total']} reviewed; {agent['pending']} pending.",
    ]
    complete = agent["pending"] == 0
    if not complete:
        lines.extend([
            "- Official grounded-answer, semantic-citation and abstention metrics: `pending manual review`.",
            "- Empty review cells are not interpreted as zero.",
        ])
    else:
        lines.extend([
            "", "| Run | Grounded 0/1/2; mean /2 | Semantic citations | Correct abstention | False abstention |",
            "|---|---|---|---|---|",
        ])
        for run in RUN_SPECS:
            manual = outputs[run]["manual_evaluation"]
            grounded = manual["grounded_answer"]
            semantic = manual["semantic_citation_validity"]
            abstention = manual["correct_abstention"]
            false = manual["false_abstention"]
            lines.append(f"| {run} | {grounded['0']}/{grounded['1']}/{grounded['2']}; {grounded['mean']:.3f} | {semantic['n']}/{semantic['N']} | {abstention['n']}/{abstention['N']} | {false['n']}/{false['N']} |")
    lines.append("<!-- END GENERATED MANUAL EVALUATION -->")
    replacement = "\n".join(lines)
    updated, count = re.subn(r"<!-- BEGIN GENERATED MANUAL EVALUATION -->.*?<!-- END GENERATED MANUAL EVALUATION -->", replacement, text, flags=re.S)
    if count != 1:
        raise RuntimeError("Report manual-evaluation markers missing or duplicated")
    audit_label = "complete" if benchmark["pending"] == 0 and agent["pending"] == 0 else "pending_review"
    updated = re.sub(r"\*\*Manual audit:\*\* `[^`]+`", f"**Manual audit:** `{audit_label}`", updated, count=1)
    report.write_text(updated, encoding="utf-8")


def aggregate() -> None:
    settings = load_settings()
    outputs: dict[str, object] = {}
    generated_rows = []
    traces_by_run: dict[str, list[dict[str, object]]] = {}
    for run, (_, _, _, relative) in RUN_SPECS.items():
        traces = read_jsonl(settings.root / relative)
        traces_by_run[run] = traces
        outputs[run] = aggregate_agent(traces)
        for trace in traces:
            generated_rows.append({
                "split": trace["split"],
                "method": trace["retrieval_method"],
                "query_id": trace["query_id"],
                "answerable": trace["answerable"],
                "status": trace["status"],
                "answer": trace["answer"],
                "citations": "|".join(trace["citations"]),
                "answer_grade_0_1_2": "",
                "citation_semantic_support": "",
                "abstention_correct": "",
                "audit_status": "pending_review",
                "reviewer_notes": "",
                "reviewed_at": "",
            })
    audit = settings.root / "results" / "manual" / "agent_audit.csv"
    merged = merge_agent_audit_rows(read_csv(audit), generated_rows)
    atomic_write_csv(audit, merged, AGENT_AUDIT_FIELDS)
    for run, traces in traces_by_run.items():
        split, method = run.split("/")
        reviews = [row for row in merged if row["split"] == split and row["method"] == method]
        outputs[run]["manual_evaluation"] = manual_metrics_for_run(traces, reviews)
    status = audit_status(settings.root, load_benchmark(settings.benchmark_path))
    outputs["manual_review"] = status
    dense_manual = outputs["test/dense"]["manual_evaluation"]
    hybrid_manual = outputs["test/hybrid"]["manual_evaluation"]
    outputs["test_manual_comparison"] = {
        "status": "complete" if dense_manual["status"] == hybrid_manual["status"] == "complete" else "pending manual review",
        "dense": dense_manual,
        "hybrid": hybrid_manual,
    }
    update_report_manual_section(settings.root, outputs, status)
    dump(settings.root / "results" / "agent" / "aggregate.json", outputs)
    report_metrics = {
        "retrieval": {
            f"{split}/{method}": json.loads((settings.root / "results" / "retrieval" / split / f"{method}_summary.json").read_text(encoding="utf-8"))
            for split, methods in (("dev", ("dense", "bm25", "hybrid", "hybrid_mmr")), ("test", ("dense", "hybrid")))
            for method in methods
        },
        "live_agent": {run: outputs[run] for run in RUN_SPECS},
        "manual_review": status,
        "test_manual_comparison": outputs["test_manual_comparison"],
    }
    dump(settings.root / "results" / "report_metrics.json", report_metrics)
    print(json.dumps(outputs, indent=2))


def audit_command(action: str) -> None:
    settings = load_settings()
    cases = load_benchmark(settings.benchmark_path)
    chunks = load_chunks(settings.chunks_path)
    manifest = json.loads(settings.manifest_path.read_text(encoding="utf-8"))
    locked = json.loads((settings.root / "configs" / "locked_config.json").read_text(encoding="utf-8"))
    if action in {"prepare", "benchmark", "agent"}:
        benchmark_checks, trace_checks = prepare_audit_artifacts(settings.root, cases, chunks, manifest, locked)
        if benchmark_checks["automatic_check"] != "passed" or trace_checks["automatic_check"] != "passed":
            raise RuntimeError("Automatic audit checks failed; inspect results/automatic_*_checks.json")
    if action == "benchmark":
        run_benchmark_audit(settings.root, cases)
    elif action == "agent":
        traces = [trace for _, (_, _, _, relative) in RUN_SPECS.items() for trace in read_jsonl(settings.root / relative)]
        run_agent_audit(settings.root, traces)
    elif action == "status":
        print(json.dumps(audit_status(settings.root, cases), ensure_ascii=False, indent=2))
    elif action == "prepare":
        print(json.dumps({"automatic_benchmark_checks": benchmark_checks["automatic_check"], "automatic_trace_checks": trace_checks["automatic_check"]}, indent=2))


def preflight() -> None:
    settings = load_settings()
    checks: dict[str, object] = {}
    chunks = load_chunks(settings.chunks_path)
    cases = load_benchmark(settings.benchmark_path)
    validate_benchmark(cases, chunks)
    manifest = json.loads(settings.manifest_path.read_text(encoding="utf-8"))
    locked = json.loads((settings.root / "configs" / "locked_config.json").read_text(encoding="utf-8"))
    benchmark_checks, trace_checks = prepare_audit_artifacts(settings.root, cases, chunks, manifest, locked)
    checks["pages"] = len(load_pages(settings.normalized_pages_path)) == 51
    checks["chunks"] = len(chunks) == 191
    checks["stable_unique_ids"] = len({row["id"] for row in chunks}) == 191
    checks["benchmark"] = len(cases) == 24
    checks["index_bytes"] = settings.vectors_path.stat().st_size == 191 * 384 * 4
    checks["automatic_benchmark_checks"] = benchmark_checks["automatic_check"] == "passed"
    checks["automatic_trace_checks"] = trace_checks["automatic_check"] == "passed"
    checks["audit_packets_exist"] = all((settings.root / "results" / "manual" / name).exists() for name in ("benchmark_review_packet.md", "agent_review_packet.md", "ai_review_hints.csv", "agent_audit.csv"))
    report_text = (settings.root / "report" / "individual" / "2A202603874_TrieuHaiDangTrinh.md").read_text(encoding="utf-8")
    report_metrics = json.loads((settings.root / "results" / "report_metrics.json").read_text(encoding="utf-8"))
    live_status = json.loads((settings.root / "results" / "agent" / "live_run_status.json").read_text(encoding="utf-8"))
    report_consistency = {
        "live_counts": live_status["requested_cases"] == live_status["successful_cases"] == 31 and live_status["failed_cases"] == 0,
        "live_tokens": (live_status["input_tokens"], live_status["output_tokens"], live_status["total_tokens"]) == (36315, 4055, 40370),
        "live_cost": abs(live_status["estimated_cost_usd"] - 0.005659) < 1e-12,
        "manual_pending_counts": report_metrics["manual_review"]["benchmark"]["pending"] == 24 and report_metrics["manual_review"]["agent"]["pending"] == 31,
        "retrieval_test_metrics": report_metrics["retrieval"]["test/dense"]["evidence_hit_at_3"]["n"] == 2 and report_metrics["retrieval"]["test/hybrid"]["evidence_hit_at_3"]["n"] == 3,
        "report_key_facts_present": all(value in report_text for value in ("51 content pages", "191 chunks", "31/31", "29/29", "40.370", "$0,005659", "66,151 ms", "24,901 ms", "30/30 passed", f"{report_metrics['manual_review']['benchmark']['reviewed']}/24 reviewed", f"{report_metrics['manual_review']['agent']['reviewed']}/31 reviewed")),
    }
    dump(settings.root / "results" / "report_consistency_checks.json", {"automatic_check": "passed" if all(report_consistency.values()) else "failed", "checks": report_consistency})
    checks["report_consistency"] = all(report_consistency.values())
    trace_paths = [
        settings.root / "results" / "agent" / "dev" / "hybrid_traces.jsonl",
        settings.root / "results" / "agent" / "test" / "dense_traces.jsonl",
        settings.root / "results" / "agent" / "test" / "hybrid_traces.jsonl",
    ]
    live_traces = [json.loads(line) for path in trace_paths if path.exists() for line in path.read_text(encoding="utf-8").splitlines() if line]
    checks["live_trace_counts"] = [sum(1 for _ in path.read_text(encoding="utf-8").splitlines() if _) for path in trace_paths] == [17, 7, 7]
    checks["live_model"] = bool(live_traces) and all(row.get("model") == "gpt-6-luna" for row in live_traces)
    checks["live_tool_use"] = all(any(event.get("event") == "search" for event in row.get("events", [])) for row in live_traces)
    checks["disclosure_top3"] = all(len(row.get("final_context", [])) <= 3 for row in live_traces)
    checks["trace_citations_in_context"] = all(all(citation in set(row.get("final_context_ids", [])) for citation in row.get("citations", [])) for row in live_traces)
    checks["live_cost_under_cap"] = sum(row.get("estimated_api_cost_usd", 0.0) for row in live_traces) < settings.live_cost_cap_usd
    serialized_traces = json.dumps(live_traces, ensure_ascii=False)
    checks["no_local_path_or_secret_in_trace"] = "D:\\Coding" not in serialized_traces and "OPENAI_API_KEY" not in serialized_traces and "gold_answer" not in serialized_traces and "gold_evidence" not in serialized_traces
    checks["env_ignored"] = subprocess.run(["git", "-c", f"safe.directory={settings.root.as_posix()}", "-C", str(settings.root), "check-ignore", ".env"], capture_output=True).returncode == 0
    rules_hash = hashlib.sha256((settings.root / "RULES.md").read_bytes()).hexdigest().upper()
    checks["user_rules_change_preserved"] = rules_hash == "E91B9A48FE462F76E4011B33EBEA7D4A9EC3A29B3321BA8032BA8850FDA97851"
    secret_hits = []
    for path in settings.root.rglob("*"):
        if not path.is_file() or any(part in {".git", ".env", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() in {".pdf", ".png", ".jpg", ".f32", ".pyc"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "sk-" in text and any(len(token) >= 24 for token in text.replace("\n", " ").split() if token.startswith("sk-")):
            secret_hits.append(str(path.relative_to(settings.root)))
    checks["no_secret_pattern"] = not secret_hits
    checks["secret_hit_files"] = secret_hits
    checks["openai_api_key_present"] = settings.has_openai_key
    checks["manual_audit_status"] = "pending_review"
    checks["passed"] = all(value is True for key, value in checks.items() if key not in {"openai_api_key_present", "manual_audit_status", "secret_hit_files"})
    dump(settings.root / "results" / "preflight.json", checks)
    print(json.dumps(checks, indent=2))
    if not checks["passed"]:
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Day 7 Agentic RAG workflow")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("inspect-day6")
    sub.add_parser("build")
    p_retrieval = sub.add_parser("retrieval")
    p_retrieval.add_argument("--split", choices=("dev", "test"), required=True)
    p_retrieval.add_argument("--methods", nargs="+", choices=RetrievalIndex.METHODS, required=True)
    sub.add_parser("lock")
    p_agent = sub.add_parser("agent")
    p_agent.add_argument("--split", choices=("dev", "test"), required=True)
    p_agent.add_argument("--methods", nargs="+", choices=RetrievalIndex.METHODS, required=True)
    p_test = sub.add_parser("test")
    p_test.add_argument("--with-agent", action="store_true")
    sub.add_parser("aggregate")
    p_audit = sub.add_parser("audit")
    p_audit.add_argument("action", choices=("prepare", "benchmark", "agent", "status"))
    sub.add_parser("preflight")
    args = parser.parse_args()
    if args.command == "inspect-day6": inspect_day6()
    elif args.command == "build": build()
    elif args.command == "retrieval": retrieval(args.split, args.methods)
    elif args.command == "lock": lock()
    elif args.command == "agent": agent_run(args.split, args.methods)
    elif args.command == "test": run_test(args.with_agent)
    elif args.command == "aggregate": aggregate()
    elif args.command == "audit": audit_command(args.action)
    elif args.command == "preflight": preflight()


if __name__ == "__main__":
    main()

