#!/usr/bin/env python3
"""Share-code gate for ghost-qbo.

This is not a substitute for a private GitHub repo. Anyone with the files can
read SKILL.md. The marker only tells Cursor/Claude: do not attach live QBO
until the human who got the code from Ghost Protocol has unlocked.

Usage:
  python3 scripts/unlock.py
  python3 scripts/unlock.py --status
  GHOST_QBO_SHARE_CODE='...' python3 scripts/unlock.py
"""
from __future__ import annotations

import getpass
import hashlib
import os
import pathlib
import sys
import time

# SHA-256 of the share code (utf-8, stripped). Rotate by changing this hash.
SHARE_CODE_SHA256 = "745d25274db33d92c55c9d57a2e9a6542068f4f5039bcf8b33b300e717627795"
MARKER = pathlib.Path.home() / ".ghost-qbo" / "unlocked"


def digest(value: str) -> str:
    return hashlib.sha256(value.strip().encode("utf-8")).hexdigest()


def unlocked() -> bool:
    return MARKER.is_file()


def unlock(code: str) -> bool:
    if digest(code) != SHARE_CODE_SHA256:
        return False
    MARKER.parent.mkdir(mode=0o700, exist_ok=True)
    MARKER.write_text(f"unlocked {int(time.time())}\n", encoding="utf-8")
    MARKER.chmod(0o600)
    return True


def main() -> int:
    if "--status" in sys.argv:
        print("unlocked" if unlocked() else "locked")
        return 0 if unlocked() else 1
    if unlocked():
        print(f"Already unlocked ({MARKER})")
        return 0
    code = os.environ.get("GHOST_QBO_SHARE_CODE") or ""
    if not code:
        code = getpass.getpass("Ghost QBO share code: ")
    if unlock(code):
        print(f"Unlocked. Marker: {MARKER}")
        return 0
    print("Wrong share code.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
