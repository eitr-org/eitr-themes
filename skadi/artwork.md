# Skaði Artwork

## Current collection

Original Codex image generation, using owner-approved designs. No third-party
artwork was used as an input. The flat-ink images used an owner-approved Eitr
wallpaper (`style-dusk-fjord.png`) as the style reference.
`skadi-a2` and `skadi-b2` were edits of `skadi-a` and `skadi-b`, using
`skadi-c` as the character reference while retaining their flat-ink style.

Native originals and verbatim generation briefs are retained in
`sources/skadi/`, outside the installable package.

Exports are subject-centred crop-to-fill with Lanczos resampling, never stretched
or padded: 3840×2160 JPEGs from 1672×941 masters, and 3440×1440 JPEGs from
separately generated 1914×822 panoramas. These are not native 4K generations.
JPEG quality is 92 without chroma subsampling, matching Eitr’s exporter.
Centred framing (0.5, 0.5) retains the subjects; the panorama crop removes only
a narrow strip at the top and bottom.

`preview.png` is the 01 wallpaper at 1280×720, a temporary artwork preview;
the owner will replace it with a desktop screenshot later.

- `backgrounds/01-spirit-wolf.jpg` and `backgrounds-ultrawide/01-spirit-wolf.jpg`: Skaði resting beside a pale-blue spirit wolf above a frozen valley. Sources: `skadi-d.png` and `skadi-d-ultrawide.png`.
- `backgrounds/02-ridge-hunt.jpg` and `backgrounds-ultrawide/02-ridge-hunt.jpg`: Skaði drawing her bow on a snowy mountain ridge. Sources: `skadi-c.png` and `skadi-c-ultrawide.png`.
- `backgrounds/03-ski-trail.jpg` and `backgrounds-ultrawide/03-ski-trail.jpg`: Skaði skiing down a bright mountainside in flat ink style. Sources: `skadi-a2.png` and `skadi-a2-ultrawide.png`.
- `backgrounds/04-frozen-lake.jpg` and `backgrounds-ultrawide/04-frozen-lake.jpg`: Skaði with two white wolves beside a frozen lake in flat ink style. Sources: `skadi-b2.png` and `skadi-b2-ultrawide.png`.

## Verbatim generation prompts

The complete batch prompts below retain the shared style instructions and each
image-specific instruction verbatim. Other images mentioned in those batches
are not additional files in this package.

### brief-goddesses.md

```text
Use your image generation tool to create four NEW desktop wallpapers and save them in this folder (/home/erick/Development/personal/eitr-testing/ideas/light-goddesses) as freyja-a.png, freyja-b.png, skadi-a.png and skadi-b.png. Landscape 16:9, the highest resolution the tool supports. Do not write code. Afterwards report each file name and its actual pixel size.

The attached style-dusk-fjord.png is the STYLE reference only (an owner-approved wallpaper from the same desktop). Match its art style closely: a clean flat vector / cel-shaded illustration with bold black ink outlines, flat colour planes with one or two shading steps, angular faceted rock and simple shapes, friendly and handcrafted like an animated-series background. Do not copy its scene or its sunset colours.

These are for two LIGHT desktop themes, so each picture is bright, airy and mostly pale, with soft daylight, so dark text and windows read well over it. Keep the top strip and the centre fairly calm; put the figures and details lower and to the sides. Figures are small in the landscape, graceful and heroic, never sexualised. No text, logos, signatures or watermarks.

Freyja (Norse goddess of love, beauty and spring; Fólkvangr is her meadow). Palette: warm cream background #FAF5F0, blush surfaces #F1E7DF and #E5D4CA, plum-brown ink #42343B, dusty rose accent #A45B72, honey gold #A47A37, sage green #537E61, soft blue #577C9D, mauve #96628D, teal #468487.
1. freyja-a.png: Freyja rides her small golden chariot drawn by two big fluffy cats across Fólkvangr, a wide rolling meadow full of wildflowers, gentle hills and a few birch trees under a pale blush sky with soft clouds; petals drift in the breeze.
2. freyja-b.png: A calm flower valley at morning with a winding stream; Freyja stands on a gentle rise in her falcon-feather cloak, the Brísingamen necklace glowing softly gold; a falcon glides above, apple trees in blossom, distant pale mountains.

Skaði (Norse giantess of winter, mountains, skiing and the hunt). Palette: cool snow background #F5F8FA, ice surfaces #E8EFF3 and #D5E0E7, slate ink #303D49, steel blue accent #467B9B, frost teal #628F91 and #3E8191, pine green #4D806F, pale gold #97752F, lavender #856CA0, berry red #B64D60.
3. skadi-a.png: Skaði skis down a bright snowy mountainside with her bow on her back, leaving a curving track; faceted snowy peaks, a few dark pines, a pale clear sky with a small winter sun.
4. skadi-b.png: A still frozen mountain lake in soft winter light; Skaði stands on the shore with two white wolves at her side, snow-laden pines, ice reflections, distant peaks under a pale lavender-blue sky with light snowfall.
```

