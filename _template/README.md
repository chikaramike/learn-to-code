# _template

Copy both files into the problem's folder, rename them to the problem (snake_case),
then fill in the story and the assertions.

    cp _template/problem.py      exercises/codewars/my_kata.py
    cp _template/test_problem.py exercises/codewars/test_my_kata.py

Rules:

- The user story goes in the module docstring, **verbatim** from the platform.
- One function per file. No top-level demo code, no `print()` at the bottom.
- Every requirement in the story becomes an assertion in the test file.
- Run it: `uv run pytest exercises/codewars/test_my_kata.py -q`

This folder is excluded from `pytest` (see `norecursedirs` in `pyproject.toml`).
