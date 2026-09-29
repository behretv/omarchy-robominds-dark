# robominds-dark theme generator

Build tool for the `omarchy-robominds-dark` Omarchy theme. Defines all colors
in one place (`palette.py`) and generates the theme files from it.

## Quick start

```bash
# each generator writes its file to the repo root
python -m theme.colors_toml        # colors.toml
python -m theme.shell_lock_toml    # shell.lock.toml
python -m theme.keyboard_rgb       # keyboard.rgb

# run the test suite
python -m pytest
```

Requires Python 3.11+ and the `toml` package (`pip install toml`).

## Output

One tiny generator per output file — no arguments, fixed input (the palette)
and output (the repo root):

| File | Purpose |
|------|---------|
| `colors.toml` | the omarchy quattro color file — the only file the installed theme needs; Omarchy auto-generates every per-app config (terminal, VS Code, Neovim (aether), shell, etc.) from it via templates on `omarchy theme set` |
| `shell.lock.toml` | shell lock screen colors |
| `keyboard.rgb` | keyboard RGB accent (hex without `#`) |

## Source of truth: `palette.py`

All colors live in `theme/palette.py` as frozen dataclasses — the raw
robominds brand families, shared with the light theme. Each color family is
its own class, with one field per shade it has. A family simply omits a field
it does not define (e.g. `Teal` has no `s100`, `Blue` has no `s900`). Named
neutrals (`midnight`, `white`, `navy_gray_*`, `near_black`, ...) are fields on
`Gray`; `muted` is a deliberate blend (gray 700/400) also kept here so the
palette contains every color the theme uses.

| Family | Shades |
|--------|--------|
| `Blue`   | 50–800 |
| `Gray`   | 50–800 + named `midnight`, `white`, `navy_gray_1`, `navy_gray_2`, `near_black`, `muted` |
| `Red`    | 100, 300, 500, 700 |
| `Violet` | 100, 300, 500, 700 |
| `Green`  | 100, 300, 500, 700 |
| `Yellow` | 100, 300, 500, 700 |
| `Orange` | 100, 300, 500, 700 |
| `Magenta`| 100, 300, 500, 700 |
| `Teal`   | 300, 500, 700 (no 100) |

The dark role mapping itself lives in the generators (`colors_toml.py`,
`shell_lock_toml.py`): backgrounds/foregrounds use the navy-tinted neutrals,
terminal colors use the brand families (lighter shades read better on dark
ground).

**To change a color:** edit the hex value in `palette.py` and re-run the
generators. Each maps semantic roles onto specific palette shades via its
dataclass (`ThemeOmarchy`, `ShellLock`); point a field at a different shade if
you want a role to use one.

## Programmatic API

```python
from theme import Blue, Gray, Teal  # raw palette
from theme import ShellLock, ThemeOmarchy

# raw shades
Blue.s400  # "#2593F4"
Gray.navy_gray_1  # "#1D2731"

# semantic roles resolved against the palette
t = ThemeOmarchy()
t.accent  # "#64B7F7"  (blue 300)
t.muted  # "#6B6B6B"  (gray blend)
```
