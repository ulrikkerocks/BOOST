# Module 06: Build a Custom Agent

**Codename:** OPERATION AGENT FORGE  
**Time:** 75 minutes  
**Scenario:** Contoso Helpdesk Agent — Build from Scratch

---

## Learning Objectives

By the end of this module, you will be able to:
- Create a custom agent using natural language description
- Configure agent instructions to define role, tone, and behavior
- Add multiple knowledge sources (SharePoint site, uploaded documents, websites)
- Test an agent with questions across different knowledge sources
- Verify knowledge source attribution in agent responses
- Understand how the AI model selection affects agent performance

## Overview

This is the heart of the course. You'll build the **Contoso Helpdesk Agent** from scratch — a custom agent that helps employees find IT information and request devices.

By the end of this module, your agent will be able to:
- ✅ Answer questions by searching the **Contoso IT SharePoint site**
- ✅ Provide WiFi connection help from an **uploaded document**
- ✅ Look up troubleshooting info from **Microsoft Support articles**
- ✅ Search the **general web** for recent tech news or solutions

This agent will serve as the foundation for all remaining modules, where you'll add topics, adaptive cards, workflows, and event triggers.

---

## The Big Picture

Here's what you'll build across Modules 06–11:

| Module | What You Add |
|---|---|
| **Module 06** (this one) | Base agent + knowledge sources |
| **Module 07** | Topic: Device request with SharePoint data |
| **Module 08** | Adaptive Card displaying device info + images |
| **Module 09** | Agent Flow: Send email when device is requested |
| **Module 10** | Event Trigger: Auto-escalate high-priority tickets |
| **Module 11** | Publish to Microsoft Teams |

Everything starts here in Module 06.

---

## Lab 6.1: Create the Contoso Helpdesk Agent

**Objective:** Use natural language creation to build a new agent.

### Step 1: Navigate to the Copilot Studio Home Page

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Sign in with your M365 account
3. You land on the **Home page**

[SCREENSHOT: Copilot Studio Home page showing the description box: "Describe what you want your agent to do"]

### Step 2: Describe Your Agent

The new Copilot Studio interface lets you **create agents using natural language**. Just describe what you want the agent to do, and AI provisions it for you.

1. In the description box on the Home page, enter:

```
You are an IT Help Desk assistant that helps Contoso employees resolve common IT issues 
and find available devices. Be polite, concise, and helpful. Use the Contoso IT SharePoint 
site as the primary knowledge source. Also search Microsoft Support for troubleshooting 
articles at https://support.microsoft.com.
```

[SCREENSHOT: Home page with the IT helpdesk description entered in the box]

2. Press **Enter** or select **Create**

3. Wait while the AI generates your agent (~10 seconds)

### Step 3: Review AI Suggestions

The AI will suggest:
- **Agent name** (e.g., "IT Help Desk Assistant" or "Contoso IT Agent")
- **Description**
- **Initial instructions** (based on your input)
- **Suggested knowledge sources** (Microsoft Support may appear)
- **Suggested topics** (e.g., "Password Reset," "Device Request")
- **Suggested channels** (e.g., Microsoft Teams)

[SCREENSHOT: AI suggestions panel showing agent name, knowledge sources, and suggested topics]

### Step 4: Accept or Customize Suggestions

1. Review the **Agent name**:
   - If it's close to "Contoso Helpdesk Agent" or "IT Help Desk Assistant," accept it
   - If not, select **Edit** and enter: `Contoso Helpdesk Agent`

2. Review the **Description**:
   - Should be something like: "Helps employees resolve IT issues and request devices"
   - Edit if needed

3. Review the **Knowledge sources**:
   - The AI may have added Microsoft Support
   - Don't add the SharePoint site yet (you'll do that manually in Lab 6.2)

