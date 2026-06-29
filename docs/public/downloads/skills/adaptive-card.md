---
name: adaptive-card
description: This is what the adaptive card should look like. Replace the blanks with dynamic values.
---
# Instructions
Never show the JSON — just render it in the conversation with the dynamic values:

{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    { "type": "TextBlock", "text": "🎫 Ticket logged", "weight": "Bolder", "size": "Large" },
    { "type": "TextBlock", "text": "${title}", "wrap": true, "spacing": "None", "isSubtle": true },
    {
      "type": "FactSet",
      "facts": [
        { "title": "Ticket #", "value": "${ticketNumber}" },
        { "title": "Category", "value": "${category}" },
        { "title": "Priority", "value": "${priority}" },
        { "title": "Status", "value": "${status}" },
        { "title": "Requestor", "value": "${requestor}" }
      ]
    }
  ],
  "actions": [
    { "type": "Action.OpenUrl", "title": "View in SharePoint", "url": "${ticketUrl}" }
  ]
}
