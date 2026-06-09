# Connecting to Zoho Mail

Three supported ways to send mail as `bart@msg2ai.xyz`. Pick one. **Method A (app
password + SMTP)** is the simplest and most reliable for a standalone opencode setup.
**Method B (OAuth API)** is what the Paperclip RTL instance already uses. **Method C
(MCP)** is best if you want the agent to call a tool instead of running a script.

---

## 0. First: find your Zoho data center (DC)

Zoho hosts accounts in regional DCs and the hostnames differ. Check the URL when you log
into Zoho Mail, or **Settings → Account → Data Center**:

| DC | Accounts host | Mail API host | SMTP host |
|----|---------------|---------------|-----------|
| US (`.com`)  | `accounts.zoho.com`  | `mail.zoho.com`  | `smtp.zoho.com` / `smtppro.zoho.com` |
| EU (`.eu`)   | `accounts.zoho.eu`   | `mail.zoho.eu`   | `smtp.zoho.eu` / `smtppro.zoho.eu` |
| IN (`.in`)   | `accounts.zoho.in`   | `mail.zoho.in`   | `smtp.zoho.in` |
| AU (`.com.au`) | `accounts.zoho.com.au` | `mail.zoho.com.au` | `smtp.zoho.com.au` |

Use **`smtppro.zoho.<dc>`** for paid org / custom-domain mailboxes (msg2ai.xyz is a custom
domain, so `smtppro` is usually correct), and plain `smtp.zoho.<dc>` for personal Zoho
addresses. The scripts default to `.com`; override with the env vars below if you are on `.eu`.

---

## Method A — App password + SMTP (recommended, simplest)

1. Log into Zoho Mail with `bart@msg2ai.xyz`.
2. Enable Two-Factor Authentication (required for app passwords):
   **My Account → Security → Multi-Factor Authentication**.
3. Generate an app-specific password:
   **My Account → Security → App Passwords → Generate New Password**
   (name it e.g. `opencode-outreach`). Copy the generated password — it is shown once.
4. Export the credentials in your shell / opencode environment:

   ```sh
   export ZOHO_SMTP_HOST="smtppro.zoho.com"   # smtppro.zoho.eu if EU; smtp.zoho.* for personal
   export ZOHO_SMTP_PORT="465"                 # 465 = SSL, or 587 = STARTTLS
   export ZOHO_SMTP_USER="bart@rtledgers.com"  # your PRIMARY mailbox login, NOT an alias
   export ZOHO_SMTP_PASS="<the app-specific password>"
   export ZOHO_FROM="bart@msg2ai.xyz"          # the alias you send AS
   ```

   > Auth uses the **primary mailbox login** (the account the app password belongs to),
   > while `From:` is the alias `bart@msg2ai.xyz`. Logging in *as the alias* typically
   > fails Zoho SMTP auth.
5. Send:
   ```sh
   python3 scripts/zoho_smtp_send.py --to person@example.com \
       --subject "Quick idea on your event-tech work" --html drafts/2026-06-09/person.html
   ```

Outgoing server reference: `smtp.zoho.com` / `smtppro.zoho.com`, **port 465 (SSL)** or
**587 (TLS)**, auth = full email address + app password. (EU: `smtp.zoho.eu` /
`smtppro.zoho.eu`.)

---

## Method B — OAuth self-client + Zoho Mail API (matches the Paperclip instance)

The RTL Paperclip container already has `ZOHO_CLIENT_ID`, `ZOHO_CLIENT_SECRET`, and
`ZOHO_REFRESH_TOKEN`. Reuse those, or create your own self-client:

1. Go to the Zoho API console: `https://api-console.zoho.<dc>` → **Add Client →
   Self Client** → Create.
2. Note the **Client ID** and **Client Secret**.
3. In the self-client **Generate Code** tab, request scope
   `ZohoMail.messages.CREATE,ZohoMail.accounts.READ` for your account, with a short
   duration. Copy the one-time **grant code**.
