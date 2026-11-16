# Day 7 — Agentic RAG

Individual submission for **2A202603874 — Trieu Hai Dang Trinh**. The implementation connects to the verified Day 6 corpus, recreates its strategy-B chunks without modifying Day 6, compares dense/BM25/hybrid retrieval, and provides an OpenAI Responses API function-calling agent with auditable traces.

## Architecture

```text
Day 6 normalized pages (read-only)
  -> deterministic strategy-B chunks + stable IDs
  -> BGE normalized float32 exact-cosine index
  -> Dense / BM25 / Hybrid RRF / Hybrid+MMR retrieval
  -> locked Hybrid RRF
  -> Responses API agent (question + maximum top-3 passages)
  -> immutable JSONL traces
  -> automatic checks + interactive human audit + aggregate
```

Gold answer/evidence never enters retrieval or the agent. It is joined locally only after execution for mechanical metrics and the human-review packet.

## Verified data path

Day 6 stored 309/191/191 chunks for strategies A/B/C in PostgreSQL 16.16 + pgvector 0.8.7 table `ingestion_chunks`. During Day 7 inspection the database port `127.0.0.1:55433` was offline and no persistent chunk export existed. Day 7 therefore rebuilds the exact 191 strategy-B chunks from Day 6's 51-page `data/normalized_pages.jsonl`, then creates a portable normalized float32 exact-cosine index using `BAAI/bge-small-en-v1.5` (384 dimensions). Dense, BM25 and hybrid all use these same chunks and IDs.

The main CLI/tests run under the requested Python 3.14 environment. `sentence-transformers`/PyTorch are not installed there, so embedding uses the already-provisioned Day 6 Python 3.11 environment and its local Hugging Face cache in offline mode. No mock or random vectors are used.

## Setup

From this repository root in PowerShell:

```powershell
Copy-Item .env.example .env  # only if .env does not already exist
# Add OPENAI_API_KEY to .env for live agent evaluation. Never commit .env.
$py = "..\.venv\Scripts\python.exe"
& $py --version
& $py -m pip install -r requirements.txt
```

The existing `.env` is ignored. The program checks key presence as a boolean and never logs its value.

## Environment variables

| Variable | Purpose |
|---|---|
| `DAY6_ROOT`, `DAY6_PDF_PATH`, `DAY6_NORMALIZED_PAGES_PATH` | Read-only Day 6 inputs |
| `EMBEDDING_PYTHON`, `EMBEDDING_MODEL` | Compatible local BGE worker/model |
| `AGENT_MODEL`, `OPENAI_REASONING_EFFORT` | Responses API model/reasoning |
| `AGENT_MAX_TOOL_CALLS`, `AGENT_MAX_OUTPUT_TOKENS` | Bounded agent execution |
| `DENSE_TOP_K`, `BM25_TOP_K`, `FINAL_CONTEXT_K`, `RRF_K` | Retrieval candidates/context/fusion |
| `RANDOM_SEED` | Reproducibility |
| `LIVE_COST_CAP_USD` | Hard cumulative live-run guardrail |

## Build/reuse corpus and run the locked workflow

Run these commands in order:

```powershell
$py = "..\.venv\Scripts\python.exe"

# Read-only Day 6 discovery
& $py scripts\lab.py inspect-day6

# Idempotent chunks, BGE index, manifest and 24-case benchmark
& $py scripts\lab.py build

# Dev retrieval: 15 answerable cases, consistent top 3
& $py scripts\lab.py retrieval --split dev --methods dense bm25 hybrid hybrid_mmr

# Lock by the predeclared selection policy before test
& $py scripts\lab.py lock

# Independent test retrieval: dense baseline + locked method
& $py scripts\lab.py test

# Live dev agent after permission to send query/retrieved text to OpenAI
& $py scripts\lab.py agent --split dev --methods hybrid

# Live test agent: baseline and locked method
& $py scripts\lab.py test --with-agent

# Structural metrics and pending manual-audit sheet
& $py scripts\lab.py aggregate

# Regenerate automatic checks and human-review packets without API calls
& $py scripts\lab.py audit prepare

# Tests and final checks
& $py -m unittest discover -s tests -v
& $py scripts\lab.py preflight
git diff --check
git status --short
```

