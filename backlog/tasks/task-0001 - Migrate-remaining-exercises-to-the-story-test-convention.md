---
id: TASK-0001
title: Migrate remaining exercises to the story + test convention
status: To Do
assignee: []
created_date: '2026-10-07'
updated_date: '2026-10-07'
labels:
  - coding
dependencies: []
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Convert the exercise files that predate the restructure to the standard shape: user
story in the module docstring (verbatim), one function, no top-level demo prints, and
a sibling `test_<problem>.py` with one assertion per requirement. Start with the
CodeWars katas (`exercises/codewars/`), then `hackerrank/`, `leetcode/`, `misc/`.
`odd_int.py` is the worked example.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Every file in `exercises/` has a matching `test_*.py`
- [ ] #2 No exercise file has top-level demo code or `print()` side effects
- [ ] #3 `uv run pytest` passes with no collection errors
<!-- AC:END -->
