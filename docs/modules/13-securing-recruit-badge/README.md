# Module 13: Securing Your Recruit Badge

**Time:** 15 minutes  
**Scenario:** Course Completion and Next Steps

---

## Congratulations!

You've completed the **Copilot Agent Academy — Recruit Course**. 🎉

You've built a production-ready AI agent from scratch — the **Contoso Helpdesk Agent** — with knowledge sources, conversational topics, Adaptive Cards, automation, event triggers, and multi-channel deployment.

This module will guide you through:
1. Verifying you've completed all course requirements
2. Claiming your **Recruit Badge**
3. Exploring advanced learning paths (Special Ops)
4. Joining the Copilot Studio community

---

## Course Completion Checklist

Before claiming your badge, ensure you've completed all the hands-on labs:

### Module 00: Course Setup ✅
- [ ] Created M365 account and Copilot Studio trial
- [ ] Created Power Apps Developer environment
- [ ] Configured Copilot Studio Authors role for publishing
- [ ] Created Contoso IT SharePoint site with Devices list
- [ ] Uploaded Guest WiFi Connection Guide document

### Module 01: Introduction to Agents ✅
- [ ] Understand the difference between LLMs, RAG, and orchestration
- [ ] Know the three types of agents (declarative, custom, autonomous)

### Module 02: Copilot Studio Fundamentals ✅
- [ ] Understand the four building blocks (Knowledge, Tools, Topics, Instructions)
- [ ] Familiar with the Overview page navigation

### Module 03: Declarative Agent for M365 Copilot ✅
- [ ] (Optional) Created a declarative agent for M365 Copilot

### Module 04: Creating a Solution ✅
- [ ] Created a solution publisher ("Contoso")
- [ ] Created a solution ("Contoso Helpdesk Agent")
- [ ] Set the preferred solution in Copilot Studio

### Module 05: Using Pre-Built Agents ✅
- [ ] Explored the agent template gallery
- [ ] Created an agent from a template (IT Help Desk or similar)

### Module 06: Build a Custom Agent ✅
- [ ] Created the Contoso Helpdesk Agent using natural language
- [ ] Configured comprehensive instructions
- [ ] Added knowledge sources:
  - [ ] Contoso IT SharePoint site
  - [ ] Guest WiFi Connection Guide (uploaded document)
  - [ ] Microsoft Support website
  - [ ] General web search (enabled)
- [ ] Tested with at least 4 questions across different knowledge sources

### Module 07: Add a Topic with Triggers ✅
- [ ] Created the "Device Request" topic
- [ ] Configured trigger phrases (e.g., "I need a laptop")
- [ ] Added a question node to gather device type
- [ ] Used Power Fx to query the SharePoint Devices list
- [ ] Displayed results with conditional branching (found vs. not found)

### Module 08: Enhance with Adaptive Cards ✅
- [ ] Replaced plain text results with an Adaptive Card
- [ ] Bound the card to `AvailableDevices` data source
- [ ] Displayed device image, title, brand, model, status, location
- [ ] Added "Request this device" button

### Module 09: Automate with Agent Flows ✅
- [ ] Created the "Send Device Request Email" Agent Flow
- [ ] Configured input parameters (DeviceTitle, UserName)
- [ ] Added Outlook "Send an email" action
- [ ] Called the flow from the Device Request topic
- [ ] Tested end-to-end (email sent when button clicked)

### Module 10: Add Event Triggers ✅
- [ ] Created a Dataverse "Support Ticket" table
- [ ] Created an event trigger ("High Priority Ticket Created")
- [ ] Built the "Escalate High Priority Ticket" topic
- [ ] Configured the topic to send escalation email automatically
- [ ] Tested by creating a high-priority ticket in Dataverse

### Module 11: Publish Your Agent ✅
- [ ] Published the agent
- [ ] Deployed to Microsoft Teams
- [ ] Tested in Teams (asked questions, triggered topics, clicked buttons)
- [ ] Enabled demo website channel

### Module 12: Understanding Licensing ✅
- [ ] Understand trial vs. production licensing
- [ ] Know how messages are counted and billed
- [ ] Can estimate costs for a production deployment

### Module 13: Securing Your Recruit Badge (This Module) ✅
- [ ] Reviewed completion checklist
- [ ] Ready to claim badge

---

## What You've Built

Let's recap the full capabilities of your **Contoso Helpdesk Agent**:

### Conversational AI
- ✅ **Knowledge grounding** — searches SharePoint sites, documents, websites, and the web
- ✅ **RAG-powered responses** — every answer cites sources
- ✅ **Graceful unknowns** — admits "I don't know" instead of hallucinating

### Structured Workflows
- ✅ **Device Request topic** — multi-step conversation with questions and branching
- ✅ **Power Fx queries** — filters SharePoint lists dynamically
- ✅ **Adaptive Cards** — rich UI with images and action buttons

