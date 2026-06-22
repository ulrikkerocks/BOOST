---
title: "08 · Enhance with Adaptive Cards"
parent: Course Modules
nav_order: 8
---
# Module 08: Enhance with Adaptive Cards

**Time:** 45 minutes  
**Scenario:** Display Devices in Rich, Interactive Cards

---

## Learning Objectives

By the end of this module, you will be able to:
- Explain what Adaptive Cards are and when to use them
- Add an Adaptive Card node to a topic flow
- Use Power Fx to bind data to Adaptive Card elements
- Display images, text, and buttons in a structured card layout
- Capture user input from Adaptive Card actions
- Test Adaptive Cards in the Test pane

## Overview

In Module 07, you displayed device results as plain text or a basic list. That works, but it's not visually engaging.

In this module, you'll replace the text-based device display with **Adaptive Cards** — rich, interactive UI components that can include:
- Images (device photos)
- Formatted text (title, subtitle, details)
- Buttons (e.g., "Request this device")
- Input fields (for later expansion)

Adaptive Cards make your agent feel polished and professional, especially in channels like Microsoft Teams.

---

## What Are Adaptive Cards?

**Adaptive Cards** are a platform-agnostic schema for UI cards. Originally developed by Microsoft, they're now an open standard supported across:
- Microsoft Teams
- Outlook
- Copilot Studio agents
- Windows notifications
- And more

### Why Use Adaptive Cards?

| Plain Text / List | Adaptive Card |
|---|---|
| Simple, fast to implement | Rich, visual, branded |
| Limited formatting | Full control over layout, images, buttons |
| Plain data dump | Structured, scannable |
| No interactivity | Buttons, input fields, actions |

**Example use cases:**
- **Device catalog** (this module) — Show device images, specs, location
- **Approval requests** — Show request details + Approve/Reject buttons
- **Order confirmation** — Show order summary, total, tracking link
- **Survey or feedback** — Inline rating or comment form

[SCREENSHOT: Example Adaptive Card showing a device with image, title, specs, and "Request" button]

---

## Lab 8.1: Add an Adaptive Card Node to the Device Request Topic

**Objective:** Replace the plain text device list with an Adaptive Card.

### Step 1: Open the Device Request Topic

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Navigate to **Agents** → **Contoso Helpdesk Agent**
3. On the Overview page, scroll to **Topics** → select **See all**
4. Select the **Device Request** topic

[SCREENSHOT: Topics list with Device Request topic highlighted]

5. The topic designer opens

### Step 2: Locate the "Devices Found" Message Node

Recall from Module 07:
- **Condition node** checks if `CountRows(Topic.AvailableDevices) > 0`
- **True branch** → Message node displays devices
- **False branch** → Message node says "no devices found"

We'll replace the **True branch** message node with an Adaptive Card.

[SCREENSHOT: Topic flow showing Condition node with True/False branches]

### Step 3: Delete the Old Message Node (True Branch)

1. On the **True** branch, select the **Message** node
2. Select the **Delete** icon (trash can) or right-click → **Delete**

[SCREENSHOT: Message node on True branch with Delete icon highlighted]

3. The node is removed

### Step 4: Add an Adaptive Card Node

1. On the **True** branch, select **+ Add node**
2. Select **Send a message** (same as before)
3. In the message node, locate the **Add** menu (or format options)
4. Select **Adaptive Card**

[SCREENSHOT: Message node menu showing "Adaptive Card" option]

5. An Adaptive Card editor appears

[SCREENSHOT: Adaptive Card editor with blank canvas or default template]

**✅ Checkpoint:** You've added an Adaptive Card node to the True branch.

---

## Lab 8.2: Design the Adaptive Card Layout

**Objective:** Create a card that displays device information (image, title, brand, model, location).

### Understanding Adaptive Card JSON

Adaptive Cards are defined using **JSON**. Copilot Studio provides a visual editor, but under the hood, it's all JSON.

**Basic structure:**
```json
{
  "type": "AdaptiveCard",
  "version": "1.5",
  "body": [
    {
      "type": "TextBlock",
      "text": "Device Name"
    }
  ]
}
```

### Step 1: Use the Adaptive Card Designer (Visual Editor)

If Copilot Studio provides a **visual Adaptive Card designer**:

1. In the Adaptive Card editor, use the toolbar to add elements:
   - **Image** — For device photo
   - **Text Block** — For device title, brand, model
   - **Column Set** — To arrange elements side-by-side

[SCREENSHOT: Adaptive Card visual designer showing toolbar with Image, TextBlock, ColumnSet options]

2. Drag and drop elements onto the canvas

### Step 2: Switch to Code Editor (Recommended for Precision)

For full control, use the **JSON code editor**:

1. In the Adaptive Card editor, locate the **Code** or **JSON** toggle
2. Select **Code** to view the raw JSON

