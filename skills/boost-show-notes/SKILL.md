---
name: boost-show-notes
description: Transform messy OneNote working notes and an episode transcript into polished show notes for the Power Platform Boost Podcast. Use this whenever Ulrikke needs to produce show notes for a new episode — typically she'll paste or upload OneNote content plus a transcript file. Also trigger on "structure show notes", "format the show notes", "make show notes", "Boost Podcast notes", or any mention of finalizing a Boost episode for publication.
---

# Boost Podcast — show notes structuring

This skill turns the raw OneNote working notes that Ulrikke and Nick scribble while recording the Power Platform Boost Podcast into the polished, publication-ready show notes that go on Spotify / Apple Podcasts.

The job is not just reformatting. It is **curation and research**: stripping the recording-shorthand that's only useful to the hosts, validating which items were actually discussed against the transcript, resolving every URL to its real title, and crediting the actual humans behind each piece of work.

## Inputs you should expect

- **OneNote messy notes** — pasted into chat or uploaded as a text/markdown file. The structure is rough: working section headers like *Power Apps / Power Pages / Power Automate / Dynamics 365 / Copilots and AI / Dataverse-Platform-ALM / Other / Community Promo's*, sometimes with sub-headers, numbered items, parenthetical asides, and `(u)` / `(n)` markers showing who's covering each item.
- **Transcript file** — Riverside-style format with `Speaker (HH:MM:SS.ms)` blocks. Used to validate inclusion and item order. Usually in the episode's folder, sometimes uploaded separately.
- Episode number and title — often inferable from filenames or from Ulrikke's message; ask if unclear.

If the transcript isn't available, the skill should still produce a useful draft but flag that order/inclusion validation was skipped.

## The shape of the output

Always start with the literal line `Show notes` (sentence case), then a blank line, then sections. Use plain text for section headers — no markdown headings, no bold. Each item is a markdown bullet on its own line:

```
* [Title](URL) by Author
```

When there is no clean author (Microsoft Learn docs, Microsoft Power Platform blog without a named author), omit `by Author` entirely. When the credit is a team rather than a person, use `by the [Name] team` (e.g., `by the Power CAT team`).

Sections, in order:

1. **Featured section** (optional) — only if the episode has an event/campaign anchor that came up repeatedly (Agent Academy, Color Cloud, MPPC, Ignite, etc.). The skill should NEVER auto-promote a featured section; ask Ulrikke each time whether there is one and what to call it.
2. **News** — everything else, with order following the transcript.
3. **Podcast** (optional) — when one or more podcast/long-form articles got highlighted at the end of the recording. Often a single item.

Sometimes there is no News header at all and items just sit directly under `Show Notes` (EP83). This is rare; default to using `News` unless Ulrikke says otherwise.

### Reference examples

See `references/examples.md` for three complete worked examples (EP83, EP84, EP86) with the OneNote input and the published output side by side. Read it before producing your first draft — it shows how items move between sections, how titles get rewritten, and how authors get credited.

## Step-by-step

### Step 1 — Read both inputs end-to-end

Read the entire OneNote dump and the entire transcript before doing anything. Catalog every item in OneNote with its URL (if any), the OneNote section it appears under, and any cues about who covers it. Then scan the transcript to build a rough ordered list of what was discussed — note URLs spoken out loud, names mentioned, topics introduced.

### Step 2 — Strip the recording shorthand

These are working notes; a lot of what's in OneNote is not for the audience. Strip:

