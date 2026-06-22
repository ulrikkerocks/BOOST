---
title: "10 · Add Event Triggers"
parent: Course Modules
nav_order: 10
---
# Module 10: Add Event Triggers

**Time:** 30 minutes  
**Scenario:** Autonomous Agent with Event-Based Activation

---

## Learning Objectives

By the end of this module, you will be able to:
- Explain what event triggers are and when to use them
- Create an event trigger based on a Dataverse table row change
- Configure a trigger to filter for specific conditions (e.g., high-priority tickets)
- Build a topic flow that executes automatically when the event occurs
- Understand the difference between conversational and autonomous agents

## Overview

Until now, your agent has been **reactive** — it waits for users to ask questions or trigger topics. In this module, you'll make the agent **autonomous** by adding an **event trigger** that activates automatically when something happens in your environment.

You'll create a trigger that monitors a Dataverse table for new high-priority support tickets and automatically escalates them to a manager via email — all without user interaction.

This demonstrates the power of **autonomous agents** — intelligent systems that monitor, reason, and act independently.

---

## What Are Event Triggers?

**Event triggers** activate agent topics based on **events**, not user input. Common event types:

| Event Type | When It Fires | Example Use Case |
|---|---|---|
| **Dataverse row added/modified** | A record is created or updated | Escalate high-priority tickets |
| **Schedule** | A specific time or recurrence | Send daily summary report at 9 AM |
| **Webhook** | External system sends a signal | Process incoming order from e-commerce site |
| **Email received** | Email arrives in a monitored inbox | Auto-categorize support emails |

### Conversational vs. Autonomous Agents

| Conversational Agent | Autonomous Agent |
|---|---|---|
| Waits for user input | Acts on events |
| Triggered by phrases or @mentions | Triggered by data changes, schedules, webhooks |
| Responds in chat | Can send notifications, create records, update systems |
| Examples: IT helpdesk, HR Q&A | Examples: Ticket escalation, monitoring alerts, scheduled reports |

**The Contoso Helpdesk Agent** is currently conversational. After this module, it will be **both** conversational **and** autonomous.

---

## The Scenario: Auto-Escalate High-Priority Tickets

You'll build an autonomous workflow:

1. A new support ticket is created in a Dataverse table (or SharePoint list)
2. If the ticket priority is **"High"**, the agent:
   - Reads the ticket details
   - Sends an email to the IT manager with ticket info
   - Logs the escalation

All of this happens **automatically** — no user interaction required.

---

## Lab 10.1: Create a Dataverse Table for Support Tickets

> **Note:** If you're comfortable with Dataverse, you can create the table yourself. If not, follow these steps.

### Step 1: Navigate to Power Apps Maker Portal

