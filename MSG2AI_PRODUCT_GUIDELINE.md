# msg2ai — Product Onboarding Guideline

Welcome to the team! This guide walks you through what msg2ai is, where to find it, and how to start exploring the product as a new intern or student user. No coding required.

---

## 1. What is msg2ai?

msg2ai is an **AI-powered guest messaging platform** for hotels, short-term rentals, conferences, and events. It lets businesses talk to their guests automatically across multiple channels — SMS, WhatsApp, RCS, and Telegram — using AI assistants that answer questions, take bookings, run surveys, and send broadcasts.

In one sentence: **msg2ai replaces "someone manually answering guest messages" with an AI assistant that knows the property, the event, and the guest.**

### Who uses it

- **Hotels & resorts** — front desk Q&A, check-in flows, surveys
- **Short-term rental hosts** (Airbnb-style) — automated guest comms via Guesty / Hostaway / Hospitable integrations
- **Event organizers** — attendee onboarding, agenda, meeting requests, check-in
- **Boutique hospitality brands** — branded multilingual concierge

---

## 2. The Three Environments

msg2ai runs in three separate environments. **Always know which one you're in** before clicking anything that sends a real message.

| Environment | URL                                            | What it's for                                                                                     |
| ----------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Dev**     | [dev.ai-ambassador.xyz](https://dev.ai-ambassador.xyz) | Internal development. Features land here first. Things may be broken — that's expected.           |
| **Test**    | [test.msg2ai.xyz](https://test.msg2ai.xyz)             | Stable test playground. Use this for QA, demos to teammates, and learning the product safely.     |
| **Prod**    | [app.msg2ai.com](https://app.msg2ai.com)               | Real customers. Real money. Real messages going to real phones. **Do not test things here.**      |

### Golden rules

1. **Default to Test** for all your exploration and learning.
2. **Never send broadcasts from Prod** unless a manager explicitly tells you to.
3. **Check the URL in the browser bar** every time you do something destructive (delete, send, archive).
4. If you're unsure which env you're in — stop and ask.

---

## 3. Getting Access

You'll get an invite to the relevant Clerk organization by email. To log in:

1. Open the environment URL from the table above.
2. Click **Sign in**.
3. Use the email your manager invited (Google login is the easiest).
4. You'll land on the **Dashboard**.

**Roles you might be assigned:**

| Role           | What you can do                                                                |
| -------------- | ------------------------------------------------------------------------------ |
| **Member**     | Use the dashboard, view messages, run reports                                  |
| **Admin**      | Everything above + manage WhatsApp templates, settings, audiences              |
| **SuperAdmin** | Internal-only. System-wide access across all customer organizations.           |

As an intern, you'll usually start as a **Member** on Test, and may be given **Admin** later.

---

## 4. The Main Features — What to Click On

Here's a tour of what's in the app and what each section does.

### Dashboard
The home screen. Shows message volume (last hour / day / week), recent activity, and the phone numbers connected to your assistants. **Start here every session** to get a feel for what's happening.

### Assistants
The AI agents that talk to guests. Each assistant has:
- A **type** — Concierge, Events, or BYO LLM
- A **language** and **persona**
- **Knowledge** (uploaded files like menus, FAQs, schedules)
- A **phone number** that guests can text

You create one with the multi-step wizard ("Create Assistant"). The wizard also supports **JSON import** if you have a pre-built configuration.

### Direct Messages
Send a one-off SMS or WhatsApp to a single contact. Live character count and SMS-segment indicator show what the recipient will see.

### Broadcasts / Campaigns
Send a message to a whole **audience group** (e.g. "all hotel guests checking in this week"). Supports scheduling, archived/active filtering, and per-row resends.

### Audiences
Lists of contacts. You can import via **CSV, JSON, or XLSX**, and optionally enrich with LinkedIn data.

### Message Logs
Every conversation, in a chat-style 2-column view (Guest vs Assistant). Filter by date, phone number, sentiment, and "no answer found" tags. **Great place to spot issues** — look for negative sentiment or unanswered questions.

### Surveys
Build short surveys (multiple choice, rating, free text), distribute them through an assistant, and view analytics.

### Check-in
QR-code-based event check-in. Attendees scan, confirm preferences, and get verified.

### Meeting Requests
Token-secured calendar links sent over WhatsApp. Used for events where attendees book meetings with speakers/sponsors.

### Content Templates (WhatsApp)
WhatsApp requires every outbound template to be pre-approved by Meta. This section is where templates are created, registered, and tracked.

### Benchmarks (SuperAdmin)
Compare different AI models side-by-side on the same set of questions.

---

## 5. How to Test the Product (Intern Playbook)

Follow these exercises on **Test** ([test.msg2ai.xyz](https://test.msg2ai.xyz)) to learn the product end-to-end. None of them touch real customers.

### Exercise 1 — Send yourself a Direct Message
1. Go to **Direct Messages**.
2. Pick an assistant (any one your org has set up).
3. Enter **your own phone number** in international format (e.g. `+15551234567`).
4. Type a short message and send.
5. Check your phone — the SMS should arrive within seconds.
6. Reply from your phone. Watch the conversation appear in **Message Logs**.

> ✅ You've now seen the full loop: outbound → delivery → inbound → AI reply.

### Exercise 2 — Create a simple Concierge assistant
1. Go to **Assistants → Create Assistant**.
2. Choose **Concierge**.
3. Give it a name, pick English, and set a friendly persona.
4. Upload one PDF (e.g. a sample menu or FAQ).
5. Skip QR onboarding for now (toggle off).
6. Finish the wizard.
7. Note the phone number it gets assigned.
8. Text that number a question whose answer is in the PDF. Check the reply.

### Exercise 3 — Import an audience
1. Go to **Audiences → Import**.
2. Download the sample CSV template.
3. Add **2–3 of your own test contacts** (your phone, a colleague who consented).
4. Upload it and verify the contacts appear.

### Exercise 4 — Run a small broadcast
1. Go to **Campaigns / Broadcasts**.
2. Create a new campaign targeting the audience from Exercise 3.
3. Pick (or create) a short message template.
4. **Schedule it 5 minutes in the future** (so you can cancel if something looks wrong).
5. Wait — check your phone — confirm receipt.

### Exercise 5 — Read the Message Logs
1. Go to **Message Logs**.
2. Filter to today.
3. Find the conversations from your earlier exercises.
4. Look for any "No Answer Found" or negative-sentiment tags. Try to understand **why** the assistant struggled.

> This last exercise is the most useful skill: **the logs tell you whether the product is actually working for users.**

---

## 6. What to Do When Something Looks Wrong

1. **Check the URL** — are you on Dev, Test, or Prod? Bugs on Dev are normal.
2. **Reproduce it** — can you make it happen again? Write down the exact steps.
3. **Screenshot it** — full browser window, including the URL bar.
4. **Check Message Logs** — was the message actually sent? What did the assistant reply?
5. **Ask in the team Slack channel** — paste the steps + screenshot + which env.

**Never** try to "fix" data on Prod (delete a customer, archive a campaign, edit a template) unless instructed.

---

## 7. Quick Reference

| Need to…                      | Go to…                                  |
| ----------------------------- | --------------------------------------- |
| Learn the product safely      | [test.msg2ai.xyz](https://test.msg2ai.xyz)         |
| See newest features (may break) | [dev.ai-ambassador.xyz](https://dev.ai-ambassador.xyz) |
| **Never click around casually** | [app.msg2ai.com](https://app.msg2ai.com) (Prod)  |
| See message volume            | Dashboard                               |
| Read conversations            | Message Logs                            |
| Send a one-off message        | Direct Messages                         |
| Send to many people           | Campaigns / Broadcasts                  |
| Manage contacts               | Audiences                               |
| Build an AI agent             | Assistants → Create Assistant           |

---

## 8. Glossary

- **Assistant** — an AI agent that handles conversations on a specific phone number
- **Audience** — a list of contacts you can target with broadcasts
- **Broadcast / Campaign** — one message sent to many recipients
- **Concierge** — assistant type for hotels & rentals (always-on guest Q&A)
- **Events assistant** — assistant type for conferences (agenda, speakers, meetings)
- **BYO LLM** — "Bring Your Own LLM" — advanced assistant where you plug in your own AI provider
- **Template (WhatsApp)** — a pre-approved message format required by Meta for outbound WhatsApp
- **Audience Group** — a labeled segment within an audience
- **Check-in** — QR-code attendee verification flow for events

---

Welcome aboard. Start on **Test**, break things on purpose, and ask questions early.
