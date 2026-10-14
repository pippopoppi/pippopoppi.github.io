#!/usr/bin/env bash
# Commit everything and push to GitHub Pages (user site: branch main, root).
set -euo pipefail
cd "$(dirname "$0")/.."
git add -A
git commit -m "${1:-Update}" || true
git push origin main
echo "Live in ~1 min: https://pippopoppi.github.io/"
