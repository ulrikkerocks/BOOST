---
title: Participant Reference Card
nav_order: 4
---
# New Copilot Studio UI: Participant Reference Card

**For participants in the Copilot Agent Academy Recruit workshop**

Print or keep this open while doing labs.

---

## The Overview Page

When you open any agent in Copilot Studio, you land on the **Overview page**.
This is your main workspace.

```
Left sidebar          │  Overview Page                    │  Test Pane
──────────────────────│───────────────────────────────────│──────────────
🏠 Home               │  [Agent Name]        [Publish] [⋯]│
🤖 Agents             │  [Description]                [⚙️]│  Test your
▶ Flows               │                                   │  agent here
⚡ Workflows (EA)     │  Instructions       [Edit]        │
🔗 Connections        │  "You are..."                     │  [Type a
⚙️ Settings           │                                   │   message...]
                      │  Triggers           [+ Add]       │
                      │                                   │
                      │  Knowledge          [+ Add]       │
                      │  ● SharePoint                     │
                      │  ● Document.pdf                   │
                      │                                   │
                      │  Tools              [+ Add]       │
                      │  ● Agent Flow                     │
                      │                                   │
                      │  Topics             [+ Add]       │
                      │  ● Available devices              │
                      │                                   │
                      │  Channels           [+ Add]       │
                      │  ● Teams & M365                   │
```

---

## Key Navigation Changes

| What you want to do | Where to find it |
|---|---|
| Create a new agent | Left sidebar → **Home** → type description |
| View all your agents | Left sidebar → **Agents** |
| Edit agent instructions | Overview page → **Instructions** → Edit |
| Add a knowledge source | Overview page → **Knowledge** → + Add knowledge |
| Add an automation (flow) | Overview page → **Tools** → + Add a tool |
| Create a new topic | Overview page → **Topics** → + Add topic (or left nav → Topics tab) |
| Add event trigger | Overview page → **Triggers** → + Add trigger |
| Publish agent | Overview page → **Publish** button (top right) |
| Publish to Teams | Overview page → **Channels** → Add channel → Teams |
| Agent settings | Overview page → **⚙️** gear icon |
| View Agent Flows | Left sidebar → **Flows** |

---

## Creating an Agent (New Flow)

1. Left sidebar → **Home**
2. Type what you want your agent to do in the description box
3. AI generates: name, description, initial instructions, suggested knowledge/topics
4. Review AI suggestions → accept or dismiss
5. You land on the **Overview page** — start customizing!

---

## Testing Your Agent

- **Test pane** is always on the right side of the Overview page
- **New test session:** click the circular arrow icon (restart/refresh) in the Test pane
- **Activity map:** click the chart icon to see which knowledge sources were searched
- **Track between topics:** click ⋯ → "Track between topics" to see topic transitions

---

## AI Model (New in 2026)

You can now choose which AI model your agent uses:

- **Settings** ⚙️ → **Advanced** → AI model selection
- Default: **GPT-4.1**
- Options include: GPT-4.1, GPT-5, Claude Sonnet 4.5/4.6, Mistral Medium 3.5
- Different models have different capabilities and credit costs

---

## Agent Flows vs. Workflows

| | Agent Flows | Workflows |
|---|---|---|
| Status | ✅ GA | 🔬 Preview (Early Release) |
| Availability | All environments | Early-release envs only |
| Used in labs | ✅ Yes | ❌ Not in this course |
| Found in | Left sidebar → Flows | Left sidebar → Workflows |

---

## Quick Troubleshoot

**"I can't find the Topics tab"**  
→ Look at the top of your agent page. There should be tabs: Overview, Topics, Analytics, Activity, Settings.  
→ Or scroll down on the Overview page to the Topics section.

**"The Publish button is greyed out / not available"**  
→ Trial environments need the Authors role. Ask your facilitator.

**"I see a Workflows option but the lab says Agent Flows"**  
→ You're in an early-release environment. Use **Flows** (Agent Flows) for the lab.

**"My AI suggestions disappeared"**  
→ They're session-only. Add components manually via the Overview page sections.

**"The connector asks me to 'Allow'"**  
→ Select Allow. This is a one-time consent to use your credentials for that connector.
