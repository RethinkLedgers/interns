# RethinkLedgers — Intern Onboarding

Welcome. This guide walks you through everything you need to be productive on day one:

1. Install **opencode** (terminal AI coding agent) on macOS or Windows
2. Pick a **free model** so you don't need a paid API key
3. Set up **GitHub + SSH** so you can clone, pull, and push private repos
4. Sync work between your laptop and GitHub, and the commands to give opencode
5. Connect **MCP servers** to opencode — including **Composio** for managed app authentication
6. Create or find **skills (agents)** for opencode
7. Get oriented on **Paperclip** and how to use opencode as its underlying LLM
8. Use the **shared Obsidian wiki** as the team's knowledge base
9. Work in **Twenty CRM** at `rethink-labs.twenty.com` and wire it into opencode
10. Join **Happenstance + Rethink Labs** with your msg2ai email

> If anything in this doc is wrong or stale, fix it in the repo and open a PR. Don't suffer in silence.

### How to use opencode (quick start)

When you run `opencode` in a terminal, it opens an interactive chat. Just type what you want in plain English — for example:

- *"Create a file called hello.py that prints 'Hello World'"*
- *"Show me the files in this directory"*
- *"Edit index.html and change the title to 'My Site'"*

Opencode will read your files, write code, run commands, and show you what it's doing. You don't need to learn special commands — just describe the task.

**Tips for beginners:**
- Be specific: say *which* file and *what* to change
- If opencode does something you don't expect, type `undo` to revert the last change
- Type `/help` anytime to see available commands
- Use `opencode run "your task"` to run it headlessly (non-interactive)

### How to read this document more clearly

This is a **Markdown** file (`.md`). To view it with proper formatting (bold text, clickable links, etc.), download a markdown viewer:

