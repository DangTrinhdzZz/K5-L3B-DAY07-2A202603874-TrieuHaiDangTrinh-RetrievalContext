from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter
from typing import Any

from .embeddings import EmbeddingWorker, load_vectors


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKC", text).casefold())


def _result(chunk: dict[str, Any], *, rank: int, score: float, method: str, **extra: Any) -> dict[str, Any]:
    return {
        "id": chunk["id"],
        "chunk_id": chunk["id"],
        "rank": rank,
        "score": float(score),
        "text": chunk["text"],
        "source_id": chunk["source_id"],
        "source": chunk["source"],
        "page": chunk["page"],
        "metadata": chunk["metadata"],
        "method": method,
        **extra,
    }


class RetrievalIndex:
    METHODS = ("dense", "bm25", "hybrid", "hybrid_mmr")

    def __init__(self, chunks: list[dict[str, Any]], vectors_path: Any, worker: EmbeddingWorker, *, rrf_k: int = 60) -> None:
        self.chunks = chunks
        self.by_id = {chunk["id"]: chunk for chunk in chunks}
        self.worker = worker
        self.dimension = 384
        self.vectors = load_vectors(vectors_path, len(chunks), self.dimension)
        self.rrf_k = rrf_k
        self._query_cache: dict[str, list[float]] = {}
        self.term_counts = [Counter(tokenize(chunk["text"])) for chunk in chunks]
        self.doc_lengths = [sum(row.values()) for row in self.term_counts]
        self.avgdl = sum(self.doc_lengths) / len(self.doc_lengths)
        self.df = Counter(term for row in self.term_counts for term in row)

    def _dense_with_vector(self, query_vector: list[float], top_k: int) -> list[dict[str, Any]]:
        scored: list[tuple[float, int]] = []
        for index in range(len(self.chunks)):
            start = index * self.dimension
            score = sum(query_vector[j] * self.vectors[start + j] for j in range(self.dimension))
            scored.append((score, index))
        scored.sort(key=lambda item: (-item[0], self.chunks[item[1]]["id"]))
        return [_result(self.chunks[i], rank=rank, score=score, method="dense") for rank, (score, i) in enumerate(scored[:top_k], 1)]

    def dense(self, query: str, top_k: int) -> list[dict[str, Any]]:
        vector = self._query_vector(query)
        return self._dense_with_vector(vector, top_k)

    def _query_vector(self, query: str) -> list[float]:
        if query not in self._query_cache:
            self._query_cache[query] = self.worker.embed([query], query=True)[0]
        return self._query_cache[query]

    def bm25(self, query: str, top_k: int, k1: float = 1.5, b: float = 0.75) -> list[dict[str, Any]]:
        terms = tokenize(query)
        scores: list[tuple[float, int]] = []
        n = len(self.chunks)
        for index, counts in enumerate(self.term_counts):
            score = 0.0
            for term in terms:
                freq = counts.get(term, 0)
                if not freq:
                    continue
                idf = math.log(1 + (n - self.df[term] + 0.5) / (self.df[term] + 0.5))
                denominator = freq + k1 * (1 - b + b * self.doc_lengths[index] / self.avgdl)
                score += idf * freq * (k1 + 1) / denominator
            scores.append((score, index))
        scores.sort(key=lambda item: (-item[0], self.chunks[item[1]]["id"]))
        return [_result(self.chunks[i], rank=rank, score=score, method="bm25") for rank, (score, i) in enumerate(scores[:top_k], 1)]

    def _hybrid_candidates(self, query: str, candidate_k: int) -> tuple[list[dict[str, Any]], list[float]]:
        query_vector = self._query_vector(query)
        dense = self._dense_with_vector(query_vector, candidate_k)
        bm25 = self.bm25(query, candidate_k)
        dense_rank = {row["id"]: row["rank"] for row in dense}
        bm25_rank = {row["id"]: row["rank"] for row in bm25}
        ids = set(dense_rank) | set(bm25_rank)
        fused = []
        for chunk_id in ids:
            score = (1 / (self.rrf_k + dense_rank[chunk_id]) if chunk_id in dense_rank else 0) + (1 / (self.rrf_k + bm25_rank[chunk_id]) if chunk_id in bm25_rank else 0)
            fused.append((score, chunk_id))
        fused.sort(key=lambda item: (-item[0], item[1]))
        rows = [_result(self.by_id[cid], rank=rank, score=score, method="hybrid", rrf_score=score, dense_rank=dense_rank.get(cid), bm25_rank=bm25_rank.get(cid)) for rank, (score, cid) in enumerate(fused, 1)]
        return rows, query_vector

    def hybrid(self, query: str, top_k: int, candidate_k: int = 10) -> list[dict[str, Any]]:
        rows, _ = self._hybrid_candidates(query, max(candidate_k, top_k))
        return [{**row, "rank": rank} for rank, row in enumerate(rows[:top_k], 1)]

    def hybrid_mmr(self, query: str, top_k: int, candidate_k: int = 10, mmr_lambda: float = 0.75) -> list[dict[str, Any]]:
        candidates, query_vector = self._hybrid_candidates(query, max(candidate_k, top_k))
        candidates = candidates[:candidate_k]
        positions = {chunk["id"]: i for i, chunk in enumerate(self.chunks)}
        selected: list[dict[str, Any]] = []
        remaining = candidates.copy()
        while remaining and len(selected) < top_k:
            best: tuple[float, str, dict[str, Any]] | None = None
            for row in remaining:
                pos = positions[row["id"]]
                start = pos * self.dimension
                relevance = sum(query_vector[j] * self.vectors[start + j] for j in range(self.dimension))
                redundancy = 0.0
                for chosen in selected:
                    other = positions[chosen["id"]] * self.dimension
                    redundancy = max(redundancy, sum(self.vectors[start + j] * self.vectors[other + j] for j in range(self.dimension)))
                mmr = mmr_lambda * relevance - (1 - mmr_lambda) * redundancy
                candidate = (mmr, row["id"], row)
                if best is None or candidate[0] > best[0] or (candidate[0] == best[0] and candidate[1] < best[1]):
                    best = candidate
            assert best is not None
            chosen = {**best[2], "score": best[0], "mmr_score": best[0], "method": "hybrid_mmr", "rank": len(selected) + 1}
            selected.append(chosen)
            remaining = [row for row in remaining if row["id"] != chosen["id"]]
        return selected

    def search(self, query: str, *, method: str, top_k: int) -> list[dict[str, Any]]:
        if method not in self.METHODS:
            raise ValueError(f"Unknown retrieval method: {method}")
        if not query.strip() or not 1 <= top_k <= 20:
            raise ValueError("query/top_k invalid")
        return getattr(self, method)(query, top_k)

