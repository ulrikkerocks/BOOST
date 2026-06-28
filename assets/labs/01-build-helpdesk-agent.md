# 🤖 Mission 01: Build Rex, Your Help Desk Buddy

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION FIRST CONTACT | ⭐ | 30 min | Copilot Studio (new experience) | Instructions, Build tab, Settings | IT |

🎥 **Watch the Walkthrough** — *Build an agent with the new interface · Build a help desk agent*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=106s

---

## 🎯 Mission Brief

In the new experience you don't map out conversations — you **describe** the agent and equip it. The whole agent lives on the **Build** tab: **Instructions**, **Knowledge**, **Skills**, **Tools**, **Memory**, **Connected agents**, and **Model**, all in one place. In this mission you'll create **Rex**, write his identity in plain language, set him up in **Settings**, and give him a greeting and suggested prompts.

## 🔎 Objectives

1. Create an agent in the new experience and set its **name, icon, and accent color**
2. Tour the **Build** tab building blocks
3. Write Rex's **Instructions**
4. Configure **Settings** (preferred solution, moderation, authentication)
5. Add a **greeting message** and **suggested prompts**

---

## 🧩 The Build tab building blocks

| Block | What it's for |
| :--- | :--- |
| **Instructions** | The agent's identity, personality, tone, scope, and behavioral rules |
| **Knowledge** | Connect your data — uploaded docs, SharePoint, OneDrive, websites, or **Microsoft IQ** |
| **Memory** | Let the agent remember previous interactions and context for better results |
| **Tools** | Let the agent take actions — connectors, **MCP**, and the new **Workflows** |
| **Skills** | Reusable behavior defined as **markdown** instructions — upload, or build from blank |
| **Connected agents** | Agent-to-agent hand-off (one agent delegates to another) |
| **Model** | The AI model that powers the agent's reasoning |

> 🧠 Everything visible at once is the point — you can see Rex's instructions, skills, tools, and knowledge together while you build.

---

## 🧪 Lab 01: Create Rex

### Prerequisites

- You're in the **new experience** with a **preferred solution** set ([Lab 00](./00-course-setup.md)).

### 1.1 Create the agent

1. On the Copilot Studio home page, choose to **create a new agent** (new experience).
2. When the Build tab opens, set the **name**:

   ```text
   Rex, your help desk buddy
   ```

3. Select the **agent icon** — pick one from the catalog (or upload your own PNG), choose a **color**, and set a **custom accent color** if you like.

### 1.2 Write Rex's instructions

In **Instructions**, enter plain text describing who Rex is and the one rule that matters most (escalate to a ticket when admin access is needed):

```text
You are Rex, the IT support agent for Contoso employees. Your job is to help
employees solve common device, access, and software issues. Be friendly,
concise, and practical. If an issue needs admin access, log a ticket and hand
it to the help desk team. Never ask for passwords or one-time codes, and never
help bypass security.
```

Select **Save** (💾).

> You'll add the *how* — password resets, VPN steps, triage, software requests — as **Skills** in [Lab 03](./03-add-a-skill.md). Keep the instructions short; skills carry the detailed playbooks.

### 1.3 Configure Settings

Open **Settings** (top right).

1. **Solution / schema / language** — confirm Rex is in your **`Help Desk Agent`** solution (it uses your **preferred solution** by default; you can change it here up front). Note the agent **schema name** and **primary language**.
2. **AI and behavior** — optionally allow **other agents to connect** to Rex (needed if another agent will delegate to him).
3. **Moderation level** — choose how strictly responses are filtered for unsafe content (under safety/access). Leave at the default for the workshop.
4. **Authentication** — for the demo, **Authenticate with Microsoft** (so SharePoint/Outlook tools run as the signed-in user) or set **No authentication** if your facilitator prefers. Save and exit Settings.

### 1.4 Add a greeting and suggested prompts

1. Set a **greeting message**, e.g.:

   ```text
   Hi, I'm Rex — your IT help desk buddy. How can I help today?
   ```

2. Add **four suggested prompts** to give users an on-ramp:

   ```text
   - Help desk hours
   - Can I install Power BI Desktop?
   - I'm locked out and forgot my password
   - My VPN keeps disconnecting
   ```

3. **Save.**

> These four map directly to the scenarios you'll test in later labs (knowledge, software list, password reset skill, VPN skill).

### 1.5 Peek at Preview

1. Open the **Preview** tab. You'll see your **greeting** and **suggested prompts**.
2. Note the **maker vs. end-user** toggle — as the **maker** you see extra detail (the agent's reasoning, inputs/outputs). Leave end-user preview **off** for now.
3. Rex has no knowledge or skills yet, so don't expect grounded answers. We fix that next.

---

## ✅ Mission Complete

Rex exists, has an identity and guardrails, lives in your solution, and greets users with suggested prompts. Time to give him something to know.

⏭️ Next: [**Mission 02 — Ground Rex with Knowledge**](./02-add-knowledge.md)

## 📚 Tactical Resources

- 🔗 [Build an agent (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/build-overview)
- 🔗 [Configure agent details and instructions (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/authoring-instructions)
- 🔗 [Configure starter prompts](https://learn.microsoft.com/microsoft-copilot-studio/configure-starter-prompts)
