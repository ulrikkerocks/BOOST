# Module 09: Automate with Agent Flows

**Time:** 50 minutes  
**Scenario:** Send Email When Device is Requested

---

## Learning Objectives

By the end of this module, you will be able to:
- Explain the difference between Agent Flows and Workflows
- Create an Agent Flow that sends an email
- Call an Agent Flow from a topic using a tool node
- Pass data from a topic to a flow using input parameters
- Test an Agent Flow end-to-end from the agent conversation

## Overview

In Modules 07 and 08, you built a topic that displays available devices in Adaptive Cards. Now you'll add automation: when a user selects "Request this device," the agent will trigger an **Agent Flow** that sends an email to IT with the request details.

This demonstrates how agents can **take action** — not just respond with information, but execute real-world tasks like sending notifications, creating records, or updating databases.

---

## 🆕 What's New: Workflows (Early Release)

> **Important:** Before we begin, let's clarify the automation landscape in Copilot Studio as of June 2026.

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

### How to Tell Which Experience You're In

**Agent Flows environment:**
- Left sidebar shows: **Flows**
- Creating a new flow: "New Agent flow" in the topic node

**Workflows environment (early release):**
- Left sidebar shows: **Flows** AND **Workflows**
- You can create either; for this lab, use **Flows** → **New Agent flow**

---

## Lab 9.1: Create an Agent Flow

**Objective:** Build an Agent Flow that sends an email notification when a device is requested.

### Step 1: Open the Device Request Topic

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Navigate to **Agents** → **Contoso Helpdesk Agent**
3. On the Overview page, select **Topics** → **See all**
4. Select the **Device Request** topic

[SCREENSHOT: Topic designer showing the Device Request topic flow]

### Step 2: Locate the Adaptive Card Node

Recall from Module 08:
- **Adaptive Card node** displays available devices
- Each card has a **"Request this device"** button with `Action.Submit`

We'll add a node **after** the Adaptive Card that calls an Agent Flow when the button is clicked.

### Step 3: Add a Tool Node to Call an Agent Flow

1. Below the **Adaptive Card** node, select **+ Add node**
2. Select **Call a tool** (or **Call an action**)

[SCREENSHOT: Add node menu showing "Call a tool" option]

3. A **Tool** node (or **Action** node) is added

[SCREENSHOT: Tool node on the canvas]

### Step 4: Create a New Agent Flow

1. In the **Tool** node, locate the **Select a tool** dropdown (or **Select an action**)
2. Select **Create a flow** (or **+ New Agent Flow**)

[SCREENSHOT: Tool node showing "Create a flow" option]

3. A new browser tab or side panel opens with the **Agent Flow designer**

[SCREENSHOT: Agent Flow designer showing blank Power Automate-style canvas]

4. You're now in the flow authoring experience (Power Automate-style)

### Step 5: Configure the Flow Trigger

Every Agent Flow starts with a trigger: **When an agent is invoked**.

1. You should see a trigger node at the top: **When Copilot Studio calls a flow** (or similar)
2. This trigger is automatically configured — no changes needed

[SCREENSHOT: Flow trigger node "When Copilot Studio calls a flow"]

### Step 6: Add Input Parameters

Input parameters are data passed **from the topic to the flow**. We'll pass the device title and user's name.

1. In the trigger node, locate **Add an input** (or **+ Add input**)
2. Select **Text**
3. **Input name:** `DeviceTitle`
4. **Description (optional):** `The title of the device being requested`

[SCREENSHOT: Trigger node showing "Add an input" with DeviceTitle text input]

5. Repeat to add a second input:
   - **Type:** Text
   - **Input name:** `UserName`
   - **Description:** `The name of the user requesting the device`

**✅ Checkpoint:** The flow trigger has two text inputs: `DeviceTitle` and `UserName`.

### Step 7: Add an Email Action

1. Below the trigger, select **+ New step**
2. Search for **Outlook** (or **Office 365 Outlook**)
3. Select **Send an email (V2)**

[SCREENSHOT: Flow action search showing "Outlook" with "Send an email (V2)" action]

4. The **Send an email** action is added

[SCREENSHOT: Send an email action on the canvas]

### Step 8: Configure the Email

1. In the **Send an email** action, configure the following fields:

| Field | Value |
|---|---|
| **To** | `support@contoso.com` (or your email for testing) |
| **Subject** | `Device Request: [Dynamic content: DeviceTitle]` |
| **Body** | See below |

**Email body template:**
```
A device request has been submitted:

Device: [Dynamic content: DeviceTitle]
Requested by: [Dynamic content: UserName]

Please process this request and contact the user.

--- 
Sent by Contoso Helpdesk Agent
```

**To insert dynamic content:**
- Position your cursor where you want the dynamic value
- Select the **Dynamic content** icon (lightning bolt)
- Select **DeviceTitle** or **UserName** from the list

