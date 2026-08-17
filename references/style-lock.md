# Style Lock — Cross-Session Portability

This file exists to make Photo Decode behave consistently in a fresh conversation with **no prior visual coaching**.

## The portability failure this prevents

A fresh model may over-interpret the words `flat`, `simplified`, `key elements`, or `graphic` and produce:
- generic SVG/vector illustration;
- UI-style pictograms;
- a uniform icon set;
- logo-like symbols;
- overly minimal geometric shapes.

That is **not** Photo Decode.

## Photo Decode visual target

Photo Decode is best understood as:

> **information-rich source → selective extraction → structural compression → background removal → editorial flattening → a new visual object**

The word `flat` is about **depth and information hierarchy**, not about destroying visual richness.

The right visual can be detailed when the source is detailed. Retain enough specific structure that a viewer can trace the new image back to the source through architecture, posture, ornament, gesture, pattern, massing, rhythm, or repeated motifs.

## KEY ELEMENTS target

KEY ELEMENTS are **miniature extracted visual fragments** from the right visual.

Think:
- a small carved architectural section;
- a miniature figure with its retained costume/shape language;
- a roof/eave fragment;
- a gesture/hand cluster;
- a structural module;
- a selected ornamental motif;
- a cropped object part.

Do not think:
- app icon;
- SVG icon;
- Material icon;
- line icon;
- pictogram;
- logo;
- emoji;
- generic symbol.

The elements should often have **different silhouettes and different levels of internal detail**, because they come from different parts of the reinterpreted visual.

## Rendering character

- editorial / museum-study quality;
- warm ivory paper;
- precise but not sterile;
- flat planes plus selected internal line/pattern/detail;
- source-specific complexity preserved selectively;
- no forced uniform stroke width;
- no forced rounded geometry;
- no icon containers;
- no generic circle/arc/blob balancing devices.

## Visual reference asset

If the runtime/tool can use local visual references, inspect:

`assets/golden-key-elements-reference.png`

The reference demonstrates the desired difference:
the elements are miniature, source-specific pieces of the reinterpreted world — not an SVG icon library.

## Final portability question

Before presenting, ask:

> If this board were generated in a brand-new session with no prior context, would KEY ELEMENTS still look like pieces of Block 2 rather than icons designed separately?

If not, regenerate.
