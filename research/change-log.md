# Change Log — Old Course vs New Copilot Studio

This document tracks specific changes needed in each module, based on comparison
between the original course (microsoft/agent-academy) and the current Copilot Studio UI.

---

## Module 00: Course Setup ✅ Mostly Current

**Last edited:** 2026-03-16
**Risk:** Low

**What's still valid:**
- M365 trial setup process
- Power Apps Developer Plan signup
- SharePoint site creation (IT Help Desk template)
- Devices list setup with sample data

**What needs checking:**
- Step 2 (Copilot Studio trial): Verify trial URL and signup flow are current
- Step 4 (Enable publishing via PPAC): Verify the Copilot Studio Authors role setup still uses same PPAC path
- Screenshots may show old PPAC UI

**Action:** Light review + screenshot check only.

---

## Module 01: Introduction to Agents ✅ Stable

**Last edited:** Unknown
**Risk:** Low

**What's still valid:**
- Agent concepts: knowledge, skills, autonomy
- LLMs and RAG conceptual overview
- Declarative vs custom agents distinction

**What needs updating:**
- Mention new autonomous agents (event-triggered, proactive) as a third category
- Reference new multi-agent orchestration as an advanced scenario
- Update any screenshots of Copilot Studio home page

**Action:** Add 1–2 paragraphs on autonomous agents; update home page screenshot.

---

## Module 02: Copilot Studio Fundamentals ⚠️ Needs UI Update

**Last edited:** 2026-02-20
**Risk:** Medium

**What's still valid:**
- Four building blocks concept: Knowledge, Tools (Actions), Topics, Instructions ✅
- How the orchestrator works (conceptual) ✅
- Mermaid sequence diagram ✅

**What needs updating:**
- Building blocks terminology: Course says "Tools (Actions)" — new UI just says "Tools"
- Overview page diagram: Add a visual of the new Overview page layout
- Navigation: Update any screenshots showing old sidebar tabs
- Fifth building block to mention: Triggers (now a first-class concept on Overview page)

**Action:** Add Overview page walkthrough section with annotated screenshot. Update "Tools (Actions)" → "Tools". Add Triggers as a building block.

---

## Module 03: Create a Declarative Agent for M365 Copilot ⚠️ Needs Review

**Last edited:** ~2 weeks ago
**Risk:** Medium

**What's still valid:**
- Concept of extending M365 Copilot with declarative agents
- Instructions/knowledge grounding approach

**What needs checking:**
- Navigation path to create declarative vs custom agent (the distinction still exists but entry point may differ)
- Screenshots of M365 Copilot integration

**Action:** Verify navigation path; update screenshots.

---

## Module 04: Creating a Solution ⚠️ Recently Updated

**Last edited:** 5 days ago (June 11, 2026)
**Risk:** Low-Medium (just updated)

**What's still valid:**
- Solution creation in PPAC
- Setting preferred solution in Copilot Studio
- Solution publisher setup

**What needs checking:**
- The recent update may have addressed new UI changes — read the updated content carefully
- Verify the "preferred solution" setting is still in the same location (Settings > Advanced)

**Action:** Read updated module, verify steps against current UI.

---

## Module 05: Using Pre-Built Agents ⚠️ UI Changes

**Last edited:** ~2 months ago
**Risk:** Medium

**What's still valid:**
- Concept of agent templates

**What needs updating:**
- Template gallery has likely changed (new templates added)
- Navigation to find templates may have changed
- Overview page now shown after selecting a template

**Action:** Update navigation steps + screenshots.

---

## Module 06: Build a Custom Agent ⚠️ Partially Updated

**Last edited:** 2026-02-19
**Risk:** Medium

**What's still valid:**
- Natural language creation flow (already in new UI)
- Lab steps appear to reference Overview page sections (Details, Knowledge, etc.)
- Knowledge source types (SharePoint, websites, files) ✅

**What needs checking:**
- Screenshots (assets/6.1_*.png etc.) — do they show current UI?
- "wheel cog" → now gear ⚙️ icon
- AI suggestions interface (dismiss, add buttons)
- Web Search toggle location

**Action:** Verify screenshots match current UI. Update any changed UI paths.

---

## Module 07: Add a Topic with Triggers 🔴 Needs Update

**Last edited:** ~2 months ago
**Risk:** High

**What's likely outdated:**
- Navigation to create a topic (old: left sidebar → Topics → New topic; new: Overview page → Topics section → Add topic, OR left sidebar → Topics)
- Topic canvas UI may have updated
- Trigger phrases entry (still exists but interface may differ)
- "Add phrase trigger" step-by-step instructions

