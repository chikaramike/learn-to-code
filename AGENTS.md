# AGENTS.md — learn-to-code

Python learning monorepo: FreeCodeCamp (Scientific Computing with Python), Exercism,
CodeWars, Coddy, PY4E practice. A practice workspace, not a product: solutions plus
the tests that prove them.

## Orientation (read first)
- `README.md` — layout, the problem loop, commands.
- `exercises/` and `courses/` — the work itself.

## Task management
- `backlog/` — task specs (`config.yml`, `tasks/`, `drafts/`, `completed/`, `archive/`).
  Mike writes tasks with acceptance criteria; agents pick up `backlog/tasks/` only.

## Conventions
- Matches the `/Developer` shared rules: JST dates, never commit secrets, no
  cross-repo moves without asking.
- **Problem shape**: one function per file, no top-level demo code (no stray
  `print()` at the bottom). The user story goes in the module docstring verbatim;
  assertions go in a sibling `test_<problem>.py`. Copy `_template/` to start one.
- Split by language only where both exist (`courses/fcc/{python,js}/`); otherwise
  the platform folder implies the language.
- Structural decisions get one `DECISIONS.md` entry. Routine changes get none.

## Verification
- No build step. Before claiming done: `uv run pytest` passes with no collection
  errors, every new exercise has a matching `test_*.py`, and no files outside the
  task's scope were touched. State what you ran.