4. Review **Suggested topics**:
   - The AI may suggest topics like "Password Reset" or "Device Request"
   - You can accept these or dismiss them (you'll build custom topics in Module 07)
   - For this lab, **dismiss the topic suggestions** (we'll build topics from scratch later)

5. Review **Suggested channels**:
   - You may see "Microsoft Teams" suggested
   - Don't configure channels yet (you'll do that in Module 11)

6. Select **Create agent** (or **Continue**)

[SCREENSHOT: Final agent creation screen with accepted suggestions]

### Step 5: Land on the Overview Page

After creation, you land on the **Overview page** for the **Contoso Helpdesk Agent**.

[SCREENSHOT: Contoso Helpdesk Agent Overview page showing Details, Instructions, Knowledge, and Test pane]

**✅ Checkpoint:** You've created the Contoso Helpdesk Agent and landed on the Overview page.

---

## Lab 6.2: Configure Agent Instructions

**Objective:** Write clear, comprehensive instructions that define the agent's role, tone, and behavior.

### Step 1: Open the Instructions Editor

1. On the **Overview page**, scroll to the **Instructions** section
2. You'll see the AI-generated instructions based on your initial description
3. Select **Edit**

[SCREENSHOT: Instructions section with Edit button]

### Step 2: Review and Refine Instructions

The AI may have generated something like:

```
You are an IT Help Desk assistant that helps employees resolve common IT issues 
and find available devices. Be polite, concise, and helpful.
```

This is a good start, but let's make it more comprehensive.

### Step 3: Write the Final Instructions

Replace the AI-generated instructions with the following:

```
You are an IT Help Desk assistant for Contoso. Your role is to help employees:
- Resolve common IT issues (password resets, software problems, connectivity)
- Find information about available devices
- Get step-by-step troubleshooting help

## Guidelines

**Tone and Style:**
- Be polite, concise, and professional
- Use simple, non-technical language when possible
- Provide step-by-step instructions for complex tasks

**Knowledge Sources (search in this order):**
1. Contoso IT SharePoint site (primary source for company-specific info)
2. Uploaded documents (WiFi guides, policy docs)
3. Microsoft Support (for general troubleshooting)
4. General web search (for recent tech news or solutions)

**Response Rules:**
- Always cite the source when providing information
- If you find multiple relevant sources, prioritize the Contoso IT site
- If you don't know the answer, admit it and suggest contacting IT support at support@contoso.com
- Do NOT make up information — always ground responses in knowledge sources

**Out of Scope:**
- Do not discuss non-IT topics (HR, finance, etc.)
- Do not share sensitive information like passwords directly in chat — link to documents instead
- Do not approve or deny requests — only provide information and guidance

## Examples of Good Responses

**User:** "What's the WiFi password?"
**Agent:** "The guest WiFi password is GuestPass2026! You can find full connection instructions in the Guest WiFi Connection Guide. [Source: Guest WiFi Connection Guide.docx]"

**User:** "My laptop won't turn on."
**Agent:** "Let's troubleshoot this step by step:
1. Check if the power adapter is firmly connected
2. Try a different power outlet
3. Press and hold the power button for 10 seconds
If it still doesn't turn on, contact IT support. [Source: Microsoft Support - Laptop troubleshooting]"
```

[SCREENSHOT: Instructions editor showing the full instructions above]

### Step 4: Save Instructions

1. Select **Save** (or **Apply**)
2. The instructions are updated

**✅ Checkpoint:** The agent now has comprehensive instructions defining its role, tone, knowledge source priority, and response guidelines.

### Why These Instructions Matter

These instructions:
- **Define the agent's personality** — polite, professional, helpful
- **Establish knowledge source priority** — Contoso IT site first, then fallback sources
- **Set boundaries** — what the agent will and won't do
- **Provide examples** — teach the LLM what "good" looks like
- **Prevent hallucinations** — explicit rule to admit "I don't know" instead of making things up

---

## Lab 6.3: Add Knowledge Sources

**Objective:** Connect the agent to multiple knowledge sources so it can answer a wide range of questions.

You'll add three knowledge sources:
1. **Contoso IT SharePoint site** — Company-specific IT information
2. **Guest WiFi Connection Guide (uploaded document)** — Step-by-step WiFi instructions
3. **Microsoft Support website** — General troubleshooting articles

### Step 1: Add the Contoso IT SharePoint Site

1. On the **Overview page**, scroll to the **Knowledge** section
2. Select **+ Add knowledge**

[SCREENSHOT: Knowledge section with "+ Add knowledge" button]

3. Select **SharePoint**
4. In the SharePoint connection dialog:
   - **Site URL:** Enter the URL of your Contoso IT site (from Module 00):
     ```
     https://[yourtenant].sharepoint.com/sites/ContosoIT
     ```
   - **Description (optional):** `Contoso IT site with devices list and help documents`

[SCREENSHOT: Add SharePoint knowledge source dialog showing URL entry]

5. Select **Add** (or **Connect**)

6. Wait while Copilot Studio indexes the SharePoint site (~30 seconds)

7. The SharePoint site appears in the **Knowledge** section

[SCREENSHOT: Knowledge section showing Contoso IT SharePoint site with green checkmark indicating successful connection]

**✅ Checkpoint:** The agent can now search the Contoso IT SharePoint site (including the Devices list and uploaded documents).

### Step 2: Add the Guest WiFi Guide (Uploaded Document)

Even though the Guest WiFi Guide is stored in the SharePoint site's Documents library, you can **also** upload it directly as a standalone knowledge source. This ensures higher priority and faster retrieval.

1. In the **Knowledge** section, select **+ Add knowledge**
2. Select **Upload files** (or **Files**)
3. Select **Browse** and choose the **Guest WiFi Connection Guide.docx** file (from Module 00)
   - If you didn't save the file locally, download it from SharePoint first:
     1. Go to the Contoso IT site
     2. Open **Documents** library
     3. Download **Guest WiFi Connection Guide.docx**

[SCREENSHOT: Upload files dialog showing file browser]

4. After selecting the file, select **Upload** (or **Add**)

5. Wait while Copilot Studio processes the document (~10 seconds)

6. The document appears in the **Knowledge** section

[SCREENSHOT: Knowledge section showing SharePoint site + Guest WiFi Connection Guide.docx]

**✅ Checkpoint:** The agent can now search the uploaded Guest WiFi guide.

### Step 3: Add Microsoft Support as a Web Knowledge Source

1. In the **Knowledge** section, select **+ Add knowledge**
2. Select **Public websites** (or **Websites**)
3. In the URL field, enter:
   ```
   https://support.microsoft.com
   ```
4. **Description (optional):** `Microsoft Support articles for general troubleshooting`

[SCREENSHOT: Add website knowledge source dialog showing Microsoft Support URL]

5. Select **Add**

6. Copilot Studio will index publicly accessible pages on Microsoft Support

> **Note:** The agent can only access **public pages** on the website. Pages requiring authentication won't be indexed.

**✅ Checkpoint:** The agent can now search Microsoft Support articles.

### Step 4: Enable General Web Search (Optional)

General web search allows the agent to search the public internet for real-time information.

1. In the **Knowledge** section, locate the **General web search** toggle
2. Verify it's **enabled** (toggle should be on/blue)
3. If it's disabled, select the toggle to enable it

[SCREENSHOT: Knowledge section showing "General web search" toggle enabled]

**When to enable web search:**
- ✅ Agent needs recent information (e.g., "What's the latest Windows 11 update?")
- ✅ Agent helps with tech news or product releases
- ❌ Agent handles sensitive/internal topics only (disable web search)
- ❌ You want complete control over sources (disable web search)

**For this course, keep web search enabled.** It allows the agent to answer questions like "What's new in Microsoft Teams?" even if you don't have that info in your knowledge base.

**✅ Checkpoint:** General web search is enabled.

### Summary of Knowledge Sources

Your agent now has **four knowledge sources**:

| Knowledge Source | Type | What It Contains |
|---|---|---|
| **Contoso IT SharePoint site** | SharePoint | Devices list, pages, site documents |
| **Guest WiFi Connection Guide.docx** | Uploaded file | WiFi connection instructions |
| **Microsoft Support** | Website | General troubleshooting articles |
| **General web search** | Internet | Real-time public web results |

---

## Lab 6.4: Test the Agent with Multiple Knowledge Sources

**Objective:** Verify the agent can answer questions from each knowledge source and correctly cites sources.

### Test 1: SharePoint Site (Devices List)

1. In the **Test pane** (right side), select the **New test session** icon (circular arrows) to start fresh
2. Type the following question:
   ```
   Do you have any Dell laptops available?
   ```

3. Press **Enter**

**Expected response:**
- The agent searches the **Devices** list on the Contoso IT SharePoint site
- Returns available Dell laptops (e.g., "Dell Latitude 7430")
- Cites the source: **[Source: Devices list, Contoso IT SharePoint site]**

[SCREENSHOT: Test pane showing response about Dell laptops with source citation]

**✅ Checkpoint:** The agent can search SharePoint list data.

### Test 2: Uploaded Document (WiFi Guide)

1. In the Test pane, type:
   ```
   What's the guest WiFi password?
   ```

2. Press **Enter**

**Expected response:**
- The agent retrieves the password from the **Guest WiFi Connection Guide.docx**
- Returns: `GuestPass2026!`
- Cites the source: **[Source: Guest WiFi Connection Guide.docx]**

[SCREENSHOT: Test pane showing WiFi password response with document source citation]

**✅ Checkpoint:** The agent can search uploaded documents.

### Test 3: Website (Microsoft Support)

1. In the Test pane, type:
   ```
   How do I reset my Windows password?
   ```

2. Press **Enter**

**Expected response:**
- The agent searches **Microsoft Support**
- Returns step-by-step instructions from a Microsoft Support article
- Cites the source: **[Source: support.microsoft.com/...]**

[SCREENSHOT: Test pane showing Windows password reset instructions with Microsoft Support citation]

**✅ Checkpoint:** The agent can search public websites.

### Test 4: General Web Search

1. In the Test pane, type:
   ```
   What's new in Windows 11 version 24H2?
   ```

2. Press **Enter**

**Expected response:**
- The agent searches the **general web**
- Returns recent information about Windows 11 updates
- May cite sources like microsoft.com, tech news sites, etc.

[SCREENSHOT: Test pane showing Windows 11 news with web search source citations]

**✅ Checkpoint:** The agent can use general web search for recent information.

### Test 5: Graceful "I Don't Know"

1. In the Test pane, type:
   ```
   What's the employee parking policy?
   ```

2. Press **Enter**

**Expected response (since parking policy isn't in any knowledge source):**
```
I don't have information about the employee parking policy in the Contoso IT knowledge base. 
This may be an HR topic — I recommend contacting IT support at support@contoso.com or 
checking with HR for parking information.
```

**✅ Checkpoint:** The agent admits when it doesn't know and suggests alternatives (following the instructions).

---

## Lab 6.5: Explore the Activity Map

**Objective:** Understand which knowledge sources the agent is searching for each question.

### Step 1: Open the Activity Map

1. In the **Test pane**, after asking a question, look for the **Activity** or **Details** link (may appear as an expandable section below the response or as a separate panel)

2. If available, select **Activity** or **Show details**

3. The **Activity map** displays:
   - Which knowledge sources were searched
   - How many results were retrieved from each source
   - Which source(s) were used in the final response

[SCREENSHOT: Activity map showing knowledge sources searched: Contoso IT SharePoint (3 results), Guest WiFi Guide (1 result)]

### Step 2: Interpret the Activity Map

**Example for "What's the WiFi password?":**
```
Knowledge Sources Searched:
  ✅ Guest WiFi Connection Guide.docx — 1 result (used)
  ✅ Contoso IT SharePoint site — 0 results
  ⏭️ Microsoft Support — skipped (answer found)
```

**What this tells you:**
- The agent searched the uploaded document first
- Found the answer immediately
- Didn't need to search other sources

**Example for "Do you have Dell laptops?":**
```
Knowledge Sources Searched:
  ✅ Contoso IT SharePoint site (Devices list) — 2 results (used)
  ⏭️ Other sources — skipped (answer found)
```

**Why the Activity map matters:**
- **Debugging** — see why the agent chose a particular source
- **Performance** — identify slow or unresponsive knowledge sources
- **Quality assurance** — verify the agent is searching the right sources

---

## Lab 6.6: Select the AI Model (Optional)

**Objective:** Understand how to change the AI model that powers your agent's reasoning.

### Step 1: View the Current Model

1. On the **Overview page**, locate the **Select your agent's model** section (near the top, below Details)
2. You'll see a dropdown showing the current model (likely **GPT-4.1**)

[SCREENSHOT: "Select your agent's model" dropdown showing GPT-4.1 selected]

### Step 2: Review Available Models

As of June 2026, available models include:
- **GPT-4.1** (default) — Fast, cost-effective, reliable
- **GPT-5** — Advanced reasoning, longer context windows
- **Claude Sonnet 4.5 / 4.6** — Strong citation accuracy, structured tasks
- **Mistral Medium 3.5** — Multilingual, efficient

### Step 3: When to Change the Model

| Scenario | Recommended Model |
|---|---|
| **General use, cost-conscious** | GPT-4.1 (default) |
| **Complex reasoning, multi-step tasks** | GPT-5 or Claude Sonnet 4.6 |
| **Large documents, long context** | GPT-5 (larger context window) |
| **Multilingual support** | Mistral Medium 3.5 |
| **Citation accuracy is critical** | Claude Sonnet 4.5/4.6 |

### Step 4: Experiment (Optional)

If you want to see the difference:

1. Select the **AI model dropdown**
2. Choose a different model (e.g., **GPT-5** or **Claude Sonnet 4.6**)
3. Select **Save** or **Apply**
4. In the **Test pane**, start a **new test session**
5. Ask the same questions you tested in Lab 6.4
6. Compare the responses:
   - Are citations clearer?
   - Are responses more detailed or concise?
   - Is reasoning more step-by-step?

[SCREENSHOT: Test pane showing comparison between GPT-4.1 and GPT-5 responses]

**For this course, GPT-4.1 is recommended.** It's the most cost-effective and performs well for standard IT helpdesk scenarios.

---

## Understanding Agent Settings

Let's explore the agent settings briefly.

### Step 1: Open Agent Settings

1. On the **Overview page**, select the **Settings** icon (gear ⚙️) at the top right
2. Select **Agent settings** (or just **Settings**)

[SCREENSHOT: Settings dropdown showing "Agent settings" option]

### Step 2: Review Settings Categories

**General:**
- **Language** — Set the agent's primary language
- **Time zone** — For scheduling and timestamps

**Advanced:**
- **Schema name** — The technical identifier for this agent (auto-generated, read-only)
- **Solution** — Which solution this agent belongs to (should show **Contoso Helpdesk Agent**)

**Security:**
- **Authentication** — Who can access this agent (if published to web)
- **Data policies** — Compliance and data residency settings

> **For this course**, you don't need to change any settings. Just be aware of where they are.

---

## Verifying the Agent Is in the Solution

Let's confirm the agent was automatically added to the **Contoso Helpdesk Agent** solution (because you set the preferred solution in Module 04).

### Step 1: Open Power Apps Maker Portal

1. Go to [https://make.powerapps.com](https://make.powerapps.com)
2. Sign in with your M365 account
3. Ensure you're in your **developer environment** (top right environment picker)

### Step 2: Navigate to Solutions

1. In the left navigation, select **Solutions**
2. Select **Contoso Helpdesk Agent** from the list

[SCREENSHOT: Solutions list showing Contoso Helpdesk Agent solution]

### Step 3: Verify the Agent Is Listed

1. In the solution, you'll see a list of **Objects**
2. Look for:
   - **Copilot** (or **Chatbot**) → **Contoso Helpdesk Agent**
   - **Connection references** → SharePoint, if applicable

[SCREENSHOT: Contoso Helpdesk Agent solution showing the agent listed under Objects]

**✅ Checkpoint:** The agent is properly packaged in the solution.

---

## Troubleshooting Common Issues

### Issue 1: SharePoint Site Won't Connect

**Symptoms:** Error when adding the SharePoint site as a knowledge source.

**Possible causes:**
- **Permissions** — You don't have access to the site
- **URL typo** — Double-check the URL
- **Site privacy** — Site is private and you're not a member

**Solutions:**
1. Open the SharePoint site in a browser and verify you can access it
2. Add yourself as a site owner/member (via SharePoint site settings)
3. Retry adding the knowledge source

### Issue 2: Agent Doesn't Find Devices List Data

**Symptoms:** Agent says "I don't have information about devices" even though the Devices list exists.

**Possible causes:**
- **Indexing delay** — SharePoint site is still being indexed
- **List permissions** — Devices list is not accessible to the agent
- **Empty list** — No items in the Devices list

**Solutions:**
1. Wait 5–10 minutes for indexing to complete
2. Verify the Devices list has at least 5 sample items (from Module 00)
3. In SharePoint, check list permissions (should be inherited from site)
4. In Copilot Studio, remove and re-add the SharePoint knowledge source

### Issue 3: Agent Hallucinates Instead of Citing Sources

**Symptoms:** Agent provides information without citing a source, or makes up information.

**Possible causes:**
- **Instructions are too permissive** — No explicit rule to cite sources
- **General web search is disabled** — Agent can't find an answer and guesses
- **Knowledge sources not indexed yet**

**Solutions:**
1. Review instructions — ensure "Always cite sources" rule is present
2. Test with a question you **know** the answer is in a knowledge source
3. Check the Activity map to see if knowledge sources were searched
4. Add a stronger instruction: "If no source is found, say 'I don't have this information' — never make up an answer."

---

## Key Takeaways

- **Natural language creation** — Describe what you want; AI provisions the agent
- **Instructions define behavior** — Clear instructions prevent hallucinations and set tone
- **Knowledge sources are prioritized** — Agent searches in the order you specify (or LLM decides)
- **RAG grounds responses** — Every answer should cite a source
- **Activity map shows what happened** — Essential for debugging and quality assurance
- **AI model selection matters** — Choose based on reasoning complexity, cost, and language needs
- **Solutions keep you organized** — All components in one package for easy management

---

## What You've Built

You now have a **production-ready knowledge base agent** that:
- ✅ Searches the Contoso IT SharePoint site (lists, documents, pages)
- ✅ Provides WiFi help from an uploaded guide
- ✅ Searches Microsoft Support for troubleshooting
- ✅ Uses general web search for recent information
- ✅ Cites sources for every answer
- ✅ Admits "I don't know" when appropriate
- ✅ Is packaged in the Contoso Helpdesk Agent solution

---

## Next Steps

In **Module 07: Add a Topic with Triggers**, you'll add a **conversational topic** that lets users request devices from the Devices list. This topic will use:
- Trigger phrases (e.g., "I need a laptop")
- Question nodes to gather requirements
- Power Fx to query the SharePoint Devices list
- Adaptive Cards to display results (Module 08)

The agent you built in Module 06 is the foundation. Now you'll add structured conversation flows on top of the generative knowledge base.

---

**Course Navigation:** [← Module 05](../05-prebuilt-agents/README.md) | [Course Index](../README.md) | [Next: Module 07 →](../07-add-topic-with-triggers/README.md)
