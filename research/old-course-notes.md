# Original Course Notes — Key Content per Module

Extracted from https://github.com/microsoft/agent-academy (docs/recruit/)
Researched: June 16, 2026

---

## Module 00: Course Setup

**Time:** 30 min
**Codename:** OPERATION DEPLOYMENT READY

Steps:
1. Get M365 account (Business Basic trial or existing)
2. Start Copilot Studio trial (aka.ms/TryCopilotStudio)
3. Create Power Apps Developer environment
4. Enable publishing (Copilot Studio Authors role in PPAC via security group)
5. Create SharePoint site (IT Help Desk template → "Contoso IT")
6. Populate Devices list with sample data + Image column

Scenario setup: Contoso IT helpdesk throughout the course.

---

## Module 01: Introduction to Agents

**Codename:** OPERATION FIRST CONTACT

Covers:
- What is an agent? (conversational AI, LLM + RAG + orchestration)
- Declarative agents (extend M365 Copilot)
- Custom/autonomous agents (built in Copilot Studio)
- Spectrum: rule-based → generative → autonomous

---

## Module 02: Copilot Studio Fundamentals

**Codename:** OPERATION CORE PROTOCOL
**Time:** 30 min

Four building blocks:
1. **Knowledge** — instruction context + knowledge sources (SharePoint, websites, files)
2. **Tools (Actions)** — what the agent can DO (connectors, flows, APIs)
3. **Topics** — conversational triggers / entry points + dialog flows
4. **Instructions** — role, persona, response guidelines, memory/context rules

How they work together: orchestrator → listens for topic → applies instructions → leverages knowledge → calls tools

---

## Module 03: Create a Declarative Agent for M365 Copilot

Creates an M365 Copilot agent (extends M365 Copilot chat).
Uses natural language grounded prompt.

---

## Module 04: Creating a Solution

**Codename:** Solution packaging
- Create solution publisher in PPAC
- Create new solution
- Set as preferred solution in Copilot Studio (Settings → Advanced)
- All subsequent agents/components go into this solution

Agents created in: **Contoso Helpdesk Agent** solution.

---

## Module 05: Using Pre-Built Agents

- Browse agent templates
- Use IT Help Desk template or similar
- Customize from a starting point vs. building from scratch

---

## Module 06: Build a Custom Agent

**Codename:** OPERATION AGENT FORGE
**Time:** 75 min
**Agent name:** Contoso Helpdesk Agent

Labs:
- 6.1: Natural language creation — describe IT helpdesk agent → AI provisions
- 6.2: Add SharePoint site as knowledge source (Contoso IT)
- 6.3: Add uploaded document (Guest WiFi Connection Guide .docx)
- 6.4: Test with 4 questions across all knowledge sources

Key prompt used in creation:
```
You are an IT Help Desk assistant that helps employees resolve common IT issues
and find available devices. Be polite, concise, and helpful. Use Microsoft Support
as the primary source: https://support.microsoft.com [...]
```

---

## Module 07: Add a Topic with Triggers

Creates a new topic in the Contoso Helpdesk Agent.
- Topic for device requests (using Devices SharePoint list)
- Trigger phrases + question nodes
- Power Fx to query SharePoint data
- Adaptive Card display of results

> Note: This module uses the Devices list from Module 00.

---

## Module 08: Enhance with Adaptive Cards

- Build Adaptive Card within topic node
- Uses Power Fx to bind SharePoint data
- Custom card layout (device image, fields)
- Integration with Devices SharePoint list + Image column (added in Module 00)

---

## Module 09: Automate with Agent Flows

- Uses Adaptive Card input from Module 08
- Creates Agent Flow (Power Automate-style) as a tool
- Flow triggered from agent topic
- Back-end action (e.g., create record, send email)

---

## Module 10: Add Event Triggers

- Makes agent autonomous (proactive, not just reactive)
- Event-based trigger (Dataverse row change, schedule, etc.)
- Frontier program note (for MCP integration)
- Agent acts without direct user input

---

## Module 11: Publish Your Agent

- Publish agent from Copilot Studio
- Deploy to Microsoft Teams
- Deploy to Microsoft 365 Copilot (requires M365 Copilot license)
- Test published agent in Teams

---

## Module 12: Understanding Licensing

- Copilot Studio trial (30 days, extendable)
- Standalone Copilot Studio subscription
- M365 Copilot license requirement for M365 Copilot channel
- Billing: messages-based or capacity packs
- Power Apps Developer Plan (free dev environment)

---

## Module 13: Secure Your Recruit Badge

- Completion checklist
- Badge claim instructions
- Community links

---

## Scenario Thread Through the Course

All hands-on labs build ONE agent:
- **Agent:** Contoso Helpdesk Agent
- **Data source:** Contoso IT SharePoint site (from Module 00)
- **Devices list:** Used in Modules 07, 08, 09
- **Solution:** Contoso Helpdesk Agent solution (created Module 04, used throughout)
- **Final state:** Published to Teams with topics, adaptive cards, flows, and event triggers

This connected scenario is a strength of the course. Preserve it in the updated version.
