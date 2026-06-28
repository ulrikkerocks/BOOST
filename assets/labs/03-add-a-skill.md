# 🧠 Mission 03: Teach Rex Skills

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION PLAYBOOK | ⭐⭐ | 40 min | Copilot Studio (new experience) | Skills, Markdown | IT |

🎥 **Watch the Walkthrough** — *Add Skills in Microsoft Copilot Studio*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=350s

---

## 🎯 Mission Brief

**Skills are the headline of the new Copilot Studio.** A skill is a set of **reusable instructions in markdown** that defines a specific behavior — *when* it should activate, the *guidelines* to follow, *examples*, and *notes*. The orchestrator loads the right skill at the right moment. No topics, no trigger phrases.

In this mission you'll give Rex four skills: `password-reset`, `vpn-troubleshooting`, `smart-triage`, and `software-installation-request`. Two of them (`smart-triage`, `software-installation-request`) reference actions you'll wire up in [Lab 04](./04-add-tools.md) and [Lab 05](./05-add-a-workflow.md) — that's expected; skills describe the behavior, tools/workflows provide the muscle.

## 🔎 Objectives

1. Understand a **skill's anatomy** and how it replaces topics
2. **Create a skill from blank** (and know you can **upload** or **download** skills)
3. Author four skills for Rex
4. See how skills are **reusable** and portable

---

## 🧬 Anatomy of a skill

When you **create a skill from blank**, you define:

- **Name** — all **lowercase, no spaces** — use **hyphens**, not underscores; don't start or end with a hyphen, e.g. `password-reset`
- **Description** — *what it does and when it should be activated* (this is how the orchestrator picks it)
- **Instructions** (markdown) — typically **when to activate**, **guidelines**, **examples**, and **notes/additional context**

> 🔁 **Skills are reusable.** You can **upload** an existing skill file, **build one from blank**, or **download** any skill to reuse it in another agent. (You can even bring in GitHub Copilot / Claude Code skills.)
>
> 🧰 Rex also has **built-in skills** out of the box — including ones that read **Word, PowerPoint, and PDF** files — which is why he could parse your FAQ document in Lab 02.

---

## 🧪 Lab 03: Author four skills

### Prerequisites

- **Rex** grounded with knowledge from [Lab 02](./02-add-knowledge.md).

For each skill: **Build** tab → **Skills** → **add a skill** → **Create from blank**, then fill in **Name**, **Description**, and **Instructions**, and **Save**.

### 3.1 `password-reset`

- **Name:** `password-reset`
- **Description:** `Use when a user asks to reset or recover their password, or says they are locked out.`
- **Instructions:**

```markdown
# When to activate
The user wants to reset their password or is locked out of their account.

# Guidelines
1. Confirm the user's full name and work email, and verify their identity
   (e.g., ask for their employee ID). Never ask for the current password.
2. Once identity is verified, send a password reset link to their work email
   using the Send-email tool.
3. Tell the user the link has been sent and what to do next.

# Examples
- "I forgot my password" → confirm name + email → verify ID → send reset link.
- "I'm locked out" → same flow.

# Notes
Never ask for passwords or one-time codes. Do not bypass identity verification.
```

### 3.2 `vpn-troubleshooting`

- **Name:** `vpn-troubleshooting`
- **Description:** `Use when a user reports VPN connection problems (can't connect, keeps dropping, slow).`
- **Instructions:**

```markdown
# When to activate
The user reports a VPN issue: cannot connect, frequent disconnects, or slow VPN.

# Guidelines
1. Ask one focused question if needed (error message, client/app, on/off corporate network).
2. Walk quick fixes first: sign out/in of the VPN client, switch network, restart client.
3. Then ordered steps: check credentials, update the VPN client, try an alternate gateway.
4. If still unresolved, offer to log a ticket (hand off to smart-triage).

# Examples
- "My VPN keeps disconnecting and restarting didn't help" → quick fixes → steps → offer ticket.

# Notes
Keep steps short and numbered. Don't request passwords.
```

### 3.3 `smart-triage`

This is the skill that turns an unresolved issue into a **ticket**. It tells Rex to read your SharePoint list's **schema** and create a record — using tools you'll add in [Lab 04](./04-add-tools.md).

- **Name:** `smart-triage`
- **Description:** `Use when an issue can't be resolved in chat or needs admin access and the user agrees to log a ticket.`
- **Instructions:**

```markdown
# When to activate
An issue cannot be resolved directly (or needs admin access) and the user agrees
to log a ticket.

# Guidelines
1. Query the IT Help Desk SharePoint site and look up the Tickets list.
2. Understand the schema of the Tickets list columns (Title, Description,
   Status, Priority, Category, Requestor).
3. Create a ticket in the Tickets list using the Create-item tool:
   - Title  = one-line summary
   - Description = symptoms + what was already tried
   - Category = Hardware | Software | Network | Access | Other
   - Priority = Low | Normal | High | Critical (Critical if user is fully blocked)
   - Status = New
4. Send the user a confirmation email (Send-email tool) including the ticket
   number and priority.

# Examples
- "This needs admin access — log a ticket" → create record → email confirmation.

# Notes
Read the live list schema before creating the record so fields map correctly.
```

> 🧠 Notice Rex isn't told *how* to read the schema step-by-step — the enhanced orchestrator figures that out using the **Create item** tool and its built-in capabilities. You describe intent; it plans the steps.

### 3.4 `software-installation-request`

- **Name:** `software-installation-request`
- **Description:** `Use when a user asks to install or request software.`
- **Instructions (v1 — knowledge only for now):**

```markdown
# When to activate
The user asks to install or request a software application.

# Guidelines
1. Look up the requested app in the Contoso Approved Software List knowledge.
2. If the app is self-service: tell the user no approval is needed and give the
   install steps.
3. If the app requires manager sign-off: tell the user approval is required.
   (In Lab 05 you'll update this skill to actually start the approval workflow.)

# Examples
- "Can I install Power BI Desktop?" → self-service → no approval, here are steps.
- "I need Microsoft Visio" → requires manager sign-off → approval needed.

# Notes
Only reference apps from the approved list. If it's not listed, offer to log a ticket.
```

> ✏️ You'll **edit** this skill in [Lab 05](./05-add-a-workflow.md) to call the manager-approval **workflow**. Editing a skill is how you iterate behavior — no rebuilding required.

### 3.5 Confirm and reuse

1. In the **Skills** list you should now see all four skills.
2. Select any skill → note you can **download** it (to reuse in another agent) — proof that skills are portable, reusable units.

> ⏳ Don't fully test the ticket/password flows yet — they need the **tools** from Lab 04. A quick `vpn-troubleshooting` check (which only needs knowledge + reasoning) is fine now.

---

## ✅ Mission Complete

Rex now has four reusable markdown skills. He *knows* how to reset a password, troubleshoot VPN, triage to a ticket, and handle software requests — but he can't yet send an email or write to SharePoint. Let's give him the tools.

⏭️ Next: [**Mission 04 — Equip Tools & Log Tickets**](./04-add-tools.md)

## 📚 Tactical Resources

- 🔗 [Skills overview for agents (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/skills-overview)
- 🔗 [Add tools and skills to an agent (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/tools-skills-legacy)
- 🔗 [Manage and delete skills in an agent (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/skills-manage)
