"""JSON-lines BGE worker intended for a Python 3.11 sentence-transformers env."""
from __future__ import annotations

import argparse
import json
import sys


QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


def main() -> None:
    # Windows child processes otherwise decode redirected stdin with the active
    # legacy code page, corrupting the paper's Unicode before tokenization.
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="BAAI/bge-small-en-v1.5")
    parser.add_argument("--stdio", action="store_true")
    args = parser.parse_args()
    if not args.stdio:
        raise SystemExit("Use --stdio")
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(args.model, device="cpu")
    dimension = int(model.get_sentence_embedding_dimension())
    print(json.dumps({"ready": True, "dimension": dimension}), flush=True)
    for line in sys.stdin:
        try:
            request = json.loads(line)
            texts = request["texts"]
            if request.get("query"):
                texts = [QUERY_PREFIX + value for value in texts]
            encoded = []
            for start in range(0, len(texts), 32):
                batch = texts[start:start + 32]
                if any(not isinstance(value, str) for value in batch):
                    raise TypeError(f"Non-string embedding input in batch starting at {start}")
                try:
                    vectors = model.encode(batch, batch_size=32, normalize_embeddings=True, show_progress_bar=False)
                except Exception as exc:
                    raise RuntimeError(f"embedding batch {start}:{start + len(batch)} lengths={[len(value) for value in batch]}: {exc}") from exc
                encoded.extend(vectors.tolist())
            print(json.dumps({"vectors": encoded}), flush=True)
        except Exception as exc:
            print(json.dumps({"error": f"{type(exc).__name__}: {exc}"}), flush=True)


if __name__ == "__main__":
    main()

