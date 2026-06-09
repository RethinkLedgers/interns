# AI Ambassador (msg2ai Events) — Intern GTM Plan

> Example planning doc. The **AI Ambassador** is msg2ai's **Events assistant**: a WhatsApp/SMS AI concierge for event organizers that handles attendee onboarding, agenda, meeting requests, and QR check-in. See [`products/ai_ambassador/ai_ambassador_product_guideline.md`](../../../products/ai_ambassador/ai_ambassador_product_guideline.md).

**Region:** Qatar · Oman · Dubai · Abu Dhabi · KSA (GCC)
**Goal:** Customer Discovery → Market Analysis → Customer Outreach (email + organized campaigns)
**Objectives:** drive **initial calls**, **signups**, and **sales growth**

## Weekly targets (KPIs to hit by end of week)

| Metric | Target |
| --- | --- |
| Target accounts researched & qualified | **60–80** event organizers/venues |
| Decision-maker contacts enriched in CRM | **120+** |
| Outreach emails sent (sequenced) | **100+** |
| Replies / positive responses | **8–12** |
| **Initial calls / demos booked** | **3–5** |
| Free signups on Test/demo | **2–3** |

> Targets are starter estimates — adjust with your manager after the first phase.

## Tools you'll use

- **msg2ai Test env** (`test.msg2ai.xyz`) — learn the Events assistant so you can pitch it credibly. **Test only — never Prod.**
- **Apollo.io** — find event organizers, venues, DMCs/PCOs and enrich decision-maker emails.
- **Twenty CRM** (`rethink-labs.twenty.com`) — log every account, contact, and call.
- **Zoho** — send sequenced outreach in small, personalized batches.
- **Happenstance.ai** — tap the team network for warm intros and to find who can connect you into target accounts.
- **Obsidian wiki** — write up market-analysis notes.
- **

> Ground rules: work from the **msg2ai email**, keep all testing on **Test**, never put API keys or contact lists in a tracked Git file, and never email at scale from Prod.

---

## Phase 1 — Product immersion + define the ICP

*Outcome: you can explain the AI Ambassador in 2 sentences and know exactly who to sell to.*

- Run Exercises 1–5 from the product guideline on **Test** (send a DM, build a Concierge assistant, import an audience, run a 5-min-delayed broadcast, read Message Logs).
- Focus on the **Events** assistant type + **Check-in** + **Meeting Requests** — these are the AI Ambassador story.
- Draft the **Ideal Customer Profile (ICP):** exhibition organizers, PCOs/conference organizers, DMCs, large venues (Dubai World Trade Centre, ADNEC, DECC Doha, Oman Convention & Exhibition Centre, RICEC Riyadh, Jeddah Superdome), expo/government-event teams, large wedding/MICE planners.
- Write a one-paragraph **value proposition** tailored to GCC (WhatsApp-first, Arabic + English, automated attendee onboarding & check-in, sponsor/speaker meeting booking).

## Phase 2 — Market analysis (GCC events landscape)

*Outcome: a short market brief that informs targeting and the pitch.*

- Map the events calendar per country: major expos, conferences, government summits, and the season's big events in Qatar, Oman, Dubai, Abu Dhabi, KSA.
- Identify the **top 8–12 venues** and **top 15–20 organizers/PCOs/DMCs** per priority market (lead with UAE + KSA — largest volume).
- Note the buying context: WhatsApp dominance in the region, Arabic-language need, peak event seasons (Oct–Apr), and Vision-2030/Expo-driven event growth in KSA.
- Deliverable: **1–2 page market brief** in the Obsidian wiki (segments, top accounts, key hooks, objections).

## Phase 3 — Customer discovery (build the target list)

*Outcome: 60–80 qualified accounts and 120+ contacts in the CRM.*

- Use **Apollo** to pull event organizers / venues / DMCs in the 5 markets; filter by title (Marketing Director, Events Director, Operations, Founder/MD).
- Qualify each account against the ICP (do they run multi-day or high-attendee events where messaging/check-in matters?).
- Enrich and import into **Twenty CRM** — one Company record per org, Contacts linked, tagged by country + segment.
- For the **top 15 accounts**, find a specific recent or upcoming event to reference in outreach (personalization hook).

## Phase 4 — Outreach prep (sequences, templates, CRM hygiene)

*Outcome: a ready-to-send campaign, fully personalized at the top of funnel.*

- Write a **3-touch email sequence** (initial → value/case follow-up → break-up), each ≤120 words, with one clear CTA: *book a 15-min call / see a live demo*.
- Build **2–3 segment variants** (venues vs. organizers vs. DMCs) and an Arabic subject-line option.
- Prepare a **demo asset**: a short Loom/screenshare of the Events assistant from Test, or a live test number they can text.
- Set up CRM stages (Prospect → Contacted → Replied → Call Booked → Signup) and a recurring follow-up view. Confirm deliverability basics (send from the msg2ai email, small batches, no spammy links).

## Phase 5 — Launch campaigns, book calls, report

*Outcome: campaign live, calls on the calendar, week wrapped up.*

- Send **Touch 1** to the full qualified list in **small batches** (e.g. 20–30 personalized), prioritizing the top-15 hooks.
- Work replies in real time → **book initial calls/demos**; log every reply and outcome in Twenty.
- Offer warm leads a **free Test signup** so they can try the AI Ambassador.
- Write the **end-of-week progress report** in [`../progress-reports/`](../progress-reports/): emails sent, open/reply rates, calls booked, signups, what resonated, objections heard, and next-week plan (Touch 2/3, expand list, add WhatsApp outreach where appropriate).

---

## Using OpenCode (and your other tools) to work faster

Most tasks above go faster with an AI agent. **OpenCode** is the team's terminal AI agent (use **Cursor** if you prefer a GUI) — point it at the work and let it draft, clean, and summarize while you steer:

- **Research & market analysis** — summarize the local landscape, structure segments/top accounts, and draft the market brief from your raw notes.
- **Customer discovery** — clean, dedupe, and reformat Apollo exports into import-ready lists for Twenty.
- **Outreach prep** — draft and tighten the 3-touch sequence and segment variants (keep each ≤120 words), and spin up subject-line options.
- **CRM hygiene & reporting** — turn your activity into the progress report, compute open/reply rates, and draft the write-up.

Other tools in the stack help too: **Tailscale** for secure access to internal/self-hosted services, **Composio** to connect apps (auth) to your agent, **Paperclip** to run agents like teammates, and the **Obsidian** wiki for notes. Always review AI output before it goes out, and **never paste API keys or contact lists into a tracked Git file or into an AI prompt that logs them.**

## Post your outcomes back to GitHub

**Everything you produce goes back to GitHub, in your own personal folder** — so your manager can see progress and the team can build on it:

- Briefs, cleaned lists, email drafts, demo links, and other artifacts → [`../workproducts/`](../workproducts/)
- Your end-of-week write-up → [`../progress-reports/`](../progress-reports/)
- Keep this plan current as things change → this `planning/` folder

Work on a branch and open a **PR against `main`** (don't push straight to `main`). Never commit secrets, API keys, or raw contact lists.

## Definition of done (end of week)

- [ ] 60–80 qualified accounts + 120+ contacts in Twenty CRM
- [ ] Market brief published to the Obsidian wiki
- [ ] 3-touch email sequence + segment variants written and reviewed
- [ ] Touch 1 sent to the full list
- [ ] 3–5 initial calls/demos booked
- [ ] End-of-week progress report submitted
