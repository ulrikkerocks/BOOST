# Facilitator Guide: Copilot Agent Academy — Recruit Course
### Updated for New Copilot Studio UI (June 2026)

**Workshop:** Copilot Agent Academy — Recruit  
**Source course:** https://microsoft.github.io/agent-academy/recruit/  
**GitHub:** https://github.com/microsoft/agent-academy  
**Delivery target:** 3 weeks from June 2026

---

## TL;DR — What Facilitators Need to Know

The core course content is in good shape. Modules 07, 09, 10, and 12 were all updated between January–March 2026 to align with the new Copilot Studio UI. The hands-on lab steps reference the correct UI elements.

**The three things to do before delivery:**
1. Add an Overview page orientation to Module 02 (new mental model intro)
2. Add a Workflows callout to Module 09 (new feature participants may see)
3. Screenshot audit — verify each module's screenshots match the June 2026 UI

---

## The Big UI Change: The Overview Page

Microsoft redesigned Copilot Studio in late 2025. The key shift:

**Old model:** Multiple tabs/sections (Topics, Actions, Settings, etc.) accessed via left sidebar navigation.  
**New model:** A single **Overview page** showing all agent components at once (scroll down to see everything).

### Overview Page Anatomy
When a participant opens an agent, they land on the Overview page. It contains:

| Section | What it is |
|---|---|
| **Details** | Agent name and description |
| **Instructions** | System prompt (up to 8,000 chars) — Edit button inline |
| **Triggers** | Event triggers (autonomous behavior) |
| **Knowledge** | Knowledge sources: SharePoint, websites, files, Dataverse, etc. |
| **Tools** | Actions: connectors, agent flows, workflows, MCP, APIs |
| **Connected Agents** | Multi-agent orchestration |
| **Topics** | Conversational topics and trigger phrases |
| **Channels** | Publishing targets (Teams, website, etc.) |
| **Suggested Prompts** | Starter prompts shown in Teams/M365 Copilot |

**Test pane** is always visible on the right.  
**Publish** button at top right.  
**Settings** (gear icon ⚙️) → language, solution, schema, advanced options.

### What This Means for Labs
The lab steps in the course already account for this. You'll see participants navigating to:
- "Overview tab" → this is the main Overview page ✅
- "Topics tab" → still accessible from agent navigation or from the Topics section on Overview ✅
- "Triggers section" → on the Overview page ✅
- "Tools tab" in agent → may route to Tools section on Overview ✅

---

## Navigation Reference: New UI

### Getting to an Agent
1. Go to https://copilotstudio.microsoft.com
2. Left sidebar: **Agents** → click your agent
3. You land on the **Overview page**

### Left Sidebar (global)
- **Home** — natural language creation entry
- **Agents** — list of all agents
- **Flows** — Agent Flows (separate from the agent overview)
- **Workflows** — New experience (only in early-release environments)
- **Connections** — manage connector auth
- **Settings** — environment-level settings

### Within an Agent
The agent-level navigation has changed. There is now an "Overview" tab that is the primary view. The following sub-pages exist:
- **Overview** ← this is where everything lives
- **Topics** (also accessible from Overview > Topics section)
- **Analytics**
- **Activity**
- **Settings** (agent-level, different from environment settings)

---

## Module-by-Module Facilitator Notes

### Module 00: Course Setup ✅ Run As-Is

**Status:** Current (last edited March 2026)

**Facilitator notes:**
- Step 2 (Copilot Studio trial): URL aka.ms/TryCopilotStudio still works
- Step 4 (Enable publishing): The Authors role setup in PPAC is required. In trial environments, publishing now requires explicit authorization. Guide participants through PPAC setup carefully — this is a common failure point.
- Verify screenshots before the workshop; the PPAC interface may have minor changes.

**Timing:** 30 min (or give as pre-work before the day)

---

### Module 01: Introduction to Agents ✅ Run As-Is

**Status:** Stable conceptual content

**Facilitator additions to make verbally:**
- Mention that Copilot Studio now has **three types of agents**:
  1. Declarative agents (extend M365 Copilot — covered in Module 03)
  2. Custom conversational agents (the main focus of this course)
  3. Autonomous/event-driven agents (introduced in Module 10)
- The course focuses on types 1 and 2, with a taste of type 3.

---

### Module 02: Copilot Studio Fundamentals ⚠️ ADD Overview Page Orientation

**Status:** Good conceptual content, but needs an Overview page visual orientation added.

**Gap:** The module teaches the four building blocks conceptually but doesn't show participants WHERE these live in the new UI.

**Add before starting labs (verbally or via slide):**

> "Before we build, let me show you the Overview page — this is where you'll spend most of your time in Copilot Studio. Every agent has one. It shows all four building blocks we just discussed on a single scrollable page..."

Then walk through the Overview page anatomy (see "Overview Page Anatomy" section above).

