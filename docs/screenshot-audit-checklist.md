# Screenshot Audit Checklist

**Purpose:** Before delivering the workshop, verify that key screenshots in the course match the current Copilot Studio UI (as of June 2026).

**How to use:**
1. Open https://microsoft.github.io/agent-academy/recruit/ in a browser
2. Sign in to https://copilotstudio.microsoft.com in a separate window
3. Compare each listed screenshot against the current UI
4. Mark ✅ (matches), ⚠️ (minor difference — note it), or 🔴 (major difference — needs update)

---

## Module 00: Course Setup

| Screenshot | What to check | Status |
|---|---|---|
| Copilot Studio trial signup screen | URL still works, form layout | ☐ |
| Power Apps Developer env creation | Environment type options | ☐ |
| PPAC Authors role setup | Security group assignment flow | ☐ |
| SharePoint IT Help Desk template | Template still available | ☐ |
| Devices list with Image column | Column configuration UI | ☐ |

---

## Module 02: Fundamentals

No screenshots (conceptual module). ✅

**New screenshot needed:** Overview page annotated diagram.  
See: `workshop/02-copilot-studio-fundamentals/overview-page-orientation.md` for the text diagram.  
Capture a real screenshot when you sign into Copilot Studio.

---

## Module 03: Declarative Agent

| Screenshot | What to check | Status |
|---|---|---|
| Creating a declarative agent | Entry point from Home page | ☐ |
| Agent creation wizard | Still uses same flow? | ☐ |

---

## Module 04: Solution

| Screenshot | What to check | Status |
|---|---|---|
| Solution creation in PPAC | PPAC UI for solution creation | ☐ |
| Preferred solution setting | Settings > Advanced in agent | ☐ |

---

## Module 06: Build a Custom Agent

These are the most important screenshots to verify.

| Screenshot | What to check | Status |
|---|---|---|
| `6.1_*` — Home page description box | Natural language creation entry UI | ☐ |
| AI suggestions after creation | Suggestions pane appearance | ☐ |
| Overview page after agent creation | Overview page with all sections | ☐ |
| Knowledge section — add SharePoint | SharePoint knowledge source dialog | ☐ |
| Knowledge section — add file | File upload dialog | ☐ |
| Test pane | Test pane UI, refresh/new session button | ☐ |
| "Wheel cog" → now gear ⚙️ | Settings icon location | ☐ |
| Web Search toggle | Still in same location? | ☐ |

---

## Module 07: Add a Topic

| Screenshot | What to check | Status |
|---|---|---|
| `7.1_01_Topics.png` — Topics tab | Tab location in agent navigation | ☐ |
| `7.1_02_FromBlank.png` — Add topic | + Add a topic button and menu | ☐ |
| `7.1_03_TopicNameAndDescription.png` | Name + description entry field | ☐ |
| Topic editor canvas | Node canvas layout | ☐ |
| `7.3_22_EditInstructions.png` | Overview tab → Edit instructions | ☐ |
| `7.3_30_TestResponse.png` | Test pane response | ☐ |

---

## Module 08: Adaptive Cards

| Screenshot | What to check | Status |
|---|---|---|
| Adaptive Card node | Card node in topic canvas | ☐ |
| Adaptive Card JSON editor | JSON editing interface | ☐ |
| Power Fx data binding | Formula field UI | ☐ |

---

## Module 09: Agent Flows

| Screenshot | What to check | Status |
|---|---|---|
| `9.1_01_AddNewAgentFlow.png` | "Add a tool" → New Agent flow | ☐ |
| `9.1_02_SelectTrigger.png` — Trigger config | Agent flow designer trigger node | ☐ |
| Agent flow designer canvas | Overall designer layout | ☐ |
| `9.1_52_Publish.png` — Publish flow | Publish button in designer | ☐ |
| `9.2_02_SelectTopics.png` — Topics tab | Topics tab in agent navigation | ☐ |

---

## Module 10: Event Triggers

| Screenshot | What to check | Status |
|---|---|---|
| `10_AddTriggerDialog.png` | Trigger library dialog | ☐ |
| `10_NavigateToTrigger.png` | Overview page Triggers section | ☐ |
| `10_ConfigureTriggerNameAndConnections.png` | Trigger setup wizard | ☐ |
| `10_EditTriggerInPowerAutomate.png` | Edit in Power Automate button | ☐ |
| `10_SelectOutlookConnector.png` | Tools tab → add connector | ☐ |
| `10_MonitorTriggerTest.png` | Test trigger panel | ☐ |

---

## Module 11: Publish

| Screenshot | What to check | Status |
|---|---|---|
| `publish.png` — Publish button | Location on Overview page (top right) | ☐ |
| `channels-tab.png` — Channels navigation | Is there still a Channels tab? | ⚠️ Likely moved to Overview section |
| `add-channel.png` — Add channel | Teams channel setup | ☐ |
| `see-agent-teams.png` — Open in Teams | Button location | ☐ |
| `m365-teams-availability-options.png` | Availability options pane | ☐ |

---

## Module 12: Licensing

No screenshots (text content module). ✅

---

## Key UI Elements to Watch For (All Modules)

These are known changes from the old UI that may appear in older screenshots:

| Old UI element | New UI element |
|---|---|
| Separate "Topics" left sidebar tab | Topics section on Overview page OR Topics tab in agent nav |
| Separate "Actions/Skills" section | "Tools" section on Overview page |
| "Settings" in left sidebar (agent-level) | Gear ⚙️ icon on Overview page |
| Agent creation wizard | Home page natural language description box |
| Multiple top-level tabs in agent | Single Overview page with sections |
| "Publish" in navigation menu | "Publish" button at top of Overview page |

---

## If You Find Outdated Screenshots

**Options:**
1. **Add a note** in the facilitator guide: "The screenshot in the course shows the old UI; in the current UI, you'll find this at..."
2. **Capture a new screenshot** and store it in `assets/screenshots/` in this repo
3. **Submit a PR** to the microsoft/agent-academy GitHub repo with updated screenshots

**Screenshot naming convention:** `XX.Y_NN_DescriptiveName.png`  
Example: `9.1_01_AddNewAgentFlow.png`
