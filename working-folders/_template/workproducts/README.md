# Work products

Anything you build during your internship that's small enough to live alongside your notes belongs here.

## What goes here

- Short scripts / one-file utilities
- Design docs and architecture sketches (`.md` with diagrams)
- Spike code that's not yet a real project
- Slides, briefs, write-ups for internal review
- Prompt files for opencode agents you've built

## What does NOT go here

- **Large or active projects** — anything with more than ~20 files, CI/CD, tests, or external contributors. Spin up a dedicated repo: `<project>-<your-name>` under [RethinkLedgers](https://github.com/RethinkLedgers), private, and link it from your top-level `README.md`.
- **Secrets** — API keys, customer data, anything sensitive. The repo is private but mistakes happen and history is hard to scrub. Use 1Password.
- **Generated artifacts** — build outputs, binaries, dependency directories (`node_modules/`, `.venv/`, etc.). Add patterns to the root `.gitignore` if they show up.
- **Anything > ~10 MB per file** — GitHub will warn you, and large files in a git repo are painful forever. Use a shared drive or S3 bucket if you have approved access.

## Organize as it grows

Start flat (just files in this folder). When you have more than ~5 things, group into subfolders by project or theme:

```
workproducts/
├── paperclip-budget-tweaks/
│   ├── proposal.md
│   └── prototype.ts
├── agent-prompts/
│   └── pr-reviewer.md
└── intern-roundup-2026-Q2.md
```

## Naming

- Lowercase, hyphens-not-spaces
- Date-prefix for time-sensitive docs: `2026-05-21-architecture-sketch.md`
- Topic-prefix for evergreen: `agent-prompts-pr-reviewer.md`

## Linking from your top-level README

When you ship a notable work product, add a one-line link to your folder's `README.md` under a `## Highlights` section. Makes evaluation week much easier.