- **Any platform:** Use **VS Code** (right-click → Open with → VS Code), or install a Markdown reader like [MarkText](https://github.com/marktext/marktext), [Obsidian](https://obsidian.md), or [Typora](https://typora.io) — all work on **Mac, Windows, and Linux**

Once you have one, open this file in that app to see headings, bullet points, code blocks, and links rendered cleanly.

## 2. Install opencode

**What is opencode?** opencode is an AI coding assistant that runs in your terminal (the black window where you type commands). You type or say what you want to build, and it writes code, runs commands, and edits files for you.

### macOS

**Video walkthrough:** Watch [youtube.com/watch?v=3POcXtKkMtw](https://www.youtube.com/watch?v=3POcXtKkMtw) for a visual guide to installing opencode on macOS. Skip 3:11–3:49 — that part covers VS Code's built-in terminal, which you don't need unless you already use VS Code.

**Before you start — do you have Homebrew?** Homebrew is a tool that installs other software on Mac. Open your Terminal app (search for "Terminal" in Spotlight). Type this and press Enter:

```bash
brew --version
```

- If you see `Homebrew` followed by a version number, you're all set.
- If you see `command not found: brew`, install Homebrew first by running:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
  Follow the on-screen prompts (you may need to enter your Mac password). This can take a few minutes.

**Install opencode using Homebrew (recommended):**

```bash
brew install anomalyco/tap/opencode
```

Wait for it to finish — you'll see a progress bar, then a message like `🍺 /opt/homebrew/Cellar/opencode/...` to confirm success.

**Refresh your terminal** so it knows about the new program you just installed:

```bash
source ~/.zshrc
```

(Or just close and reopen your Terminal window.)

**Verify the installation:**

```bash
opencode --version
```

You should see something like `v0.x.x`. If you see `command not found`, go back and run `source ~/.zshrc`, or open a fresh Terminal window.

### If you're on Windows

**Windows Subsystem for Linux (WSL2) is strongly recommended** — everything in this guide works the same way inside WSL.

**Option A — WSL2 (recommended).** Open PowerShell as Administrator (right-click PowerShell → "Run as administrator"):

```powershell
wsl --install -d Ubuntu
```

Your computer will restart. After that, launch "Ubuntu" from the Start menu. It will finish setting up and ask you to create a username and password. Now you're on Linux — follow the macOS Homebrew instructions above (yes, inside Ubuntu the Mac instructions work).

**Option B — Native Windows via Scoop.** In PowerShell:
```powershell
scoop install opencode
```

**Option C — npm.** If you have Node 18+ already:
```powershell
npm install -g opencode-ai
```

Verify:
```powershell
opencode --version
```

### First launch (everyone)

In any project folder, type:

```bash
opencode
```

The first time you run this, opencode will say something like "No API provider configured" and ask you to pick one. **Do not pick anything yet** — go to section 2 first to set up a free model. When you come back, you'll use the `/connect` command to add the provider.

---

## 2. Pick a free model

**What is a "model"?** Think of a model as the AI brain that powers opencode. Different models have different strengths — some are better at coding, some are faster, some are free.

**What is an "API key"?** A secret code that proves you're allowed to use a particular model provider. You get it from the provider's website and paste it into opencode.

**Which one should you pick?** Start with **DeepSeek V4 via OpenRouter** — it's free and excellent at coding.

### Recommended: DeepSeek V4 through OpenRouter

**Step 1 — Create an OpenRouter account**

Go to [openrouter.ai](https://openrouter.ai) in your web browser.

Click the **Sign Up** or **Get Started** button. You can sign up with your Google account (click the Google button) or with any email address. Use your **msg2ai email** (the one your manager gave you for work).

Once you're signed in, you'll land on the OpenRouter dashboard.

**Step 2 — Create an API key**

On the left sidebar, click **Keys** (or go to [openrouter.ai/keys](https://openrouter.ai/keys)).

Click the **Create Key** button. A popup will appear showing a long string of random letters and numbers — **this is your API key**. Copy it to your clipboard (click the copy icon or select it and press Cmd+C on Mac / Ctrl+C on Windows).

⚠️ **Important:** This is the only time you'll see this key. If you lose it, you'll need to create a new one.

**Step 3 — Add the key to opencode**

In your terminal (where opencode is running or where you're about to run it), opencode uses a command called `/connect` to add API providers.

If you already ran `opencode` and it prompted you to pick a provider:
- You'll see a list of providers. Type `OpenRouter` (or scroll to it with arrow keys) and press Enter.
- It will ask for your API key. Paste it (Cmd+V on Mac, Ctrl+V on Windows — or right-click → Paste in some terminals).
- Press Enter.

If you haven't run opencode yet:
- Run `opencode` from your terminal.
- When asked to pick a provider, choose **OpenRouter** and paste your key.

**Step 4 — Select the DeepSeek V4 model**

After pasting your API key, opencode will show a list of available models. Look for one called **DeepSeek V4** — it may appear as something like `deepseek/deepseek-v4` or `deepseek/deepseek-chat-v4:free`.

Use the arrow keys to scroll to it and press Enter.

If you don't see DeepSeek V4 in the list:
1. Type `/model` and press Enter
2. Search for "deepseek v4" or "deepseek/deepseek"
3. Select the one with `:free` at the end if available

**That's it.** You now have a free AI coding assistant running on DeepSeek V4.

### Alternative: Google Gemini (also free, huge daily quota)

If OpenRouter isn't working for you or you want a backup:

1. Go to [aistudio.google.com](https://aistudio.google.com).
2. Sign in with your Google account (use your msg2ai email).
3. Click **Get API key** → **Create API key**.
4. Copy the key that appears.
5. In opencode, type `/connect`, choose **Google Gemini**, paste the key.
6. When asked to pick a model, choose `gemini-2.5-pro`.

### Switching models later

Want to try a different model later? Inside opencode, type:

```
/model
```

This shows the model list again — pick a new one anytime. You can add multiple providers by running `/connect` again.

Need to check which provider and model you're currently using? Type `/model` and it will show your current selection.

---

## 3. Set up GitHub and SSH

**What is GitHub?** GitHub is a website that stores and manages code. Think of it as Google Drive for code — your team's code lives there, and you download it to your laptop to work on it, then upload your changes back.

**Why SSH?** Normally every time you download or upload code, GitHub would ask for your username and password. SSH keys skip that — you set it up once and it just works. You'll generate a pair of keys: a **private key** (like a key, stays on your laptop) and a **public key** (like a lock, you give it to GitHub).

### 3.1 Create a GitHub account (if you don't have one)

If you already have a GitHub account, you can skip to step 3.

**Step 1 — Sign up**

Open your web browser and go to [github.com/signup](https://github.com/signup).

Enter:
- **Email:** Use your **msg2ai email** (the work email your manager gave you).
- **Password:** Create a strong password (use a password manager like 1Password if you have one).
- **Username:** Choose something professional — ideally your first and last name (e.g. `ariannacant`). This will be your GitHub identity.
- Verify you're human (the puzzle they show you).

Click **Create account**.

**Step 2 — Verify your email**

GitHub will send a confirmation code to your msg2ai email. Open your email inbox, find the message from GitHub, and enter the code on the verification page.

**Step 3 — Turn on two-factor authentication (2FA)**

**What is 2FA?** An extra layer of security. Even if someone guesses your password, they can't log in without a code from your phone. The RethinkLedgers organization requires this.

1. In GitHub, click your profile picture (top-right corner) → **Settings**.
2. In the left sidebar, click **Password and authentication**.
3. Scroll down to "Two-factor authentication" and click **Enable two-factor authentication**.
4. Choose **Authenticator app** (not SMS).
5. Open your authenticator app on your phone:
   - Don't have one? Install **Google Authenticator** (iOS/Android), **Authy**, or use **1Password** if you have it.
   - Scan the QR code shown on GitHub with your authenticator app.
   - Enter the 6-digit code from the app into GitHub to confirm.
6. Save your recovery codes (GitHub shows you a list of one-time use codes — save them in your password manager or take a screenshot).

**Step 4 — Tell your manager your GitHub username**

Look at the top-left corner of any GitHub page. You'll see a dropdown that says something like "Personal account" and below it your username (e.g. `ariannacant`).

Send an email to your manager with your GitHub username so they can invite you to the **RethinkLedgers** organization. You won't be able to see any of the team's repos until they do this.

### 3.2 Install git (if needed)

**What is git?** The program that downloads and uploads code between your laptop and GitHub.

Check if you already have it. In your terminal:

```bash
git --version
```

If you see something like `git version 2.x.x`, you already have it and can skip installation.

**If you need to install it:**

- **macOS:** Run `brew install git` in your terminal. (If `brew` isn't installed, run `xcode-select --install` instead — this installs Apple's version of git.)
- **Windows (WSL):** `sudo apt update && sudo apt install git -y`
- **Windows (native):** Download from [git-scm.com/download/win](https://git-scm.com/download/win) and run the installer.

**Tell git who you are** (do this once):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-msg2ai-email@example.com"
```

Replace `"Your Full Name"` with your actual name (e.g. `"Arianna Cant"`) and the email with your actual msg2ai email.

### 3.3 Generate an SSH key

Think of this as creating a key and a lock. The **private key** (the actual key) stays on your laptop. The **public key** (the lock) goes to GitHub.

In your terminal, run:

```bash
ssh-keygen -t ed25519 -C "your-msg2ai-email@example.com"
```

Replace the email with your actual msg2ai email. Here's what each part means:
- `ssh-keygen` = the program that creates keys
- `-t ed25519` = the type of key (ed25519 is modern and secure)
- `-C "..."` = a comment/label so you remember what this key is for

**What you'll see next:**

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/you/.ssh/id_ed25519):
```

Just press **Enter** to accept the default location. (Don't type anything — just press Enter.)

Then it will ask:

```
Enter passphrase (empty for no passphrase):
```

**Set a passphrase** — yes, it's annoying, but it protects your key if your laptop is lost or stolen. Type something you'll remember (or use a password manager). You'll need to type it again to confirm:

```
Enter same passphrase again:
```

Type the same passphrase and press Enter.

When it finishes, you'll see something like:

```
The key fingerprint is:
SHA256:... your-msg2ai-email@example.com
```

This means your key was created. Two files were saved:
- `~/.ssh/id_ed25519` — your **private key** (never share this!)
- `~/.ssh/id_ed25519.pub` — your **public key** (this is the one you'll give to GitHub)

### 3.4 Register your key with your computer (ssh-agent)

The **ssh-agent** is a program that remembers your passphrase so you don't have to type it every time you connect to GitHub.

**On macOS:**

Run these two commands, one at a time:

```bash
eval "$(ssh-agent -s)"
```

This starts the ssh-agent. You should see: `Agent pid XXXXX` (the number will be different).

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

This adds your key to the agent. It will ask for the passphrase you set in step 3.3. Type it and press Enter. You should see: `Identity added: /Users/you/.ssh/id_ed25519 (your-email@example.com)`

The `--apple-use-keychain` part tells macOS to save your passphrase in your login keychain (the same place your Mac passwords are stored) so you won't be asked again.

**Create the SSH config file** so your computer knows to use this key for GitHub automatically:

```bash
nano ~/.ssh/config
```

This opens a simple text editor. Paste in the following (use Cmd+V on Mac or Ctrl+Shift+V in most terminals):

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Press **Ctrl+X** to exit, then press **Y** to confirm saving, then press **Enter** to keep the same filename.

(If you prefer a visual editor, you can use `open -a TextEdit ~/.ssh/config` instead of `nano`.)

**On Windows (WSL):**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**On Windows (native PowerShell):**

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

### 3.5 Add your public key to GitHub

Now you need to give GitHub your "lock" (the public key). 

**Step 1 — Copy your public key**

In your terminal, run:

```bash
# On macOS:
pbcopy < ~/.ssh/id_ed25519.pub

# On WSL / Linux:
cat ~/.ssh/id_ed25519.pub   # then select and copy the output by hand

# On Windows PowerShell:
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | clip
```

(If you're on macOS and `pbcopy` doesn't work, run `cat ~/.ssh/id_ed25519.pub`, select the output with your mouse, and copy it manually.)

**Step 2 — Go to GitHub SSH settings**

Open your web browser and go to [github.com/settings/keys](https://github.com/settings/keys).

Or navigate there manually:
1. Click your profile picture (top-right corner of GitHub).
2. Click **Settings**.
3. In the left sidebar, click **SSH and GPG keys**.

**Step 3 — Add the key**

1. Click the green **New SSH key** button (top-right).
2. **Title:** Enter a label to remember which computer this key is for — e.g. `laptop-mac-2026` or `office-windows`.
3. **Key type:** Leave as "Authentication Key" (the default).
4. **Key:** Click inside the big text box and press **Cmd+V** (Mac) or **Ctrl+V** (Windows) to paste your public key. It should look like a long string starting with `ssh-ed25519 AAA...`.
5. Click **Add SSH key**.

GitHub will ask you to confirm your password. Enter it and click **Confirm**.

### 3.6 Test the connection

Let's make sure everything is wired up correctly. In your terminal:

```bash
ssh -T git@github.com
```

**If everything is set up correctly**, you'll see:

```
Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

This message is **the success message** — it means GitHub knows who you are and your SSH key is working. The "does not provide shell access" part is normal; GitHub only lets you interact with repos, not log in as a user.

**If something is wrong**, you might see:

```
git@github.com: Permission denied (publickey).
```

This usually means:
- Your key wasn't added to the ssh-agent (go back to section 3.4)
- You didn't paste the key correctly in GitHub's settings (go back to section 3.5)
- You need to wait a moment and try again

### 3.7 Clone a private repo (download the team's code)

Now that everything is set up, you can download (clone) the team's repos.

**Important:** Always use the **SSH** URL (starts with `git@github.com:`) — not the HTTPS URL (starts with `https://github.com/`). SSH URLs work with the key you just set up; HTTPS URLs will ask you for a password every time.

To clone this repo (the one containing this onboarding guide):

```bash
git clone git@github.com:RethinkLedgers/interns.git
cd interns
```

The `git clone` command downloads the repo. The `cd interns` command moves you into that folder.

When it finishes, you'll see the repo's files on your computer. You're all set.

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

### Your personal working folder in this repo

Inside this repo, every intern gets a folder at `working-folders/<your-firstname>/` for your profile, weekly progress reports, and small work products.

**Create yours on day one** as your first PR:

```bash
cp -r working-folders/_template working-folders/<your-firstname>
git add working-folders/<your-firstname>
git commit -m "Add working folder for <your-firstname>"
git push -u origin <your-firstname>/setup
```

(Use a branch and PR — don't push straight to `main`. See Section 4 above.)

The template includes:

- `README.md` — fill in your bio, project, and contact info
- `progress-reports/` — drop one markdown file per week, every Friday EOD
- `workproducts/` — small things you build that live alongside your notes

See [`working-folders/README.md`](./working-folders/README.md) in this repo for the full convention and rules. **Weekly progress reports are required** — they're the main thing your manager and Arianna read before your 1:1.

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

### 5b. Composio — managed authentication for 1,000+ apps

The hard part of connecting an AI agent to a real app — GitHub, Slack, Linear, Gmail, Notion — is almost never the API call itself. It's **authentication**: OAuth handshakes, storing tokens, refreshing them before they expire, juggling scopes, and keeping each person's credentials separate. Doing that by hand for every app and every intern is a maintenance sinkhole.

**[Composio](https://composio.dev)** exists to handle exactly that. Think of it as a **managed authentication layer for AI agents**: you authorize an app **once** through Composio's OAuth flow, and Composio securely stores and refreshes those credentials from then on. opencode — or any other AI harness (Claude Code, Cursor, a custom agent) — can then act on that app **without ever touching the credentials itself**.

Composio brokers 1,000+ apps this way through a single MCP connection. It also routes tool calls on demand, so opencode only loads the handful of tools a task actually needs instead of thousands of definitions — but the headline feature is the auth: **connect once, and every agent you build inherits that connection.**

This is why Composio matters for two things you'll do constantly: **building skills** (a skill needs authenticated access to specific apps — Composio supplies it) and **connecting to APIs** (authenticate through Composio once, and never hand-wire an OAuth flow again).

#### Install Composio

```bash
curl -fsSL https://composio.dev/install | bash
composio login
```

`composio login` opens a browser to authenticate. Free tier is fine for the internship.

#### Authenticate the apps you'll use (the one-time step)

From the terminal, link the apps your work needs. Each command opens an OAuth flow in the browser — this is the **one** time you log in; Composio holds and refreshes the connection afterward:

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

- **Raw MCP server** (Section 5): one server = one set of tools you wire up and authenticate yourself. Right for narrow, local capabilities (filesystem, custom internal APIs) where there's no login to manage.
- **Composio MCP**: one connection = managed authentication plus on-demand access to a catalog of 1,000+ apps. Right for anything that needs a login — Composio owns the OAuth tokens and refreshes them, so opencode never sees a raw credential.

Use both. Local custom MCPs for project-specific glue; Composio for every off-the-shelf app that needs you to log in.

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

## 10. Join Happenstance + Rethink Labs

**What is Happenstance?** [Happenstance](https://happenstance.ai) is an AI-powered networking platform the team uses to stay connected. Joining the Rethink Labs group on Happenstance is how you'll receive invitations to team events, see who else is in the org, and tap into the network.

**Step 1 — Sign up**

Go to [happenstance.ai](https://happenstance.ai) and create an account. **You must sign up with your msg2ai email** (the work email your manager gave you) — that's how the system knows you belong to Rethink Labs and automatically sends you the group invitation.

**Step 2 — Accept the group invite**

Once you've signed up, ask your manager to send you the Rethink Labs group invitation, or check your msg2ai inbox for an auto-invite. Follow the link to join.

**Step 3 — Set up your profile**

Add your name, role (e.g. "Intern"), and a photo so the team can recognize you.

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
| Authenticate an app via Composio | `composio add <github\|slack\|linear\|...>` |
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
