# ⚡ Module 10: Autonomous Event Triggers

**Codename:** OPERATION NIGHT WATCH  
**Time:** 30 minutes  
**Scenario:** Auto-Escalate High-Priority Tickets

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Explain what event triggers are and when to use them
- Create an event trigger that watches the **Tickets** SharePoint list
- Filter the trigger for specific conditions (high-priority tickets)
- Have Bit send an escalation **automatically**, with no user interaction
- Understand the difference between conversational and autonomous agents

## 🧭 Overview

Until now, Bit has been **reactive** — he waits for a user. In this module you'll make him **autonomous**: the moment a **High** or **Critical** ticket lands in the **Tickets** list, Bit escalates it to the IT lead — no one has to ask.

Crucially, this watches the **same Tickets list** Bit already writes to in `smart-triage` (Module 07). One ticket store, end to end — a ticket Bit logs can immediately trigger an escalation.

---

## 🧩 What Are Event Triggers?

**Event triggers** activate the agent based on **events**, not user input:

| Event Type | When It Fires | Example |
|---|---|---|
| **SharePoint item added/modified** | A list item is created or changed | Escalate a new high-priority ticket |
| **Dataverse row added/modified** | A record is created or updated | React to a new record |
| **Schedule** | A time or recurrence | Daily summary at 9 AM |
| **Webhook** | An external system signals | Process an incoming order |

### Conversational vs. Autonomous Agents

| Conversational | Autonomous |
|---|---|
| Waits for user input | Acts on events |
| Triggered by a message | Triggered by data changes, schedules, webhooks |
| Responds in chat | Sends notifications, creates records, updates systems |
| Bit answering an employee | Bit escalating a high-priority ticket on its own |

After this module, Bit is **both** conversational *and* autonomous.

---

## 🎬 The Scenario: Auto-Escalate High-Priority Tickets

The autonomous flow:

1. A new ticket is created in the **Tickets** list (by `smart-triage`, or by anyone).
2. If **Priority** is **High** or **Critical**, Bit:
   - reads the ticket details, and
   - emails the **IT lead** to escalate.

All of it happens **automatically**.

---

## 🧰 Prerequisites

- The **Tickets** SharePoint list from [Module 00](../00-course-setup/) (the same one `smart-triage` writes to in [Module 07](../07-add-topic-with-triggers/)).
- The **Office 365 Outlook** connection from [Module 07](../07-add-topic-with-triggers/).
- A mailbox to receive escalations (use your own for testing in place of the IT lead).

> 🏫 **In the facilitated workshop**, the Tickets list and connections are pre-provisioned. If you're at the office, complete [Module 00](../00-course-setup/) and [Module 07](../07-add-topic-with-triggers/) first.

---

## 🧪 Lab 10.1: Add an Event Trigger on the Tickets List

**Objective:** Configure Bit to watch the Tickets list for new high-priority items.

### Step 1: Open the Triggers Area

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com) and open **Bit**.
2. On the **Build** page, find the **Triggers** area (separate from Skills — this is for **event** triggers, not conversation).

<!-- SCREENSHOT: Build page showing the Triggers area with "+ Add trigger" -->

### Step 2: Add the Trigger

1. Select **+ Add trigger** → choose a **SharePoint** event → **When an item is created** (and optionally **modified**).
2. Point it at your **IT Help Desk** site and the **Tickets** list.

![Workflow trigger type picker — Manual, Recurrence (schedule), Connector (external service), and HTTP request](/screenshots/10/01_trigger-types.png)

> 🆕 **Reality check.** In this environment, autonomous behavior is configured through a **Workflow's trigger**, not a separate "Triggers" block on the agent. Use **Connector** to fire from a SharePoint item being created (the Tickets list), or **Recurrence** for a scheduled check.

### Step 3: Filter for High/Critical

1. Add a **condition** so the trigger only fires for urgent tickets:
   - **Field:** Priority
   - **Condition:** is **High** or **Critical**
2. **Name the trigger:** `High Priority Ticket Created`
3. **Save.**

<!-- SCREENSHOT: Trigger filter — Priority is High or Critical -->

**✅ Checkpoint:** The trigger fires only when a High/Critical ticket appears in the Tickets list.

> 🧠 The trigger provides the **item's data** (Title, Description, Priority, Category, Requestor) for the escalation step to use.

---

