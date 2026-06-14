# Phase 3 — Customer Discovery: Target List Summary

---

## Outcome vs Targets

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Qualified Accounts (Companies) | **72** | 60–80 | ✅ MET |
| Qualified Contacts | **83** | 120+ | ⚠️ 37 SHORT |
| Director/Founder/Head | 45 | — | Strong |
| Metro Manila | 52 | — | ✅ |
| Cebu/Visayas | 3 | — | ⚠️ Gap |
| Davao/Mindanao | 1 | — | ⚠️ Gap |
| Accounts with 2+ contacts | 7 | — | Shallow |

---

## 1. Apollo Data Sources (7 unique CSVs converted → .md)

| File | Contacts | Key Contribution |
|------|----------|------------------|
| qualified accounts for event industry.csv | 45 | Original ICP-qualified list |
| apollo-contacts-export.csv | 19 | Early raw export |
| apollo-contacts-export (1).csv | 15 | Additional event contacts |
| apollo-contacts-export (2).csv | 48 | Large raw export |
| apollo-contacts-export (3).csv | 24 | MICE-focused contacts |
| apollo-contacts-export (4).csv | 20 | Hotel Directors (newest) |
| apollo-contacts-export (6).csv | 25 | Managing Directors/Founders |

Duplicates removed: files (5), (7), (8), (9), (10), (11), (12), (13) — all copies.

---

## 2. ICP Qualification — Who's In

All 72 accounts pass ICP filter: they run multi-day or high-attendee events where messaging/check-in/registration matters.

| Segment | Companies | Contacts | Examples |
|---------|-----------|----------|---------|
| **Venue/Hotel** | 19 | 24 | Shangri-La, Marriott, NUSTAR, Crimson, Edsa Shangri-La |
| **PR/Marketing Agency** | 18 | 19 | Golden Pencil, NuWorks, Team One, Stratworks |
| **Event Agency** | 12 | 15 | M&SE, SiGMA World, Fireworks Trade, RUNRIO |
| **Event Tech/Platform** | 5 | 6 | BoomPop, Venuespring, Guestable |
| **Other (Non-Event Core)** | 5 | 6 | Hacking HR, PMAP, IBPAP, EAB |
| **F&B/Hospitality Support** | 3 | 3 | AWC, Little Caesars, Philippine Wine Merchants |
| **Entertainment** | 2 | 2 | Tier One, Entertainment Company |
| **Hospitality Services** | 1 | 1 | Hospitality Innovators |
| **Travel/Tourism** | 1 | 1 | Holland America Line |
| **Venue (Cultural)** | 1 | 1 | Bonifacio Art Foundation |
| **Venue (Religious)** | 1 | 1 | Every Nation |

---

## 3. Enriched Data — Ready for Twenty CRM Import

### Companies CSV (`twenty_crm_companies_import.csv`)
- 72 companies, each with: Name, Website, Industry, **Segment**, City, Region, Country, LinkedIn URL
- **Tagged by segment** — import into CRM, apply tags by segment

### Contacts CSV (`twenty_crm_contacts_import.csv`)
- 83 contacts, each with: Name, Title, Company, Email, Seniority, **Segment**, Industry, LinkedIn, Website, **City**, **Region**, Country
- **Tagged by city + segment + seniority** — linked to parent Company by name
- 80/83 have city filled (96%), 80/83 have region filled (96%)

---

## 4. Personalization Hooks — Top 15 Accounts

File: `outreach-sequence-top15.md`

Each of the top 15 accounts has a personalized email 1 referencing their specific property:
- **New World Makati**: "Your team handles 200+ events/year..."
- **Edsa Shangri-La**: "Shangri-La Group already uses Twenty..."
- **NUSTAR Resort**: "Premier integrated resort in Visayas..."
- **Crimson Hotel**: "Filinvest City MICE market..."
- **Kingsford Hotel**: "Proximity to NAIA..."
- **(10 more in the file)**

All 15 contacts are Director-level decision-makers at Venue/Hotel segment.

---

## 5. Salesforce/Twenty CRM Import Order

1. **Import Companies** (`twenty_crm_companies_import.csv`) — create 72 Company records
2. **Apply company tags** by Segment (Venue/Hotel, Event Agency, PR/Marketing Agency, etc.)
3. **Import Contacts** (`twenty_crm_contacts_import.csv`) — create 83 Contact records linked by Company Name
4. **Apply contact tags** by Segment, City, Seniority

---

## 6. Gaps — What's Missing (37 contacts)

### Major Venues — Not in dataset (run Apollo search)

| Missing Target | Suggested Title | Est. Contacts |
|----------------|----------------|---------------|
| SMX Convention Center | Events Director / Sales Director | 2–3 |
| PICC (Philippine Intl Convention Center) | Events Director / Marketing Director | 2–3 |
| World Trade Center Manila | General Manager / Events Director | 2–3 |
| Hilton Manila | Director of Sales & Marketing | 1–2 |
| Dusit Thani Manila | Director of Sales & Marketing | 1–2 |
| Solaire Resort | Events Director / Marketing Director | 2–3 |

### DMCs — None in dataset (run Apollo search)

| Missing DMC | Suggested Title | Est. Contacts |
|-------------|----------------|---------------|
| Destination Managers Inc. | Managing Director / Operations Director | 1–2 |
| AsiaPlan | Managing Director / Operations Director | 1–2 |
| Trailblazer DMC | Managing Director / Operations Director | 1–2 |
| Pacific World | Managing Director / Operations Director | 1–2 |
| Tempo DMC | Managing Director / Operations Director | 1–2 |

### Geographic Expansion

| Missing Hotel | City | Est. Contacts |
|--------------|------|---------------|
| Marco Polo Cebu | Cebu City | 1–2 |
| Waterfront Cebu | Cebu City | 1–2 |
| Radisson Blu Cebu | Cebu City | 1–2 |
| Seda Cebu | Cebu City | 1–2 |
| Seda Davao | Davao City | 1–2 |
| Marco Polo Davao | Davao City | 1–2 |

### Account Depth — 65/72 companies have only 1 contact
Pull one more contact per top 30 companies (even an Event Coordinator or Sales Manager).

---

## Files Delivered

| File | Description |
|------|-------------|
| `twenty_crm_companies_import.csv` | 72 companies with Segment tags → CRM import |
| `twenty_crm_contacts_import.csv` | 83 contacts with Segment/City/Region tags → CRM import |
| `phase3-consolidated-target-list.md` | Full report: all contacts, ICP assessment, gaps |
| `phase3-summary.md` | This document |
| `outreach-sequence-top15.md` | 5-touch email sequence with personalized hooks |
| All 7 `.md` source files | Converted Apollo exports |
