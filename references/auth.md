# Auth for ghost-qbo

npx skills add has no --password flag. Two layers:

## 1. Install lock (real)

Make the GitHub repo private. Add the friend as a collaborator.

They already have GitHub CLI signed in:

```bash
gh auth login
npx skills add dev-gp-1/ghost-qbo -g -a cursor
```

Or SSH:

```bash
npx skills add git@github.com:dev-gp-1/ghost-qbo.git -g -a cursor
```

The skills CLI uses git credentials, then gh repo clone, then SSH. Optional: GITHUB_TOKEN / GH_TOKEN.

## 2. Use lock (share code)

After the files are on disk, unlock once:

```bash
python3 ~/.cursor/skills/ghost-qbo/scripts/unlock.py
# or
GHOST_QBO_SHARE_CODE='<code from Richard>' python3 ~/.cursor/skills/ghost-qbo/scripts/unlock.py
python3 ~/.cursor/skills/ghost-qbo/scripts/unlock.py --status
```

Success writes ~/.ghost-qbo/unlocked (0600). Cursor must not attach live QBO until that marker exists.

The share code is not in git. Only a SHA-256 hash is. Rotate by changing SHARE_CODE_SHA256 in scripts/unlock.py.

If the repo is public, layer 2 is honor-system: anyone can still read SKILL.md. Flip the repo private for a real gate.
