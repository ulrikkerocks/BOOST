# 🎴 Module 08: Enhance with Adaptive Cards

**Codename:** OPERATION SHOWCASE  
**Time:** 40 minutes  
**Scenario:** Present a Logged Ticket as a Rich Card

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Explain what Adaptive Cards are and when to use them
- Design an Adaptive Card with the JSON schema
- Have Bit present a logged ticket as a rich card instead of plain text
- Bind live values (ticket number, priority, etc.) into the card
- Test the card in the Preview pane

## 🧭 Overview

In Module 07, when Bit logs a ticket he confirms it as **plain text**. That works, but a **rich card** is clearer and more professional — especially once Bit is published to Microsoft Teams.

In this module you'll give Bit an **Adaptive Card** so that, after `smart-triage` logs a ticket, he presents a tidy confirmation card: ticket number, summary, category, priority, status, requestor — and a button to open the ticket in SharePoint.

> 🧭 **Where this fits Bit's story.** This module makes an *existing* capability (the ticket from Module 07) look better. If you'd rather practice on the software flow, the same technique applies to a **software-request card** — see the alternative at the end.

---

## 🧰 Prerequisites

- **Bit** with the `smart-triage` skill and the **Create item** / **Send email** tools from [Module 07](../07-add-topic-with-triggers/).

> 🏫 **In the facilitated workshop**, you'll already have logged a ticket in Module 07. If you're at the office, complete [Module 07](../07-add-topic-with-triggers/) first.

---

## 🧩 What Are Adaptive Cards?

**Adaptive Cards** are a platform-agnostic schema for UI cards. Originally developed by Microsoft, they're now an open standard supported across **Microsoft Teams**, **Outlook**, **Copilot Studio agents**, Windows notifications, and more.

### Why Use Adaptive Cards?

| Plain Text | Adaptive Card |
|---|---|
| Simple, fast | Rich, visual, branded |
| Limited formatting | Full control over layout and buttons |
| Plain data dump | Structured, scannable |
| No interactivity | Buttons, input fields, actions |

**Example use cases:**
- **Ticket confirmation** (this module) — number, priority, status, and a link
- **Approval requests** — request details + Approve/Reject buttons
- **Order confirmation** — summary, total, tracking link
- **Survey / feedback** — inline rating or comment form

![Example Adaptive Card showing a ticket confirmation with fields and a "View in SharePoint" button](/screenshots/08/01_ticket-card.png)

---

## 🆕 Adaptive Cards in the New Experience

In classic Copilot Studio you added an Adaptive Card **node** inside a topic flow and bound it with Power Fx. There are **no topics** in the new experience — so instead you give Bit a **card template** and instruct the relevant **skill** to present its result as that card. The orchestrator fills the card's placeholders from the values the skill just produced (the ticket it created).

> ⚠️ **Preview note.** The exact way to attach an Adaptive Card in the new experience is evolving (it may appear as a card capability, a prompt/tool, or a card block referenced from a skill). The transferable skills here — **designing the card JSON** and **deciding what data binds into it** — are identical regardless of where the button lives. Confirm the current authoring path in your tenant before the workshop; the facilitator notes cover fallbacks.

---

## 🧪 Lab 8.1: Design the Ticket Confirmation Card

**Objective:** Author the Adaptive Card JSON for a logged ticket.

Adaptive Cards are defined with **JSON**. Here's the ticket confirmation card — a header, the summary, a **FactSet** of ticket details, and an **open-in-SharePoint** button:

```json
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    {
      "type": "TextBlock",
      "text": "🎫 Ticket logged",
      "weight": "Bolder",
      "size": "Large"
    },
    {
      "type": "TextBlock",
      "text": "${title}",
      "wrap": true,
      "spacing": "None",
      "isSubtle": true
    },
    {
      "type": "FactSet",
      "facts": [
        { "title": "Ticket #", "value": "${ticketNumber}" },
        { "title": "Category", "value": "${category}" },
        { "title": "Priority", "value": "${priority}" },
        { "title": "Status", "value": "${status}" },
        { "title": "Requestor", "value": "${requestor}" }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "View in SharePoint",
      "url": "${ticketUrl}"
    }
  ]
}
```

<!-- SCREENSHOT: Adaptive Card editor showing the ticket confirmation JSON -->

**What this card includes:**
- A **header** and the ticket **summary** (`${title}`)
- A **FactSet** — ticket number, category, priority, status, requestor
- An **Action.OpenUrl** button to view the item in SharePoint

**Data binding:** the `${...}` placeholders are filled at runtime with the values from the ticket `smart-triage` just created.

