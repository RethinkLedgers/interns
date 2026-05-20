# ActionNotes.AI — Intern Onboarding & Testing Guide

> **Welcome!** This guide is for new intern testers joining the ActionNotes.AI
> team. No coding background needed. By the end you'll know what the product
> does, where to log in, and exactly how to test each feature.

---

## 1. What Is ActionNotes.AI?

**One-liner:** *Turn Conferences Into Closed Deals.*

ActionNotes helps people at conferences and events capture everything they
see, hear, and meet — and then have AI turn it into a tidy follow-up plan
the next morning.

Imagine you spend a day at a big conference. You meet 30 people, snap photos
of 12 business cards, scribble notes on three sessions, and record two voice
memos in the hallway. The next day you're staring at a pile of chaos.
**ActionNotes turns that pile into:**

- a clean **summary** of your day,
- a list of **action items** ("email Sarah the deck by Friday"),
- a **contact directory** with draft follow-up emails ready to send,
- and a downloadable **End of Day Report** you can email to yourself or your team.

That's the whole product, in one paragraph.

---

## 2. The Two Versions You'll Use

ActionNotes has **two live versions** of the app. They look almost identical,
but they serve different purposes. As a tester, you'll spend nearly all your
time on **Dev**.

### 🧪 Dev — the testing playground

**URL:** <https://dev.actionnotes.ai>

This is where new features land first. Things may occasionally be broken,
buggy, or weird-looking — that's the whole point: **your job is to find those
problems before they reach real customers.** Feel free to create test
accounts, upload silly notes, click everything.

**Important things to know about Dev:**

- "Sign in with Google" **doesn't work on Dev** — you'll see a friendly error.
  Use email + password sign-up instead.
- If you're testing the paid plans, use this **fake credit card** (Stripe test mode):
  - Card number: `4242 4242 4242 4242`
  - Expiry: any future date (e.g. `12/30`)
  - CVC: any three digits (e.g. `123`)
  - ZIP: any (e.g. `10001`)
- Nothing you do here charges real money or emails real customers.

### 🚀 Prod — the live customer site

**URL:** <https://www.actionnotes.ai>

This is the real product that paying customers use. **Don't test on Prod.**
Visit it only if:

- You're checking that a fix has shipped (someone will tell you when).
- You're showing the product to a friend who might want to sign up.
- A team member explicitly asks you to reproduce a bug there.

If you create an account on Prod, use a real card only if you actually intend
to subscribe. Anything you do here is real.

> **Rule of thumb:** When in doubt, use **Dev**. The URL bar tells you which
> version you're on — *always glance at it before you click anything important.*

---

## 3. What's Inside the App — A Feature Tour

Here's everything you can do in ActionNotes, grouped by what a user would
look for in the menu.

### 📝 Capture notes

The heart of the product. You can add notes four ways:

- **Text notes** — type anything.
- **Photos** — snap or upload a picture (e.g. a conference slide, a poster,
  a whiteboard). The app reads the image.
- **Voice memos** — record yourself talking. The app automatically writes
  out what you said ("transcription").
- **Business cards** — take a photo of a card and the app extracts the name,
  title, email, phone, and company.

Notes are organised into **Sessions** — usually one session per conference day.

### 📱 WhatsApp shortcuts

Users can add notes by texting our WhatsApp number, without opening the app:

| Type this           | And it does this              |
| ------------------- | ----------------------------- |
| `@notes [text]`     | Adds a quick note             |
| `summary`           | Sends back today's summary    |
| `todos`             | Lists your action items       |
| `contacts`          | Lists your contacts           |
| A photo or audio    | Treated as a note (no command needed) |

### 🤖 AI-generated reports

After a day of capture, click **Generate Report** and the AI produces:

- **Executive summary** — a few paragraphs about your day.
- **Key takeaways** — 8–12 bullets about important people and moments.
- **Themes** — recurring topics with percentages (e.g. "AI ethics — 35%").
- **Action items** — prioritised to-dos with suggested due dates.
- **Contact highlights** — the most important people you met, with a
  pre-written follow-up email for each.

You can pick the **scope** of the report:

- Just one session (today)
- All your notes ever
- Since the last report you generated
- Since a date you choose

Reports can be downloaded as **Markdown, JSON, or PDF**, or **emailed**.

### 👥 Contacts & follow-ups

- Every person mentioned in a note becomes a **contact**.
- **LinkedIn enrichment** — click a button and the app searches the web for
  that person's LinkedIn profile and adds it.
- Export the contact list as a **CSV** to import into a CRM.
- Action items can be sent to your **Google Calendar** or **Microsoft 365**
  with one click (after connecting your account).

### 🏢 Teams

If your account is on a **Team plan**, several people can work together:

- Invite teammates by email.
- Share sessions so everyone on the team sees the same notes.
- See a unified **team feed** of all activity.
- Look at **team analytics** (who captured how many notes, etc.).
- Hook up **webhooks** to send activity to Zapier, HubSpot, or Zoho.

