"""Tests for theme.palette — the single source of truth (raw brand palette)."""

from __future__ import annotations

import pytest

from theme.palette import Blue, Gray, Green, Magenta, Red, Teal, Yellow

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
    assert gray.near_black == "#0A0A0A"  # darkest background (dark theme only)
    assert gray.muted == "#6B6B6B"  # blend of s700/s400, not a raw brand shade


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


def test_magenta_family():
    magenta = Magenta()
    assert magenta.s100 == "#F6E7F2"
    assert magenta.s300 == "#C97FB8"
    assert magenta.s500 == "#A63A8F"
    assert magenta.s700 == "#7A2968"


def test_visualization_colors_from_styleguide():
    # Data-viz / overlay colors from the robominds styleguide, per family.
    assert Red().visualize == "#FF3B30"  # overlay: collision
    assert Red().diverge_neg == "#E06E6E"  # diverging: below target
    assert Gray().diverge_mid == "#F0EFEC"  # diverging: within target
    assert Gray().visualize == "#8C8C8C"  # overlay: excluded
    assert Blue().visualize == "#3D9BF0"  # diverging: above target
    assert Blue().info_bg == "#E6F2FC"  # status: info background
    assert Green().visualize == "#00FF85"  # overlay: target pose
    assert Teal().visualize == "#00E5FF"  # overlay: selected (cyan)
    assert Yellow().visualize == "#FFD400"  # overlay: candidate
    assert Yellow().categorical == "#F2C230"  # cat-5 chart area


def test_families_are_immutable():
    # frozen dataclass: mutation raises
    with pytest.raises(Exception):
        Blue().s50 = "#000000"  # type: ignore[misc]
