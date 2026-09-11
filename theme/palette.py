"""Single source of truth for all robominds-dark colors.

Two layers, mirroring the style guide's own structure:

1. **Brand families** (``Blue``, ``Gray``, ...) — the raw palette, identical to
   the light theme. These are the CI colors and do not change between modes.

2. **Dark mode** (:class:`DarkMode`) — the dark-specific semantic colors from
   the style guide's ``[data-theme="dark"]`` block. The brand colors were
   designed for light backgrounds, so dark mode re-assigns roles using
   lighter, navy-tinted values (never pure black/white).

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


@dataclass(frozen=True)
class Red:
    s100: str = "#FBEAEA"
    s300: str = "#E88585"
    s500: str = "#D32F2F"
    s700: str = "#9C1F1F"


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


@dataclass(frozen=True)
class Yellow:
    s100: str = "#FDF4E0"
    s300: str = "#F4C64D"
    s500: str = "#E8A100"
    s700: str = "#9C6D00"


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


# ---------------------------------------------------------------------------
# Dark mode — dark-specific semantic colors ([data-theme="dark"])
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class DarkMode:
    """Dark-mode surfaces and text. Navy-tinted, never pure black/white."""

    # Surfaces — progressively lighter navy tints.
    bg: str = "#0E1830"  # --rm-bg — main background
    surface: str = "#161F35"  # --rm-surface — cards, panels
    surface_2: str = "#1E2842"  # --rm-surface-2 — second level
    surface_3: str = "#27324F"  # --rm-surface-3 — hover on surfaces

    # Text — light, never pure white (avoids halation on dark ground).
    text: str = "#F2F4F8"  # --rm-text — primary (16:1)
    text_muted: str = "#A8B2C4"  # --rm-text-muted — secondary (8.3:1)
    text_subtle: str = "#7A879E"  # --rm-text-subtle — placeholders, meta
    text_on_accent: str = "#071022"  # --rm-text-on-accent

    # Primary action — lighter blue reads better on dark ground.
    primary: str = "#2593F4"  # --rm-primary = blue-500 (5.5:1)
    primary_hover: str = "#64B7F7"  # --rm-primary-hover = blue-400
    primary_active: str = "#0073D7"  # --rm-primary-active = blue-600
    primary_subtle: str = "#1A2C52"  # --rm-primary-subtle — tint behind primary

    # Status — lightened variants for contrast on dark ground.
    success: str = "#3DBE6E"  # --rm-success (7.4:1)
    warning: str = "#F4C64D"  # --rm-warning (10.9:1)
    danger: str = "#F27272"  # --rm-danger (6.2:1)
    info: str = "#4BA5F6"  # --rm-info (6.7:1)
    neutral: str = "#8B97AC"  # --rm-neutral — offline / unknown
    success_bg: str = "#12301F"
    warning_bg: str = "#322608"
    danger_bg: str = "#351515"
    info_bg: str = "#0F2743"  # --rm-info-bg
    neutral_bg: str = "#1E2842"

    # Borders and dividers.
    border: str = "#2A3550"  # --rm-border
    border_strong: str = "#3E4C6E"  # --rm-border-strong

    # Links and selection.
    link: str = "#64B7F7"  # --rm-link = blue-400
    link_hover: str = "#94D1F9"  # --rm-link-hover = blue-300
    link_visited: str = "#B79BE8"  # --rm-link-visited
    selection_bg: str = "#23407A"  # --rm-selection-bg
    selection_fg: str = "#F2F4F8"  # --rm-selection-fg
