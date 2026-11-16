from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentic_rag.audit import (
    AGENT_AUDIT_FIELDS,
    BENCHMARK_REVIEW_FIELDS,
    agent_review_complete,
    atomic_write_csv,
    manual_metrics_for_run,
    merge_agent_audit_rows,
    parse_bool,
    parse_support,
    read_csv,
    run_agent_audit,
    run_benchmark_audit,
)


def audit_row(query_id: str, answerable: bool, *, reviewed: bool = False) -> dict[str, str]:
    return {
        "split": "dev",
        "method": "hybrid",
        "query_id": query_id,
        "answerable": str(answerable),
        "status": "answered" if answerable else "abstain",
        "answer": "answer",
        "citations": "c1" if answerable else "",
        "answer_grade_0_1_2": "2" if reviewed and answerable else "",
        "citation_semantic_support": "[true]" if reviewed and answerable else ("[]" if reviewed else ""),
        "abstention_correct": "true" if reviewed and not answerable else "",
        "audit_status": "reviewed" if reviewed else "pending_review",
        "reviewer_notes": "kept" if reviewed else "",
        "reviewed_at": "2026-01-01T00:00:00+00:00" if reviewed else "",
    }


class AuditTests(unittest.TestCase):
    def test_parser_and_validation(self):
        self.assertTrue(parse_bool("yes"))
        self.assertFalse(parse_bool("0"))
        self.assertEqual(parse_support("[true, false]", 2), [True, False])
        self.assertEqual(parse_support("true,false", 2), [True, False])
        with self.assertRaises(ValueError):
            parse_bool("maybe")
        with self.assertRaises(ValueError):
            parse_support("[true]", 2)
        self.assertTrue(agent_review_complete(audit_row("q1", True, reviewed=True)))
        self.assertTrue(agent_review_complete(audit_row("q2", False, reviewed=True)))
        self.assertFalse(agent_review_complete(audit_row("q3", True)))

    def test_merge_preserves_existing_review(self):
        existing = [audit_row("q1", True, reviewed=True)]
        generated = [{**audit_row("q1", True), "answer": "new trace answer"}]
        merged = merge_agent_audit_rows(existing, generated)
        self.assertEqual(merged[0]["answer"], "new trace answer")
        self.assertEqual(merged[0]["answer_grade_0_1_2"], "2")
        self.assertEqual(merged[0]["reviewer_notes"], "kept")
        self.assertEqual(merged[0]["audit_status"], "reviewed")

    def test_benchmark_audit_resumes_and_updates_atomically(self):
        cases = [
            {"id": "q1", "split": "dev", "answerable": True, "question": "one", "gold_answer": "a", "physical_page": 1, "gold_evidence": "e"},
            {"id": "q2", "split": "test", "answerable": False, "question": "two", "expected_behavior": "search_and_abstain", "corpus_check": "search"},
        ]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / "results/manual/benchmark_reviews.csv"
            atomic_write_csv(path, [{"query_id": "q1", "decision": "approve", "notes": "old", "reviewed_at": "then"}], BENCHMARK_REVIEW_FIELDS)
            answers = iter(["a", "new note"])
            run_benchmark_audit(root, cases, input_fn=lambda _: next(answers), output_fn=lambda _: None)
            rows = read_csv(path)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["notes"], "old")
            self.assertEqual(rows[1]["query_id"], "q2")
            self.assertEqual(rows[1]["decision"], "approve")

    def test_agent_audit_resumes_and_does_not_overwrite_reviewed_row(self):
        traces = [
            {"split": "dev", "retrieval_method": "hybrid", "query_id": "q1", "answerable": True, "status": "answered", "answer": "a", "citations": ["c1"], "final_context": [{"id": "c1", "text": "passage"}]},
            {"split": "dev", "retrieval_method": "hybrid", "query_id": "q2", "answerable": False, "status": "abstain", "answer": "insufficient", "citations": [], "final_context": []},
        ]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / "results/manual/agent_audit.csv"
            atomic_write_csv(path, [audit_row("q1", True, reviewed=True), audit_row("q2", False)], AGENT_AUDIT_FIELDS)
            answers = iter(["e", "true", "", "reviewed q2"])
            run_agent_audit(root, traces, input_fn=lambda _: next(answers), output_fn=lambda _: None)
            rows = read_csv(path)
            self.assertEqual(rows[0]["reviewer_notes"], "kept")
            self.assertEqual(rows[1]["audit_status"], "reviewed")
            self.assertEqual(rows[1]["abstention_correct"], "true")
            self.assertEqual(rows[1]["citation_semantic_support"], "[]")

    def test_manual_aggregate_pending_and_complete(self):
        traces = [
            {"query_id": "q1", "answerable": True, "status": "answered"},
            {"query_id": "q2", "answerable": False, "status": "abstain"},
        ]
        pending = manual_metrics_for_run(traces, [audit_row("q1", True), audit_row("q2", False)])
        self.assertEqual(pending["status"], "pending manual review")
        self.assertEqual(pending["grounded_answer"], "pending manual review")
        complete = manual_metrics_for_run(traces, [audit_row("q1", True, reviewed=True), audit_row("q2", False, reviewed=True)])
        self.assertEqual(complete["status"], "complete")
        self.assertEqual(complete["grounded_answer"], {"0": 0, "1": 0, "2": 1, "N": 1, "mean": 2.0})
        self.assertEqual(complete["semantic_citation_validity"], {"n": 1, "N": 1})
        self.assertEqual(complete["correct_abstention"], {"n": 1, "N": 1})

    def test_generated_packets_and_automatic_checks(self):
        benchmark_packet = (ROOT / "results/manual/benchmark_review_packet.md").read_text(encoding="utf-8")
        agent_packet = (ROOT / "results/manual/agent_review_packet.md").read_text(encoding="utf-8")
        benchmark_checks = json.loads((ROOT / "results/automatic_benchmark_checks.json").read_text(encoding="utf-8"))
        trace_checks = json.loads((ROOT / "results/automatic_trace_checks.json").read_text(encoding="utf-8"))
        self.assertEqual(benchmark_packet.count("Student checklist:"), 24)
        self.assertEqual(agent_packet.count("### Student fields"), 31)
        self.assertEqual(benchmark_checks["automatic_check"], "passed")
        self.assertEqual(trace_checks["automatic_check"], "passed")
        with (ROOT / "results/manual/ai_review_hints.csv").open(encoding="utf-8", newline="") as handle:
            hints = list(csv.DictReader(handle))
        self.assertEqual(len(hints), 31)
        self.assertTrue(all(row["disclaimer"] == "AI/mechanical hints, not official labels" for row in hints))


if __name__ == "__main__":
    unittest.main()
