# Changelog

## 2.0.0 — stable architecture rewrite

Clean rewrite of Photo Decode after cold-start portability failures in v1.x.

### Removed architectural shortcuts

- fixed-medium / engraving-style drift;
- ambiguous `icon-like/glyph-like` KEY ELEMENT guidance;
- crop/cutout KEY ELEMENT behavior;
- extra analytical block drift.

### Added

- Visual Structure Ledger;
- source-adaptive reconstruction model;
- explicit anti-filter gate;
- KEY ELEMENTS visual-grammar reconstruction protocol;
- pixel-independence / grammar / teaching tests;
- cold-start portability gate;
- cross-image style diversity evaluation;
- multi-category golden behavior reference.
