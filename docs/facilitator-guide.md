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

### Module 06: Build a Custom Agent

**Last edited:** Current  
**Risk:** Low

**Facilitator notes:**
- **This is the heart of the course** — participants build the foundation agent used in all remaining modules
- **Timing guidance:** Allow 75 minutes. Natural language creation is fast (~5 min), but configuring knowledge sources and testing thoroughly takes time
- **Common pitfall:** SharePoint site permissions. If the agent can't access the Contoso IT site, participants need to verify:
  - The SharePoint site was created in Module 00
  - The site is in the same tenant as the Copilot Studio environment
  - The user has access to the site (Owner or Member role)
- **Setup requirements:** Verify before starting:
  - Module 00 completed (SharePoint site + Devices list created)
  - Guest WiFi document uploaded to Documents library
  - Preferred solution set to "Contoso Helpdesk Agent" solution
- **Troubleshooting:**
  - **AI suggestions dismissed:** If participants accidentally dismiss the AI suggestions pane after agent creation, they can't get it back. Not a problem — they can still add knowledge/topics manually via Overview page sections
  - **Knowledge source not working:** Test each source individually. SharePoint indexing can take 2-3 minutes. General web search should work immediately
  - **Agent gives generic answers:** Check that knowledge sources show "Ready" status in the Knowledge section
- **Testing checkpoint:** Have participants test at least one question from each knowledge source before moving on:
  - SharePoint: "What devices are available?"
  - Uploaded doc: "How do I connect to guest WiFi?"
  - Microsoft Support: "How do I reset my password?"
  - General web: "What's new with Windows 11?"

**Status:** Updated February 2026; references new UI Overview page elements. ✅ Current

---

### Module 07: Add a Topic with Triggers

**Last edited:** Current  
**Risk:** Medium

**Facilitator notes:**
- **Timing guidance:** Allow 60 minutes. Topic creation is visual and intuitive, but Power Fx expressions can slow down participants unfamiliar with formulas
- **Common pitfall #1:** Power Fx filter syntax errors. The OData filter string must be perfectly formatted:
  ```
  Concatenate("Status eq 'Available' and AssetType eq '", Topic.VarDeviceType, "'")
  ```
  Watch for: missing quotes, wrong quote types, extra spaces, incorrect field names
- **Common pitfall #2:** SharePoint connector authentication. First-time use requires signing in. If the connector shows "Not connected," participants must:
  1. Click the connector card
  2. Select "Sign in"
  3. Authenticate with their M365 account
- **Setup requirements:** Module 06 completed with Contoso Helpdesk Agent functional
- **Troubleshooting:**
  - **No devices returned:** Check the SharePoint Devices list has records with Status="Available" and AssetType matching what user typed (e.g., "Laptop" not "laptop" if case-sensitive)
  - **Connector error:** Verify SharePoint connector is added to the solution and authenticated
  - **Topic doesn't trigger:** Verify trigger phrases include variations like "I need a laptop," "request device," "show me laptops"
- **Teaching moment:** This is the first structured topic. Emphasize the difference between generative responses (Module 06) and predictable flows (Module 07). Use the table from the module README to illustrate when to use each

**Status:** Updated February 2026; lab steps reference new UI. ✅ Current

---

### Module 08: Enhance with Adaptive Cards

**Last edited:** Current  
**Risk:** Medium-High

**Facilitator notes:**
- **Timing guidance:** Allow **60-90 minutes** (not the 45 min listed in the module). This is consistently the longest lab for participants new to JSON or Power Fx data binding
- **Common pitfall:** JSON syntax errors. Even one missing comma or bracket breaks the card. Recommend participants use the built-in Adaptive Card Designer visual editor if available, or copy/paste the provided JSON exactly
- **Setup requirements:** Module 07 completed with working Device Request topic
- **Troubleshooting:**
  - **Card doesn't render:** Check JSON syntax in an online validator (adaptivecards.io/designer)
  - **Data doesn't appear:** Verify Power Fx binding syntax: `${Topic.AvailableDevices.DeviceTitle}` — case-sensitive, must match variable names exactly
  - **Image not showing:** Image URLs must be publicly accessible. If using SharePoint images, ensure guest access is enabled or use sample URLs
  - **"Request" button doesn't work:** Verify the button `onCardAction` is mapped to the correct topic variable to capture the selection