**Terminology note:** The course says "Tools (Actions)" — in the new UI, this is just called **"Tools"**. The concept is the same.

**Addition needed:** See `workshop/02-copilot-studio-fundamentals/overview-page-orientation.md` for ready-to-use content.

**Timing:** 30 min + 5 min for Overview page orientation demo

---

### Module 03: Create a Declarative Agent for M365 Copilot ⚠️ Verify Before Workshop

**Status:** Updated 2 weeks ago (June 2026)

**Verify:**
- Navigation path to create a declarative agent vs. a custom agent
- The distinction still exists but the entry point on the Home page may label it differently

---

### Module 04: Creating a Solution ✅ Run As-Is

**Status:** Updated 5 days before this guide was written (June 11, 2026 — most recent update in the course)

**Facilitator notes:**
- Solution creation steps should be current
- Preferred solution setting: Settings > Advanced (verify this location in current UI)

---

### Module 05: Using Pre-Built Agents ✅ Run As-Is (with note)

**Facilitator note:** Template gallery has been updated with new templates. The specific template used in the lab may look different or have been updated. The concept is the same — browse and customize a starting template.

---

### Module 06: Build a Custom Agent ✅ Run As-Is

**Status:** Updated February 2026; references new UI Overview page elements.

**Key lab steps to watch:**
- Natural language creation on the Home page → AI provisions agent
- AI suggestions (name, description, knowledge, topics) appear after provisioning
- "wheel cog" → is now a gear ⚙️ icon for Settings

**If participants see a different suggestions UI:**
- The suggestions pane has evolved; if dismissed, it's gone (not re-creatable in same session)
- Main sections (Details, Knowledge) are still there on the Overview page

---

### Module 07: Add a Topic with Triggers ✅ Run As-Is

**Status:** Updated February 2026; lab steps reference new UI.

**Key navigation:**
- "Select the Topics tab near the name of the agent" ✅ (this still works)
- "+ Add a topic" → From blank ✅
- "Select the Overview tab and select Edit" (for Instructions) ✅

**Power Fx filter expression:**
```
Concatenate("Status eq 'Available' and AssetType eq '", Topic.VarDeviceType, "'")
```
This SharePoint OData filter is still valid. ✅

**Timing:** 60 min

---

### Module 08: Enhance with Adaptive Cards ✅ Run As-Is

**Status:** Updated February 2026.

**Facilitator notes:**
- Adaptive Card JSON editor is in the topic node
- Power Fx for data binding is unchanged
- Most time-consuming lab — allocate buffer time

**Timing:** Typically 60-90 min (more than the listed 30 min if participants are new to JSON)

---

### Module 09: Automate with Agent Flows ⚠️ ADD Workflows Callout

**Status:** Updated February 2026; Agent Flows steps are current.

**New thing to explain:** Since May 2026, there is a new "Workflows" experience in early-release environments. Standard environments still use Agent Flows. The lab uses Agent Flows throughout.

**Where to add it:** Before the lab starts, mention:

> "Since this course was written, Microsoft released a new experience called **Workflows** (currently in preview/early release). If you ever see a 'Workflows' option in the left sidebar, that's the new experience. For today, we'll use **Agent Flows** which is GA and available in all environments. The concepts are the same — the designer looks different."

**Full callout block:** See `workshop/09-add-an-agent-flow/workflows-callout.md`

**Agent Flows navigation:**
- In the topic: "+ icon" → "Add a tool" → "New Agent flow" ✅
- Agent Flows designer loads in a new view ✅
- After publishing: add to topic via "Add a tool" ✅

**Timing:** 30 min

---

### Module 10: Add Event Triggers ✅ Run As-Is

**Status:** Updated February 2026; all navigation references current UI.

**Key navigation:**
- "Navigate to the Overview tab and locate the Triggers section" ✅
- "+ Add trigger" → search for SharePoint trigger ✅
- "Test Trigger" icon on the trigger card ✅
- "Tools tab in your agent" → add Outlook connector ✅

**Facilitator notes:**
- Generative AI must be enabled (Settings > Orchestration). If already enabled by default, step 1 is a verify step.
- The Power Automate cloud flow created automatically — participants won't see it explicitly; it happens behind the scenes.
- "Test trigger" panel can take a few minutes to show the event.

**Timing:** 45 min

---

### Module 11: Publish Your Agent ⚠️ Verify Channels Navigation

**Status:** Updated January 2026.

**Verify before workshop:**
- Step 11.2 says "Select Channel in the top navigation of the agent." In the new UI, Channels is a **section on the Overview page**, not a separate top-nav tab. The course screenshot is `channels-tab.png`. Check if there's still a "Channels" tab in agent navigation or if it redirects to Overview.
- If it's now a section on Overview, update verbal instructions accordingly: "Scroll down on the Overview page to the Channels section."

