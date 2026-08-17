---
name: photo-decode
description: Turn an uploaded image into a fixed five-block editorial analysis board: original source, background-free flat reinterpretation, image essence, color palette derived only from the reinterpretation, and key elements derived only from the reinterpretation. Use for photos, paintings, portraits, news scenes, landscapes, groups, architecture, interiors, products, retail displays, and other visual references when the user wants a high-end editorial visual deconstruction and reconstruction.
---

# Photo Decode · 解图

**Tagline:** 一张图，解出另一种视觉。 / Decode one image into another visual language.

## Core outcome

Create one polished **3:2 landscape editorial analysis board** with exactly five titled blocks:

1. **ORIGINAL SOURCE**
2. **REINTERPRETED VISUAL (FLAT)**
3. **IMAGE ESSENCE**
4. **COLOR PALETTE**
5. **KEY ELEMENTS**

The five blocks are a dependency chain, not five independent analyses:

`ORIGINAL SOURCE → REINTERPRETED VISUAL (FLAT) → COLOR PALETTE + KEY ELEMENTS`

`IMAGE ESSENCE` explains the visual logic of the source and the reinterpretation.

## Non-negotiable transformation rule

The right-side visual is **not** a copy, filter, tracing, vectorization, or lightly stylized version of the original.

It must follow this sequence:

**complex information → extract → select → compress → remove photographic background → flatten → reorganize → new visual object**

The result must feel visibly new while remaining traceable to the source.

### Right panel must

- identify the visual/narrative anchor first;
- preserve the minimum identity-defining shapes and relationships needed for recognition;
- remove incidental environment, clutter, photographic depth, texture noise, realistic lighting, reflections, and non-essential secondary objects;
- compress three-dimensional volume into a two-dimensional graphic language;
- use clean silhouettes, flat color planes, simplified internal structure, controlled line rhythm, and restrained tonal separation;
- preserve important left/right, top/bottom, scale, direction, overlap, repetition, and hierarchy relationships when they are identity-defining;
- create strong visual impact through simplification, not through invented decoration;
- contain **no unsupported circles, arches, waves, blobs, grids, suns, dots, or ornamental geometry** unless that form is traceable to the retained subject structure.

### Background rule

For portraits, products, groups, architecture, news scenes, objects, interiors, and displays: **remove the photographic background completely** from the right visual.

For landscapes or paintings where the environment is itself the subject: remove the **photographic/painterly backdrop quality**. Retain only identity-defining environmental layers as simplified flat subject planes (for example: mountain ridge, sea band, village mass), never as a realistic background.

## Five-block contract

### 1. ORIGINAL SOURCE

- Use the uploaded image as the source reference.
- Preserve the source faithfully; do not redraw, extend, repair, beautify, or invent content.
- Keep it legible and visually dominant enough for before/after comparison.

### 2. REINTERPRETED VISUAL (FLAT)

This is the design engine of the board.

Before rendering, internally create a short **Source → Retained Feature → Flat Treatment** ledger. Do not display the ledger unless requested.

Example:

- ornate carved column → vertical silhouette + selected floral rhythm → flat ivory/stone bands
- stepped tower → narrowing stacked tiers → simplified gold planes
- portrait hair → irregular outer contour → one dark flat mass
- group interaction → primary figure + supporting arc → hierarchy of 1 hero / 2 support silhouettes

Every major retained feature must have a source justification. Every major new mark must have a retained-feature justification.

### 3. IMAGE ESSENCE

Include:

- one concise editorial title;
- optional short subtitle;
- a short paragraph (roughly 35–80 English words or equivalent Chinese length) explaining what visually defines the image and what the flat reinterpretation preserves.

Rules:

- describe visible structure, rhythm, contrast, gesture, hierarchy, or atmosphere;
- avoid generic AI copy such as “timeless beauty”, “quiet elegance”, “where art meets…” unless truly specific;
- do not invent dates, locations, identities, brands, historical claims, or relationships not supplied by the user;
- for news images, describe visible action and visual tension without identifying people or asserting unprovided event facts;
- for portraits, never infer or name a real person from the image alone. Use a user-provided identity only if the user supplied it.

