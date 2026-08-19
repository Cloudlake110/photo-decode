# Photo Decode / 解图

**一张图，解出另一种视觉。**

**Search aliases:** `Photo Decode` · `PhotoDecode` · `photo-decode` · `解图`

Photo Decode is a portable Agent Skill for visual analysis and structural image decoding. It uses the `SKILL.md` format so compatible AI environments can install and run it without requiring Codex.

It supports photographs, paintings, portraits, landscapes, architecture, products, animals and action scenes. Its visual reconstruction and image generation workflow is source-adaptive, not a style filter.

Its signature pipeline is:

> **analyze structure → choose what matters → remove background → compress relations → reconstruct a source-adaptive flat visual → derive palette → reconstruct key visual grammar**

## Why V2 exists

V1 exposed two portability failures in clean sessions:

1. unrelated inputs could collapse into one engraving/printmaking look;
2. `KEY ELEMENTS` could degrade into crops/cutouts instead of meaningful visual abstractions.

V2 removes both shortcuts from the architecture itself.

## Fixed five-block board

1. `ORIGINAL SOURCE`
2. `REINTERPRETED VISUAL (FLAT)`
3. `IMAGE ESSENCE`
4. `COLOR PALETTE`
5. `KEY ELEMENTS`

## Example gallery

See the [eight-case V2 regression gallery](examples/v2-regression/README.md) for side-by-side source images and completed Photo Decode boards across documentary scenes, group gesture, landscape, artwork, animals, sports/action and ornate architecture.

| Documentary / group action | Ornate architecture |
| --- | --- |
| [![Load-Bearing Flow](examples/v2-regression/assets/01-bridge-board.png)](examples/v2-regression/README.md#01--load-bearing-flow) | [![Rings Upon an Axis](examples/v2-regression/assets/08-rings-upon-axis-board.png)](examples/v2-regression/README.md#08--rings-upon-an-axis) |

## What “flat” means

Flat means **structural depth and information are compressed**. It does not mean every source becomes a minimal vector drawing.

An ornate temple may stay richly articulated. A portrait may become restrained. A city may preserve dense roofline rhythm. A sports image may preserve collision/action geometry. The visual language follows the source.

## KEY ELEMENTS in V2

KEY ELEMENTS are **independently reconstructed visual grammar units**. They are not crops, screenshots, masks or generic icons.

They answer: *what forms, relations, rhythms, junctions, gestures or motifs make this image visually itself?*

## Cold-start reliability

V2 includes a mandatory cold-start test. A release fails if a clean new session:

- applies one fixed art style across unrelated inputs; or
- turns KEY ELEMENTS into crops/icons.

See `references/portability-test.md`.

## Golden behavior reference

See `assets/golden-behavior-reference.png`. It demonstrates **behavioral diversity**, not one style to imitate.

## Install and use

If your AI supports installing Agent Skills, send it this instruction:

```text
Please install and use Photo Decode / 解图 from this GitHub repository:
https://github.com/Cloudlake110/photo-decode
```

The repository root is the complete Skill package. A compatible AI can download it, detect `SKILL.md`, install the `photo-decode` Skill and use it immediately. Codex is one supported host, not a prerequisite.

If your AI requires a file or folder upload instead of a repository URL, download the repository and add the repository root as one Skill.

### Optional manual installation in Codex

```bash
git clone https://github.com/Cloudlake110/photo-decode.git ~/.codex/skills/photo-decode
```

Start a new Codex session if the Skill does not appear immediately.

## Use after installation

Upload an image and say:

```text
调用“解图 / Photo Decode”处理这张图片。
```

or:

```text
Use Photo Decode on this image.
```

## Version

**v2.0.0 — stable architecture rewrite.**

## License

Source-available for personal, educational, research, and other non-commercial use. See [`LICENSE.md`](LICENSE.md) and [`NOTICE.md`](NOTICE.md).
