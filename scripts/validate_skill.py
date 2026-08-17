#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "NOTICE.md",
    "LICENSE.md",
    "agents/openai.yaml",
    "references/layout-spec.md",
    "references/transformation-pipeline.md",
    "references/scene-routing.md",
    "references/quality-gates.md",
    "references/prompt-template.md",
    "references/style-lock.md",
    "evals/evals.json",
    "evals/style-portability.json",
    "assets/layout-spec.svg",
    "assets/golden-key-elements-reference.png",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("FAIL missing files:", *missing, sep="\n- ")
    sys.exit(1)

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
needles = [
    "1. **ORIGINAL SOURCE**",
    "2. **REINTERPRETED VISUAL (FLAT)**",
    "3. **IMAGE ESSENCE**",
    "4. **COLOR PALETTE**",
    "5. **KEY ELEMENTS**",
    "HEX code under **every** swatch",
    "derive the palette from **REINTERPRETED VISUAL (FLAT)** only",
    "derive the key elements from **REINTERPRETED VISUAL (FLAT)** only",
]
not_found = [n for n in needles if n not in skill]
if not_found:
    print("FAIL required rule missing:", *not_found, sep="\n- ")
    sys.exit(1)

with (ROOT / "evals/evals.json").open(encoding="utf-8") as f:
    data = json.load(f)
if data.get("skill") != "photo-decode" or len(data.get("cases", [])) < 8:
    print("FAIL eval manifest")
    sys.exit(1)

print("PASS photo-decode skill structure and locked rules")
