# Afterglow and the realm wallpapers

This directory owns the native masters, provenance and export recipes for the
eleven themes moved from Eitr. Each package owns its exported wallpapers.
Afterglow's written-brief replacements and earlier prompts are in the batch
04 and earlier manifests. Palette and integration code stays in Eitr.

From an adjacent Eitr checkout, or with `EITR_CHECKOUT` set to its directory,
run `python3 sources/eitr-realms/export.py 13` to rebuild batch 13, for example.
Manifest paths are relative to the Store checkout. The `eitr:` prefix denotes
a reference whose master belongs to the Eitr checkout. Regenerate the previews
and catalog with the Eitr tools after exporting.

The original wallpaper artwork is licensed CC BY 4.0. See `artwork.json` and
each package's `artwork.md` for provenance.

## Realm themes — Batch 05

Alfheim, Asgard, Helheim, Jotunheim, Midgard, Muspelheim, Niflheim, Ragnarök, Svartalfheim and Vanaheim are dark themes. All ten use the owner's realm palettes (2026-10-27 and 2026-10-28); each theme’s `artwork.md` names its palette and integration base. `artwork-batch-05.json` retains the exact written prompts, native source hashes and crop framing. Native sources and `export.py` live in `branding/sources/wallpapers/batch-05/`; the script rebuilds both exports and their manifest entries. No reference images were used.

## Realm environments — Batch 06

At the owner's request, these ten second realm wallpapers use scenic landscapes
and rich painterly concept-art lighting instead of the default ink screenprint
style and no-scenery rule. This exception applies only to the ten Batch 06
images, in both aspect ratios. The environments follow each theme's
`colors.toml`, with calm space at the top for the desktop bar.

`artwork-batch-06.json` records exact written briefs, source dimensions, hashes
and framing. No reference images were supplied. All architecture and compositions
are original, without characters, readable lettering or third-party designs.
Native masters and `export.py` live in
`branding/sources/wallpapers/batch-06/`. The exporter updates the 4K and ultrawide
manifests without rebuilding previews. Separate panoramic compositions preserve
landmarks where a crop would lose them; exports never stretch or pad images.

## Realm paintings and illustrations — Batch 07

The owner explicitly requested scenic backgrounds and varied rendering media
for additional realm wallpapers, excluding Ragnarök. This batch-specific exception includes oil painting, gouache, pastel
matte painting, cel shading, loose brushwork, graphic novel, grey wash and
flat poster treatments, with realistic rendering only where requested.
The owner then curated every realm: each keeps two to four wallpapers in a
chosen order, the first being its preview. Wallpapers left out are marked
removed in their batch manifest with their prompts kept, and their exports and
native sources are deleted.

`artwork-batch-07.json` records each rendering style, exact written prompt,
native source dimensions and hashes, and crop offsets. No reference images
were used. Original compositions and characters contain no readable lettering,
logos or third-party likenesses. Sources and `export.py` live under
`branding/sources/wallpapers/batch-07/`; exports are 3840×2160 and 3440×1440
JPEGs, resampled from the recorded native sizes rather than native 4K detail.
Seven separately composed panoramic masters preserve subjects where a crop
would lose them; other ultrawides use recorded subject-preserving crops.
The soul gate uses its panoramic master for both exports. No stretching or
padding is used. Selected artwork has passed agent visual inspection and
remains available for owner review.

## Ragnarök — Batch 08

Three owner-approved painterly dark fantasy wallpapers lead Ragnarök's four-image
set: Blood Eclipse, Fenrir Devours the Sun and Dying Yggdrasil, followed by World
Tree Pyre from batch 06. The owner explicitly permits scenic and painterly
rendering for batch 08. Written briefs only, without reference images.

`artwork-batch-08.json` records the exact prompts for both aspect ratios, rendering
style, native dimensions, hashes and centering. Six native PNGs and `export.py`
live under `branding/sources/wallpapers/batch-08/`. The 16:9 masters are preserved
byte-for-byte; new 1935×812 panoramic compositions preserve complete subjects and
calm dark space. Crop-to-fill exports are 3840×2160 and 3440×1440 JPEGs without
stretching or padding.

## Realm curation — Batch 13

Svartalfheim starts with Feasting Hall, followed by Hammer Warriors and Forge
Canyon. The owner-approved hall uses the fjords' ink cel-shaded vector style,
bold contours, flat warm colours and a scenic carved interior. Its preview uses Feasting Hall. Asgard retains Radiant Citadel, Bifrost Hall and
Storm Bridge (now 03); Cloud Fortress and Cavern City are retired.

`themes/artwork-batch-13.json` below this directory records the three supplied prompts verbatim,
the original dwarfs-b.png edit input (provenance only, not distributed), and
style-fjord-c.png as the owner-approved batch 12 Eitr dusk fjord master.
Two native PNGs live in
`branding/sources/wallpapers/batch-13/`. Centred Lanczos exports preserve the
table and round door at 3840×2160 and 3440×1440, using the separately generated
panorama without stretching or padding; these are not native 4K detail.
Retired records retain their prompts and hashes; unused native sources are removed.