4. Exchange the grant code for a **refresh token** (one time):
   ```sh
   curl -s "https://accounts.zoho.com/oauth/v2/token" \
     -d grant_type=authorization_code \
     -d client_id="$ZOHO_CLIENT_ID" \
     -d client_secret="$ZOHO_CLIENT_SECRET" \
     -d code="<grant code>"
   # -> save the "refresh_token" from the JSON response (it does not expire)
   ```
5. Export for the sender script:
   ```sh
   export ZOHO_CLIENT_ID="..."
   export ZOHO_CLIENT_SECRET="..."
   export ZOHO_REFRESH_TOKEN="..."
   export ZOHO_ACCOUNTS_HOST="accounts.zoho.com"   # accounts.zoho.eu if EU
   export ZOHO_MAIL_HOST="mail.zoho.com"           # mail.zoho.eu if EU
   export ZOHO_FROM="bart@msg2ai.xyz"
   ```
6. Send:
   ```sh
   python3 scripts/zoho_send.py --to person@example.com \
       --subject "Quick idea on your event-tech work" --html drafts/2026-06-09/person.html
   ```

How the API works (the script does all of this):
- Refresh an access token: `POST https://<ZOHO_ACCOUNTS_HOST>/oauth/v2/token`
  with `grant_type=refresh_token&client_id=…&client_secret=…&refresh_token=…`.
- Resolve the account id: `GET https://<ZOHO_MAIL_HOST>/api/accounts`
  (header `Authorization: Zoho-oauthtoken <access_token>`).
- Send: `POST https://<ZOHO_MAIL_HOST>/api/accounts/{accountId}/messages` with JSON body
  `{ "fromAddress", "toAddress", "subject", "content", "mailFormat": "html",
  optional "ccAddress"/"bccAddress" }`.
- Required scope: `ZohoMail.messages.CREATE` (or `ZohoMail.messages.ALL`).

---

## Method C — Zoho MCP (call a tool instead of a script)

Configure a Zoho MCP server so the agent can call `sendEmail` directly. Two common options:

**C1. Composio-hosted Zoho (what the Paperclip instance uses).** Add an HTTP MCP to
`~/.config/opencode/opencode.jsonc`:
```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "zoho": {
      "type": "remote",
      "url": "https://connect.composio.dev/mcp",
      "headers": { "x-consumer-api-key": "${COMPOSIO_API_KEY}" },
      "enabled": true
    }
  }
}
```
Set `COMPOSIO_API_KEY` in your env and connect the Zoho Mail toolkit + your
`bart@msg2ai.xyz` account in the Composio dashboard. (Do not paste API keys into the
file — use the `${ENV}` form.)

**C2. A standalone Zoho Mail MCP server** (local stdio):
```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "zoho-mail": {
      "type": "local",
      "command": ["npx", "-y", "<zoho-mail-mcp-package>"],
      "environment": {
        "ZOHO_CLIENT_ID": "${ZOHO_CLIENT_ID}",
        "ZOHO_CLIENT_SECRET": "${ZOHO_CLIENT_SECRET}",
        "ZOHO_REFRESH_TOKEN": "${ZOHO_REFRESH_TOKEN}",
        "ZOHO_ACCOUNT_REGION": "com"
      },
      "enabled": true
    }
  }
}
```

Once configured, the skill sends by calling the MCP tool (e.g. `ZohoMail_sendEmail` /
`sendEmail`) with: `fromAddress=bart@msg2ai.xyz`, `toAddress`, `subject`,
`content` (the HTML), `mailFormat=html`. Verify the tool is available with opencode's
tool list before relying on it; fall back to Method A/B if the MCP is not connected.

---

## Quick decision guide
- Just want it to work now, scripting is fine → **Method A**.
- Want parity with the Paperclip RTL automation / no app password → **Method B**.
- Want the agent to "have a send-email tool" natively → **Method C**.

## Sanity test (any method)
Send one email to yourself first (`--to bart@msg2ai.xyz`) and confirm it lands before
running outreach in `send_mode=send`.
