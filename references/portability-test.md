# Cold-Start Portability Test

The Skill is considered portable only when it reproduces correct behavior in a clean session with no historical conversation context.

## Procedure

1. Open a new conversation/session.
2. Install/load Photo Decode V2 from the repository only.
3. Do not provide extra style explanation.
4. For each input, say only: `调用解图 / Use Photo Decode on this image.`
5. Evaluate against [`quality-gates.md`](quality-gates.md).

## Required categories

At minimum:

- portrait;
- ornate cultural/religious scene;
- dynamic action or news scene;
- city/architecture;
- group/crowd;
- painting/artwork.
- landscape;
- product/retail display.

## Cross-image style diversity check

Compare at least four Block 2 outputs. Fail if they all converge on the same medium, texture, hatch, contour treatment or illustration genre when sources are unrelated.

## KEY ELEMENTS check

Fail if elements look like crops, cutouts, screenshots or a generic icon library. Pass only when they are independent visual grammar reconstructions.
