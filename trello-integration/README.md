# Trello ↔ Claude integration (via Composio)

Goal: let **Claude drive Trello automatically** — create cards, update/move them, add
checklists, and post comments — using **Composio** as the managed-auth layer (the same
tool the team already uses for app authentication).

Once connected, you can just ask Claude things like *"create a Trello card for each phase
of Ivy's plan"* or *"move the 'Outreach prep' card to Done and comment with the result,"*
and it will call the Trello tools directly.

> This folder holds **setup helpers + docs**. No secrets are committed: `.env` is
> gitignored and credentials live in your local Composio/Claude config, not in the repo.

---

## Setup — fast path (the Composio CLI is already installed)

The `composio` CLI is present on this machine, so this is the shortest route. The only
human-gated steps are the two browser logins (Composio, then Trello).

### 1. Authenticate the Composio CLI to your org
```bash
composio login        # opens your browser; signs the CLI into YOUR Composio org
composio whoami       # should now show your real email (not a pg-test-… identity)
```
> Tip: in Claude Code, run interactive logins with a leading `!` (e.g. `! composio login`)
> so the output lands in the session and Claude can continue immediately.

### 2. Connect your Trello account
```bash
composio link trello  # returns an OAuth link — approve Composio's access to Trello
```

### 3. That's it — Claude can now drive Trello
Claude (or you) can call tools straight through the CLI, e.g.:
```bash
composio execute TRELLO_CREATE_CARD -d '{ "name": "Smoke test", "idList": "<listId>" }'
composio search "create card" "get my boards" --toolkits trello --human   # discover slugs
```
Verify by asking Claude to create a test card, or run a read tool like `TRELLO_GET_BOARDS`.

---

## Optional — native MCP tools inside Claude Code

If you'd rather have Trello as first-class tools (instead of Claude shelling out to
`composio execute`), register a Composio MCP server. Helper: `generate_mcp_url.py`.

```bash
cp .env.example .env                 # set COMPOSIO_API_KEY + USER_ID  (.env is gitignored)
pip install -r requirements.txt
python generate_mcp_url.py           # prints the MCP URL + the claude mcp add command
```
Then add it at **local** scope (keeps the key out of git — do NOT use `--scope project`):
```bash
claude mcp add --transport http trello-composio "YOUR_MCP_URL" \
  --headers "X-API-Key:YOUR_COMPOSIO_API_KEY"
exit && claude
claude mcp list                      # should list: trello-composio
```

---

## Driving updates *automatically* on events

For "push a Trello update every time a PR merges / a task finishes," add a **hook** in
`.claude/settings.json` that runs a `composio execute TRELLO_…` (or curl) command on the
event. Ask and we'll wire one up after the connection is verified.

## Security notes
- Credentials stay **out of git**: `.env` is ignored; only `.env.example` is tracked.
- Trello tokens are held by Composio (encrypted), not in this repo.
- Treat the Composio API key like any credential — rotate it from the dashboard if exposed.

## Source
Composio's official guide: <https://composio.dev/toolkits/trello/framework/claude-code>

---

*Related but separate:* `../trello-powerup/` is a parked **Trello Power-Up** (for interns to
turn a plan into cards from the Trello UI). Complementary to this Claude-side integration.
