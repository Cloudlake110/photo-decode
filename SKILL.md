---
name: photo-decode
description: Analyze an uploaded image, reconstruct its visual logic into a source-adaptive background-free flat composition, then derive a palette and independently redrawn key visual elements. Use when the user asks to 解图 / Photo Decode a photo, painting, news scene, portrait, group, landscape, architecture, product, retail display, animal, sports/action scene, or other visual reference.
---

# Photo Decode V2 · 解图

**Core promise:** 一张图，解出另一种视觉。

**System identity:** visual analysis + structural distillation + source-adaptive reconstruction.
**It is NOT:** a filter, a named art style, a tracing/vectorization routine, a crop extractor, or an icon generator.

## Mandatory cold-start rule

Before the first render in a session, read these files in order:

1. `references/core-model.md`
2. `references/reconstruction-protocol.md`
3. `references/key-elements-protocol.md`
4. `references/layout-spec.md`
5. `references/scene-routing.md`
6. `references/quality-gates.md`
7. `references/prompt-compiler.md`
8. `assets/golden-behavior-reference.png`

Do not rely on prior chat history. The Skill must work in a clean session.

## Fixed output contract

Create exactly one **3:2 landscape editorial board** with exactly five numbered blocks:

1. **ORIGINAL SOURCE**
2. **REINTERPRETED VISUAL (FLAT)**
3. **IMAGE ESSENCE**
4. **COLOR PALETTE**
5. **KEY ELEMENTS**

No sixth analytical block. Do not rename these labels.

The dependency graph is strict:

`ORIGINAL SOURCE → ANALYSIS MODEL → REINTERPRETED VISUAL → COLOR PALETTE + KEY ELEMENTS`

`IMAGE ESSENCE` explains the visual logic discovered by the analysis model.

## The two-stage intelligence model

### Stage A — Visual analysis (must happen before drawing)

Internally build a **Visual Structure Ledger** with these fields:

- **Anchor:** the primary visual/narrative subject or relation.
- **Hierarchy:** hero / support / tertiary groups.
- **Spatial grammar:** scale, direction, overlap, symmetry/asymmetry, repetition, rhythm, axes.
- **Identity cues:** the minimum forms needed for recognition.
- **Tension / action:** gesture, force, flow, gaze, contact, weight, motion, conflict.
- **Keep:** structures that must survive.
- **Delete:** incidental background, texture, clutter, realism and context that can disappear.
- **Source-style cues:** line character, shape logic, ornament density, material rhythm, color relationships that actually belong to this image.
- **Key-element candidates:** 4–6 visual grammar units that explain why the final reconstruction is recognizable.

Do not display this ledger unless the user asks.

### Stage B — Visual reconstruction

Build a new two-dimensional composition from the ledger.

The reconstruction must:

- remove photographic/painterly background as background;
- preserve identity-defining relationships, not every pixel;
- compress complexity without flattening all images to the same complexity level;
- preserve meaningful ornament, rhythm, anatomy, architecture or equipment when those are identity-defining;
- use flat planes, controlled contours, selected internal detail and limited tonal hierarchy;
- remain recognizably derived from the source while looking like a newly designed visual object.

## Source-adaptive style rule — HARD

**There is no default Photo Decode art style.** The board layout is consistent; the reconstructed visual is source-adaptive.

Do NOT default unrelated inputs to any fixed medium or look, including:

- engraving / etching / woodcut / linocut;
- comic / anime / posterized illustration;
- generic vector iconography;
- one universal contour style;
- one universal texture or hatch pattern;
- one universal geometric abstraction language.

A named style is allowed only when the user explicitly requests it or when it is genuinely derived from the source artwork's own visual language.

`FLAT` means **depth and information are structurally compressed**. It does not mean “turn everything into simple SVG shapes.”

## Block rules

### 1. ORIGINAL SOURCE

Use the uploaded source faithfully. Do not beautify, repair, extend or reinterpret this block.

### 2. REINTERPRETED VISUAL (FLAT)

This is the primary design output.

It must be:

- a reconstruction, not a filter;
- background-free in photographic terms;
- source-adaptive, not medium-templated;
- compressed but not generically simplified;
- coherent as a standalone composition;
- faithful to important spatial/action relationships.

**Anti-cheat test:** If the right visual could be produced by applying one named style/filter to the source, it fails.

### 3. IMAGE ESSENCE

Include:

- one concise editorial title;
- optional short subtitle or 2–4 keywords;
- 35–80 English words or equivalent Chinese explaining the structural visual logic.

Describe visible structure, rhythm, relation, gesture, tension, hierarchy and atmosphere. Do not invent identity, date, location, event facts, brand, relationship or history not supplied by the user.

### 4. COLOR PALETTE

Derive **only from the completed REINTERPRETED VISUAL**.

- 5–8 swatches; default 6.
- Every swatch must have a readable uppercase HEX value.
- Do not reintroduce source colors that were intentionally removed.
- Do not include the board paper color unless it is intentionally part of the reconstructed visual.

### 5. KEY ELEMENTS

KEY ELEMENTS are **not crops and not icons**.

They are 4–6 **independently reconstructed visual grammar units** that help a viewer understand what makes the image visually recognizable or structurally distinctive.

Each element must be freshly redrawn/recomposed from the analysis ledger and the right-side reconstruction. It may represent:

- a signature form;
- a structural junction;
- a relation between forms;
- a repeated rhythm/pattern;
- a gesture/action unit;
- an identifying object architecture;
- a distinctive contour or motif.

A KEY ELEMENT must NOT be:

- a rectangular crop or screenshot;
- a zoomed detail;
- a masked cutout copied from the right visual;
- raw segmentation;
- a generic SVG/UI icon;
- a pictogram family forced into one line weight.

**Reconstruction test:** if an element visibly contains the same pixel texture or exact local rendering as the right visual, treat it as a crop and redraw it.

**Insight test:** every element should teach the viewer something about the image's visual grammar that is not obvious from a simple crop.

## Generation workflow

1. Read mandatory reference files and golden reference.
2. Inspect source.
3. Classify scene type.
4. Build Visual Structure Ledger.
5. Select source-adaptive reconstruction logic.
6. Construct Block 2.
7. Run the anti-filter gate.
8. Derive Block 4 from Block 2.
9. Reconstruct Block 5 from the ledger + Block 2; never crop.
10. Write Block 3.
11. Compose fixed five-block board.
12. Run all gates in `references/quality-gates.md`.
13. If any hard gate fails, fix/regenerate before presenting.

## Hard stop conditions

Do not present as final if:

- block names/layout drift;
- right visual is a fixed-style transformation or filter;
- unrelated inputs would plausibly receive the same texture/medium;
- right visual is only a traced/vectorized source;
- incidental background survives as realistic scenery;
- meaningful source structure has been over-simplified merely to look “flat”;
- palette comes from source instead of reconstruction;
- any HEX value is missing;
- KEY ELEMENTS are crops, screenshots, masked cutouts or generic icons;
- KEY ELEMENTS do not explain visual grammar;
- invented factual claims appear.

## Output behavior

When the user uploads an image and asks to call 解图 / Photo Decode, proceed directly to the final board unless essential input is genuinely missing.
