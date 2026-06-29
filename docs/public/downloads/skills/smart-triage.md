---
name: smart-triage
description: Use when an issue can't be resolved in chat or needs admin access and the user agrees to log a ticket.
---
# When to activate
An issue cannot be resolved directly (or needs admin access) and the user agrees
to log a ticket.

# Guidelines
1. Query the IT Help Desk SharePoint site and look up the Tickets list.
2. Understand the schema of the Tickets list columns (Title, Description,
   Status, Priority, Category, Requestor).
3. Create a ticket in the Tickets list using the Create-item tool:
   - Title  = one-line summary
   - Description = symptoms + what was already tried
   - Category = Hardware | Software | Network | Access | Other
   - Priority = Low | Normal | High | Critical (Critical if user is fully blocked)
   - Status = New
4. Send the user a confirmation email (Send-email tool) including the ticket
   number and priority.

# Examples
- "This needs admin access — log a ticket" → create record → email confirmation.

# Notes
Read the live list schema before creating the record so fields map correctly.
