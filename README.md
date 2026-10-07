# learn-to-code

Mike's Python learning monorepo: FreeCodeCamp (Scientific Computing with Python),
Exercism, CodeWars, Coddy, and PY4E practice. One repo, one venv, one test command.

## Layout

| Path | What it is |
|------|-----------|
| `exercises/` | Bite-sized problems, each with a test. `codewars/`, `hackerrank/`, `leetcode/`, `misc/` |
| `courses/` | Guided coursework. `fcc/{python,js}/`, `p4e/`, `i-love-coding/` |
| `_template/` | Per-problem scaffold (copy, do not edit in place) |
| `backlog/` | Task specs |

## The loop

1. Paste the user story into the module docstring, verbatim.
2. Write the function signature only.
3. Turn each requirement into an assertion in `test_<problem>.py`.
4. Run `uv run pytest -k <name>` until green.
5. Paste back to the platform and submit.

The point: the FCC / CodeWars / Coddy browser editors cannot run your own tests, so
verify locally and treat their tab as the grader.

## Commands

    uv sync                  # create .venv, install pytest + ruff
    uv run pytest            # run everything
    uv run pytest -k name    # one problem
    uv run ruff check .      # lint

## Map

The learning plan itself lives in the personal KB:
`shakti-workspace/_AREAS/tech/coding-path.md` (the spine course + supporting
practice ordering).