1. Go to [https://make.powerapps.com](https://make.powerapps.com)
2. Sign in with your M365 account
3. Ensure you're in your **developer environment** (top right environment picker)

[SCREENSHOT: Power Apps maker portal home page]

### Step 2: Create a New Table

1. In the left navigation, select **Tables** (or **Data** → **Tables**)
2. Select **+ New table** (top toolbar)
3. Choose **Create a table** (or **Blank table**)

[SCREENSHOT: Tables page with "+ New table" button]

4. In the **New table** dialog:
   - **Display name:** `Support Ticket`
   - **Plural name:** `Support Tickets` (auto-generated)
   - **Description (optional):** `Tracks IT support tickets for auto-escalation`
   - Enable **Track changes** (optional, for auditing)

[SCREENSHOT: New table dialog showing Support Ticket configuration]

5. Select **Create** (or **Save**)

6. The table is created and you land on the table designer

[SCREENSHOT: Support Ticket table designer showing default columns]

### Step 3: Add Columns to the Support Ticket Table

Every Dataverse table has a default **Name** column (primary field). We'll add more columns to store ticket details.

1. In the table designer, select **+ New column** (or **Add column**)

2. Add the following columns:

| Column Name | Data Type | Configuration |
|---|---|---|
| **Priority** | Choice | Choices: `Low`, `Medium`, `High` |
| **Description** | Multiple Lines of Text | Max length: 2000 |
| **Status** | Choice | Choices: `New`, `In Progress`, `Resolved`, `Escalated` |
| **Assigned To** | Single Line of Text | - |
| **Created By Email** | Single Line of Text | - |

**Example: Adding the Priority column:**
1. Select **+ New column**
2. **Display name:** `Priority`
3. **Data type:** **Choice** (or **Option Set**)
4. **Choices:**
   - `Low`
   - `Medium`
   - `High`
5. **Default choice:** `Medium`
6. Select **Save**

[SCREENSHOT: New column dialog showing Priority choice column with Low/Medium/High options]

Repeat for the other columns.

**✅ Checkpoint:** The Support Ticket table has columns: Name, Priority, Description, Status, Assigned To, Created By Email.

### Step 4: Add Sample Data

1. In the table designer, select **Data** (or **Edit in Excel** → add data, or use **+ New row**)
2. Add at least 2 sample tickets:

| Name | Priority | Description | Status | Assigned To | Created By Email |
|---|---|---|---|---|---|
| WiFi Not Working | High | Unable to connect to office WiFi | New | Unassigned | user@contoso.com |
| Slow Laptop | Low | Laptop is running slowly | New | Unassigned | user2@contoso.com |

[SCREENSHOT: Support Tickets table showing sample data in grid view]

3. Select **Save** (if editing in Excel, publish changes)

**✅ Checkpoint:** The Support Ticket table contains sample data.

---

## Lab 10.2: Create an Event Trigger in Copilot Studio

**Objective:** Configure the agent to monitor the Support Ticket table for new rows.

### Step 1: Navigate to the Triggers Section

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Select **Agents** → **Contoso Helpdesk Agent**
3. On the **Overview page**, scroll to the **Triggers** section

[SCREENSHOT: Overview page showing Triggers section with "+ Add trigger" button]

> **Note:** The **Triggers** section is separate from **Topics**. Topics have **phrase triggers** (conversational). The Triggers section is for **event triggers** (autonomous).

### Step 2: Add a New Trigger

1. In the **Triggers** section, select **+ Add trigger**
2. Select **When a row is added or modified** (or **Dataverse row change**)

[SCREENSHOT: Add trigger menu showing "When a row is added or modified" option]

3. A trigger configuration dialog appears

[SCREENSHOT: Trigger configuration dialog]

### Step 3: Configure the Trigger

1. **Table:** Select **Support Tickets** from the dropdown
2. **When to trigger:**
   - Select **When a row is added** (we want to trigger on new tickets)
   - Optional: Also select **When a row is modified** if you want to catch priority changes

[SCREENSHOT: Trigger configuration showing "When a row is added" selected]

3. **Filter condition (optional but recommended):**
   - We only want to trigger on **High** priority tickets
   - Select **Add condition** (or **Filter rows**)
   - **Field:** Priority
   - **Condition:** Equals
   - **Value:** High

[SCREENSHOT: Trigger filter showing "Priority equals High" condition]

4. **Name the trigger:** `High Priority Ticket Created`
5. Select **Save** (or **Create**)

**✅ Checkpoint:** The event trigger is configured to activate when a new Support Ticket with Priority = "High" is created.

---

## Lab 10.3: Create a Topic for the Event Trigger

**Objective:** Build the topic flow that executes when the event trigger fires.

### Step 1: Create a New Topic

1. On the **Overview page**, scroll to **Topics** → select **See all**
2. Select **+ New topic** → **From blank**

[SCREENSHOT: Topics page with "+ New topic" button]

3. The topic designer opens

### Step 2: Name the Topic

1. **Topic name:** `Escalate High Priority Ticket`
2. **Description:** `Automatically escalates high-priority support tickets to the IT manager`

[SCREENSHOT: Topic designer showing "Escalate High Priority Ticket" name]

### Step 3: Configure the Trigger

Unlike conversational topics (which use phrase triggers), this topic uses the **event trigger** you created in Lab 10.2.

1. In the **Trigger** node, locate the **Trigger type** dropdown
2. Change from **Phrases** to **Event**
3. Select the event trigger: **High Priority Ticket Created**

[SCREENSHOT: Trigger node showing "Event" type with "High Priority Ticket Created" selected]

4. The trigger node now shows the Dataverse table and condition

**✅ Checkpoint:** The topic is triggered by the "High Priority Ticket Created" event.

### Step 4: Access Trigger Output (Ticket Data)

When the event fires, the trigger automatically provides data about the **row that triggered it**. This data is available as variables.

Common trigger outputs:
- `Trigger.Name` — The ticket name (title)
- `Trigger.Priority` — Priority (High, in this case)
- `Trigger.Description` — Ticket description
- `Trigger.CreatedByEmail` — Who created the ticket

You can reference these in your topic flow.

---

## Lab 10.4: Build the Escalation Flow

**Objective:** Send an email to the IT manager with ticket details.

### Step 1: Add a Tool Node to Send Email

1. Below the **Trigger** node, select **+ Add node**
2. Select **Call a tool**
3. Select **Create a flow** (or select an existing Agent Flow if you want to reuse the one from Module 09)

[SCREENSHOT: Tool node with "Create a flow" option]

4. The Agent Flow designer opens

### Step 2: Create the Escalation Email Flow

1. **Flow name:** `Send High Priority Escalation Email`

2. **Trigger:** "When Copilot Studio calls a flow" (already configured)

3. **Add inputs:**
   - `TicketName` (Text)
   - `TicketDescription` (Text)
   - `TicketPriority` (Text)
   - `CreatedBy` (Text)

[SCREENSHOT: Flow trigger showing four text inputs]

4. **Add action:** **Send an email (V2)** (Outlook connector)

5. **Configure email:**

| Field | Value |
|---|---|
| **To** | `manager@contoso.com` (or your email for testing) |
| **Subject** | `🚨 High Priority Ticket: [TicketName]` |
| **Body** | See below |

**Email body template:**
```
A high-priority support ticket requires immediate attention:

Ticket Name: [TicketName]
Priority: [TicketPriority]
Created By: [CreatedBy]

Description:
[TicketDescription]

Please review and assign this ticket as soon as possible.

---
Auto-escalated by Contoso Helpdesk Agent
```

Use **dynamic content** to insert the four input parameters.

[SCREENSHOT: Send email action showing dynamic content in Subject and Body]

6. Select **Save**
7. Close the flow designer to return to the topic

### Step 3: Map the Flow Inputs in the Topic

1. Back in the topic, the **Tool** node now shows **Send High Priority Escalation Email**
2. Map the inputs using Power Fx:

| Flow Input | Power Fx Expression |
|---|---|
| **TicketName** | `Trigger.Name` |
| **TicketDescription** | `Trigger.Description` |
| **TicketPriority** | `Trigger.Priority` |
| **CreatedBy** | `Trigger.CreatedByEmail` |

[SCREENSHOT: Tool node showing mapped inputs with Trigger variables]

3. Select **Save**

**✅ Checkpoint:** The topic calls the Agent Flow and passes ticket data from the trigger.

### Step 4: Add a Confirmation Message (Optional)

Autonomous topics don't have a conversation with a user, but you can log actions for auditing.

1. Below the **Tool** node, select **+ Add node** → **Send a message**
2. **Message:** `Escalation email sent for ticket: {Trigger.Name}`

> **Note:** This message won't be shown to a user (there is no user in autonomous workflows). However, it appears in the agent's activity log and can be useful for debugging.

[SCREENSHOT: Message node with escalation confirmation]

3. Select **Save**

---

## Lab 10.5: Test the Event Trigger

**Objective:** Create a new high-priority ticket and verify the agent sends an escalation email.

### Step 1: Save the Topic

1. In the topic designer, select **Save**

[SCREENSHOT: Topic designer Save button]

### Step 2: Create a High-Priority Ticket

1. Go to **Power Apps** ([https://make.powerapps.com](https://make.powerapps.com))
2. Navigate to **Tables** → **Support Tickets**
3. Select **+ New row** (or **Edit in Excel** → add row)

4. Create a new ticket:
   - **Name:** `Server Down - Urgent`
   - **Priority:** **High**
   - **Description:** `Production server is unresponsive. Critical issue.`
   - **Status:** `New`
   - **Created By Email:** `user@contoso.com`

[SCREENSHOT: New Support Ticket form showing high-priority ticket]

5. Select **Save & Close**

**Expected behavior:**
- Dataverse saves the row
- The **High Priority Ticket Created** event trigger fires
- The **Escalate High Priority Ticket** topic activates
- The Agent Flow sends an email to `manager@contoso.com`

### Step 3: Verify the Email

1. Open your email inbox (manager@contoso.com or your test email)
2. Look for an email with:
   - **Subject:** `🚨 High Priority Ticket: Server Down - Urgent`
   - **Body:** Ticket details (name, priority, description, created by)

[SCREENSHOT: Email inbox showing escalation email with ticket details]

**✅ Checkpoint:** The event trigger successfully activated the topic and sent the escalation email.

### Step 4: Check Agent Activity Log (Optional)

1. In Copilot Studio, go to **Agents** → **Contoso Helpdesk Agent**
2. On the Overview page, locate **Activity** (or select **Activity** from the top menu or overflow)
3. You should see a log entry for the autonomous topic execution

[SCREENSHOT: Activity log showing "Escalate High Priority Ticket" topic execution with timestamp]

---

## Troubleshooting Event Triggers

### Issue 1: Trigger Doesn't Fire

**Symptoms:** Create a high-priority ticket but no email is sent.

**Possible causes:**
- Event trigger isn't saved or published
- Dataverse table isn't being monitored (permissions issue)
- Filter condition is incorrect

**Solutions:**
1. Verify the trigger is saved:
   - In Copilot Studio, go to **Overview** → **Triggers** section → verify "High Priority Ticket Created" is listed
2. Check the trigger filter:
   - Ensure **Priority equals High** is configured correctly
3. Test with a simplified trigger:
   - Remove the filter condition temporarily (trigger on **all** new tickets)
   - Create a Low or Medium priority ticket — does it trigger?
   - If yes, the filter condition was the issue

### Issue 2: Email Sends But Data Is Missing

**Symptoms:** Email arrives but shows blank fields for ticket name or description.

**Possible causes:**
- Input mapping in the topic uses incorrect variable names
- Dataverse column names don't match `Trigger.*` references

**Solutions:**
1. Verify trigger output variable names:
   - In the topic, hover over `Trigger.Name` — does it autocomplete?
   - Check the Dataverse table: is the column called "Name" or "Title"?
2. Add a debug message node before the Tool node:
   - Display: `Ticket: {Trigger.Name}, Priority: {Trigger.Priority}`
   - Check the activity log to see if the variables are populated

### Issue 3: Multiple Emails Send for One Ticket

**Symptoms:** One ticket triggers multiple email escalations.

**Possible causes:**
- Trigger is configured for both **"added"** and **"modified"**
- The Dataverse row is being updated immediately after creation (e.g., by another automation)

**Solutions:**
1. Change the trigger to only fire on **"added"**
2. Add a condition in the topic flow:
   - Check if `Trigger.Status = "New"` before sending email
   - This prevents re-triggering if the row is modified

---

## Advanced Event Trigger Scenarios

You can extend event triggers to:

### Scheduled Triggers

Run a topic every day at 9 AM to send a summary report:

1. Create a new trigger: **Schedule**
2. **Recurrence:** Daily at 9:00 AM
3. Topic flow:
   - Query Dataverse for tickets created in the last 24 hours
   - Format as a summary
   - Send email to IT manager

### Webhook Triggers

React to external systems:

1. Create a trigger: **Webhook**
2. External system (e.g., e-commerce site) sends HTTP POST to the webhook URL
3. Topic processes the payload (e.g., new order, inventory alert)

### Multi-Condition Triggers

Trigger only when multiple conditions are met:

- **Trigger:** When a Support Ticket is **modified**
- **Filters:**
  - Priority = "High" **AND**
  - Status = "In Progress" **AND**
  - Modified date is > 48 hours ago (overdue)

---

## Key Takeaways

- **Event triggers** make agents autonomous — they act without user input
- **Common event types:** Dataverse row changes, schedules, webhooks, emails
- **Autonomous topics** have event triggers instead of phrase triggers
- **Trigger outputs** provide data about the event (e.g., the row that was created)
- **Use cases:** Auto-escalations, scheduled reports, monitoring alerts, workflow automation

---

## What You've Built

You now have an agent that is:
- ✅ **Conversational** — answers questions, handles device requests (Modules 06–09)
- ✅ **Autonomous** — monitors Support Tickets table and auto-escalates high-priority items (Module 10)

This combination of conversational + autonomous capabilities is the future of AI agents.

---

## Next Steps

In **Module 11: Publish Your Agent**, you'll deploy the Contoso Helpdesk Agent to **Microsoft Teams** so employees can access it in their daily workflows.

Publishing unlocks the full value of your agent — moving it from development to production, where real users can benefit from it.

---

**Course Navigation:** [← Module 09](../09-automate-with-agent-flows/README.md) | [Course Index](../README.md) | [Next: Module 11 →](../11-publish-your-agent/README.md)
