#!/usr/bin/env bash
# Verify a single email address with hunter.io before outreach.
# Usage:  HUNTER_API_KEY=xxxx ./hunter_verify.sh person@example.com
# Prints a one-line verdict; exits 0 ONLY if result == "deliverable" (or status == "valid").
# Fail-closed: any missing key / bad response / parse error -> non-zero (treat as unverified).
# Docs: https://hunter.io/api-documentation/v2#email-verifier
set -euo pipefail

EMAIL="${1:-}"
if [[ -z "$EMAIL" ]]; then echo "usage: hunter_verify.sh <email>" >&2; exit 2; fi
if [[ -z "${HUNTER_API_KEY:-}" ]]; then echo "missing HUNTER_API_KEY" >&2; exit 2; fi

# URL-encode the address for the query string (@ and + matter for plus-addressing).
ENC="$(printf '%s' "$EMAIL" | sed -e 's/%/%25/g' -e 's/@/%40/g' -e 's/+/%2B/g')"
RESP="$(curl -sS "https://api.hunter.io/v2/email-verifier?email=${ENC}&api_key=${HUNTER_API_KEY}")"

if command -v python3 >/dev/null 2>&1; then
  # Pass email + raw response as ARGV (not stdin) so the program and its data don't collide.
  python3 -c '
import json, sys
email, raw = sys.argv[1], sys.argv[2]
try:
    data = json.loads(raw).get("data", {})
except Exception as e:
    print(f"{email}: verify_error (unparseable response: {e})"); sys.exit(1)
status = data.get("status", "unknown")     # valid|invalid|accept_all|webmail|disposable|unknown
result = data.get("result", status)        # deliverable|risky|undeliverable|unknown
score  = data.get("score")
print(f"{email}: result={result} status={status} score={score}")
sys.exit(0 if (result == "deliverable" or status == "valid") else 1)
' "$EMAIL" "$RESP"
else
  # Fallback if python3 is unavailable: crude but safe (fails closed on anything but a clean match).
  echo "$RESP"
  echo "$RESP" | grep -q '"result":"deliverable"' && exit 0 || exit 1
fi
