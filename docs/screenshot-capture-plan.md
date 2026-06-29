# Screenshot Capture Plan

**Purpose:** The rebuilt course (Bit, new experience) contains **91 `[SCREENSHOT: …]` placeholders** and **zero captured images**. This is the worklist for capturing them, grouped by *where* each is taken (so you sign into each surface once) and tracked per module.

> ♻️ **Rewritten for the new course (Bit).** The previous version of this plan listed 193 shots for the *old* modules (Devices list, Topics, Power Fx, Agent Flows, Dataverse table). Every placeholder changed in the rewrite — this plan reflects the **current** 91.

---

## Prerequisite: you have to build Bit first

These can't be captured cold. The course is a progressive build of **Bit**, and most shots show Bit (or the supporting setup) in a specific state. To capture them you need a live M365 tenant + Copilot Studio (new experience), the IT Help Desk site + Tickets list + the two knowledge docs (Module 00), and Bit built up through each module's steps.

**The efficient path:** run the course end-to-end on a clean tenant, capturing as you go. The state at each step *is* the screenshot. Budget it as a guided build session, not a separate "screenshot day."

---

## Scope at a glance — 91 shots by capture surface

| Capture surface | ~Count | Where | Notes |
|---|---:|---|---|
| **Copilot Studio** (Build page, Preview, Skills, Tools, Settings, Model, Triggers, Workflow designer, Adaptive Card editor, Evaluate, Publish, Monitor, templates, declarative) | ~55 | 00, 02, 03, 05–12 | The dominant bucket — one long build session covers most |
| **Power Apps maker / Solutions** | ~12 | 04, 06, 13 | Publisher, solution, Objects, export |
| **SharePoint** | ~5 | 00, 07 | Site, Tickets list, sample rows, ticket row |
| **Microsoft 365 Copilot (chat)** | ~4 | 03, 11 | @mention + response; Bit in M365 Copilot |
| **PPAC (Power Platform Admin Center)** | ~3 | 00, 12 | Environments, security roles, extend trial |
| **M365 Admin Center** | ~3 | 00, 12 | Security groups, members, purchase options |
| **Public signup pages** (no tenant needed) | ~3 | 00 | M365 trial, CS trial activation, Power Apps Dev Plan |
| **Outlook inbox** | ~2 | 07, 10 | PDF confirmation email, escalation email |
| **Word / docs** | ~1 | 00 | The two knowledge docs side by side |

### Per-module counts
| Module | # | Module | # |
|---|--:|---|--:|
| 00 Course Setup | 14 | 07 Skills + Tools | 5 |
| 01 Introduction | 0 *(Mermaid diagrams — done)* | 08 Adaptive Cards | 4 |
| 02 Fundamentals | 6 | 09 Workflows | 8 |
| 03 Declarative | 8 | 10 Event Triggers | 5 |
| 04 Solution | 9 | 11 Evaluate/Publish | 6 |
| 05 Pre-built | 7 | 12 Licensing | 3 |
| 06 Build Bit | 14 | 13 Badge | 2 |

---

## Suggested capture order

1. **Module 00 satellite surfaces first** — public signup pages, PPAC, M365 Admin, SharePoint, Word. These set up the environment everything else depends on. *(In the facilitated workshop these are pre-provisioned — capture them once on a clean tenant for the online course.)*
2. **One Copilot Studio build session, Modules 02 → 11 in order** — ~55 of 91. Build Bit step by step; capture each screen as you reach it. Modules 06 → 10 must be in sequence (each builds on the last).
3. **Power Apps / Solutions** — Module 04 (solution) and the verify/export shots (06, 13) interleave with the CS session.
4. **M365 Copilot, Outlook, M365 Admin** — channel + email shots come after Bit is published/acting.

---

## Conventions

**Storage:** `docs/public/screenshots/<module-number>/` — e.g. `docs/public/screenshots/06/`. (VitePress serves `docs/public/` at the site root; with `base: '/BOOST/'` the served path is `/BOOST/screenshots/...`.)

**Naming:** `NN_descriptive-name.png`, numbered in the order they appear in the module — e.g. `06/03_bit-named-with-icon.png`.

**Wiring into the module:** replace each placeholder line, e.g.

```markdown
[SCREENSHOT: Build page showing the agent named Bit with an icon and accent color]
```

with a VitePress image reference (absolute path includes the base):

