# Manual review handoff

Run from the Day 7 repository root in PowerShell. The audit commands resume automatically and do not overwrite completed reviews.

```powershell
$py = "..\.venv\Scripts\python.exe"

# 1. Audit all 24 benchmark cases.
& $py scripts\lab.py audit benchmark

# 2. Audit all 31 agent executions.
& $py scripts\lab.py audit agent

# 3. Confirm completion counts.
& $py scripts\lab.py audit status

# 4. Recompute official manual metrics after reviews are complete.
& $py scripts\lab.py aggregate

# 5. Run all tests.
& $py -m unittest discover -s tests -v

# 6. Run final preflight.
& $py scripts\lab.py preflight

# 7. Read the updated report and aggregate.
Get-Content -Raw report\individual\2A202603874_TrieuHaiDangTrinh.md
Get-Content -Raw results\agent\aggregate.json

# 8. Inspect whitespace/diff/status.
git diff --check
git status --short
```

Before submission, confirm that:

- `audit status` reports benchmark 24/24 and agent 31/31 reviewed.
- `results/manual/agent_audit.csv` contains your reasons and no unintended edits.
- `results/agent/aggregate.json` reports manual evaluation as `complete`.
- The report is updated with reviewed semantic metrics; do not copy mechanical hints as official labels.
- `.env` remains ignored and no secret appears in Git output.
- Do not commit or push until every check above is complete and understood.