### brief-goddesses-2.md

```text
Use your image generation tool to create four NEW desktop wallpapers and save them in this folder (/home/erick/Development/personal/eitr-testing/ideas/light-goddesses) as skadi-c.png, skadi-d.png, freyja-c.png and freyja-d.png. Landscape 16:9, the highest resolution the tool supports. Do not write code. Afterwards report each file name and its actual pixel size.

Style: rich, beautiful fantasy illustration, clearly drawn and hand-painted (confident linework, painterly shading and soft light), centred on the goddess as a striking character, with a detailed landscape. Not photorealistic and not a flat cartoon. Original designs only: do not imitate any specific artist or existing artwork. Dignified, heroic and graceful; never sexualised, modest clothing. These are wallpapers for LIGHT desktop themes: overall bright and airy, with the figure placed to the left or right third so the opposite side and the top strip stay calm for windows and a top bar. No text, logos, signatures or watermarks.

Skaði, Norse giantess of winter, mountains, skiing and the hunt. Palette: snow white #F5F8FA, ice #E8EFF3 and #D5E0E7, slate #303D49, steel blue #467B9B, frost teal #628F91 and #3E8191, pine green #4D806F, a touch of berry red #B64D60 and lavender #856CA0.
Her look: frost-pale skin with flowing blue rune markings on her face, long white hair in thick braids blowing in the wind, a heavy white fur mantle over dark quilted leather, a tall bow and a quiver, carved bone and silver details.
1. skadi-c.png: Skaði draws her bow on a windswept snowy ridge in a light blizzard, eyes fixed on a distant target, snow peaks and pale sky behind her.
2. skadi-d.png: Skaði rests in the snow beside a huge, gentle pale-blue spirit wolf with frost markings, her hand on its fur, a frozen valley and soft winter light behind them.

Freyja, Norse goddess of love, beauty, spring and battle. Palette: warm cream #FAF5F0, blush #F1E7DF and #E5D4CA, plum-brown #42343B, dusty rose #A45B72, honey gold #A47A37, sage green #537E61, soft blue #577C9D, mauve #96628D.
Her look: long flowing golden-red hair, a delicate gold crown with flowers, the Brísingamen necklace glowing gold at her throat, a flowing gown with gold embroidery and a green-gold cloak, great falcon-feather wings.
3. freyja-c.png: Freyja stands with her falcon wings half open in a sunlit spring meadow full of wildflowers, one hand resting on a tall spear, her two cats (one grey tabby, one white) at her feet, gentle hills and blossoming trees behind her.
4. freyja-d.png: Freyja sits on a sun-warmed rock above a flowering valley at golden morning, her spear and a round gold-rimmed shield laid beside her, wildflowers and a falcon perched nearby, soft clouds and distant mountains.
```

### brief-skadi-redraw.md

