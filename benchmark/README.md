# Day 7 benchmark

`questions.jsonl` contains 24 unique cases: 15 answerable + 2 unanswerable dev cases and 5 answerable + 2 unanswerable test cases. The 20 answerable cases inherit Day 6's pre-retrieval verified questions and are resolved to the rebuilt Day 7 chunk IDs. Four near-topic absence cases specify a corpus-wide check procedure.

Every case has `manual_audit_status: pending_review`. Gold fields are evaluation-only and are never sent to a retriever or agent. Run `python scripts/lab.py build` to deterministically regenerate and validate the file.

