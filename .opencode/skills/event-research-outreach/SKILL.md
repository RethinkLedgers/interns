---
name: event-research-outreach
description: >-
  Run daily event-tech / conference / short-term-rental (STR) market research and
  personalized B2B email outreach for msg2ai.xyz, AI-Ambassador, and ActionNotes
  (RethinkLedgers). Use when asked to research event-tech news, conferences,
  speakers, authors, startups, funding, partnerships or trends; build/maintain an
  outreach contact database; find and verify contact emails (hunter.io); draft or
  send personalized HTML outreach from bart@msg2ai.xyz; or run the "daily research
  and outreach" routine. Covers connecting to Zoho Mail (app password / SMTP, OAuth
  API, or MCP) to send mail. Triggers: "event-tech research", "conference outreach",
  "STR outreach", "daily outreach", "draft outreach emails", "find speakers/authors".
license: MIT
compatibility: opencode
metadata:
  owner: RethinkLedgers
  brand: msg2ai
  sender: bart@msg2ai.xyz
---

# Event Research & Outreach

Daily market research + personalized B2B outreach engine for the msg2ai family of
products. This skill is the standalone (opencode-runnable) version of the Paperclip
RTL routines **"Daily AI Event Tech Research & Outreach"**, **"Daily Conference
Research and Outreach"**, and **"Daily STR Research and outreach"**.

Goal each run: produce a dated analysis report of **new** discoveries, grow a
deduplicated master contact database, and draft (or send) ~10 personalized, verified
outreach emails.

## Inputs / parameters

Ask the user (or accept from the prompt) — sensible defaults in brackets:

- **focus** — `event-tech` (default) | `conferences` | `str` (short-term rental / hospitality).
- **send_mode** — `draft` (default, safe) | `send`. In `draft` mode, write `.eml`/HTML
  files and DB rows but **do not** send. Only send when the user explicitly says "send".
- **target_count** — emails to prepare this run [10].
- **workdir** — where reports/DB live [`./outreach`]. Create if missing.

> Outbound email is outward-facing and hard to reverse. Default to `draft`. Never send
> without an explicit instruction, and never send to an unverified address.

## Workflow

### 1. Daily research (event analysis)
Research and analyze, for the chosen **focus**, items from roughly the last 24–72h:
- News, articles, opinion pieces; product launches; funding/M&A; partnerships.
- Upcoming conferences and industry events; CFPs and speaker line-ups.
- Emerging trends relevant to **AI, hospitality, events, and guest engagement**.

Identify and summarize: authors/journalists, speakers/organizers, relevant
startups/companies, influencers/publications.

Write `./outreach/reports/daily-<focus>-analysis-<YYYY-MM-DD>.md`. The report must
contain **only new discoveries / new activity for that day** — do not repeat prior
research unless there is a meaningful update. Cross-check the master DB (step 2) so the
report and the outreach list stay deduplicated.

### 2. Master tracking database (persistent, deduplicated)
Maintain `./outreach/outreach-master.csv` (create with the header below on first run).
Before adding anyone, **search the file first**; update the existing row if you find
new info instead of creating a duplicate (dedupe on lowercased `email`, else on
`name|company`).

```
id,name,company,role,email,email_status,linkedin,website,socials,focus,source_url,relevance,status,first_seen,last_touch,draft_path,notes
```

`status` pipeline (one of):
`not_contacted` → `researching` → `draft_created` → `ready_for_review` → `sent` →
`awaiting_response` → `follow_up_needed` → `partnership_active` → `not_a_fit`.

### 3. Contact & opportunity research
For each new qualified target collect: full name, company, role/title, email, LinkedIn,
website, social profiles, conference participation, notable articles/talks. Then write a
one-line **relevance** note: how they map to a msg2ai collaboration (partnership, AI
integration, conference collab, hospitality/event-tech, media/co-marketing). Use
`references/msg2ai-positioning.md` for the product framing and links to cite.

### 4. Verify the email (hunter.io) — mandatory before send
Run `scripts/hunter_verify.sh "<email>"` (needs `HUNTER_API_KEY`). Accept only
`deliverable` (treat `risky`/`accept_all` as draft-only, never auto-send). Record the
result in `email_status`. See the script for the exact endpoint.

### 5. Draft the outreach email
One personalized **HTML** email per qualified target:
- From: **Bart Cant** `<bart@msg2ai.xyz>`.
- Personalized to their recent work/article/initiative/conference activity (no generic copy).
- Reference, where relevant: AI-Ambassador events `https://www.ai-ambassador.xyz/events`
  and ActionNotes `https://www.actionnotes.ai`.
- Tie to a concrete msg2ai collaboration angle (see positioning reference).
- Warm, concise, professional, partnership-focused. Aim for **target_count** (~10) emails.
- Save each as `./outreach/drafts/<YYYY-MM-DD>/<slug>.html` and set `draft_path` +
  `status=draft_created` (or `ready_for_review`).
- Do **not** re-draft for already-contacted targets unless there is a significant new
  development, a follow-up is due, or a new collaboration angle emerged.

### 6. Send (only in send_mode=send, only verified addresses)
Send via Zoho using whichever connection the user configured (see
`references/zoho-setup.md`):
- **OAuth Mail API:** `python3 scripts/zoho_send.py --to <email> --subject "<s>" --html <file>`
- **SMTP app password:** `python3 scripts/zoho_smtp_send.py --to <email> --subject "<s>" --html <file>`
- **MCP:** call the Zoho MCP `sendEmail`/`ZohoMail_sendEmail` tool with
  `fromAddress=bart@msg2ai.xyz`, `toAddress`, `subject`, `content` (HTML), `mailFormat=html`.

After a successful send set `status=sent` and `last_touch=<date>`. On failure, leave the
draft and record the error in `notes`.

### 7. Summary
End each run with: # new items researched, # new contacts added, # emails drafted, #
sent (if any), and anything needing human review.

## Connecting to Zoho
Read `references/zoho-setup.md` for full setup of all three methods (app password + SMTP,
OAuth self-client API, and MCP), including how to find your Zoho data-center (.com vs
.eu) and the required scopes. The Paperclip RTL instance already uses the OAuth method
via `ZOHO_CLIENT_ID` / `ZOHO_CLIENT_SECRET` / `ZOHO_REFRESH_TOKEN`.

## Files in this skill
- `scripts/zoho_send.py` — send HTML email via Zoho Mail OAuth API (refresh-token flow).
- `scripts/zoho_smtp_send.py` — send HTML email via Zoho SMTP using an app password.
- `scripts/hunter_verify.sh` — verify an address with hunter.io before sending.
- `references/zoho-setup.md` — Zoho connection guide (app password / OAuth / MCP).
- `references/msg2ai-positioning.md` — product positioning + links for personalization.

## Conventions & guardrails
- Idempotent: re-running the same day should not duplicate report entries, DB rows, or emails.
- Never hardcode secrets in reports/drafts. Read tokens from env (see references).
- Respect opt-outs and anti-spam norms: one tailored email, clear value, easy to ignore;
  honor any prior "not_a_fit"/unsubscribe in the DB.
- Keep all generated artifacts under `workdir` for local review. **Do NOT commit them** —
  `outreach-master.csv` and the drafts contain third-party personal data (names, emails,
  LinkedIn). On first run, write a `.gitignore` containing `*` into `workdir` so the contact
  DB and drafts can never be accidentally committed (GDPR/privacy). Version-control the
  skill itself, not the people you researched.
