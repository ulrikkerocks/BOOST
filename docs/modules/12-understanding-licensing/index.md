# 💳 Module 12: Understanding Licensing

**Codename:** OPERATION WAR CHEST  
**Time:** 20 minutes  
**Scenario:** Licensing Models and Cost Planning

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Explain the Copilot Studio licensing model (messages vs. capacity)
- Understand trial vs. production licensing
- Identify when Microsoft 365 Copilot licenses include Copilot Studio usage
- Estimate costs for a production agent deployment
- Understand Power Apps Developer Plan benefits

## 🧭 Overview

You've built and published **Bit** — he's functional and production-ready. Before deploying to hundreds or thousands of users, you need to understand the **licensing and cost model**.

In this module, you'll learn what's included in the trial, how production licensing works (pay-per-message vs. capacity packs), how M365 Copilot licenses affect costs, and how to estimate monthly spend. This is essential for planning deployments and budgeting.

---

## 💳 The Copilot Studio Licensing Model (June 2026)

As of June 2026, Copilot Studio uses a **message-based** licensing model. You pay for the number of **sessions** or **messages** your agents process.

### Key Terms

| Term | Definition |
|---|---|
| **Message** | A single turn in a conversation (user sends a message, agent responds = 1 message) |
| **Session** | A conversation from start to finish (multiple messages) |
| **Capacity pack** | Prepaid bundle of messages (e.g., 25,000 messages/month) |
| **Pay-per-message** | Per-message billing (no upfront commitment) |
| **M365 Copilot license** | Microsoft 365 Copilot subscription ($30/user/month) — includes some Copilot Studio usage |

---

## 💳 Licensing Options

You have three main licensing paths:

### Option 1: Copilot Studio Trial (30–90 Days)

**What you get:**
- **30 days** free (extendable to 90 days)
- **Full capabilities** — knowledge, skills, tools, workflows, triggers, channels
- **Unlimited messages** (for trial users)
- **Publishing requires the Authors role** (configured in Module 00)

**Limitations:**
- **Trial environment only** — not for production use
- **Limited users** — only trial participants can access the agent
- **No SLA** — Microsoft can disable the trial at any time

**Who should use this:** learning/training (like this course), proof-of-concept, evaluating before committing.

**How to extend the trial:**
1. Go to [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com)
2. Select **Environments** → select your trial environment
3. If eligible, select **Extend trial** (appears near trial expiration)

[SCREENSHOT: Power Platform Admin Center showing "Extend trial" option]

### Option 2: Copilot Studio Standalone Subscription

**What you get:** a **production environment** with SLA, **pay-per-message** or **capacity packs**, and all features.

**Pricing (as of June 2026):**
- **Pay-per-message:** ~$0.01–$0.03 per message (varies by region and volume)
- **Capacity pack:** $200/month for 25,000 messages (~$0.008 per message)

**Who should use this:** organizations deploying standalone agents, custom agents for external users, high-volume scenarios.

