# Tools

Standalone tooling that supports the intern program — kept out of the onboarding docs so
the guides stay focused.

| Tool | What it is |
| --- | --- |
| [`trello-integration/`](./trello-integration/) | Drive Trello from Claude via **Composio** (create/update cards, checklists, comments). Setup guide + a helper script. |
| [`trello-powerup/`](./trello-powerup/) | A parked **"Plan → Cards"** Trello Power-Up (turns a plan's `## Phase N` sections into cards from the Trello UI). |

> Secrets stay out of git: `.env*` and `.opencode/` are gitignored. Only example configs
> (`.env.example`) and docs are tracked here.
