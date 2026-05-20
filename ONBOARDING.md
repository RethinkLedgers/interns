# RethinkLedgers — Intern Onboarding

Welcome. This guide walks you through everything you need to be productive on day one:

1. Install **opencode** (terminal AI coding agent) on macOS or Windows
2. Pick a **free model** so you don't need a paid API key
3. Set up **GitHub + SSH** so you can clone, pull, and push private repos
4. Sync work between your laptop and GitHub, and the commands to give opencode
5. Connect **MCP servers** to opencode — including **Composio** for 1,000+ apps
6. Create or find **skills (agents)** for opencode
7. Get oriented on **Paperclip** and how to use opencode as its underlying LLM
8. Use the **shared Obsidian wiki** as the team's knowledge base
9. Work in **Twenty CRM** at `rethink-labs.twenty.com` and wire it into opencode

> If anything in this doc is wrong or stale, fix it in the repo and open a PR. Don't suffer in silence.

---

## 1. Install opencode

opencode is an open-source AI coding agent that runs in your terminal. Think Claude Code, but provider-agnostic — you bring your own model.

### macOS

Pick **one** of these:

```bash
# Homebrew (recommended)
brew install anomalyco/tap/opencode

# OR universal installer
curl -fsSL https://opencode.ai/install | bash

# OR npm (if you already have Node 18+)
npm install -g opencode-ai
```

Verify:

```bash
opencode --version
```

### Windows

You have three reasonable paths. **WSL2 is strongly recommended** — most tooling (git, ssh, node) behaves more predictably on Linux, and every command in this doc works there unchanged.

**Option A — WSL2 (recommended).** In PowerShell as Administrator:

```powershell
wsl --install -d Ubuntu
```

Restart, finish the Ubuntu setup, then **inside the Ubuntu terminal** run the macOS Homebrew or curl command above.

**Option B — Native Windows via Scoop or Chocolatey.** In PowerShell:

```powershell
# Scoop
scoop install opencode

# OR Chocolatey
choco install opencode
```

**Option C — npm.** If you have Node 18+ installed:

```powershell
npm install -g opencode-ai
```

Verify in a fresh PowerShell window:

```powershell
opencode --version
```

### First launch

In any project folder, run:

```bash
opencode
```

On first run it will prompt you to pick a model provider. Skip ahead to the next section before you pick anything.

---

## 2. Pick a free model