- `(u)`, `(U)`, `(n)`, `(N)` markers — assignment of who covers what during recording.
- Number prefixes like `1.`, `2.`, `3.` used to track recording order. (Don't take them as gospel for the published order — see Step 4.)
- Personal sub-headers used as on-air prompts: *"Win $$$"*, *"Steve built a thing"*, *"Sean did a thing"*, *"And we have one as well!!"*, etc.
- Sub-bullets and indented explanations that describe what the host plans to say (e.g. *"Fun how they run into issues with connection ownership..."*, *"10 tips for the timeline – Second tab, filtering..."*, the `Module 1-5` listings).
- Parenthetical asides about the people involved (e.g. *"(Steve was getting whiny that we weren't mentioning him lately 😂)"*).
- Pasted quotes from LinkedIn posts. Keep the link, drop the quote.
- The entire **Shout out!** section — those are personal thank-yous between Ulrikke and listeners, not show notes content.
- Any item that appears in OneNote but is NOT discussed in the transcript. Confirm with Ulrikke before silently dropping anything substantial.

See `references/stripping.md` for a checklist with examples of each pattern.

### Step 3 — Resolve titles and authors for every item

For each surviving item:

**URL — trust OneNote.** If OneNote provides a URL, use it. Do NOT replace it with a "more canonical" alternative just because one exists. The only reasons to replace:
- The OneNote URL is a LinkedIn safety redirect (`linkedin.com/safety/go/?url=...`) and you can decode the underlying destination — use the destination.
- The OneNote URL is genuinely broken (404, redirect-only with no content).
- A YouTube/LinkedIn shortlink (e.g. `youtu.be/...`) can be normalized to its full form — that's a friendly rewrite, not a replacement.

When OneNote has no URL at all but only a descriptive title (e.g. *"Jonas rapp and xrm fetch xml builder"* or *"NEW Workflows Feature In Copilot Studio (20-Min Full Demo) by Matthew Devaney"*), THEN you go hunt for the URL via web search / fetch. Surface what you found and confirm with `[CHECK URL]` if uncertain.

**Title — prefer OneNote when it's already clean.** If OneNote has a publishable-looking title (e.g. *"Custom tools and rich UI for app-based conversations are now in Public Preview"* — a real headline copied from the page; or *"Modifying PowerApps Ribbon with Gemini/Copilot CLI"* — a clear topical phrase), use it as-is. Don't fetch and substitute the page's own `<title>` just because it differs slightly.

Only fetch and substitute when:
- OneNote has no title, only a URL → fetch the page title.
- OneNote has a fragment / placeholder / hint (*"5 types of apps by Josh and Charles"*, *"Jonas rapp and xrm fetch xml builder"*) that wouldn't read well as published — fetch the canonical title.
- The OneNote text is a quoted excerpt rather than a title — fetch the real title.

A useful test: if you were a listener reading the published show notes, would the OneNote text read naturally as the link label? If yes, keep it. If it reads like a recording-shorthand prompt, fetch the real title.

**Special pattern: `[Real Name] on [Platform]`** — when OneNote has a short line like *"Charles Lamanna on LinkedIn"*, *"Megan Walker on YouTube"*, *"Jukka on his blog"* sitting near a URL, that IS the intended title. It looks like a header, but it's not — it's Ulrikke's clean, minimal label for a person's post when she doesn't want to lift the post's actual long-form headline. Keep it as-is. Distinguish from jokey shorthand like *"Steve built a thing"* / *"Sean did a thing"* / *"Win $$$"*, which use a verb or non-name phrase and ARE stripped.

**If a fetch fails on a LinkedIn (or other) URL and the OneNote item has a pasted quoted excerpt under it**, DO NOT promote that quote to the title — the quote is the post's opening line, not its headline. Mark the item with `[CHECK TITLE]`, include the URL, and surface the quote (plus a candidate title if you can infer one from context) in the Review block so Ulrikke can drop in the real headline herself.

If a fetch fails for other reasons and there's no quote-vs-title ambiguity, just mark `[CHECK TITLE]` so Ulrikke can verify.

**Author** — Add `by [Author Name]` when there is a clear human author. Research/correct names. Patterns seen:
- GitHub usernames decoded to real names: `ToluVictor` → "Tolu Victor", `nickmeron` → "Nir Meron".
- LinkedIn slugs decoded carefully: `valentinicola` → "Nicola Valenti" (the slug puts surname first or last depending on locale — verify by reading the LinkedIn profile name).
- OneNote shorthand expanded: "Josh and Charles" → "Charles Sexton and Josh Giles"; "Ana Black" → "Ania Black" (correct spelling).
- Microsoft official docs / blog posts without a named author: NO `by` suffix.
- Team work: `by the Power CAT team`, `by the Microsoft Power Platform team`.

When in doubt, mark with `[CHECK AUTHOR]` instead of guessing.

### Step 4 — Order items by the transcript

The OneNote order is unreliable. Sometimes Ulrikke numbers items as they're discussed, but not consistently within or across episodes. The transcript is the canonical source of truth for what got covered in what order.

Walk through the transcript chronologically. For each topic raised, find the matching OneNote item and emit it in transcript order. If the transcript discusses something with a URL that you couldn't match to any OneNote item, surface it at the end of the draft as a **Suggested addition** — see Step 6.

### Step 5 — Decide on sections

Before you place items, ask Ulrikke:

- *"Is there a featured anchor topic for this episode (Agent Academy, Color Cloud, an event, a campaign)?"* If yes, ask what to call the section and which items belong there.
- *"Should there be a Podcast section at the bottom?"* Default yes if one of the surviving items is itself a podcast or a long-form career/reflection piece that wasn't a tech news item.

If she says no to both, output one News section.

### Step 6 — Draft and surface decisions

Produce the show notes in canonical format. At the end, before delivering, surface a short **Review** block to Ulrikke covering, in this order:

- **Suggested tail additions** — community plugs at the end of the episode (other podcasts, newsletters, community resources, recurring shout-outs) that came up in the transcript but weren't in OneNote. These are *high-confidence add-to-bottom-of-News* recommendations. Present each with the proposed entry already formatted as `* [Title](URL) by Author` so Ulrikke can copy-paste it in with a yes. These almost always get added.
- **Other suggested additions** — URLs/topics that came up in the transcript but weren't in OneNote and aren't tail community plugs. Lower confidence; Ulrikke decides each.
- **Dropped items** — OneNote items you removed because they didn't appear in the transcript, with a one-line reason each.
- **`[CHECK TITLE]` / `[CHECK URL]` / `[CHECK AUTHOR]` markers** — items where you couldn't confidently resolve something.
- **Ambiguous calls** — anything else worth flagging.

The Review block is for Ulrikke's eyes only — once she accepts the final version, the published show notes are just the clean section blocks above.

## Special cases

- **Release wave episodes** (e.g. EP81 was "2026 Release Wave 1"): these don't get the normal structure. The show notes are typically just the link to the official release wave plan documentation. If Ulrikke says "this is a release wave episode," ask what link she wants and produce a minimal output.
- **Solo episodes / guest episodes**: detect from the transcript who's speaking. The host pair Nick + Ulrikke is the default; if a third speaker appears prominently, ask Ulrikke if the guest should be credited somewhere (often in the episode description, not in the show notes body).
- **No transcript available**: produce a draft from OneNote alone, but be conservative about dropping items (without the transcript you can't tell what was actually discussed) and explicitly note that order may be off.

## Output delivery

Return the final show notes as a plain Markdown code block so it copies cleanly into the podcast platform. Follow it with the Review block in normal prose so it doesn't get accidentally pasted into the description.

### Additional delivery formats (agreed August 2026)

These outputs supplement the existing show notes and Review; they do not replace them. For a full show-notes request, deliver in this order:

1. Normal show notes, in the existing Markdown code block.
2. Review, in normal prose, with the existing review behavior.
3. A comma-separated author/credit list, in show-notes order. Reuse the finalized credits without the leading `by`; retain repeated credits when multiple items credit the same author or team. Omit items with no credit. Preserve team and multi-person credits.
4. A separate YouTube-ready Show Notes code block.
5. A separate Events code block when an event list is supplied.

When Ulrikke requests only one of these outputs (for example, YouTube notes now and Events next), return the requested subset using the already-finalized episode content.

### YouTube Show Notes

Put the entire copyable section inside a fenced `markdown` code block. Start with literal `## Show Notes`, followed by a blank line. Preserve the finalized section labels (such as News and Podcast) as plain text, section order, item order, titles, credits, and URLs. This is a formatting pass over the same finalized notes, not a second curation/research pass.

Use a plain `- ` bullet, never `\- `. Keep each item on one line and put a blank line between items and around section labels. Use the URL itself as the visible link text, matching the requested copy format:

```markdown
## Show Notes

News

- Title (by Author): [URL](URL)

- Title without an author: [URL](URL)

Podcast

- Episode title (by Podcast Name — hosts, with guest Guest Name): [URL](URL)
```

Omit the entire `(by ...)` portion when no credit exists. Preserve full team/group credits; do not invent hosts or guests. An item finalized without a URL remains plain text without a fabricated link or dangling colon. Keep unresolved checks visible and explained in Review; do not silently invent missing details. Explicitly requested bare URLs may replace `[URL](URL)` without changing their destinations.

### YouTube Events

When events are supplied, put them in their own fenced `markdown` code block starting with literal `# Events`, then a blank line. Use:

```markdown
# Events

- Event name (City, Country | Dates): [URL](URL)

- Event name (City | Dates): [URL](URL)
```

Use plain `- ` bullets, never `\- `, one line per event, with a blank line between events. Join wrapped location/date text onto that line and use an unescaped `|`. Preserve the supplied names, location detail, date wording/ranges, URLs, and order; omit country when not supplied. Flag missing details rather than guessing. Do not add events from old examples or research a new calendar during this formatting pass. If events are not supplied, omit this block.
