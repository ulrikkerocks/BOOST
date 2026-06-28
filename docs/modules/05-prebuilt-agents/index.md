# Module 05: Using Pre-Built Agents

**Codename:** OPERATION HEAD START  
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

You don't always need to build an agent from scratch. Copilot Studio provides **pre-built agent templates** that give you a head start on common scenarios like IT helpdesk, HR support, and sales qualification.

In this module — the workshop's **"Your First Agent"** opener — you'll explore the template gallery, create a quick agent from a template, and customize it. This is your fast hands-on win before you build **Bit** properly from scratch in Module 06.

> 🧭 **This is a quick first agent, not Bit.** The template agent here is a throwaway to get your hands dirty. You'll build **Bit, your Contoso IT help desk buddy** — the agent this course centers on — from a blank canvas in **Module 06**. Keep this template agent around as a reference.

---

## Prerequisites

- A **Copilot Studio** environment in the **new experience** (from [Module 00](../00-course-setup/)).
- For the customization step: the **IT Help Desk** SharePoint site with the **Contoso IT FAQ** ([Module 00](../00-course-setup/)).

> 🏫 **In the facilitated workshop**, this is your first hands-on lab — your environment and SharePoint site are already provisioned, so you can start right here. If you're following along **at the office**, complete [Module 00](../00-course-setup/) first.

---

## What Are Agent Templates?

