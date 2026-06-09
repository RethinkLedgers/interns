#!/usr/bin/env python3
"""
Generate a Composio Tool Router MCP URL for the Trello toolkit.

This URL is what you paste into `claude mcp add` so Claude Code can drive Trello
(create/update cards, checklists, comments) on your behalf.

Setup:
    pip install -r requirements.txt        # composio-core, python-dotenv
    cp .env.example .env                    # then edit .env with real values

Run:
    python generate_mcp_url.py

Security: .env is gitignored — your COMPOSIO_API_KEY never lands in git.
Source: https://composio.dev/toolkits/trello/framework/claude-code
"""
import os
import sys

try:
    from composio import Composio
except ImportError:
    sys.exit(
        "Missing dependency. Run:  pip install -r requirements.txt\n"
        "If `from composio import Composio` still fails, check Composio's current\n"
        "SDK package name in their docs (the import has changed across versions)."
    )

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # optional — fine if you export the env vars yourself

api_key = os.getenv("COMPOSIO_API_KEY")
user_id = os.getenv("USER_ID")

if not api_key or not user_id:
    sys.exit("Set COMPOSIO_API_KEY and USER_ID first (copy .env.example -> .env and fill them in).")

client = Composio(api_key=api_key)
session = client.create(user_id=user_id, toolkits=["trello"])
mcp_url = session.mcp.url

print("\n=== Composio MCP URL (Trello toolkit) ===\n")
print(mcp_url)
print("\n=== Add it to Claude Code (LOCAL scope keeps your key out of git) ===\n")
print(f'claude mcp add --transport http trello-composio "{mcp_url}" \\')
print('  --headers "X-API-Key:<paste-your-COMPOSIO_API_KEY-here>"')
print("\nThen restart Claude Code and verify with:  claude mcp list\n")
