# Claude QuickBooks connector to Cursor

Claude.ai QuickBooks connector is a consumer Intuit sign-in inside Claude. It does not install into Cursor.

## What to tell a friend shifting over

1. Install the skill:

```bash
npx skills add dev-gp-1/ghost-qbo -g -a cursor
```

2. Clone and build official MCP once:

```bash
git clone https://github.com/intuit/quickbooks-online-mcp-server.git
cd quickbooks-online-mcp-server && npm install && npm run build
```

3. One token-store file per client. Point Cursor MCP at that file (see mcp.example.json). No secrets in mcp.json.

4. In Cursor: pick client COTA, run get_company_info.

5. Optional Grok handoff:

```bash
npx skills add dev-gp-1/ghost-handoff -g -a cursor
```

## Do not

- Install QuickBooks Desktop Web Connector for this.
- Share one refresh token across clients.
- Put QUICKBOOKS_CLIENT_SECRET in git or chat.
- Enable writes to see if it works.
