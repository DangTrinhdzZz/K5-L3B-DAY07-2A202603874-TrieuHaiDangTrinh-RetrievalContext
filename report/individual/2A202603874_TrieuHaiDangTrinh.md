# Báo cáo Day 7 — Agentic RAG

**Học viên:** Trieu Hai Dang Trinh · **MSSV:** 2A202603874 · **Lớp:** L3B
**Ngày chạy offline:** 2026-11-16 · **Manual audit:** `pending_review`

## 1. Dữ liệu và benchmark

Nguồn là preprint *An Introduction to Double/Debiased Machine Learning*, arXiv:2504.08324v2, được arXiv liên kết với giấy phép CC BY-SA 4.0. PDF có 60 physical pages; Day 6 giữ pages 1–51 có main text/technical appendix và loại references-only pages 52–60, tức 51 content pages. Day 7 chỉ đọc PDF và `data/normalized_pages.jsonl` của Day 6, không sửa repo Day 6.

Day 6 dùng PostgreSQL 16.16 + pgvector 0.8.7, bảng `ingestion_chunks`, strategy B/C có 191 chunk. Lúc kiểm tra Day 7, port `127.0.0.1:55433` không hoạt động và Day 6 không có file export chunk/vector. Vì vậy Day 7 tái tạo đúng strategy-B section/paragraph-aware, page-local, max 900 chars từ normalized pages. Thống kê tái tạo khớp Day 6: 191 chunks, min/mean/median/max = 35/671,984/779/899 chars, tổng 128.349 chars. Stable ID là SHA-256 của document/version/strategy/page/boundary/text, rút gọn 32 ký tự.

- Embedding thật: `BAAI/bge-small-en-v1.5`, revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, 384 chiều, normalized vectors.
- Query prefix: `Represent this sentence for searching relevant passages: `.
- Day 7 vector backend: portable float32 exact-cosine index ở `artifacts/bge_vectors.f32`; corpus ở `artifacts/chunks.jsonl`.
- Main CLI/tests: Python 3.14.6. Embedding worker: Day 6 Python 3.11.9 + cache local/offline vì Python 3.14 hiện tại không có `sentence-transformers`/PyTorch.
- Local embedding/retrieval service cost: USD 0.

Benchmark `benchmark/questions.jsonl` có 24 câu không trùng ID/nội dung: dev 15 answerable + 2 insufficient-evidence; test 5 answerable + 2 insufficient-evidence. Hai split rời nhau. 20 câu answerable kế thừa benchmark Day 6 đã xác minh trước retrieval, sau đó resolve sang Day 7 chunk IDs. Bốn câu thiếu evidence có thủ tục search toàn corpus. Gold answer/evidence chỉ dùng khi tính metric sau retrieval; retriever/agent chỉ nhận `question` gốc. Automatic benchmark validation kiểm schema/count/split/duplicate/source/page/chunk/evidence/hash và đạt `passed`; không phát hiện obvious cross-split duplicate candidate. Nhãn bắt đầu ở trạng thái `pending_review`; số review hiện hành được aggregate cập nhật trong generated manual-evaluation section. Packet đầy đủ ở `results/manual/benchmark_review_packet.md`.

## 2. Retrieval và thí nghiệm dev

Ba phương pháp bắt buộc dùng cùng 191 chunks/IDs:

1. **Dense:** normalized BGE query → exact cosine.
2. **BM25:** lexical BM25 (`k1=1.5`, `b=0.75`), không model bổ sung.
3. **Hybrid:** Reciprocal Rank Fusion của dense top 10 và BM25 top 10, `RRF k=60`; không cộng raw scores.

Hai cấu hình cải thiện được thử:

- **Improvement 1 — Hybrid RRF:** giả thuyết lexical evidence/number/term có thể bù dense distractors.
- **Improvement 2 — Hybrid RRF + MMR:** dùng cùng BGE vectors, `lambda=0.75`, giả thuyết giảm redundancy. Kết quả thực tế giảm điểm nên không chọn.

Top 3 và context đều có chunk ID, rank, score, source, physical page, text và metadata. Candidate top 10 chỉ dùng nội bộ.

| Cấu hình | Phương pháp | Split | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Mean latency | Cost |
|---|---|---|---:|---:|---:|---:|---:|
| Dense baseline | BGE exact cosine | dev | 7/15 (46,7%) | 11/15 (73,3%) | 11/15 (73,3%) | 57,192 ms | $0 |
| BM25 | lexical | dev | 8/15 (53,3%) | 15/15 (100%) | 15/15 (100%) | 1,405 ms | $0 |
| Improvement 1 | Dense + BM25 RRF | dev | 10/15 (66,7%) | 15/15 (100%) | 15/15 (100%) | 22,341 ms | $0 |
| Improvement 2 | RRF + BGE MMR | dev | 7/15 (46,7%) | 10/15 (66,7%) | 10/15 (66,7%) | 28,449 ms | $0 |