> 💡 **Tip:** Validate any card JSON in the [Adaptive Cards Designer](https://adaptivecards.io/designer/) — paste it, add sample data, and preview before wiring it into Bit.

**✅ Checkpoint:** You have a valid ticket confirmation card.

---

## 🧪 Lab 8.2: Have Bit Present the Card

**Objective:** Wire the card so Bit shows it after logging a ticket.

1. Add the card to Bit using your tenant's current Adaptive Card authoring path (a card capability/tool, or a card referenced from the skill).
2. Edit the **`smart-triage`** skill to present the confirmation as the card. Replace the plain-text confirmation step with:

   ```markdown
   # Confirm with a card
   After creating the ticket, present the confirmation as the Ticket Confirmation
   Adaptive Card, filling: ticketNumber, title, category, priority, status,
   requestor, and ticketUrl (the SharePoint item link). Still send the
   confirmation email as before.
   ```

3. **Save** the skill.

<!-- SCREENSHOT: smart-triage skill updated to present the ticket as an Adaptive Card -->

**✅ Checkpoint:** `smart-triage` now confirms tickets with the card.

---

## 🧪 Lab 8.3: Test the Card

1. **Preview** → new chat → log a ticket (as in Module 07):

   ```text
   My laptop won't connect to any monitor and I've tried two cables. Please log a ticket.
   ```

2. After `smart-triage` creates the row, Bit presents the **ticket confirmation card** — number, category, priority, status, requestor, and the **View in SharePoint** button.

<!-- SCREENSHOT: Preview pane showing the rendered ticket confirmation card -->

**Verify:**
- ✅ The fields show the real ticket values
- ✅ The button opens the SharePoint item
- ✅ The confirmation email still sends

**✅ Checkpoint:** Bit confirms tickets with a rich, interactive card.

---

## 🔀 Alternative: A Software-Request Card

The same technique fits the software flow. Instead of a ticket, present a **software-request card** from `software-installation-request`:

```json
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    { "type": "TextBlock", "text": "💿 Software request", "weight": "Bolder", "size": "Large" },
    {
      "type": "FactSet",
      "facts": [
        { "title": "Application", "value": "${application}" },
        { "title": "Distribution", "value": "${distribution}" },
        { "title": "Approval needed", "value": "${approvalNeeded}" }
      ]
    }
  ]
}
```

This is a great place to practice once you've automated approvals in Module 09 — the card can show whether a request is **self-service** or **awaiting manager sign-off**.

---

## 🚀 Advanced Adaptive Card Features

### Input Fields
Collect data directly in the card:
```json
{ "type": "Input.Text", "id": "note", "placeholder": "Add a note for the help desk" }
```

### Action.OpenUrl
Open a link when a button is clicked (used above for the SharePoint item).

### Conditional Formatting
Show/hide elements based on data with `$when`:
```json
{ "type": "TextBlock", "text": "⚠️ Critical — fully blocked", "$when": "${priority == 'Critical'}" }
```

### Accessibility
Always include `altText` for images and clear, descriptive button labels for screen readers.

---

## 🛠️ Troubleshooting Adaptive Cards

### Issue 1: Card doesn't render (blank or error)
- **JSON syntax** — validate in the [Adaptive Cards Designer](https://adaptivecards.io/designer/)
- **Schema version** — try `1.5` (or lower if your channel doesn't support it)
- **Placeholder names** — make sure the skill fills the exact `${...}` names used in the card

### Issue 2: Fields are blank
- The skill didn't pass a value for that placeholder — check the `smart-triage` instructions list every field
- Test with the question you know produces a complete ticket

### Issue 3: The button doesn't open the item
- `${ticketUrl}` wasn't populated — have the skill include the SharePoint item link when it creates the ticket

---

## 🧠 Key Takeaways

- **Adaptive Cards** provide rich, interactive UI for agent responses
- **JSON-based** — defined with the Adaptive Card schema; validate in the designer
- **New experience** — give Bit the card template and let a **skill** present its result as the card (no topic nodes)
- **Data binding** — `${...}` placeholders are filled from the skill's values
- **Platform-agnostic** — cards render in Teams, Outlook, and web
- **Actions** — buttons can open URLs, submit data, or collect input

---

## 🏗️ What You've Built

Bit now confirms a logged ticket with a **rich Adaptive Card** — number, category, priority, status, requestor, and a link to the SharePoint item — instead of plain text.

---

## ⏭️ Next Steps

In **Module 09: Automate Approvals with Workflows**, you'll handle the trickier case — software that needs a **manager's approval** — using the new **Workflows** designer, and call it from the `software-installation-request` skill.

---

**Course Navigation:** [← Module 07](../07-add-topic-with-triggers/) | [Course Index](../) | [Next: Module 09 →](../09-automate-with-agent-flows/)