[SCREENSHOT: Send an email action showing dynamic content inserted into Subject and Body fields]

2. Select **Save** (top right of the flow designer)

3. The flow is saved and automatically connected to your Copilot Studio agent

**✅ Checkpoint:** The Agent Flow sends an email with device request details.

### Step 9: Name the Flow

1. At the top of the flow designer, locate the flow name (default: "Untitled")
2. Rename it to: `Send Device Request Email`

[SCREENSHOT: Flow designer toolbar showing flow name "Send Device Request Email"]

3. Select **Save** again

4. Close the flow designer tab or panel to return to the topic designer

**✅ Checkpoint:** The Agent Flow is created and named.

---

## Lab 9.2: Call the Agent Flow from the Topic

**Objective:** Wire the tool node in the topic to pass data to the flow.

### Step 1: Select the Flow in the Tool Node

1. Back in the **Device Request** topic designer, locate the **Tool** node (added in Lab 9.1, Step 3)
2. In the **Select a tool** dropdown, you should now see **Send Device Request Email** (the flow you just created)
3. Select it

[SCREENSHOT: Tool node showing "Send Device Request Email" selected]

### Step 2: Map Input Parameters

The tool node now shows the two input parameters you defined in the flow: **DeviceTitle** and **UserName**.

1. **DeviceTitle** field:
   - Select the **fx** icon
   - Enter the Power Fx expression:
     ```powerFx
     Topic.AvailableDevices.Title
     ```
   - OR, if you want to reference the specific device the user clicked:
     ```powerFx
     Topic.SelectedDevice
     ```
     (You'll need to create this variable if not already done — see Step 3 below)

2. **UserName** field:
   - Select the **fx** icon
   - Enter:
     ```powerFx
     User.DisplayName
     ```
     (This retrieves the logged-in user's name from the session context)

[SCREENSHOT: Tool node showing DeviceTitle and UserName fields populated with Power Fx expressions]

**✅ Checkpoint:** The tool node is configured to pass device title and user name to the flow.

### Step 3: (Optional) Capture Which Device Was Clicked

If you want to know which specific device the user clicked (when multiple Adaptive Cards are displayed), you need to capture the `Action.Submit` data.

**Option A: Use the first device in the list (simplest for this lab)**
- Keep `Topic.AvailableDevices.Title` — this passes the first device's title
- OR use: `First(Topic.AvailableDevices).Title`

**Option B: Capture the clicked device (advanced)**
1. After the Adaptive Card node, add a **Question** node:
   - **Ask:** (leave blank — the Adaptive Card action automatically answers)
   - **Save response as:** `SelectedDeviceTitle`
2. In the Tool node, reference: `Topic.SelectedDeviceTitle`

**For this lab, Option A is fine.** We'll assume the user wants the first available device.

---

## Lab 9.3: Test the Agent Flow End-to-End

**Objective:** Verify the agent sends an email when a device is requested.

### Step 1: Save the Topic

1. In the topic designer, select **Save** (top toolbar)

[SCREENSHOT: Topic designer Save button]

### Step 2: Open the Test Pane

1. Navigate to the **Overview page** (or stay in the topic designer if Test pane is visible)
2. Select **New test session** (circular arrows icon)

### Step 3: Trigger the Device Request Topic

1. In the Test pane, type:
   ```
   I need a laptop
   ```

2. Press **Enter**

3. Select **Laptop** when asked "What type of device do you need?"

**Expected flow:**
- Agent queries SharePoint for available laptops
- Displays Adaptive Card(s) with device details
- Shows "Request this device" button

[SCREENSHOT: Test pane showing Adaptive Card with "Request this device" button]

### Step 4: Click the "Request this device" Button

1. In the Test pane, select **Request this device** on one of the Adaptive Cards

**Expected behavior:**
- The tool node activates
- Agent Flow runs (sends email)
- Agent responds: "Your device request has been noted. An IT team member will follow up soon." (or similar confirmation)

[SCREENSHOT: Test pane showing confirmation message after button click]

### Step 5: Verify the Email Was Sent

1. Open your email inbox (the address you specified in the flow: `support@contoso.com` or your test email)
2. Look for an email with:
   - **Subject:** `Device Request: [Device Title]`
   - **Body:** Device title, user name, request message

[SCREENSHOT: Email inbox showing device request email with dynamic content populated]

**✅ Checkpoint:** The Agent Flow successfully sends an email when the device is requested.

---

## Troubleshooting Agent Flows

### Issue 1: Flow Doesn't Trigger

**Symptoms:** Click "Request this device" but no email is sent.

**Possible causes:**
- Flow isn't connected to the tool node
- Flow trigger is misconfigured
- Flow encountered an error

**Solutions:**
1. Verify the tool node shows the correct flow name: **Send Device Request Email**
2. In the flow designer, check the **Run history** (top toolbar → **Run history**)
   - If no runs appear, the flow isn't being triggered
   - If runs appear with errors, review the error details
3. Test the flow manually:
   - In the flow designer, select **Test** → **Manually** → **Test**
   - Enter sample values for `DeviceTitle` and `UserName`
   - Verify the email sends

[SCREENSHOT: Flow run history showing successful runs with timestamps]

### Issue 2: Email Sends But Dynamic Content Is Blank

**Symptoms:** Email arrives but shows blank fields for device title or user name.

**Possible causes:**
- Input parameters aren't mapped correctly in the tool node
- Power Fx expression references a non-existent variable

**Solutions:**
1. Re-check the tool node input mappings:
   - `DeviceTitle`: Should reference a variable that contains the device title
   - `UserName`: Should reference `User.DisplayName` or a stored user variable
2. Add a debug message node **before** the tool node:
   - Display: `Topic.AvailableDevices.Title` and `User.DisplayName`
   - Verify they contain values

### Issue 3: Multiple Emails Send for One Click

**Symptoms:** One button click sends multiple emails.

**Possible causes:**
- Adaptive Card is displaying multiple cards (one per device), and all buttons are wired to the same flow
- User clicked multiple times

**Solution:**
- This is expected if multiple devices are available (one card per device)
- To send only one email per user action, add logic to track which device was clicked (Option B from Lab 9.2, Step 3)

---

## Understanding Agent Flows vs. Power Automate Cloud Flows

**Agent Flows:**
- Created **inside Copilot Studio**
- Billed as part of **Copilot Studio** (no separate Power Automate license needed)
- Tightly integrated with topics (easy to call from a tool node)
- Limited to scenarios where the agent calls the flow

**Power Automate Cloud Flows:**
- Created in **Power Automate** (make.powerautomate.com)
- Billed separately (requires Power Automate license or pay-per-use)
- Can be triggered by **many sources** (email, schedule, HTTP, button, etc.)
- Can also be called from Copilot Studio agents (via connectors)

**When to use each:**

| Scenario | Use Agent Flow | Use Power Automate Cloud Flow |
|---|---|---|
| Agent needs to send an email, create a record | ✅ | ✅ |
| Agent needs to call a flow **and get a response** | ✅ | ✅ |
| Non-agent trigger (schedule, email arrival, etc.) | | ✅ |
| Complex multi-step approvals | | ✅ (Approvals connector) |
| Simple automation tied to agent topic | ✅ | |

**For this course, Agent Flows are the right choice** — they're simple, integrated, and don't require separate licensing.

---

## Advanced Agent Flow Scenarios

You can extend Agent Flows to:

### Return Data to the Agent

Agent Flows can return values to the topic:

1. In the flow, add a **Respond to Copilot Studio** action
2. Add **outputs** (e.g., `ConfirmationNumber`, `ApprovalStatus`)
3. In the topic, the tool node receives the outputs as variables
4. Display the returned data in a message: "Your request number is {Topic.ConfirmationNumber}"

### Create Records in Dataverse or SharePoint

Instead of (or in addition to) sending email:

1. Add a **SharePoint** action: **Create item**
2. Select the **Devices Requests** list (you'd create this in SharePoint)
3. Map fields: Device title, user name, status ("Pending")

### Trigger Approvals

Use the **Approvals** connector:

1. Add **Start and wait for an approval** action
2. Send approval request to IT manager
3. Return approval status to the agent
4. Agent notifies the user: "Your request has been approved!"

---

## Key Takeaways

- **Agent Flows** automate tasks triggered by agent conversations
- **Two automation options:** Agent Flows (stable, GA) and Workflows (new, preview)
- **For this course, use Agent Flows** — available in all environments
- **Tool nodes** call Agent Flows from topic flows
- **Input parameters** pass data from topics to flows
- **Output parameters** return data from flows to topics
- **Common uses:** Send emails, create records, trigger approvals, call APIs

---

## What You've Built

You now have a fully functional device request workflow:
- ✅ User asks for a device → Topic activates
- ✅ Agent asks what type → User responds
- ✅ Agent queries SharePoint → Displays available devices in Adaptive Cards
- ✅ User clicks "Request this device" → **Agent Flow sends email to IT**
- ✅ Agent confirms: "Your request has been noted"

This is a production-ready feature that could be deployed to Teams today.

---

## Next Steps

In **Module 10: Add Event Triggers**, you'll make the agent **autonomous** — it will act **without user input** based on events like:
- A new high-priority ticket is created in Dataverse
- A scheduled time is reached (e.g., daily summary report)
- A webhook is received from an external system

This transforms the agent from **reactive** (waits for user input) to **proactive** (monitors and acts independently).

---

**Course Navigation:** [← Module 08](../08-enhance-with-adaptive-cards/README.md) | [Course Index](../README.md) | [Next: Module 10 →](../10-add-event-triggers/README.md)
