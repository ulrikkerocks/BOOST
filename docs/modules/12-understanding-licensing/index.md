# Module 12: Understanding Licensing

**Time:** 20 minutes  
**Scenario:** Licensing Models and Cost Planning

---

## Learning Objectives

By the end of this module, you will be able to:
- Explain the Copilot Studio licensing model (messages vs. capacity)
- Understand trial vs. production licensing
- Identify when Microsoft 365 Copilot licenses include Copilot Studio usage
- Estimate costs for a production agent deployment
- Understand Power Apps Developer Plan benefits

## Overview

You've built and published the Contoso Helpdesk Agent — it's functional and production-ready. Before deploying to hundreds or thousands of users, you need to understand the **licensing and cost model**.

In this module, you'll learn:
- What's included in the Copilot Studio trial
- How production licensing works (pay-per-message vs. capacity packs)
- How M365 Copilot licenses affect Copilot Studio costs
- How to estimate monthly costs based on usage

This knowledge is essential for planning deployments, budgeting, and making informed decisions about agent architecture.

---

## The Copilot Studio Licensing Model (June 2026)

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

## Licensing Options

You have three main licensing paths:

### Option 1: Copilot Studio Trial (30–90 Days)

**What you get:**
- **30 days** free (extendable to 90 days)
- **Full capabilities** — all features available (knowledge, topics, flows, triggers, channels)
- **Unlimited messages** (for trial users)
- **Publishing requires Authors role** (configured in Module 00)

**Limitations:**
- **Trial environment only** — not for production use
- **Limited users** — only trial participants can access the agent
- **No SLA** — Microsoft can disable the trial at any time

**Who should use this:**
- Learning and training (like this course)
- Proof-of-concept projects
- Evaluating Copilot Studio before committing to production

**How to extend the trial:**
1. Go to [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com)
2. Select **Environments** → select your trial environment
3. If eligible, select **Extend trial** (option appears near trial expiration)

[SCREENSHOT: Power Platform Admin Center showing "Extend trial" option]

### Option 2: Copilot Studio Standalone Subscription

**What you get:**
- **Production environment** with SLA
- **Pay-per-message** or **capacity packs**
- **All features** — same capabilities as trial

**Pricing (as of June 2026):**
- **Pay-per-message:** ~$0.01–$0.03 per message (varies by region and volume)
- **Capacity pack:** $200/month for 25,000 messages (~$0.008 per message)

**Who should use this:**
- Organizations deploying standalone agents (not using M365 Copilot)
- Custom agents for external users (customers, partners)
- High-volume scenarios where capacity packs offer cost savings