## 🧪 Lab 10.2: Define the Escalation

**Objective:** When the trigger fires, email the IT lead with the ticket details.

You have two equivalent ways to do this — use whichever your tenant exposes:

- **A short Workflow** (reusing the muscle from Module 09): the trigger calls a workflow that sends the escalation email. Inputs: the ticket's title, description, priority, requestor.
- **A direct escalation action**: the trigger's autonomous behavior calls **Send an email** directly.

**Escalation email:**

| Field | Value |
|---|---|
| **To** | `itlead@contoso.com` (use your own address for testing) |
| **Subject** | `🚨 High priority ticket: <ticket title>` |
| **Body** | ticket title, priority, category, requestor, and the description |

```text
A high-priority ticket needs attention:

Ticket: <title>
Priority: <priority>
Category: <category>
Requestor: <requestor>

Description:
<description>

Auto-escalated by Bit, the Contoso Helpdesk Agent.
```

<!-- SCREENSHOT: The escalation email step mapping the ticket fields from the trigger -->

**✅ Checkpoint:** A High/Critical ticket triggers an escalation email to the IT lead.

---

## 🧪 Lab 10.3: Test the Trigger

**Objective:** Create a high-priority ticket and confirm the escalation fires.

### Option A: Let Bit create it (end-to-end)

1. **Preview** → new chat → describe a fully-blocking issue and ask Bit to log a ticket:

   ```text
   Our whole team can't reach the production database — everyone is blocked. Please log a ticket.
   ```

2. `smart-triage` sets **Priority = Critical** and writes the row. The trigger sees a Critical ticket and fires the escalation.

### Option B: Add a row directly

1. Open the **Tickets** list in SharePoint → **+ New**:
   - **Title:** `Production database unreachable`
   - **Priority:** **Critical**
   - **Category:** `Network`
   - **Requestor:** `you@contoso.com`
2. Save the row.

### Verify

1. Check the **IT lead** mailbox (your test address) for the escalation email with the ticket details.

<!-- SCREENSHOT: Inbox showing the auto-escalation email for the Critical ticket -->

**✅ Checkpoint:** A High/Critical ticket — whether logged by Bit or added by hand — auto-escalates to the IT lead.

---

## 🪂 Fallback and Notes

> ⚠️ **Facilitator note.** Autonomous triggers and their connectors are evolving in the new experience. If a **SharePoint item-created** trigger isn't available for autonomous agents in your tenant, use one of these instead:
> - a **Scheduled** trigger that scans the Tickets list for new High/Critical items every few minutes, or
> - a **Workflow** with a SharePoint "When an item is created" trigger that sends the escalation.
>
> The teaching point — *the agent acts on an event without a user* — is identical. Confirm the available path before the workshop.

> 🔁 **Avoid double-sends.** If you trigger on both *created* and *modified*, a later edit to the same ticket can re-fire. Trigger on **created** only, or add a guard (e.g., only escalate when **Status = New**).

---

## 🚀 Advanced Event Trigger Scenarios

- **Scheduled triggers** — every morning at 9 AM, summarize the previous day's tickets and email the IT lead.
- **Webhook triggers** — react to an external system (e.g., a monitoring tool posts an alert).
- **Multi-condition triggers** — escalate only when Priority = High **and** Status is still **New** after a set time (overdue).

---

## 🧠 Key Takeaways

- **Event triggers** make agents autonomous — they act without user input
- **One ticket store** — Bit watches the same Tickets list he writes to (no separate table)
- **Filter to what matters** — only High/Critical tickets escalate
- **Trigger data** — the new item's fields feed the escalation
- **Guard against double-sends** — trigger on *created*, or check Status

---

## 🏗️ What You've Built

Bit is now:
- ✅ **Conversational** — answers, resets passwords, logs tickets, runs approvals (Modules 06–09)
- ✅ **Autonomous** — watches the Tickets list and auto-escalates High/Critical items (Module 10)

---

## ⏭️ Next Steps

In **Module 11: Evaluate, Publish, Share & Monitor**, you'll prove Bit is reliable with an evaluation set, then publish him to **Microsoft Teams** and **Microsoft 365 Copilot**, share him, and watch usage on the **Monitor** tab.

---

**Course Navigation:** [← Module 09](../09-automate-with-agent-flows/) | [Course Index](../) | [Next: Module 11 →](../11-publish-your-agent/)
