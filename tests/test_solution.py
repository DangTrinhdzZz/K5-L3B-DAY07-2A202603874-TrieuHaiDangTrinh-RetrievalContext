from __future__ import annotations

import json
import sys
import tempfile
import unittest
from array import array
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentic_rag.agent import aggregate_agent
from agentic_rag.benchmark import load_benchmark, validate_benchmark
from agentic_rag.corpus import build_chunks, load_chunks, load_pages
from agentic_rag.embeddings import write_vectors
from agentic_rag.evaluation import evidence_hit
from agentic_rag.retrieval import RetrievalIndex


class Worker:
    def embed(self, texts, *, query):
        vector = [0.0] * 384
        vector[0] = 1.0
        return [vector[:] for _ in texts]


def mini_chunk(cid, text, page):
    return {"id": cid, "chunk_id": cid, "document_id": "doc", "source_id": "doc", "source": "doc.pdf", "page": page, "text": text, "metadata": {"page": page}}


class SolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d6 = ROOT.parent / "K5-L3B-DAY06-TrieuHaiDangTrinh-2A202603874-DataIngestion"

    def test_corpus_loading_stable_ids_and_idempotency(self):
        pages = load_pages(self.d6 / "data" / "normalized_pages.jsonl")
        first = build_chunks(pages)
        second = build_chunks(pages)
        self.assertEqual(len(first), 191)
        self.assertEqual([row["id"] for row in first], [row["id"] for row in second])
        self.assertTrue(all(row["source"] and row["page"] and row["metadata"]["section_id"] for row in first))

    def test_dense_bm25_rrf_mmr_schema_and_metadata(self):
        chunks = [mini_chunk("a", "orthogonality cross fitting", 1), mini_chunk("b", "hospital treatment effect", 2), mini_chunk("c", "cross fitting folds", 3)]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "vectors.f32"
            vectors = []
            for i in range(3):
                vector = [0.0] * 384
                vector[i] = 1.0
                vectors.append(vector)
            write_vectors(path, vectors)
            index = RetrievalIndex(chunks, path, Worker())
            for method in RetrievalIndex.METHODS:
                rows = index.search("cross fitting", method=method, top_k=2)
                self.assertEqual(len(rows), 2)
                self.assertEqual([row["rank"] for row in rows], [1, 2])
                self.assertTrue(all({"chunk_id", "rank", "score", "text", "source", "page", "metadata"} <= row.keys() for row in rows))
            hybrid = index.search("cross fitting", method="hybrid", top_k=2)
            self.assertIn("dense_rank", hybrid[0])
            self.assertIn("bm25_rank", hybrid[0])

    def test_benchmark_counts_disjointness_and_no_gold_in_query_contract(self):
        if not (ROOT / "benchmark" / "questions.jsonl").exists():
            self.skipTest("Run scripts/lab.py build first")
        chunks = load_chunks(ROOT / "artifacts" / "chunks.jsonl")
        rows = load_benchmark(ROOT / "benchmark" / "questions.jsonl")
        validate_benchmark(rows, chunks)
        dev = {row["id"] for row in rows if row["split"] == "dev"}
        test = {row["id"] for row in rows if row["split"] == "test"}
        self.assertFalse(dev & test)
        self.assertEqual((len(dev), len(test)), (17, 7))
        for row in rows:
            self.assertNotIn("gold_answer", {"question": row["question"]})

    def test_evidence_requires_chunk_source_page_and_quote(self):
        case = {"answerable": True, "gold_chunk_ids": ["a"], "source": "doc", "physical_page": 1, "gold_evidence": "cross fitting"}
        good = {**mini_chunk("a", "cross fitting", 1), "source_id": "doc"}
        self.assertTrue(evidence_hit(good, case))
        self.assertFalse(evidence_hit({**good, "page": 2}, case))

    def test_citation_abstention_trace_aggregation_pending_semantic_review(self):
        traces = [{"status": "answered", "events": [{"event": "search"}], "citations": ["a"], "citation_ids_in_context": True, "answerable": True, "latency_ms": 1, "usage": {"total_tokens": 3}}, {"status": "abstain", "events": [{"event": "search"}], "citations": [], "citation_ids_in_context": True, "answerable": False, "latency_ms": 1, "usage": {}}]
        result = aggregate_agent(traces)
        self.assertEqual(result["tool_use"], {"n": 2, "N": 2})
        self.assertEqual(result["grounded_answer_0_1_2"], "pending_review")
        self.assertEqual(result["behavioral_abstention_on_unanswerable"]["n"], 1)

    def test_missing_api_key_is_boolean_not_required_for_offline_components(self):
        from agentic_rag.config import load_settings
        self.assertIsInstance(load_settings().has_openai_key, bool)

    def test_vector_artifact_rejects_wrong_size(self):
        chunks = [mini_chunk("a", "x", 1)]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.f32"
            with path.open("wb") as handle:
                array("f", [1.0]).tofile(handle)
            with self.assertRaises(ValueError):
                RetrievalIndex(chunks, path, Worker())

    def test_live_trace_schema_scope_and_cost_cap(self):
        paths = [ROOT / "results/agent/dev/hybrid_traces.jsonl", ROOT / "results/agent/test/dense_traces.jsonl", ROOT / "results/agent/test/hybrid_traces.jsonl"]
        if not all(path.exists() for path in paths):
            self.skipTest("Live evaluation not run")
        traces = [[json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line] for path in paths]
        self.assertEqual([len(rows) for rows in traces], [17, 7, 7])
        flat = [row for rows in traces for row in rows]
        self.assertTrue(all(row["model"] == "gpt-6-luna" and row["status"] != "error" for row in flat))
        self.assertTrue(all(len(row["final_context"]) <= 3 for row in flat))
        self.assertTrue(all(any(event["event"] == "search" for event in row["events"]) for row in flat))
        self.assertTrue(all(all(citation in row["final_context_ids"] for citation in row["citations"]) for row in flat))
        self.assertLess(sum(row["estimated_api_cost_usd"] for row in flat), 1.0)
        payload = json.dumps(flat)
        for forbidden in ("D:\\\\Coding", "OPENAI_API_KEY", "gold_answer", "gold_evidence"):
            self.assertNotIn(forbidden, payload)

    def test_live_manual_audit_remains_pending(self):
        path = ROOT / "results/manual/agent_audit.csv"
        if not path.exists():
            self.skipTest("Agent audit not generated")
        import csv
        with path.open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 31)
        self.assertTrue(all(row["audit_status"] == "pending_review" for row in rows))
        self.assertTrue(all(not row["answer_grade_0_1_2"] and not row["citation_semantic_support"] and not row["abstention_correct"] for row in rows))


if __name__ == "__main__":
    unittest.main()