```markdown
![Build page showing the agent named Bit with an icon and accent color](/screenshots/06/03_bit-named-with-icon.png)
```

Keep the placeholder text as the alt text — it's already descriptive and accessible.

**Redaction:** scrub real tenant names, emails, and GUIDs before publishing. Use the Contoso naming the course assumes (helpdesk@contoso.com, IT Help Desk site, etc.).

---

## Worklist by module

Line numbers point to the placeholder in each module's `index.md` (will drift as images are wired in — re-grep `\[SCREENSHOT:` if unsure).

### Module 00 — Course Setup (14)
- [ ] L62 — M365 trial signup ("Try for free") *(public)*
- [ ] L81 — Copilot Studio trial activation page *(public)*
- [ ] L86 — Copilot Studio Home, description box *(Copilot Studio)*
- [ ] L100 — Home with the **Try it now** toggle highlighted *(Copilot Studio)*
- [ ] L134 — Power Apps Developer Plan signup *(public)*
- [ ] L147 — PPAC Environments list *(PPAC)*
- [ ] L168 — M365 Admin, Security groups *(M365 Admin)*
- [ ] L187 — Security group members flow *(M365 Admin)*
- [ ] L203 — PPAC → Security roles → Copilot Studio Authors *(PPAC)*
- [ ] L226 — SharePoint home, "Create site" *(SharePoint)*
- [ ] L240 — SharePoint "+ New" → List *(SharePoint)*
- [ ] L265 — Add Choice column (Priority) *(SharePoint)*
- [ ] L278 — Tickets list with sample rows *(SharePoint)*
- [ ] L323 — The two knowledge docs side by side *(Word)*

### Module 01 — Introduction (0)
Three diagrams — **done** as Mermaid (no screenshots).

### Module 02 — New Fundamentals (6)
- [ ] L46 — Full Build page (all blocks + Preview) *(CS)*
- [ ] L99 — Preview pane, maker-vs-end-user toggle *(CS)*
- [ ] L127 — Instructions block *(CS)*
- [ ] L156 — Knowledge block (two docs) *(CS)*
- [ ] L188 — Skills block (four skills) *(CS)*
- [ ] L212 — Tools block ("+ Add a tool") *(CS)*

### Module 03 — Declarative Agent (8)
- [ ] L81 — CS Home description box *(CS)*
- [ ] L101 — Declarative agent creation dialog *(CS)*
- [ ] L124 — Instructions field *(CS)*
- [ ] L141 — Add knowledge (SharePoint URL) *(CS)*
- [ ] L154 — Publish confirmation *(CS)*
- [ ] L169 — M365 Copilot chat input *(M365 Copilot)*
- [ ] L177 — M365 Copilot @mention dropdown *(M365 Copilot)*
- [ ] L193 — M365 Copilot response + citation *(M365 Copilot)*

### Module 04 — Solution (9)
- [ ] L92 — Maker portal, dev environment selected *(Power Apps)*
- [ ] L99 — Solutions section *(Power Apps)*
- [ ] L108 — New solution dialog, "New publisher" *(Power Apps)*
- [ ] L124 — New publisher dialog (Contoso) *(Power Apps)*
- [ ] L138 — "+ New solution" *(Power Apps)*
- [ ] L150 — New solution dialog (Contoso Helpdesk Agent) *(Power Apps)*
- [ ] L164 — Solution details, empty Objects *(Power Apps)*
- [ ] L186 — Preferred solution dropdown *(CS)*
- [ ] L217 — Solution Objects with components *(Power Apps)*

### Module 05 — Pre-built (7) ✅ DONE
- [x] L77 — Agents page, "Start with an agent template" *(CS)* → `01_agents-page-start-from-template.png`
- [x] L85 — Website Q&A template config screen *(CS)* → `02_template-preview.png`
- [x] L112 — Template config with "Create" button *(CS)* → `03_template-create-button.png`
- [x] L119 — Build page after agent created *(CS)* → `04_template-agent-build-page.png`
- [x] L141 — Topics + Suggested prompts sections *(CS)* → `05_topics-and-suggested-prompts.png`
- [x] L172 — Add knowledge → SharePoint URL entry *(CS)* → `06_add-knowledge-sharepoint.png`
- [x] L187 — Preview response with citations *(CS)* → `07_preview-response-with-citation.png`
- Note: "IT Help Desk" template not present in this env; used "Website Q&A" instead. Module text updated accordingly.