### 🎟️ Conference presets (admin feature)

This one is mostly for our internal team and event-organiser partners:

- An admin sets up a "conference preset" — name, dates, venue, a logo,
  and a list of invited email addresses.
- Everyone on that list gets an email invite to claim a free seat.
- When they sign in, they see a **branded banner** at the top of their
  dashboard (with the conference logo and a sponsor logo).
- Each person can claim **one** preset, once, forever.

You probably won't create presets yourself, but you may be asked to test
the **claim flow** by clicking an invite link sent to your test email.

### 💳 Plans

Four tiers, all managed by Stripe:

| Plan        | Who it's for                          |
| ----------- | ------------------------------------- |
| Free        | Casual users, light testing           |
| Individual  | A single power user (the "Pro" plan)  |
| Team        | Small groups (3- or 10-seat options)  |
| Enterprise  | Big companies (with SSO, audit logs)  |

---

## 4. Your First Week — Test Checklist

Work through this list on **Dev** (<https://dev.actionnotes.ai>). Tick each
item as you go and **report anything weird** to your team lead — that's your
main job.

### Day 1 — Sign up & basic capture

- [ ] Sign up with email + password at the Dev URL.
- [ ] Complete the email verification step (check your inbox).
- [ ] Land on the dashboard. Does anything look broken? Take a screenshot.
- [ ] Create a new **session** called "Test Conference Day 1".
- [ ] Add a **text note** ("Met Alice from Acme Corp, she's interested in our pricing").
- [ ] Add a **photo** — any photo from your phone.
- [ ] Record a **voice memo** — say a short sentence. Wait ~30 seconds and
      check that the transcription appears under the note.
- [ ] If you have a real or sample business card handy, snap it and check
      that the name, email, and company are extracted correctly.

### Day 2 — AI reports

- [ ] Add 3–5 more text notes, mentioning different people and topics.
- [ ] Click **Generate Report** with scope "This session".
- [ ] Read through the report. Does the summary make sense? Are the action
      items reasonable?
- [ ] Try **emailing the report** to yourself. Check that the PDF attachment
      arrives and is readable.
- [ ] Try **downloading** the report as Markdown.
- [ ] Try generating a report with each of the other three scopes (`All notes`,
      `Since last`, `Since date`). Note any differences.

### Day 3 — Contacts & calendar

- [ ] Open the **Contacts** page. Are all the people you mentioned listed?
- [ ] Click **Enrich with LinkedIn** on a contact. Does a profile URL appear
      (or a sensible fallback)?
- [ ] Export the contact list as **CSV** and open it in a spreadsheet app.
- [ ] Go to the **Action Items** page. Click "Sync to Google Calendar" and
      connect your Google account. Check that the actions appear in your
      Google Calendar.

### Day 4 — Plans & teams

- [ ] Upgrade your account to the **Team plan** using the test card above.
- [ ] Create a team called "Test Team".
- [ ] Invite a second test email (you can use a `+team@…` Gmail alias to
      reuse your inbox).
- [ ] From the second account, accept the invite.
- [ ] Share a session with the team. Check that the second account can see it.
- [ ] Look at the **team feed** and **team analytics** pages.

### Day 5 — Edge cases & polish

- [ ] Try uploading a really large photo (>10MB). What happens?
- [ ] Try recording a long voice memo (>2 minutes). Does it still transcribe?
- [ ] Try generating a report on a session with **zero notes**. Friendly
      error, or scary crash?
- [ ] Try the app on **your phone** in a browser. Does it work? Is anything
      hard to tap?
- [ ] Turn off your wifi mid-capture and add a note offline. Turn wifi
      back on — does the note sync?

---

## 5. How to Report a Bug

When something looks wrong, write it up like this. Even small details help.

```
What I did: clicked "Generate Report" with scope "All notes"
What I expected: a report appears
What actually happened: spinner ran for 60 seconds, then a red error popped up
URL: https://dev.actionnotes.ai/reports/new
Browser: Chrome on Mac
Time: 2026-05-20, around 2:15pm
Screenshot: [attach it]
```

The four magic ingredients are: **steps to reproduce, expected, actual,
screenshot**. With those, an engineer can usually fix it the same day.

If something is **really broken on Prod** (real customers affected),
flag it to your team lead immediately — don't wait until the end of the day.

---

## 6. Things to Remember

1. **Always check the URL.** Dev is `dev.actionnotes.ai`. Prod is
   `www.actionnotes.ai`. Mistaking one for the other is the #1 mistake
   new testers make.
2. **Dev is for breaking things.** Be curious, try weird inputs, click
   buttons in the wrong order. That's the whole point.
3. **Prod is for real customers.** Only touch it when asked, and never
   create junk data there.
4. **No question is too basic.** If you can't figure out how a feature
   works, that's a UX bug worth reporting on its own.
5. **Screenshots > descriptions.** A 3-second screenshot saves 20 minutes
   of back-and-forth.

Welcome to the team — happy testing! 🧪