**How to purchase:**
1. Go to [Microsoft 365 Admin Center](https://admin.microsoft.com)
2. **Billing** → **Purchase services**
3. Search for **"Copilot Studio"**, select a plan, and complete the purchase

[SCREENSHOT: M365 Admin Center showing Copilot Studio purchase options]

### Option 3: Microsoft 365 Copilot License (Includes Copilot Studio)

**What you get:** M365 Copilot ($30/user/month) **includes** a Copilot Studio message entitlement, with a per-user allocation pooled across all agents in the tenant.

**Who should use this:** organizations already deploying M365 Copilot, declarative agents (Module 03), internal agents for M365 Copilot users.

**Example:** 500 M365 Copilot licenses × ~100 Copilot Studio messages/user/month (hypothetical) = **50,000 messages/month** included across all agents.

**Important:** M365 Copilot licenses **do not** cover users without M365 Copilot licenses, external users, or usage beyond the included allocation (purchase additional capacity).

---

## 🧩 What Counts as a "Message"?

Understanding billable messages is critical for cost estimation.

**Billable messages:**
- ✅ User sends a message → agent responds with a knowledge search → **1 message**
- ✅ User asks Bit to log a ticket → Bit triages and creates the row → **1 message**
- ✅ User clicks an Adaptive Card button → agent acts → **1 message**
- ✅ An event trigger fires → autonomous escalation runs → **1 message**

**NOT billable (free):**
- ❌ The Preview/test pane in Copilot Studio → **0 messages**
- ❌ A workflow executing → generally included in the Copilot Studio subscription

**Example session:**
```
User: "What are the help desk hours?"       → 1 message
Bit:  "[hours from the FAQ]"

User: "I'm locked out — reset my password"  → 1 message
Bit:  "Confirm your name and employee ID…"

User: "[provides details]"                   → 1 message
Bit:  "Reset link sent to your work email."

User: "Also, our finance drive is down — log a ticket" → 1 message
Bit:  "Logged ticket #1234 (Access, High). Emailed you the details."

Total: 4 messages
```

**Cost (pay-per-message model):** 4 messages × $0.02 = **$0.08**

---

## 💰 Estimating Monthly Costs

Let's estimate costs for a production deployment of **Bit**.

### Scenario: 1,000 Employees

**Assumptions:** 1,000 employees have access; **20% active** (200/month); **5 messages/session**; **2 sessions/user/month**.

```
Total messages/month = Users × Sessions/user × Messages/session
                     = 200 × 2 × 5
                     = 2,000 messages/month
```

| Licensing Model | Cost |
|---|---|
| **Pay-per-message** ($0.02/message) | 2,000 × $0.02 = **$40/month** |
| **Capacity pack** ($200 for 25,000 messages) | **$200/month** (overpaying at this volume) |
| **M365 Copilot licenses** | **Included** (if within allocation) |

**Recommendation:** for this scenario, **pay-per-message** is most cost-effective. Above ~10,000 messages/month, capacity packs get cheaper.

---

## 💻 Power Apps Developer Plan (Free for Developers)

You've used the **Power Apps Developer Plan** throughout this course (Module 00):

**What you get:** a free developer environment, the Copilot Studio trial (extendable to 90 days), Power Apps/Automate/Dataverse, no user limits in dev, full feature parity for testing.

**Limitations:** development/testing only, no SLA, single user.

**Keep it active:** sign in to [make.powerapps.com](https://make.powerapps.com) at least once every 90 days — inactive dev environments may be disabled.

---

## 💳 Licensing Note: Teams Classic Chatbot Deprecation

- **After June 2026**, Teams classic chatbot creation is **disabled**; all new agents are created in Copilot Studio.
- **No impact on this course** — you're already using Copilot Studio (the new experience).
- Existing Teams classic chatbots can be exported/migrated into Copilot Studio.

---

## 💳 Billing and Cost Management Tips

### 1. Monitor Usage
Use the **Monitor** tab (Module 11) to track message volume — sessions/day × 30, and average messages/session.

[SCREENSHOT: Monitor tab showing session metrics]

### 2. Set Up Billing Alerts
In Azure Cost Management (if using Azure-based billing), set budget alerts at 50%, 80%, and 100%.

### 3. Optimize for Cost
- **Use knowledge effectively** — comprehensive answers reduce back-and-forth
- **Add suggested prompts** — guide users to the right questions
- **Lean on skills** — clear behaviors reduce ambiguity and retries
- **Filter autonomous triggers** — only fire on what matters (e.g., High/Critical tickets, Module 10)

### 4. Right-Size Your Licensing
- Start with **pay-per-message** (no commitment)
- Switch to **capacity packs** above ~10,000 messages/month
- Leverage **M365 Copilot entitlements** if you already have those licenses

---

## 💳 FAQ: Licensing Questions

**Q1: Do I need a Power Automate license for Workflows?**
Generally no — **Workflows** built in Copilot Studio are included. A separate Power Automate license applies if you use standalone Power Automate cloud flows triggered by the agent.

**Q2: Can I use the free trial forever?**
No — trials are 30–90 days for evaluation. After that, purchase a license or move to a paid environment.

**Q3: What if I exceed my M365 Copilot message allocation?**
Purchase additional Copilot Studio capacity; overage is billed separately.

**Q4: Do autonomous triggers consume messages?**
Yes — each time an event trigger fires and runs, it counts. **Filter** to high-value events (e.g., Priority = High/Critical in Module 10) to control cost.

**Q5: Can I deploy agents to external users?**
Yes — buy Copilot Studio standalone licenses, configure authentication, and ensure compliance with data residency/privacy.

---

## 🧠 Key Takeaways

- **Trial:** 30–90 days, full features, free — great for learning and POCs
- **Production:** pay-per-message or capacity packs — choose by volume
- **M365 Copilot:** includes a Copilot Studio entitlement — leverage it if you have the licenses
- **Power Apps Developer Plan:** free for development/testing (not production)
- **Messages = the cost unit:** every user turn, button click, or autonomous trigger counts
- **Monitor usage** to estimate and control costs

---

## 🎓 What You've Learned

You now understand:
- ✅ How Copilot Studio licensing works (trial, standalone, M365 Copilot)
- ✅ What counts as a billable message
- ✅ How to estimate monthly costs for Bit in production
- ✅ When to use pay-per-message vs. capacity packs
- ✅ The Power Apps Developer Plan benefits and limitations

---

## ⏭️ Next Steps

In **Module 13: Securing Your Recruit Badge**, you'll complete the course checklist, recap everything Bit can do, export your solution, and claim your **Recruit Badge** — plus where to go next.

---

**Course Navigation:** [← Module 11](../11-publish-your-agent/) | [Course Index](../) | [Next: Module 13 →](../13-securing-recruit-badge/)
