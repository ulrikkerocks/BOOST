# BOOST — Copilot Agent Academy Recruit Course Update

**Project:** Update the [Microsoft Copilot Agent Academy Recruit Course](https://microsoft.github.io/agent-academy/recruit/) for delivery as a **1-day hands-on workshop**, reflecting the redesigned Copilot Studio UI (2025/2026).

**Delivery target:** 3 weeks from June 2026 (see [facilitator guide](docs/facilitator-guide.md)).

**Live site:** https://ulrikkerocks.github.io/BOOST/

---

## Context

Microsoft significantly redesigned Copilot Studio in late 2025. The new UI introduces a central **Overview page** as the primary authoring surface, a new **Workflows** experience (alongside Agent Flows), natural-language agent creation, and updated navigation throughout. Roughly half the original course's screenshots and step-by-step instructions referenced the old UI.

This repo contains a fully rewritten version of the Recruit course (Modules 00–13) that reflects the current experience, published as a GitHub Pages site, plus the supporting research and workshop-delivery materials.

---

## Current Status

| Area | Status |
|---|---|
| Module content (00–13) | ✅ Written — all 14 modules rewritten for the new UI (~6,100 lines) |
| Research & gap analysis | ✅ Done — see [research/change-log.md](research/change-log.md) |
| Facilitator guide | ✅ Done — [docs/facilitator-guide.md](docs/facilitator-guide.md) |
| Participant reference card | ✅ Done — [docs/participant-reference-card.md](docs/participant-reference-card.md) |
| GitHub Pages site | ✅ Live — Jekyll (Minima dark) + custom "Tech Forward" theme |
| **Screenshots** | 🔴 **Not captured** — 193 `[SCREENSHOT: …]` placeholders across the modules. See [docs/screenshot-capture-plan.md](docs/screenshot-capture-plan.md) |
| Full end-to-end delivery rehearsal | ⬜ Pending |

---

## Repository Structure

```
BOOST/
├── README.md                       # This file
├── research/                       # Analysis behind the rewrite
│   ├── old-course-notes.md         # Notes from the original course modules
│   ├── new-ui-notes.md             # New Copilot Studio UI documentation
│   └── change-log.md               # Per-module gap analysis + priority order
├── docs/                           # The published GitHub Pages site (source)
│   ├── _config.yml                 # Jekyll config (Minima dark, baseurl /BOOST)
│   ├── README.md                   # Course landing page
│   ├── facilitator-guide.md        # Delivery notes, timing, pitfalls
│   ├── participant-reference-card.md
│   ├── screenshot-audit-checklist.md
│   ├── screenshot-capture-plan.md  # Worklist for the 193 pending screenshots
│   ├── assets/main.scss            # "Tech Forward" custom theme
│   ├── modules/00-course-setup … 13-securing-recruit-badge/   # 14 module READMEs
│   ├── 02-copilot-studio-fundamentals/overview-page-orientation.md  # supplemental
│   └── 09-add-an-agent-flow/workflows-callout.md                    # supplemental
└── assets/
    └── presentation/               # Conference decks (EPPC26 / Color Cloud 2026) + extracted images
```

> **Note:** GitHub Pages builds from the `docs/` folder on the `wip/rig/recruit-course-update` branch (legacy Jekyll build). There is no `Gemfile` or Actions workflow — the site relies on GitHub's built-in `github-pages` gem, so only Pages-whitelisted plugins are available.

---

## The Course

A progressive, hands-on build of the **Contoso Helpdesk Agent** — an IT helpdesk assistant — across 14 modules. Full module list, schedule, and learning path are in the [course landing page](docs/README.md).

| Phase | Modules | Focus |
|---|---|---|
| Foundation | 00–02 | Environment setup, agent concepts, Copilot Studio interface |
| Getting started | 03–05 | Declarative agents, solutions (ALM), pre-built templates |
| Build your agent | 06–09 | Custom agent, topics & triggers, Adaptive Cards, Agent Flows |
| Advanced | 10–11 | Event triggers (autonomous), publishing to Teams |
| Production | 12–13 | Licensing & cost, badge / wrap-up |

**Format:** 1 full day (~8 hours hands-on), or self-paced over 1–2 weeks.
**Audience:** Makers, IT Pros, Power Platform enthusiasts.
**Environment:** Each participant needs their own M365 tenant + Copilot Studio trial.

---

## What Changed in Copilot Studio (Reference)

The new mental model, in brief:

- **Old:** Agent editor with tabs/sections in a left sidebar (Topics, Actions, Settings…).
- **New (2025/2026):** A single **Overview page** showing all components at once — Details, Instructions, Knowledge, Tools, Triggers, Agents, Topics, Suggested Prompts — with an always-visible **Test pane** and a top-right **Publish** button.

Other notable changes the course addresses: natural-language agent creation, new AI model selection (GPT-4.1 default; GPT-5, Claude, Mistral options), the new **Workflows** experience (vs. Agent Flows), GA multi-agent orchestration, and updated licensing.

For the full per-module breakdown of what changed and what needed updating, see **[research/change-log.md](research/change-log.md)**.

---

## Working on This Repo

**Edit course content:** modify the module `README.md` files under [docs/modules/](docs/modules). Markdown renders directly on the Pages site.

**Preview the site:** push to `wip/rig/recruit-course-update`; GitHub Pages rebuilds from `docs/` (~60–90s). Check build status with:

```bash
gh api repos/ulrikkerocks/BOOST/pages/builds/latest
```

**Theme changes:** edit [docs/assets/main.scss](docs/assets/main.scss) (it `@import`s the Minima theme, then overrides).

---

## Remaining Work

1. [ ] **Capture the 193 screenshots** — biggest remaining task. Plan in [docs/screenshot-capture-plan.md](docs/screenshot-capture-plan.md).
2. [ ] Replace each `[SCREENSHOT: …]` placeholder with the captured image.
3. [ ] Create the 3 conceptual diagrams in Module 01 (architecture / sequence / multi-agent).
4. [ ] Run a full end-to-end delivery rehearsal against a live tenant.
5. [ ] Final screenshot audit against the current UI ([checklist](docs/screenshot-audit-checklist.md)).

---

## Source Material

| Resource | URL |
|---|---|
| Official course site | https://microsoft.github.io/agent-academy/recruit/ |
| GitHub source repo | https://github.com/microsoft/agent-academy |
| Copilot Studio docs | https://learn.microsoft.com/en-us/microsoft-copilot-studio/ |
| What's New | https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new |
| Copilot Studio Blog | https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/ |

**License:** MIT. Original course © Microsoft; this is an independent modernization for workshop delivery.
