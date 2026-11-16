# Dev error analysis

All figures below come from `results/retrieval/dev/*_traces.jsonl`. Semantic manual review remains `pending_review`.

## q01 — defining components of DML

- Expected evidence: physical page 9, “Neyman orthogonality and cross-fitting.”
- Dense top 3: pages 1, 4 and 16; it retrieved high-level DML and ingredient passages but missed the exact page-9 definition. Hit@1=0, Hit@3=0.
- Hypothesis: the broad semantic query overweights title/overview passages; exact terms and the “Section 2” cue benefit lexical matching.
- Change tested: RRF of dense top 10 and BM25 top 10.
- After: Hybrid places the exact page-9 chunk at rank 3, so Hit@3 changes 0→1. The remaining limitation is rank 3 rather than rank 1.
- MMR result: the diversity penalty removes that rank-3 evidence, regressing Hit@3 1→0.

## q11 — HRS panel size and waves

- Expected evidence: physical page 29, 656 households over waves 7–11.
- Dense: the exact evidence is rank 3 (Hit@1=0, Hit@3=1); ranks 1–2 are broader hospitalization passages.
- Hypothesis: exact numbers and acronym-heavy facts are better separated by BM25 than by a dense vector alone.
- Change tested: Hybrid RRF.
- After: exact page-29 evidence moves to rank 1, changing Hit@1 0→1 while retaining Hit@3=1.
- MMR result: unrelated page-30/page-34 diversity replaces the exact chunk; Hit@1 and Hit@3 both become 0. This is why MMR was not selected.

Across dev, Hybrid repairs all four dense Hit@3 misses (q01, q06, q08, q10), while MMR regresses five Hybrid hits (q01, q06, q08, q10, q11). The result supports RRF for this small corpus but not the tested MMR setting.

