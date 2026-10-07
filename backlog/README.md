# `backlog/` — Task Specs

Task tracker storage for the **Backlog** CLI, run from `/Developer/learn-to-code`.
Task specs are files here; the CLI reads/writes them. `filesystem_only: true`, so
there is no DB, just these files.

## Layout

| Path | What it's for |
|------|--------------|
| `config.yml` | Backlog CLI config (statuses, task prefix `TASK`, date format) |
| `tasks/` | Active task specs — `TASK-NNNN`, frontmatter + description body |
| `drafts/` | Draft task specs (not yet tracked) |
| `completed/` | Finished tasks (moved here) |
| `archive/` | Archived drafts / tasks |
| `.locks/` | CLI lock files (transient, gitignored) |

## Conventions

- One task with subtasks in the body, not many separately-tracked tasks.
- Tasks reviewed on Sundays (weekly review).
- Run the CLI from `/Developer/learn-to-code`.
