from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Page:
    document_id: str
    source: str
    page: int
    text: str
    metadata: dict[str, Any]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_pages(path: Path) -> list[Page]:
    pages: list[Page] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            item = json.loads(line)
            pages.append(Page(item["document_id"], item["source"], int(item["page"]), item["text"], item["metadata"]))
    if len(pages) != 51 or [p.page for p in pages] != list(range(1, 52)):
        raise ValueError("Expected the verified 51 physical content pages from Day 6")
    return pages


def _chunk_id(page: Page, start: int, end: int, text: str) -> str:
    version = str(page.metadata.get("version", "unknown"))
    text_hash = hashlib.sha256(text.encode()).hexdigest()
    material = f"{page.document_id}|{version}|B|{page.page}|{start}|{end}|{text_hash}"
    return hashlib.sha256(material.encode()).hexdigest()[:32]


def _chunk(page: Page, text: str, start: int, section_id: str, section_title: str) -> dict[str, Any]:
    end = start + len(text)
    text_hash = hashlib.sha256(text.encode()).hexdigest()
    metadata = {
        **page.metadata,
        "page_start": page.page,
        "page_end": page.page,
        "start_char": start,
        "end_char": end,
        "section_id": section_id,
        "section_title": section_title,
        "strategy": "B",
        "char_count": len(text),
        "token_count_estimate": (len(text.split()) * 4 + 2) // 3,
        "text_hash": text_hash,
    }
    return {
        "id": _chunk_id(page, start, end, text),
        "chunk_id": _chunk_id(page, start, end, text),
        "document_id": page.document_id,
        "source_id": page.document_id,
        "source": page.source,
        "page": page.page,
        "text": text,
        "metadata": metadata,
    }


def chunk_page(page: Page, max_size: int = 900) -> list[dict[str, Any]]:
    """Byte-for-byte compatible port of Day 6's strategy-B chunker."""
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", page.text) if part.strip()]
    units: list[tuple[str, int, str, str]] = []
    section_id = str(page.metadata.get("section_id", "front"))
    section_title = str(page.metadata.get("section_title", "Front matter"))
    cursor = 0
    heading_pattern = re.compile(r"^((?:\d+|[A-Z])(?:\.\d+)*)\.?\s+(.+)$")
    for paragraph in paragraphs:
        start = page.text.find(paragraph, cursor)
        start = cursor if start < 0 else start
        cursor = start + len(paragraph)
        if paragraph in {"Appendix", "References"}:
            section_id = paragraph.lower()
            section_title = paragraph
        else:
            heading = heading_pattern.match(paragraph)
            if heading and len(paragraph.split()) <= 14 and not paragraph.endswith((".", ",", ";", ":")):
                section_id, section_title = heading.group(1), heading.group(2).strip()
        if len(paragraph) <= max_size:
            units.append((paragraph, start, section_id, section_title))
            continue
        local = 0
        while local < len(paragraph):
            end = min(local + max_size, len(paragraph))
            if end < len(paragraph):
                sentence = max(paragraph.rfind(". ", local + max_size // 2, end), paragraph.rfind("; ", local + max_size // 2, end))
                if sentence >= 0:
                    end = sentence + 1
                else:
                    space = paragraph.rfind(" ", local + max_size // 2, end)
                    if space > local:
                        end = space
            value = paragraph[local:end].strip()
            if value:
                units.append((value, start + local, section_id, section_title))
            local = max(end, local + 1)

    chunks: list[dict[str, Any]] = []
    pending: list[tuple[str, int]] = []
    pending_section = (section_id, section_title)

    def flush() -> None:
        if not pending:
            return
        value = "\n\n".join(item[0] for item in pending)
        start = pending[0][1]
        chunks.append(_chunk(page, value, start, *pending_section))
        pending.clear()

    for value, start, sid, title in units:
        candidate = value if not pending else "\n\n".join([*(x[0] for x in pending), value])
        if pending and ((sid, title) != pending_section or len(candidate) > max_size):
            flush()
        if not pending:
            pending_section = (sid, title)
        pending.append((value, start))
    flush()
    return chunks


def build_chunks(pages: list[Page]) -> list[dict[str, Any]]:
    chunks = [chunk for page in pages for chunk in chunk_page(page)]
    if len(chunks) != 191 or len({c["id"] for c in chunks}) != 191:
        raise ValueError(f"Day 6 strategy-B compatibility failed: got {len(chunks)} chunks")
    return chunks


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows)
    path.write_text(payload, encoding="utf-8")


def load_chunks(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]
    if not rows or len(rows) != len({row["id"] for row in rows}):
        raise ValueError("Chunk artifact is empty or contains duplicate IDs")
    return rows

