from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .corpus import write_jsonl


UNANSWERABLE = [
    {
        "id": "q21",
        "split": "dev",
        "question": "What numerical effect does the paper report for DML on Vietnam's GDP growth in 2025?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "The paper discusses econometric DML methods, not Vietnam GDP estimates.",
        "corpus_check": "Search all normalized pages for Vietnam, GDP, and growth; inspect any matches in context.",
    },
    {
        "id": "q22",
        "split": "dev",
        "question": "Which GPU model and training duration were used to train the DML method described in the paper?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "DML is an inference framework here, not a trained foundation model with a GPU training run.",
        "corpus_check": "Search all normalized pages for GPU, graphics processor, and training duration.",
    },
    {
        "id": "q23",
        "split": "test",
        "question": "What acceptance rate at NeurIPS 2025 does the paper report for this work?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "The source is an economics preprint and contains no NeurIPS acceptance-rate claim.",
        "corpus_check": "Search all normalized pages for NeurIPS, acceptance, and conference.",
    },
    {
        "id": "q24",
        "split": "test",
        "question": "Which exact Python package version do the authors require to reproduce every experiment?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "The paper mentions a companion website but does not mandate one exact package version for all experiments.",
        "corpus_check": "Search all normalized pages for Python, package, version, requirements, and reproduce.",
    },
]


def prepare_benchmark(day6_questions: Path, chunks: list[dict[str, Any]], output: Path) -> list[dict[str, Any]]:
    by_page: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for chunk in chunks:
        by_page.setdefault((chunk["source_id"], chunk["page"]), []).append(chunk)
    rows: list[dict[str, Any]] = []
    with day6_questions.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            source = json.loads(line)
            evidence = source["evidence_quote"]
            candidates = [chunk for chunk in by_page.get((source["gold_source_id"], int(source["gold_page"])), []) if evidence in chunk["text"]]
            if not candidates:
                raise ValueError(f"Evidence for {source['id']} does not resolve to a Day 7 chunk")
            rows.append({
                "id": source["id"],
                "query_id": source["id"],
                "split": source["split"],
                "question": source["question"],
                "answerable": True,
                "gold_answer": source["expected_answer"],
                "source": source["gold_source_id"],
                "physical_page": int(source["gold_page"]),
                "gold_evidence": evidence,
                "gold_chunk_ids": [chunk["id"] for chunk in candidates],
                "scoring_criteria": "Answer must preserve every material condition in gold_answer and cite supporting context.",
                "question_type": source.get("question_type"),
                "manual_audit_status": "pending_review",
            })
    rows.extend({**row, "query_id": row["id"], "manual_audit_status": "pending_review"} for row in UNANSWERABLE)
    validate_benchmark(rows, chunks)
    write_jsonl(output, rows)
    return rows


def load_benchmark(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def validate_benchmark(rows: list[dict[str, Any]], chunks: list[dict[str, Any]]) -> None:
    ids = [row.get("id") for row in rows]
    if len(rows) != 24 or len(ids) != len(set(ids)):
        raise ValueError("Benchmark must contain exactly 24 unique cases")
    expected = {("dev", True): 15, ("dev", False): 2, ("test", True): 5, ("test", False): 2}
    actual = {(split, answerable): sum(row["split"] == split and row["answerable"] is answerable for row in rows) for split, answerable in expected}
    if actual != expected:
        raise ValueError(f"Invalid split counts: {actual}")
    chunk_ids = {chunk["id"] for chunk in chunks}
    for row in rows:
        if row.get("manual_audit_status") != "pending_review" or not row.get("question", "").strip():
            raise ValueError(f"{row.get('id')}: invalid audit/question")
        if row["answerable"]:
            required = ("gold_answer", "source", "physical_page", "gold_evidence", "gold_chunk_ids", "scoring_criteria")
            if any(not row.get(key) for key in required) or not set(row["gold_chunk_ids"]) <= chunk_ids:
                raise ValueError(f"{row['id']}: invalid gold fields")
            if not any(chunk["id"] in row["gold_chunk_ids"] and row["gold_evidence"] in chunk["text"] for chunk in chunks):
                raise ValueError(f"{row['id']}: evidence does not resolve")
        elif row.get("expected_behavior") != "search_and_abstain" or not row.get("corpus_check"):
            raise ValueError(f"{row['id']}: invalid abstention case")

