# 🧰 Mission 00: Course Setup — Switch to the New Experience

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION COLD START | ⭐ | 20 min | Copilot Studio (new experience), SharePoint | Setup, New Experience | IT |

🎥 **Watch the Walkthrough** — *Intro & the new designer experience*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=0s

---

## 🎯 Mission Brief

Before you build **Rex**, you need to be standing in the **new** Copilot Studio — not the classic one — and you need a base of operations: a SharePoint **Tickets** list to act as the ticketing system, two **knowledge documents**, and a **solution**. This mission gets you there and resets any classic-era muscle memory.

## 🔎 Objectives

1. Switch from the **classic** experience to the **new** experience with **Try it now**
2. Understand what's different (no topics, no migration path, enhanced orchestration by design)
3. Prepare the **Tickets** SharePoint list, the **two knowledge docs**, and a **solution**

---

## 🆕 Get into the new experience

1. Go to **Copilot Studio**: https://copilotstudio.microsoft.com
2. If you land on the **classic** home page, look **top-right** for **Try it now** and select it — that switches you to the **new** experience.

   > 🔁 You can switch back to classic anytime with the same toggle. Existing **classic** agents still open in the classic designer; agents you create in the **new** experience always open in the new designer.
3. Confirm the environment selector points at a **dev/sandbox** environment.

### What actually changed (say this out loud before you build)

- **No topics, no trigger phrases.** The new experience has **Skills** and **Workflows** instead. You describe behavior; the orchestrator decides what to do.
- **Enhanced orchestration by design.** In classic, orchestration was a configurable setting. In the new experience every agent uses the improved, deep-reasoning orchestration runtime — there's no toggle.
- **No migration path.** You can't move agents between classic and new (either direction). Build net-new here.
- **Everything on one Build page.** Instructions, Knowledge, Skills, Tools, Memory, Connected agents, and Model live together.

> 📚 Microsoft publishes a *Classic vs. new agent experience* comparison if learners want the full list of differences.

---

## 🧪 Lab 00: Set up your base of operations

### ✨ Use case

> **As a** Contoso employee
> **I want** fast IT help — password resets, VPN fixes, software requests — and a ticket logged when I need admin help
> **So that** I stay productive and nothing falls through the cracks.

That's the agent (**Rex**) you'll build across these labs.

### Step 1 — Create the Tickets list (your ticketing system)

Reza's ticketing system is simply a **SharePoint list**. We'll use the **Tickets** list on your **IT Help Desk** site.

1. In **SharePoint**, open (or create) your **IT Help Desk** site. If you're creating it, use the **IT Help Desk** team-site template, which includes a **Tickets** list.
2. Open the **Tickets** list and note its columns — the agent will read this **schema** at runtime to decide what to fill in. A typical Tickets list has columns like:

   | Column | Type | Used for |
   | :--- | :--- | :--- |
   | **Title** | Single line | Short summary of the issue |
   | **Description** | Multi-line | Symptoms / details |
   | **Status** | Choice (New, In progress, Resolved, Closed) | Lifecycle |
   | **Priority** | Choice (Low, Normal, High, Critical) | Triage |
   | **Category** | Choice (Hardware, Software, Network, Access, Other) | Routing |
   | **Requestor** | Person/Text | Who raised it |

   > 🔎 **Confirm your real columns before class.** Open the list → **Settings → List settings** and note the actual **display + internal names** and choice values. You'll point the **Create item** tool at this list in [Lab 04](./04-add-tools.md). The good news: in the new experience the agent **reads the list schema itself** via the `smart-triage` skill, so you mostly just need the **site URL + list name** right.
3. Copy the **site URL** and the **list name** — you'll need both.

### Step 2 — Prepare the two knowledge documents

You'll upload two documents as Rex's knowledge in [Lab 02](./02-add-knowledge.md). **Ready-made copies are included in this folder** — use them as-is, or recreate your own from the outlines below:

- 📄 **`Contoso_IT_FAQ.docx`**
- 📄 **`Contoso_Approved_Software_List.docx`**

**1) `Contoso IT FAQ`** covers:
- Help desk **hours** (Mon–Fri, 7:00 AM–7:00 PM local; high-priority monitored 24/7)
- How to reach the help desk (`helpdesk@contoso.com`, extension 4357 "HELP")
- Ticket response times, device enrollment, password policy, Wi‑Fi, and software/data basics

**2) `Contoso Approved Software List`** explains the three distribution types — **Self-service**, **Manager sign-off**, and **Not listed** — and lists the approved apps:

| Application | Category | Distribution |
| :--- | :--- | :--- |
| Microsoft Power BI Desktop | Analytics & reporting | Self-service |
| Microsoft Visual Studio Code | Development | Self-service |
| Microsoft PowerToys | Utilities | Self-service |
| Microsoft Power Automate Desktop | Automation | Self-service |
| Microsoft Visio | Diagramming | Manager sign-off |
| Microsoft Project | Project management | Manager sign-off |
| Microsoft 365 Copilot | Productivity (AI) | Manager sign-off |
| Visual Studio Professional | Development | Manager sign-off |

> These two docs drive several later scenarios: help-desk hours (Lab 02), "Can I install **Power BI Desktop**?" → self-service (Lab 02), and the manager-approval workflow for **Microsoft Visio** (Lab 05). Keep the app names consistent with this table.

### Step 3 — Create a solution (set it as preferred)

1. In **Power Apps** (https://make.powerapps.com), same environment → **Solutions** → **+ New solution** (create a publisher with a prefix like `aa` if needed). Name it **`Help Desk Agent`**.
2. Set it as your **preferred solution** so Rex lands inside it.

   > 🧩 You can also confirm/change the target solution **up front** in the agent's **Settings** right after you create Rex (Lab 01). In the video this i