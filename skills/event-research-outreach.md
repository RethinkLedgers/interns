# Skill: `event-research-outreach`

An opencode **packaged skill** (`SKILL.md` + `references/` + `scripts/`) that runs an
end-to-end **research → outreach** workflow. Adaptable per vertical — events, conferences,
short-term rentals.

> **Public repo — no credentials here.** Zoho keys, refresh tokens, and the hunter.io key
> belong in environment variables or gitignored config (`.env*`, `.opencode/`), never in the repo.

## What it does

- **Research** target events/companies and write a dated analysis report of new findings.
- Maintain a **deduplicated master contact database** with a status pipeline.
- **Verify** every email address (via hunter.io) before it's used.
- **Draft** personalized HTML outreach from your msg2ai sender address. It **defaults to
  draft mode** — it won't send without an explicit instruction, and never to unverified addresses.

## Layout

```text
~/.config/opencode/skills/event-research-outreach/
  SKILL.md                        # workflow: research → dedup DB → contact research → verify → draft/send
  references/zoho-setup.md        # Zoho sending options (SMTP, OAuth API, MCP)
  references/msg2ai-positioning.md
  scripts/zoho_send.py            # Zoho Mail sender (Python stdlib)
  scripts/hunter_verify.sh        # hunter.io email verification
```

## Sending through Zoho Mail — pick one path

- **SMTP (app password):** set the Zoho SMTP env vars and use the SMTP sender (ports **465**
  SSL / **587** TLS; `smtppro.zoho.com` for a custom domain).
- **OAuth API (self-client):** a client ID, secret, and refresh token supplied as env vars;
  needs the `ZohoMail.messages.CREATE` scope.
- **MCP:** point opencode at a Zoho Mail MCP (e.g. a Composio-hosted one) and let the agent
  call its `sendEmail` tool.

> Zoho's **data-center hostnames differ by region** (`.com` vs `.eu`) — use the one that
> matches your account.

## Install & run

Place the package under `~/.config/opencode/skills/event-research-outreach/` (global), then
open opencode anywhere and ask, e.g. *"run the event-tech research and outreach for today."*
It **defaults to draft mode** — review the drafts before any send, and never send to
unverified addresses.
