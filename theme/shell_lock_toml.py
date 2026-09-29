"""Generate ``shell.lock.toml`` — shell lock screen colors — from the palette.

CLI: ``python -m theme.shell_lock_toml`` or ``python3 theme/shell_lock_toml.py``
"""

import sys
from dataclasses import asdict, dataclass
from pathlib import Path

# Support both `python -m theme.shell_lock_toml` (package context) and
# `python3 theme/shell_lock_toml.py` (direct file, as used by the Makefile).
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from theme import palette
else:
    from . import palette

OUT_FILE = Path(__file__).resolve().parent.parent / "shell.lock.toml"


@dataclass(frozen=True)
class ShellLock:
    """Colors for the shell lock screen (subset of the palette)."""

    text: str = palette.Gray.s300
    placeholder: str = palette.Gray.s700
    text_error: str = palette.Red.s500
    border: str = palette.Gray.s700
    border_active: str = palette.Blue.s300
    border_error: str = palette.Red.s500


def render() -> str:
    d = asdict(ShellLock())
    # shell.lock.toml uses hyphenated keys.
    return (
        f'text              = "{d["text"]}"\n'
        f'placeholder       = "{d["placeholder"]}"\n'
        f'text-error        = "{d["text_error"]}"\n'
        f'border            = "{d["border"]}"\n'
        f'border-active     = "{d["border_active"]}"\n'
        f'border-error      = "{d["border_error"]}"\n'
    )


def main() -> int:
    OUT_FILE.write_text(render(), encoding="utf-8")
    print(f"  ✓ {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
