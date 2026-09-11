"""Generate the omarchy theme files from the color palette.

The palette (see :mod:`theme.palette`) is the single source of truth for every
color. This module maps semantic roles onto specific shades and renders:

* ``colors.toml`` — the omarchy quattro color file (the only file Omarchy needs
  to derive all per-app configs: terminal, VS Code, Neovim, shell, ...).
* ``shell.lock.toml`` — shell lock screen colors.
* ``keyboard.rgb`` — keyboard RGB accent (hex without ``#``).

CLI::

    python -m theme.theme_omarchy             # writes all three to repo root
    python -m theme.theme_omarchy --out-dir dist
"""

import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import toml

# Support both `python -m theme.theme_omarchy` (package context) and
# `python3 theme/theme_omarchy.py` (direct file, as used by the Makefile).
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from theme import palette
else:
    from . import palette

HERE = Path(__file__).resolve().parent


@dataclass
class ThemeOmarchy:
    """Semantic roles -> shades, in ``colors.toml`` emission order.

    Backgrounds/foregrounds use the dark-mode navy-tinted surfaces and text;
    terminal colors use the brand families (lighter shades read better on dark
    ground). See :class:`palette.DarkMode`.
    """

    mode: str = "dark"
    accent: str = palette.Blue.s400
    selection: str = palette.Blue.s800
    muted: str = "#6B6B6B"  # deliberate blend — comments (shared with light)
    background: str = palette.Gray.navy_gray_1
    dark_background: str = palette.Gray.navy_gray_2
    darker_background: str = "#0A0A0A"  # deepest navy — no brand shade this dark
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
    blue: str = palette.Blue.s400
    magenta: str = palette.Violet.s300
    brown: str = palette.Orange.s700
    bright_red: str = palette.Red.s500
    bright_yellow: str = palette.Yellow.s500
    bright_green: str = palette.Green.s500
    bright_cyan: str = palette.Teal.s500
    bright_blue: str = palette.Blue.s500
    bright_magenta: str = palette.Magenta.s500


@dataclass
class ShellLock:
    """Colors for the shell lock screen (subset of the palette)."""

    text: str = palette.Gray.s300
    placeholder: str = palette.Gray.s700
    text_error: str = palette.Red.s500
    border: str = palette.Gray.s700
    border_active: str = palette.Blue.s400
    border_error: str = palette.Red.s500


def generate_colors_toml(theme: ThemeOmarchy) -> str:
    return toml.dumps(asdict(theme))


def generate_shell_lock_toml(lock: ShellLock) -> str:
    d = asdict(lock)
    # shell.lock.toml uses a hyphenated key for the error text color.
    return (
        f'text              = "{d["text"]}"\n'
        f'placeholder       = "{d["placeholder"]}"\n'
        f'text-error        = "{d["text_error"]}"\n'
        f'border            = "{d["border"]}"\n'
        f'border-active     = "{d["border_active"]}"\n'
        f'border-error      = "{d["border_error"]}"\n'
    )


def generate_keyboard_rgb() -> str:
    """Keyboard RGB accent — the accent color as hex without ``#``."""
    return palette.Blue.s400.lstrip("#") + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m theme.theme_omarchy",
        description="Generate the omarchy theme files from the color palette.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="output directory (default: repo root)",
    )
    args = parser.parse_args(argv)

    out_dir = args.out_dir or HERE.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "colors.toml").write_text(generate_colors_toml(ThemeOmarchy()), encoding="utf-8")
    print(f"  ✓ colors.toml: {out_dir / 'colors.toml'}")
    (out_dir / "shell.lock.toml").write_text(generate_shell_lock_toml(ShellLock()), encoding="utf-8")
    print(f"  ✓ shell.lock.toml: {out_dir / 'shell.lock.toml'}")
    (out_dir / "keyboard.rgb").write_text(generate_keyboard_rgb(), encoding="utf-8")
    print(f"  ✓ keyboard.rgb: {out_dir / 'keyboard.rgb'}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