### Automation
- ✅ **Agent Flow** — sends email when device is requested
- ✅ **Input/output parameters** — passes data between topics and flows

### Autonomous Behavior
- ✅ **Event trigger** — monitors Support Ticket table for high-priority items
- ✅ **Auto-escalation** — sends manager email without user input

### Multi-Channel Deployment
- ✅ **Microsoft Teams** — deployed as a Teams app
- ✅ **Demo website** — web-based access for testing
- ✅ **Ready for M365 Copilot** — can be extended as a declarative agent

This is a **production-ready, enterprise-grade AI agent** that could be deployed to thousands of users today.

---

## Claiming Your Recruit Badge

### Step 1: Verify Your Solution

1. Go to [https://make.powerapps.com](https://make.powerapps.com)
2. Select **Solutions**
3. Select **Contoso Helpdesk Agent**
4. Verify the solution contains:
   - **Copilot:** Contoso Helpdesk Agent
   - **Cloud flows:** Send Device Request Email, Send High Priority Escalation Email
   - **Connection references:** SharePoint, Outlook
   - **Tables:** Support Ticket (if created in Module 10)

[SCREENSHOT: Contoso Helpdesk Agent solution showing all components]

**✅ Checkpoint:** Your solution is complete and properly packaged.

### Step 2: Export Your Solution (Proof of Completion)

To demonstrate your work, export the solution as a .zip file.

1. In the **Solutions** page, select **Contoso Helpdesk Agent**
2. Select **Export** (top toolbar)
3. In the export dialog:
   - **Version:** Leave as default or increment to 1.1.0.0
   - **Export as:** **Managed** (for production) or **Unmanaged** (for backup)
4. Select **Export**

[SCREENSHOT: Export solution dialog]

5. Wait while the solution is packaged (~30 seconds)
6. The .zip file downloads to your computer

**✅ Checkpoint:** You have a portable backup of all your work.

### Step 3: Claim Your Badge

> **Note:** Badge claiming process depends on how this course is being delivered. If this is an instructor-led workshop, follow the facilitator's instructions. If this is self-paced, follow the steps below.

#### Option A: Microsoft Learn Badge (If Available)

If this course is part of a Microsoft Learn learning path:

1. Go to [Microsoft Learn](https://learn.microsoft.com)
2. Sign in with your Microsoft account
3. Navigate to the **Copilot Agent Academy** learning path
4. Complete any required knowledge checks or assessments
5. Your badge will appear in your **Profile** → **Achievements**

[SCREENSHOT: Microsoft Learn profile showing Copilot Agent Academy Recruit Badge]

#### Option B: GitHub Repository Badge (Community Edition)

If this course is delivered via GitHub (microsoft/agent-academy):

1. Go to the [Agent Academy GitHub repository](https://github.com/microsoft/agent-academy)
2. Navigate to **Badges** or **Completion** section
3. Follow the instructions to submit proof of completion (screenshot of your published agent in Teams, or exported solution .zip file)
4. Community moderators will review and issue the badge

#### Option C: Workshop Certificate (Instructor-Led)

If this is an instructor-led workshop:

1. Notify the facilitator that you've completed all modules
2. Demonstrate your agent in Teams or the demo website
3. Receive a course completion certificate

---

## Next Steps: From Recruit to Special Ops

Congratulations on completing the Recruit course! You've built a strong foundation. Here's what's next:

### Advanced Learning Paths

**Special Ops (Advanced Course)**  
Covers:
- **Multi-agent orchestration** — build agents that call other agents
- **Model Context Protocol (MCP)** — integrate frontier models (OpenAI, Anthropic, Google)
- **Computer Use agents** — agents that control desktop applications
- **Real-time voice agents** — voice-powered conversational AI
- **Frontier Tuning** — fine-tune models for domain-specific tasks
- **Custom metrics and evals** — measure agent quality and performance
- **Production-grade ALM** — CI/CD pipelines, environment strategies, testing frameworks

**Who should take Special Ops:**
- Agent builders ready for advanced scenarios
- Platform architects designing multi-agent systems
- Teams deploying agents at enterprise scale

### Community and Resources

**Join the Copilot Studio Community:**
- [Copilot Studio Community Forums](https://powerusers.microsoft.com/t5/Copilot-Studio-Community/ct-p/PVACommunity)
- [Power Platform YouTube Channel](https://www.youtube.com/@mspowerplatform)
- **LinkedIn Learning:** Copilot Studio courses
- **Microsoft Learn:** Copilot Studio learning paths

**Stay Updated:**
- [What's New in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new) — monthly feature releases
- [Copilot Studio Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/)
- **Weekly Office Hours:** Join live Q&A sessions with Microsoft product teams

### Build Your Portfolio

Now that you have a complete agent, consider:

1. **Deploy to production** — Get approval to deploy the Contoso Helpdesk Agent (or a similar agent) in your organization
2. **Build a second agent** — Try a different domain (HR, sales, finance) to reinforce your skills
3. **Share your work** — Write a blog post, create a YouTube tutorial, or present at a local user group
4. **Contribute to the community** — Answer questions in forums, share templates, contribute to open-source agent projects

---

## Reflection: What You've Learned

Take a moment to reflect on your journey:

**Technical Skills:**
- ✅ Copilot Studio interface navigation (Overview page, topics, channels)
- ✅ Knowledge source configuration (SharePoint, documents, websites, web search)
- ✅ Instruction writing (system prompts, tone, guardrails)
- ✅ Topic design (triggers, questions, conditions, variables)
- ✅ Power Fx expressions (filtering, counting, data manipulation)
- ✅ Adaptive Card design (JSON schema, data binding)
- ✅ Agent Flow creation (Power Automate-style automation)
- ✅ Event triggers (autonomous agents)
- ✅ Publishing and channel deployment
- ✅ Licensing and cost estimation

**Conceptual Understanding:**
- ✅ LLMs, RAG, and orchestration
- ✅ Generative vs. structured conversation flows
- ✅ When to use topics vs. generative responses
- ✅ Autonomous agents vs. conversational agents
- ✅ Multi-channel deployment strategies
- ✅ Agent analytics and optimization

**Business Value:**
- ✅ How AI agents reduce support burden
- ✅ ROI of automation (fewer manual tasks, faster resolutions)
- ✅ Licensing models and cost-benefit analysis
- ✅ Change management for agent adoption

---

## Continuing Your Learning Journey

### Suggested Projects

**Project 1: Extend the Contoso Helpdesk Agent**
- Add a "Password Reset" topic with step-by-step instructions
- Integrate with a ticketing system (Dataverse, ServiceNow, Jira)
- Add a "Frequently Asked Questions" knowledge source (FAQ document)
- Implement multi-language support (Spanish, French, etc.)

**Project 2: Build a New Agent**
- **HR Onboarding Agent** — help new employees with benefits, policies, first-day setup
- **Sales Qualification Agent** — capture lead info, recommend products, schedule demos
- **Facilities Agent** — book conference rooms, report maintenance issues, check building schedules

**Project 3: Multi-Agent System**
- Build 3 specialized agents (IT, HR, Facilities)
- Create an **Orchestrator Agent** that routes user requests to the right specialist
- Demonstrate agent-to-agent communication

### Certifications

Consider pursuing these certifications:
- **Microsoft Certified: Power Platform Fundamentals (PL-900)**
- **Microsoft Certified: Power Platform Functional Consultant Associate (PL-200)**
- **Microsoft Certified: Power Platform Developer Associate (PL-400)**

---

## Final Thoughts

You started this course with a blank canvas. Now you have:
- ✅ A fully functional, production-ready AI agent
- ✅ Hands-on experience with every major feature of Copilot Studio
- ✅ A portable solution you can import into any environment
- ✅ The knowledge to estimate costs, plan deployments, and optimize performance

**This is just the beginning.**

AI agents are transforming how organizations work — from customer service to IT support, from HR to sales. You now have the skills to be part of that transformation.

**Go build amazing agents. The world is waiting.**

---

## Badge Claim Confirmation

I confirm that I have completed all required labs in the Copilot Agent Academy — Recruit Course and I am ready to claim my badge.

**Agent Name:** Contoso Helpdesk Agent  
**Completion Date:** [Your date]  
**Environment:** [Your developer environment name]

---

## Acknowledgments

Thank you for participating in the **Copilot Agent Academy — Recruit Course**.

**Course Authors:**
- Microsoft Agent Academy Team
- Copilot Studio Product Group
- Power Platform Community Contributors

**Special Thanks:**
- Microsoft Learn content team
- Microsoft MVP contributors
- Workshop facilitators and community moderators

---

## Stay Connected

- **Microsoft Tech Community:** [aka.ms/PowerPlatformCommunity](https://aka.ms/PowerPlatformCommunity)
- **GitHub:** [microsoft/agent-academy](https://github.com/microsoft/agent-academy)
- **Twitter/X:** Follow @MSPowerPlat and #CopilotStudio
- **LinkedIn:** Microsoft Power Platform group

---

## See You in Special Ops! 🚀

Ready for the next level? The **Special Ops** course awaits. You'll build cutting-edge agents with multi-agent orchestration, MCP integration, voice capabilities, and production-grade DevOps.

Until then, keep building, keep learning, and keep pushing the boundaries of what's possible with AI agents.

**Welcome to the Copilot Agent Academy community, Recruit. Your journey has just begun.**

---

**Course Navigation:** [← Module 12](../12-understanding-licensing/README.md) | [Course Index](../README.md) | **[🎓 Claim Badge](#badge-claim-confirmation)**
