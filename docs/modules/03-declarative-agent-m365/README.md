# Module 03: Create a Declarative Agent for M365 Copilot

**Time:** 25 minutes  
**Scenario:** Extending Microsoft 365 Copilot

---

## Learning Objectives

By the end of this module, you will be able to:
- Explain what a declarative agent is and when to use one
- Create a declarative agent that extends Microsoft 365 Copilot
- Add knowledge sources using a grounded prompt approach
- Publish a declarative agent to the M365 Copilot interface
- Invoke your agent from within M365 Copilot using `@mention`

## Overview

Declarative agents are lightweight extensions for **Microsoft 365 Copilot**. They add domain-specific knowledge and capabilities to the M365 Copilot chat experience without requiring users to leave their workflow.

In this module, you'll create a simple declarative agent that M365 Copilot users can invoke with an `@mention` — for example, `@IT Support` — to get answers grounded in your organization's IT knowledge.

> **Note:** This module requires a **Microsoft 365 Copilot license**. If you don't have one, you can read through the steps to understand the concepts, then proceed to Module 04.

---

## What Is a Declarative Agent?

A **declarative agent** is a specialized agent that:
- **Extends M365 Copilot** — appears as an `@mentionable` entity in the M365 Copilot chat
- **Is defined declaratively** — uses a JSON manifest (no visual designer)
- **Adds custom knowledge** — grounds M365 Copilot in your organization's specific data
- **Has limited capabilities** — can search knowledge and respond conversationally, but can't trigger workflows or use complex multi-step topics

### Declarative vs. Custom Agents

| Feature | Declarative Agent | Custom Agent |
|---|---|---|
| **Where it appears** | Inside M365 Copilot chat | Standalone (Teams, web, mobile) |
| **How users invoke it** | `@mention` (e.g., `@HR Policy`) | Direct chat in Teams or website |
| **Capabilities** | Knowledge grounding + simple instructions | Full capabilities (topics, flows, tools, adaptive cards) |
| **Authoring** | JSON manifest | Visual designer in Copilot Studio |
| **License requirement** | M365 Copilot | Copilot Studio (or trial) |
| **Best for** | Extending M365 Copilot with domain knowledge | Standalone agents with complex workflows |

### When to Use Declarative Agents

Use a declarative agent when:
- Your users already have **M365 Copilot licenses**
- You want to add domain-specific knowledge to M365 Copilot (e.g., HR policies, product docs, legal guidelines)
- The use case is **simple Q&A** — no multi-step workflows or complex forms
- You want to minimize user context switching (stay inside M365 Copilot)

**Example scenarios:**
- **HR Policy Agent** — `@HR Policy what is the parental leave policy?`
- **Product Docs Agent** — `@Product Docs how do I configure SSO for our app?`
- **Legal Compliance Agent** — `@Legal what are the data retention requirements for customer emails?`

---

## Lab 3.1: Create a Declarative Agent

**Objective:** Build a declarative agent that extends M365 Copilot with IT support knowledge.

### Step 1: Navigate to the Copilot Studio Home Page

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Sign in with your M365 account
3. You land on the **Home page**

[SCREENSHOT: Copilot Studio Home page with "Describe what you want your agent to do" prompt box]

### Step 2: Create a New Declarative Agent

1. On the Home page, look for the agent type selector
   - You may see options: **Custom agent** vs. **Declarative agent**
   - Select **Declarative agent**

> **Note:** If you don't see a "Declarative agent" option, you may need to use the declarative agent creation flow directly from the M365 admin center or Teams admin center. The exact entry point may vary depending on your environment. If this option is not visible, skip to the "Alternative: Create via Teams Admin Center" section below.

2. Enter a name for your agent: `IT Support Assistant`

3. In the **Description** field, enter:
   ```
   An IT support agent that helps employees resolve common IT issues and find information 
   from the Contoso IT SharePoint site.
   ```

4. Select **Create**

[SCREENSHOT: Declarative agent creation dialog with name and description fields]