```text
Use your image generation/editing tool to edit two attached images and save the results in this folder (/home/erick/Development/personal/eitr-testing/ideas/light-goddesses): edit skadi-a.png into skadi-a2.png and skadi-b.png into skadi-b2.png. Landscape 16:9, the highest resolution the tool supports. Do not write code; afterwards report each file name and its actual pixel size.

The third attached image, skadi-c.png, is the CHARACTER reference: it shows how the goddess Skaði looks in this theme. In both edits, keep everything else exactly as it is (the art style with bold black ink outlines and flat cel-shaded colours, the scene, composition, landscape, sky, colours, her pose and size, the skis and track in skadi-a, the two white wolves and the frozen lake in skadi-b) and change only Skaði's character design to match the reference, drawn in each picture's own flat ink style:
- frost-pale skin with flowing blue rune markings on her face (and a few on her hands),
- long white hair in thick braids blowing in the wind (not blonde),
- a heavy white fur mantle over dark quilted leather with brown leather straps and a carved bone-and-silver brooch,
- a carved pale bone bow with knotwork, and a leather quiver with red-fletched arrows.
Keep her dignified and heroic; modest clothing. No text, logos, signatures or watermarks.
```

### brief-uw-goddesses.md

```text
Use your image generation/editing tool to make ultrawide versions of the eight attached wallpapers and save each one in this folder (/home/erick/Development/personal/eitr-testing/ideas/light-goddesses) as <name>-ultrawide.png: freyja-a-ultrawide.png, freyja-b-ultrawide.png, freyja-c-ultrawide.png, freyja-d-ultrawide.png, skadi-a2-ultrawide.png, skadi-b2-ultrawide.png, skadi-c-ultrawide.png and skadi-d-ultrawide.png. Each must be a 21:9 landscape image at the highest resolution the tool supports. Do not write code; afterwards report each file name and its actual pixel size.

Extend each picture sideways (outpaint left and right) so it fills 21:9. Keep everything already in each picture exactly as it is: its own art style (the flat ink cel-shaded ones stay flat ink; the painterly ones stay painterly), colours, the goddess, her face, markings, hair, clothes, wings, animals and weapons, the landscape and sky, at the same size and in the same place relative to each other. Every figure keeps natural hands and anatomy. Only add new matching scenery at the sides (more meadow, flowers, trees, hills, snow, pines, mountains, water and sky continuing naturally). Never stretch, squash or pad with flat colour, and add no text, logos or watermarks.
```

## Palette contrast

Ratios against `background`, calculated with Eitr’s `walker/scripts/themes/palette.py`
`contrast` helper (WCAG sRGB). Owner-approved base colours are unchanged.
Bright variants and `bright_foreground` use 88% of each sRGB channel to make
them slightly darker for a light theme. `orange` aliases yellow, and `brown`
aliases muted, following Eitr Light’s role mapping.

| Text role | Contrast | Below 4.5:1 |
|---|---:|:---:|
| foreground | 10.42:1 |  |
| muted | 3.68:1 | Yes |
| accent | 4.31:1 | Yes |
| second | 3.36:1 | Yes |
| alert | 4.67:1 |  |
| bright_foreground | 11.58:1 |  |
| red | 4.67:1 |  |
| green | 4.25:1 | Yes |
| yellow | 4.02:1 | Yes |
| blue | 4.31:1 | Yes |
| magenta | 4.23:1 | Yes |
| cyan | 4.14:1 | Yes |
| orange | 4.02:1 | Yes |
| bright_red | 5.71:1 |  |
| bright_green | 5.20:1 |  |
| bright_yellow | 4.96:1 |  |
| bright_blue | 5.31:1 |  |
| bright_magenta | 5.21:1 |  |
| bright_cyan | 5.07:1 |  |

`color1`–`color6` alias the named colours, `color9`–`color14` their bright
variants, `color7` is foreground, `color8` is muted, and `color15` is
bright_foreground, so their ratios are identical. Surface roles are not text.
