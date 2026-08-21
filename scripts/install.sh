#!/usr/bin/env bash
# Lightweight gate: share code, then install into Cursor (or first arg agent).
# npx skills add itself has no password. This wrapper is what you send friends
# after they clone (or after GitHub access on a private repo).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AGENT="${1:-cursor}"
python3 "$ROOT/scripts/unlock.py"
npx --yes skills add "$ROOT" -g -a "$AGENT"
echo "Installed ghost-qbo for $AGENT. In chat: attach QBO for this client"
