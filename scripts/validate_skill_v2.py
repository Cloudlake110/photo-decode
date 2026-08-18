#!/usr/bin/env python3
from pathlib import Path
import json, re, struct, sys

ROOT=Path(__file__).resolve().parents[1]
required=[
 'SKILL.md','README.md','README.zh-CN.md','agents/openai.yaml',
 'references/core-model.md','references/reconstruction-protocol.md',
 'references/key-elements-protocol.md','references/layout-spec.md',
 'references/scene-routing.md','references/quality-gates.md',
 'references/prompt-compiler.md','references/portability-test.md',
 'evals/cases.json','evals/portability.json','assets/golden-behavior-reference.png'
]
missing=[p for p in required if not (ROOT/p).exists()]
if missing:
 print('FAIL missing files:', *missing, sep='\n- '); sys.exit(1)

skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
frontmatter_match=re.match(r'^---\n(.*?)\n---', skill, re.DOTALL)
if not frontmatter_match:
 print('FAIL invalid SKILL.md frontmatter'); sys.exit(1)
frontmatter_lines=[line for line in frontmatter_match.group(1).splitlines() if line.strip()]
frontmatter_keys={line.split(':', 1)[0].strip() for line in frontmatter_lines if ':' in line}
if frontmatter_keys != {'name','description'}:
 print('FAIL SKILL.md frontmatter keys:', *sorted(frontmatter_keys), sep='\n- '); sys.exit(1)

required_phrases=[
 'There is no default Photo Decode art style',
 'KEY ELEMENTS are **not crops and not icons**',
 'Visual Structure Ledger',
 'Reconstruction test',
 'Insight test',
 'Cold-start portability gate',
]
# One phrase lives in quality gates, validate full reference corpus too.
corpus='\n'.join(p.read_text(encoding='utf-8') for p in [ROOT/'SKILL.md', ROOT/'references/quality-gates.md', ROOT/'references/key-elements-protocol.md'])
not_found=[x for x in required_phrases if x not in corpus]
if not_found:
 print('FAIL required V2 rule missing:', *not_found, sep='\n- '); sys.exit(1)

evals_data=json.loads((ROOT/'evals/cases.json').read_text(encoding='utf-8'))
portability_data=json.loads((ROOT/'evals/portability.json').read_text(encoding='utf-8'))
if evals_data.get('version') != '2.0.0' or portability_data.get('version') != '2.0.0':
 print('FAIL eval version mismatch'); sys.exit(1)

required_cases={'portrait','ornate','city','action','crowd','artwork','landscape','product_display','global'}
case_ids={case.get('id') for case in evals_data.get('cases', [])}
missing_cases=sorted(required_cases-case_ids)
if missing_cases:
 print('FAIL missing eval cases:', *missing_cases, sep='\n- '); sys.exit(1)

required_categories=set(portability_data.get('required_categories', []))
if not {'landscape','product_display'}.issubset(required_categories):
 print('FAIL portability categories missing landscape/product_display'); sys.exit(1)

openai_yaml=(ROOT/'agents/openai.yaml').read_text(encoding='utf-8')
for marker in ['interface:','display_name:','short_description:','default_prompt:','\u0024photo-decode']:
 if marker not in openai_yaml:
  print('FAIL agents/openai.yaml missing:', marker); sys.exit(1)

golden=ROOT/'assets/golden-behavior-reference.png'
with golden.open('rb') as f:
 header=f.read(24)
if len(header) < 24 or header[:8] != b'\x89PNG\r\n\x1a\n':
 print('FAIL invalid golden PNG'); sys.exit(1)
width,height=struct.unpack('>II', header[16:24])
if width < 1000 or height < 800:
 print('FAIL golden reference dimensions'); sys.exit(1)

# Ensure V1 ambiguity is not reintroduced as positive guidance.
forbidden_positive=[
 'simplified icon-like/glyph-like elements',
 'simplified icon-like elements from the reinterpreted visual only'
]
for phrase in forbidden_positive:
 if phrase in corpus:
  print('FAIL legacy ambiguity found:', phrase); sys.exit(1)

print('PASS Photo Decode V2 static package checks: architecture, metadata, eval coverage, and golden reference')
