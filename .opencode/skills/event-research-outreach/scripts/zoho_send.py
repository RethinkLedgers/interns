#!/usr/bin/env python3
"""Send an HTML email as bart@msg2ai.xyz via the Zoho Mail OAuth API.

Uses the refresh-token (self-client) flow. No third-party deps — stdlib only.

Env vars (see references/zoho-setup.md, Method B):
  ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, ZOHO_REFRESH_TOKEN   (required)
  ZOHO_FROM            sender address            [bart@msg2ai.xyz]
  ZOHO_ACCOUNTS_HOST   OAuth host                [accounts.zoho.com]   (.eu for EU DC)
  ZOHO_MAIL_HOST       Mail API host             [mail.zoho.com]       (.eu for EU DC)

Usage:
  python3 zoho_send.py --to person@example.com --subject "Hi" --html draft.html
  python3 zoho_send.py --to a@x.com --cc b@y.com --subject "Hi" --body-text "plain text"

Exit codes: 0 ok, 2 bad args/missing env, 1 API error.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def _env(name, default=None, required=False):
    val = os.environ.get(name, default)
    if required and not val:
        sys.exit(f"[zoho_send] missing required env var: {name} (2)")
    return val


def _post(url, data=None, headers=None, method="POST"):
    body = None
    if data is not None and not isinstance(data, (bytes, str)):
        body = urllib.parse.urlencode(data).encode()
    elif isinstance(data, str):
        body = data.encode()
    elif isinstance(data, bytes):
        body = data
    req = urllib.request.Request(url, data=body, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def refresh_access_token(accounts_host, cid, secret, refresh_token):
    url = f"https://{accounts_host}/oauth/v2/token"
    status, raw = _post(url, {
        "grant_type": "refresh_token",
        "client_id": cid,
        "client_secret": secret,
        "refresh_token": refresh_token,
    }, headers={"Content-Type": "application/x-www-form-urlencoded"})
    data = json.loads(raw) if raw else {}
    token = data.get("access_token")
    if not token:
        sys.exit(f"[zoho_send] token refresh failed ({status}): {raw} (1)")
    return token


def get_account_id(mail_host, token, from_addr):
    url = f"https://{mail_host}/api/accounts"
    status, raw = _post(url, headers={"Authorization": f"Zoho-oauthtoken {token}"}, method="GET")
    if status != 200:
        sys.exit(f"[zoho_send] /api/accounts failed ({status}): {raw} (1)")
    data = json.loads(raw).get("data", [])
    # Prefer the account whose primary/send address matches ZOHO_FROM.
    for acc in data:
        addrs = {acc.get("primaryEmailAddress", "").lower()}
        for sm in acc.get("sendMailDetails", []) or []:
            addrs.add(str(sm.get("fromAddress", "")).lower())
        if from_addr.lower() in addrs:
            return str(acc.get("accountId"))
    if data:
        return str(data[0].get("accountId"))
    sys.exit("[zoho_send] no Zoho accounts returned (1)")


def send(mail_host, token, account_id, payload):
    url = f"https://{mail_host}/api/accounts/{account_id}/messages"
    status, raw = _post(url, json.dumps(payload), headers={
        "Authorization": f"Zoho-oauthtoken {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    ok = status in (200, 201)
    print(f"[zoho_send] send status={status} {raw[:400]}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--to", required=True)
    ap.add_argument("--cc")
    ap.add_argument("--bcc")
    ap.add_argument("--subject", required=True)
    ap.add_argument("--html", help="path to an HTML file (email body)")
    ap.add_argument("--body-text", help="plain-text body (alternative to --html)")
    ap.add_argument("--from", dest="from_addr", default=os.environ.get("ZOHO_FROM", "bart@msg2ai.xyz"))
    args = ap.parse_args()

    if not args.html and not args.body_text:
        sys.exit("[zoho_send] provide --html FILE or --body-text TEXT (2)")
    if args.html:
        with open(args.html, "r", encoding="utf-8") as fh:
            content, mail_format = fh.read(), "html"
    else:
        content, mail_format = args.body_text, "plaintext"

    cid = _env("ZOHO_CLIENT_ID", required=True)
    secret = _env("ZOHO_CLIENT_SECRET", required=True)
    refresh_token = _env("ZOHO_REFRESH_TOKEN", required=True)
    accounts_host = _env("ZOHO_ACCOUNTS_HOST", "accounts.zoho.com")
    mail_host = _env("ZOHO_MAIL_HOST", "mail.zoho.com")

    token = refresh_access_token(accounts_host, cid, secret, refresh_token)
    account_id = get_account_id(mail_host, token, args.from_addr)

    payload = {
        "fromAddress": args.from_addr,
        "toAddress": args.to,
        "subject": args.subject,
        "content": content,
        "mailFormat": mail_format,
    }
    if args.cc:
        payload["ccAddress"] = args.cc
    if args.bcc:
        payload["bccAddress"] = args.bcc

    sys.exit(0 if send(mail_host, token, account_id, payload) else 1)


if __name__ == "__main__":
    main()
