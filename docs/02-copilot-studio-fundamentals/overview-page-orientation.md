# Module 02 Addition: The Copilot Studio Overview Page

**Insert this section BEFORE the "Four Building Blocks" section in Module 02.**  
**Purpose:** Give participants a visual mental model of where the building blocks live in the UI, before explaining what they are.

---

## 🗺️ Your Home Base: The Overview Page

Before we dive into the four building blocks, let's orient you in the new Copilot Studio interface. When you open any agent, you'll land on the **Overview page** — this is your main authoring surface.

> **Why this matters:** Everything you build in this course lives on the Overview page. Understanding this layout now will save you time in every lab.

### What the Overview Page Looks Like

The Overview page is a **single scrollable canvas** showing all your agent's components at once. You no longer navigate to separate tabs for each feature — it's all visible in one view.

```
┌─────────────────────────────────────────────────────────────┐
│  [Agent Name]                           [Publish] [...]     │
│  [Description]                                       [⚙️]   │
├─────────────────────────────────────────────────────────────┤
│  Instructions                            [Edit]             │
│  You are a helpful IT assistant...                          │
├─────────────────────────────────────────────────────────────┤
│  Triggers                                [+ Add trigger]    │
│  (Event-based autonomous activation)                        │
├─────────────────────────────────────────────────────────────┤
│  Knowledge                               [+ Add knowledge]  │
│  ● Contoso IT SharePoint                                    │
│  ● Guest WiFi Guide.docx                                    │
├─────────────────────────────────────────────────────────────┤
│  Tools                                   [+ Add a tool]     │
│  (Connectors, Agent Flows, Workflows)                       │
├─────────────────────────────────────────────────────────────┤
│  Topics                                  [+ Add a topic]    │
│  ● Available devices                                        │
│  ● Request device                                           │
├─────────────────────────────────────────────────────────────┤
│  Channels                                [+ Add channel]    │
│  ● Teams and Microsoft 365                                  │
└─────────────────────────────────────────────────────────────┘
```

On the **right side**, you always have the **Test pane** — a live chat window for testing your agent as you build it.

### Overview Page Sections at a Glance

| Section | What you do here | Corresponds to... |
|---|---|---|
| **Instructions** | Define agent persona, tone, and behavior rules | Building block 4: Instructions |
| **Triggers** | Add event-based triggers for autonomous behavior | Autonomous agents (Module 10) |
| **Knowledge** | Connect SharePoint, documents, websites | Building block 1: Knowledge |
| **Tools** | Add connectors, flows, and APIs | Building block 2: Tools |
| **Topics** | Define conversational entry points | Building block 3: Topics |
| **Channels** | Publish to Teams, websites, etc. | Module 11: Publishing |

> **💡 Tip:** You can do everything from the Overview page. You don't need to navigate away to add knowledge, create a topic, or test — it's all right here.

### Navigation: How to Get Around

**Left sidebar** (always visible):
- **Home** — Create a new agent using natural language
- **Agents** — Your list of agents
- **Flows** — Your Agent Flows (separate from the agent view)
- **Connections** — Manage your connector connections

**Within an agent:**
- The **Overview** tab is your main view
- **Topics** tab takes you to the full topic list
- **Analytics**, **Activity**, **Settings** are also accessible

---

## 🏗️ Creating a New Agent: The Natural Language Flow

One more thing before we dive in. When you create a new agent in the **new** Copilot Studio, the experience starts with natural language:

1. Go to **Home** in the left sidebar
2. Type a description of what you want your agent to do
3. AI provisions a starter agent for you — suggesting a name, instructions, knowledge sources, topics, and even trigger phrases
4. You land on the **Overview page** with the agent ready to customize

This is exactly what you'll do in **Module 06**. For now, just know that the Overview page is your destination after creation.

---

> **→ Continue to: The Four Building Blocks**  
> Now that you know where everything lives, let's understand what each piece does.
