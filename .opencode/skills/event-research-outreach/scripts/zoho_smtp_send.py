#!/usr/bin/env python3
"""Send an HTML email as bart@msg2ai.xyz via Zoho SMTP using an app password.

Stdlib only (smtplib). See references/zoho-setup.md, Method A.

Env vars:
  ZOHO_SMTP_HOST   [smtppro.zoho.com]   (smtp.zoho.com personal; *.zoho.eu for EU DC)
  ZOHO_SMTP_PORT   [465]                 (465 = SSL, 587 = STARTTLS)
  ZOHO_SMTP_USER   [bart@rtledgers.com]  PRIMARY mailbox login — an alias such as
                                         bart@msg2ai.xyz usually fails SMTP auth
  ZOHO_SMTP_PASS   (required)            Zoho app-specific password
  ZOHO_FROM        [ZOHO_SMTP_USER]      From: address

Usage:
  python3 zoho_smtp_send.py --to person@example.com --subject "Hi" --html draft.html
  python3 zoho_smtp_send.py --to a@x.com --cc b@y.com --subject "Hi" --body-text "..."

Exit codes: 0 ok, 2 bad args/missing env, 1 send error.
"""
import argparse
import os
import smtplib
import ssl
import sys
from email.message import EmailMessage


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--to", required=True)
    ap.add_argument("--cc")
    ap.add_argument("--bcc")
    ap.add_argument("--subject", required=True)
    ap.add_argument("--html")
    ap.add_argument("--body-text")
    args = ap.parse_args()

    host = os.environ.get("ZOHO_SMTP_HOST", "smtppro.zoho.com")
    port = int(os.environ.get("ZOHO_SMTP_PORT", "465"))
    user = os.environ.get("ZOHO_SMTP_USER", "bart@rtledgers.com")  # primary login, NOT an alias
    password = os.environ.get("ZOHO_SMTP_PASS")
    from_addr = os.environ.get("ZOHO_FROM", "bart@msg2ai.xyz")     # the alias to send AS
    if not password:
        sys.exit("[zoho_smtp] missing ZOHO_SMTP_PASS (app password) (2)")
    if not args.html and not args.body_text:
        sys.exit("[zoho_smtp] provide --html FILE or --body-text TEXT (2)")

    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = args.to
    if args.cc:
        msg["Cc"] = args.cc
    msg["Subject"] = args.subject

    if args.html:
        with open(args.html, "r", encoding="utf-8") as fh:
            html = fh.read()
        msg.set_content("This email requires an HTML-capable client.")
        msg.add_alternative(html, subtype="html")
    else:
        msg.set_content(args.body_text)

    rcpts = [args.to]
    if args.cc:
        rcpts += [a.strip() for a in args.cc.split(",") if a.strip()]
    if args.bcc:
        rcpts += [a.strip() for a in args.bcc.split(",") if a.strip()]

    ctx = ssl.create_default_context()
    try:
        if port == 465:
            with smtplib.SMTP_SSL(host, port, context=ctx, timeout=30) as s:
                s.login(user, password)
                s.send_message(msg, from_addr=from_addr, to_addrs=rcpts)
        else:  # 587 STARTTLS
            with smtplib.SMTP(host, port, timeout=30) as s:
                s.ehlo()
                s.starttls(context=ctx)
                s.login(user, password)
                s.send_message(msg, from_addr=from_addr, to_addrs=rcpts)
    except Exception as e:  # noqa: BLE001
        sys.exit(f"[zoho_smtp] send failed: {e} (1)")
    print(f"[zoho_smtp] sent to {rcpts} via {host}:{port}")


if __name__ == "__main__":
    main()
