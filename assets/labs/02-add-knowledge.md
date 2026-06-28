# 📚 Mission 02: Ground Rex with Knowledge

| 🕵️ Codename | ⭐ Difficulty | ⏱️ Time | 🧩 Products | 🏷️ Tags | 🏭 Industry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPERATION SOURCE OF TRUTH | ⭐ | 25 min | Copilot Studio (new experience), SharePoint | Knowledge, Memory | IT |

🎥 **Watch the Walkthrough** — *Grounding the help desk agent with knowledge*
▶️ https://www.youtube.com/watch?v=CaEEv9Y-ibs&t=270s

---

## 🎯 Mission Brief

Rex can talk, but he doesn't know Contoso's help desk hours or which software needs approval. **Knowledge** fixes that. In the new experience you add knowledge right on the **Build** tab, and the orchestrator decides which sources to search per question. You'll upload the two documents from Lab 00, turn on **Memory**, and run Rex's first real test.

## 🔎 Objectives

1. Add **Knowledge** to Rex — by uploading documents (and know the other options)
2. Turn on **Memory**
3. Run a first **Preview** test and watch Rex search knowledge and load built-in skills

---

## 📥 Knowledge options in the new experience

From the **Knowledge** block you can ground Rex with:

- **Uploaded documents** (Word, PDF, etc.) — what we'll use
- **Public websites**
- **SharePoint** sites and **OneDrive** libraries
- **Microsoft IQ** for organizational M365 data

> The orchestrator chooses which sources to search automatically — you don't route questions to sources like you did with classic topics.

---

## 🧪 Lab 02: Upload knowledge and enable memory

### Prerequisites

- **Rex** from [Lab 01](./01-build-helpdesk-agent.md).
- The two documents from [Lab 00](./00-course-setup.md): **Contoso IT FAQ** and **Contoso Approved Software List**.

### 2.1 Upload the two documents

1. On the **Build** tab, open **Knowledge** → choose to **upload** documents.
2. Upload **`Contoso IT FAQ`** (help desk email, helpline number, hours, Q&A).
3. Upload **`Contoso Approved Software List`** (apps + self-service vs. manager sign-off).
4. Wait until both show as added/ready.

> 💡 You could also point Knowledge at the **IT Help Desk SharePoint site** instead of (or in addition to) uploads — useful when the content already lives in SharePoint. For this workshop, uploads keep everyone's data identical.

### 2.2 Turn on Memory

1. In the **Memory** block, toggle **Memory on** and **Save**.
2. This lets Rex carry context across turns (and conversations) for better follow-ups.

### 2.3 First test in Preview

1. Open **Preview** and select the suggested prompt **Help desk hours** (or type it).
2. Watch what Rex does:
   - searches the **knowledge base**, then
   - **loads skills** — including the **built-in skills** that can read Word, PowerPoint, and PDF files, then
   - answers with the hours, sourced from your **Contoso IT FAQ** document.

   > 👀 As the **maker**, the preview shows this reasoning (search → skill load → answer). That visibility is your main debugging tool throughout these labs.
3. Try a software question:

   ```text
   Can I install Power BI Desktop?
   ```

   Rex explores the **Approved Software List**, sees Power BI is **self-service**, and replies that no manager approval is needed (plus install guidance). Flip the **end-user** preview toggle on to see the cleaner, user-facing version — then back off to keep the detailed maker view.

---

## ✅ Mission Complete

Rex now answers from your Contoso docs and remembers context. He still can't *do* anything — reset a password, log a ticket — because those need **Skills** and **Tools**. Skills are next.

⏭️ Next: [**Mission 03 — Teach Rex Skills**](./03-add-a-skill.md)

## 📚 Tactical Resources

- 🔗 [Knowledge overview for agents (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/knowledge-copilot-studio)
- 🔗 [Add knowledge sources to an agent (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/knowledge-add-existing-copilot)
- 🔗 [Use Microsoft IQ (preview)](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/use-microsoft-iq)
