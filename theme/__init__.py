"""robominds dark theme — single source of truth + generators."""

from .palette import Blue, Gray, Green, Magenta, Orange, Red, Teal, Violet, Yellow


# Imported lazily so `python -m theme.colors_toml` does not trip a runpy
# RuntimeWarning (the package __init__ would otherwise load the module before
# runpy executes it as __main__).
def __getattr__(name):  # PEP 562
    if name == "ThemeOmarchy":
        from . import colors_toml

        return colors_toml.ThemeOmarchy
    if name == "ShellLock":
        from . import shell_lock_toml

        return shell_lock_toml.ShellLock
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "Blue",
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
