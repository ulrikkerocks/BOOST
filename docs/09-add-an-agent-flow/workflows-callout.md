---
title: "Supplemental: Workflows Callout"
nav_exclude: true
---
# Module 09 Addition: Agent Flows vs. Workflows

**Insert this as a callout section BEFORE Lab 09 in Module 09.**  
**Purpose:** Inform participants about the new Workflows experience that launched in May 2026, so they aren't confused if they encounter it.

---

## 🆕 What's New: Workflows (Early Release)

> **Note for facilitators:** Read this section aloud or display it as a slide before starting the lab. It sets context for participants who may be in early-release environments.

Since this course was originally written, Microsoft released a **new experience called Workflows** in Copilot Studio. Here's what you need to know:

### Two Ways to Automate Your Agent

You now have two automation experiences in Copilot Studio:

| Feature | Agent Flows | Workflows (Preview) |
|---|---|---|
| **Status** | Generally Available (GA) | Public Preview / Early Release |
| **Where to find it** | Left sidebar → Flows | Left sidebar → Workflows |
| **Access** | All environments | Early-release environments only |
| **Designer** | Power Automate-style canvas | New redesigned visual canvas |
| **Key difference** | Proven, stable, familiar | New features: agent nodes, prompt nodes |
| **This lab uses** | ✅ Yes | ❌ Not in this lab |

### Agent Flows (What We're Using Today)

Agent Flows are the original automation experience in Copilot Studio. They use the Power Automate-style designer and are:
- **Stable and production-ready** (GA)
- Available in **all environments** (no early-release required)
- **Tightly integrated** with your agent topics (called directly from topic nodes)
- Billed within Copilot Studio (no separate Power Automate license needed)

### Workflows (The New Experience — Coming Soon to All)

Workflows is Microsoft's next-generation automation canvas. It includes:
- **Agent nodes** — embed other agents as steps in a workflow
- **Prompt nodes** — make a single AI call with dynamic content
- **Node-level testing** — test individual steps without running the full workflow
- **Inline configuration** — configure actions directly in the canvas without a side panel

Workflows will eventually replace Agent Flows as the primary experience. For now, stick with **Agent Flows** for this lab.

> **If you see "Workflows" in your left sidebar:** You're in an early-release environment. You can explore it after the lab, but the lab steps in Module 09 use **Agent Flows**. Both are accessed differently but produce the same result — your agent calling an automated workflow.

---

### How to Tell Which Experience You're In

**Agent Flows environment:**
- Left sidebar shows: **Flows**
- Creating a new flow: "New Agent flow" in the topic node

**Workflows environment (early release):**
- Left sidebar shows: **Flows** AND **Workflows**
- You can create either; for this lab, use **Flows** → **New Agent flow**

---

> **→ Start Lab 09: Create an Agent Flow**  
> Let's build an automation that sends a device request email to a manager.
