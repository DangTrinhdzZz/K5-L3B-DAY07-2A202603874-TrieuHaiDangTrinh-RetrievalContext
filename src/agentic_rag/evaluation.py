from __future__ import annotations

import json
import statistics
import time
from pathlib import Path
from typing import Any

from .corpus import write_jsonl
from .retrieval import RetrievalIndex


def evidence_hit(result: dict[str, Any], case: dict[str, Any]) -> bool:
    return bool(case["answerable"] and result["id"] in case["gold_chunk_ids"] and result["source_id"] == case["source"] and result["page"] == case["physical_page"] and case["gold_evidence"] in result["text"])


def run_retrieval(index: RetrievalIndex, cases: list[dict[str, Any]], *, method: str, split: str, output_dir: Path, top_k: int = 3) -> dict[str, Any]:
    answerable = [case for case in cases if case["split"] == split and case["answerable"]]
    traces: list[dict[str, Any]] = []
    for case in answerable:
        started = time.perf_counter()
        error = None
        results: list[dict[str, Any]] = []
        try:
            results = index.search(case["question"], method=method, top_k=top_k)
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
        latency = (time.perf_counter() - started) * 1000
        marked = [{**result, "evidence_hit": evidence_hit(result, case)} for result in results]
        traces.append({
            "query_id": case["id"],
            "split": split,
            "question": case["question"],
            "method": method,
            "top_k": top_k,
            "results": marked,
            "context_ids": [row["id"] for row in marked],
            "latency_ms": latency,
            "hit_at_1": bool(marked and marked[0]["evidence_hit"]),
            "evidence_hit_at_3": any(row["evidence_hit"] for row in marked[:3]),
            "context_evidence": any(row["evidence_hit"] for row in marked),
            "error": error,
        })
    n = len(traces)
    summary = {
        "method": method,
        "split": split,
        "answerable_queries": n,
        "hit_at_1": {"n": sum(row["hit_at_1"] for row in traces), "N": n},
        "evidence_hit_at_3": {"n": sum(row["evidence_hit_at_3"] for row in traces), "N": n},
        "context_evidence_rate": {"n": sum(row["context_evidence"] for row in traces), "N": n},
        "mean_latency_ms": statistics.mean(row["latency_ms"] for row in traces) if traces else None,
        "errors": sum(bool(row["error"]) for row in traces),
        "embedding_cost_usd": 0,
    }
    for key in ("hit_at_1", "evidence_hit_at_3", "context_evidence_rate"):
        summary[key]["rate"] = summary[key]["n"] / summary[key]["N"] if summary[key]["N"] else None
    output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_dir / f"{method}_traces.jsonl", traces)
    (output_dir / f"{method}_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


def choose_and_lock(dev_dir: Path, output: Path, settings: Any, manifest_hash: str) -> dict[str, Any]:
    methods = ("dense", "bm25", "hybrid", "hybrid_mmr")
    summaries = [json.loads((dev_dir / f"{method}_summary.json").read_text(encoding="utf-8")) for method in methods]
    ranked = sorted(summaries, key=lambda row: (-row["evidence_hit_at_3"]["rate"], -row["hit_at_1"]["rate"], row["mean_latency_ms"], row["method"]))
    selected = ranked[0]["method"]
    locked = {
        "locked": True,
        "selection_policy": ["highest dev Evidence Hit@3", "then highest dev Hit@1", "then lower mean retrieval latency", "then method name for deterministic tie-break"],
        "selected_method": selected,
        "baseline_method": "dense",
        "candidate_top_k": max(settings.dense_top_k, settings.bm25_top_k),
        "final_context_k": settings.final_context_k,
        "rrf_k": settings.rrf_k,
        "mmr_lambda": 0.75 if selected == "hybrid_mmr" else None,
        "embedding_model": settings.embedding_model,
        "corpus_manifest_sha256": manifest_hash,
        "dev_summaries": {row["method"]: row for row in summaries},
        "test_metrics_seen_before_lock": False,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(locked, indent=2) + "\n", encoding="utf-8")
    return locked

