# New Copilot Studio UI — Research Notes

Source: Microsoft Learn docs + Microsoft Copilot Blog (researched June 16, 2026)

---

## The New Mental Model

The core shift is from a **tab/menu navigation model** to an **Overview page model**.

### Old Model
- Agent had a left sidebar with discrete sections: Topics, Actions, Flows, etc.
- You navigated INTO each section separately.
- Creating an agent had a separate wizard flow.

### New Model (current)
- **Home page** = natural language creation entry point.
  - A description box prompts: "Describe what you want your agent to do."
  - AI generates name, description, instructions, suggests knowledge/tools/triggers/channels.
  - Suggestions are session-only (don't persist if dismissed).
- **Overview page** = single-page authoring canvas after agent is created.
  - All sections visible at once (scroll down):
    - **Details** (name, description, agent status preview) — Edit button inline
    - **Select your agent's model** — AI model dropdown (options include GPT-5 Chat, GPT-4.1, etc.)
    - **Instructions** — Edit button inline (up to 8,000 chars)
    - **Knowledge** — Add knowledge sources; includes "General web search" toggle (enabled by default)
    - **Tools** — Add tools; includes "Work IQ" toggle (M365 personalization layer)
    - **Triggers** — Add triggers (event-based activation)
    - **Agents** — Sub-agents for multi-agent orchestration
    - **Topics** — Shows first 3 topics + "See all" link
    - **Suggested Prompts** — Starter prompts for Teams/M365 channels
  - **Channels is NOT on the Overview canvas** — accessed via the "+8" overflow menu in top nav
  - **Test pane** always visible on the right (restart session button = "new test session" icon)
  - **Publish** button top right
  - **+8 overflow menu** in the tab bar → expands to: Knowledge, Tools, Agents, Topics, Activity, Evaluation, Analytics, Channels

---

## Navigation Structure (New)

```
Left Sidebar (global):
├── Home
├── Agents (list)  ← currently active when inside an agent
├── Flows
├── Tools
└── ... (more)

Within an Agent (top tab bar):
├── Overview  ← PRIMARY authoring surface (always visible as tab)
└── +8 (overflow menu):
    ├── Knowledge
    ├── Tools
    ├── Agents
    ├── Topics
    ├── Activity
    ├── Evaluation
    ├── Analytics
    └── Channels  ← publish/deploy targets

Top action bar (top right within agent):
├── Publish  (button)
├── Test  (button)
└── ...  (more options)
```

---

## Key UI Element Changes

### Creating an Agent
- **New:** Home page → type natural language description → AI provisions agent → lands on Overview page
- **Old:** "New agent" button → wizard/form → opens topic editor

### Agent Overview Page
- **New:** Single scrollable page with all sections
- **Old:** Multiple tabs (Settings, Topics, Actions, etc.)

### Topics
- Still exist as a named concept
- Accessible from Overview page (Topics section) or left sidebar (Topics link)
- Creating topics: Still uses visual conversation designer (nodes)
- Authoring with Copilot: Describe what you want the topic to do → AI generates it
- Triggers: "Phrases" trigger is still the main entry point for conversational topics

### Agent Flows vs Workflows
- **Agent Flows** = original Copilot Studio flows (Power Automate-style experience inside Copilot Studio). Still available.
- **Workflows** = NEW experience (public preview / early release env). Redesigned visual canvas:
  - More intuitive layout
  - Agent nodes (embed agents inside a workflow)
  - Prompt nodes (single AI call with dynamic content)
  - Inline configuration
  - Node-level testing
  - Part of the "Agents + Workflows" push from Build 2026

### Testing
- Test pane always on right side of Overview page
- "New test session" icon (circular arrows/restart icon) = start fresh
- Activity map shows real-time which knowledge sources agent searches
- Can pin sessions and submit feedback

### Publishing
- `Publish` button at top right of Overview page
- Confirm dialog: "Publish this agent"
- After publish: three dots → Go to demo website
- Publishing to Teams/M365 Copilot requires Copilot Studio Authors role (set in PPAC)

### Settings
- Agent settings: gear ⚙️ on Overview page → language, solution, schema, advanced
- Environment settings: Settings in left sidebar (admin, licensing)

---

## What the Course Screenshots Currently Show (Old UI)

Based on module content, the course was written with the **old UI** where:
- Module 06 screenshots show: "wheel cog" for Agent Settings, separate Details/Knowledge sections (these still exist in new UI, just on Overview page)
- Module 07 would show Topics creation via left sidebar navigation
- Module 08 would show Adaptive Cards canvas (this is relatively stable)
- Module 09 would show Agent Flows creation (Power Automate-style)

> **Note:** Module 06 appears to already reference the new Overview page model (Details section, Knowledge section, AI suggestions sections visible). The last edit was 2026-02-19, which may mean it was partially updated. Verify by checking the actual screenshots.

---

## New Features to Add to Course (Not in Original)

### High Priority (affects Recruit course)
1. **New Overview page** — Show the full page layout upfront in Module 02 Fundamentals
2. **Workflows vs Agent Flows** — Module 09 should explain the difference and when to use each
3. **AI model selection** — Module 06 or 02, show how to choose primary AI model
4. **Activity map** — Already referenced in Module 06, but expand for Module 07+

### Medium Priority
5. **Multi-agent orchestration** — Brief mention in Module 02, expand in Module 10
6. **Agent status/readiness page** — New in May 2026; mention in Module 11 publish
7. **MCP** — Already in Special Ops; reference from Recruit as "next step"
8. **New licensing: Copilot Studio messages** — Module 12 update

### Out of Scope for Recruit (mention as "next level")
- Computer Use agents
- Real-time voice agents
- Frontier Tuning
- Custom metrics/evals

---

## Licensing Updates (Module 12)

Current licensing model (June 2026):
- **Copilot Studio standalone** = pay-per-message OR capacity pack
- **M365 Copilot license** = includes some Copilot Studio usage
- **Trial** = 30 days, extendable to 90 days, full capabilities EXCEPT publishing (need Authors role setup)
- **Copilot Studio Authors role** = required to publish from trial (set in PPAC)
- **Power Apps Developer Plan** = free developer environment for building/testing
- **After June 2026:** Teams classic chatbot app redirects to web app; classic chatbot creation ends

---

## Sources
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started
- https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/
- https://github.com/microsoft/agent-academy (source repo, docs/recruit/)
