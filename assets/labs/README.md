# 🕵️ Agent Academy — Build "Rex" in the New Copilot Studio

![Mission Status: ACTIVE](https://img.shields.io/badge/Mission-ACTIVE-brightgreen)

**Welcome, Recruit.**

Microsoft **rebuilt Copilot Studio**. This isn't a UI refresh — it's a new **agentic orchestrator**, a new **agent-building interface**, and a new headline concept: **Skills** (reusable instructions written in markdown). The classic world of **topics and triggers is gone** in this experience; you shape an agent with **Instructions, Knowledge, Skills, Tools, Memory,** and **Connected agents** — all on one **Build** page — and let the enhanced orchestrator do the reasoning.

These labs rebuild, end-to-end, the agent from Reza Dorrani's walkthrough: **Rex, your help desk buddy** — an IT support agent for Contoso employees that answers from your docs, resets passwords, troubleshoots VPN, **logs tickets to a SharePoint list**, emails confirmations (with a **PDF report**), and kicks off a **manager-approval workflow** for software requests.

> 🎥 Source walkthrough: Reza Dorrani — **"Microsoft Rebuilt Copilot Studio — Here's Everything New."**
> ▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs
> Every lab links to the exact moment in the video.

> 🟢 **Everything here uses the NEW experience only.** No topics, no trigger phrases, no classic orchestration toggle. If a step sounds like classic Copilot Studio, it's a bug — tell your facilitator.

---

## 🎯 Mission Objective

By the end you'll be able to:

- Switch into the **new experience** and explain how it differs from classic (no topics, no migration path, enhanced orchestration by design)
- Build an agent on the **Build** tab from natural-language **Instructions**, and configure **Settings**, a **greeting**, and **suggested prompts**
- Ground it with **Knowledge** (uploaded docs / SharePoint / OneDrive / websites) and turn on **Memory**
- Author reusable **Skills** in markdown (`password-reset`, `vpn-troubleshooting`, `smart-triage`, `software-installation-request`) — and upload/download them
- Equip **Tools** (Outlook **Send an email**, SharePoint **Create item**) with **AI-filled** inputs
- Have the agent **log a ticket** to SharePoint and **email** a confirmation — then iterate a skill to also **generate and attach a PDF**
- Build a **Workflow** in the new designer for **manager approvals** and call it from a skill
- **Evaluate** with a quick conversation set, **Publish** to Teams + Microsoft 365, **Share**, and **Monitor**

---

## 🧪 Prerequisites

- **Copilot Studio** with the **new experience** available (look for **Try it now** on the home page)
- A Microsoft 365 tenant with **SharePoint**, **Outlook**, and (for the workflow) **Approvals**
- A SharePoint **Tickets** list to act as the ticketing system — your **IT Help Desk** site ([Lab 00](./00-course-setup.md))
- Two knowledge documents you'll upload (templates provided in [Lab 00](./00-course-setup.md)):
  1. **Contoso IT FAQ** — help desk email, helpline number, hours, basic Q&A
  2. **Contoso Approved Software List** — requestable apps + whether each is self-service or needs manager sign-off
- A Power Platform **solution** as your preferred solution

> ⚠️ Skills, Workflows, and Evaluate are **production-ready preview**. Labels may shift; these labs target **June 2026**. Fallbacks are in [`FACILITATOR-NOTES.md`](./FACILITATOR-NOTES.md).

---

## 🧭 Curriculum Overview

Run in order — each lab builds on Rex from the last.

| Lab | Title | Mission Briefing | Video |
| :--- | :--- | :--- | :--- |
| `00` | 🧰 [Course Setup](./00-course-setup.md) | Switch to the new experience; prep the Tickets list, docs, and solution | 0:00 |
| `01` | 🤖 [Build Rex](./01-build-helpdesk-agent.md) | Create the agent, instructions, settings, greeting, suggested prompts | 1:46 / 4:00 |
| `02` | 📚 [Ground Rex with Knowledge](./02-add-knowledge.md) | Upload the two docs, enable Memory, run a first test | 4:30 |
| `03` | 🧠 [Teach Rex Skills](./03-add-a-skill.md) | Author 4 reusable markdown skills | 5:50 |
| `04` | 🔧 [Equip Tools & Log Tickets](./04-add-tools.md) | Send-email + create-item tools; ticket end-to-end; add a PDF report | 7:44 / 16:00 |
| `05` | 🔁 [Automate Approvals with a Workflow](./05-add-a-workflow.md) | Manager-approval workflow, called from a skill | 17:43 |
| `06` | 🧪 [Evaluate Rex](./06-test-evaluate-monitor.md) | Generate a quick conversation set and run an evaluation | 25:01 |
| `07` | 📢 [Publish, Share & Monitor](./07-publish-and-share.md) | Ship to Teams + M365 Copilot; watch the Monitor tab | 26:08 |

> ✅ Finish all eight and you've shipped Rex — a grounded, action-taking, ticket-logging help desk agent built entirely in the new experience.

*Built for the EPPC 2026 Agent Academy workshop · #EPPC26*
