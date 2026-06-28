# 🧪 Mission 06: Evaluate Rex

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION QUALITY CONTROL | ⭐⭐ | 25 min | Copilot Studio (new experience) | Evaluations, Testing | IT |

🎥 **Watch the Walkthrough** — *Copilot Studio agent evaluations*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=1501s

---

## 🎯 Mission Brief

You've been testing Rex by hand in **Preview**. **Evaluations** make that repeatable: a set of **test cases** that validate Rex produces the outcome you want, so after you tweak an instruction, skill, or knowledge source you can re-check quality fast. The new experience can even **generate a starter set for you**.

## 🔎 Objectives

1. Understand **evaluations** as test cases for desired outcomes
2. Generate a **quick conversation set** (AI-generated) or upload your own **CSV**
3. **Run** the evaluation and read the results
4. Use results to decide what to change (instructions / skills / knowledge)

---

## 🧪 Lab 06: Evaluate the agent

### Prerequisites

- Feature-complete **Rex** from [Lab 05](./05-add-a-workflow.md).

### 6.1 Open evaluations and build a test set

1. Open the **Evaluate** area for Rex.
2. Choose how to create your test set:
   - **Upload a CSV** of conversations you author yourself, **or**
   - **Quick conversation set** — a very handy option that **generates ~10 conversations** automatically from Rex's **description, instructions, and skills**.
3. Use **Quick conversation set** to generate the starter cases.

   > ⚠️ The set is **AI-generated** — review it. It's an excellent starting point, not a finished test plan. Add or edit cases to cover the scenarios you care about, for example:
   >
   > | Scenario | What good looks like |
   > | :--- | :--- |
   > | "Help desk hours" | Answers from the FAQ doc |
   > | "Can I install Power BI Desktop?" | Self-service; no approval needed |
   > | "I'm locked out and forgot my password" | Verifies identity, emails a reset link |
   > | "My VPN keeps dropping — log a ticket" | Triages, creates a Tickets row, emails confirmation |
   > | "I need Microsoft Visio" | Detects manager sign-off; starts the approval workflow |
   > | "What's my password?" | Refuses; never asks for/handles passwords |

### 6.2 Run and interpret

1. **Run** the evaluation (it runs under your account): it prepares the test cases, runs them, and reports the **quality of the output**.
2. Read the results case by case. Where Rex underperforms, the fix is usually one of:
   - sharpen the **instructions**,
   - tighten a **skill** (its *when-to-activate* description or guidelines), or
   - improve a **knowledge** source.
3. Make the change and **re-run** to confirm the quality moved in the right direction.

> 🔁 This is the tightening loop: generate/maintain a test set, run it after every meaningful change, and only ship when the key cases pass.

---

## ✅ Mission Complete

You have a repeatable evaluation that proves Rex behaves — and a clear playbook for what to change when he doesn't. Let's put him in front of users.

⏭️ Next: [**Mission 07 — Publish, Share & Monitor**](./07-publish-and-share.md)

## 📚 Tactical Resources

- 🔗 [Create a test set for an agent (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-create)
- 🔗 [Test an agent (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/authoring-test-bot)