Policy được ghi trước test trong `configs/selection_policy.json`: ưu tiên dev Evidence Hit@3, rồi Hit@1, latency, sau đó deterministic name tie-break. `configs/locked_config.json` khóa **Hybrid**, candidate 10, final context 3, RRF k=60 và ghi `test_metrics_seen_before_lock=false`.

## 3. Phân tích hai lỗi dev

**q01:** Dense top 3 lấy overview pages 1/4 và ingredient passage page 16 nhưng bỏ exact definition page 9 (Hit@3=0). Hybrid đưa exact chunk page 9 vào rank 3 (Hit@3 0→1) nhờ lexical section/term signals. MMR loại chunk đó để tăng diversity, làm Hit@3 1→0. Hạn chế còn lại: exact evidence chỉ rank 3.

**q11:** Dense đưa exact “656 households, waves 7–11” page 29 ở rank 3 (Hit@1=0). Hybrid đưa nó lên rank 1 (Hit@1 0→1). MMR chọn các passage page 29/30/34 đa dạng hơn nhưng mất exact fact, làm Hit@3 1→0. Chi tiết top result nằm trong `results/dev_error_analysis.md`.

Trên toàn dev, Hybrid sửa cả bốn dense Hit@3 misses q01/q06/q08/q10. MMR làm mất năm Hybrid hits q01/q06/q08/q10/q11. Điều này bác bỏ giả thuyết MMR ở cấu hình đã thử.

## 4. Test độc lập sau khi khóa

Không chỉnh config theo test. Dense baseline và locked Hybrid chạy trên cùng 5 answerable test cases:

| Cấu hình | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Mean latency | Errors | Cost |
|---|---:|---:|---:|---:|---:|---:|
| Dense baseline | 1/5 (20%) | 2/5 (40%) | 2/5 (40%) | 66,151 ms | 0 | $0 |
| Locked Hybrid | 3/5 (60%) | 3/5 (60%) | 3/5 (60%) | 24,901 ms | 0 | $0 |

Test chỉ có 5 answerable queries nên kết quả mang tính mô tả, không chứng minh Hybrid tốt hơn tổng quát.

## 5. Agent và đánh giá

Implementation ở `src/agentic_rag/agent.py` dùng OpenAI Responses API, `gpt-6-luna`, strict function tool `search_evidence`, reasoning effort `low`, tối đa 2 tool calls và max output theo `.env`. Prompt bắt buộc gọi retrieval, coi document text là data, chỉ trả lời từ context, cite `[chunk_id | page N]`, và abstain khi thiếu evidence. Code ép method/top-k theo experiment config, không nhận gold, retry hữu hạn cho rate limit/timeout/connection/API error, kiểm citation ID thuộc context, và ghi model/parameters/tool calls/results/context IDs/answer/citations/latency/token usage/error.

API model listing xác nhận tài khoản thấy `gpt-6-luna`. Sau khi người dùng cho phép rõ phạm vi dữ liệu, live evaluation chạy đủ 17 dev Hybrid cases và hai nhánh 7-case test (Dense, locked Hybrid). Mỗi request chỉ gửi question, system/tool schema và tối đa top-3 passages gồm chunk ID/source/page/text; không gửi gold, expected abstention, audit label, local path, secret hay toàn corpus. Cả 31/31 cases thành công, không retry vượt giới hạn và không có API error.

| Cấu hình / split | Tool use | Số lượt gọi | Context evidence | Citation syntax | Câu answered có citation | Abstention thô | Từ chối nhầm thô |
|---|---|---|---|---|---|---|---|
| Hybrid / dev | 17/17 | 1 call: 17 | 14/15 (93,3%) | 18/18 | 15/15 | 2/2 | 0/15 |
| Dense / test | 7/7 | 1 call: 7 | 2/5 (40%) | 6/6 | 5/5 | 2/2 | 0/5 |
| Hybrid / test | 7/7 | 1 call: 7 | 3/5 (60%) | 5/5 | 5/5 | 2/2 | 0/5 |

Tổng tool use là 31/31 với phân bố đúng một call cho cả 31 executions. Tổng citation syntax là 29/29. Raw abstention là 6/6 executions của insufficient cases và raw false-abstention là 0/25 answerable executions; đây chưa phải nhãn semantic correctness.

