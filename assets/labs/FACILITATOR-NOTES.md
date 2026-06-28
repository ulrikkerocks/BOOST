# 🎤 Facilitator Notes — Build "Rex" in the New Copilot Studio

For Nick. Not for distribution to attendees. Read before you run the workshop.

> ♻️ **v2 — rebuilt from Reza's actual transcript.** These labs now follow the video step-for-step and use the **new experience only** (no topics, no triggers, no activity map, no OData "Get items" lookups). The agent is **Rex, your help desk buddy**.

---

## ⏱️ Timing (≈ 3.5–4 hours with breaks)

| Lab | Budget | Notes |
| :--- | :--- | :--- |
| 00 Setup | 20 min | Pre-provision the **Tickets** list + both knowledge docs + solution before class if you can. |
| 01 Build Rex | 30 min | Core. Cover Settings (solution/moderation/auth), greeting, suggested prompts. |
| 02 Knowledge | 25 min | Uploads index fast; show the maker-vs-end-user preview toggle on "Help desk hours". |
| 03 Skills | 40 min | The headline. Spend time on skill anatomy (name lowercase, description = when-to-activate). |
| 04 Tools + tickets + PDF | 40 min | Highest-risk: connections, send-email context, the live SharePoint create. |
| 05 Workflow | 45 min | The 100-second / parallel "respond to agent" pattern is the key teaching point. |
| 06 Evaluate | 25 min | "Quick conversation set" is a great live demo. |
| 07 Publish/Share/Monitor | 20 min | Consider "publish for yourself" on a shared tenant. |

**90-minute cut:** 00 (pre-done) → 01 → 02 → 03 → 04, then *demo* 05–07.

---

## ✅ Confirm before class

1. **New experience is on.** Each attendee's home page should show **Try it now** (or already be in the new experience). If only classic shows, an admin may need to enable it.
2. **Tickets list.** Your list lives here: `https://agentacademygroupb.sharepoint.com/sites/Recruit25/Lists/Tickets/AllItems.aspx` (Group B tenant — I couldn't read it directly behind sign-in). Open it and confirm the **site URL**, **list name** (`Tickets`), and **column display/internal names + choice values**. In the new experience Rex reads the schema himself via `smart-triage`, so the **site URL + list name** are what matter most for the **Create item** tool.
3. **Knowledge docs.** Have **Contoso IT FAQ** and **Contoso Approved Software List** ready (templates/outlines are in Lab 00). Keep app names consistent — **Power BI Desktop = self-service**, **Microsoft Visio = manager sign-off** drive the demos.
4. **Approvals + manager set.** For Lab 05, the test user must have a **manager** populated in the directory, and Approvals must be available.
5. **Connections.** Pre-authorize Office 365 Outlook, SharePoint, and Office 365 Users to avoid connection-card delays mid-demo.

---

## 🗺️ Coverage map — labs vs. transcript

| Video moment | Lab |
| :--- | :--- |
| Intro, new orchestrator, "Try it now" toggle | 00 |
| Build tab key concepts (Instructions/Knowledge/Memory/Tools/Skills/Connected agents/Model) | 00 + 01 |
| Name "Rex", icon/accent, instructions | 01 |
| Settings (preferred solution, moderation, auth), greeting + 4 suggested prompts | 01 |
| Upload 2 knowledge docs; Memory on | 02 |
| First test "Help desk hours"; maker vs end-user preview | 02 |
| Skills: password-reset, vpn-troubleshooting, smart-triage, software-installation-request; upload/download | 03 |
| Tools: Outlook Send email + SharePoint Create item; AI-fill; user vs maker | 04 |
| Test password reset (email) + log ticket (create item + email) | 04 |
| Update smart-triage to generate + attach PDF | 04 §4.5 |
| No topics / no migration / enhanced orchestration | 00 (+ noted in 01–03) |
| Workflow manager_approval_for_software (get manager, approval, if/else, parallel respond, 100s) | 05 |
| Update software-installation-request to call workflow; test Visio | 05 |
| Evaluations: quick conversation set / CSV; run | 06 |
| Publish (demo website + Teams/M365); open in M365 Copilot; share; Monitor tab | 07 |

Built-in skills (Word/PPT/PDF reading) are noted in Labs 02–04. Connected agents and Model are introduced conceptually in Lab 01 (Reza mentions both but the Rex build doesn't deep-dive them).

---

## ⚠️ Preview-feature fallbacks

- **Skills (03):** if "create from blank" or upload isn't lit up, present the markdown and discuss; the skill bodies in Lab 03 are copy-paste ready.
- **Workflows (05):** if the **new** workflow designer isn't present, the same logic builds as an **agent flow** (get manager → approval → condition → respond, with the parallel respond). The 100-second constraint still applies.
- **Evaluate (06):** if "quick conversation set" is missing, upload a small **CSV** using the scenario table in Lab 06.
- **Tenant hiccup insurance:** record a 5–10 min screen capture of the full Rex happy path in *your* tenant the night before.

---

## 🧩 Naming used across the labs (keep consistent)

- Agent: **Rex, your help desk buddy**
- Solution: **Help Desk Agent**
- Skills: **`password-reset`**, **`vpn-troubleshooting`**, **`smart-triage`**, **`software-installation-request`** (lowercase, hyphens — underscores are invalid)
- Tools: **Office 365 Outlook → Send an email**, **SharePoint → Create item**
- Workflow: **`manager_approval_for_software`**
- SharePoint list: **Tickets** (on the **IT Help Desk** site)
- Knowledge: **Contoso IT FAQ**, **Contoso Approved Software List**

---

## 📂 Files in this set

```
README.md                     ← attendee landing page / curriculum index
00-course-setup.md
01-build-helpdesk-agent.md    ← Build Rex
02-add-knowledge.md           ← Knowledge + Memory
03-add-a-skill.md             ← Teach Rex Skills (4 skills)
04-add-tools.md               ← Tools + log tickets + PDF report
05-add-a-workflow.md          ← Manager-approval workflow
06-test-evaluate-monitor.md   ← Evaluate Rex
07-publish-and-share.md       ← Publish, Share & Monitor
FACILITATOR-NOTES.md          ← this file (don't distribute)
```

Source: Reza Dorrani, *"Microsoft Rebuilt Copilot Studio — Here's Everything New"* (June 2026), full transcript. Format mirrors the Microsoft Agent Academy *Recruit* curriculum.