**Agent templates** are pre-configured agents built by Microsoft and the community. They typically include:
- **Pre-written instructions** — identity and guidance optimized for a scenario
- **Suggested skills** — reusable behaviors for common tasks
- **Knowledge placeholders** — spots for your data (you'll replace these)
- **Suggested tools** — connectors relevant to the scenario
- **Starter prompts** — example questions users can ask

Templates save time by providing a **proven structure** you can adapt to your needs.

---

## Common Agent Templates

As of June 2026, Copilot Studio offers templates for scenarios like:

| Template | Use Case |
|---|---|
| **IT Help Desk** | Password resets, troubleshooting, software requests |
| **HR Support** | Leave policies, benefits, onboarding |
| **Customer Service** | Order status, returns, FAQs |
| **Sales Qualification** | Lead capture, product recommendations, demo scheduling |
| **Facilities Management** | Room bookings, maintenance requests |
| **Finance & Expense** | Expense approvals, budget queries, invoice lookups |
| **Onboarding Assistant** | New employee orientation, checklist tracking |

> **Note:** Microsoft regularly adds new templates. The gallery you see may include additional templates (and exact names may differ).

---

## Lab 5.1: Browse the Template Gallery

**Objective:** Explore available agent templates and understand what each one offers.

### Step 1: Navigate to the Template Gallery

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Sign in with your M365 account (confirm you're in the **new experience**)
3. From the **Home page**, look for an entry point to templates:
   - A **"Start from a template"** section on the Home page
   - An **"Explore templates"** link or button
   - **Create agent** → **From a template**

[SCREENSHOT: Copilot Studio Home page showing a "Start from a template" section with template cards]

### Step 2: Explore Template Details

1. Browse the available templates
2. Select a template card (e.g., **IT Help Desk** or a similar support template)
3. You'll see a preview with a **description**, **key features**, **sample prompts**, and a **preview image**

[SCREENSHOT: Template preview page showing an IT Help Desk template with description, features, and sample prompts]

4. Select **Back** to return to the gallery

### Step 3: Compare Templates

Explore at least three templates (e.g., **IT Help Desk**, **HR Support**, **Customer Service**).

**Reflection questions:**
- How do the **instructions** differ between templates?
- What **skills or starter prompts** are included by default?
- Are there any suggested **knowledge** sources or **tools**?

**✅ Checkpoint:** You've explored the template gallery and understand what each template provides.

---

## Lab 5.2: Create an Agent from a Template

**Objective:** Create an agent using the **IT Help Desk** template and see what it includes.

### Step 1: Select the IT Help Desk Template

1. In the template gallery, locate the **IT Help Desk** (or similar support) template
2. Select the template card
3. Select **Create agent** (or **Use this template**)

[SCREENSHOT: IT Help Desk template preview with a "Create agent" button]

### Step 2: Configure the Agent

1. You may be prompted to customize:
   - **Agent name:** `IT Help Desk Template Demo` (or leave the default)
   - **Language:** select your language
   - **Environment:** verify you're in your developer environment
2. Select **Create** and wait while Copilot Studio provisions the agent (~30 seconds)
3. You land on the **Build page** for the new agent

[SCREENSHOT: Build page for the IT Help Desk agent created from a template]

**✅ Checkpoint:** You've created an agent from the IT Help Desk template.

### Step 3: Review What the Template Includes

Explore the new agent's **Build page** blocks:

#### 3a. Instructions

Read the pre-written **Instructions**. Notice:
- **Clear role definition** — "You are an IT Help Desk assistant…"
- **Scope boundaries** — what the agent can help with
- **Escalation path** — what to do when stuck

> **Tip:** Save this pattern — you'll write similar instructions for Bit in Module 06.

#### 3b. Skills and Starter Prompts

In the **Skills** block (and the agent's starter prompts), see what behaviors the template ships with — common helpdesk tasks like password help or software guidance. In the new experience these are **skills** (markdown behaviors), not topic flows.

[SCREENSHOT: Build page Skills block and starter prompts for the template agent]

#### 3c. Knowledge (Placeholders)

In the **Knowledge** block you may see placeholders for "your IT knowledge base" (not connected yet). Templates don't include **your** organization's knowledge — you add that yourself (next).

#### 3d. Tools

In the **Tools** block you may see suggested connectors (e.g., a ticketing system) as placeholders.

**✅ Checkpoint:** You've reviewed the template agent's instructions, skills, knowledge, and tools.

---

## Lab 5.3: Customize the Template Agent

**Objective:** Adapt the template to Contoso by adding the IT Help Desk SharePoint site as a knowledge source.

### Step 1: Add the IT Help Desk SharePoint Site

1. On the **Build page**, open the **Knowledge** block
2. Select **+ Add knowledge** → **SharePoint**
3. Enter the URL of your **IT Help Desk** site:
   ```text
   https://[yourtenant].sharepoint.com/sites/ITHelpDesk
   ```
4. Select **Add**

[SCREENSHOT: Add knowledge dialog showing SharePoint URL entry]

**✅ Checkpoint:** The agent can now search the IT Help Desk SharePoint site.

### Step 2: Test the Agent

1. In the **Preview pane** (right side), type:
   ```text
   What are the help desk hours?
   ```
2. Press **Enter**
3. The agent should search the IT Help Desk site, find the **Contoso IT FAQ**, and return the hours with a source citation.

[SCREENSHOT: Preview pane showing the response with help desk hours and a source citation]

**✅ Checkpoint:** The template agent successfully uses your organization's knowledge.

### Step 3: Customize the Instructions

1. Open the **Instructions** block and select **Edit**
2. Modify the instructions to reference Contoso:
   ```text
   You are an IT Help Desk assistant for Contoso. You help employees with common IT
   issues. Be polite, concise, and professional.

   You can help with:
   - Password resets
   - VPN and connectivity troubleshooting
   - Software installation requests

   Always search the Contoso knowledge first. If an issue needs admin access, log a
   ticket and hand it to the help desk team.
   ```
3. Select **Save**

**✅ Checkpoint:** The agent's instructions now reference your organization.

---

## When to Use a Template vs. Build from Scratch

| Scenario | Recommendation |
|---|---|
| **Common use case** (IT helpdesk, HR, customer service) | Start with a template |
| **Unique workflow** (custom business process) | Build from scratch |
| **Learning agent authoring** | Try both — templates teach patterns, scratch teaches fundamentals |
| **Tight deadline** | Use a template and customize |
| **Need complete control** | Build from scratch |

**Best practice:** Even if you build from scratch, **review templates for inspiration** — they show you how to write effective instructions, structure knowledge, and pick good starter prompts.

---

## Customizing Templates: What to Change

| Component | What to Customize |
|---|---|
| **Instructions** | Replace the generic company name with yours; add specific guidance |
| **Knowledge** | Add your SharePoint sites, documents, knowledge bases |
| **Skills** | Add/adjust skills to match your processes |
| **Tools** | Connect to your systems (ticketing, email, HR) |
| **Channels** | Publish to your Teams, website, or M365 Copilot |
| **Branding** | Update the agent name, description, icon |

---

## For This Course: Keep It, but Build Bit Fresh

After creating the **IT Help Desk Template Demo**, you have two paths:

- **Keep and customize** the template, or
- **Use it as a reference and build fresh.**

**For this course, build fresh.** Keep the template agent in your environment (don't delete it), and in **Module 06** build **Bit** from a blank canvas. You get both: the learning value of building from scratch *and* a template to reference.

---

## Key Takeaways

- **Templates** provide pre-built agents for common scenarios (IT, HR, sales, etc.)
- **Included:** instructions, suggested skills, knowledge placeholders, suggested tools, starter prompts
- **Not included:** your organization's specific knowledge — you add that
- **Customization is required** — templates are starting points, not finished products
- **Use templates to learn** — even if you build from scratch, they teach best practices

---

## What You've Learned

You now know how to:
- Browse the Copilot Studio template gallery
- Create an agent from a template
- Customize it by adding knowledge and editing instructions
- Decide when to use a template vs. build from scratch

---

## Next Steps

In **Module 06: Build the Contoso Helpdesk Agent**, you'll create **Bit** from a blank canvas — defining his instructions, grounding him with knowledge, and turning on memory. It's the heart of the course and the foundation for everything that follows.

Everything from Modules 01–05 comes together as you build Bit.

---

**Course Navigation:** [← Module 04](../04-creating-a-solution/) | [Course Index](../) | [Next: Module 06 →](../06-build-custom-agent/)
