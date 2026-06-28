# Course Build Plan — Bit, the Contoso Helpdesk Agent (New Experience)

> Internal planning doc (not published to the site). The master plan for converting the
> Agent Academy Recruit course from **classic** Copilot Studio to the **new experience**,
> told through **Bit** — re-skinned from Nick's Rex/Reza labs onto the Contoso storyline.

## Protagonist

**Bit — your Contoso IT help desk buddy.** Bit *is* the Contoso Helpdesk Agent; "Bit" is the
character/name, "Contoso Helpdesk Agent" is the role. Wherever Nick's drafts say "Rex," we say "Bit."
No Reza video links.

## Naming spine (keep consistent across all modules)

- **Agent:** Bit
- **Solution:** Contoso Helpdesk Agent
- **Skills:** `password-reset`, `vpn-troubleshooting`, `smart-triage`, `software-installation-request`
  (lowercase, hyphens — never underscores)
- **Workflow:** `manager_approval_for_software` (underscores are valid for workflows — call this out)
- **SharePoint list:** Tickets (on the **IT Help Desk** site)
- **Knowledge:** Contoso IT FAQ, Contoso Approved Software List

## Storyline arc (14 modules, 00–13)

Act III (06–11) is Nick's/Reza's capability spine, order preserved so dependencies resolve.

| # | Module | What Bit gains | Source | Builds on |
|---|--------|----------------|--------|-----------|
| 00 | Course Setup | world prep: new experience, Tickets list, 2 docs, solution | Nick+classic | — |
| 01 | Introduction to Agents | concept | classic | — |
| 02 | New Copilot Studio Fundamentals | concept (Build page) | classic+Nick | — |
| 03 | Declarative Agent for M365 | a throwaway lightweight agent (not Bit) — **side quest** | classic | concept |
| 04 | Creating a Solution | the container Bit lives in | classic | — |
| 05 | Using Pre-Built Agents | explore templates — **side quest** | classic | concept |
| 06 | Build Bit + Knowledge & Memory | identity, guardrails; learns 2 docs; remembers | Nick 01+02 | 00, 02 |
| 07 | Skills + Tools & Tickets | 4 skills + Outlook/SharePoint tools; logs a ticket + PDF | Nick 03+04 | 06 |
| 08 | Adaptive Cards | richer responses (card content TBD during build) | gap-fill | 07's ticket |
| 09 | Workflows (approvals) | manager-approval for software (100s pattern) | Nick 05 | 07's software skill |
| 10 | Event Triggers | auto-escalate High/Critical tickets — proactive Bit | gap-fill | 07's Tickets list |
| 11 | Evaluate + Publish/Share/Monitor | prove + ship Bit | Nick 06+07 | all |
| 12 | Understanding Licensing | what Bit costs | classic | — |
| 13 | Securing Your Recruit Badge | graduation + recap | classic | all |

Merges holding it at 14: Memory→06, Tools→07, Evaluate→11.

## Coherence rules (the "does it add up" guarantees)

1. **One ticket store, end to end.** Bit logs to the **SharePoint Tickets list** (07); the escalation
   trigger (10) watches *that same list* — no separate Dataverse table. One source of truth.
2. **08 builds on 07.** The Adaptive Card shows the ticket Bit just logged (exact card content decided
   during the build — keep the module flexible).
3. **03 & 05 are concept side-quests** (kept as full modules) — they don't touch Bit; frame them as
   "alternatives before we build Bit from scratch" so the spine stays clear.

## Two delivery modes (online vs workshop day)

The course serves two audiences and must work for both:

- **Online course material** = complete & **self-contained**. All 14 modules (00–13), numerical
  order in the sidebar. Someone revisiting at the office (no pre-provisioned env) starts at Module 00,
  does setup/security themselves, and the whole thing flows. **Nothing is removed online.**
- **Facilitated workshop day** = a re-sequenced subset (the ColorCloud "Mission Briefing"). Module 00
  (SharePoint + security) is **pre-provisioned**; 01–02 (intro/fundamentals) are **presentation, not
  labs**. Labs start at **05 ("Your First Agent")** and follow the Mission order:
  - **Mission #1 Your first agent:** 05
  - **Mission #2 Build:** 03 → 04 → 06
  - **Mission #3 Enhance:** 07 → 08 → 09
  - **Mission #4 Deploy:** 10 → 11 → Free Play Challenge
  - **Mission Complete:** 12 → 13 → Plan Your First Agent → Keep building

**Implications for module authoring:**
- Every module needs an **explicit, self-contained Prerequisites block** + a note: *"Workshop
  environments come with Module 00 pre-provisioned; if you're following along at the office, complete
  Module 00 first."* So the day can skip/re-sequence and the office revisit still flows.
- Sidebar stays **flat numerical 00–13**. The Mission grouping lives only in `docs/workshop-agenda.md`.
- Titles: **keep my descriptive titles** (05 = Using Pre-Built Agents, 06 = Build the Contoso Helpdesk
  Agent (Bit), 07 = Skills + Tools, 09 = Workflows, 11 = Evaluate + Publish).
- Branding nuance to reconcile later: README says EPPC 2026; the agenda slide is ColorCloud 2026.

## Conversion recipe (per module)

Keep classic scaffolding → swap classic concepts (Topics→Skills, Agent Flows→Workflows, Overview
page→Build page) → re-skin every example to Bit's helpdesk scenario (no device requests) → author
diagrams as Mermaid → fix module cross-refs + nav links → match house style (`# Module NN:`, bold
Codename/Time/Scenario, `[SCREENSHOT: …]` placeholders, no YAML frontmatter, no emoji headings).

## Concerns tracker

| # | Concern | Status |
|---|---------|--------|
| 1 | Lab 00 truncated | ✅ resolved |
| 2 | Built-in skill *generates* a PDF | ⚠️ verify before Module 07 (storyline beat) |
| 3 | Tickets list from template | ✅ resolved (00 creates it explicitly) |
| 4 | Site-name mismatch | ✅ addressed + facilitator note |
| 5 | Underscores (skills) vs hyphens (workflow) | 📌 note in 07/09 |
| 6 | Auth context (user vs maker) | 📌 reconcile in 06/07 |
| 7 | The two .docx match the outlines | ⚠️ quick verify |
| 8 | Labs orphaned from site | ✅ resolved |
| 9 | Reza/Rex dependency | ✅ resolving (Bit) |
| 10 | Visuals | 🔄 diagrams inline; tenant screenshots → guided capture |

## Progress

- ✅ 00, 01, 02 published — **retrofit to introduce Bit** (pending)
- ⏳ 03–13 remaining
- Publish: push `agent-academy-labs` → `wip/rig/vitepress-rebuild` (deploy branch); preview at
  https://ulrikkerocks.github.io/BOOST/ (unlisted, noindex). CI uses `npm ci`.
