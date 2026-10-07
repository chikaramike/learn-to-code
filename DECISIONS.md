# Decisions

Newest first. One entry per real structural/architecture decision: date, decision,
rationale. Routine changes get no entry.

## 2026-10-07 — Repo restructured to `exercises/` + `courses/` with a local pytest harness

Dropped the `01_problems/` / `02_courses/` numeric split and the stray
`python-practice/` bucket: the three overlapped (fcc problems lived under courses,
drills duplicated problems, and the numbering carried no meaning). Now `exercises/`
holds bite-sized problems (each with a test) and `courses/` holds guided, multi-file
work. Added `pyproject.toml` (uv + pytest + ruff) and `_template/`, so each problem
is a runnable module with assertions. Rationale: the FCC / CodeWars / Coddy browser
editors cannot run your own tests, so the local loop (story in the docstring,
assertions in `test_*.py`, `uv run pytest`) replaces guessing inside their editor.
History preserved with `git mv`.

## 2026-10-07 — Adopted the workspace agent-context standard

Added `AGENTS.md`, `backlog/`, `DECISIONS.md`, `CHANGELOG.md` per
`/Developer/AGENTS.md`. Rationale: every repo Mike owns carries the same agent
context, so any agent tool can orient inside the repo without a workspace-level file.
