# Screenshot Capture Plan

**Purpose:** The rewritten course modules contain **193 `[SCREENSHOT: …]` placeholders** and **zero captured images**. This is the worklist for capturing them. It groups the work by *where* each screenshot is taken (so you log into each surface once) and tracks progress per module.

> **How this differs from [screenshot-audit-checklist.md](screenshot-audit-checklist.md):** the audit checklist was written to *verify the original Microsoft course's* screenshots against the new UI. This plan is the *capture worklist for this rewrite's* placeholders. Once capture is done, the audit checklist becomes the final QA pass.

---

## Prerequisite: you have to build the agent first

These screenshots can't be captured cold. The course is a progressive build of the **Contoso Helpdesk Agent**, and most screenshots show that agent in a specific state. To capture them you need:

- A live M365 tenant + Copilot Studio trial (Module 00)
- The Contoso IT SharePoint site, **Devices** list with sample data, and Guest WiFi doc (Module 00)
- The agent built up through each module's steps

**The efficient path:** actually run the course end-to-end on a clean tenant, capturing as you go. The agent state at each step *is* the screenshot. Budget this as a guided build session, not a separate "screenshot day."

---

## Scope at a glance

**193 screenshots across 14 modules.** By capture surface:

| Capture surface | ~Count | Where | Notes |
|---|---:|---|---|
| **Copilot Studio** (authoring, topic designer, agent flows, channels, analytics) | ~140 | Modules 02–12 | The dominant bucket — one long build session covers most |
| **Power Apps maker / Dataverse** | ~19 | 04, 06, 10, 13 | Solutions, publisher, the Support Ticket table |
| **Microsoft Teams** | ~8 | 11 | Upload custom app + chat with the published agent |
| **SharePoint** | ~6 | 00 | Site, Devices list, document library |
| **PPAC (Power Platform Admin Center)** | ~4 | 00, 04, 12 | Environments, security roles, trial |
| **Microsoft 365 Admin Center** | ~3 | 00, 12 | Security groups, purchase options |
| **M365 Copilot (chat)** | ~3 | 03 | Declarative agent @mention + response |
| **Outlook inbox** | ~2 | 09, 10 | Received automation email |
| **M365 trial signup** | ~1 | 00 | |
| **Word** | ~1 | 00 | Guest WiFi guide doc |
| **Microsoft Learn** | ~1 | 13 | Badge on profile |
| **Downloaded file / desktop** | ~1 | 11 | Teams app .zip |
| **Diagrams — NOT screenshots** | 3 | 01 | Create with Mermaid / a diagram tool, don't capture |

Per-module exact counts:

| Module | Count | Module | Count |
|---|---:|---|---:|
| 00 Course Setup | 15 | 07 Topics & Triggers | 30 |
| 01 Introduction *(diagrams)* | 3 | 08 Adaptive Cards | 16 |
| 02 Fundamentals | 6 | 09 Agent Flows | 18 |
| 03 Declarative Agent | 8 | 10 Event Triggers | 23 |
| 04 Solution | 10 | 11 Publish | 26 |
| 05 Pre-built Agents | 8 | 12 Licensing | 3 |
| 06 Custom Agent | 24 | 13 Badge | 3 |

---

## Suggested capture order

1. **Module 00 satellite surfaces first** — M365 signup, PPAC, M365 Admin, SharePoint, Word. These set up the environment the rest depends on.
2. **One Copilot Studio build session, Modules 02 → 11 in order** — this is ~140 of the 193. Build the agent step by step; capture each screen as you reach it. Modules 06–08 (knowledge → topic → Adaptive Card) and the topic-designer shots in 07/09/10 must be done in sequence because each builds on the last.
3. **Power Apps / Dataverse** — Module 04 (solution) and Module 10 (Support Ticket table) interleave with the CS session.
4. **Teams + Outlook + Learn** — Module 11 (publish to Teams, chat) and the automation emails (09, 10) come last, after the agent is published.
5. **Module 01 diagrams** — produce separately (see below).

---

## Conventions

**Storage:** `docs/assets/screenshots/<module-number>/` — e.g. `docs/assets/screenshots/06/`. Must live under `docs/` so Jekyll publishes them. (`docs/assets/` is not excluded in `_config.yml`.)

**Naming:** `NN_descriptive-name.png`, numbered in the order they appear in the module — e.g. `06/03_ai-suggestions-panel.png`. (The audit checklist's `XX.Y_NN_Name.png` scheme mirrors the *original* course's filenames; for new captures the simpler per-module form is enough.)

**Wiring into the module:** replace each placeholder line, e.g.

```markdown
[SCREENSHOT: AI suggestions panel showing agent name, knowledge sources, and suggested topics]
```

with a Jekyll-safe image reference (works with the `/BOOST` baseurl):

