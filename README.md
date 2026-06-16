# BOOST — Copilot Agent Academy Recruit Course Update

**Project:** Update the [Microsoft Copilot Agent Academy Recruit Course](https://microsoft.github.io/agent-academy/recruit/) for delivery as a 3-week workshop.

**Context:** Microsoft released a significantly redesigned version of Copilot Studio in 2025/2026. The new UI introduces a remodeled Overview page as the primary authoring surface, a new Workflows experience (alongside Agent Flows), new agent creation patterns, and updated navigation throughout. Approximately half the existing course screenshots and step-by-step instructions reference the old UI.

**Goal:** Produce an updated, workshop-ready version of the full Recruit course (Modules 00–13) that reflects the current Copilot Studio experience.

---

## Source Material

| Resource | URL |
|---|---|
| Official course site | https://microsoft.github.io/agent-academy/recruit/ |
| GitHub source repo | https://github.com/microsoft/agent-academy |
| Copilot Studio docs | https://learn.microsoft.com/en-us/microsoft-copilot-studio/ |
| What's New | https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new |
| Copilot Studio Blog | https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/ |

---

## Course Structure (Original)

| Module | Title | Time | Status |
|---|---|---|---|
| 00 | 🧰 Course Setup | 30 min | ✅ Likely current |
| 01 | 🧠 Introduction to Agents | 30 min | ✅ Conceptual - likely stable |
| 02 | 🛠️ Copilot Studio Fundamentals | 30 min | ⚠️ UI screenshots may be outdated |
| 03 | 👩‍💻 Create a Declarative Agent for M365 Copilot | - | ⚠️ Needs review |
| 04 | 🧩 Creating a Solution | - | ⚠️ Recently updated (5 days ago) |
| 05 | 🚀 Get Started with Pre-Built Agents | - | ⚠️ UI changes |
| 06 | ✍️ Build a Custom Agent | 75 min | ⚠️ Overview page is new |
| 07 | 🧠 Add a Topic with Triggers | - | 🔴 Topic authoring UI changed |
| 08 | 🪪 Enhance with Adaptive Cards | - | 🔴 New UI affected |
| 09 | 🔁 Automate with Agent Flows | - | 🔴 New Workflows experience added |
| 10 | 🧭 Add Event Triggers | - | 🔴 Autonomous agent changes |
| 11 | 📢 Publish Your Agent | - | ⚠️ Publish flow changed |
| 12 | 🪪 Understanding Licensing | - | ⚠️ Licensing model updated |
| 13 | 🚨 Securing Your Recruit Badge | - | ✅ Stable |

---

## What Changed in Copilot Studio (Key for Course Update)

### New UI Mental Model

**Old model:** Agent editor had tabs/sections in left sidebar (Topics, Actions/Flows, etc.)

**New model (2025/2026):** Central **Overview page** is the primary authoring surface with all sections visible at once:
- Instructions (edit inline)
- Knowledge sources
- Tools
- Topics
- Connected Agents
- Triggers
- Channels
- Suggested Prompts
- Testing pane (right side, always visible)

### Key UI Changes

1. **Home page** — Natural language creation box is prominent. Describe your agent → AI generates name, description, instructions, suggests knowledge/tools/triggers.
2. **Overview page** — New central authoring canvas. All agent components visible in one scrollable page.
3. **Settings** — Accessed via gear ⚙️ icon (language, solution, schema name, primary AI model).
4. **Publish** — Prominent `Publish` button at top of page.
5. **Test pane** — Always-visible on right side with "new test session" icon.
6. **Workflows** — New visual designer (in addition to Agent Flows). Now in early release environments. Redesigned canvas with agent nodes, inline config, node-level testing.
7. **Topics** — Still exist, now accessible from Overview page and sidebar. Authored with natural language via Copilot.
8. **Models** — New primary model selection: GPT-4.1 (default), GPT-5, GPT-5.5 Reasoning, Claude Sonnet 4.5/4.6, Mistral Medium 3.5.
9. **Multi-agent orchestration** — Now GA (A2A protocol).
10. **Computer Use** — Now GA (agents control browser/desktop UI).
11. **MCP (Model Context Protocol)** — Full integration with MCP servers.

### Features the Course Must Address

| Feature | Module(s) | Action |
|---|---|---|
| New Overview page authoring | 02, 06, 07, 08, 09, 10 | Update screenshots + steps |
| Natural language agent creation | 06 | Verify steps still match new UI |
| New Workflows (vs Agent Flows) | 09 | Update with new Workflows experience |
| AI model selection | 02, 06 | Add new model selection section |
| Topics via Overview page | 07 | Update navigation steps |
| Adaptive Cards on new canvas | 08 | Update screenshots |
| Event triggers (autonomous) | 10 | Update for new triggers model |
| Publishing flow | 11 | Update steps for new publish flow |
| New licensing tiers | 12 | Update for current plans |

---

## Workshop Format

**Duration:** 1 day (hands-on workshop)
**Audience:** Makers, IT Pros, Power Platform enthusiasts
**Environment:** Each participant needs own M365 tenant + Copilot Studio trial

---

## Folder Structure

```
BOOST/
├── README.md                    # This file
├── research/
│   ├── old-course-notes.md      # Notes from original course modules
│   ├── new-ui-notes.md          # New Copilot Studio UI documentation
│   └── change-log.md            # What changed and where
├── workshop/
│   ├── 00-course-setup/         # Updated module
│   ├── 01-introduction/         # Updated module
│   ├── 02-fundamentals/         # Updated module
│   ├── 03-declarative-agent/    # Updated module
│   ├── 04-solution/             # Updated module
│   ├── 05-prebuilt-agents/      # Updated module
│   ├── 06-custom-agent/         # Updated module
│   ├── 07-topics-triggers/      # Updated module
│   ├── 08-adaptive-cards/       # Updated module
│   ├── 09-agent-flows/          # Updated module
│   ├── 10-event-triggers/       # Updated module
│   ├── 11-publish/              # Updated module
│   ├── 12-licensing/            # Updated module
│   └── facilitator-guide.md     # Facilitator notes
└── assets/
    └── screenshots/             # New UI screenshots
```

---

## Next Steps

1. [ ] Review each module against the live Copilot Studio UI
2. [ ] Document exact UI differences per module
3. [ ] Rewrite/update modules 06–11 (most impacted)
4. [ ] Update screenshots with new UI
5. [ ] Write facilitator guide with timing and tips
6. [ ] Test full workshop flow end to end
