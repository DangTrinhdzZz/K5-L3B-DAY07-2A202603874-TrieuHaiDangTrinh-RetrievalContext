from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[2]


def _path(name: str, default: Path) -> Path:
    value = os.getenv(name)
    path = Path(value) if value else default
    return path if path.is_absolute() else (ROOT / path).resolve()


@dataclass(frozen=True)
class Settings:
    root: Path
    day6_root: Path
    day6_pdf_path: Path
    normalized_pages_path: Path
    day6_chunks_path: Path | None
    day6_vector_path: Path | None
    day6_collection: str
    embedding_python: Path
    embedding_model: str
    agent_model: str
    reasoning_effort: str
    max_tool_calls: int
    max_output_tokens: int
    dense_top_k: int
    bm25_top_k: int
    final_context_k: int
    rrf_k: int
    random_seed: int
    live_cost_cap_usd: float

    @property
    def chunks_path(self) -> Path:
        return self.root / "artifacts" / "chunks.jsonl"

    @property
    def vectors_path(self) -> Path:
        return self.root / "artifacts" / "bge_vectors.f32"

    @property
    def manifest_path(self) -> Path:
        return self.root / "artifacts" / "corpus_manifest.json"

    @property
    def benchmark_path(self) -> Path:
        return self.root / "benchmark" / "questions.jsonl"

    @property
    def has_openai_key(self) -> bool:
        return bool(os.getenv("OPENAI_API_KEY", "").strip())


def load_settings() -> Settings:
    load_dotenv(ROOT / ".env", override=False)
    default_d6 = (ROOT.parent / "K5-L3B-DAY06-TrieuHaiDangTrinh-2A202603874-DataIngestion").resolve()
    day6_root = _path("DAY6_ROOT", default_d6)
    raw_chunks = os.getenv("DAY6_CHUNKS_PATH", "").strip()
    raw_vectors = os.getenv("DAY6_VECTOR_PATH", "").strip()
    return Settings(
        root=ROOT,
        day6_root=day6_root,
        day6_pdf_path=_path("DAY6_PDF_PATH", day6_root / "data" / "raw" / "An Introduction to Double Machine Learning.pdf"),
        normalized_pages_path=_path("DAY6_NORMALIZED_PAGES_PATH", day6_root / "data" / "normalized_pages.jsonl"),
        day6_chunks_path=_path("DAY6_CHUNKS_PATH", Path(raw_chunks)) if raw_chunks else None,
        day6_vector_path=_path("DAY6_VECTOR_PATH", Path(raw_vectors)) if raw_vectors else None,
        day6_collection=os.getenv("DAY6_COLLECTION", "ingestion_chunks:B"),
        embedding_python=_path("EMBEDDING_PYTHON", day6_root / "starter" / ".venv" / "Scripts" / "python.exe"),
        embedding_model=os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5"),
        agent_model=os.getenv("AGENT_MODEL", "gpt-6-luna"),
        reasoning_effort=os.getenv("OPENAI_REASONING_EFFORT", "low"),
        max_tool_calls=int(os.getenv("AGENT_MAX_TOOL_CALLS", "2")),
        max_output_tokens=int(os.getenv("AGENT_MAX_OUTPUT_TOKENS", "1200")),
        dense_top_k=int(os.getenv("DENSE_TOP_K", "10")),
        bm25_top_k=int(os.getenv("BM25_TOP_K", "10")),
        final_context_k=int(os.getenv("FINAL_CONTEXT_K", "3")),
        rrf_k=int(os.getenv("RRF_K", "60")),
        random_seed=int(os.getenv("RANDOM_SEED", "202603874")),
        live_cost_cap_usd=float(os.getenv("LIVE_COST_CAP_USD", "1.0")),
    )

