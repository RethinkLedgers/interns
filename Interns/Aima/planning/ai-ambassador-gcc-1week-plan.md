# AI Ambassador (msg2ai Events) — Intern GTM Plan

> Example planning doc. The **AI Ambassador** is msg2ai's **Events assistant**: a WhatsApp/SMS AI concierge for event organizers that handles attendee onboarding, agenda, meeting requests, and QR check-in. See [`products/ai_ambassador/ai_ambassador_product_guideline.md`](../../../products/ai_ambassador/ai_ambassador_product_guideline.md).

**Region:** Qatar · Oman · Dubai · Abu Dhabi · KSA (GCC)
**Vertical focus:** **Hotels Concierge** — hotels, resorts, and boutique hospitality brands deploying an AI guest concierge for front-desk Q&A, check-in, and in-stay service.
**Goal:** Customer Discovery → Market Analysis → Customer Outreach (email + organized campaigns)
**Objectives:** drive **initial calls**, **signups**, and **sales growth** with GCC hotels & resorts

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

> Ground rules: work from the **msg2ai email**, keep all testing on **Test**, never put API keys or contact lists in a tracked Git file, and never email at scale from Prod.

---

## Phase 1 — Product immersion + define the ICP

*Outcome: you can explain the AI Ambassador in 2 sentences and know exactly who to sell to.*

- Run Exercises 1–5 from the product guideline on **Test** (send a DM, build a Concierge assistant, import an audience, run a 5-min-delayed broadcast, read Message Logs).
- Focus on the **Concierge** assistant type + **guest Q&A** + **Check-in** + **Surveys** — these are the hotel-concierge story.
- Draft the **Ideal Customer Profile (ICP):** 4–5★ hotels & resorts, boutique & lifestyle hotel brands, serviced apartments, and regional hotel groups across Dubai, Abu Dhabi, Doha, Muscat, Riyadh & Jeddah; decision-makers in Guest Experience, Front Office, Rooms Division, and Marketing.
- Write a one-paragraph **value proposition** tailored to GCC hotels (WhatsApp-first concierge, Arabic + English, 24/7 guest Q&A, automated check-in & upsells, post-stay surveys — fewer front-desk calls, higher guest satisfaction).

## Phase 2 — Market analysis (GCC hotel landscape)

*Outcome: a short market brief that informs targeting and the pitch.*

- Map the **hotel market** per country: key clusters and hotel density in Dubai, Abu Dhabi, Doha, Muscat, Riyadh & Jeddah, including the major regional groups and fast-growing KSA tourism developments (NEOM, Red Sea, Diriyah).
- Identify the **top 15–20 hotel groups & independent properties** per priority market (lead with UAE + KSA — largest room inventory).
- Note the buying context: WhatsApp dominance for guest comms, Arabic + English need, high seasonal occupancy swings, and Vision-2030 / tourism-target-driven hotel growth in KSA.
- Deliverable: **1–2 page market brief** in the Obsidian wiki (segments, top accounts, key hooks, objections).

## Phase 3 — Customer discovery (build the target list)

*Outcome: 60–80 qualified accounts and 120+ contacts in the CRM.*

- Use **Apollo** to pull hotels, resorts & hotel groups in the 5 markets; filter by title (Guest Experience, Front Office/Rooms Division, GM, Marketing Director).
- Qualify each account against the ICP (star rating, room count, brand vs. independent, how they currently handle guest messaging).
- Enrich and import into **Twenty CRM** — one Company record per property/group, Contacts linked, tagged by country + segment + room-count band.
- For the **top 15 accounts**, find a specific hook (new property, renovation, award, occupancy push) to reference in outreach.

## Phase 4 — Outreach prep (sequences, templates, CRM hygiene)

*Outcome: a ready-to-send campaign, fully personalized at the top of funnel.*

- Write a **3-touch email sequence** (initial → value/case follow-up → break-up), each ≤120 words, with one clear CTA: *book a 15-min call / see a live demo*.
- Build **2–3 segment variants** (large hotel groups vs. independent/boutique hotels vs. resorts/serviced apartments) and an Arabic subject-line option.
- Prepare a **demo asset**: a short Loom/screenshare of the Events assistant from Test, or a live test number they can text.
- Set up CRM stages (Prospect → Contacted → Replied → Call Booked → Signup) and a recurring follow-up view. Confirm deliverability basics (send from the msg2ai email, small batches, no spammy links).

## Phase 5 — Launch campaigns, book calls, report

*Outcome: campaign live, calls on the calendar, week wrapped up.*

- Send **Touch 1** to the full qualified list in **small batches** (e.g. 20–30 personalized), prioritizing the top-15 hooks.
- Work replies in real time → **book initial calls/demos**; log every reply and outcome in Twenty.
- Offer warm leads a **free Test signup** so they can try the AI Ambassador.
- Write the **end-of-week progress report** in [`../progress-reports/`](../progress-reports/): emails sent, open/reply rates, calls booked, signups, what resonated, objections heard, and next-week plan (Touch 2/3, expand list, add WhatsApp outreach where appropriate).

---

## msg2ai-leads skills — your build-and-outreach toolkit

The **`msg2ai-leads`** repo packages five Claude Code skills that take a website all the way to outreach. Full guide: **[SKILLS-OVERVIEW.md](https://github.com/RethinkLedgers/msg2ai-leads/blob/main/SKILLS-OVERVIEW.md)**.

**Pipeline:** ① build a JSON config from a URL (`/event-assistant-creation`, `/concierge-assistant-creation`) → ② set it live on msg2ai-server (`import-event-assistant.js` / `import-concierge-assistant.js`) → ③ make a promo video (`/website-to-video`, `/event-promo-video`, `/str-property-to-video`) → ④–⑤ **outreach**.

### Outreach skills (lean on these for Phase 4–5)

The outreach skills read straight from a built event/property package (its JSON + import receipt + short URLs), so steps ①–③ feed your campaigns automatically. **Prefer these over writing outreach from scratch** — they keep messaging on-brand and pull real details from the assistant you built:

- **`/draft-organizer-email`** — the first "your assistant is ready, here are test questions" note after onboarding (plain professional draft + QR onboarding).
- **`/ai-ambassador-email-pitch`** — a polished, mobile-responsive **HTML** pitch once you have a promo video (value first, video last).
- **`/event-outreach-followup`** — a short nudge when the first email gets no reply, or to announce a new video (`nudge` / `video-launch` / `two-tools` variants).
- **`/drip-campaign-outreach`** — a full multi-touch sequence with US / EMEA wording variants, pushed to li-extract for scheduling. Event cadence (vacation-rental campaigns run a shorter 4-touch, email-only):

  | Touch | Timing | Purpose |
  | --- | --- | --- |
  | 1 | Day 0 | "Your assistant is ready" — try it with test questions |
  | 2 | +7 days | Re-engage from a new angle (a speaker, a specific session) |
  | 3 | +14 days | Video — AI Ambassador + ActionNotes, clickable poster, 2 CTAs |
  | 4 | +21 days | Partnership offer — free setup, "sponsored by" framing |
  | 5 | event end +5 days | Post-event recap + next-event opportunity |

> These power the **Outreach prep** and **Launch** phases above — build the assistant and video first, then let the outreach skills turn that package into emails and a drip sequence.

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
