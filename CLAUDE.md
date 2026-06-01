# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **documentation-only** repository — onboarding material for the Rethink-Labs intern program. There is no build, no tests, no lint, no application code. Everything is Markdown. "Working" on this repo means editing prose, keeping the two onboarding guides accurate, and maintaining the per-intern working folders.

The internship's tech stack (which the docs explain, but which lives in *other* repos) is: **opencode** as the terminal AI agent (with **Cursor** as a GUI alternative), **Tailscale** for secure access to internal/self-hosted services, **Paperclip** to orchestrate agents like employees, **Twenty** as the CRM, **Composio** for managed app authentication, and an **Obsidian** vault as the team wiki. When editing the docs, keep this mental model — the guides exist to get an intern from zero to productive across those tools.

## Critical guardrail: the admin doc is secret

`ONBOARDING-ADMIN.md` is **gitignored on purpose** and must never be committed. It holds contacts, budgets, contractor/legal runbook details, and credential-handoff procedures. The `.gitignore` also excludes `opencode.json*`, `.opencode/`, `.composio/`, and `.env*` because they carry API keys.

- Never `git add -f` the admin doc or any ignored secret file, and never paste its contents into a tracked file (including this one).
- `git add .` is discouraged throughout the docs — stage specific files. If you ever see the admin doc or a config file appear in `git status` as staged, stop and unstage it.

## Structure

- `ONBOARDING.md` — the intern-facing guide (numbered sections 1–11, then an Intro videos section and a cheat-sheet table). This is the primary artifact; most edits land here.
- `ONBOARDING-ADMIN.md` — the admin/Arianna-facing counterpart (gitignored). The two docs are *parallel*: a change to one (e.g. who issues Twenty invites, the GitHub org name) often needs a matching change in the other to stay consistent.
- `products/` — per-product onboarding/testing guidelines for the team's products (e.g. `MSG2AI_PRODUCT_GUIDELINE.md`, `actionnotes/product-guideline.md`). New files land here as products come online.
- `working-folders/` — one folder per intern, each copied from `_template/`. The template is `README.md` (profile) + `progress-reports/` + `workproducts/`, each with its own README explaining the convention. `working-folders/README.md` is the index and rulebook.

## Conventions when editing

- **Keep the cheat-sheet table (bottom of `ONBOARDING.md`) in sync** with the body. If you add or change a command in a section, update the corresponding table row.
- **`> TODO — fill in:` blockquotes are intentional**, not bugs. They mark facts only an admin can supply (exact repo names, invite owners, the Paperclip instance URL). Don't invent values to "resolve" them — leave them or ask.
- **Brand is `Rethink-Labs`, but the GitHub org slug is `RethinkLedgers` — keep them separate.** In prose, headers, and local paths use the company name **`Rethink-Labs`**. In any `github.com:`/`github.com/` URL or `<org>/repo` path, the org is **`RethinkLedgers`** (the live GitHub org — do *not* rewrite these to `Rethink-Labs`, or clones break). Don't reintroduce `rtledgers`: the company email domain is `rethink-labs.com`, `@rethink-ai.com` is reserved for staff like Arianna, and `ONBOARDING.md` refers to the intern work email as the **msg2ai email**. Twenty workspace stays `rethink-labs.twenty.com`. The local-only `ONBOARDING-ADMIN.md` still uses the old `RethinkLedgers`/`rtledgers` names (left untouched on purpose — update once admin/email ownership is confirmed).
- **No secrets in any tracked file**, including working-folder examples. The docs repeat this rule everywhere; honor it.
- Per-intern folders are owned by their intern — edit `working-folders/<name>/` only for that intern's own work.

## Contribution workflow

Everything goes through a branch + PR against `main` (interns are told not to push straight to `main`). Branch naming in use: `docs/<topic>` for doc changes and `<firstname>/<task>` for intern work (e.g. `jane/setup`). Match the existing pattern when creating a branch here.
