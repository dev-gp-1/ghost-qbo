---
name: ghost-qbo
description: Connect QuickBooks Online in Cursor via official Intuit MCP. One connector per client, own realm and TOKEN_STORE_PATH, official QUICKBOOKS_* env names, get_company_info / search_* / 11 reports. Use when the user says QBO, QuickBooks, Intuit MCP, one connector per client, attach sandbox, P&L, AR aging, Claude QuickBooks connector, or /firm-mode qbo. Not Desktop Web Connector. Require ~/.ghost-qbo/unlocked before live attach.
license: MIT
metadata:
  author: Ghost Protocol / Richard
  version: "1.1.0"
  homepage: ghostprotocol.us
  related: dev-gp-1/ghost-handoff
---

# Ghost QBO (Cursor from Claude)

Claude.ai has a native QuickBooks connector. Cursor does not. Use official Intuit QBO MCP plus this skill.

Desktop Web Connector (.qwc / SOAP / local Windows) is a different product. Do not install QBWC for this.

Never print Client Secret, refresh tokens, or access tokens. Never mix two clients in one MCP process. Never print the share-code hash as a password.

## Unlock before live attach

`npx skills add` has no password. Before attaching a live QBO company, require this marker:

```bash
python3 ~/.cursor/skills/ghost-qbo/scripts/unlock.py --status
# locked -> ask the user for the share code from Ghost Protocol, then:
python3 ~/.cursor/skills/ghost-qbo/scripts/unlock.py
# or GHOST_QBO_SHARE_CODE=... python3 .../unlock.py
```

If status is locked, stop. Do not copy token stores. Do not run Intuit OAuth. Do not call get_company_info against a live realm. Demo/docs are fine.

See references/auth.md. Private GitHub is the real install lock; this marker is the use lock.

## When to use

- User asks to connect QuickBooks / QBO in Cursor or Claude Code.
- User says one connector per client, entity wall, COTA vs HMNS, TOKEN_STORE_PATH.
- User is leaving Claude's QuickBooks connector and needs the developer MCP path.
- `/firm-mode qbo <client>`.

## Hard rules

1. Pick the client first. Then the tool. COTA never touches HMNS.
2. One connector per client. One realm. One token-store file. Create another client instead of attaching a second company.
3. Official env names only: QUICKBOOKS_CLIENT_ID, QUICKBOOKS_CLIENT_SECRET, QUICKBOOKS_REFRESH_TOKEN, QUICKBOOKS_REALM_ID, QUICKBOOKS_ENVIRONMENT.
4. Token store = QUICKBOOKS_TOKEN_STORE_PATH (absolute path). Official MCP is one process = one realm. Multi-client = swap the store file and restart MCP.
5. Reads always on. get_* and search_* never disabled.
6. Writes off unless the human turns flags off AND confirms. Default DISABLE_WRITE/UPDATE/DELETE=true.
7. Validate a new attach in order: get_company_info, then one report, then one search.
8. Secrets stay in the token-store .env. Not git. Not .cursor/mcp.json.
9. invalid_grant / HTTP 401 on token refresh = re-authorize. Do not invent a new token.

## Claude to Cursor

Claude.ai native connector is consumer Intuit sign-in, one company, chat P&L. This skill is Intuit Developer app + refresh token, many clients, MCP tool names, sandbox or production.

Friends shifting over: install this skill, unlock, clone official MCP, paste tokens into that client's store, point MCP at that store. See references/claude-to-cursor.md.

## Attach (live)

Only after unlock status is unlocked.

1. Register an app on developer.intuit.com with scope com.intuit.quickbooks.accounting.
2. Sandbox redirect: http://localhost:8000/callback. Production needs public HTTPS.
3. Handshake (npm run auth in intuit/quickbooks-online-mcp-server).
4. Copy references/token-store.example.env to a per-client file, e.g. ~/qbo-stores/cota.env. Fill the five official fields. Leave DISABLE_* true.
5. Point the MCP host at that file (absolute path). Restart the QBO MCP process.
6. Run get_company_info. Then one report. Then one search.

Example MCP block (secret-free) is references/mcp.example.json.

## Tools (official MCP names)

Start: get_company_info, get_preferences, query.

Search: search_customers, search_invoices, search_estimates, search_bills, search_vendors, search_employees, search_accounts, search_items, search_journal_entries, search_bill_payments, search_purchases, search_payments, search_sales_receipts, search_credit_memos, search_refund_receipts, search_purchase_orders, search_vendor_credits, search_deposits, search_transfers, search_time_activities, search_classes, search_departments, search_terms, search_payment_methods, search_tax_codes, search_tax_rates, search_tax_agencies, search_attachables.

Reports: get_profit_and_loss, get_balance_sheet, get_cash_flow, get_trial_balance, get_general_ledger, get_customer_sales, get_aged_receivables, get_aged_receivables_detail, get_customer_balance, get_aged_payables, get_vendor_expenses.

Create/update/delete stay blocked while DISABLE_* is true. Destructive actions need a human confirm even if flags are off.

## firm-mode

If the repo has potato-firm: `/firm-mode qbo cota`. Same rules. Propose-only. Mercury and R365 are sibling 1-per-client connectors.

## Safety

Do not log secrets. Do not enable writes to try it. Access tokens refresh 5 minutes before expiry. Official MCP cannot serve four companies at once. Swap TOKEN_STORE_PATH and restart.

## Troubleshooting

- unlock.py locked: ask Ghost Protocol for the share code
- invalid_grant / 401: re-authorize; verify CLIENT_ID + SECRET
- Wrong company: wrong token store. Stop. Switch file. Restart MCP
- Claude connector habits: this is not claude.ai. Use MCP tool names
- Desktop Web Connector docs: wrong product. Ignore .qwc
- Empty store: playbook stops. Fill cota.env then restart

## Install

```bash
npx skills add dev-gp-1/ghost-qbo -g -a cursor
python3 ~/.cursor/skills/ghost-qbo/scripts/unlock.py
```
