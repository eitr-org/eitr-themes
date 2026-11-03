# Eitr themes

Official extra themes for [Eitr Linux](https://eitr.info). Built-in themes ship
with Eitr itself; the themes here are installed one by one from Eitr's catalog,
which downloads only the themes you choose.

| Theme | Description |
|---|---|
| Catppuccin | Catppuccin Mocha: soft pastels on a deep blue-purple base |
| Catppuccin Latte (light) | Catppuccin Latte: bright pastels on a soft cream base |
| Daylight (light) | Pure white and charcoal with quiet, minimal artwork |
| Gruvbox | Gruvbox: warm charcoal, earthy greens and muted amber |
| Jade | Deep forest green and warm cream with quiet night scenes |
| Kanagawa | Kanagawa: ink-dark blues and muted gold with Japanese artwork |
| Moss | Charcoal, olive and copper with candlelit Norse figures |
| Nord | The popular Nord palette: cool arctic blues and soft snow |
| One Dark Pro | One Dark Pro: cool charcoal with bright blue and violet accents |
| Rosé Pine (light) | Rosé Pine Dawn: warm cream, muted rose and soft teal |
| Stillwater | Near-black and ash grey with quiet, wintry artwork |
| Wisteria (light) | Soft white and vivid blue with violet flowers and airy skies |

## Format

Each folder is a data-only theme package described by `eitr-theme.json`; the
format is documented in Eitr's
[theme author guide](https://github.com/eitr-org/eitr/blob/main/distro/THEMES.md).
Eitr refuses packages containing code, links or executable files, and generates
editor and application colors locally. `eitr-catalog.json` is the index the
catalog reads; regenerate and check it with Eitr's
`tools/theme-catalog-index.py` after changing a theme. `sources/` holds artwork
source material and is not part of any package.

## Credits

Palettes named after their projects (Catppuccin, Gruvbox, Kanagawa, Nord,
One Dark Pro, Rosé Pine) follow those projects' published colours; all of them
are MIT licensed. Wallpaper provenance is in each theme's `artwork.md`.
Everything else is GPL-3.0, like Eitr.
