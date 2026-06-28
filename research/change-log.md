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

## Module 07: Add a Topic with Triggers ⚠️ Likely Current — Screenshots to Verify

**Last edited:** 2026-02-19
**Risk:** Low-Medium

**Confirmed current in the source:**
- Lab 7.1.01: "Select the Topics tab near the name of the agent" ✅ (new UI)
- Lab 7.3.22: "Select the Overview tab and select Edit" ✅ (new UI Overview page)
- Lab 7.3.23+: References Instructions editing on Overview page ✅

**What still needs checking:**
- Screenshots — do they show the current UI as of June 2026?
- Topic name/trigger description entry UI (small changes possible)
- "Topics tab near the name" — in new UI this may be labeled differently

**What's still valid:**
- Topic design concepts, node types, Power Fx explanations ✅
- All node types (Message, Question, Adaptive Card, Condition, Variable, Tool, etc.) ✅
- Power Fx filter expressions ✅
- Overview tab references ✅

**Action:** Screenshot verification only. Content appears current. Low effort update.

---

## Module 08: Enhance with Adaptive Cards ⚠️ Likely Current — Screenshots to Verify

**Last edited:** 2026-02-19
**Risk:** Low-Medium (same era as Modules 07, 09, 10 which appear current)

**What's still valid:**
- Adaptive Card Designer concept ✅
- Power Fx for data binding ✅
- Card schema structure ✅
- Topics tab navigation consistent with new UI ✅

**What still needs checking:**
- Screenshots — do they show the current UI?
- Adaptive Card JSON editor interface

**Action:** Screenshot verification. Content likely current (same edit date as 07, 09, 10).

---

## Module 09: Automate with Agent Flows ⚠️ Current + Add Workflows Callout

**Last edited:** 2026-02-19
**Risk:** Low-Medium

**Confirmed current in the source:**
- Lab 9.2.01: "Select Agents in left-hand side menu" ✅ (new UI)
- Lab 9.2.02: "Select the Topics tab" ✅
- Agent Flows lab steps appear to work with current designer ✅

**What needs adding (not a rewrite, just an addition):**
- **Callout box** explaining new Workflows experience (May 2026 public preview)
- "Agent Flows vs Workflows" comparison table (similar to the Agent Flows vs Power Automate table already in Module 09)
- Brief note: Workflows are in early release environments; standard envs use Agent Flows

**What's still valid:**
- All Agent Flows concepts, designer walkthrough, expressions ✅
- SharePoint connector, Outlook connector steps ✅
- Power Fx expression in topic node ✅

**Action:** Add "What's Coming: Workflows" callout section + comparison table. Light effort. Screenshots may need refresh.

---

## Module 10: Add Event Triggers ✅ Current — Screenshots to Verify

**Last edited:** 2026-02-19
**Risk:** Low

**Confirmed current in the source:**
- Lab 10.1.04: "Navigate to the Overview tab and locate the Triggers section" ✅
- Lab 10.1.05: "Click + Add trigger" ✅
- "Test Trigger" icon referenced ✅
- "Tools tab in your agent" navigation ✅
- No Frontier program requirement found in current module ✅ (may have been removed)

**What's still valid:**
- All event trigger concepts, SharePoint trigger, Power Automate cloud flow creation ✅
- Tool configuration (Outlook connector) ✅
- Authentication considerations section ✅

**What still needs checking:**
- Screenshots — do they show the current UI?
- Verify "Navigate to the Tools tab" nav path in new UI

**Action:** Screenshot verification only. Content appears fully current.

---

## Module 11: Publish Your Agent ⚠️ Mostly Current — Channel Nav Needs Check

**Last edited:** 2026-01-14
**Risk:** Low-Medium

**Confirmed current in the source:**
- Lab 11.1: "select the publish button at the top of the agent overview" ✅ (correct new UI)
- Publish popup confirmation ✅
- Notification after publishing ✅

**What may need updating:**
- Lab 11.2: "Select Channel in the top navigation of the agent" — in new UI, Channels is a SECTION on the Overview page, not a separate top-nav tab. Verify if a "Channels" tab still exists or if it redirects to Overview > Channels.
- Trial environment note: Currently says trial CANNOT publish (paid env required). Verify this is still true — some trial environments can publish after Authors role setup.

**What's still valid:**
- Teams and M365 Copilot channel setup steps ✅
- Admin approval flow ✅
- Availability options ✅

**Action:** Verify Channels navigation path. Update trial publishing note if needed. Low effort.

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

| Priority | Module | Effort | Notes |
|---|---|---|---|
| 1 (High) | 12 — Licensing | Medium | Significant changes: model retirement, Teams app retirement, new billing |
| 2 (Medium) | 02 — Fundamentals | Medium | Add Overview page walkthrough, update "Tools (Actions)" terminology, add Triggers building block |
| 3 (Medium) | 09 — Agent Flows | Low | Add Workflows callout + comparison table only |
| 4 (Medium) | 11 — Publish | Low | Verify Channels navigation path; trial publishing note |
| 5 (Low) | 06 — Custom Agent | Low | Screenshot check; content likely current |
| 6 (Low) | 07 — Topics | Low | Screenshot check; content appears current |
| 7 (Low) | 08 — Adaptive Cards | Low | Screenshot check; content likely current |
| 8 (Low) | 10 — Event Triggers | Low | Screenshot check; content appears current |
| 9 (Low) | 05 — Pre-Built Agents | Low | Template gallery may have changed |
| 10 (Low) | 04 — Solution | Low | Just updated 5 days ago |
| 11 (Low) | 03 — Declarative Agent | Low | Verify nav path |
| 12 (Low) | 01 — Introduction | Low | Add autonomous agent mention |
| 13 (Low) | 00 — Setup | Low | Screenshot check only |

## Revised Overall Assessment

The course is **in much better shape than initially feared.** Modules 07, 09, 10 were updated alongside the new UI launch (all last-edited 2026-02-19). They already reference the Overview page, Triggers section, Topics tab, and current navigation.

**Main work needed:**
1. Module 12: Licensing content has changed significantly (model changes, Teams retirement)
2. Module 02: Add Overview page visual/walkthrough for orientation
3. Module 09: Add Workflows callout (new capability participants will see in EA environments)
4. All modules: Screenshot audit (are the current screenshots showing correct UI?)
5. Module 11: Verify Channels navigation