**What's still valid:**
- Concept of topics and triggers ✅
- Conversation nodes (Message, Question, Condition) ✅
- Natural language authoring with Copilot ✅

**Action:** Full step-by-step rewrite for topic creation navigation. New screenshots needed.

---

## Module 08: Enhance with Adaptive Cards 🔴 Needs Verification

**Last edited:** ~2 months ago
**Risk:** High

**What's likely outdated:**
- Navigation to Adaptive Card builder within a topic node
- Power Fx formula interface may have changed
- Integration with SharePoint data

**What's still valid:**
- Adaptive Card Designer concept ✅
- Power Fx for data binding ✅
- Card schema structure ✅

**Action:** Walk through lab in live Copilot Studio to verify all navigation steps. Update screenshots.

---

## Module 09: Automate with Agent Flows 🔴 Major Update Needed

**Last edited:** ~2 months ago
**Risk:** Very High

**What's changed:**
- **New Workflows experience** launched (May 2026) — now in early release environments
- Two options now exist:
  - **Agent Flows**: original experience (Power Automate-style designer in Copilot Studio)
  - **Workflows**: new redesigned canvas with agent nodes, prompt nodes, inline config
- The course only covers Agent Flows; needs to explain both
- Navigation path to create a flow may have changed

**Workshop Decision Needed:**
- Use Agent Flows (stable, familiar) OR new Workflows (new, preview)?
- Recommendation: Teach Agent Flows (GA, stable) but **mention/show Workflows as the future direction**

**Action:** Major rewrite. Verify Agent Flows navigation is unchanged. Add "Workflows Preview" callout section. Update screenshots.

---

## Module 10: Add Event Triggers 🔴 Needs Update

**Last edited:** ~2 months ago
**Risk:** High

**What's changed:**
- Autonomous agents and event triggers have evolved significantly
- New trigger types available (beyond just timer/message-based)
- Event trigger configuration on Overview page (Triggers section)
- The "Frontier program" mentioned for MCP — may no longer be required

**What's still valid:**
- Concept of autonomous/proactive agent behavior ✅
- Dataverse row-change triggers ✅ (still a core pattern)

**Action:** Verify Frontier program requirement. Update trigger setup navigation. New screenshots.

---

## Module 11: Publish Your Agent ⚠️ Needs Update

**Last edited:** ~2 months ago
**Risk:** Medium

**What's changed:**
- Publish button location moved to top of Overview page
- "Agent lifecycle visibility" improvements (new readiness/status page, May 2026)
- Go to demo website: now from three dots menu on Overview page
- Teams channel: may require M365 Copilot license depending on agent type

**What's still valid:**
- Publish to Teams concept ✅
- Demo website ✅
- Channel configuration ✅

**Action:** Update publish navigation steps. Add agent status/readiness section.

---

## Module 12: Understanding Licensing ⚠️ Needs Update

**Last edited:** ~2 months ago
**Risk:** Medium

**What's changed (key):**
- After June 2026: Teams classic chatbot creation app is retired → redirects to web app
- GPT-4o retired Oct 2025; default model is now GPT-4.1
- New model options (GPT-5, Claude, Mistral) have their own cost implications
- Agent usage estimator now available (April 2026)
- New Copilot Studio messages model (pay-per-use)

**What's still valid:**
- Basic licensing tiers concept ✅
- Trial limitations ✅
- Developer plan ✅

**Action:** Update model/billing details. Add Teams app retirement note. Reference usage estimator.

---

## Module 13: Badge ✅ Stable

No updates needed.

---

## Summary: Priority Order for Updates

| Priority | Module | Effort |
|---|---|---|
| 1 (Critical) | 09 — Agent Flows/Workflows | High |
| 2 (Critical) | 07 — Topics + Triggers | High |
| 3 (High) | 02 — Fundamentals | Medium |
| 4 (High) | 08 — Adaptive Cards | Medium |
| 5 (High) | 10 — Event Triggers | High |
| 6 (Medium) | 06 — Custom Agent | Low-Medium |
| 7 (Medium) | 11 — Publish | Low |
| 8 (Medium) | 12 — Licensing | Low |
| 9 (Low) | 05 — Pre-Built Agents | Low |
| 10 (Low) | 04 — Solution | Low (just updated) |
| 11 (Low) | 03 — Declarative Agent | Low |
| 12 (Low) | 01 — Introduction | Low |
| 13 (Low) | 00 — Setup | Low |
