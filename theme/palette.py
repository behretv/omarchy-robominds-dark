"""Single source of truth for all robominds-dark colors.

Every color in the theme is defined here, organized by family and intensity.
The brand families are shared with the light theme (``Gray.near_black`` is the
one dark-only addition: the darkest background). The dark theme's role mapping
lives in the generator — this module holds raw shades only.

Generators import from this module; nothing else defines colors.
"""

from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Brand families — the raw palette (identical to the light theme)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Blue:
    s50: str = "#DDF4FD"
    s100: str = "#C0E6FC"
    s200: str = "#94D1F9"
    s300: str = "#64B7F7"
    s400: str = "#2593F4"
    s500: str = "#0073D7"
    s600: str = "#0052BB"
    s700: str = "#053C72"
    s800: str = "#0A1946"
    visualize: str = "#3D9BF0"  # diverging pos-1 (over-Soll)
    info_bg: str = "#E6F2FC"  # status: info background (blue tint)


@dataclass(frozen=True)
class Gray:
    s50: str = "#F9F9F9"
    s100: str = "#F2F2F2"
    s200: str = "#E6E6E6"
    s300: str = "#DBDBDB"
    s400: str = "#BBBBBB"
    s700: str = "#4D4D4D"
    s800: str = "#3C3C3C"
    midnight: str = "#262626"
    white: str = "#FFFFFF"
    navy_gray_1: str = "#1D2731"
    navy_gray_2: str = "#0E0E13"
    near_black: str = "#0A0A0A"  # darkest background — no brand shade this dark
    muted: str = "#6B6B6B"  # deliberate blend of s700/s400 — comments, hints
    visualize: str = "#8C8C8C"  # overlay: excluded by filter
    diverge_mid: str = "#F0EFEC"  # diverging scale: within target (neutral)


@dataclass(frozen=True)
class Red:
    s100: str = "#FBEAEA"
    s300: str = "#E88585"
    s500: str = "#D32F2F"
    s700: str = "#9C1F1F"
    visualize: str = "#FF3B30"  # overlay: collision / no-go zone
    diverge_neg: str = "#E06E6E"  # diverging scale: below target


@dataclass(frozen=True)
class Violet:
    s100: str = "#EDE6FA"
    s300: str = "#A98BE0"
    s500: str = "#6D46B8"
    s700: str = "#3F2373"


@dataclass(frozen=True)
class Green:
    s100: str = "#E9F5EE"
    s300: str = "#6FC08D"
    s500: str = "#15803D"
    s700: str = "#0F5C2E"
    visualize: str = "#00FF85"  # overlay: target pose / grasp point


@dataclass(frozen=True)
class Yellow:
    s100: str = "#FDF4E0"
    s300: str = "#F4C64D"
    s500: str = "#E8A100"
    s700: str = "#9C6D00"
    visualize: str = "#FFD400"  # overlay: detected candidate
    categorical: str = "#F2C230"  # cat-5 — lighter yellow for chart areas


@dataclass(frozen=True)
class Orange:
    s100: str = "#FCEDE0"
    s300: str = "#F0A96A"
    s500: str = "#E4761B"
    s700: str = "#A34F0E"


@dataclass(frozen=True)
class Magenta:
    s100: str = "#F6E7F2"
    s300: str = "#C97FB8"
    s500: str = "#A63A8F"
    s700: str = "#7A2968"


@dataclass(frozen=True)
class Teal:
    # No s100 in the brand palette.
    s300: str = "#66BDB6"
    s500: str = "#12857F"
    s700: str = "#0B5C5C"
    visualize: str = "#00E5FF"  # overlay: selected instance (cyan)