### Step 3: Configure the Agent's Instructions

Declarative agents use **instructions** (a system prompt) to define their behavior.

1. You'll land on a configuration page or manifest editor
2. Locate the **Instructions** field (may be labeled "Grounded prompt" or "System message")
3. Enter the following instructions:

```
You are an IT Support Assistant for Contoso. Your role is to help employees:
- Find answers to common IT questions
- Troubleshoot basic technical issues
- Locate IT resources and documentation

Guidelines:
- Be polite, concise, and helpful
- Search the Contoso IT SharePoint site for answers
- If you don't know the answer, suggest contacting IT support at support@contoso.com
- Cite sources when providing information
- Do not discuss topics outside of IT support
```

[SCREENSHOT: Instructions field showing the system prompt above]

4. Select **Save** or **Continue**

### Step 4: Add a Knowledge Source

Declarative agents can be grounded in knowledge sources just like custom agents.

1. Locate the **Knowledge** section (may be labeled "Data sources" or "Connections")
2. Select **+ Add knowledge** (or similar)
3. Choose **SharePoint**
4. Enter the URL of the **Contoso IT** SharePoint site you created in Module 00:
   ```
   https://[yourtenant].sharepoint.com/sites/ContosoIT
   ```
5. Select **Add** or **Connect**

[SCREENSHOT: Add knowledge source dialog showing SharePoint URL entry]

6. The SharePoint site is added as a knowledge source
7. The agent will now be able to search documents, pages, and lists on that site

> **Note:** You can also add specific documents, websites, or other knowledge sources. For this lab, the SharePoint site is sufficient.

### Step 5: Publish the Declarative Agent

1. Select **Publish** (top right) or **Save and publish**
2. In the publish confirmation dialog, select **Publish**
3. Wait while the agent is published (~30 seconds)
4. You'll see a confirmation: "Your agent is now available in Microsoft 365 Copilot"

[SCREENSHOT: Publish confirmation dialog showing success message]

**✅ Checkpoint:** Your declarative agent is published and available in M365 Copilot.

---

## Lab 3.2: Test the Declarative Agent in M365 Copilot

**Objective:** Invoke the declarative agent from Microsoft 365 Copilot and verify it can answer IT questions.

### Step 1: Open Microsoft 365 Copilot

1. Go to [https://copilot.microsoft.com](https://copilot.microsoft.com) (M365 Copilot web interface)
2. Or open **Microsoft Teams** → select **Copilot** from the left sidebar

[SCREENSHOT: M365 Copilot interface with chat input box]

### Step 2: Invoke Your Declarative Agent

1. In the M365 Copilot chat, type `@`
2. You should see a list of available agents, including **IT Support Assistant**
3. Select **IT Support Assistant** from the list (or continue typing `@IT Support Assistant`)

[SCREENSHOT: M365 Copilot showing @mention dropdown with IT Support Assistant agent]

4. Type a question after the `@mention`:
   ```
   @IT Support Assistant What's the guest WiFi password?
   ```

5. Press **Enter**

### Step 3: Review the Response

The agent should:
- Search the **Contoso IT** SharePoint site
- Find the **Guest WiFi Connection Guide.docx** document
- Return the password: `GuestPass2026!`
- Cite the source document

[SCREENSHOT: M365 Copilot response showing the answer with source citation]

**Example response:**
```
The guest WiFi password is **GuestPass2026!**

Source: Guest WiFi Connection Guide.docx (Contoso IT SharePoint site)
```

**✅ Checkpoint:** The declarative agent successfully answered the question using the SharePoint knowledge source.

### Step 4: Test with Another Question

1. Ask a second question:
   ```
   @IT Support Assistant How do I connect to the VPN?
   ```

2. If you haven't created a VPN guide document, the agent should respond:
   ```
   I don't have specific information about VPN connection steps in the knowledge base. 
   Please contact IT support at support@contoso.com for assistance.
   ```

This demonstrates that the agent:
- Searches knowledge sources first
- Admits when it doesn't know (doesn't hallucinate)
- Follows the instructions to suggest contacting IT support

