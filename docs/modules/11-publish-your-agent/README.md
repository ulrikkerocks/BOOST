# Module 11: Publish Your Agent

**Time:** 30 minutes  
**Scenario:** Deploy to Microsoft Teams and Web

---

## Learning Objectives

By the end of this module, you will be able to:
- Publish an agent to make it available to end users
- Deploy an agent to Microsoft Teams as an app
- Access the agent demo website for testing
- Configure agent settings for production use
- Understand publishing permissions and licensing requirements

## Overview

Your Contoso Helpdesk Agent is fully functional — it has knowledge sources, topics, Adaptive Cards, Agent Flows, and event triggers. Now it's time to **publish** it so real users can access it.

In this module, you'll:
1. Publish the agent (make it production-ready)
2. Deploy it to Microsoft Teams
3. Test it in Teams
4. Explore other publishing channels (web, mobile, M365 Copilot)

Once published, employees can chat with the agent directly in Teams — no need to open Copilot Studio.

---

## What Does "Publishing" Mean?

In Copilot Studio, **publishing** is the process of:
1. **Finalizing changes** — creating a snapshot of the current agent state
2. **Making the agent available** to channels (Teams, web, etc.)
3. **Enabling end-user access** — users can now interact with the live agent

### Published vs. Draft

| State | What It Means | Who Can Access |
|---|---|---|
| **Draft** | Work in progress, unpublished changes | Only you (in the Test pane) |
| **Published** | Production-ready snapshot | End users (via channels: Teams, web, etc.) |

