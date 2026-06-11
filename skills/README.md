# Skills

Reusable **skills** the intern team uses with opencode (and Claude Code) — packaged
workflows you install once and run by name. This folder catalogs them. The skill format
and install steps are covered in **ONBOARDING.md §8** ("Create or find skills (agents) for
opencode").

> **Public repo — keep these docs free of credentials.** Real keys (Zoho, hunter.io, etc.)
> live in environment variables or gitignored config (`.env*`, `.opencode/`), never here.
> Share skill **docs** in this folder; keep runnable packages (with their secrets) out of
> the repo.

## Available skills

| Skill | What it does | Where |
| --- | --- | --- |
| [`event-research-outreach`](./event-research-outreach.md) | Research → deduplicated contact DB → email verification → draft-by-default personalized outreach | this folder |
| **msg2ai-leads** (5 skills) | Website → live assistant → promo video → outreach (`event-assistant-creation`, `concierge-assistant-creation`, import scripts, the video skills, and `draft-organizer-email` / `ai-ambassador-email-pitch` / `event-outreach-followup` / `drip-campaign-outreach`) | [RethinkLedgers/msg2ai-leads → `SKILLS-OVERVIEW.md`](https://github.com/RethinkLedgers/msg2ai-leads/blob/main/SKILLS-OVERVIEW.md) |
| opencode **agents** (Build, Plan, Explore, custom subagents) | Primary agents + `@name` subagents | ONBOARDING.md §8 |

## How skills are installed

A packaged skill is a folder with a `SKILL.md` plus optional `references/` and `scripts/`,
installed under `~/.config/opencode/skills/<name>/` (global) or a repo's `.opencode/skills/`.
Note that `.opencode/` is gitignored in this repo — so a skill's **documentation** lives here
in `skills/`, while the runnable package (which may carry credentials) stays on your machine
or in a private location.
