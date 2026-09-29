"""Generate ``keyboard.rgb`` — the keyboard RGB accent (hex without ``#``).

CLI: ``python -m theme.keyboard_rgb`` or ``python3 theme/keyboard_rgb.py``
"""

import sys
from pathlib import Path

# Support both `python -m theme.keyboard_rgb` (package context) and
# `python3 theme/keyboard_rgb.py` (direct file, as used by the Makefile).
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from theme import palette
else:
    from . import palette

OUT_FILE = Path(__file__).resolve().parent.parent / "keyboard.rgb"

# The keyboard accent is the theme accent (ThemeOmarchy.accent = Blue.s300).
ACCENT = palette.Blue.s300


def render() -> str:
    return ACCENT.lstrip("#") + "\n"


def main() -> int:
    OUT_FILE.write_text(render(), encoding="utf-8")
    print(f"  ✓ {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