**How to purchase:**
1. Go to [Microsoft 365 Admin Center](https://admin.microsoft.com)
2. **Billing** → **Purchase services**
3. Search for **"Copilot Studio"**
4. Select a plan and complete purchase

[SCREENSHOT: M365 Admin Center showing Copilot Studio purchase options]

### Option 3: Microsoft 365 Copilot License (Includes Copilot Studio)

**What you get:**
- **M365 Copilot** ($30/user/month) **includes** Copilot Studio message entitlement
- **Per-user allocation:** Each M365 Copilot user gets a certain number of Copilot Studio messages per month (exact allocation varies; check current Microsoft documentation)
- **Pooled usage:** Messages are shared across all agents in the tenant

**Who should use this:**
- Organizations already deploying M365 Copilot
- Building declarative agents for M365 Copilot users (Module 03)
- Internal agents for employees with M365 Copilot licenses

**Example:**
- Your company has 500 M365 Copilot licenses
- Each user gets ~100 Copilot Studio messages/month (hypothetical allocation)
- **Total:** 50,000 messages/month included across all agents

**Important:** M365 Copilot licenses **do not** cover:
- Users without M365 Copilot licenses accessing agents
- External users (customers, partners)
- High-volume scenarios exceeding the included allocation (you'll need to purchase additional capacity)

---

## What Counts as a "Message"?

Understanding what counts as a billable message is critical for cost estimation.

**Billable messages:**
- ✅ User sends a message → agent responds with knowledge search → **1 message**
- ✅ User triggers a topic → agent asks a question → **1 message**
- ✅ User clicks an Adaptive Card button → agent calls a flow → **1 message**
- ✅ Event trigger fires → autonomous topic runs → **1 message**

**NOT billable (free):**
- ❌ Test pane in Copilot Studio (development/testing) → **0 messages**
- ❌ Agent Flow executes → **0 messages** (flows are billed separately via Power Automate, but often included in Copilot Studio subscription)

**Example session:**
```
User: "What's the WiFi password?"  → 1 message
Agent: "[Response with password]"

User: "I need a laptop"            → 1 message
Agent: "What type of device?"

User: Selects "Laptop"             → 1 message
Agent: [Displays Adaptive Card]

User: Clicks "Request this device" → 1 message
Agent: "Your request has been noted."

Total: 4 messages
```

**Cost (pay-per-message model):** 4 messages × $0.02 = **$0.08**

---

## Estimating Monthly Costs

Let's estimate costs for a production deployment of the Contoso Helpdesk Agent.

### Scenario: 1,000 Employees Using the Agent

**Assumptions:**
- 1,000 employees have access to the agent in Teams
- **20% active usage** — 200 employees use the agent each month
- **Average session length:** 5 messages per session
- **Sessions per user per month:** 2

**Calculation:**
```
Total messages/month = Users × Sessions/user × Messages/session
                     = 200 × 2 × 5
                     = 2,000 messages/month
```

**Cost options:**

| Licensing Model | Cost |
|---|---|
| **Pay-per-message** ($0.02/message) | 2,000 × $0.02 = **$40/month** |
| **Capacity pack** ($200 for 25,000 messages) | **$200/month** (overpaying, not cost-effective) |
| **M365 Copilot licenses** (500 users) | **Included** (if within allocation) |

**Recommendation:** For this scenario, **pay-per-message** is most cost-effective. If usage grows to 10,000+ messages/month, capacity packs become cheaper.

---

## Power Apps Developer Plan (Free for Developers)

You've been using the **Power Apps Developer Plan** throughout this course (configured in Module 00). Here's what it includes:

**What you get:**
- **Free developer environment** (separate from production)
- **Copilot Studio trial** (extendable to 90 days)
- **Power Apps, Power Automate, Dataverse** for development
- **No user limits** in dev environment
- **Full feature parity** with production (for testing)

**Limitations:**
- **Development/testing only** — not for production use
- **No SLA**
- **Single user** (you can't add team members to a dev plan environment)

**Who should use this:**
- Developers learning Power Platform
- Building proof-of-concept agents
- Testing before deploying to production

**How to keep it active:**
- Sign in to [https://make.powerapps.com](https://make.powerapps.com) at least once every 90 days
- Developer environments that are inactive for 90+ days may be disabled

---

## Licensing After June 2026: Teams Classic Chatbot Deprecation

**Important change:**
- **Before June 2026:** You could create "classic chatbots" directly in Teams
- **After June 2026:** Teams classic chatbot creation is **disabled**; all new agents must be created in Copilot Studio

**What this means:**
- If you have existing Teams chatbots (created before June 2026), they'll redirect to the web app experience
- **No impact on this course** — you're already using Copilot Studio (the current platform)

**Migration path:**
- Existing Teams classic chatbots can be exported and imported into Copilot Studio
- Microsoft provides migration tools and documentation

---

## Billing and Cost Management Tips

### 1. Monitor Usage

Use **Analytics** (Module 11) to track message volume:
- **Sessions per day** → Multiply by 30 for monthly estimate
- **Average messages per session** → Multiply to get total messages/month

[SCREENSHOT: Analytics page showing session metrics]

### 2. Set Up Billing Alerts

In **Azure Cost Management** (if using Azure-based billing):
- Set up budget alerts at 50%, 80%, and 100% of your monthly limit
- Receive email notifications when thresholds are exceeded

### 3. Optimize for Cost

**Strategies to reduce message consumption:**
- **Use knowledge sources effectively** — reduce back-and-forth by providing comprehensive answers upfront
- **Add suggested prompts** — guide users to ask the right questions (fewer clarifying messages)
- **Use topics for forms** — structured flows reduce ambiguity and retry messages
- **Cache frequent queries** — (advanced) use agent flows to cache common responses

### 4. Right-Size Your Licensing

- **Start with pay-per-message** (no upfront commitment)
- **Switch to capacity packs** when volume justifies it (>10,000 messages/month)
- **Leverage M365 Copilot entitlements** if your organization already has those licenses

---

## FAQ: Licensing Questions

### Q1: Do I need a Power Automate license for Agent Flows?

**Answer:** No. **Agent Flows** are included in the Copilot Studio license. You only need a separate Power Automate license if you're using **Power Automate Cloud Flows** (created outside Copilot Studio) that are triggered by the agent.

### Q2: Can I use the free trial forever?

**Answer:** No. Trials are limited to 30–90 days and are intended for evaluation, not production. After the trial, you must purchase a license or migrate to a paid environment.

### Q3: What happens if I exceed my message allocation (M365 Copilot users)?

**Answer:** You can purchase additional Copilot Studio capacity packs to cover overage. Usage beyond the included allocation is billed separately.

### Q4: Do autonomous agents (event triggers) consume messages?

**Answer:** Yes. Each time an event trigger fires and the topic executes, it counts as a **message**. For high-frequency triggers (e.g., monitoring thousands of rows), this can add up quickly.

**Cost optimization:** Use filters to trigger only on high-priority events (e.g., Priority = "High" in Module 10).

### Q5: Can I deploy agents to external users (customers) with Copilot Studio?

**Answer:** Yes. Copilot Studio supports external user scenarios (e.g., customer support chatbots on public websites). You'll need to:
- Purchase Copilot Studio standalone licenses (pay-per-message or capacity packs)
- Configure **authentication** (anonymous access or external identity providers)
- Ensure compliance with data residency and privacy requirements

---

## Key Takeaways

- **Trial:** 30–90 days, full features, free — great for learning and POCs
- **Production:** Pay-per-message or capacity packs — choose based on volume
- **M365 Copilot:** Includes Copilot Studio message entitlement — leverage if you have these licenses
- **Power Apps Developer Plan:** Free forever for development/testing (not production)
- **Messages = cost unit:** Every user turn (message, button click, topic trigger, event trigger) counts
- **Monitor usage** with Analytics to estimate and control costs

---

## What You've Learned

You now understand:
- ✅ How Copilot Studio licensing works (trial, standalone, M365 Copilot)
- ✅ What counts as a billable message
- ✅ How to estimate monthly costs for a production agent
- ✅ When to use pay-per-message vs. capacity packs
- ✅ The Power Apps Developer Plan benefits and limitations

---

## Next Steps

In **Module 13: Securing Your Recruit Badge**, you'll:
- Complete the course checklist
- Claim your **Copilot Agent Academy Recruit Badge**
- Explore next steps for advanced agent development (Special Ops curriculum)
- Join the Copilot Studio community

You're almost done — one more module to go!

---

**Course Navigation:** [← Module 11](../11-publish-your-agent/README.md) | [Course Index](../README.md) | [Next: Module 13 →](../13-securing-recruit-badge/README.md)
