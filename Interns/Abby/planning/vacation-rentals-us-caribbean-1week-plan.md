# AI Ambassador (msg2ai Events) — Intern GTM Plan

> Example planning doc. The **AI Ambassador** is msg2ai's **Events assistant**: a WhatsApp/SMS AI concierge for event organizers that handles attendee onboarding, agenda, meeting requests, and QR check-in. See `[products/ai_ambassador/ai_ambassador_product_guideline.md](../../../products/ai_ambassador/ai_ambassador_product_guideline.md)`.

**Region:** United States · Caribbean
**Vertical focus:** **Vacation Rentals** — short-term rental (STR) hosts, property managers, and vacation-rental management companies (Airbnb/VRBO-style, beach & resort destinations).
**Goal:** Customer Discovery → Market Analysis → Customer Outreach (email + organized campaigns)
**Objectives:** drive **initial calls**, **signups**, and **sales growth** with US & Caribbean vacation-rental operators

## Weekly targets (KPIs to hit by end of week)


| Metric                                  | Target                            |
| --------------------------------------- | --------------------------------- |
| Target accounts researched & qualified  | **60–80** event organizers/venues |
| Decision-maker contacts enriched in CRM | **120+**                          |
| Outreach emails sent (sequenced)        | **100+**                          |
| Replies / positive responses            | **8–12**                          |
| **Initial calls / demos booked**        | **3–5**                           |
| Free signups on Test/demo               | **2–3**                           |


> Targets are starter estimates — adjust with your manager after the first phase.

## Tools you'll use

- **msg2ai Test env** (`test.msg2ai.xyz`) — learn the Events assistant so you can pitch it credibly. **Test only — never Prod.**
- **Apollo.io** — find event organizers, venues, DMCs/PCOs and enrich decision-maker emails.
- **Twenty CRM** (`rethink-labs.twenty.com`) — log every account, contact, and call.
- **Zoho** — send sequenced outreach in small, personalized batches.
- **Happenstance.ai** — tap the team network for warm intros and to find who can connect you into target accounts.
- **Obsidian wiki** — write up market-analysis notes.

> Ground rules: work from the **msg2ai email**, keep all testing on **Test**, never put API keys or contact lists in a tracked Git file, and never email at scale from Prod.

---

## Phase 1 — Product immersion + define the ICP

*Outcome: you can explain the AI Ambassador in 2 sentences and know exactly who to sell to.*

- Run Exercises 1–5 from the product guideline on **Test** (send a DM, build a Concierge assistant, import an audience, run a 5-min-delayed broadcast, read Message Logs).
- Draft the **Ideal Customer Profile (ICP):** STR property managers and vacation-rental management companies (managing ~25–500+ units), boutique resort & villa operators, and hosts in top US leisure markets (Florida, Gulf Coast, Smokies/Gatlinburg, Outer Banks, Hawaii, Arizona) and the Caribbean (Puerto Rico, Dominican Republic, Bahamas, Jamaica, Turks & Caicos, USVI).
- Write a one-paragraph **value proposition** tailored to vacation rentals (SMS/WhatsApp guest concierge, English + Spanish, automated check-in/checkout instructions, 24/7 answers to "where's the WiFi / how do I get in", upsells, and review prompts — fewer manual messages per booking).

## Phase 2 — Market analysis (US & Caribbean vacation-rental landscape)

*Outcome: a short market brief that informs targeting and the pitch.*

- Map the **top leisure markets** and their peak seasons: US (Florida & Gulf Coast, Smokies, Outer Banks, Hawaii, Arizona, mountain/ski towns) and the Caribbean (Puerto Rico, DR, Bahamas, Jamaica, Turks & Caicos, USVI).
- Identify the **top 15–20 property managers / vacation-rental management companies** per priority market, plus the PMS ecosystems they run on (**Guesty, Hostaway, Hospitable, Lodgify**) — integration fit is a strong qualifier.
- Note the buying context: SMS-first guest comms in the US (WhatsApp common for international/Caribbean guests), English + Spanish need, high message volume per booking (pre-arrival, check-in, in-stay, review), and seasonal demand spikes.
- Deliverable: **1–2 page market brief** in the Obsidian wiki (segments, top accounts, key hooks, objections).

## Phase 3 — Customer discovery (build the target list)

*Outcome: 60–80 qualified accounts and 120+ contacts in the CRM.*

- Use **Apollo** to pull vacation-rental management companies / STR property managers in the target markets; filter by title (Owner/Founder, Operations, Guest Experience, Revenue/Marketing).
- Qualify each account against the ICP (unit count, which PMS they use, how many guest messages they handle manually).
- Enrich and import into **Twenty CRM** — one Company record per operator, Contacts linked, tagged by market + PMS + unit-count band.
- For the **top 15 accounts**, find a specific hook (number of listings, a destination, a recent expansion) to reference in outreach.
- search for specific Property Managers on Happenstance

## Phase 4 — Outreach prep (sequences, templates, CRM hygiene)

*Outcome: a ready-to-send campaign, fully personalized at the top of funnel.*

- Write a **3-touch email sequence** (initial → value/case follow-up → break-up), each ≤120 words, with one clear CTA: *book a 15-min call / see a live demo*.
- Build **2–3 segment variants** (large PM companies vs. boutique/villa operators vs. by-PMS, e.g. Guesty vs. Hostaway) and a Spanish subject-line option for Caribbean accounts.
- Prepare a **demo asset**: a short Loom/screenshare of the Events assistant from Test, or a live test number they can text.
- Set up CRM stages (Prospect → Contacted → Replied → Call Booked → Signup) and a recurring follow-up view. Confirm deliverability basics (send from the msg2ai email, small batches, no spammy links).

## Phase 5 — Launch campaigns, book calls, report

*Outcome: campaign live, calls on the calendar, week wrapped up.*

- Send **Touch 1** to the full qualified list in **small batches** (e.g. 20–30 personalized), prioritizing the top-15 hooks.
- Work replies in real time → **book initial calls/demos**; log every reply and outcome in Twenty.
- Offer warm leads a **free Test signup** so they can try the AI Ambassador.
- Write the **end-of-week progress report** in `[../progress-reports/](../progress-reports/)`: emails sent, open/reply rates, calls booked, signups, what resonated, objections heard, and next-week plan (Touch 2/3, expand list, add WhatsApp outreach where appropriate).

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

- Briefs, cleaned lists, email drafts, demo links, and other artifacts → `[../workproducts/](../workproducts/)`
- Your end-of-week write-up → `[../progress-reports/](../progress-reports/)`
- Keep this plan current as things change → this `planning/` folder

Work on a branch and open a **PR against `main`** (don't push straight to `main`). Never commit secrets, API keys, or raw contact lists.

## Definition of done (end of week)

- [ ] 60–80 qualified accounts + 120+ contacts in Twenty CRM
- [ ] Market brief published to the Obsidian wiki
- [ ] 3-touch email sequence + segment variants written and reviewed
- [ ] Touch 1 sent to the full list
- [ ] 3–5 initial calls/demos booked
- [ ] End-of-week progress report submitted