### 4. COLOR PALETTE

**Critical dependency:** derive the palette from **REINTERPRETED VISUAL (FLAT)** only — never directly from ORIGINAL SOURCE.

- show 5–8 swatches; default 6;
- exclude the board paper color from the palette unless that color is deliberately part of the right visual;
- keep colors visibly distinct and useful;
- put a readable uppercase HEX code under **every** swatch, e.g. `#C8B59A`;
- no swatch may be unlabeled.

If a source color was removed during reinterpretation, it must not reappear merely because it existed in the original.

### 5. KEY ELEMENTS

**Critical dependency:** derive the key elements from **REINTERPRETED VISUAL (FLAT)** only — never directly from ORIGINAL SOURCE.

- show 4–6 simplified icon-like/glyph-like elements;
- use the same flat visual language and palette as the right visual;
- each element must correspond to a retained component in the right visual;
- do not include any background element that was removed;
- do not introduce a new object just because it was visible in the original source;
- use concise labels under the elements when labels improve clarity.

## Fixed editorial layout

Read `references/layout-spec.md` before rendering.

Default visual system:

- canvas: 3:2 landscape, e.g. 1536×1024;
- warm ivory / off-white paper base;
- generous margins and disciplined grid;
- thin hairline dividers;
- small uppercase sans/mono block labels;
- editorial serif display title + clean sans body;
- no glossy UI cards, no neon, no generic AI gradient, no excessive drop shadows;
- premium museum/editorial-board feeling, not a corporate slide and not a scrapbook.

## Scene routing

Read `references/scene-routing.md` and apply the matching branch.

Important hierarchy rules:

- **single portrait:** retain 3–5 identity-defining visual features; remove setting;
- **group/crowd:** do not flatten everyone equally; select a hero, support, and tertiary layer;
- **news scene:** extract the visible action/conflict axis; background and witnesses are secondary unless structurally necessary;
- **landscape:** preserve large spatial topology and color masses, but convert scenery to flat subject layers;
- **product/display:** preserve product hierarchy, arrangement rhythm, and hero/support relationships; remove retail/environment clutter;
- **architecture/interior:** preserve defining structural modules, axes, apertures, and circulation rhythm; remove incidental people/details unless crucial;
- **painting/artwork:** preserve composition and motifs while converting painterly information into a fresh flat visual language; do not add motifs not present in the source.

## Generation workflow

1. Inspect the source image.
2. Classify the scene type.
3. Identify the visual anchor and supporting hierarchy.
4. List the minimum retained features.
5. Decide what background/context is deleted.
6. Construct the flat reinterpretation.
7. Derive the palette **from the flat reinterpretation**.
8. Derive key elements **from the flat reinterpretation**.
9. Write the image essence.
10. Compose the five-block board.
11. Run every gate in `references/quality-gates.md`.
12. If any hard gate fails, regenerate/fix before presenting.

## Hard failure conditions

Do not present the result as final if any of these are true:

- one of the five block titles is missing;
- the right visual still looks like a copied photograph or a lightly filtered source;
- the right visual retains an incidental photographic background;
- the palette was visibly inherited from colors removed from the right visual;
- any palette swatch lacks a HEX label;
- KEY ELEMENTS contains background/context removed from the right visual;
- KEY ELEMENTS is derived independently from the source rather than from the right visual;
- all figures in a crowd are treated equally when a clear hierarchy exists;
- generic circles/blobs/arches/waves appear without traceable justification;
- invented dates, identities, locations, relationships, or historical claims appear;
- the fixed five-block framework is replaced by a different moodboard/template.

## Reference files

- `references/layout-spec.md` — fixed five-block layout and typography
- `references/transformation-pipeline.md` — flat reinterpretation method
- `references/scene-routing.md` — rules by image type
- `references/quality-gates.md` — preflight and final validation
- `references/prompt-template.md` — image generation prompt compiler

## Output behavior

When the user provides an image and asks to use Photo Decode/解图, proceed directly unless essential information is missing. Generate the final board rather than stopping at a prose explanation.
