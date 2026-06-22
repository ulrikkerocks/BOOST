---
title: "00 · Course Setup"
parent: Course Modules
nav_order: 0
---
# Module 00: Course Setup

**Codename:** OPERATION DEPLOYMENT READY  
**Time:** 30 minutes  
**Scenario:** Contoso Helpdesk Agent

---

## Learning Objectives

By the end of this module, you will be able to:
- Set up a Microsoft 365 account for Copilot Studio
- Activate a Copilot Studio trial environment
- Create a Power Apps Developer environment for testing
- Configure publishing permissions via the Power Platform Admin Center
- Create a SharePoint site with sample data for the hands-on labs

## Overview

Before you can build agents in Copilot Studio, you need the right environment and data. This module walks you through a complete setup process that will support all the labs in this course.

You'll be working with a single scenario throughout the course: **building the Contoso Helpdesk Agent** — an AI assistant that helps employees resolve common IT issues and request devices.

By the end of this setup, you'll have:
- ✅ A Copilot Studio environment ready to build in
- ✅ Publishing permissions configured
- ✅ A SharePoint site with real data to ground your agent

---

## Prerequisites

- **A Microsoft 365 account** with admin permissions  
  (Business Basic trial is sufficient — we'll guide you through signup)
- **A web browser** (Microsoft Edge or Chrome recommended)
- **Willingness to experiment!** This course is hands-on.

---

## Step 1: Get a Microsoft 365 Account

If you already have an M365 account (work, school, or personal), you can use it for this course. If not, you'll need to sign up for a trial.

### Option A: Use an Existing M365 Account

If you have an existing M365 account with **admin permissions**, you can skip to Step 2.

> **Note:** You need admin permissions to create environments and configure publishing settings. If you're using a work account with restricted permissions, ask your IT admin to grant you the **Power Platform Administrator** role, or use Option B.

### Option B: Sign Up for an M365 Business Basic Trial

1. Go to [Microsoft 365 Business Basic Trial](https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-business-basic)
2. Select **Try for free**
3. Enter your email address (use a personal email)
4. Follow the prompts to create a new account:
   - Create a business name (e.g., "Contoso Learning")
   - Set up your admin credentials
   - Verify your phone number

[SCREENSHOT: M365 trial signup page showing "Try for free" button and email entry]

5. Complete the trial activation
6. You'll receive admin access to a new M365 tenant

**Time:** ~5 minutes

---

## Step 2: Start Your Copilot Studio Trial

Now that you have an M365 account, you can activate Copilot Studio.

1. Open a new browser tab
2. Go to [https://aka.ms/TryCopilotStudio](https://aka.ms/TryCopilotStudio)
3. Sign in with the M365 account from Step 1
4. Select your **Country/region** from the dropdown
5. Select **Get started**

[SCREENSHOT: Copilot Studio trial activation page with country selector and "Get started" button]

6. Wait while Copilot Studio provisions your environment (~30 seconds)
7. You'll land on the Copilot Studio **Home page**

[SCREENSHOT: Copilot Studio Home page showing the natural language description box: "Describe what you want your agent to do"]

**✅ Checkpoint:** You should see the Copilot Studio Home page with a description box prompting you to create an agent.

**Time:** ~2 minutes

---

## Step 3: Create a Power Apps Developer Environment

For full testing and publishing capabilities, you'll create a dedicated developer environment. This is free and gives you isolated resources for learning.

### 3.1: Sign Up for the Power Apps Developer Plan

1. Go to [https://powerapps.microsoft.com/developerplan/](https://powerapps.microsoft.com/developerplan/)
2. Select **Get started free**
3. Sign in with the same M365 account
4. Accept the terms and select **Get started**

[SCREENSHOT: Power Apps Developer Plan signup page]

5. A new developer environment will be created (this takes ~2 minutes)

### 3.2: Verify Your Environment

1. Go to [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com)
2. Sign in if prompted
3. In the left navigation, select **Environments**
4. You should see at least two environments:
   - **(default)** or **Contoso (default)**
   - **[Your Name]'s Environment** (the developer environment)

[SCREENSHOT: Power Platform Admin Center showing Environments list with default and developer environments]

**✅ Checkpoint:** You have a developer environment listed in the Power Platform Admin Center.

**Time:** ~5 minutes

---

## Step 4: Enable Publishing Permissions

To publish agents to Microsoft Teams or other channels, you need the **Copilot Studio Authors** role. This is configured in the Power Platform Admin Center using a security group.

> **Why this matters:** Without this role, the **Publish** button will be disabled. This is a common blocker for trial users.

### 4.1: Create a Security Group

1. Go to [https://admin.microsoft.com](https://admin.microsoft.com) (Microsoft 365 Admin Center)
2. In the left navigation, expand **Teams & groups** → select **Active teams & groups**
3. Select **Security groups** tab
4. Select **+ Add a security group**

[SCREENSHOT: M365 Admin Center showing Security groups tab with "Add a security group" button]

5. In the **Set up the basics** step:
   - **Name:** `Copilot Studio Authors`
   - **Description:** `Users allowed to publish Copilot Studio agents`
6. Select **Next**
7. In the **Edit settings** step, leave defaults and select **Next**
8. In the **Review** step, select **Create group**
9. Select **Close** after the group is created

### 4.2: Add Yourself to the Security Group

1. In the **Security groups** list, select the **Copilot Studio Authors** group you just created
2. Select the **Members** tab
3. Select **View all and manage members**
4. Select **+ Add members**
5. Search for your account, select it, and select **Add (1)**
6. Select **Close**

[SCREENSHOT: Security group members page showing "Add members" flow]

**✅ Checkpoint:** You are listed as a member of the **Copilot Studio Authors** group.

### 4.3: Assign the Role in Power Platform Admin Center

1. Go back to [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com)
2. In the left navigation, select **Environments**
3. Select your **developer environment** (e.g., "[Your Name]'s Environment")
4. Select **Settings** in the top toolbar
5. Expand **Users + permissions** → select **Security roles**
6. Select **Copilot Studio Authors** role in the list
7. Select **+ Add people** (or **Edit members**)
8. In the search box, search for the **Copilot Studio Authors** security group
9. Select the group and select **Add**

[SCREENSHOT: PPAC Settings > Security roles > Copilot Studio Authors showing group assignment]

10. Select **Save**

**✅ Checkpoint:** The **Copilot Studio Authors** security group is assigned to the **Copilot Studio Authors** role in your environment.

> **Note:** It may take 5–10 minutes for permissions to propagate. If the **Publish** button is still disabled later in the course, wait a few minutes and refresh the page.

**Time:** ~10 minutes

---

## Step 5: Create the Contoso IT SharePoint Site

Throughout this course, you'll build an agent that helps employees find IT information and request devices. The agent will use a SharePoint site as its knowledge source.

Let's create that site now.

### 5.1: Create the SharePoint Site

1. Go to [https://www.office.com](https://www.office.com) and sign in
2. Select the **App launcher** (nine dots) in the top-left corner
3. Select **SharePoint**
4. Select **+ Create site**
5. Select **Team site**

[SCREENSHOT: SharePoint home showing "Create site" button and Team site option]

6. In the site creation wizard:
   - **Site name:** `Contoso IT`
   - **Site description:** `Internal IT help desk resources and device inventory`
   - **Privacy settings:** Private (only members can access)
7. Select **Next**
8. Add yourself as a member (you should be listed as owner by default)
9. Select **Finish**

[SCREENSHOT: SharePoint site creation wizard showing site name and description fields]

10. The site is created and you land on the home page

**✅ Checkpoint:** You have a SharePoint site called **Contoso IT**.

### 5.2: Create the Devices List

The agent will help employees find available devices using a SharePoint list. Let's create that list and populate it with sample data.

1. On the **Contoso IT** site home page, select **+ New** → **List**

[SCREENSHOT: SharePoint site showing "+ New" menu with "List" option]

2. Select **Blank list**
3. **Name:** `Devices`
4. **Description:** `Available IT devices for employee requests`
5. Select **Create**

The list is created with a default **Title** column.

### 5.3: Add Columns to the Devices List

Now add columns to track device details.

1. In the **Devices** list, select **+ Add column** (top toolbar)
2. Select **Choice** from the dropdown
3. **Name:** `Category`
4. **Choices:** (add these options, one per line)
   ```
   Laptop
   Monitor
   Keyboard
   Mouse
   Headset
   Webcam
   Docking Station
   ```
5. **Default value:** Leave blank
6. Select **Save**

[SCREENSHOT: Add Choice column dialog showing Category column setup with device types]

7. Repeat to add the following columns:

| Column Name | Type | Configuration |
|---|---|---|
| **Brand** | Single line of text | - |
| **Model** | Single line of text | - |
| **Status** | Choice | Choices: `Available`, `Reserved`, `Out of Stock` |
| **Location** | Single line of text | E.g., "Warehouse A" |
| **Notes** | Multiple lines of text | - |

**✅ Checkpoint:** Your **Devices** list has columns: Title, Category, Brand, Model, Status, Location, Notes.

### 5.4: Add Sample Data

Add at least 5 sample devices so the agent has data to search.

1. In the **Devices** list, select **+ New** to add a new item
2. Fill in the fields. Example:

| Title | Category | Brand | Model | Status | Location | Notes |
|---|---|---|---|---|---|---|
| Dell Latitude 7430 | Laptop | Dell | Latitude 7430 | Available | Warehouse A | 16GB RAM, 512GB SSD |
| HP 27-inch Monitor | Monitor | HP | E273 | Available | Warehouse A | Full HD, HDMI |
| Logitech Wireless Keyboard | Keyboard | Logitech | K380 | Available | Warehouse B | Bluetooth, multi-device |
| Apple Magic Mouse | Mouse | Apple | Magic Mouse 2 | Reserved | Warehouse A | Rechargeable |
| Jabra Evolve2 65 | Headset | Jabra | Evolve2 65 | Available | Warehouse B | Active noise cancellation |

3. Select **Save** after each item

[SCREENSHOT: SharePoint Devices list showing sample items in grid view]

**✅ Checkpoint:** Your **Devices** list contains at least 5 items with varied data.

### 5.5: Add an Image Column (for Module 08)

In Module 08, you'll display device images in an Adaptive Card. Let's prepare the column now.

1. In the **Devices** list, select **+ Add column** → **Image**
2. **Name:** `DeviceImage`
3. Select **Save**

4. (Optional) Add sample images:
   - Edit each device item
   - In the **DeviceImage** field, paste a public image URL or upload a local file
   - Example URLs:
     - Laptop: `https://via.placeholder.com/150?text=Laptop`
     - Monitor: `https://via.placeholder.com/150?text=Monitor`
   - Select **Save**

> **Note:** Images are optional for now. You can add real device images later or use placeholders.

**✅ Checkpoint:** Your **Devices** list has a **DeviceImage** column.

**Time:** ~15 minutes

---

## Step 6: Upload the Guest WiFi Document

In Module 06, you'll add a document as a knowledge source. Let's create that document now.

### 6.1: Create the Document

1. Open **Microsoft Word** (or any text editor)
2. Create a new document
3. Add the following content:

```
Guest WiFi Connection Guide

Welcome! Here's how to connect to the Contoso Guest WiFi network.

Network Name (SSID): Contoso-Guest

Steps:
1. Open your device's WiFi settings
2. Select "Contoso-Guest" from the list of networks
3. When prompted, enter the password: GuestPass2026!
4. Accept the terms of use
5. You're connected!

Troubleshooting:
- If the network doesn't appear, make sure WiFi is enabled on your device
- If you can't connect, restart your device and try again
- For further assistance, contact IT Support at support@contoso.com

Note: Guest WiFi has limited access. For full network access, please use your employee credentials.
```

4. Save the file as **Guest WiFi Connection Guide.docx**

[SCREENSHOT: Word document showing Guest WiFi guide content]

### 6.2: Upload to SharePoint

1. Go back to your **Contoso IT** SharePoint site
2. In the left navigation, select **Documents**
3. Select **Upload** → **Files**
4. Select the **Guest WiFi Connection Guide.docx** file
5. Select **Open**

[SCREENSHOT: SharePoint Documents library with uploaded Guest WiFi guide]

**✅ Checkpoint:** The **Guest WiFi Connection Guide.docx** file is uploaded to the **Documents** library on the Contoso IT site.

**Time:** ~5 minutes

---

## Step 7: Bookmark the SharePoint Site URL

You'll need the SharePoint site URL several times during the course. Let's save it now.

1. On the **Contoso IT** site, copy the URL from the browser address bar
2. The URL should look like:  
   `https://[yourtenant].sharepoint.com/sites/ContosoIT`
3. Save this URL in a text file or bookmark it

> **Tip:** You'll use this URL in Module 06 when adding the SharePoint site as a knowledge source.

---

## Summary

Congratulations! You've completed the course setup. You now have:

- ✅ **Microsoft 365 account** with admin access
- ✅ **Copilot Studio trial** activated
- ✅ **Power Apps Developer environment** created
- ✅ **Publishing permissions** configured via security group and PPAC
- ✅ **Contoso IT SharePoint site** with:
  - Devices list (5+ sample items with columns: Title, Category, Brand, Model, Status, Location, Notes, DeviceImage)
  - Guest WiFi Connection Guide document uploaded

You're ready to start building agents!

---

## Key Takeaways

- **Copilot Studio trial:** 30 days (extendable to 90 days) with full capabilities
- **Publishing requires permissions:** Copilot Studio Authors role via security group
- **SharePoint as a knowledge source:** Agents can search SharePoint sites, lists, and documents
- **Developer environments are free:** Power Apps Developer Plan gives you a safe sandbox

---

## Next Steps

In **Module 01: Introduction to Agents**, you'll learn what agents are, how they work, and the different types of agents you can build in Copilot Studio.

---

**Course Navigation:** [Course Index](../README.md) | [Next: Module 01 →](../01-introduction-to-agents/README.md)
