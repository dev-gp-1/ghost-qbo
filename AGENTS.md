# Ghost QBO Skill

Cursor / Claude Code skill for QuickBooks Online via official Intuit MCP. One connector per client.

## Install

```bash
npx skills add . -g -a cursor
python3 scripts/unlock.py
# published:
npx skills add dev-gp-1/ghost-qbo -g -a cursor
```

Before a live attach, require `~/.ghost-qbo/unlocked` (run scripts/unlock.py). If missing, stop and ask the user for the share code from Ghost Protocol. Never print the hash as a password. Never print QBO secrets.

When the user wants QBO, QuickBooks, Intuit MCP, or `/firm-mode qbo`, follow SKILL.md. Pick the client first. Never mix realms.