Token/cost/latency thật theo Responses API usage và [pricing chính thức](https://developers.openai.com/api/docs/pricing) của `gpt-6-luna` $0,10/M input + $0,50/M output, tính bảo thủ không trừ cache:

| Run | Input | Output | Total | Mean latency | Estimated cost |
|---|---:|---:|---:|---:|---:|
| Dev Hybrid | 19.814 | 2.155 | 21.969 | 4.027 ms | $0,0030589 |
| Test Dense | 8.081 | 1.011 | 9.092 | 3.932 ms | $0,0013136 |
| Test Hybrid | 8.420 | 889 | 9.309 | 3.809 ms | $0,0012865 |
| **Tổng** | **36.315** | **4.055** | **40.370** | **3.956 ms weighted mean** | **$0,005659** |

Chi phí bằng 0,57% cap $1. Context Evidence Rate dùng gold cục bộ sau live run; gold không được gửi API. Các tỷ lệ abstention ở bảng trên chỉ là hành vi thô theo status.

<!-- BEGIN GENERATED MANUAL EVALUATION -->
### Manual semantic evaluation status (generated by `scripts/lab.py aggregate`)

- Benchmark review: 0/24 reviewed; 24 pending.
- Agent review: 0/31 reviewed; 31 pending.
- Official grounded-answer, semantic-citation and abstention metrics: `pending manual review`.
- Empty review cells are not interpreted as zero.
<!-- END GENERATED MANUAL EVALUATION -->

## 6. Tái lập, traces và kiểm thử

Lệnh đầy đủ ở root `README.md`. Lệnh chính:

```powershell
$py = "..\.venv\Scripts\python.exe"
& $py scripts\lab.py inspect-day6
& $py scripts\lab.py build
& $py scripts\lab.py retrieval --split dev --methods dense bm25 hybrid hybrid_mmr
& $py scripts\lab.py lock
& $py scripts\lab.py test
& $py scripts\lab.py audit prepare
& $py scripts\lab.py audit status
& $py scripts\lab.py aggregate
& $py -m unittest discover -s tests -v
& $py scripts\lab.py preflight
```

Kết quả unit tests hiện tại: **30/30 passed**. Tests bao phủ load corpus, stable IDs/idempotency, dense schema, BM25, RRF/MMR, metadata/source/page, benchmark count/split/disjointness, gold isolation contract, citation/abstention aggregation, vector corruption, missing API key boolean, live trace schema/data scope/cost cap, parser/validation audit, resume, atomic non-destructive update, pending/completed manual aggregation và starter error propagation.

Automatic trace validation kiểm đúng 31 execution, query/split/method/model, đúng một tool call, top-3 disclosure, citation-in-context, corpus metadata, không gold/secret/local path, nonnegative token/latency/cost, schema, duplicate và locked-config chronology; kết quả `passed`. Trạng thái bàn giao hiện tại là benchmark 0/24 reviewed và agent 0/31 reviewed. `aggregate` giữ official semantic metrics ở `pending manual review`, không diễn giải ô trống là điểm 0.

Artifact paths:

- Manifest/index/chunks: `artifacts/`
- Retrieval traces/metrics thật: `results/retrieval/dev/`, `results/retrieval/test/`
- Locked config: `configs/locked_config.json`
- Live agent traces và aggregate: `results/agent/`
- Automatic checks: `results/automatic_benchmark_checks.json`, `results/automatic_trace_checks.json`
- Report-number source: `results/report_metrics.json` (regenerated by `scripts/lab.py aggregate`)
- Manual benchmark packet: `results/manual/benchmark_review_packet.md`
- Manual agent packet/hints: `results/manual/agent_review_packet.md`, `results/manual/ai_review_hints.csv`
- Manual review outputs: `results/manual/benchmark_reviews.csv`, `results/manual/agent_audit.csv`
- Handoff commands: `MANUAL_REVIEW_HANDOFF.md`
- Rubric coverage: `report/rubric_coverage.md`

## 7. Kết luận và giới hạn

Hybrid RRF được chọn trung thực từ dev và cải thiện test strict Hit@3 từ 2/5 lên 3/5 so với dense. BM25 rất mạnh trên benchmark có exact terminology; MMR diversity gây hại ở top-3 nhỏ. Giới hạn gồm một English preprint, một embedding model, 20 answerable cases, test N=5, exact-quote metric nhạy với chunk boundaries/PDF spacing, flat text làm mất layout table/formula, latency chỉ một live run và portable exact search không kiểm chứng pgvector runtime trong Day 7. Trạng thái semantic audit hiện hành nằm trong generated manual-evaluation section.

Không thực hiện advanced 15-point challenge, reranker, query-rewrite model hay LLM judge. Không sửa Day 6, không dùng example corpus làm corpus chính, không commit `.env`, và không tạo kết quả giả.

