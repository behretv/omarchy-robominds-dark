"""Generate ``colors.toml`` — the omarchy quattro color file — from the palette.

The palette (see :mod:`theme.palette`) is the single source of truth for every
color. This module maps semantic roles onto specific shades and renders the
flat ``colors.toml`` at the repo root — the only file Omarchy needs to derive
all per-app configs (terminal, VS Code, Neovim, shell, ...).

CLI: ``python -m theme.colors_toml`` or ``python3 theme/colors_toml.py``
"""

import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import toml

# Support both `python -m theme.colors_toml` (package context) and
# `python3 theme/colors_toml.py` (direct file, as used by the Makefile).
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from theme import palette
else:
    from . import palette

OUT_FILE = Path(__file__).resolve().parent.parent / "colors.toml"


@dataclass(frozen=True)
class ThemeOmarchy:
    """Semantic roles -> shades, in ``colors.toml`` emission order.

    Backgrounds/foregrounds use the dark navy-tinted neutrals; terminal colors
    use the brand families (lighter shades read better on dark ground).
    """

    mode: str = "dark"
    accent: str = palette.Blue.s300
    selection: str = palette.Blue.s700
    muted: str = palette.Gray.muted
    background: str = palette.Gray.navy_gray_1
    dark_background: str = palette.Gray.navy_gray_2
    darker_background: str = palette.Gray.near_black
    lighter_background: str = palette.Blue.s800
    foreground: str = palette.Gray.s300
    dark_foreground: str = palette.Gray.s700
    light_foreground: str = palette.Gray.s400
    bright_foreground: str = palette.Gray.s200
    red: str = palette.Red.s300
    yellow: str = palette.Yellow.s300
    orange: str = palette.Orange.s500
    green: str = palette.Green.s300
    cyan: str = palette.Teal.s300
    blue: str = palette.Blue.s300
    magenta: str = palette.Violet.s300
    brown: str = palette.Orange.s700
    bright_red: str = palette.Red.s500
    bright_yellow: str = palette.Yellow.s500
    bright_green: str = palette.Green.s500
    bright_cyan: str = palette.Teal.s500
    bright_blue: str = palette.Blue.s400
    bright_magenta: str = palette.Magenta.s500


def render() -> str:
    return toml.dumps(asdict(ThemeOmarchy()))


def main() -> int:
    OUT_FILE.write_text(render(), encoding="utf-8")
    print(f"  ✓ {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