**Important:** The **Test pane** always shows the **latest draft** version. After publishing, there are two versions:
- **Draft** (what you're editing in Copilot Studio)
- **Published** (what end users see in Teams or other channels)

To push new changes to users, you must **publish again**.

---

## Prerequisites for Publishing

Before you can publish, ensure:

1. ✅ **Copilot Studio Authors role** is assigned (you did this in Module 00, Step 4)
2. ✅ **Agent is saved** (all topics, flows, knowledge sources are saved)
3. ✅ **No critical errors** — check for red error indicators in topics

If you skipped Module 00, Step 4 (publishing permissions), go back and complete it now. Without the Copilot Studio Authors role, the **Publish** button will be disabled.

---

## Lab 11.1: Publish the Agent

**Objective:** Create a published version of the Contoso Helpdesk Agent.

### Step 1: Navigate to the Agent Overview Page

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Select **Agents** → **Contoso Helpdesk Agent**
3. You land on the **Overview page**

[SCREENSHOT: Contoso Helpdesk Agent Overview page]

### Step 2: Review the Agent Before Publishing

Before publishing, do a final check:

1. **Test in the Test pane:**
   - Ask a knowledge question: "What's the WiFi password?"
   - Trigger the Device Request topic: "I need a laptop"
   - Verify Adaptive Cards display correctly

2. **Check for errors:**
   - Review the **Topics** section — any topics with error icons?
   - Review **Knowledge** sources — are they all connected?

[SCREENSHOT: Overview page showing no errors, all knowledge sources connected]

3. If everything looks good, proceed to publish

### Step 3: Publish the Agent

1. At the top right of the Overview page, select **Publish**

[SCREENSHOT: Overview page with Publish button highlighted]

2. A confirmation dialog appears:
   - **Title:** "Publish this agent"
   - **Message:** "Publishing will make the latest version of your agent available to users in the channels you've configured."

[SCREENSHOT: Publish confirmation dialog]

3. Select **Publish**

4. Wait while the agent is published (~10 seconds)

5. You'll see a success message: "Your agent has been published"

[SCREENSHOT: Publish success message]

**✅ Checkpoint:** The agent is now published and ready to deploy to channels.

---

## Lab 11.2: Deploy the Agent to Microsoft Teams

**Objective:** Make the agent available as an app in Microsoft Teams.

### Step 1: Navigate to Channels

1. On the **Overview page**, scroll to the **Channels** section (or select **Channels** from the top menu/overflow if not visible on Overview)

> **Note:** In the new UI, **Channels** may be in the top navigation **+8** overflow menu. Select **+8** (or **More**) → **Channels**.

[SCREENSHOT: Overview page or top menu showing Channels option]

2. The **Channels** page opens, showing available channels:
   - **Microsoft Teams**
   - **Demo website**
   - **Mobile app**
   - **Microsoft 365 Copilot** (if you have M365 Copilot licenses)
   - **Custom website**
   - And more

[SCREENSHOT: Channels page showing Microsoft Teams, Demo website, and other channel cards]

### Step 2: Configure the Microsoft Teams Channel

1. Locate the **Microsoft Teams** channel card
2. Select **Turn on** (or **Configure** if already partially set up)

[SCREENSHOT: Microsoft Teams channel card with "Turn on" button]

3. A configuration dialog appears:

**Teams app details:**
- **App name:** `Contoso Helpdesk Agent` (or customize)
- **Short description:** `IT help desk assistant for Contoso employees`
- **Long description:** (optional) Detailed description for the Teams app store
- **Icon:** (optional) Upload a custom icon (512x512 px recommended)

[SCREENSHOT: Teams channel configuration dialog showing app name and description fields]

4. Select **Save** (or **Apply**)

5. The Teams channel status changes to **On** (or **Configured**)

**✅ Checkpoint:** The agent is configured for Microsoft Teams.

### Step 3: Generate the Teams App Package

1. In the **Microsoft Teams** channel card, select **Download** (or **Get Teams manifest**)

[SCREENSHOT: Microsoft Teams channel card showing "Download" or "Get manifest" button]

2. A `.zip` file downloads to your computer:
   - **File name:** `ContosoHelpdeskAgent.zip` (or similar)
   - **Contents:** Teams app manifest JSON and icons

3. Save this file — you'll upload it to Teams in the next step

> **Alternative:** Some environments allow you to **Open in Teams** directly without downloading a zip file. If you see an "Open in Teams" button, select it and skip to Step 5.

[SCREENSHOT: Downloaded Teams app zip file]

**✅ Checkpoint:** You have the Teams app package (.zip file).

### Step 4: Upload the App to Microsoft Teams

1. Open **Microsoft Teams** (desktop app or web: [https://teams.microsoft.com](https://teams.microsoft.com))
2. In the left sidebar, select **Apps** (or the app store icon)

[SCREENSHOT: Teams left sidebar with Apps icon highlighted]

3. In the Apps page, select **Manage your apps** (or **Upload an app** in some versions)
4. Select **Upload a custom app** (or **Upload an app to your org's catalog** if you have admin permissions)

> **Note:** If you see **"Upload a custom app is disabled"**, your tenant admin has restricted custom app uploads. Ask your IT admin to enable custom app uploads or upload the app for you.

[SCREENSHOT: Teams Apps page showing "Upload a custom app" option]

5. Select **Upload for me or my teams** (or **Upload for [Organization]**)

6. Browse to the **ContosoHelpdeskAgent.zip** file you downloaded
7. Select **Open**

8. Teams uploads and installs the app (~5 seconds)

9. The **Contoso Helpdesk Agent** app page appears

[SCREENSHOT: Teams showing Contoso Helpdesk Agent app details page with "Add" button]

### Step 5: Add the Agent to Your Teams Chat

1. On the agent's app page in Teams, select **Add**
2. The agent opens in a **chat window** in Teams

[SCREENSHOT: Teams chat window showing Contoso Helpdesk Agent conversation]

**✅ Checkpoint:** The agent is now available in Microsoft Teams.

---

## Lab 11.3: Test the Agent in Microsoft Teams

**Objective:** Verify the agent works correctly in the Teams environment.

### Step 1: Start a Conversation

1. In the Teams chat with **Contoso Helpdesk Agent**, type:
   ```
   Hi
   ```

2. Press **Enter**

**Expected response:**
- The agent greets you: "Hello! I'm the Contoso IT Help Desk assistant. How can I help you today?"

[SCREENSHOT: Teams chat showing agent greeting]

### Step 2: Ask a Knowledge Question

1. Type:
   ```
   What's the guest WiFi password?
   ```

2. Press **Enter**

**Expected response:**
- The agent searches the knowledge sources (uploaded Guest WiFi guide)
- Returns: "The guest WiFi password is GuestPass2026!"
- Cites the source document

[SCREENSHOT: Teams chat showing WiFi password response with source citation]

### Step 3: Trigger the Device Request Topic

1. Type:
   ```
   I need a laptop
   ```

2. Press **Enter**

**Expected flow:**
- Agent asks: "What type of device do you need?"
- Shows buttons: Laptop, Monitor, Keyboard, Mouse, Headset
- Select **Laptop**
- Agent displays Adaptive Cards with available laptops

[SCREENSHOT: Teams chat showing Device Request topic with Adaptive Card]

3. Select **Request this device** on one of the cards

**Expected result:**
- Agent Flow sends email to IT (you should receive the email if you're using your test address)
- Agent confirms: "Your device request has been noted. An IT team member will follow up soon."

[SCREENSHOT: Teams chat showing confirmation message after device request]

**✅ Checkpoint:** The agent works end-to-end in Microsoft Teams.

---

## Lab 11.4: Access the Demo Website

**Objective:** Test the agent in a web browser (useful for external users or embedding on a website).

### Step 1: Enable the Demo Website Channel

1. Back in **Copilot Studio**, navigate to **Channels** (Overview page → Channels section or top menu → Channels)
2. Locate the **Demo website** channel card
3. Select **Turn on** (or **Configure**)

[SCREENSHOT: Channels page showing Demo website card]

4. The demo website is automatically enabled (no additional configuration needed)

### Step 2: Open the Demo Website

1. In the **Demo website** channel card, select **Go to demo website** (or **Open**)

[SCREENSHOT: Demo website channel card with "Go to demo website" link]

2. A new browser tab opens with the agent embedded in a web page

[SCREENSHOT: Demo website showing chat widget with Contoso Helpdesk Agent]

### Step 3: Test the Agent on the Web

1. In the demo website chat widget, type:
   ```
   Can you help me find a monitor?
   ```

2. Press **Enter**

3. Verify the agent responds and the Device Request topic activates

**✅ Checkpoint:** The agent works on the demo website.

### Step 4: (Optional) Share the Demo Website Link

The demo website URL can be shared with others for testing:
- Copy the URL from the browser address bar
- Share with stakeholders, testers, or colleagues
- They can access the agent without installing Teams or signing in (depending on authentication settings)

> **Note:** By default, the demo website requires authentication (sign-in with an M365 account). To allow anonymous access, adjust the **Authentication** settings in the agent's settings (gear icon ⚙️ → Security → Authentication → **No authentication**).

---

## Publishing to Other Channels

You can also publish the agent to:

### Microsoft 365 Copilot (M365 Copilot Extension)

**Requirements:**
- Users must have **Microsoft 365 Copilot licenses**
- Agent must be published to the **Microsoft 365 Copilot** channel

**Steps:**
1. In **Channels**, select **Microsoft 365 Copilot**
2. Select **Turn on**
3. Configure the agent as a **declarative agent** (similar to Module 03)
4. Publish
5. Users can invoke the agent in M365 Copilot using `@Contoso Helpdesk Agent`

[SCREENSHOT: Channels page showing Microsoft 365 Copilot channel card]

### Custom Website (Embed in Your Own Site)

**Use case:** Embed the agent in your company's internal website or customer support portal.

**Steps:**
1. In **Channels**, select **Custom website**
2. Select **Turn on**
3. Copy the **embed code** (HTML iframe or JavaScript snippet)
4. Paste the code into your website's HTML

[SCREENSHOT: Custom website channel showing embed code]

### Mobile App (Teams Mobile)

The agent automatically works in **Microsoft Teams Mobile** once deployed to the Teams channel (no extra configuration needed).

### Facebook Messenger, Slack, Telegram (via connectors)

Copilot Studio supports additional channels through connectors. These may require additional setup and API keys.

---

## Understanding Agent Analytics

After publishing, you can monitor agent usage and performance.

### Step 1: Open Analytics

1. In Copilot Studio, navigate to **Agents** → **Contoso Helpdesk Agent**
2. Select **Analytics** (top menu or overflow)

[SCREENSHOT: Analytics page showing usage charts]

### Step 2: Review Key Metrics

**Common metrics:**
- **Total sessions** — Number of conversations
- **Engagement rate** — % of sessions where users sent multiple messages
- **Resolution rate** — % of sessions marked as resolved
- **Escalation rate** — % of sessions escalated to human support
- **Top topics** — Most frequently triggered topics
- **Knowledge source performance** — Which sources are used most often

[SCREENSHOT: Analytics dashboard showing session count, engagement rate, and top topics chart]

### Step 3: Use Insights to Improve the Agent

**Example insights:**
- If **escalation rate is high** → Add more knowledge sources or improve instructions
- If **Device Request topic is rarely triggered** → Add more trigger phrases or promote the feature
- If **users abandon sessions early** → Simplify question flows or reduce friction

---

## Troubleshooting Publishing Issues

### Issue 1: Publish Button Is Disabled

**Symptoms:** The Publish button is grayed out or doesn't respond.

**Possible causes:**
- **Copilot Studio Authors role not assigned** (Module 00, Step 4)
- **Agent has critical errors** (red error indicators in topics)
- **Environment-level restrictions**

**Solutions:**
1. Verify the Copilot Studio Authors role is assigned (PPAC → Environments → Security roles)
2. Check for errors in topics:
   - Go to **Topics** → select each topic → look for red error icons
   - Fix any broken Power Fx expressions, missing variables, or invalid nodes
3. Wait 5–10 minutes if you just assigned the Authors role (permissions take time to propagate)

### Issue 2: Agent Doesn't Appear in Teams After Upload

**Symptoms:** Upload the .zip file but the agent doesn't show up in Teams.

**Possible causes:**
- **Zip file is corrupted** or incomplete
- **Custom app uploads are disabled** in your Teams tenant
- **Manifest validation failed**

**Solutions:**
1. Re-download the Teams app package from Copilot Studio
2. Check Teams admin center for custom app upload permissions:
   - Go to [https://admin.teams.microsoft.com](https://admin.teams.microsoft.com)
   - **Teams apps** → **Setup policies** → Verify "Upload custom apps" is enabled
3. Try uploading to **"Upload for me"** instead of **"Upload for my organization"**

### Issue 3: Agent Works in Test Pane But Not in Teams

**Symptoms:** Agent responds correctly in Copilot Studio Test pane but gives errors or no response in Teams.

**Possible causes:**
- **Draft version vs. Published version mismatch** — you're testing the draft, but Teams shows the last published version
- **Publishing didn't complete successfully**
- **Teams app cache issue**

**Solutions:**
1. Publish the agent again to ensure the latest version is live
2. In Teams, remove the agent and re-add it:
   - Right-click the agent in Teams chat → **Uninstall**
   - Re-upload the app package
3. Clear Teams cache (desktop app): Sign out → Close Teams → Delete cache folder → Restart Teams

---

## Key Takeaways

- **Publishing** creates a production-ready snapshot of your agent
- **Channels** determine where users can access the agent (Teams, web, M365 Copilot, etc.)
- **Microsoft Teams** is the most common deployment channel for internal agents
- **Demo website** provides a web-based testing environment and can be shared externally
- **Analytics** help you measure agent performance and identify improvement opportunities
- **Permissions** — the Copilot Studio Authors role is required to publish

---

## What You've Achieved

You've successfully:
- ✅ Published the Contoso Helpdesk Agent
- ✅ Deployed it to Microsoft Teams
- ✅ Tested it end-to-end in Teams
- ✅ Enabled the demo website for web access
- ✅ Learned how to monitor agent performance with Analytics

Your agent is now **live and production-ready**. Employees can access it from Teams and start resolving IT issues, requesting devices, and getting instant help.

---

## Next Steps

In **Module 12: Understanding Licensing**, you'll learn about the licensing and cost models for Copilot Studio — how trials work, when you need paid licenses, and how to estimate costs for production deployments.

Then in **Module 13: Securing Your Recruit Badge**, you'll complete the course and claim your badge!

---

**Course Navigation:** [← Module 10](../10-add-event-triggers/README.md) | [Course Index](../README.md) | [Next: Module 12 →](../12-understanding-licensing/README.md)