### Module 06 — Build Bit (14)
- [ ] L68 — Home description box *(CS)*
- [ ] L84 — Home with the IT support description *(CS)*
- [ ] L97 — Build page, agent named Bit + icon *(CS)*
- [ ] L129 — Instructions block (Bit) *(CS)*
- [ ] L147 — Settings (solution/moderation/auth) *(CS)*
- [ ] L176 — Greeting + four suggested prompts *(CS)*
- [ ] L195 — Knowledge upload dialog *(CS)*
- [ ] L202 — Knowledge: both docs added *(CS)*
- [ ] L217 — Memory toggled on *(CS)*
- [ ] L235 — Preview: help desk hours + reasoning *(CS)*
- [ ] L250 — Preview: Power BI self-service + toggle *(CS)*
- [ ] L277 — Preview reasoning expanded *(CS)*
- [ ] L289 — Model block (GPT-4.1) *(CS)*
- [ ] L314 — Solution showing Bit under Objects *(Power Apps)*

### Module 07 — Skills + Tools (5)
- [ ] L190 — Add Outlook "Send an email (V2)" tool *(CS)*
- [ ] L206 — Add SharePoint "Create item" tool *(CS)*
- [ ] L225 — Preview: password-reset flow + email *(CS)*
- [ ] L251 — New ticket row + confirmation email *(SharePoint + Outlook)*
- [ ] L284 — Email with the PDF report attached *(Outlook)*

### Module 08 — Adaptive Cards (4)
- [ ] L55 — Example ticket confirmation card *(CS / designer)*
- [ ] L113 — Card editor showing the JSON *(CS)*
- [ ] L145 — smart-triage updated to present the card *(CS)*
- [ ] L161 — Preview: rendered ticket card *(CS)*

### Module 09 — Workflows (8)
- [ ] L57 — New workflow designer (named) *(CS)*
- [ ] L71 — Input parameters *(CS)*
- [ ] L80 — Get manager (V2) *(CS)*
- [ ] L92 — Start and wait for an approval *(CS)*
- [ ] L103 — If/else on outcome *(CS)*
- [ ] L120 — Parallel branches (approval + respond) *(CS)*
- [ ] L146 — software-installation-request calls the workflow *(CS)*
- [ ] L162 — Preview: approval started + manager's Approvals card *(CS / Approvals)*

### Module 10 — Event Triggers (5)
- [ ] L82 — Triggers area, "+ Add trigger" *(CS)*
- [ ] L89 — SharePoint "item created" trigger on Tickets *(CS)*
- [ ] L99 — Trigger filter: Priority High/Critical *(CS)*
- [ ] L138 — Escalation email step mapping fields *(CS / workflow)*
- [ ] L171 — Inbox: auto-escalation email *(Outlook)*

### Module 11 — Evaluate / Publish (6)
- [ ] L44 — Evaluate area, "Quick conversation set" *(CS)*
- [ ] L66 — Evaluation results + scores *(CS)*
- [ ] L80 — Publish dialog, channels *(CS)*
- [ ] L91 — Bit inside M365 Copilot *(M365 Copilot)*
- [ ] L100 — Share dialog *(CS)*
- [ ] L108 — Monitor tab *(CS)*

### Module 12 — Licensing (3)
- [ ] L66 — PPAC, "Extend trial" *(PPAC)*
- [ ] L83 — M365 Admin, Copilot Studio purchase options *(M365 Admin)*
- [ ] L181 — Monitor tab, session metrics *(CS)*

### Module 13 — Badge (2)
- [ ] L95 — Solution showing Bit and components *(Power Apps)*
- [ ] L105 — Export solution dialog *(Power Apps)*

---

## Capture methods

- **You capture, I wire (recommended).** During a tenant run-through, you/Nick screenshot each step (you're building Bit anyway). Save them per the naming convention; I replace the placeholders and help redact. Best fit because several steps mutate your tenant.
- **I drive your Chrome.** Install/connect the **Claude in Chrome** extension and sign into your tenant; I navigate read-only screens you've already built and capture them. I won't perform tenant-mutating steps (site/group/agent creation) on your account — you do those, I capture.
- **Public pages now.** The three signup pages (M365 trial, CS trial activation, Power Apps Dev Plan) need no tenant and can be captured anytime.

After capture, this file's checkboxes become the QA pass — see [screenshot-audit-checklist.md](screenshot-audit-checklist.md).
