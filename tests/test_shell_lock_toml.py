"""Tests for theme.shell_lock_toml — generates shell.lock.toml."""

from __future__ import annotations

from pathlib import Path

from theme.shell_lock_toml import render

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_shell_lock_toml_matches_shipped_file():
    assert render() == (REPO_ROOT / "shell.lock.toml").read_text()