**✅ Checkpoint:** The agent handles unknown questions gracefully.

---

## Alternative: Create via Teams Admin Center

If the declarative agent option is not visible in Copilot Studio, you can create it via the **Teams admin center**:

1. Go to [https://admin.teams.microsoft.com](https://admin.teams.microsoft.com)
2. In the left navigation, select **Teams apps** → **Manage apps**
3. Select **+ New app** → **Copilot declarative agent**
4. Follow the prompts to configure the agent (name, instructions, knowledge sources)
5. Publish the agent to make it available in M365 Copilot

> **Note:** The exact steps may vary depending on your tenant configuration and admin permissions. Consult your M365 admin if you encounter issues.

---

## How Declarative Agents Work

Under the hood, a declarative agent is defined by a **JSON manifest** that specifies:
- **Name and description**
- **Instructions** (system prompt)
- **Knowledge sources** (SharePoint sites, documents, etc.)
- **Invocation name** (the `@mention` users type)

When a user invokes the agent:
1. M365 Copilot routes the message to your declarative agent
2. The agent searches the configured knowledge sources
3. The agent generates a response grounded in the retrieved content
4. The response appears in the M365 Copilot chat

**Key difference from custom agents:** Declarative agents run **inside** M365 Copilot's interface, not as standalone chat experiences.

---

## Limitations of Declarative Agents

Declarative agents are intentionally simple. They **cannot**:
- Use visual topic flows (no conversation designer)
- Call tools or connectors (no workflows, no API calls)
- Display adaptive cards
- Have multi-step forms or conditional branching
- Be published to channels other than M365 Copilot

**If you need these capabilities**, build a **custom agent** instead (which you'll do starting in Module 06).

---

## When to Use Declarative vs. Custom Agents

Use this decision tree:

```
Do your users have M365 Copilot licenses?
├─ Yes → Is the use case simple Q&A with knowledge grounding?
│         ├─ Yes → Build a declarative agent
│         └─ No (need workflows, forms, etc.) → Build a custom agent
└─ No → Build a custom agent and publish to Teams or web
```

**Example mapping:**

| Use Case | Agent Type |
|---|---|
| HR policy Q&A for M365 users | Declarative |
| IT helpdesk with device request forms | Custom |
| Product docs Q&A for M365 users | Declarative |
| Customer support chatbot on public website | Custom |
| Autonomous ticket escalation agent | Custom (event-triggered) |

---

## Key Takeaways

- **Declarative agents** extend M365 Copilot with custom knowledge and instructions
- **Invoked via `@mention`** — users stay inside the M365 Copilot chat
- **Simple Q&A use cases** — no multi-step workflows or complex forms
- **Grounded in knowledge** — SharePoint sites, documents, websites
- **Requires M365 Copilot license** for end users
- **JSON manifest-based** — no visual designer (unlike custom agents)

---

## Real-World Use Cases

Organizations use declarative agents to:

1. **HR Support** — `@HR Policy` answers questions about benefits, leave, expense policies
2. **Legal Compliance** — `@Legal` provides guidance on contracts, NDAs, data retention
3. **Product Documentation** — `@Product Docs` helps engineers find API references, config guides
4. **Sales Enablement** — `@Sales Playbook` surfaces competitive intel, pitch decks, objection handling
5. **IT Troubleshooting** — `@IT Support` (what you just built!) helps with password resets, WiFi, VPN

---

## Next Steps

Now that you've created a declarative agent, you'll shift focus to **custom agents** — the powerful, full-featured agents that give you complete control over conversational flows, tools, and publishing channels.

But first, in **Module 04: Creating a Solution**, you'll set up proper **solution packaging** so all your work is organized, version-controlled, and ready for ALM (Application Lifecycle Management).

---

**Course Navigation:** [← Module 02](../02-copilot-studio-fundamentals/README.md) | [Course Index](../README.md) | [Next: Module 04 →](../04-creating-a-solution/README.md)
