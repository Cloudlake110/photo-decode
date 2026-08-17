# Photo Decode v1.0.0 — Release Notes

**Release date:** 2026-08-17  
**Codename:** 解图 / Photo Decode  
**Status:** Stable first public release candidate

## What Photo Decode does

Photo Decode turns a source image into a fixed five-block editorial analysis board. Its signature move is the second block: a **background-free flat reinterpretation** created by extracting, selecting, compressing and reorganizing the source image into a new graphic object.

## Locked v1.0 behaviors

- Exactly five titled blocks.
- `REINTERPRETED VISUAL (FLAT)` is not a filter, tracing, vector copy, or light stylization.
- Photographic/painterly background is removed; meaningful environmental structure is retained only as flat subject layers when necessary.
- `COLOR PALETTE` is derived only from the reinterpreted visual.
- Every palette swatch carries a readable HEX value.
- `KEY ELEMENTS` are derived only from the reinterpreted visual.
- Removed background/context cannot return as a key element.
- Group/news images use visual hierarchy rather than equal treatment of every figure.
- Unsupported generic circles, blobs, arches, waves or grids are rejected unless traceable to source structure.
- Text avoids invented identity, location, date, event fact or human relationship.

## Stability-test coverage

v1.0 was iterated across:

- portraits
- group portraits
- complex news/documentary scenes
- high-saturation landscapes
- paintings/artworks
- architecture/interiors
- products and retail displays
- strong graphic/advertising images

## Public gallery

The repository ships only five selected recent examples to keep the release lightweight:

- portrait
- saturated landscape
- complex news scene
- group portrait
- retail/product display

## Rights / licensing

Photo Decode is published as source-available for personal, educational, research and non-commercial use. It is not presented as OSI open source because the current license includes non-commercial restrictions. Third-party source images embedded in examples retain their own rights.

See `LICENSE.md` and `NOTICE.md`.

## Next

Planned v1.1 focus:

- broader edge-case evals
- more deterministic hierarchy selection
- improved flat-reinterpretation consistency across image models
- RED Skill packaging and distribution
- replacement of any public example whose source redistribution rights are unclear
