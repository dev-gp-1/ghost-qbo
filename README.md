# Ghost QBO

**Cursor / Claude Code skill** for QuickBooks Online the official Intuit way.

Claude's native QuickBooks connector does not come with you to Cursor. This skill does: one tenant, many clients, **one QBO connector per client**, official QUICKBOOKS_* env names, Intuit MCP tools.

Not QuickBooks Desktop Web Connector (.qwc / SOAP).

## Install in Cursor

```bash
npx skills add dev-gp-1/ghost-qbo -g -a cursor
```

Claude Code (during the shift):

```bash
npx skills add dev-gp-1/ghost-qbo -g -a claude-code
```

Pair with the handoff skill if you also kick work to Grok:

```bash
npx skills add dev-gp-1/ghost-handoff -g -a cursor
```

Then say:

- attach QBO for this client
- /firm-mode qbo cota
- one connector per client, pick COTA not HMNS
- run get_company_info then P&L on this realm

## Contains

* SKILL.md — pick client first, official MCP tools, writes off by default
* references/ — example client registry, token-store env, secret-free MCP block, Claude to Cursor notes
* Official MCP path: one TOKEN_STORE_PATH per client (swap + restart; Intuit MCP is one realm per process)

## Official sources

- https://github.com/intuit/quickbooks-online-mcp-server
- Claude QuickBooks connector (consumer; not this runtime)
- Desktop Web Connector is out of scope

Public repo: https://github.com/dev-gp-1/ghost-qbo

## License

MIT
