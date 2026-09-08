# Stripping checklist — what NOT to keep from OneNote

OneNote is the hosts' working scratchpad during recording. A lot of it is for them, not for the audience. Strip everything in this list before publishing.

## Coverage markers

These tell the hosts who's covering an item during recording. They appear in many forms:

- `(u)`, `(U)` — Ulrikke covers this
- `(n)`, `(N)` — Nick covers this
- Sometimes at the end of a line: `... by Megan Walker (u)`
- Sometimes on its own bullet

Strip in all forms. Never appear in published notes.

## Number prefixes

Sometimes Ulrikke or Nick numbers items as they're discussed:

```
        1. https://microsoft.github.io/agent-academy/events/hackathon/
        2. Agent Academy Live | Agent Academy
        3. How to Call Power Automate Flows from a Code App...
```

- These track *recording* order, not section assignment.
- Numbering is inconsistent — sometimes 1-6 then it stops, sometimes restarts, sometimes never used.
- Strip the number prefix. Use the transcript for canonical order.

## Personal sub-headers

Working-section headers like *Power Apps / Power Pages / Copilots and AI* are also stripped — they become `News` (or one of the featured sections). But there's a second category of even shorter, more personal sub-headers that get added on the fly during recording:

- `Win $$$`
- `Steve built a thing`
- `Sean did a thing`
- `And we have one as well!!`
- `Steve was getting whiny that we weren't mentioning him lately 😂`

Always strip. These are on-air prompts, not content.

### NOT shorthand: `[Name] on [Platform]` lines

Distinguish carefully from `[Real Name] on [Platform]` lines:

- `Charles Lamanna on LinkedIn`
- `Megan Walker on YouTube`
- `Jukka on his blog`

These look like sub-headers but they're actually clean published titles. Ulrikke writes them when a person's post doesn't have a great long-form headline (or she just wants a minimal label). Keep them as the title. The giveaway: they contain a real human name + a platform name, and they sit immediately above a URL belonging to that person.

`Steve built a thing` ≠ `Charles Lamanna on LinkedIn`. The first is a verb-based jokey prompt. The second is a publishable title.

## Sub-bullets and inline descriptions

When an item has indented sub-bullets, those are usually talking points the host wrote for themselves:

```
        3. How to Call Power Automate Flows from a Code App (and some gotchas) by Josh and Charles
Fun how they run into issues with connection ownership and connection references
        - Power Apps trigger (when power apps calls a flow), Change package number npm 1.1.1...
        - Run some terminal commands. Just solution flows. Own connection!!
```

Keep only the top-level item. Drop everything indented underneath.

Similarly:

```
https://www.ppcookbook.com/post/time-for-the-timeline by Ana Black
10 tips for the timeline - Second tab, filtering, restrict number of records, enable quick create, HTML formatting, use icons, automate and test
```

The "10 tips for the timeline..." line is a description of the post for the host's reference. Drop it; the published item is just the title and link.

## Module lists / course outlines

```
📢 The FREE Copilot Studio Foundations course is now LIVE on YouTube 👇 by Howdang Rashid
🧭 𝗠𝗼𝗱𝘂𝗹𝗲 𝟭 - Introduction to Copilot Studio
💬 𝗠𝗼𝗱𝘂𝗹𝗲 𝟮 - Building Your First Agent
📚 𝗠𝗼𝗱𝘂𝗹𝗲 𝟯 - Knowledge & Grounding
⚡ 𝗠𝗼𝗱𝘂𝗹𝗲 𝟰 - Agent Actions
🚀 𝗠𝗼𝗱𝘂𝗹𝗲 𝟱 - Publishing & Next Steps
        6. Microsoft Copilot Studio | FULL COURSE for Beginners
```

The Module 1-5 listing is content from the post itself, copy-pasted for reference. Drop it. Keep only the course title and link.

## Quoted blocks from LinkedIn posts

```
https://www.linkedin.com/posts/jukkaniiranen_udpp26-share-...
"The Kit was never a product and therefore it doesn't need to be deprecated. There was no formal support for it - even when the entire governance story of Microsoft's low-code platform relied on it for many years."
Azure Resource Graph APIs
```

The quoted text is for the host's reference during discussion. Drop it. Keep only the link and resolve to the post's actual title.

**Important:** if you can't fetch the URL to get the real title, do NOT promote the quoted excerpt to the title — quotes are post bodies, not headlines. Mark the item with `[CHECK TITLE]` and surface the quote in the Review block as a hint, so Ulrikke can look up and drop in the real LinkedIn headline herself.

## The Shout out! section

Always at the very bottom of OneNote. Looks like:

```
Shout out!
        - To EY Kalman for sending me this t-shirt from PPCC 2025 three times and getting it in return
        - And Sandra Kiel for the Minecraft Pig!
```

These are personal thank-yous between the hosts and listeners. Discussed on-air but **never** appear in published show notes. Strip the entire section.

## Parenthetical asides about people

Anything in parentheses that's personal commentary:

- `(Steve was getting whiny that we weren't mentioning him lately 😂 )`
- `(but only if you're paying attention 😉)`
- `(side note: this is hilarious)`

Strip.

## Items in OneNote but NOT in the transcript

These get dropped:

- EP86 OneNote had `https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/` — not in published notes.
- EP85 OneNote had `https://www.linkedin.com/posts/kierra-dotson-8a2b05111_29-of-employees-admit-to-actively-sabotaging...` — not in published notes.

Always validate with the transcript before dropping anything substantive, and surface the drop in the Review block at the end so Ulrikke can override.

## What NOT to strip

Be conservative about these — they look like noise but are actually content:

- **Author attribution lines** like `by Josh and Charles` — these tell you who to credit.
- **Short hints that ARE the item title**, like `Jonas rapp and xrm fetch xml builder` (no URL, no other text). These are pointers to research — the item needs the real title and URL found.
- **Multiple URLs for the same item** — pick the most canonical one (Microsoft Learn over LinkedIn-share, direct over redirect), don't drop both.
- **Discovery credits** — `Enhanced Authorization = No discovered by Valentin Gasenko` — the "discovered by" is meaningful and the human deserves credit.
