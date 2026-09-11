"""Tests for theme.theme_omarchy — generates the omarchy theme files."""

from __future__ import annotations

import tomllib
from dataclasses import asdict
from pathlib import Path

import toml

from theme.theme_omarchy import (
    ShellLock,
    ThemeOmarchy,
    generate_colors_toml,
    generate_keyboard_rgb,
    generate_shell_lock_toml,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def _parse(path: Path) -> dict[str, str]:
    return tomllib.loads(path.read_text())


def test_colors_toml_matches_shipped_file():
    generated = generate_colors_toml(ThemeOmarchy())
    assert _parse(generated) == _parse(REPO_ROOT / "colors.toml")


def test_colors_toml_key_order_and_mode():
    text = generate_colors_toml(ThemeOmarchy())
    keys = [line.split(" = ")[0] for line in text.strip().splitlines() if "=" in line]
    assert keys[0] == "mode"
    assert keys[-1] == "bright_magenta"
    assert _parse(text)["mode"] == "dark"


def test_every_color_value_is_hex():
    for role, value in asdict(ThemeOmarchy()).items():
        if role == "mode":
            continue
        assert value.startswith("#"), f"{role} = {value!r} is not a hex color"


def test_shell_lock_matches_shipped_file():
    generated = generate_shell_lock_toml(ShellLock())
    assert generated == (REPO_ROOT / "shell.lock.toml").read_text()


def test_keyboard_rgb_matches_shipped_file():
    assert generate_keyboard_rgb() == (REPO_ROOT / "keyboard.rgb").read_text()
