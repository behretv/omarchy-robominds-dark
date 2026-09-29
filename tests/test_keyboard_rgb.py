"""Tests for theme.keyboard_rgb — generates keyboard.rgb (accent, no ``#``)."""

from __future__ import annotations

from pathlib import Path

from theme.colors_toml import ThemeOmarchy
from theme.keyboard_rgb import render

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_keyboard_rgb_matches_shipped_file():
    assert render() == (REPO_ROOT / "keyboard.rgb").read_text()


def test_keyboard_rgb_is_the_theme_accent():
    assert render() == ThemeOmarchy.accent.lstrip("#") + "\n"
