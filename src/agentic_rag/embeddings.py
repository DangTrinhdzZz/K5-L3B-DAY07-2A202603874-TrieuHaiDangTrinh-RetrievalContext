from __future__ import annotations

import json
import os
import subprocess
from array import array
from pathlib import Path


class EmbeddingWorker:
    def __init__(self, python: Path, script: Path, model: str) -> None:
        if not python.exists():
            raise FileNotFoundError(f"Embedding Python not found: {python}")
        environment = os.environ.copy()
        day6_hf_cache = python.parents[2] / ".cache" / "huggingface"
        if day6_hf_cache.exists():
            environment.update({
                "HF_HOME": str(day6_hf_cache),
                "HF_HUB_OFFLINE": "1",
                "TRANSFORMERS_OFFLINE": "1",
            })
        self.process = subprocess.Popen(
            [str(python), "-u", str(script), "--stdio", "--model", model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            env=environment,
        )
        ready_line = self.process.stdout.readline() if self.process.stdout else ""
        if not ready_line:
            error = self.process.stderr.read() if self.process.stderr else "worker exited"
            raise RuntimeError(f"Embedding worker failed: {error[-2000:]}")
        ready = json.loads(ready_line)
        self.dimension = int(ready["dimension"])
        if self.dimension != 384:
            raise ValueError(f"Expected BGE dimension 384, got {self.dimension}")

    def embed(self, texts: list[str], *, query: bool) -> list[list[float]]:
        if not texts:
            return []
        assert self.process.stdin and self.process.stdout
        self.process.stdin.write(json.dumps({"texts": texts, "query": query}, ensure_ascii=False) + "\n")
        self.process.stdin.flush()
        response = json.loads(self.process.stdout.readline())
        if "error" in response:
            raise RuntimeError(response["error"])
        return response["vectors"]

    def close(self) -> None:
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()

    def __enter__(self) -> "EmbeddingWorker":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


def write_vectors(path: Path, vectors: list[list[float]], dimension: int = 384) -> None:
    if not vectors or any(len(vector) != dimension for vector in vectors):
        raise ValueError("Invalid vector matrix")
    values = array("f", (value for vector in vectors for value in vector))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        values.tofile(handle)


def load_vectors(path: Path, count: int, dimension: int = 384) -> array:
    values = array("f")
    with path.open("rb") as handle:
        try:
            values.fromfile(handle, count * dimension)
        except EOFError as exc:
            raise ValueError("Vector artifact is truncated") from exc
        if handle.read(1):
            raise ValueError("Vector artifact has trailing bytes")
    if len(values) != count * dimension:
        raise ValueError(f"Vector artifact size mismatch: {len(values)} floats")
    return values