- **Teaching moment:** Show a before/after comparison (plain text list vs. Adaptive Card) to illustrate the value of rich UI
- **Buffer time:** If the workshop is running behind, consider showing a completed Adaptive Card demo and letting participants implement it as homework

**Status:** Updated February 2026. ✅ Current

---

### Module 09: Automate with Agent Flows ⚠️ ADD Workflows Callout

**Last edited:** Current  
**Risk:** Low

**Facilitator notes:**
- **NEW (June 2026):** Explain the difference between Agent Flows (GA) and Workflows (preview) before starting the lab. See `workshop/09-add-an-agent-flow/workflows-callout.md` for ready content
- **Timing guidance:** Allow 50 minutes. Flow creation is straightforward, but connector authentication and testing add time
- **Common pitfall:** Outlook connector permissions. Sending email requires delegated permissions. First-time use triggers a consent prompt. If participants see "Forbidden" or "Unauthorized":
  1. Check the Outlook connector shows "Connected" status
  2. Re-authenticate via Connections page
  3. Verify the user has permission to send email from their mailbox
- **Setup requirements:** Module 08 completed with Adaptive Card topic working
- **Troubleshooting:**
  - **Flow doesn't trigger:** Verify the flow is published and added to the topic as a tool node (not just created)
  - **Email not received:** Check spam/junk folder. Check flow run history for errors
  - **Input parameters not passing:** Verify parameter names match exactly between the topic variable and the flow input (case-sensitive)
- **Teaching moment:** After the flow works, ask participants: "What else could we automate?" (e.g., create a Planner task, log to Dataverse, post to Teams channel)
- **If participants see "Workflows" in the sidebar:** Reassure them both experiences work. For consistency with the lab, guide them to use **Flows** → **New Agent flow**

**Status:** Updated February 2026; Agent Flows steps are current. ✅ Current

---

### Module 10: Add Event Triggers

**Last edited:** Current  
**Risk:** Medium

**Facilitator notes:**
- **Timing guidance:** Allow 45 minutes (30 min listed in module is tight). Event trigger testing requires waiting for events to fire, which adds buffer time
- **Common pitfall:** Dataverse table doesn't exist. Participants must create a Support Tickets table in Power Apps first (or use the provided SharePoint list alternative). If using Dataverse:
  - Verify the table exists in the same environment as the agent
  - Verify the table has the required columns: Title, Priority, Description, RequestedBy
