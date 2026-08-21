# Ghost QBO

**Cursor / Claude Code skill** for QuickBooks Online the official Intuit way.

Claude's native QuickBooks connector does not come with you to Cursor. This skill does: one tenant, many clients, **one QBO connector per client**, official QUICKBOOKS_* env names, Intuit MCP tools.

Not QuickBooks Desktop Web Connector (.qwc / SOAP).

## Install in Cursor

```bash
npx skills add dev-gp-1/ghost-qbo -g -a cursor
python3 ~/.cursor/skills/ghost-qbo/scripts/unlock.py
```

Claude Code (during the shift):

```bash
npx skills add dev-gp-1/ghost-qbo -g -a claude-code
python3 ~/.claude/skills/ghost-qbo/scripts/unlock.py
```

`npx skills add` has no password. Two layers (see references/auth.md):

1. **Install lock (real)** — make this repo private; friend `gh auth login` then the same npx command (or `git@github.com:dev-gp-1/ghost-qbo.git`).
2. **Use lock (share code)** — `scripts/unlock.py` writes `~/.ghost-qbo/unlocked`. Ask Richard for the code. Cursor should not attach live QBO until that marker exists.

From a clone, friends can also:

```bash
bash scripts/install.sh cursor
```

Pair with the handoff skill if you also kick work to Grok:

```bash
npx skills add dev-gp-1/ghost-handoff -g -a cursor
```

Then say: attach QBO for this client / `/firm-mode qbo cota`.

## Contains

* SKILL.md — pick client first, official MCP tools, writes off, unlock before live attach
* scripts/unlock.py — share-code gate (hash only in git)
* references/ — registry, token-store env, MCP block, Claude notes, auth.md

## License

MIT
