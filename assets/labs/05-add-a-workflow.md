# 🔁 Mission 05: Automate Approvals with a Workflow

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION CHAIN REACTION | ⭐⭐⭐ | 45 min | Copilot Studio (new experience), Workflows, Approvals, Office 365 | Workflows, Approvals | IT |

🎥 **Watch the Walkthrough** — *Add the new workflow experience to agents*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=1063s

---

## 🎯 Mission Brief

Some software on the Contoso list needs **manager sign-off**. That's a multi-step process — find the manager, request approval, wait, react — and it can take longer than a chat turn. The new **Workflows** designer handles it. You'll build `manager_approval_for_software`, add it to Rex as a **tool**, then update the `software-installation-request` skill to call it.

## 🔎 Objectives

1. Create a **Workflow** from the **Tools** block (new workflow designer)
2. Define **input parameters** and a **Respond to the agent** action (mind the **100-second** limit)
3. Build the approval: **Get manager** → **Start and wait for an approval** → **If/else**
4. Run the approval and the "respond to agent" step **in parallel**
5. **Call the workflow from a skill** and test the Visio request

---

## 🔁 Workflows, briefly

A **Workflow** is the new flows format in Copilot Studio, with a revamped visual designer and testing. Attach it to an agent as a **tool**: the agent calls it, passes inputs, and the workflow can **respond back to the agent**.

> ⏱️ **The 100-second rule.** When an agent calls a workflow, the workflow must **respond within ~100 seconds**. A human approval takes longer than that — so we **start** the approval and **immediately respond** to the agent ("approval started"), running both in **parallel**.
>
> 🧠 Workflows include **agentic actions** too — call other agents, classify info with AI, use M365 Copilot, and more.

---

## 🧪 Lab 05: Build the manager-approval workflow

### Prerequisites

- Rex with skills + tools from [Lab 04](./04-add-tools.md).
- **Approvals** available, and the **Office 365 Users** connector (to look up the manager).
- A test user whose **manager** is set in the directory (Reza's manager is "Sarah").

### 5.1 Create the workflow

1. **Build** → **Tools** → **+ Add a tool** → **Workflows** → **create a new workflow**. This opens the **new workflow designer**.
2. Name it:

   ```text
   manager_approval_for_software
   ```

### 5.2 Define inputs (what the agent passes in)

Add these **input parameters**:

| Input | Type |
| :--- | :--- |
| `applicationName` | Text |
| `requesterEmail` | Text |
| `businessReason` | Text |

### 5.3 Get the manager

1. Add a step using the **Office 365 Users** connector → **Get manager (V2)**.
2. For the input (user/UPN), pass **`requesterEmail`**.

### 5.4 Start and wait for an approval

1. Add **Approvals → Start and wait for an approval**.
2. **Approval type:** *First to respond*.
3. **Title:** `Approval needed for [applicationName]`
4. **Details:** include `requesterEmail`, `businessReason`, and `applicationName`.
5. **Assigned to:** the **Mail** property from the **Get manager** step.

### 5.5 Branch on the outcome

After the approval completes, add an **If/else (Condition)** on the approval **outcome**:

- **If** outcome **= Approve** → your approved path. For the demo, add a **Compose** action with the static value `approve` (in production: notify the team / provision the license / write to your system of record).
- **Else** (rejected) → add a **Compose** with `rejected`.

### 5.6 Respond to the agent — in parallel

Because the approval will **wait**, you must still respond to Rex within ~100 seconds:

1. Create a **parallel branch** alongside the approval branch.
2. In the parallel branch, add **Respond to the agent** with a message like:

   ```text
   Manager approval process has started. You will be notified once it completes.
   ```

So the workflow **simultaneously**: (a) starts the approval and waits for the manager, and (b) tells Rex the process kicked off.

### 5.7 Publish the workflow

**Publish** the workflow so Rex can call it.

### 5.8 Update the skill to call the workflow

1. **Skills** → open **`software-installation-request`** → **edit instructions**. Add:

   ```markdown
   # If manager sign-off is needed
   If the requested app requires manager sign-off (per the Approved Software List),
   call the manager_approval_for_software workflow, passing the application name,
   the requester's email, and a short business reason. Then tell the user the
   approval request has been sent to their manager.
   ```

2. **Save** the skill.

### 5.9 Test the Visio request

1. **Preview** → new chat:

   ```text
   I need Microsoft Visio installed for a project.
   ```

2. Rex uses `software-installation-request`, checks the **Approved Software List**, sees Visio **requires manager approval**, and calls **`manager_approval_for_software`**. He replies that the approval request was sent.
3. **Watch the workflow run:** it triggers, **gets the manager** (e.g., Sarah), and **responds back to Rex**.
4. **As the manager:** open the manager's mailbox/Approvals, **approve or reject** with comments, and submit. The workflow then continues into your **If/else** branch.

   > In production the approved branch would notify the team to provision the license; here the **Compose** values prove the branch logic works.

---

## ✅ Mission Complete

Rex can now run a real, long-running **approval process** through a Workflow and report status back to the user — all triggered from a skill. He's feature-complete. Time to prove he's reliable.

⏭️ Next: [**Mission 06 — Evaluate Rex**](./06-test-evaluate-monitor.md)

## 📚 Tactical Resources

- 🔗 [What is a flow? (Workflows vs. agent flows)](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio#what-is-a-flow)
- 🔗 [Use agent flows / workflows as tools](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)
- 🔗 [Asynchronous responses for long-running flows](https://learn.microsoft.com/microsoft-copilot-studio/flow-asynchronous-response)