[SCREENSHOT: Adaptive Card editor showing Code/JSON toggle]

3. You'll see a default card template (or blank card JSON)

### Step 3: Replace with Device Card Template

Delete the existing JSON and replace it with the following:

```json
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    {
      "type": "ColumnSet",
      "columns": [
        {
          "type": "Column",
          "width": "auto",
          "items": [
            {
              "type": "Image",
              "url": "${DeviceImage}",
              "size": "Medium",
              "style": "Default",
              "altText": "Device image"
            }
          ]
        },
        {
          "type": "Column",
          "width": "stretch",
          "items": [
            {
              "type": "TextBlock",
              "text": "${Title}",
              "weight": "Bolder",
              "size": "Large"
            },
            {
              "type": "TextBlock",
              "text": "${Brand} ${Model}",
              "spacing": "None",
              "isSubtle": true
            },
            {
              "type": "TextBlock",
              "text": "Status: ${Status}",
              "spacing": "Small"
            },
            {
              "type": "TextBlock",
              "text": "Location: ${Location}",
              "spacing": "None"
            }
          ]
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.Submit",
      "title": "Request this device",
      "data": {
        "action": "request",
        "deviceTitle": "${Title}"
      }
    }
  ]
}
```

[SCREENSHOT: Adaptive Card code editor showing the JSON template above]

**What this card includes:**
- **ColumnSet** — Two-column layout (image on left, details on right)
- **Image** — Displays the device image (from `DeviceImage` column)
- **TextBlocks** — Title, Brand/Model, Status, Location
- **Action button** — "Request this device" (will be wired in Module 09)

**Data binding:** Notice `${Title}`, `${Brand}`, etc. — these are **placeholders** that will be replaced with actual data using Power Fx.

**✅ Checkpoint:** The Adaptive Card JSON is configured.

---

## Lab 8.3: Bind Data to the Adaptive Card with Power Fx

**Objective:** Connect the card to the `AvailableDevices` variable so it displays real data.

### Step 1: Locate the Data Binding Section

1. In the Adaptive Card node, look for a section labeled:
   - **Data source** or
   - **Bind data** or
   - **For each** (if displaying multiple cards)

[SCREENSHOT: Adaptive Card node showing "Data source" or "Bind data" field]

### Step 2: Configure Data Source

1. In the **Data source** field, select **Power Fx** or **fx** icon
2. Enter the following expression:
   ```powerFx
   Topic.AvailableDevices
   ```

[SCREENSHOT: Data source field showing "Topic.AvailableDevices"]

**What this does:**
- For each item in the `AvailableDevices` variable (the filtered SharePoint list results), display one Adaptive Card
- The card template (`${Title}`, `${Brand}`, etc.) is populated with values from each item

### Step 3: Test Data Binding (Preview)

Some Adaptive Card editors provide a **Preview** or **Sample data** view:

1. Locate the **Preview** button (if available)
2. Enter sample data to see how the card will look:
   ```json
   {
     "Title": "Dell Latitude 7430",
     "Brand": "Dell",
     "Model": "Latitude 7430",
     "Status": "Available",
     "Location": "Warehouse A",
     "DeviceImage": "https://via.placeholder.com/150?text=Laptop"
   }
   ```

3. The preview renders the card with the sample data

[SCREENSHOT: Adaptive Card preview showing populated card with device info and image]

**✅ Checkpoint:** The Adaptive Card is bound to the `AvailableDevices` data source.

---

## Lab 8.4: Handle the Action Button (Optional Preview)

In Module 09, you'll wire the "Request this device" button to an Agent Flow that sends an email. For now, we'll just acknowledge the action.

### Step 1: Add a Message Node After the Adaptive Card

1. Below the Adaptive Card node, select **+ Add node**
2. Select **Send a message**

3. In the **Message** field, enter:
   ```
   Great! Your device request has been noted. An IT team member will follow up soon.
   ```

[SCREENSHOT: Message node with acknowledgment text]

> **Note:** This is a placeholder message. In Module 09, you'll replace this with an Agent Flow that sends an email and creates a record.

4. Select **Save**

**✅ Checkpoint:** The topic flow now includes an Adaptive Card node and a placeholder acknowledgment.

---

## Lab 8.5: Test the Adaptive Card

**Objective:** Verify the Adaptive Card displays correctly with real SharePoint data.

### Step 1: Save the Topic

1. At the top of the topic designer, select **Save**

[SCREENSHOT: Topic designer toolbar with Save button]

2. Wait for the save confirmation

### Step 2: Open the Test Pane

1. Navigate back to the **Overview page** (or stay in the topic designer if the Test pane is visible)
2. In the Test pane, select **New test session** (circular arrows icon)

### Step 3: Trigger the Topic

