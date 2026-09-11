"""Tests for theme.palette — the single source of truth (raw brand palette)."""

from __future__ import annotations

import pytest

from theme.palette import Blue, DarkMode, Gray, Green, Magenta, Red, Teal, Yellow


# ---------------------------------------------------------------------------
# Brand families hold the CI shades as fields (identical to the light theme)
# ---------------------------------------------------------------------------


def test_blue_has_full_shade_range():
    blue = Blue()
    assert blue.s50 == "#DDF4FD"
    assert blue.s100 == "#C0E6FC"
    assert blue.s200 == "#94D1F9"
    assert blue.s300 == "#64B7F7"
    assert blue.s400 == "#2593F4"
    assert blue.s500 == "#0073D7"
    assert blue.s600 == "#0052BB"
    assert blue.s700 == "#053C72"
    assert blue.s800 == "#0A1946"


def test_gray_includes_named_neutrals_alongside_shades():
    gray = Gray()
    assert gray.s50 == "#F9F9F9"
    assert gray.s100 == "#F2F2F2"
    assert gray.s200 == "#E6E6E6"
    assert gray.s300 == "#DBDBDB"
    assert gray.s400 == "#BBBBBB"
    assert gray.s700 == "#4D4D4D"
    assert gray.s800 == "#3C3C3C"
    assert gray.midnight == "#262626"
    assert gray.white == "#FFFFFF"
    assert gray.navy_gray_1 == "#1D2731"
    assert gray.navy_gray_2 == "#0E0E13"


def test_red_family_has_100_300_500_700():
    red = Red()
    assert red.s100 == "#FBEAEA"
    assert red.s300 == "#E88585"
    assert red.s500 == "#D32F2F"
    assert red.s700 == "#9C1F1F"


def test_teal_has_no_s100():
    teal = Teal()
    assert not hasattr(teal, "s100")
    assert teal.s300 == "#66BDB6"
    assert teal.s500 == "#12857F"
    assert teal.s700 == "#0B5C5C"


def test_families_are_immutable():
    # frozen dataclass: mutation raises
    with pytest.raises(Exception):
        Blue().s50 = "#000000"  # type: ignore[misc]


# ---------------------------------------------------------------------------
# Dark mode — dark-specific semantic colors from [data-theme="dark"]
# ---------------------------------------------------------------------------


def test_dark_mode_surfaces_are_navy_tinted_not_black():
    d = DarkMode()
    assert d.bg == "#0E1830"
    assert d.surface == "#161F35"
    assert d.surface_2 == "#1E2842"
    assert d.surface_3 == "#27324F"
    # never pure black
    for v in (d.bg, d.surface, d.surface_2, d.surface_3):
        assert v != "#000000"


def test_dark_mode_text_is_light_not_pure_white():
    d = DarkMode()
    assert d.text == "#F2F4F8"
    assert d.text_muted == "#A8B2C4"
    assert d.text_subtle == "#7A879E"
    assert d.text_on_accent == "#071022"
    # never pure white (avoids halation on dark ground)
    assert d.text != "#FFFFFF"


def test_dark_mode_primary_uses_lighter_blue():
    d = DarkMode()
    assert d.primary == "#2593F4"  # blue-500
    assert d.primary_hover == "#64B7F7"  # blue-400
    assert d.primary_active == "#0073D7"  # blue-600
    assert d.primary_subtle == "#1A2C52"


def test_dark_mode_status_colors_are_lightened():
    d = DarkMode()
    assert d.success == "#3DBE6E"
    assert d.warning == "#F4C64D"
    assert d.danger == "#F27272"
    assert d.info == "#4BA5F6"
    assert d.neutral == "#8B97AC"
    assert d.success_bg == "#12301F"
    assert d.warning_bg == "#322608"
    assert d.danger_bg == "#351515"
    assert d.info_bg == "#0F2743"
    assert d.neutral_bg == "#1E2842"


def test_dark_mode_borders_and_links():
    d = DarkMode()
    assert d.border == "#2A3550"
    assert d.border_strong == "#3E4C6E"
    assert d.link == "#64B7F7"
    assert d.link_hover == "#94D1F9"
    assert d.link_visited == "#B79BE8"
    assert d.selection_bg == "#23407A"
    assert d.selection_fg == "#F2F4F8"
