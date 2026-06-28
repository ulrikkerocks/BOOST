# 🔧 Mission 04: Equip Tools & Log Tickets

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION ACTION STATION | ⭐⭐ | 40 min | Copilot Studio (new experience), SharePoint, Outlook | Tools, Connectors, Ticketing, PDF | IT |

🎥 **Watch the Walkthrough** — *Add Tools · Test the agent · Update skills (PDF report)*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=464s

---

## 🎯 Mission Brief

Skills tell Rex *what* to do; **Tools** let him actually *do* it. Rex needs to **send email** and **create SharePoint items** so the `password-reset` and `smart-triage` skills can complete. You'll add two connector tools, let **AI fill** their inputs, test the full ticket flow end-to-end, then **iterate** the `smart-triage` skill to also generate and attach a **PDF report**.

## 🔎 Objectives

1. Add the **Office 365 Outlook → Send an email** tool
2. Add the **SharePoint → Create item** tool
3. Understand **AI-filled inputs** and the **user-vs-maker** execution context
4. Test **password reset** and **ticket logging** end-to-end
5. **Edit** `smart-triage` to generate a one-page **PDF** and attach it to the confirmation email

---

## 🔧 Tools in the new experience

Add tools from the **Build** tab → **Tools**. Types include **connectors**, **MCP servers**, **REST APIs**, the new **Workflows**, and **prompts**. The orchestrator decides when to call a tool based on the conversation, Rex's instructions, your **skills**, and each tool's **description** — there are no manual triggers.

> 🤖 **AI-filled inputs:** for connector actions, Copilot Studio can **let AI fill the inputs** from conversation context (the default). You can also fill a field manually or add extra context to guide the AI.
>
> 👤 **Execution context:** a tool can run **as the user** interacting with the agent, or **as the maker** (your account). Pick deliberately — e.g., sending email "as the user" vs. "as the maker."

---

## 🧪 Lab 04: Wire up tools, then log a ticket

### Prerequisites

- Rex with the four skills from [Lab 03](./03-add-a-skill.md).
- Your **Tickets** list **site URL + list name** from [Lab 00](./00-course-setup.md).

### 4.1 Add the Send-email tool

1. **Build** → **Tools** → **+ Add a tool** → **Connectors** → **Office 365 Outlook**.
2. Choose the **Send an email (V2)** action.
3. Decide the **context**: send **as the user** interacting with Rex, or **as the maker** (your account). For the demo, the maker context is simplest.
4. Leave inputs (To, Subject, Body) set to **AI fills** (the default). **Save / Add.**

   > The `password-reset` and `smart-triage` skills reference "send email" — this is the tool that makes that real.

### 4.2 Add the Create-item tool

1. **Tools** → **+ Add a tool** → **Connectors** → **SharePoint** → **Create item**.
2. Set inputs to **Value**, and add context so it targets the right list. For example:

   ```text
   The site address must be the IT Help Desk site and the list name must be Tickets.
   ```

   (Paste your actual **site URL** and confirm the **list name** is `Tickets`.)
3. **Save / Add.**

   > 🧠 You don't pre-map every column. The `smart-triage` skill (Lab 03) tells Rex to read the **list schema** at runtime, and the orchestrator maps the fields when it calls **Create item**.

### 4.3 Test: password reset (email tool)

1. **Preview** → new chat:

   ```text
   I'm locked out and I forgot my password.
   ```

2. Following `password-reset`, Rex confirms your **name and email**, then asks to **verify identity** (employee ID). Provide it.
3. On verification, Rex calls **Send an email** and tells you a reset link was sent. **Check your mailbox** for the email.

### 4.4 Test: log a ticket (triage → create item + email)

1. New chat. Describe something needing admin access, e.g.:

   ```text
   My account can't access the shared finance drive and I think it needs admin rights.
   ```

2. Rex searches knowledge, recognizes it needs admin access, and offers to log a ticket. Reply:

   ```text
   Yes, please log a ticket.
   ```

3. `smart-triage` activates. Watch Rex:
   - grab the **Tickets list metadata** and understand the **column schema**,
   - call **Create item** to create the record, then
   - call **Send an email** with the **ticket number and priority**.
4. **Verify in SharePoint:** open the **Tickets** list — the new row is there. **Check your mailbox** for the confirmation email.

   > 🎉 That's an agent answering *and* acting: reading a list schema, writing a record, and emailing a confirmation — all driven by a markdown skill plus two connector tools.

### 4.5 Iterate: add a PDF report to the ticket

Skills are editable — let's level up `smart-triage` so it also produces a PDF.

1. **Skills** → open **`smart-triage`** → **edit the instructions**. Keep the triage steps and add:

   ```markdown
   # After creating the ticket
   - Generate a one-page PDF report that summarizes the ticket (number, summary,
     description, category, priority, requestor, date).
   - When sending the confirmation email, attach the PDF report to the email.
   ```

2. **Save** the skill. (Rex uses his **built-in PDF skill** to generate the document — no extra tool needed.)
3. **Preview** → new chat → test a hardware issue:

   ```text
   I spilled coffee on my phone and now it won't turn on at all.
   ```

   Then **log a ticket**. Rex creates the **Tickets** row, **generates the PDF**, and **sends the confirmation email with the PDF attached**.
4. **Verify:** new row in the Tickets list, and an email with the **PDF attachment**.

---

## ✅ Mission Complete

Rex now takes real action: resets passwords by email, logs tickets to SharePoint, and emails confirmations with a generated PDF report. Next we'll handle the trickier case — software that needs a **manager's approval** — using the new **Workflows** designer.

⏭️ Next: [**Mission 05 — Automate Approvals with a Workflow**](./05-add-a-workflow.md)

## 📚 Tactical Resources

- 🔗 [Tools overview for agents (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/tools-overview)
- 🔗 [Add tools and skills to an agent (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/tools-skills-legacy)
- 🔗 [Use connectors as tools](https://learn.microsoft.com/microsoft-copilot-studio/advanced-connectors)
