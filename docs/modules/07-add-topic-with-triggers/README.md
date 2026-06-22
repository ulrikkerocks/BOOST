---
title: "07 · Add a Topic with Triggers"
parent: Course Modules
nav_order: 7
---
# Module 07: Add a Topic with Triggers

**Time:** 60 minutes  
**Scenario:** Device Request Topic with SharePoint Data

---

## Learning Objectives

By the end of this module, you will be able to:
- Create a custom topic in the Copilot Studio topic designer
- Configure trigger phrases to activate a topic
- Add question nodes to gather user input
- Use Power Fx expressions to query SharePoint lists
- Store and use variables in a conversation flow
- Display dynamic data in message nodes
- Add conditional branching based on user responses

## Overview

In Module 06, you built a knowledge-based agent that answers questions generatively. Now you'll add a **structured topic** — a conversation flow you design node-by-node.

The **Device Request** topic will:
1. Trigger when users say phrases like "I need a laptop"
2. Ask what type of device they need
3. Query the **Devices** SharePoint list for available items
4. Display matching devices to the user

This topic demonstrates the power of combining **generative AI** (knowledge grounding) with **structured flows** (predictable, step-by-step conversations).

---

## Topics vs. Generative Responses: When to Use Each

| Scenario | Use Generative | Use Topic |
|---|---|---|
| Open-ended Q&A | ✅ | |
| Knowledge base search | ✅ | |
| Multi-step form or wizard | | ✅ |
| Data entry with validation | | ✅ |
| Conditional logic (if/else) | | ✅ |
| Guaranteed behavior | | ✅ |

**For this module:** Device requests need a **topic** because we want to:
- Ask specific questions in a specific order
- Query structured data (SharePoint list)
- Display results in a controlled format

---

## Lab 7.1: Create a New Topic

**Objective:** Create the Device Request topic and configure trigger phrases.

### Step 1: Navigate to the Topics Section

1. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. In the left sidebar, select **Agents**
3. Select your **Contoso Helpdesk Agent**
4. You land on the **Overview page**

5. Scroll to the **Topics** section
6. Select **See all** (or **+ Add a topic**)

[SCREENSHOT: Overview page Topics section with "See all" link]

7. You land on the **Topics** list page

[SCREENSHOT: Topics list page showing system topics and any AI-suggested topics]

### Step 2: Create a New Topic

1. Select **+ New topic** (top toolbar)
2. Select **From blank** (or just "+ New topic" if no template options appear)

[SCREENSHOT: New topic creation dialog showing "From blank" option]

3. The **Topic designer** opens — a visual canvas for building conversation flows

[SCREENSHOT: Topic designer showing blank canvas with trigger and initial message nodes]

### Step 3: Name the Topic

1. At the top of the canvas, you'll see a **Topic name** field (default: "Untitled")
2. Change the name to: `Device Request`

[SCREENSHOT: Topic name field showing "Device Request"]

3. Add a **Description** (optional but recommended):
   ```
   Helps users find and request available devices from the Devices SharePoint list
   ```

### Step 4: Configure Trigger Phrases

Trigger phrases tell the agent when to activate this topic.

1. In the **Trigger** node (top of the canvas), select **Edit** or **+ Add phrases**

[SCREENSHOT: Trigger node with "Edit" or "+ Add phrases" option]

2. Enter the following trigger phrases (one per line or one at a time):
   ```
   I need a device
   I need a laptop
   I need a monitor
   I need a keyboard
   I want to request a device
   Can I get a laptop
   Show me available devices
   Request equipment
   ```

[SCREENSHOT: Trigger phrases list showing all 8 phrases]

3. Select **Save** or **Done**

**How triggers work:**
- When a user says something similar to these phrases, the agent activates this topic
- The LLM matches on **intent**, not exact wording (e.g., "I'd like a laptop please" will also trigger)
- Once triggered, the topic flow takes over the conversation

**✅ Checkpoint:** The Device Request topic has 8 trigger phrases configured.

---

## Lab 7.2: Add a Question Node to Gather Device Type

**Objective:** Ask the user what type of device they need.

### Step 1: Add a Question Node

1. Below the **Trigger** node, select **+ Add node** (or click the **+** button on the connection line)
2. Select **Ask a question**

[SCREENSHOT: Add node menu showing "Ask a question" option]

3. A **Question** node is added to the canvas

[SCREENSHOT: Question node on the canvas]

### Step 2: Configure the Question