**Trial environment note (important):**
Module 11 says: "There was a recent change to Copilot Studio Trial environments that prohibits the publishing of agents." This means:
- **Participants with trial environments cannot complete Module 11** unless the Authors role is set up AND they have the right env type.
- **Solution for the workshop:** Set this up in Module 00 (PPAC Authors role step). Or treat Module 11 as a demo/walkthrough rather than hands-on for trial users.

**Timing:** 30 min

---

### Module 12: Understanding Licensing ✅ Run As-Is

**Status:** Updated March 2026; covers Copilot Credits model (replaced "messages" Sept 2025).

**Key current facts (verify before each delivery):**
- Currency: **Copilot Credits** (not messages)
- Cost: $0.01/credit pay-as-you-go OR $200/month for 25,000 credits/pack
- M365 Copilot-licensed users interacting via internal channels: **no credits consumed** (fair use applies)
- Default AI model: GPT-4.1 (GPT-4o retired Oct 2025)
- New model options: GPT-5, Claude Sonnet 4.5/4.6, Mistral Medium 3.5 — each has different credit implications (premium AI tools rate applies to reasoning models)

**Add verbally:**
- "Since this module was written, Microsoft retired the Teams classic chatbot creation app (June 2026). You now create and manage Teams agents entirely from the Copilot Studio web interface."

**Timing:** 15 min

---

## Common Issues & Troubleshooting

### "I don't see the Overview page / my UI looks different"
The Overview page is the new standard. If someone sees an older UI, they may be in a different environment or accessing via an older direct URL. Have them navigate to https://copilotstudio.microsoft.com and sign in fresh.

### "Where is the Channels tab?"
In the new UI, Channels is a section on the Overview page. Scroll down on the Overview page to find it.

### "I can't publish my agent"
Two possible causes:
1. Trial environment without Authors role setup (fix: Module 00 PPAC step)
2. Publishing requires a paid environment

### "I see 'Workflows' in the sidebar but the lab says 'Agent Flows'"
This means you're in an early-release environment. For this workshop, use Agent Flows. Workflows is a preview feature.

### "The AI suggestions disappeared"
When creating an agent via natural language, AI suggests components. These suggestions are session-only — if dismissed, they won't reappear. Guide participants to add the components manually via the Overview page sections.

### "The SharePoint connector says I need to allow permissions"
This is expected — participants must select "Allow" when the agent first tries to use their credentials for a connector action. This is a one-time per-connection consent.

---

## Suggested Schedule (Full Day Workshop)

| Time | Module | Notes |
|---|---|---|
| 09:00–09:15 | Welcome + logistics | |
| 09:15–09:45 | Module 01: Introduction to Agents | Conceptual, keep pace |
| 09:45–10:15 | Module 02: Fundamentals + Overview page demo | **Add Overview page orientation** |
| 10:15–10:30 | Break | |
| 10:30–11:00 | Module 03: Declarative Agent | |
| 11:00–11:30 | Module 04: Creating a Solution | |
| 11:30–12:00 | Module 06: Build a Custom Agent (setup) | Module 05 optional |
| 12:00–13:00 | Lunch | |
| 13:00–13:45 | Module 06: Build a Custom Agent (labs) | |
| 13:45–14:45 | Module 07: Add a Topic | Allow extra time |
| 14:45–15:00 | Break | |
| 15:00–16:00 | Module 08: Adaptive Cards | May run over |
| 16:00–16:30 | Module 09: Agent Flows + Workflows intro | **Add Workflows callout** |
| 16:30–17:00 | Module 10: Event Triggers | |
| 17:00–17:15 | Module 11: Publish (demo) | Demo if trial limitations |
| 17:15–17:30 | Module 12: Licensing | |
| 17:30–17:45 | Badge + wrap up | |

---

## Pre-Workshop Checklist

- [ ] Confirm all participants have M365 tenant access
- [ ] Verify Copilot Studio trial signup (aka.ms/TryCopilotStudio) still works
- [ ] Walk through Module 00 yourself — verify all steps
- [ ] Set up the PPAC Authors role in your demo tenant
- [ ] Verify SharePoint IT Help Desk template still exists
- [ ] Add Overview page orientation slide/demo to your Module 02 materials
- [ ] Test Module 06 lab end-to-end in your own environment
- [ ] Verify Module 11 Channels navigation
- [ ] Prepare Workflows callout talking points for Module 09
- [ ] Check module screenshots against current UI (screenshot audit checklist)

---

## Resources

| Resource | URL |
|---|---|
| Course site | https://microsoft.github.io/agent-academy/recruit/ |
| Course GitHub | https://github.com/microsoft/agent-academy |
| Copilot Studio | https://copilotstudio.microsoft.com |
| What's New | https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new |
| Licensing docs | https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing |
| Trial signup | https://aka.ms/TryCopilotStudio |
| Usage Estimator | https://aka.ms/copilotstudioestimator |
| M365 Dev tenant | https://developer.microsoft.com/microsoft-365/dev-program |
