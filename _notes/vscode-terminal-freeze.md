# VS Code terminal freezing (z4h + Powerlevel10k + tmux)

Date: 2026-10-26 (JST)

## Symptom
The integrated terminal in VS Code locks up and accepts no typing, usually after
`cd` into a directory or after a few basic commands.

## Setup found
- Shell: `/bin/zsh` with **zsh4humans (z4h)** and **Powerlevel10k** (`~/.zshrc`).
- Prompt: `os_icon dir vcs` on the left. The `vcs` segment runs git status on every prompt.
- `~/.zshrc` sets `zstyle ':z4h:' start-tmux command tmux -u new -A -D -t z4h`,
  so every shell starts inside tmux.
- `zstyle ':z4h:' term-shell-integration 'yes'` overlaps with VS Code's own shell integration.
- VS Code settings: Nerd Font (MesloLGM), `customGlyphs` on, `gpuAcceleration` off,
  `python.terminal.executeInFileDir` on (auto `cd` before running Python files).
- Ghostty config is empty, so Ghostty uses the same `.zshrc`. Only the terminal around it differs.

## VS Code vs Ghostty
| Area | Same in both? | Note |
|---|---|---|
| zsh, z4h, p10k, prompt | Yes | One shared `~/.zshrc` |
| tmux | Same config, different effect | tmux runs inside VS Code's xterm.js |
| Shell integration | No | VS Code's overlaps with z4h's; Ghostty has none |
| Rendering and fonts | No | xterm.js with GPU and glyph settings vs native |
| Auto `cd` on Python run | VS Code only | `python.terminal.executeInFileDir` |

## Likely causes (most likely first)
1. **tmux `-D` flag.** It detaches other clients from the `z4h` session. A terminal open
   in Ghostty and one in VS Code can kick each other off the shared session, which looks like a freeze.
2. **z4h plus VS Code shell integration** both emitting escape sequences.
3. **p10k `vcs` segment** stalling on every prompt in a git repo.
4. **`python.terminal.executeInFileDir`** sending an auto `cd` that triggers the prompt refresh.
5. A running program waiting on stdin, or a debugger or REPL holding the input.
6. `Ctrl+S` flow control (press `Ctrl+Q` to resume).

## Troubleshooting guide
**Quick unfreeze:** `Ctrl+C`, then `Ctrl+\`, then `Ctrl+Q`, or kill the terminal with the trash icon.

**Diagnose in order:**
1. Run `zsh -f` in a VS Code terminal. If the freeze stops, the cause is z4h or p10k.
2. Disable tmux inside VS Code only. Put this in `~/.zshrc` before `z4h init`:
   ```zsh
   [[ $TERM_PROGRAM == vscode ]] && zstyle ':z4h:' start-tmux no
   ```
   Or change `-D` to `-d` in the tmux command.
3. Turn off VS Code shell integration:
   ```json
   "terminal.integrated.shellIntegration.enabled": false
   ```
   Then run **Developer: Reload Window**.
4. Stop p10k git status in this repo (`~/.p10k.zsh`):
   ```zsh
   typeset -g POWERLEVEL9K_VCS_DISABLED_WORKDIR_PATTERN='~/Developer/learning/*'
   ```
5. Run `z4h update` in Terminal.app or Ghostty, not VS Code.
6. Turn off `python.terminal.executeInFileDir` if the freeze follows running a Python file.

## Status
No config has been changed yet. The tmux `$TERM_PROGRAM == vscode` edit is the proposed first fix.