1. In the **Question** node, locate the **Ask a question** field
2. Enter the question:
   ```
   What type of device do you need?
   ```

[SCREENSHOT: Question node with question text entered]

3. Below the question, configure the **Response type** (what kind of answer you expect):
   - Select **Multiple choice options** (or **Choice** if that's the label)

4. Add the following choices (one per line or via "+ Add option"):
   ```
   Laptop
   Monitor
   Keyboard
   Mouse
   Headset
   ```

[SCREENSHOT: Question node showing multiple choice options: Laptop, Monitor, Keyboard, Mouse, Headset]

5. The user will see these as buttons or quick replies in the chat

### Step 3: Save the User's Answer to a Variable

1. In the **Question** node, locate the **Save response as** field (may be labeled "Save user response" or "Variable")
2. Select **Create a new variable** (or "+ New variable")
3. Variable name: `DeviceType`
4. Select **Save** or **Done**

[SCREENSHOT: Question node showing "Save response as: DeviceType"]

**What this does:**
- When the user selects "Laptop", the value `Laptop` is stored in the variable `DeviceType`
- You can use this variable later in the flow (e.g., to filter the Devices list)

**✅ Checkpoint:** The topic asks "What type of device do you need?" and stores the answer in the `DeviceType` variable.

---

## Lab 7.3: Query the SharePoint Devices List with Power Fx

**Objective:** Retrieve available devices from the SharePoint list, filtered by the user's choice.

### Step 1: Add a Variable Management Node

We'll use a **Set a variable value** node to run a Power Fx query against the SharePoint list.

1. Below the **Question** node, select **+ Add node**
2. Select **Variable management** → **Set a variable value**

[SCREENSHOT: Add node menu showing "Variable management" > "Set a variable value"]

3. A **Set variable** node is added

[SCREENSHOT: Set variable node on the canvas]

### Step 2: Create a Variable to Store Results

1. In the **Set variable** node, locate the **Variable** field
2. Select **Create a new variable**
3. Variable name: `AvailableDevices`
4. Select **Save**

[SCREENSHOT: Set variable node with "AvailableDevices" variable created]

### Step 3: Write the Power Fx Expression

Now you'll write a Power Fx formula to query the SharePoint list.

1. In the **Set variable** node, locate the **Value** field (or **To value**)
2. Select the **fx** icon to open the formula editor

[SCREENSHOT: Set variable node showing "Value" field with fx icon]

3. Enter the following Power Fx formula:

```powerFx
Filter(
    'Contoso IT'.Devices,
    Category = Topic.DeviceType && Status = "Available"
)
```

**What this formula does:**
- `'Contoso IT'.Devices` — References the **Devices** list on the **Contoso IT** SharePoint site
- `Filter(...)` — Filters the list based on conditions
- `Category = Topic.DeviceType` — Matches the Category column to the user's choice (e.g., "Laptop")
- `Status = "Available"` — Only shows devices with Status = "Available"

[SCREENSHOT: Power Fx formula editor showing the Filter expression]

4. Select **Save** or **Done**

**✅ Checkpoint:** The `AvailableDevices` variable now contains a filtered list of devices matching the user's choice and availability status.

### Power Fx Tips

**Accessing SharePoint data:**
- Syntax: `'SiteName'.ListName`
- If the site name has spaces, wrap it in single quotes: `'Contoso IT'`

**Common operators:**
- `=` — Equals
- `&&` — AND
- `||` — OR
- `>`, `<`, `>=`, `<=` — Comparison

**Referencing variables:**
- Topic-level variables: `Topic.VariableName`
- Global variables: `Global.VariableName`

---

## Lab 7.4: Display the Results to the User

**Objective:** Show the user which devices are available.

### Step 1: Add a Condition Node to Check Results

Before displaying devices, check if any were found.

1. Below the **Set variable** node, select **+ Add node**
2. Select **Add a condition** (or **Condition**)

[SCREENSHOT: Add node menu showing "Add a condition"]

3. A **Condition** node is added with two branches: **True** and **False**

[SCREENSHOT: Condition node showing two branches]

### Step 2: Configure the Condition

1. In the **Condition** node, locate the **Condition** field
2. Select the **fx** icon to open the formula editor
3. Enter:
   ```powerFx
   CountRows(Topic.AvailableDevices) > 0
   ```

**What this checks:**
- `CountRows(...)` — Counts how many devices are in the `AvailableDevices` variable
- `> 0` — If more than 0, condition is **True**; otherwise **False**

[SCREENSHOT: Condition node showing the CountRows formula]

4. Select **Save**

**✅ Checkpoint:** The flow branches based on whether devices were found.

### Step 3: Add a Message Node for "Devices Found" (True Branch)

1. On the **True** branch, select **+ Add node**
2. Select **Send a message**

[SCREENSHOT: Add node menu on True branch showing "Send a message"]

3. A **Message** node is added

4. In the **Message** field, enter:
   ```
   Here are the available {Topic.DeviceType} devices:
   ```

5. Below the message, add a **dynamic list** of devices:
   - Select **Add** → **Table** (or **List**)
   - Configure the table to display device details:
     - **Data source:** `Topic.AvailableDevices`
     - **Columns to show:**
       - `Title` (Device name)
       - `Brand`
       - `Model`
       - `Location`

[SCREENSHOT: Message node showing dynamic table configuration with AvailableDevices as data source]

> **Note:** The exact UI for configuring tables/lists varies. You may need to use Power Fx to format the output. If a visual table isn't available, use a text-based format:

**Alternative (text-based):**
```
Here are the available {Topic.DeviceType} devices:

{ForAll(Topic.AvailableDevices, Title & " - " & Brand & " " & Model & " (Location: " & Location & ")")}
```

6. Select **Save**

**✅ Checkpoint:** If devices are found, the agent displays them in a list or table.

### Step 4: Add a Message Node for "No Devices Found" (False Branch)

1. On the **False** branch, select **+ Add node**
2. Select **Send a message**

[SCREENSHOT: Add node menu on False branch]

3. In the **Message** field, enter:
   ```
   Sorry, there are no available {Topic.DeviceType} devices at the moment. Please contact IT support at support@contoso.com to check availability.
   ```

[SCREENSHOT: Message node on False branch showing "no devices" message]

4. Select **Save**

**✅ Checkpoint:** If no devices are found, the agent explains and suggests contacting IT.

---

## Lab 7.5: Test the Device Request Topic

**Objective:** Verify the topic works end-to-end.

### Step 1: Save the Topic

1. At the top of the topic designer, select **Save** (or **Save topic**)

[SCREENSHOT: Topic designer toolbar with Save button]

2. Wait for the save confirmation

### Step 2: Open the Test Pane

1. Select **Test** (top right) or navigate back to the Overview page
2. The **Test pane** should appear on the right side

[SCREENSHOT: Test pane next to topic designer or Overview page]

3. Select **New test session** (circular arrows icon) to start fresh

### Step 3: Trigger the Topic

1. In the Test pane, type:
   ```
   I need a laptop
   ```

2. Press **Enter**

**Expected flow:**
1. Agent recognizes the trigger phrase and activates the **Device Request** topic
2. Agent asks: **"What type of device do you need?"**
3. You see buttons: Laptop, Monitor, Keyboard, Mouse, Headset

[SCREENSHOT: Test pane showing question with multiple choice buttons]

3. Select **Laptop**

**Expected result:**
- Agent queries the Devices SharePoint list
- Filters for `Category = "Laptop"` and `Status = "Available"`
- Displays matching devices (e.g., "Dell Latitude 7430 - Dell Latitude 7430 (Location: Warehouse A)")

[SCREENSHOT: Test pane showing list of available laptops]

**✅ Checkpoint:** The topic successfully queries SharePoint and displays results.

### Step 4: Test the "No Devices" Path

1. Start a **new test session**
2. Type:
   ```
   I need a webcam
   ```

3. Press **Enter**
4. Select **Headset** (or any category with no "Available" items in your Devices list)

**Expected result:**
- Agent searches for available headsets
- Finds none (assuming you don't have any)
- Displays: "Sorry, there are no available Headset devices at the moment. Please contact IT support..."

[SCREENSHOT: Test pane showing "no devices" message]

**✅ Checkpoint:** The topic handles the "no results" scenario gracefully.

---

## Lab 7.6: Update Agent Instructions to Mention Topics

**Objective:** Tell the agent to suggest the Device Request topic for device-related questions.

### Step 1: Edit Instructions

1. Navigate to the **Overview page**
2. Scroll to the **Instructions** section
3. Select **Edit**

4. Add the following paragraph to the instructions (under the "Response Rules" section):

```
**When to use topics:**
- If the user asks about requesting or finding devices, suggest using the Device Request topic: "I can help you find available devices. Just say 'I need a laptop' or 'request a device' and I'll show you what's available."
- For general device questions (e.g., "What devices do you have?"), search the Devices list and provide a summary.
```

[SCREENSHOT: Instructions editor showing the new "When to use topics" section]

5. Select **Save**

**✅ Checkpoint:** The agent now knows to guide users toward the Device Request topic.

### Step 2: Test the Updated Instructions

1. In the Test pane, start a new session
2. Type:
   ```
   Can you help me get a laptop?
   ```

3. Press **Enter**

**Expected behavior:**
- The agent may trigger the Device Request topic directly (if the phrase matches)
- OR the agent may respond generatively with: "I can help you find available devices. Just say 'I need a laptop'..."

Either response is correct — the agent is learning to guide users.

---

## Understanding Topic Flow Execution

When a topic is triggered, here's what happens:

1. **User sends message** → "I need a laptop"
2. **Agent checks topics** → Matches "I need a laptop" to Device Request topic trigger
3. **Topic activates** → Topic flow takes control
4. **Nodes execute sequentially:**
   - Question node → Asks "What type of device?"
   - User responds → "Laptop"
   - Variable is set → `DeviceType = "Laptop"`
   - Power Fx query runs → Filters SharePoint list
   - Condition checks → Are there results?
   - Message displays → Shows devices or "none found"
5. **Topic ends** → Control returns to generative agent

The user experiences this as a **seamless conversation**, not a rigid form.

---

## Advanced Topic Features (Preview)

You can extend topics with:

### Adaptive Cards (Module 08)
- Instead of plain text lists, display devices in rich, interactive cards
- Show device images, details, and action buttons

### Tool Calls (Module 09)
- Add a node that triggers an **Agent Flow** (e.g., send email when device is requested)

### Validation
- Add validation to question nodes (e.g., "Please select a valid category")

### Loops
- Repeat sections of the flow (e.g., "Would you like to request another device?")

---

## Troubleshooting Common Issues

### Issue 1: Topic Doesn't Trigger

**Symptoms:** Type "I need a laptop" but the agent responds generatively instead of activating the topic.

**Solutions:**
1. Verify trigger phrases are saved in the topic
2. Check the topic is **published** (some environments require explicit publish)
3. Rephrase the trigger more closely (e.g., exact match: "I need a device")
4. Check if another topic with similar triggers is conflicting

### Issue 2: Power Fx Query Returns No Results

**Symptoms:** Agent says "no devices found" even though devices exist.

**Possible causes:**
- SharePoint list name or column name is incorrect
- SharePoint site isn't indexed yet
- Permissions issue

**Solutions:**
1. Test the formula manually:
   - In the Power Fx editor, select **Test formula** (if available)
   - Or add a temporary message node that displays `Topic.AvailableDevices` to see raw results
2. Verify SharePoint connection in the Knowledge section
3. Check SharePoint column names match exactly (case-sensitive)
4. Ensure the Devices list has items with `Status = "Available"`

### Issue 3: Variable Not Saving

**Symptoms:** The agent asks the question but doesn't filter results correctly.

**Solutions:**
1. Verify the **Save response as** field in the Question node is set to `DeviceType`
2. Check the Power Fx formula references `Topic.DeviceType`, not just `DeviceType`
3. Add a debug message node that displays `Topic.DeviceType` to verify the value

---

## Key Takeaways

- **Topics** provide structured, predictable conversation flows
- **Trigger phrases** activate topics when the user's intent matches
- **Question nodes** gather input and save it to variables
- **Power Fx** queries SharePoint lists and manipulates data
- **Condition nodes** create branching logic (if/else)
- **Message nodes** display static or dynamic content
- **Combining generative + topics** = flexible, intelligent agents with structured workflows

---

## What You've Built

You now have an agent with:
- ✅ Generative knowledge base (from Module 06)
- ✅ Structured Device Request topic with:
  - 8 trigger phrases
  - Question node to gather device type
  - Power Fx query to filter SharePoint data
  - Conditional branching for "found" vs "not found"
  - Dynamic display of results

---

## Next Steps

In **Module 08: Enhance with Adaptive Cards**, you'll replace the plain text device list with a rich, interactive **Adaptive Card** that displays:
- Device images (using the `DeviceImage` column from Module 00)
- Formatted device details
- Action buttons (e.g., "Request this device")

Adaptive Cards make your agent's responses visually engaging and user-friendly.

---

**Course Navigation:** [← Module 06](../06-build-custom-agent/README.md) | [Course Index](../README.md) | [Next: Module 08 →](../08-enhance-with-adaptive-cards/README.md)
