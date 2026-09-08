# BOOST show-notes source of truth

Maintain the show-notes rules in [boost-show-notes/SKILL.md](boost-show-notes/SKILL.md)
and its `references/` folder in `ulrikkerocks/BOOST`. All changes go here first.
The repository currently uses `wip/rig/recruit-course-update` as its default branch;
use the reviewed version on that branch once the proposed addition is merged.

## Use from either assistant

For an assistant working in a checkout, refresh the checkout before starting an
episode and explicitly ask it to read `skills/boost-show-notes/SKILL.md`.
`AGENTS.md` and `CLAUDE.md` point to that same source, without copied rules.

For a chat with GitHub access, use this instruction:

> For BOOST show notes, read `skills/boost-show-notes/SKILL.md` from
> `ulrikkerocks/BOOST` on its current default branch, plus its referenced files.
> Use that version instead of older uploaded copies. Tell me the commit used.
> If you cannot read it, say so and ask for a freshly generated package.

A saved URL or pointer does not grant repository access or guarantee that the
assistant has read the source. Confirm the file was loaded before relying on it.

## When an upload is needed

Run from the repository root:

```text
python scripts/package-boost-show-notes.py
```

This creates `dist/boost-show-notes.skill` (a ZIP containing the skill and its
references) and `dist/boost-show-notes.source.json` with the source commit and
file hashes. Build from a clean, updated checkout for a release. Replace the old
uploaded skill with this package in each tool that needs an upload, using that
tool's supported upload flow. Do not edit a package independently.

Uploaded files are snapshots: they do not automatically synchronize with GitHub.
Claude's current installed skill and ChatGPT project settings have not been
changed by adding these repository files.

## Scope and provenance

The initial source preserves the project's supplied `boost-show-notes.skill`
editorial instructions and all three reference files. The additional output
rules come from the August 2026 Show Notes Creation conversation: retain normal
notes and Review, add the comma-separated credits, add a YouTube Show Notes code
block and optional Events code block, and use plain `-` bullets without escapes.
The explicit requested URL display was `[URL](URL)`; bare URLs remain available
when requested. Examples are formatting examples, not a current event calendar.

The old package's `PROGRESS.md` is a historical development checkpoint, not part
of the maintained skill. It has not been imported as current instructions.
