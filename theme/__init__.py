"""robominds dark theme — single source of truth + generator."""

from .palette import (
    Blue,
    DarkMode,
    Gray,
    Green,
    Magenta,
    Orange,
    Red,
    Teal,
    Violet,
    Yellow,
)

# Imported lazily so `python -m theme.theme_omarchy` does not trip a runpy
# RuntimeWarning (the package __init__ would otherwise load the module before
# runpy executes it as __main__).
def __getattr__(name):  # PEP 562
    if name in ("ThemeOmarchy", "ShellLock"):
        from . import theme_omarchy

        return getattr(theme_omarchy, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "Blue",
    "DarkMode",
    "Gray",
    "Green",
    "Magenta",
    "Orange",
    "Red",
    "ShellLock",
    "Teal",
    "ThemeOmarchy",
    "Violet",
    "Yellow",
]
