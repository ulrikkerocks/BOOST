# 📢 Mission 07: Publish, Share & Monitor

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION GO LIVE | ⭐⭐ | 20 min | Copilot Studio (new experience), Teams, Microsoft 365 Copilot | Publishing, Channels, Monitoring | IT |

🎥 **Watch the Walkthrough** — *Publish to Teams & Microsoft 365 · Share · Monitor*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=1568s

---

## 🎯 Mission Brief

Rex answers, acts, logs tickets, generates PDFs, and runs approvals — and you've evaluated him. Final step: **publish**, get him into **Microsoft 365 Copilot**, **share** with colleagues, and watch usage on the **Monitor** tab.

## 🔎 Objectives

1. **Publish** Rex and see the available channels
2. Open Rex in **Microsoft 365 Copilot** and **share** it
3. Use the **Monitor** tab to track interactions and value

---

## 🧪 Lab 07: Ship and watch

### Prerequisites

- Evaluated **Rex** from [Lab 06](./06-test-evaluate-monitor.md).

### 7.1 Publish

1. Select **Publish**. Rex publishes to the available **channels** — these include a **demo website** and, by default, **Teams + Microsoft 365**.

   > Each publish creates a new version; publish for yourself, validate, then widen access.

### 7.2 Open in Microsoft 365 Copilot

1. Use the provided **link** to add Rex to **Microsoft 365 Copilot**.
2. Add it, then **interact with Rex directly in M365 Copilot** — try "Help desk hours" or "I need Microsoft Visio" to confirm the full experience works in the channel.

### 7.3 Share

1. From here you can **share the agent with other users** so your colleagues can use Rex.
2. For broader stakeholder testing without a full rollout, the **demo website** link is handy (internal stakeholders only — not for customers).

### 7.4 Monitor

1. Open the **Monitor** tab.
2. As users interact with Rex, **traffic appears** here. You get **full interaction details** and can quantify the **savings/value** the agent generates.
3. Use what you see to feed the improvement loop: spot weak spots → add **evaluation** cases ([Lab 06](./06-test-evaluate-monitor.md)) → adjust **instructions / skills / knowledge** → **republish**.

---

## ✅ Mission Complete — Field Manual Cleared 🎖️

You built **Rex, your help desk buddy**, entirely in the **new** Copilot Studio:

- Created the agent from **Instructions** on the **Build** tab, with **Settings**, a greeting, and suggested prompts
- Grounded him with **Knowledge** and enabled **Memory**
- Authored four reusable **markdown Skills** (`password-reset`, `vpn-troubleshooting`, `smart-triage`, `software-installation-request`)
- Equipped **Tools** (Outlook **Send an email**, SharePoint **Create item**) and logged tickets end-to-end — with a generated **PDF** report
- Automated **manager approvals** with the new **Workflows** designer, called from a skill
- **Evaluated** with a quick conversation set, then **Published** to Teams + Microsoft 365 Copilot, **Shared**, and **Monitored**

No topics. No triggers. All new experience. 🚀 *#EPPC26*

## 📚 Tactical Resources

- 🔗 [Key concepts — Publish and deploy your agent](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels)
- 🔗 [Connect and configure an agent for Teams and Microsoft 365](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
- 📺 [Reza Dorrani — Microsoft Rebuilt Copilot Studio](https://www.youtube.com/watch?v=CaEEv9Y-ibs)
