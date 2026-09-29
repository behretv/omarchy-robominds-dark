"""Tests for theme.colors_toml — generates colors.toml from the palette."""

from __future__ import annotations

import tomllib
from dataclasses import asdict
from pathlib import Path

from theme import palette
from theme.colors_toml import ThemeOmarchy, render

REPO_ROOT = Path(__file__).resolve().parent.parent


def _parse(text: str) -> dict[str, str]:
    return tomllib.loads(text)


def test_colors_toml_matches_shipped_file():
    assert _parse(render()) == _parse((REPO_ROOT / "colors.toml").read_text())


def test_colors_toml_key_order_and_mode():
    keys = [line.split(" = ")[0] for line in render().strip().splitlines() if "=" in line]
    assert keys[0] == "mode"
    assert keys[-1] == "bright_magenta"
    assert _parse(render())["mode"] == "dark"


def test_every_color_value_is_hex():
    for role, value in asdict(ThemeOmarchy()).items():
        if role == "mode":
            continue
        assert value.startswith("#"), f"{role} = {value!r} is not a hex color"


def test_no_stray_literals_every_value_is_a_palette_color():
    # Values must come from the palette — spot-check the ones that used to be
    # inline literals.
    t = ThemeOmarchy()
    assert t.muted == palette.Gray.muted
    assert t.darker_background == palette.Gray.near_black