1. Type:
   ```
   I need a laptop
   ```

2. Press **Enter**

**Expected flow:**
1. Agent asks: "What type of device do you need?"
2. Select **Laptop**
3. Agent displays **Adaptive Cards** for each available laptop

[SCREENSHOT: Test pane showing Adaptive Card with device image, title "Dell Latitude 7430", brand/model, status, location, and "Request this device" button]

**Verify:**
- ✅ Device image displays (if you added images in Module 00)
- ✅ Title, brand, model, status, location are correct
- ✅ Card layout is clean and readable
- ✅ "Request this device" button appears

### Step 4: Test with a Category That Has No Devices

1. Start a new test session
2. Type: `I need a webcam`
3. Select a category with no "Available" items

**Expected result:**
- Agent follows the **False** branch
- Displays: "Sorry, there are no available [category] devices at the moment..."

[SCREENSHOT: Test pane showing "no devices" message for category with no results]

**✅ Checkpoint:** The Adaptive Card displays correctly for available devices, and the "no devices" path still works.

---

## Troubleshooting Adaptive Cards

### Issue 1: Card Doesn't Render (Blank or Error)

**Possible causes:**
- JSON syntax error (missing comma, bracket, etc.)
- Invalid Adaptive Card schema version
- Data binding field name mismatch

**Solutions:**
1. Validate JSON using the [Adaptive Cards Designer](https://adaptivecards.io/designer/)
   - Copy your JSON, paste into the designer, check for errors
2. Verify field names match SharePoint column names exactly: `Title`, `Brand`, `Model`, `Status`, `Location`, `DeviceImage`
3. Check the Adaptive Card version is `1.5` (or lower if your environment doesn't support 1.5)

### Issue 2: Image Doesn't Display

**Possible causes:**
- `DeviceImage` column is empty for that device
- Image URL is broken or private
- Image URL is a SharePoint internal URL (not publicly accessible)

**Solutions:**
1. In SharePoint, verify the `DeviceImage` column has valid URLs or uploaded images
2. Use placeholder images for testing:
   - `https://via.placeholder.com/150?text=Laptop`
   - `https://via.placeholder.com/150?text=Monitor`
3. If using SharePoint-hosted images, ensure they're set to "Anyone with the link" permissions

### Issue 3: Multiple Cards Display When Only One Device Exists

**Symptoms:** You see duplicate cards or more cards than expected.

**Possible causes:**
- Data binding is set to loop through `AvailableDevices`, which is correct
- SharePoint list has duplicate items

**Solution:**
1. Check the SharePoint Devices list — ensure there are no duplicate entries
2. Verify the Power Fx filter is correct (Module 07, Lab 7.3)

---

## Advanced Adaptive Card Features

You can extend Adaptive Cards with:

### Input Fields
Add input fields to collect data directly in the card:
```json
{
  "type": "Input.Text",
  "id": "justification",
  "placeholder": "Why do you need this device?"
}
```

### Action.OpenUrl
Open a link when a button is clicked:
```json
{
  "type": "Action.OpenUrl",
  "title": "View in SharePoint",
  "url": "https://contoso.sharepoint.com/sites/ContosoIT/Lists/Devices"
}
```

### Conditional Formatting
Use `$when` expressions to show/hide elements based on data:
```json
{
  "type": "TextBlock",
  "text": "⚠️ Last one available!",
  "$when": "${Quantity} == 1"
}
```

### Accessibility
Always include `altText` for images and clear button labels for screen readers.

---

## Key Takeaways

- **Adaptive Cards** provide rich, interactive UI for agent responses
- **JSON-based** — defined using the Adaptive Card schema
- **Data binding with Power Fx** — populate cards with dynamic data from variables
- **Platform-agnostic** — cards render beautifully in Teams, Outlook, and web
- **Actions** — buttons can trigger flows, open URLs, or submit data
- **Visual + Code editors** — use the visual designer for quick layouts, code editor for precision

---

## What You've Built

You now have a Device Request topic with:
- ✅ Trigger phrases
- ✅ Question node to gather device type
- ✅ Power Fx query to filter SharePoint data
- ✅ **Adaptive Card** displaying:
  - Device image
  - Title, brand, model, status, location
  - "Request this device" button (wired in Module 09)

---

## Next Steps

In **Module 09: Automate with Agent Flows**, you'll wire the "Request this device" button to an **Agent Flow** that:
- Sends an email to IT with the device request details
- Logs the request in a SharePoint list or Dataverse table
- Confirms the action to the user

You'll also learn about the new **Workflows** experience and how it differs from Agent Flows.

---

**Course Navigation:** [← Module 07](../07-add-topic-with-triggers/README.md) | [Course Index](../README.md) | [Next: Module 09 →](../09-automate-with-agent-flows/README.md)