Live agent execution uses `gpt-6-luna`, Responses API function calling, a strict `search_evidence` schema, maximum two tool calls, retrieval-only context, bounded retries, and citation-ID enforcement. If the preferred model is absent, the code chooses the first visible low-cost function-calling fallback from `gpt-5-nano`, `gpt-4.1-nano`, and `gpt-4o-mini`; it never fabricates a model response.

The locked configuration is `configs/locked_config.json`: Hybrid RRF, dense/BM25 candidate top 10, final context top 3 and RRF k=60. Do not rerun test with a newly tuned configuration.

Command map:

| Stage | Command |
|---|---|
| Build/reuse corpus | `& $py scripts\lab.py build` |
| Run retrieval dev | `& $py scripts\lab.py retrieval --split dev --methods dense bm25 hybrid hybrid_mmr` |
| Lock config | `& $py scripts\lab.py lock` |
| Run independent test retrieval | `& $py scripts\lab.py test` |
| Run live dev agent | `& $py scripts\lab.py agent --split dev --methods hybrid` |
| Run live test baseline/chosen | `& $py scripts\lab.py test --with-agent` |
| Aggregate | `& $py scripts\lab.py aggregate` |
| Preflight | `& $py scripts\lab.py preflight` |

## Manual audit

Review packets can be read before entering labels:

- `results/manual/benchmark_review_packet.md` — all 24 benchmark cases.
- `results/manual/agent_review_packet.md` — all 31 executions with cited/final context.
- `results/manual/ai_review_hints.csv` — explicitly non-official mechanical hints.

Interactive audit is resumable and writes atomically after each completed row:

```powershell
$py = "..\.venv\Scripts\python.exe"
& $py scripts\lab.py audit benchmark
& $py scripts\lab.py audit agent
& $py scripts\lab.py audit status
& $py scripts\lab.py aggregate
```

`aggregate` preserves existing reviews. Before completion, official grounded-answer, semantic-citation and abstention metrics say `pending manual review`; after all rows validate, they are calculated per run and for Dense versus Hybrid test.

## Expected artifact layout

- Corpus/index manifest: `artifacts/corpus_manifest.json`
- Same-corpus chunks/index: `artifacts/chunks.jsonl`, `artifacts/bge_vectors.f32`
- Benchmark: `benchmark/questions.jsonl` (15+2 dev, 5+2 test)
- Dev/test retrieval traces and summaries: `results/retrieval/`
- Locked configuration: `configs/locked_config.json`
- Live `gpt-6-luna` traces and aggregate metrics: `results/agent/`
- Manual audit checklists: `results/manual/`
- Automatic benchmark/trace checks: `results/automatic_benchmark_checks.json`, `results/automatic_trace_checks.json`
- Individual report: `report/individual/2A202603874_TrieuHaiDangTrinh.md`
- Rubric mapping: `report/rubric_coverage.md`
- Student handoff: `MANUAL_REVIEW_HANDOFF.md`

Gold answers/evidence are used only by local evaluation after retrieval. Retrieval and agent inputs receive only the original question; agent context contains at most three retrieved passages with chunk ID, source, physical page and text. The completed live run used 40,370 tokens and an estimated USD 0.005659. Semantic answer/citation/abstention labels remain `pending_review` until the student checks them.

## Cost, privacy and known limitations

- Live cost is conservatively estimated from API token usage without cache discounts; the run stayed below the USD 1 guardrail.
- Only question, system/tool schema and top-3 passages were sent. Gold, labels, corpus/PDF, local paths, key and secrets were excluded.
- Limitations: one English preprint, test N=5 answerable cases, exact-quote metrics, flattened PDF layout, one embedding model, and one live timing run.
- Citation syntax only proves that an ID is in context. It does not establish semantic support; human review remains required.
