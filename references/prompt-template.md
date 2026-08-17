# Prompt Compiler Template

Use this as the default image-generation instruction structure.

## Role

Create a high-end 3:2 editorial analysis board called **Photo Decode / 解图** from the uploaded source image.

## Fixed layout

Render exactly five titled blocks:

1. ORIGINAL SOURCE
2. REINTERPRETED VISUAL (FLAT)
3. IMAGE ESSENCE
4. COLOR PALETTE
5. KEY ELEMENTS

Use a warm ivory paper background, thin editorial dividers, disciplined grid, small uppercase block labels, serif editorial headline, clean sans body.

## Source block

Keep the uploaded source image faithful and recognizable. Do not redraw or alter its content.

## Reinterpreted visual block

Analyze the source and identify the main visual anchor and support hierarchy. Create a new flat visual object by:

- extracting the minimum identity-defining features;
- deleting incidental background and clutter;
- compressing detail selectively;
- reducing photographic/painterly depth and texture without erasing source-specific visual identity;
- converting form into flat color planes and clear silhouettes while retaining selected internal ornament, pattern, contour breaks, line hierarchy, and material cues when important;
- preserving identity-defining spatial/gesture/hierarchy relationships;
- avoiding unsupported decorative geometry;
- making the result feel new, graphic, editorial, and high-impact, not copied.

### Critical style lock

`FLAT` does **not** mean generic vector minimalism.

Do not make the right panel look like:
- an SVG illustration;
- a corporate vector infographic;
- a UI icon system;
- a logo/pictogram treatment;
- a uniform-stroke line-art set;
- a generic geometric poster template.

Information-rich sources are allowed to remain richly articulated after flattening. The desired result is a **premium editorial illustration / museum design study** with selective detail, not a stripped-down icon.

## Image essence

Write a specific editorial title and short description focused on visual structure, rhythm, contrast, gesture, hierarchy, or atmosphere. Do not invent identities, dates, locations, relationships, or event facts.

## Color palette

Extract 5–8 colors from the **reinterpreted visual only**. Show a readable uppercase HEX code directly below every swatch. Do not derive the palette from the original source.

## Key elements

Extract 4–6 **miniature visual fragments** from the **reinterpreted visual only**.

Each key element must:
- feel like a small isolated fragment cut from / recomposed from the right-panel visual;
- retain the same drawing character, line hierarchy, internal detail, ornament/pattern, and palette;
- preserve its own natural silhouette and proportion;
- correspond to something actually retained in the right visual.

Do **not** normalize the elements into one icon family. Do **not** turn them into SVG symbols, line icons, pictograms, logos, emoji-like shapes, or generic UI glyphs. Different elements may have different complexity and silhouettes because they come from different parts of the right visual.

Do not include background/context removed from the right visual.

## Final negatives

No copied/photo-filtered right panel. No photographic background in the right panel. No generic vector/SVG aesthetic. No UI icon set. No pictogram family. No generic AI blobs/circles/waves/arcs unless traceable to retained structure. No unlabeled swatches. No background elements in KEY ELEMENTS after background removal. No fake dates, locations, identities, or metadata. No missing block titles. No sixth block. No generic moodboard or corporate presentation style.
