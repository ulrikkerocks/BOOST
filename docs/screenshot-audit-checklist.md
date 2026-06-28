# Screenshot Audit Checklist (QA Pass)

**Purpose:** The **final quality gate** before workshop delivery. Use this *after* screenshots have been captured and wired in (per [screenshot-capture-plan.md](screenshot-capture-plan.md)) to verify every image is current, correct, clean, and accessible.

- **Capture worklist** (what's missing, how to capture it) → [screenshot-capture-plan.md](screenshot-capture-plan.md)
- **This document** (verify what's been captured) → you are here

> This checklist was rewritten in June 2026. It previously referenced the *original* Microsoft course's screenshot filenames (e.g. `6.1_*.png`); those don't apply to this rewrite, which uses inline `[SCREENSHOT: …]` placeholders replaced by images under `docs/assets/screenshots/`.

---

## How to use

1. Sign in to https://copilotstudio.microsoft.com (and the satellite surfaces: Power Apps, PPAC, M365 Admin, SharePoint, Teams).
2. For each module below, open its `README.md` on the [live site](https://ulrikkerocks.github.io/BOOST/) and walk the screenshots top to bottom.
3. Mark each module's row: ✅ all good · ⚠️ minor issues noted · 🔴 needs recapture.

---

## Per-module sign-off

| Module | # shots | Images render | UI is current | Redacted | Alt text | Status |
|---|---:|:--:|:--:|:--:|:--:|:--:|
| 00 Course Setup | 15 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 01 Introduction *(3 diagrams)* | 3 | ☐ | n/a | n/a | ☐ | ☐ |
| 02 Fundamentals | 6 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 03 Declarative Agent | 8 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 04 Solution | 10 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 05 Pre-built Agents | 8 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 06 Custom Agent | 24 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 07 Topics & Triggers | 30 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 08 Adaptive Cards | 16 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 09 Agent Flows | 18 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 10 Event Triggers | 23 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 11 Publish | 26 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 12 Licensing | 3 | ☐ | ☐ | ☐ | ☐ | ☐ |
| 13 Badge | 3 | ☐ | ☐ | ☐ | ☐ | ☐ |

**Column meaning:**
- **Images render** — no broken images; correct path; readable at page width.
- **UI is current** — matches Copilot Studio / Power Platform as of delivery (see watch-list below).
- **Redacted** — no real tenant names, emails, GUIDs, or personal data; uses Contoso naming.
- **Alt text** — every image has descriptive alt text (the placeholder text is a good default).

---

## Known UI changes to watch for

Screenshots captured even a few months apart can drift. Flag any image still showing the **left column** below:

| Old UI element | Current (2025/2026) UI element |
|---|---|
| Separate "Topics" left sidebar tab | Topics section on the Overview page / Topics tab in agent nav |
| Separate "Actions / Skills" section | "Tools" section on the Overview page |
| Agent-level "Settings" in left sidebar | Gear ⚙️ icon on the Overview page |
| Agent creation wizard | Home page natural-language description box |
| Multiple top-level tabs in the agent | Single Overview page with sections |
| "Publish" in a navigation menu | "Publish" button at the top-right of the Overview page |
| GPT-4o model references | GPT-4.1 default (GPT-5 / Claude / Mistral options) |

---

## High-priority shots (verify these first)

These carry the most instructional weight — a stale one here is most likely to derail a participant:

- [ ] **06** L124 — Overview page after agent creation (the core mental-model shot)
- [ ] **06** L485 — Model selection dropdown (GPT-4.1) — model list changes often
- [ ] **07** L235 — Power Fx Filter expression editor
- [ ] **08** L288 — Populated Adaptive Card preview
- [ ] **10** L160 — Overview Triggers section ("+ Add trigger")
- [ ] **11** L98 — Publish button location (top-right)
- [ ] **11** L138 — Channels page (verify Channels nav path in current UI)
- [ ] **12** L98 — Copilot Studio purchase/licensing options (licensing changes frequently)

---

## Cross-cutting checks

- [ ] Consistent capture style — same browser zoom, light/dark mode, and crop convention throughout.
- [ ] No personal/tenant data anywhere (names, emails, GUIDs, real ticket data).
- [ ] Images are reasonably sized (compress large PNGs; keep page loads fast).
- [ ] Each image sits next to the step it illustrates (not drifted up/down after edits).
- [ ] Module 01's three diagrams render (Mermaid blocks or exported images).
- [ ] Spot-check on mobile width — wide screenshots remain legible / don't overflow.

---

## If a screenshot is outdated

1. **Recapture** following [screenshot-capture-plan.md](screenshot-capture-plan.md) and replace the file in place (same filename).
2. If you can't recapture immediately, **add a facilitator note** flagging the difference, and log it in the per-module table above as ⚠️.
3. Consider contributing fixes upstream to [microsoft/agent-academy](https://github.com/microsoft/agent-academy) where they apply to the source course.
