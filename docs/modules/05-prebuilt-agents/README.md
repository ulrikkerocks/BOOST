---
title: "05 · Using Pre-Built Agents"
parent: Course Modules
nav_order: 5
---
# Module 05: Using Pre-Built Agents

**Time:** 20 minutes  
**Scenario:** Agent Templates and Starting Points

---

## Learning Objectives

By the end of this module, you will be able to:
- Browse the Copilot Studio agent template gallery
- Identify common agent templates and their use cases
- Create an agent from a template
- Customize a template-based agent for your organization
- Decide when to use a template vs. build from scratch

## Overview

You don't always need to build an agent from scratch. Copilot Studio provides **pre-built agent templates** that give you a head start on common scenarios like IT helpdesk, HR support, sales qualification, and more.

In this module, you'll explore the template gallery, create an agent from a template, and learn how to customize it. This will prepare you for **Module 06**, where you'll build a custom agent from the ground up.

> **Note:** Templates are a great way to learn how experienced builders structure agents. Even if you plan to build custom agents, reviewing templates can teach you best practices for instructions, topic flows, and knowledge integration.

---

## What Are Agent Templates?

**Agent templates** are pre-configured agents built by Microsoft and the community. They include:
- **Pre-written instructions** — system prompts optimized for specific scenarios
- **Sample topics** — conversational flows for common tasks
- **Knowledge sources** — placeholders for your data (you'll replace these)
- **Suggested tools** — connectors and flows relevant to the scenario
- **Starter prompts** — example questions users can ask

Templates save time by providing a **proven structure** you can adapt to your needs.

---

## Common Agent Templates

As of June 2026, Copilot Studio offers templates for scenarios like:

| Template | Use Case |
|---|---|
| **IT Help Desk** | Password resets, device requests, troubleshooting |
| **HR Support** | Leave policies, benefits, onboarding |
| **Customer Service** | Order status, returns, FAQs |
| **Sales Qualification** | Lead capture, product recommendations, demo scheduling |
| **Facilities Management** | Room bookings, maintenance requests |
| **Finance & Expense** | Expense approvals, budget queries, invoice lookups |
| **Onboarding Assistant** | New employee orientation, checklist tracking |

> **Note:** Microsoft regularly adds new templates. The gallery you see may include additional templates not listed here.

---

## Lab 5.1: Browse the Template Gallery

**Objective:** Explore available agent templates and understand what each one offers.

### Step 1: Navigate to the Template Gallery

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Sign in with your M365 account
3. You land on the **Home page**

4. Look for one of the following entry points to templates:
   - **"Start from a template"** section on the Home page
   - **"Explore templates"** link or button
   - **"Create agent"** → Select **"From a template"**

[SCREENSHOT: Copilot Studio Home page showing "Start from a template" section with template cards]

### Step 2: Explore Template Details

1. Browse the available templates
2. Select a template card (e.g., **IT Help Desk**)
3. You'll see a preview page with:
   - **Description** — what the agent does
   - **Key features** — topics and capabilities included
   - **Sample prompts** — example questions users can ask
   - **Preview screenshot** — what the agent looks like in action

[SCREENSHOT: Template preview page showing IT Help Desk template with description, features, and sample prompts]

4. Select **Back** to return to the gallery

### Step 3: Compare Templates

Explore at least three templates:
- **IT Help Desk** (relevant to this course)
- **HR Support** (see how HR-specific instructions differ)
- **Customer Service** (see retail/e-commerce patterns)

**Reflection questions:**
- How do the instructions differ between templates?
- What topics are included by default?
- Are there any suggested knowledge sources?

**✅ Checkpoint:** You've explored the template gallery and understand what each template provides.

---

## Lab 5.2: Create an Agent from a Template

**Objective:** Create an agent using the **IT Help Desk** template and see what it includes.

### Step 1: Select the IT Help Desk Template

1. In the template gallery, locate the **IT Help Desk** template
2. Select the template card
3. Select **Create agent** (or **Use this template**)

[SCREENSHOT: IT Help Desk template preview with "Create agent" button]

### Step 2: Configure the Agent

1. You may be prompted to customize the agent:
   - **Agent name:** `IT Help Desk Template Demo` (or leave default)
   - **Language:** Select your language
   - **Environment:** Verify you're in your developer environment

2. Select **Create**

3. Wait while Copilot Studio provisions the agent (~30 seconds)
4. You land on the **Overview page** for the new agent

[SCREENSHOT: Overview page for the IT Help Desk agent created from template]

**✅ Checkpoint:** You've created an agent from the IT Help Desk template.

### Step 3: Review the Agent Components

Now explore what the template includes.

#### 3a. Review Instructions

1. On the **Overview page**, scroll to the **Instructions** section
2. Select **Edit** (or expand to read)
3. Review the pre-written instructions

**Example instructions from IT Help Desk template:**
```
You are an IT Help Desk assistant that helps employees with common IT issues. 
Be polite, concise, and professional. 

You can help with:
- Password resets
- Software installation guidance
- Hardware troubleshooting
- Device requests

If you cannot resolve an issue, escalate to IT support at support@contoso.com.
```

Notice:
- **Clear role definition** — "You are an IT Help Desk assistant"
- **Scope boundaries** — what the agent can help with
- **Escalation path** — what to do when stuck

> **Tip:** Save this pattern. You'll use similar instructions in Module 06.

#### 3b. Review Topics

1. Scroll to the **Topics** section on the Overview page
2. Select **See all** to view the full topic list
3. You may see topics like:
   - **Password Reset** — guides users through password recovery
   - **Device Request** — helps users request new hardware
   - **Software Install** — provides installation instructions

[SCREENSHOT: Topics list showing Password Reset, Device Request, and Software Install topics]

4. Select one topic (e.g., **Password Reset**) to open the topic designer
5. Review the conversation flow:
   - **Trigger phrases** — "reset my password," "forgot password," etc.
   - **Question nodes** — asking for user confirmation
   - **Message nodes** — providing instructions
   - **Condition nodes** — branching logic

[SCREENSHOT: Topic designer showing Password Reset topic flow]

6. Select **Back** or close the topic to return to the Overview page

#### 3c. Review Knowledge (Placeholders)

1. Scroll to the **Knowledge** section
2. You may see:
   - Placeholder references to **"Your IT knowledge base"** (not connected yet)
   - General web search (enabled by default)

Templates don't include **your organization's specific knowledge sources** — you need to add those yourself.

#### 3d. Review Tools

1. Scroll to the **Tools** section
2. You may see suggested tools or placeholders (e.g., "Add a connector to your ticketing system")

**✅ Checkpoint:** You've reviewed the agent's instructions, topics, knowledge, and tools.

---

## Lab 5.3: Customize the Template Agent

**Objective:** Adapt the template to your organization by adding the Contoso IT SharePoint site as a knowledge source.

### Step 1: Add the Contoso IT SharePoint Site

1. On the **Overview page**, scroll to the **Knowledge** section
2. Select **+ Add knowledge**
3. Select **SharePoint**
4. Enter the URL of your **Contoso IT** site:
   ```
   https://[yourtenant].sharepoint.com/sites/ContosoIT
   ```
5. Select **Add**

[SCREENSHOT: Add knowledge dialog showing SharePoint URL entry]

6. The SharePoint site is added as a knowledge source

**✅ Checkpoint:** The agent can now search the Contoso IT SharePoint site.

### Step 2: Test the Agent

1. In the **Test pane** (right side), type:
   ```
   What's the guest WiFi password?
   ```

2. Press **Enter**

3. The agent should:
   - Search the Contoso IT SharePoint site
   - Find the **Guest WiFi Connection Guide.docx**
   - Return the password: `GuestPass2026!`

[SCREENSHOT: Test pane showing response with WiFi password and source citation]

**✅ Checkpoint:** The template agent successfully uses your organization's knowledge.

### Step 3: Customize the Instructions

1. Scroll to the **Instructions** section
2. Select **Edit**
3. Modify the instructions to reference Contoso:
   ```
   You are an IT Help Desk assistant for Contoso. You help employees with common IT issues.
   Be polite, concise, and professional.

   You can help with:
   - Password resets
   - Software installation guidance
   - Hardware troubleshooting
   - Device requests (search the Devices list on the Contoso IT SharePoint site)

   Always search the Contoso IT SharePoint site for answers before responding.
   If you cannot resolve an issue, escalate to IT support at support@contoso.com.
   ```

4. Select **Save**

**✅ Checkpoint:** The agent's instructions now reference your organization.

---

## When to Use a Template vs. Build from Scratch

| Scenario | Recommendation |
|---|---|
| **Common use case** (IT helpdesk, HR support, customer service) | Start with a template |
| **Unique workflow** (custom business process) | Build from scratch |
| **Learning agent authoring** | Try both — templates teach patterns, scratch teaches fundamentals |
| **Tight deadline** | Use a template and customize |
| **Need complete control** | Build from scratch |

**Best practice:** Even if you build from scratch, **review templates for inspiration**. They show you:
- How to write effective instructions
- Common topic patterns (e.g., form-based flows for requests)
- How to structure knowledge sources
- Starter prompts that guide users

---

## Customizing Templates: What to Change

When you use a template, you'll typically customize:

| Component | What to Customize |
|---|---|
| **Instructions** | Replace generic company name with yours, add specific policies |
| **Knowledge** | Add your SharePoint sites, documents, knowledge bases |
| **Topics** | Add/remove topics, edit flows to match your process |
| **Tools** | Connect to your systems (ticketing, CRM, HR systems) |
| **Channels** | Publish to your Teams, website, or mobile app |
| **Branding** | Update agent name, description, icon |

---

## Template Lifecycle: Keep or Replace?

After creating the **IT Help Desk Template Demo**, you have two options:

### Option A: Keep and Customize
- Continue building on this template
- Add more topics, knowledge, tools
- Publish to Teams when ready

### Option B: Use as Reference, Build Fresh
- Keep the template agent for reference
- Create a **new blank agent** in Module 06
- Apply what you learned from the template

**For this course**, we recommend **Option B**:
- Keep the template agent in your environment (don't delete it)
- In Module 06, you'll build the **Contoso Helpdesk Agent** from scratch
- This gives you both: the learning experience of building from scratch **and** a template to reference

---

## Key Takeaways

- **Templates** provide pre-built agents for common scenarios (IT, HR, sales, etc.)
- **Included:** Instructions, topics, knowledge placeholders, suggested tools
- **Not included:** Your organization's specific knowledge sources — you add those
- **Customization is required** — templates are starting points, not finished products
- **Use templates to learn** — even if you build from scratch, templates teach best practices

---

## Template vs. Scratch: A Real Example

Let's compare building the same agent both ways:

### From Template (IT Help Desk)
- ✅ Pre-written instructions with IT helpdesk role definition
- ✅ Topics for password reset, device request, software install
- ✅ Suggested escalation flow
- ⚠️ Still need to add your SharePoint site, customize instructions, edit topics
- **Time saved:** ~30 minutes (instructions and topics already structured)

### From Scratch (What you'll do in Module 06)
- ✅ Full control over every instruction, topic, flow
- ✅ Learn exactly how each component works
- ✅ Understand design decisions (why structure it this way?)
- ⚠️ More time upfront
- **Learning value:** Higher — you build the mental model

**Bottom line:** Templates are great for production speed. Building from scratch is great for learning.

---

## What You've Learned

You now know how to:
- Browse the Copilot Studio template gallery
- Create an agent from a template
- Customize a template by adding knowledge sources and editing instructions
- Decide when to use a template vs. build from scratch
- Use templates as learning resources (even if you build custom agents)

---

## Next Steps

In **Module 06: Build a Custom Agent**, you'll create the **Contoso Helpdesk Agent** from scratch using natural language creation. This is the longest lab in the course (75 minutes) and the foundation for all subsequent modules.

Everything you learned in Modules 01–05 comes together in Module 06. You'll see how the four building blocks (knowledge, tools, topics, instructions) work together to create an intelligent agent.

---

**Course Navigation:** [← Module 04](../04-creating-a-solution/README.md) | [Course Index](../README.md) | [Next: Module 06 →](../06-build-custom-agent/README.md)
