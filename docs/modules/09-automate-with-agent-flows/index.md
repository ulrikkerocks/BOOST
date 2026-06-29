# 🔁 Module 09: Automate Approvals with Workflows

**Codename:** OPERATION CHAIN REACTION  
**Time:** 45 minutes  
**Scenario:** Manager Approval for Software

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Create a **Workflow** from the **Tools** block using the new workflow designer
- Define **input parameters** and a **Respond to the agent** action (mind the **100-second** limit)
- Build an approval: **Get manager** → **Start and wait for an approval** → **If/else**
- Run the approval and the "respond to agent" step **in parallel**
- Call the workflow from the `software-installation-request` skill and test a Visio request

## 🧭 Overview

Some software on the Contoso list needs **manager sign-off**. That's a multi-step process — find the manager, request approval, wait, react — and it can take longer than a single chat turn. The new **Workflows** designer handles it.

You'll build `manager_approval_for_software`, add it to Bit as a **tool**, then update the `software-installation-request` skill (from Module 07) to call it.

---

## 🔁 Workflows, Briefly

A **Workflow** is the new flows format in Copilot Studio, with a revamped visual designer and testing. Attach it to an agent as a **tool**: the agent calls it, passes inputs, and the workflow can **respond back to the agent**.

> ⏱️ **The 100-second rule.** When an agent calls a workflow, the workflow must **respond within ~100 seconds**. A human approval takes longer than that — so we **start** the approval and **immediately respond** to Bit ("approval started"), running both in **parallel**.
>
> 🧠 Workflows include **agentic actions** too — call other agents, classify info with AI, use M365 Copilot, and more.

> ⚠️ **Hyphens vs. underscores (again).** Your **skills** use hyphens (`software-installation-request`). This **workflow** is named `manager_approval_for_software` with **underscores** — workflows follow different naming rules. Both are correct.

---

## 🧰 Prerequisites

- **Bit** with the `software-installation-request` skill from [Module 07](../07-add-topic-with-triggers/).
- **Approvals** available, and the **Office 365 Users** connector (to look up the manager).
- A test user whose **manager** is set in the directory.

> 🏫 **In the facilitated workshop**, Approvals, the connectors, and a test user with a manager are pre-provisioned. If you're at the office, ensure your test account has a **manager** populated in Microsoft Entra ID, and that **Approvals** is available.

---

## 🧪 Lab 9.1: Create the Workflow

1. **Build** → **Tools** → **+ Add a tool** → **Workflows** → **create a new workflow**. This opens the **new workflow designer**.
2. Name it:

   ```text
   manager_approval_for_software
   ```

![New workflow designer — Start trigger, the Add palette (Agent, Classify, M365 Copilot, Human review, Connector, If/Else, Loop), and the trigger config panel](/screenshots/09/01_workflow-designer.png)

---

## 🧪 Lab 9.2: Define Inputs (What the Agent Passes In)

Add these **input parameters**:

| Input | Type |
|---|---|
| `applicationName` | Text |
| `requesterEmail` | Text |
| `businessReason` | Text |

<!-- SCREENSHOT: Workflow input parameters: applicationName, requesterEmail, businessReason -->

---

## 🧪 Lab 9.3: Get the Manager

1. Add a step using the **Office 365 Users** connector → **Get manager (V2)**.
2. For the input (user/UPN), pass **`requesterEmail`**.

<!-- SCREENSHOT: Get manager (V2) action with requesterEmail as the input -->

---

## 🧪 Lab 9.4: Start and Wait for an Approval

1. Add **Approvals → Start and wait for an approval**.
2. **Approval type:** *First to respond*.
3. **Title:** `Approval needed for [applicationName]`
4. **Details:** include `requesterEmail`, `businessReason`, and `applicationName`.
5. **Assigned to:** the **Mail** property from the **Get manager** step.

<!-- SCREENSHOT: Start and wait for an approval configured with the manager's mail as the assignee -->

---

## 🧪 Lab 9.5: Branch on the Outcome

After the approval completes, add an **If/else (Condition)** on the approval **outcome**:

- **If** outcome **= Approve** → your approved path. For the demo, add a **Compose** action with the static value `approve` (in production: notify the team / provision the license / write to your system of record).
- **Else** (rejected) → add a **Compose** with `rejected`.

<!-- SCREENSHOT: If/else condition branching on the approval outcome -->

---

## 🧪 Lab 9.6: Respond to the Agent — in Parallel

Because the approval will **wait**, you must still respond to Bit within ~100 seconds:

1. Create a **parallel branch** alongside the approval branch.
2. In the parallel branch, add **Respond to the agent** with a message like:

   ```text
   Manager approval process has started. You will be notified once it completes.
   ```

So the workflow **simultaneously**: (a) starts the approval and waits for the manager, and (b) tells Bit the process kicked off.

<!-- SCREENSHOT: Parallel branches — approval+wait on one side, Respond to the agent on the other -->

---

## 📢 Lab 9.7: Publish the Workflow

**Publish** the workflow so Bit can call it.

**✅ Checkpoint:** `manager_approval_for_software` is published and available to Bit as a tool.

---

## 🧪 Lab 9.8: Update the Skill to Call the Workflow

1. **Skills** → open **`software-installation-request`** → **edit instructions**. Add:

   ```markdown
   # If manager sign-off is needed
   If the requested app requires manager sign-off (per the Approved Software List),
   call the manager_approval_for_software workflow, passing the application name,
   the requester's email, and a short business reason. Then tell the user the
   approval request has been sent to their manager.
   ```

2. **Save** the skill.

<!-- SCREENSHOT: software-installation-request skill updated to call the workflow -->

---

## 🧪 Lab 9.9: Test the Visio Request

1. **Preview** → new chat:

   ```text
   I need Microsoft Visio installed for a project.
   ```

2. Bit uses `software-installation-request`, checks the **Approved Software List**, sees Visio **requires manager approval**, and calls **`manager_approval_for_software`**. He replies that the approval request was sent.
3. **Watch the workflow run:** it triggers, **gets the manager**, and **responds back to Bit**.
4. **As the manager:** open the manager's mailbox/Approvals, **approve or reject** with comments, and submit. The workflow then continues into your **If/else** branch.

<!-- SCREENSHOT: Preview showing Bit starting the approval, and the manager's Approvals card -->

> In production the approved branch would notify the team to provision the license; here the **Compose** values prove the branch logic works.

**✅ Checkpoint:** Bit starts a real, long-running approval and reports status back to the user.

---

## 🪂 Fallback: No New Workflow Designer?

> ⚠️ **Facilitator note.** If the **new** workflow designer isn't present in your tenant, the same logic builds as an **agent flow**: **Get manager → Start and wait for an approval → If/else**, with the **Respond to the agent** running in a **parallel** branch. The **100-second** constraint still applies. Confirm which is available before the workshop.

---

## 🧠 Key Takeaways

- **Workflows** are the new flows format — attach them to Bit as **tools**
- **The 100-second rule** — respond to the agent fast; run long work (approvals) in **parallel**
- **Get manager → approval → if/else** — a real, multi-step business process
- **Skills call workflows** — `software-installation-request` triggers the approval; you describe intent, the orchestrator passes the inputs
- **Workflows use underscores; skills use hyphens** — different naming rules

---

## 🏗️ What You've Built

Bit can now run a **manager-approval process** for software that needs sign-off:
- ✅ A `manager_approval_for_software` workflow (get manager → approval → branch, with a parallel respond)
- ✅ The `software-installation-request` skill calls it
- ✅ Self-service apps install immediately; manager-sign-off apps route to the manager

---

## ⏭️ Next Steps

In **Module 10: Autonomous Event Triggers**, you'll make Bit **proactive** — automatically escalating a **high-priority ticket** the moment one is created in the Tickets list, with no one having to ask.

---

**Course Navigation:** [← Module 08](../08-enhance-with-adaptive-cards/) | [Course Index](../) | [Next: Module 10 →](../10-add-event-triggers/)
