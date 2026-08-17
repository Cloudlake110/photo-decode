#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo "Photo Decode · GitHub Publisher"
echo "Repository: Cloudlake110/photo-decode"
echo

if ! command -v gh >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "GitHub CLI is not installed. Installing with Homebrew..."
    brew install gh
  else
    echo "GitHub CLI is not installed and Homebrew was not found."
    echo "Install GitHub CLI from https://cli.github.com/ then run this file again."
    read -r -p "Press Enter to close..."
    exit 1
  fi
fi

./scripts/publish_github.sh

echo
read -r -p "Done. Press Enter to close..."
