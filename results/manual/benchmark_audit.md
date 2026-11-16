# Benchmark manual audit checklist

Status: **pending_review**. This file is a checklist for the student; no item below has been represented as manually confirmed.

For each answerable case, open the declared physical PDF page, confirm the quote and answer, then verify that each `gold_chunk_ids` entry contains the full evidence. For each unanswerable case, perform the stated corpus-wide term search and inspect plausible matches rather than treating a top-k miss as proof of absence. Confirm that dev/test questions are substantively distinct.

## Dev

- [ ] q01 — pending_review
- [ ] q02 — pending_review
- [ ] q03 — pending_review
- [ ] q04 — pending_review
- [ ] q05 — pending_review
- [ ] q06 — pending_review
- [ ] q07 — pending_review
- [ ] q08 — pending_review
- [ ] q09 — pending_review
- [ ] q10 — pending_review
- [ ] q11 — pending_review
- [ ] q12 — pending_review
- [ ] q13 — pending_review
- [ ] q14 — pending_review
- [ ] q15 — pending_review
- [ ] q21 (unanswerable) — pending_review
- [ ] q22 (unanswerable) — pending_review

## Test

- [ ] q16 — pending_review
- [ ] q17 — pending_review
- [ ] q18 — pending_review
- [ ] q19 — pending_review
- [ ] q20 — pending_review
- [ ] q23 (unanswerable) — pending_review
- [ ] q24 (unanswerable) — pending_review

Record corrections in a benchmark changelog and regenerate hashes before rerunning. Never edit test based on retrieval/model output without declaring that it is no longer an independent holdout.

