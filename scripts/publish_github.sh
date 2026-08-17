#!/usr/bin/env bash
set -euo pipefail

OWNER="Cloudlake110"
REPO="photo-decode"
DESC="Photo Decode 解图 — turn any image into a five-block editorial visual deconstruction and flat reinterpretation board."

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it first: https://cli.github.com/"
  exit 1
fi

if ! gh auth status --hostname github.com >/dev/null 2>&1; then
  echo "Opening GitHub in your browser for authorization..."
  gh auth login --hostname github.com --git-protocol https --web
fi

gh auth setup-git

if [ ! -d .git ]; then
  git init -b main
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "Release Photo Decode v1.0.0"
fi

if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$OWNER/$REPO.git"
  fi
  git push -u origin main
else
  gh repo create "$OWNER/$REPO" --public --description "$DESC" --source=. --remote=origin --push
fi

echo "Published: https://github.com/$OWNER/$REPO"