opencode supports 75+ providers via [models.dev](https://models.dev). **Important:** Anthropic restricted opencode's access to Claude models in early 2026, so don't plan on using Claude through opencode — use it through Claude Code instead.

Below are the three best free options as of May 2026. Start with **OpenRouter** unless you have a reason not to.

### Option A — OpenRouter (recommended for coding)

OpenRouter aggregates many model providers and exposes several capable models with a free tier (currently strong options: DeepSeek V3, Qwen 2.5 Coder, Llama 3.3).

1. Sign up at [openrouter.ai](https://openrouter.ai) (Google login works).
2. Go to **Keys → Create Key**, copy the key.
3. In opencode, run `/connect`, choose **OpenRouter**, paste the key.
4. When picking a model, look for entries with `:free` in the name (e.g. `deepseek/deepseek-chat-v3:free`).

### Option B — Google Gemini (huge free quota)

Best if you want a large daily request budget and don't mind occasionally weaker code quality.

1. Sign in at [aistudio.google.com](https://aistudio.google.com).
2. Click **Get API key → Create API key**.
3. In opencode, run `/connect`, choose **Google Gemini**, paste the key.
4. Pick `gemini-2.5-pro` (1M-token context).

### Option C — NVIDIA build.nvidia.com (free open models)

1. Create an account at [build.nvidia.com](https://build.nvidia.com).
2. Generate an API key from your account page.
3. In opencode, run `/connect`, search **NVIDIA**, paste the key.
4. Pick a Nemotron or Llama variant.

### Switching models later

Inside opencode, run `/model` to change models at any time. Run `/connect` again to add another provider.

---

## 3. Set up GitHub and SSH

You will be added to the **RethinkLedgers** organization on GitHub. Most repos there are **private** — HTTPS clones will pester you for credentials constantly, so we use SSH keys.

### 3.1 Create a GitHub account (if you don't have one)

1. Go to [github.com/signup](https://github.com/signup) and use your **work email** (`...@rethink-ai.com` or your assigned address).
2. Enable 2FA: **Settings → Password and authentication → Enable two-factor**. Use an authenticator app (1Password, Authy, Google Authenticator). **Don't skip this — the org will require it.**
3. Send your GitHub username to your manager so they can invite you to **RethinkLedgers**.

### 3.2 Install git

- **macOS:** `brew install git` (or `xcode-select --install` to get Apple's version).
- **Windows (WSL):** `sudo apt update && sudo apt install git -y`
- **Windows (native):** [git-scm.com/download/win](https://git-scm.com/download/win)

Set your identity once:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@rethink-ai.com"
```

### 3.3 Generate an SSH key

Use **ed25519** — it's faster and shorter than RSA.

```bash
ssh-keygen -t ed25519 -C "you@rethink-ai.com"
```

Press Enter to accept the default path (`~/.ssh/id_ed25519`). When prompted for a passphrase, **set one** — it protects the key if your laptop is stolen.

### 3.4 Add the key to your ssh-agent

**macOS:**

```bash
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

Then create or edit `~/.ssh/config`:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

**Windows (WSL):**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Windows (native PowerShell):**

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

### 3.5 Add the public key to GitHub

Copy your public key to clipboard:

```bash
# macOS
pbcopy < ~/.ssh/id_ed25519.pub

# WSL / Linux
cat ~/.ssh/id_ed25519.pub   # then copy by hand

# Windows PowerShell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | clip
```

On GitHub: **Settings → SSH and GPG keys → New SSH key**. Title it something like `laptop-mac-2026`, paste the key, save.

### 3.6 Test the connection

```bash
ssh -T git@github.com
```

You should see:

> Hi `your-username`! You've successfully authenticated, but GitHub does not provide shell access.

That message is the success case. If you see a permission error, your key wasn't added to the agent or wasn't pasted into GitHub correctly.

### 3.7 Clone a private repo

Use the **SSH** URL (`git@github.com:Org/repo.git`), not HTTPS:

```bash
git clone git@github.com:RethinkLedgers/<repo-name>.git
cd <repo-name>
```

---

## 4. Syncing local ↔ GitHub (and telling opencode)

### Daily git workflow

```bash
# Before starting work — pull the latest from main
git checkout main
git pull

# Create a branch for your task
git checkout -b your-name/short-task-description

# ...edit files...

# Stage and commit
git add <specific files>            # avoid `git add .` — it grabs junk
git commit -m "Short summary of what changed"

# Push your branch up
git push -u origin your-name/short-task-description
```

Then on GitHub, click **Compare & pull request** to open a PR. Tag your manager for review. After it's approved and merged, on your laptop:

```bash
git checkout main
git pull
git branch -d your-name/short-task-description    # cleanup
```

### What to ask opencode to do

opencode is great at *driving* git, but it cannot guess your intent. Use direct commands. Examples that work well:

- *"Create a branch called `bart/add-budget-warning`, then update `src/budget.ts` so warnings fire at 80% instead of 90%."*
- *"Stage only the files I edited in `src/budget/`, commit with a short message about the threshold change, and push the branch."*
- *"Pull the latest `main` and rebase my current branch on top. If there are conflicts, stop and show me."*
- *"Open a PR against `main` titled `Lower budget warning threshold to 80%`, with a 3-bullet summary."*

Avoid vague prompts like "fix git" or "make a PR." Tell it the branch name, the commit message, and which files matter. Opencode will read the repo before acting if you ask it to — *"First read `src/budget.ts` and `tests/budget.test.ts`, then propose a change."*

**Safety:** never let opencode run `git push --force`, `git reset --hard`, or `rm -rf` without you understanding why. When in doubt, ask it to **show the diff** before committing.

---

## 5. Connect MCP servers to opencode

**MCP (Model Context Protocol)** lets opencode call external tools — GitHub APIs, databases, filesystems, web fetchers, etc. — through a standard interface.

### Config file location

opencode looks for `opencode.json` (or `opencode.jsonc`) either:

- Globally: `~/.config/opencode/opencode.json`
- Per project: `./opencode.json` in your repo root

### Add a local (stdio) MCP server

Local servers run on your machine as a subprocess. Example: the official "everything" server for testing.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "everything": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-everything"],
      "enabled": true
    }
  }
}
```

A more useful real example — give opencode access to your filesystem outside the project:

```json
{
  "mcp": {
    "filesystem": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "/Users/you/Documents"],
      "enabled": true
    }
  }
}
```

### Add a remote (HTTP) MCP server

```json
{
  "mcp": {
    "linear": {
      "type": "remote",
      "url": "https://mcp.linear.app/sse",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer YOUR_LINEAR_TOKEN"
      }
    }
  }
}
```

> Never commit secrets. Put tokens in environment variables and reference them with `${env:VAR_NAME}` if your config supports it, or keep `opencode.json` in `.gitignore` when it has secrets.

### Use MCP tools in prompts

Once a server is enabled, opencode discovers its tools automatically. Reference them by server name:

> *"Use the `filesystem` MCP to read `~/Documents/spec.md` and summarize the requirements."*

Run `/mcp` inside opencode to list active servers and their tools.

### 5b. Composio — one MCP server for 1,000+ apps

Wiring up a separate MCP for every SaaS app you touch (GitHub, Slack, Linear, Gmail, Jira, Figma, Notion…) gets old fast, and stuffing all those tool definitions into the model's context wastes thousands of tokens before you've even typed a prompt. **[Composio](https://composio.dev)** solves both problems: it's a single MCP server that brokers access to 1,000+ apps via a **tool router**. The model only sees the tools it actually needs for the current task — the rest are discovered on demand.

This matters for two things you'll do constantly: **building skills** (each skill needs a specific bundle of tools — Composio is where those tools come from) and **connecting to APIs** (you authenticate once with Composio, then any future agent inherits that connection).

#### Install Composio

```bash
curl -fsSL https://composio.dev/install | bash
composio login
```

`composio login` opens a browser to authenticate. Free tier is fine for the internship.

#### Connect apps you'll actually use

From the terminal, link the apps your work needs. Each command opens an OAuth flow in the browser:

```bash
composio add github
composio add linear
composio add slack
composio add gmail
composio add notion
```

Run `composio apps` to see the full catalog, and `composio integrations` to see what you've already connected.

#### Wire Composio into opencode

Add this to your `opencode.json` (global at `~/.config/opencode/opencode.json` or per-project):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "composio": {
      "type": "remote",
      "url": "https://connect.composio.dev/mcp",
      "enabled": true
    }
  }
}
```

Restart opencode. Run `/mcp` and you should see `composio` listed with its meta-tools (`SEARCH_TOOLS`, `EXECUTE_TOOL`, etc.). Try it:

> *"Use composio to find my three most-recently-assigned Linear issues and summarize them."*

opencode will ask Composio's router to find the right Linear tool, call it, and return results — without ever loading the full Linear API surface into context.

#### How Composio supercharges skills

Recall from Section 6 that an opencode skill is a markdown agent with a system prompt and a permission scope. Composio is where you give that skill **superpowers it didn't have on its own**:

| Skill idea | Tools Composio supplies |
|---|---|
| `ticket-triage` — reads new Linear issues, files duplicates, asks for clarification | Linear (read/comment), GitHub (search issues), Slack (DM author) |
| `pr-reviewer` — reads diffs, runs lint, leaves review comments | GitHub (read PR, post review), Sentry (link related errors) |
| `meeting-notes` — turns a Zoom transcript into a wiki note + Linear tickets | Zoom, Notion or Obsidian, Linear (create issue) |
| `daily-standup` — gathers each agent's progress, posts a digest to Slack | Linear, GitHub, Slack |

The skill's system prompt just says *"You have access to Composio's tool router — use `SEARCH_TOOLS` to find what you need."* You don't have to enumerate tools at build time.

#### Mental model — Composio vs. raw MCP

- **Raw MCP server** (Section 5): one server = one set of tools, all loaded into context. Right for narrow, local capabilities (filesystem, custom internal APIs).
- **Composio MCP**: one server = router into a catalog of 1,000+ tools, loaded on demand. Right for SaaS/business apps and anything where the tool surface is large.

Use both. Local custom MCPs for project-specific glue; Composio for everything off-the-shelf.

---

## 6. Create or find skills (agents) for opencode

In opencode, "skills" are called **agents** — markdown files with a system prompt and a permission scope. There are two kinds:

- **Primary agents** (e.g. Build, Plan) — what you talk to at the top level.
- **Subagents** (e.g. Explore, Scout) — invoked with `@name` in a prompt or by another agent.

### Create one interactively

```bash
opencode agent create
```

It asks for: name, scope (global vs. project), description, permissions (can it edit files? run bash?), and generates the system prompt for you.

### Where the file lives

- Global: `~/.config/opencode/agents/<name>.md`
- Project: `.opencode/agents/<name>.md` (commit this to share with the team)

### Structure

```markdown
---
description: Reviews PRs for security issues before merge
mode: subagent
permission:
  edit: deny
  bash: deny
---
You are a security-focused code reviewer. When invoked, read the diff between
the current branch and `main`, then flag any of: hardcoded secrets, SQL
injection risk, missing auth checks, unsafe deserialization. Be concise.
```

Invoke it inline:

> *"@security-review the changes on this branch."*

### Find community agents

There is no central marketplace yet. The best sources:

- The opencode GitHub repo — search **Discussions** and **Issues** for `agent:` or `skill:` posts: [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)
- The `.opencode/agents/` folder of repos you respect — copy any you like into your own.
- Our org's shared agents will live in **`RethinkLedgers/opencode-agents`** (ask your manager when this is provisioned).

Share one back by opening a PR to the opencode repo or to our shared agents repo.

---

## 7. Paperclip + RethinkLedgers

### What Paperclip is

[Paperclip](https://paperclip.ing) is an open-source platform for **managing AI agents the way you'd manage employees**. You model your organization — org chart, roles, goals, budgets, governance — and Paperclip orchestrates agents inside that structure. Agents have a boss, a job description, a budget, and recurring "heartbeats" that wake them up to do work.

In short:

- **What it is:** a Node.js server + React UI that runs locally or self-hosted.
- **What it manages:** companies, org charts, projects, goals, tickets, budgets, audit trails.
- **What it does *not* do:** generate code or run an LLM itself. You **bring your own agent** — opencode, Claude Code, Cursor, a Python script, an HTTP webhook. Anything that can receive a heartbeat.
- **License:** MIT, self-hosted, no Paperclip account needed.

### Why we're using it for RethinkLedgers

The **RethinkLedgers** organization is the GitHub home for our intern cohort's work building on top of Paperclip. The goal of the internship is to use Paperclip to coordinate a small "company" of AI agents on real tasks, with opencode as the LLM-driving runtime behind each agent.

### Quickstart — run Paperclip locally

In any working directory (a fresh folder is fine):

```bash
npx paperclipai onboard --yes
```

This interactive command:

- Sets up an embedded Postgres + local file storage
- Walks you through creating your first company (name, mission, budget cap)
- Starts the Node.js server and opens the React UI in your browser

No Paperclip account is needed. The UI runs at `http://localhost:3000` by default.

### Wire opencode in as the agent runtime

Inside Paperclip, when you create an agent, you specify how it executes its heartbeats. The simplest pattern:

1. Each agent has a working directory (a git repo it operates on).
2. On each heartbeat, Paperclip writes the agent's current goal + ticket into a prompt file in that directory.
3. Paperclip invokes `opencode` non-interactively to act on that prompt.

A minimal heartbeat command (configured in the agent's settings in the Paperclip UI):

```bash
cd /path/to/agent/workdir && opencode run "$(cat .paperclip/current-prompt.md)"
```

`opencode run "<prompt>"` runs opencode headlessly — no TUI, no manual input — which is what you want for a scheduled agent. Output, costs, and tool calls all flow back to Paperclip for the audit trail.

### Typical Paperclip workflow

1. **Define the company** in the UI — give it a mission and a monthly budget.
2. **Create agents** — give each a title (e.g. "Researcher", "Reviewer"), a system prompt, the opencode `run` command above, and a heartbeat schedule (e.g. every 15 minutes, or on-demand).
3. **File tickets** — these are the unit of work. Assign them to agents.
4. **Watch the audit log** — every tool call, token, and dollar is tracked per agent, project, and goal.
5. **Cap spending** — set hard budget limits so a runaway agent can't burn through credits.

### Where to go from here

- Skim the [Paperclip homepage](https://paperclip.ing) for the high-level pitch.
- Read your first issue in the [RethinkLedgers org](https://github.com/RethinkLedgers) once you're added.
- When you hit something this doc didn't cover, **edit this doc** and open a PR — that's the easiest way to make next month's intern's life better.

---

## 8. The RethinkLedgers Obsidian wiki

Our team's shared knowledge base lives in an **Obsidian vault**. Obsidian is a free, local-first, markdown-based note-taking app — every "note" is just a `.md` file, every "link" is `[[wiki-style]]`, and the whole vault is a regular folder you can put in git. That means our wiki is **the same kind of artifact as our code**: editable in any text editor, version-controlled, and readable by opencode.

> **What lives here:** onboarding context, project briefs, meeting notes, architecture decisions, intern weekly updates, agent prompts that aren't yet codified into opencode skills, and anything else that's prose rather than code. If you're tempted to put it in a Slack message that you'll want to find again in three weeks — put it in the wiki instead.

### 8.1 Install Obsidian

- **macOS:** `brew install --cask obsidian` (or download from [obsidian.md](https://obsidian.md))
- **Windows:** download the installer from [obsidian.md](https://obsidian.md), or `winget install Obsidian.Obsidian`

It's free for personal use, no account required.

### 8.2 Get the shared vault

The shared wiki is a git repo so we get history, blame, and PR review for free.

```bash
git clone git@github.com:RethinkLedgers/<wiki-repo-name>.git ~/Obsidian/RethinkLedgers
```

> **TODO — fill in:** the exact repo name (`<wiki-repo-name>`) is set by your manager during onboarding. If you can't find it, ask in the intern channel.

Then in Obsidian: **Open folder as vault** → pick `~/Obsidian/RethinkLedgers`. Trust the vault when prompted (this lets community plugins run; only do this for vaults you trust, which ours is).

### 8.3 Editing conventions

- **Atomic notes.** One concept per file. If a note grows past ~500 lines, split it.
- **Link liberally.** `[[Note Name]]` to connect things — backlinks are how the wiki gets useful.
- **Use folders for major areas, tags for cross-cutting topics.** Suggested top-level folders: `00 - Onboarding`, `10 - Projects`, `20 - Meetings`, `30 - Decisions`, `40 - People`, `90 - Drafts`.
- **Daily notes for ongoing work.** Use the Daily Notes core plugin; one note per day under `daily/YYYY-MM-DD.md`.
- **Don't paste secrets.** The vault is private but it's still on GitHub. API keys, customer data, anything sensitive — keep it out.

### 8.4 Sync workflow

The vault is just a git repo, so it follows the same rules as Section 4:

```bash
cd ~/Obsidian/RethinkLedgers
git pull               # before you start editing
# ...edit in Obsidian...
git add <files>
git commit -m "Add notes on agent budget escalation"
git push
```

For trivial daily-note updates we let people push straight to `main`. For anything that touches shared docs (project briefs, decisions, onboarding), open a PR so someone can sanity-check it.

> **TODO — fill in:** confirm with your manager which folders require PR review vs. direct push, and whether we use the [Obsidian Git plugin](https://github.com/Vinzent03/obsidian-git) for auto-sync (recommended — it commits and pushes from inside Obsidian on a timer so you never forget).

### 8.5 Let opencode read the wiki

Because the vault is plain markdown, opencode can read it the same way it reads any repo — just `cd` into the vault and ask:

> *"Read everything under `10 - Projects/Paperclip-Heartbeats/` and summarize the open questions."*

For richer use (full-vault search, backlink awareness, tag queries), wire up an Obsidian MCP server in `opencode.json`. A popular option:

```json
{
  "mcp": {
    "obsidian": {
      "type": "local",
      "command": ["npx", "-y", "obsidian-mcp-server"],
      "enabled": true,
      "environment": {
        "OBSIDIAN_VAULT_PATH": "/Users/you/Obsidian/RethinkLedgers"
      }
    }
  }
}
```

With that enabled, opencode can search by tag, follow backlinks, and create new notes in the vault. Useful prompts:

> *"Use the obsidian MCP to find every note tagged `#decision` from the last 30 days and summarize them."*
>
> *"Create a new note `30 - Decisions/2026-05-21 budget-warning-threshold.md` with a summary of the change I just shipped."*

### 8.6 Why a wiki *and* code?

The split is roughly: **code answers "how does it work,"** the **wiki answers "why did we build it this way."** Decisions, tradeoffs, dead ends, and people-context belong in the wiki. PR descriptions and code comments rot fast; a linked wiki note stays findable.

---

## 9. CRM — Twenty and `rethink-labs.twenty.com`

### 9.1 What Twenty is

[Twenty](https://twenty.com) is an open-source CRM — think Salesforce or HubSpot, but MIT-licensed, GraphQL-first, and built for technical teams. It's the #1 open-source CRM on GitHub and the platform we use for tracking people, companies, opportunities, and the work surrounding them.

Why it matters for the internship:

- **Standard CRM primitives.** People, Companies, Opportunities (deals), Notes, Tasks, custom Objects. Pipelines and Kanban views for any object.
- **GraphQL + REST APIs.** Every field on every object is queryable and mutable through the API the moment you create it — no extra config, no schema regeneration.
- **Native MCP server in every Cloud workspace.** This is the part that makes Twenty special for our stack: opencode (and any other MCP-aware agent) can read and write CRM data directly, with workspace-scoped API keys. No glue code required.
- **Custom objects + no-code workflows.** You can model domain-specific entities (e.g. "Onboarding Cohort," "Compliance Filing") without touching the codebase.

### 9.2 `rethink-labs.twenty.com` — our workspace

`rethink-labs.twenty.com` is the **Rethink Labs Twenty Cloud workspace** — the live CRM instance the team runs day-to-day. It's auth-gated (the page just says "Twenty" until you log in), so you need an account on the workspace before you can see anything.

> **TODO — fill in:** who issues workspace invites (likely your manager or an admin on the RethinkLedgers team), and the SSO/email-domain rules for signing in.

What lives there (typical for a sales/ops CRM):

- **People & Companies** — every prospect, customer, partner, and the relationships between them.
- **Opportunities** — deals in flight, with stage, value, owner, and close date.
- **Notes & Tasks** — meeting recaps, follow-ups, internal context attached to a record.
- **Custom objects** — anything Rethink Labs models beyond the defaults. Ask before assuming an object is generic vs. team-specific.

### 9.3 Day-one access checklist

1. Ask your manager for an invite to `rethink-labs.twenty.com`.
2. Sign in, take the in-app tour.
3. **Settings → Members:** confirm your role (Admin vs. Member determines what you can edit and whether you can mint API keys).
4. **Settings → APIs & Webhooks → Generate API key** — create one named `opencode-<your-name>` with a short expiration (30–90 days). You'll use this in Section 9.5 below.
5. Star a few real records (a customer, a deal) so the Home view is useful from the start.

> **Don't experiment in production.** Twenty has no "test mode." If you want to try a workflow or custom object, ask whether to use the prod workspace with a `[TEST]` prefix on the record name, or whether the team maintains a separate sandbox workspace.

### 9.4 Conventions

- **Don't bulk-edit without asking.** The API supports 50k-record imports — easy to nuke a pipeline by accident. Get a second pair of eyes on anything that touches >10 records.
- **Notes > Slack messages.** If a piece of context (customer call summary, blocker, decision) belongs to a record, write it as a Note on that record. Future-you will find it; future-you will not find a Slack thread from August.
- **Use the right object.** Don't put a person's notes on the company record or vice versa. Twenty's join behavior depends on this.
- **Custom field changes are schema changes.** Adding a field is fine; renaming or deleting one can break integrations. Coordinate with the team before changing custom-object schemas.

### 9.5 Connect Twenty to opencode (the fun part)

Because every Twenty Cloud workspace ships a native MCP server, you can give opencode CRM superpowers in three lines of config.

1. Generate an API key in Twenty: **Settings → APIs & Webhooks → Generate API key** (Section 9.3 step 4).
2. Add this to your `opencode.json` (use the per-project config if the key should only apply to one repo, global config otherwise):

   ```json
   {
     "$schema": "https://opencode.ai/config.json",
     "mcp": {
       "twenty": {
         "type": "remote",
         "url": "https://rethink-labs.twenty.com/mcp",
         "enabled": true,
         "headers": {
           "Authorization": "Bearer YOUR_TWENTY_API_KEY"
         }
       }
     }
   }
   ```

3. Restart opencode and run `/mcp` — you should see `twenty` listed alongside any other servers (e.g. `composio`).

> **Keep that key out of git.** If `opencode.json` lives inside a repo, add it to `.gitignore`, or move the secret into an env var and reference it (`"Authorization": "Bearer ${env:TWENTY_API_KEY}"`) where supported.

Now try prompts like:

> *"Use the twenty MCP to list every Opportunity in stage `Negotiation` with a close date this month, sorted by value."*
>
> *"Find the Person record for `jane@acme.com` and add a Note summarizing today's call. Then create a Task for me to follow up next Tuesday."*
>
> *"Show me the Company schema — which custom fields exist on it?"*

### 9.6 Composio vs. native Twenty MCP

Both work, with a useful distinction:

- **Native Twenty MCP** (this section) — direct, low-latency, full schema access including custom objects in our workspace. Best when you want deep CRM work.
- **Composio's Twenty toolkit** (Section 5b) — useful inside cross-app workflows where the same agent also touches Slack, Linear, etc. Slightly less customized to our schema, but you only authenticate once.

Default to the native MCP for CRM-heavy tasks and reach for Composio when you're orchestrating across many apps.

### 9.7 Where to learn more

- [twenty.com](https://twenty.com) — product home, pricing, feature tour
- [twentyhq/twenty on GitHub](https://github.com/twentyhq/twenty) — source, issues, roadmap
- [Twenty docs](https://twenty.com/developers) — GraphQL/REST API reference and MCP setup

---

## Cheat sheet

| Task | Command |
|---|---|
| Install opencode (mac) | `brew install anomalyco/tap/opencode` |
| Install opencode (win) | `scoop install opencode` |
| Add a model provider | `/connect` inside opencode |
| Switch model | `/model` inside opencode |
| List MCP servers | `/mcp` inside opencode |
| Install Composio | `curl -fsSL https://composio.dev/install \| bash` |
| Authenticate Composio | `composio login` |
| Connect an app to Composio | `composio add <github\|slack\|linear\|...>` |
| Create an agent | `opencode agent create` |
| Test SSH to GitHub | `ssh -T git@github.com` |
| Clone private repo | `git clone git@github.com:RethinkLedgers/<repo>.git` |
| Start Paperclip locally | `npx paperclipai onboard --yes` |
| Run opencode headlessly | `opencode run "<prompt>"` |
| Install Obsidian (mac) | `brew install --cask obsidian` |
| Install Obsidian (win) | `winget install Obsidian.Obsidian` |
| Clone the team wiki | `git clone git@github.com:RethinkLedgers/<wiki-repo>.git ~/Obsidian/RethinkLedgers` |
| Open the CRM | [rethink-labs.twenty.com](https://rethink-labs.twenty.com) |
| Generate Twenty API key | Twenty → Settings → APIs & Webhooks |
