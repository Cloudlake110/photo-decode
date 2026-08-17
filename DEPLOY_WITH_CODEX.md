# Deploy Photo Decode v1.0.0 with Codex

Target repository: `https://github.com/Cloudlake110/photo-decode`

## Goal

Replace the temporary mobile-upload layout with this complete repository tree and publish a clean `main` branch.

## Codex execution checklist

1. Inspect this folder and read `SKILL.md`, `README.md`, `README.zh-CN.md`, `NOTICE.md`, `LICENSE.md`, and `references/`.
2. Run:
   ```bash
   python3 scripts/validate_skill.py
   ```
   Stop if validation does not print `PASS`.
3. Clone the current repository into a temporary directory:
   ```bash
   git clone https://github.com/Cloudlake110/photo-decode.git /tmp/photo-decode-github
   ```
4. Preserve `/tmp/photo-decode-github/.git`, but replace the repository working tree with the contents of this release folder.
5. Explicitly remove mobile-bootstrap leftovers if present:
   - `UPLOAD-INSTRUCTIONS.txt`
   - `photo-decode-mobile-upload.zip`
   - `PHOTO-DECODE-SHOWCASE.png` (the five individual gallery cases now replace it)
6. Confirm the repository contains:
   - `SKILL.md`
   - `README.md`
   - `README.zh-CN.md`
   - `references/`
   - `evals/`
   - `agents/`
   - `assets/`
   - `scripts/`
   - `examples/gallery/` with exactly five selected PNG boards
7. Run `python3 scripts/validate_skill.py` again from the cloned repository.
8. Commit:
   ```bash
   git add -A
   git commit -m "feat: publish complete Photo Decode v1.0.0 repository"
   git push origin main
   ```
9. If GitHub authentication is required, use browser-based authentication. Do not ask the user to paste a personal access token into chat.
10. If GitHub CLI is available, create tag `v1.0.0` and a GitHub Release using `RELEASE_NOTES.md`. If `gh` is unavailable, leave tag/release creation for later; do not block the repository sync.
11. Final verification:
   - GitHub root README renders
   - `SKILL.md` opens
   - `references/quality-gates.md` opens
   - five example images render
   - no mobile bootstrap artifacts remain
   - report final commit SHA