```markdown
![AI suggestions panel showing agent name, knowledge sources, and suggested topics]({{ '/assets/screenshots/06/03_ai-suggestions-panel.png' | relative_url }})
```

Keep the placeholder text as the alt text — it's already descriptive and accessible.

**Redaction:** scrub real tenant names, emails, and GUIDs before publishing. Use the Contoso naming the course assumes.

---

## Module 01 — diagrams, not screenshots

These three are conceptual and should be authored (Mermaid renders natively on GitHub Pages), not captured from a UI:

- [ ] `01` L61 — LLM at the center of an agent architecture (inputs: user message, context → outputs: response, tool calls)
- [ ] `01` L93 — Sequence diagram: User → Agent → Knowledge → LLM → Tool/API → Response *(already described as Mermaid in the source — convert to a real ` ```mermaid ` block)*
- [ ] `01` L197 — Orchestrator agent connected to Flight / Hotel / Payment agents

---

## Worklist by module

Line numbers point to the placeholder in each module's `README.md`.

### Module 00 — Course Setup (15)
- [ ] L60 — M365 trial signup ("Try for free") *(M365 signup)*
- [ ] L79 — Copilot Studio trial activation page *(Copilot Studio)*
- [ ] L84 — Copilot Studio Home, description box *(Copilot Studio)*
- [ ] L103 — Power Apps Developer Plan signup *(Power Apps)*
- [ ] L116 — PPAC Environments list *(PPAC)*
- [ ] L137 — M365 Admin Center, security groups *(M365 Admin)*
- [ ] L156 — Security group members flow *(M365 Admin)*
- [ ] L172 — PPAC → Security roles → Copilot Studio Authors *(PPAC)*
- [ ] L198 — SharePoint home, "Create site" *(SharePoint)*
- [ ] L208 — SharePoint site creation wizard *(SharePoint)*
- [ ] L220 — SharePoint "+ New" → List *(SharePoint)*
- [ ] L249 — Add Choice column (Category) *(SharePoint)*
- [ ] L280 — Devices list with sample items *(SharePoint)*
- [ ] L342 — Guest WiFi guide Word doc *(Word)*
- [ ] L352 — SharePoint Documents library with guide uploaded *(SharePoint)*

### Module 01 — Introduction (3) — see "diagrams" section above

### Module 02 — Fundamentals (6)
- [ ] L44 — Full Overview page (Details → Suggested Prompts + Test pane)
- [ ] L118 — Test pane conversation, "New test session" icon
- [ ] L157 — Knowledge section (SharePoint + doc + web search toggle)
- [ ] L201 — Tools section ("+ Add", Work IQ toggle)
- [ ] L243 — Topic designer: Trigger → Question → Condition → Message
- [ ] L282 — Instructions section with Edit button

### Module 03 — Declarative Agent (8)
- [ ] L71 — Copilot Studio Home, description box *(Copilot Studio)*
- [ ] L91 — Declarative agent creation dialog *(Copilot Studio)*
- [ ] L115 — Instructions field *(Copilot Studio)*
- [ ] L132 — Add knowledge source (SharePoint URL) *(Copilot Studio)*
- [ ] L146 — Publish confirmation *(Copilot Studio)*
- [ ] L161 — M365 Copilot chat input *(M365 Copilot)*
- [ ] L169 — M365 Copilot @mention dropdown *(M365 Copilot)*
- [ ] L186 — M365 Copilot response with citation *(M365 Copilot)*

### Module 04 — Solution (10)
- [ ] L82 — PPAC home *(PPAC)*
- [ ] L105 — Power Apps maker, Solutions *(Power Apps)*
- [ ] L113 — Solutions, "New Publisher" *(Power Apps)*
- [ ] L129 — New Publisher dialog (Contoso) *(Power Apps)*
- [ ] L143 — "+ New solution" *(Power Apps)*
- [ ] L155 — New solution dialog *(Power Apps)*
- [ ] L170 — Solution details, empty Objects *(Power Apps)*
- [ ] L195 — Copilot Studio Settings → Advanced/Environment *(Copilot Studio)*
- [ ] L203 — Preferred solution dropdown *(Copilot Studio)*
- [ ] L232 — Solution Objects with agent components *(Power Apps)*

### Module 05 — Pre-built Agents (8)
- [ ] L73 — Home, "Start from a template"
- [ ] L85 — IT Help Desk template preview
- [ ] L115 — Template preview, "Create agent"
- [ ] L129 — Overview page for template-created agent
- [ ] L173 — Topics list (Password Reset, Device Request, Software Install)
- [ ] L182 — Password Reset topic flow
- [ ] L219 — Add knowledge (SharePoint URL)
- [ ] L239 — Test pane: WiFi password + citation

### Module 06 — Custom Agent (24)
- [ ] L60 — Home, description box
- [ ] L75 — Home with IT helpdesk description entered
- [ ] L91 — AI suggestions panel
- [ ] L118 — Final agent creation screen
- [ ] L124 — Overview page (Details, Instructions, Knowledge, Test)
- [ ] L140 — Instructions section, Edit
- [ ] L200 — Instructions editor (full text)
- [ ] L234 — Knowledge section, "+ Add knowledge"
- [ ] L244 — Add SharePoint knowledge dialog
- [ ] L252 — Knowledge: SharePoint connected (green check)
- [ ] L268 — Upload files dialog
- [ ] L276 — Knowledge: SharePoint + WiFi doc
- [ ] L290 — Add website knowledge (Microsoft Support URL)
- [ ] L308 — Knowledge: "General web search" enabled
- [ ] L352 — Test pane: Dell laptops + citation
- [ ] L370 — Test pane: WiFi password + doc citation
- [ ] L388 — Test pane: password reset + Support citation
- [ ] L406 — Test pane: Windows 11 news + web citations
- [ ] L445 — Activity map: knowledge sources searched
- [ ] L485 — Model dropdown, GPT-4.1 selected
- [ ] L519 — Test pane: GPT-4.1 vs GPT-5 comparison
- [ ] L534 — Settings dropdown, "Agent settings"
- [ ] L569 — Solutions list with the agent solution *(Power Apps)*
- [ ] L578 — Solution showing agent under Objects *(Power Apps)*

### Module 07 — Topics & Triggers (30)
- [ ] L65 — Overview Topics section, "See all"
- [ ] L69 — Topics list (system + suggested)
- [ ] L76 — New topic, "From blank"
- [ ] L80 — Topic designer blank canvas
- [ ] L87 — Topic name "Device Request"
- [ ] L100 — Trigger node, "+ Add phrases"
- [ ] L114 — Trigger phrases list (8)
- [ ] L136 — Add node menu, "Ask a question"
- [ ] L140 — Question node on canvas
- [ ] L150 — Question node with text
- [ ] L164 — Question node, multiple-choice options
- [ ] L175 — Question node, "Save response as: DeviceType"
- [ ] L196 — Add node → "Set a variable value"
- [ ] L200 — Set variable node on canvas
- [ ] L209 — Set variable "AvailableDevices"
- [ ] L218 — Set variable Value field, fx icon
- [ ] L235 — Power Fx editor: Filter expression
- [ ] L270 — Add node → "Add a condition"
- [ ] L274 — Condition node, two branches
- [ ] L289 — Condition node, CountRows formula
- [ ] L300 — True branch → "Send a message"
- [ ] L319 — Message node, dynamic table (AvailableDevices)
- [ ] L339 — False branch add-node menu
- [ ] L346 — False branch "no devices" message
- [ ] L362 — Topic designer Save
- [ ] L371 — Test pane next to designer
- [ ] L389 — Test pane: multiple-choice buttons
- [ ] L398 — Test pane: available laptops list
- [ ] L418 — Test pane: "no devices" message
- [ ] L442 — Instructions editor, "When to use topics"

### Module 08 — Adaptive Cards (16)
- [ ] L56 — Example Adaptive Card (device, specs, Request button)
- [ ] L71 — Topics list, Device Request highlighted
- [ ] L84 — Topic flow, Condition node True/False
- [ ] L91 — Message node on True branch, Delete icon
- [ ] L102 — Message node menu, "Adaptive Card"
- [ ] L106 — Adaptive Card editor, blank/default
- [ ] L143 — Adaptive Card designer toolbar
- [ ] L154 — Adaptive Card editor, Code/JSON toggle
- [ ] L228 — Adaptive Card code editor (JSON template)
- [ ] L253 — Adaptive Card node, "Data source" field
- [ ] L263 — Data source: "Topic.AvailableDevices"
- [ ] L288 — Adaptive Card preview, populated
- [ ] L308 — Message node, acknowledgment text
- [ ] L326 — Topic designer toolbar, Save
- [ ] L349 — Test pane: populated card (Dell Latitude 7430)
- [ ] L367 — Test pane: "no devices" for empty category

### Module 09 — Agent Flows (18)
- [ ] L87 — Topic designer, Device Request flow
- [ ] L102 — Add node, "Call a tool"
- [ ] L106 — Tool node on canvas
- [ ] L113 — Tool node, "Create a flow"
- [ ] L117 — Agent Flow designer, blank canvas
- [ ] L128 — Flow trigger "When Copilot Studio calls a flow"
- [ ] L139 — Trigger node, DeviceTitle input
- [ ] L154 — Action search, Outlook "Send an email (V2)"
- [ ] L158 — Send an email action on canvas
- [ ] L188 — Send email with dynamic content
- [ ] L201 — Flow name "Send Device Request Email"
- [ ] L221 — Tool node, flow selected
- [ ] L247 — Tool node, fields with Power Fx
- [ ] L277 — Topic designer Save
- [ ] L300 — Test pane: card with "Request this device"
- [ ] L311 — Test pane: confirmation after click
- [ ] L320 — Outlook inbox: device request email *(Outlook)*
- [ ] L347 — Flow run history, successful runs

### Module 10 — Event Triggers (23)
- [ ] L75 — Power Apps maker home *(Power Apps)*
- [ ] L83 — Tables, "+ New table" *(Power Apps)*
- [ ] L91 — New table dialog (Support Ticket) *(Power Apps)*
- [ ] L97 — Support Ticket table designer *(Power Apps)*
- [ ] L126 — New column (Priority choice) *(Power Apps)*
- [ ] L142 — Support Tickets table sample data *(Power Apps)*
- [ ] L160 — Overview Triggers section, "+ Add trigger"
- [ ] L169 — Add trigger menu, "When a row is added or modified"
- [ ] L173 — Trigger configuration dialog
- [ ] L182 — Trigger config, "When a row is added"
- [ ] L191 — Trigger filter, "Priority equals High"
- [ ] L209 — Topics, "+ New topic"
- [ ] L218 — Topic "Escalate High Priority Ticket"
- [ ] L228 — Trigger node, Event type selected
- [ ] L258 — Tool node, "Create a flow"
- [ ] L274 — Flow trigger, four text inputs
- [ ] L305 — Send email action, dynamic content
- [ ] L322 — Tool node, mapped Trigger variables
- [ ] L337 — Message node, escalation confirmation
- [ ] L351 — Topic designer Save
- [ ] L366 — New Support Ticket form (high priority) *(Power Apps)*
- [ ] L383 — Outlook inbox: escalation email *(Outlook)*
- [ ] L393 — Activity log: topic execution

### Module 11 — Publish (26)
- [ ] L75 — Agent Overview page
- [ ] L90 — Overview, no errors, sources connected
- [ ] L98 — Overview, Publish button highlighted
- [ ] L104 — Publish confirmation dialog
- [ ] L112 — Publish success message
- [ ] L128 — Channels option
- [ ] L138 — Channels page (Teams, Demo website, etc.)
- [ ] L145 — Teams channel card, "Turn on"
- [ ] L155 — Teams channel config dialog
- [ ] L167 — Teams channel card, "Get manifest"
- [ ] L177 — Downloaded Teams app .zip *(file/desktop)*
- [ ] L186 — Teams sidebar, Apps icon *(Teams)*
- [ ] L193 — Teams Apps, "Upload a custom app" *(Teams)*
- [ ] L204 — Teams app details, "Add" *(Teams)*
- [ ] L211 — Teams chat window *(Teams)*
- [ ] L233 — Teams chat, agent greeting *(Teams)*
- [ ] L249 — Teams chat, WiFi password + citation *(Teams)*
- [ ] L266 — Teams chat, Device Request Adaptive Card *(Teams)*
- [ ] L274 — Teams chat, confirmation after request *(Teams)*
- [ ] L290 — Channels, Demo website card
- [ ] L298 — Demo website card, "Go to demo website"
- [ ] L302 — Demo website with chat widget
- [ ] L345 — Channels, M365 Copilot card
- [ ] L357 — Custom website channel, embed code
- [ ] L378 — Analytics, usage charts
- [ ] L390 — Analytics dashboard (sessions, engagement, topics)

### Module 12 — Licensing (3)
- [ ] L74 — PPAC, "Extend trial" *(PPAC)*
- [ ] L98 — M365 Admin, Copilot Studio purchase options *(M365 Admin)*
- [ ] L241 — Analytics, session metrics *(Copilot Studio)*

### Module 13 — Badge (3)
- [ ] L151 — Solution showing all components *(Power Apps)*
- [ ] L166 — Export solution dialog *(Power Apps)*
- [ ] L187 — Microsoft Learn profile, Recruit badge *(Microsoft Learn)*

---

## Effort estimate

- **Module 00 satellite surfaces:** ~30–45 min (signup/admin/SharePoint screens are quick once you're logged in).
- **Main Copilot Studio build session (02–11):** this is essentially delivering the workshop yourself once — budget **half a day to a full day**, since you're building the working agent, not just clicking around.
- **Teams + Outlook + Learn tail:** ~30 min after publish.
- **Module 01 diagrams:** ~1 hour to author 3 Mermaid diagrams.
- **Wiring + redaction:** ~1–2 hours to drop 193 images in and replace placeholders.

Realistic total: **~1.5–2 days** of focused work, gated on a clean tenant with the Module 00 environment built.
