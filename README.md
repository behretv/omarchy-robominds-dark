# omarchy-robominds-dark

A dark Omarchy theme using the official robominds brand colors, extracted from
the [robominds living style guide](https://brand.robominds.de).

## Install

```bash
omarchy theme install https://github.com/<org>/omarchy-robominds-dark.git
```

Or clone manually:

```bash
git clone https://github.com/<org>/omarchy-robominds-dark.git \
  ~/.config/omarchy/themes/robominds-dark
omarchy theme set robominds-dark
```

## How it works

This repo doubles as:

1. **An installable Omarchy theme** — the repo root is the theme directory.
   `colors.toml` is the only required file; Omarchy auto-generates terminal
   configs, VS Code theme, Neovim (aether) config, shell colors, and more from
   it via templates on `omarchy theme set`.

2. **A build tool** — the [`theme/`](theme/) directory contains
   `palette.py` (the single source of truth: every color as dataclasses) plus
   one tiny generator per output file (`colors_toml.py`, `shell_lock_toml.py`,
   `keyboard_rgb.py`). Edit colors in one place, regenerate.

```
omarchy-robominds-dark/
├── colors.toml           ← generated: the omarchy quattro color file
├── shell.lock.toml       ← generated: shell lock screen colors
├── keyboard.rgb          ← generated: keyboard RGB accent (hex without #)
├── backgrounds/          ← wallpaper images (add your own)
├── icons.theme           ← icon theme name
├── preview.png           ← theme picker preview
├── unlock.png            ← lock screen image
├── LICENSE
├── README.md             ← you are here
├── .gitignore
├── tests/                ← pytest suite for the palette + generator
└── theme/                ← build tooling (not part of the installed theme)
    ├── palette.py        ← single source of truth: all colors as dataclasses
    ├── colors_toml.py    ← roles -> shades, writes colors.toml
    ├── shell_lock_toml.py← writes shell.lock.toml
    ├── keyboard_rgb.py   ← writes keyboard.rgb
    └── README.md         ← build tool docs
```

## Regenerating the theme files

```bash
python -m theme.colors_toml        # writes colors.toml to repo root
python -m theme.shell_lock_toml    # writes shell.lock.toml
python -m theme.keyboard_rgb       # writes keyboard.rgb
```

Requires Python 3.11+ and the `toml` package (`pip install toml`). Run the test
suite with `python -m pytest`.

## Adding backgrounds

Drop wallpaper images into `backgrounds/` (jpg, png, webp). Omarchy cycles
through them with `omarchy theme bg next`.

## License

MIT