- **Setup requirements:** Module 09 completed with working Agent Flow
- **Troubleshooting:**
  - **Trigger doesn't fire:** 
    1. Verify the trigger is published (triggers don't work in draft mode)
    2. Check the trigger condition filter is correct (e.g., Priority = "High")
    3. Create a test record in the Dataverse table that meets the condition
    4. Wait 2-3 minutes for the background flow to poll
  - **"Generative AI not enabled" error:** Go to Settings > Orchestration > Enable generative AI orchestration
  - **Email not sent:** Verify the Outlook connector is still authenticated (check Connections page)
- **Teaching moment:** Explain the difference between conversational (user-initiated) and autonomous (event-driven) agents. This is a preview of advanced agent capabilities
- **Demo strategy:** If time is short, demonstrate the trigger working with a live test record rather than having each participant create their own Dataverse table

**Status:** Updated February 2026; all navigation references current UI. ✅ Current

---

### Module 11: Publish Your Agent ⚠️ Verify Channels Navigation

**Last edited:** Current  
**Risk:** Low

**Facilitator notes:**
- **Timing guidance:** Allow 30 minutes. Publishing is fast, but Teams app installation and testing add time
- **Common pitfall:** Copilot Studio Authors role not assigned. If the Publish button is grayed out:
  1. Go to Power Platform Admin Center (admin.powerplatform.microsoft.com)
  2. Select the environment
  3. Settings > Users + permissions > Security roles
  4. Assign "Copilot Studio Authors" role to the user
  5. Wait 5 minutes, then refresh Copilot Studio
- **Setup requirements:** Modules 06-10 completed with fully functional agent
- **Troubleshooting:**
  - **Publish fails:** Check for error indicators (red exclamation marks) in topics or flows. Fix errors before publishing
  - **Teams channel not available:** Verify Microsoft Teams integration is enabled in the environment (Settings > Features)
  - **Agent doesn't appear in Teams:** After publishing to Teams, participants must:
    1. Go to the Channels section (via +8 overflow menu)
    2. Select Teams channel
    3. Copy the app install link or download the app package
    4. In Teams: Apps > Manage your apps > Upload an app > Upload the .zip file
  - **Agent gives old responses in Teams:** Remind participants that published version ≠ draft. They need to publish again after making changes
- **Teaching moment:** Show the difference between Test pane (draft) and Teams (published). Make a change, don't publish, and show that Teams still has the old version
- **Demo website:** Show participants the demo website link (available after publishing) for quick testing without Teams installation

**Status:** Updated January 2026.

**✅ VERIFIED 2026-06-16 (live UI audit):**
Channels is accessible via the **"+8" overflow menu in the top navigation**. It is NOT a section on the Overview page scrollable canvas. Participants must:
1. Open their agent → Overview page
2. Click **+8** in the top tab bar (next to "Overview")
3. Select **Channels** from the dropdown

Once selected, Channels becomes the active tab. The page shows: Published agent status, Share a preview (Demo website), Microsoft channels (M365+Teams, SharePoint, Teams Phone Agent), Other channels (Web app, Native app, etc.), and Customer engagement hub options.

The course instruction "Select Channel in the top navigation" is essentially correct — add the verbal note: **"Click +8 in the top navigation, then choose Channels."**

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

### Module 13: Securing Your Recruit Badge

**Last edited:** Current  
**Risk:** Low

**Facilitator notes:**
- **This is the wrap-up module** — use it to celebrate completion and set expectations for next steps
- **Timing guidance:** Allow 15 minutes. This is a checklist review + badge claim + community resources
- **Common pitfall:** None — this is a celebration module, not a technical lab
- **Setup requirements:** All prior modules completed
- **Facilitator actions:**
  1. Walk through the completion checklist as a group — use it as a retrospective
  2. Share the badge claim link (if available) or explain the post-workshop process
  3. Highlight 2-3 community resources participants should bookmark
  4. Ask: "What will you build next?" — invite participants to share their agent ideas
  5. Mention the Special Ops advanced course (if offering it) or other learning paths
- **Teaching moment:** Emphasize the journey doesn't end here. Point to:
  - Microsoft Learn modules for deeper dives
  - Copilot Studio Community forums for peer support
  - Power Platform User Groups for local meetups
  - GitHub Copilot Studio samples repo for inspiration
- **Badge claim process (adjust to your workshop delivery model):**
  - If badging platform: provide claim link + completion code
  - If certificate: share template or email certificate after event
  - If internal tracking: explain how completion will be recorded
- **Feedback collection:** Use this module to distribute post-workshop survey or feedback form

**Status:** Current. ✅

**Timing:** 15 min (can extend to 30 if doing group retrospective or Q&A)

---

## Common Issues & Troubleshooting

### "I don't see the Overview page / my UI looks different"
The Overview page is the new standard. If someone sees an older UI, they may be in a different environment or accessing via an older direct URL. Have them navigate to https://copilotstudio.microsoft.com and sign in fresh.

### "Where is the Channels tab?"
Channels is in the top navigation but hidden under the **+8 overflow menu**. From the agent Overview page, click **+8** (top right of the tab bar, next to "Overview") and select **Channels**. It is NOT a section on the Overview scrollable canvas — it opens as its own dedicated page.

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
- [x] Verify Module 11 Channels navigation ✅ confirmed: click +8 → Channels
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
