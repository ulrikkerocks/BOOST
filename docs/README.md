---
title: Home
nav_order: 1
---
# Agent Academy Recruit Course — Updated for New Copilot Studio UI

**Last Updated:** June 2026  
**Duration:** 1 day (~8 hours hands-on)  
**Audience:** Makers, IT Pros, Power Platform enthusiasts  
**Source:** [microsoft.github.io/agent-academy/recruit](https://microsoft.github.io/agent-academy/recruit/)

---

## Overview

Welcome to the **Copilot Agent Academy — Recruit Course**! This hands-on workshop teaches you how to build production-ready AI agents using Microsoft Copilot Studio.

By the end of this course, you will:
- ✅ Understand the fundamentals of conversational and autonomous AI agents
- ✅ Build a custom agent with knowledge sources, topics, and automation
- ✅ Create rich user experiences with Adaptive Cards
- ✅ Publish your agent to Microsoft Teams and other channels
- ✅ Understand licensing, costs, and production considerations

You'll build the **Contoso Helpdesk Agent** — a real-world AI assistant that helps employees find IT information and request devices.

---

## Prerequisites

Before starting this course, ensure you have:

- **Microsoft 365 account** (Business Basic trial or existing tenant)
- **Copilot Studio trial access** (sign up at [aka.ms/TryCopilotStudio](https://aka.ms/TryCopilotStudio))
- **Power Apps Developer environment** (optional but recommended — created in Module 00)
- **Basic familiarity with Microsoft 365** (SharePoint, Teams, Outlook)

**No coding experience required** — this course uses visual designers and natural language creation.

---

## Course Modules

| Module | Title | Duration | Topics |
|--------|-------|----------|--------|
| [00](modules/00-course-setup/) | Course Setup | 30 min | M365 setup, SharePoint site, sample data, publishing permissions |
| [01](modules/01-introduction-to-agents/) | Introduction to Agents | 30 min | LLMs, RAG, orchestration, agent types |
| [02](modules/02-copilot-studio-fundamentals/) | Copilot Studio Fundamentals | 30 min | Four building blocks, Overview page navigation |
| [03](modules/03-declarative-agent-m365/) | Declarative Agent for M365 Copilot | 30 min | Extend M365 Copilot, declarative agents |
| [04](modules/04-creating-a-solution/) | Creating a Solution | 20 min | Solution publisher, solution setup, preferred solution |
| [05](modules/05-prebuilt-agents/) | Using Pre-Built Agents | 20 min | Template gallery, customizing templates |
| [06](modules/06-build-custom-agent/) | Build a Custom Agent | 75 min | Natural language creation, knowledge sources, AI model selection |
| [07](modules/07-add-topic-with-triggers/) | Add a Topic with Triggers | 60 min | Topic designer, trigger phrases, Power Fx, SharePoint data |
| [08](modules/08-enhance-with-adaptive-cards/) | Enhance with Adaptive Cards | 60 min | Adaptive Card designer, data binding, rich UI |
| [09](modules/09-automate-with-agent-flows/) | Automate with Agent Flows | 50 min | Agent Flows, email automation, connectors |
| [10](modules/10-add-event-triggers/) | Add Event Triggers | 45 min | Event-based activation, autonomous agents, Dataverse triggers |
| [11](modules/11-publish-your-agent/) | Publish Your Agent | 30 min | Publishing to Teams, demo website, channels |
| [12](modules/12-understanding-licensing/) | Understanding Licensing | 20 min | Copilot Credits, trial vs. production, cost planning |
| [13](modules/13-securing-recruit-badge/) | Securing Your Recruit Badge | 15 min | Completion checklist, badge claim, next steps |

**Total:** ~8 hours (including breaks)

---

## Workshop Resources

### For Facilitators
- **[Facilitator Guide](facilitator-guide.md)** — Detailed notes for workshop delivery, common pitfalls, troubleshooting, and timing guidance
- **[Screenshot Audit Checklist](screenshot-audit-checklist.md)** — Verify all screenshots match the June 2026 UI before delivery

### For Participants
- **[Participant Reference Card](participant-reference-card.md)** — Quick reference for Overview page navigation and key UI elements

### Supplemental Content
- **[02-copilot-studio-fundamentals/overview-page-orientation.md](02-copilot-studio-fundamentals/overview-page-orientation.md)** — Visual walkthrough of the new Overview page model (add to Module 02)
- **[09-automate-with-agent-flows/workflows-callout.md](09-add-an-agent-flow/workflows-callout.md)** — Explanation of Agent Flows vs. Workflows (add to Module 09)

---

## The Scenario: Contoso Helpdesk Agent

All modules build a connected scenario around a single agent:

| Component | Details |
|---|---|
| **Agent Name** | Contoso Helpdesk Agent |
| **Purpose** | Help employees find IT information and request devices |
| **Data Source** | Contoso IT SharePoint site (created in Module 00) |
| **Solution** | Contoso Helpdesk Agent solution (created in Module 04) |
| **Final Features** | Knowledge grounding, conversational topics, Adaptive Cards, email automation, event triggers |
| **Published To** | Microsoft Teams + demo website |

---

## Learning Path: What You'll Build

The course follows a progressive build model. Each module adds new capabilities to the same agent:

### Phase 1: Foundation (Modules 00-02)
- Set up your environment (M365, Copilot Studio, SharePoint)
- Understand agent concepts and the Copilot Studio interface
- Learn the four building blocks: Knowledge, Tools, Topics, Instructions

### Phase 2: Getting Started with Agents (Modules 03-05)
- Create a declarative agent for M365 Copilot (extends Copilot with custom knowledge)
- Set up a solution for proper application lifecycle management (ALM)
- Explore pre-built agent templates from the gallery

### Phase 3: Build Your Custom Agent (Modules 06-09)
- **Module 06:** Create the base agent with multiple knowledge sources (SharePoint, documents, websites, web search)
- **Module 07:** Add a structured topic: "Device Request" with trigger phrases and SharePoint data queries
- **Module 08:** Enhance the topic with Adaptive Cards for rich visual display
- **Module 09:** Automate actions with an Agent Flow (send email when device is requested)

### Phase 4: Advanced Features (Modules 10-11)
- **Module 10:** Add event triggers for autonomous behavior (auto-escalate high-priority tickets)
- **Module 11:** Publish to Microsoft Teams and deploy the agent to end users

### Phase 5: Production Readiness (Modules 12-13)
- **Module 12:** Understand licensing (Copilot Credits, trial vs. production, cost estimation)
- **Module 13:** Complete the course, claim your badge, explore next steps

---

## Delivery Format

### Full-Day Workshop (Recommended)
| Time | Activity | Duration |
|------|----------|----------|
| 09:00–10:30 | Modules 00-02: Setup and fundamentals | 90 min |
| 10:30–10:45 | Break | 15 min |
| 10:45–12:00 | Modules 03-06: Declarative agents, solutions, templates, start custom agent | 75 min |
| 12:00–13:00 | Lunch | 60 min |
| 13:00–15:00 | Modules 06-08: Complete custom agent, topics, Adaptive Cards | 120 min |
| 15:00–15:15 | Break | 15 min |
| 15:15–17:00 | Modules 09-11: Agent Flows, event triggers, publishing | 105 min |
| 17:00–17:30 | Modules 12-13: Licensing, badge, wrap-up | 30 min |

**Total:** 8 hours (including breaks and lunch)

### Self-Paced (Alternative)
Participants can complete the course at their own pace over 1-2 weeks. Provide:
- Access to the module READMEs
- Participant reference card for UI navigation
- Support channel (Teams/email) for questions

---

## What's New: June 2026 UI Updates

This course has been updated to reflect the **new Copilot Studio UI** released in late 2025. Key changes:

### The Overview Page Model
**Old model:** Multiple tabs/sections (Topics, Actions, Settings, etc.) accessed via left sidebar navigation.  
**New model:** A single **Overview page** showing all agent components at once (scroll down to see everything).

The Overview page contains:
- **Details** — Agent name and description
- **Instructions** — System prompt (up to 8,000 chars)
- **Knowledge** — SharePoint, websites, files, Dataverse, general web search
- **Tools** — Connectors, Agent Flows, Workflows, MCP, APIs
- **Triggers** — Event-based activation
- **Agents** — Multi-agent orchestration
- **Topics** — Conversational flows
- **Suggested Prompts** — Starter prompts for Teams/M365 Copilot

**Test pane** is always visible on the right. **Publish** button is at the top right.

### Natural Language Agent Creation
**New:** Home page → describe what you want → AI provisions the agent with suggested components.  
**Old:** "New agent" button → wizard/form → opens topic editor.

### Agent Flows vs. Workflows
- **Agent Flows** — Original automation experience (GA, available in all environments). This course uses Agent Flows.
- **Workflows** — New preview experience (early-release environments only) with agent nodes, prompt nodes, and node-level testing. Not covered in this course.

For more details, see the [Facilitator Guide](facilitator-guide.md) and [research/new-ui-notes.md](../research/new-ui-notes.md).

---

## Next Steps After Recruit

### Special Ops Level (Advanced Course)
- Multi-agent orchestration
- Custom connectors and APIs
- Dataverse integration patterns
- Production deployment strategies
- Analytics and monitoring

### Microsoft Learn Paths
- [Build bots with Microsoft Copilot Studio](https://learn.microsoft.com/en-us/training/paths/work-power-virtual-agents/)
- [Extend Microsoft Copilot for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/)
- [Power Platform fundamentals](https://learn.microsoft.com/en-us/training/paths/power-plat-fundamentals/)

### Community
- **Copilot Studio Community:** [powerusers.microsoft.com/t5/Microsoft-Copilot-Studio/ct-p/PVACommunity](https://powerusers.microsoft.com/t5/Microsoft-Copilot-Studio/ct-p/PVACommunity)
- **Power Platform User Groups:** Find local meetups at [powerusers.microsoft.com](https://powerusers.microsoft.com/)
- **GitHub Samples:** [github.com/microsoft/copilot-studio-samples](https://github.com/microsoft/copilot-studio-samples)

---

## Support

### During the Workshop
- Ask your facilitator
- Check the [Participant Reference Card](participant-reference-card.md) for UI guidance
- Review module README files for step-by-step instructions

### After the Workshop
- **Copilot Studio Community forums:** Ask questions, share your agents, get peer support
- **Microsoft Learn documentation:** [learn.microsoft.com/microsoft-copilot-studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/)
- **GitHub Issues:** Report course issues at [github.com/microsoft/agent-academy/issues](https://github.com/microsoft/agent-academy/issues)

---

## Course Credits

- **Source:** Microsoft Agent Academy Recruit Course
- **Original Authors:** Microsoft Copilot Studio team
- **Updated for June 2026 UI:** Workshop modernization project
- **License:** MIT (see repository root)

---

**Ready to build AI agents?** Start with [Module 00: Course Setup](modules/00-course-setup/) →
