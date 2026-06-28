# UI Gap Analysis — Original vs. BOOST Site

**Date:** 2026-06-22
**Original:** https://microsoft.github.io/agent-academy/recruit/
**BOOST:** https://ulrikkerocks.github.io/BOOST/

Comparison of the published BOOST site against the original Microsoft Agent Academy site, to guide redesigning BOOST to "look more like the original."

---

## TL;DR

The two sites are built on **fundamentally different generators with opposite layout philosophies**:

- **Original = VitePress** (a docs generator). Light, structured, with a persistent left sidebar, top-bar dropdown nav, built-in local search, and a right-hand "On this page" outline.
- **BOOST = Jekyll + Minima** (a *blog* theme) with a custom dark "Tech Forward" stylesheet. No sidebar, no search, no per-page TOC; instead every page is dumped into a horizontal link wall across the top.

No amount of CSS tweaking makes Minima look like the original, because the **layout primitives the original relies on (sidebar, TOC, search) don't exist in Minima.** Closing the gap is primarily a *theme* decision, not a styling one.

---

## The original, in detail

**Tech stack** (from `microsoft/agent-academy`):
- VitePress `^2.0.0-alpha.12`, default theme + a small `custom.css` (mostly a speaker grid + light/dark helpers).
- Mermaid for diagrams; custom Vite plugins for "missions" and downloadable files.
- Microsoft Clarity analytics.
- `base: /agent-academy/`, `cleanUrls: true`, **local search** enabled.

**Design language:**
| Aspect | Original |
|---|---|
| Theme mode | **Light by default**, with a dark-mode toggle |
| Top bar | Logo + dropdown nav (Home / Courses / Labs / Events) + search box + GitHub link + theme toggle |
| Left sidebar | **Persistent, hierarchical, collapsible** course tree (Recruit ▸ 13 modules; Operative ▸ …) |
| Right rail | **"On this page"** auto-TOC from headings |
| Typography | VitePress default (Inter), generous line-height, clean hierarchy |
| Accent | Calm blue links on white; restrained, professional |
| Landing | Hero image (Agent Academy robot mascot) + "Mission Objective" sections |
| Feel | Polished product-docs site; easy to navigate a long course |

---

## BOOST, in detail

**Tech stack** (this repo):
- Jekyll + **Minima** theme (`skin: dark`) + custom `docs/assets/main.scss` ("Tech Forward").
- Legacy GitHub Pages build from `/docs`; no `Gemfile`, no Actions, no remote theme.
- No search plugin, no TOC, no nav config.

**Design language:**
| Aspect | BOOST |
|---|---|
| Theme mode | **Dark only**, near-black background |
| Top bar | Minima header lists **every page as a flat horizontal wall of links** (unusable at 14+ pages) |
| Left sidebar | **None** |
| Right rail | **None** (no per-page TOC) |
| Typography | Inter (good), but H1 uses a blue→purple gradient that fights legibility |
| Accent | Blue/purple gradients + glows ("Tech Forward") |
| Landing | **Duplicate H1**, no hero image |
| Feel | A dark blog page, not a course you can navigate |

---

## Side-by-side gap table

| # | Dimension | Original (VitePress) | BOOST (Minima) | Gap |
|---|---|---|---|---|
| 1 | **Primary navigation** | Persistent hierarchical left sidebar | None — horizontal link wall | 🔴 Critical |
| 2 | **Search** | Built-in local search | None | 🔴 Critical |
| 3 | **On-page TOC** | Right-hand "On this page" | None | 🔴 High |
| 4 | **Theme mode** | Light default + dark toggle | Dark only, no toggle | 🟠 Medium (preference) |
| 5 | **Landing page** | Hero image + mission sections | Duplicate H1, no hero | 🟠 Medium |
| 6 | **Course structure visible** | Whole course tree always in view | Not visible | 🔴 High |
| 7 | **Typography/readability** | Clean, calm | Gradient H1, glows | 🟠 Medium |
| 8 | **Breadcrumbs / prev-next** | Prev/next page links at bottom | None | 🟡 Low |
| 9 | **Favicon** | Present | **404 (missing)** | 🟡 Low (bug) |
| 10 | **Mobile nav** | Collapsible drawer | Link wall wraps poorly | 🟠 Medium |

---

## Bugs found on BOOST (fix regardless of theme decision)

1. **Duplicate H1** on the landing page — the Markdown `# …` heading plus a theme-rendered title both show. (Remove the Markdown H1, or use front-matter `title`.)
2. **Favicon 404** — `https://ulrikkerocks.github.io/favicon.ico` is requested and missing (console error). Add a favicon and reference it.
3. **Horizontal nav wall** — Minima renders all pages in the header because each module README is a top-level page with no nav structure.

---

## Options to close the gap

### Option A — Switch to **Just the Docs** (recommended)
Adopt the [Just the Docs](https://just-the-docs.com/) Jekyll theme via `remote_theme: just-the-docs/just-the-docs` (works on GitHub Pages — `jekyll-remote-theme` is whitelisted).

- **Gets us:** persistent hierarchical sidebar, **built-in search**, right-side TOC, light theme (configurable, dark available), clean docs typography, prev/next, mobile drawer. ~90% structural parity with the original.
- **Cost:** add front matter to each page (`nav_order`, `parent`, `title`) to build the sidebar tree; retire the "Tech Forward" SCSS (or port accents as Just-the-Docs color overrides); reorganize nav.
- **Effort:** ~half a day. **Risk:** low (stays on Jekyll/Pages).

### Option B — Keep the dark brand, add the missing structure
Stay on Minima/"Tech Forward" but hand-build a sidebar, search, and TOC.

- **Gets us:** keeps BOOST visually distinct (the original goal in `copilot-instructions.md`).
- **Cost:** substantial custom Liquid/JS/CSS; search needs a plugin or hand-rolled index; ongoing maintenance.
- **Effort:** 1–2+ days. **Risk:** medium (fragile, reinventing what a docs theme gives free).

### Option C — Go full **VitePress** (exact match, same stack)
Migrate BOOST to VitePress like the original.

- **Gets us:** pixel-level parity, same components/plugins, dark+light, best search.
- **Cost:** abandon legacy Jekyll Pages → build with **GitHub Actions** (Node); convert `_config.yml`→`config.mts`, adapt front matter, set `base: /BOOST/`.
- **Effort:** 1–2 days. **Risk:** medium (new build pipeline), but it *is* what the original uses.

---

## Recommendation

**Option A (Just the Docs)** is the best effort-to-result trade: it delivers the original's *structure* (sidebar + search + TOC + clean light layout) while staying on the current GitHub Pages/Jekyll build. Option C is the move only if exact parity or the VitePress component set (missions, download-files) matters. Option B is the move only if keeping the distinct dark brand outranks matching the original.

**Note the tension to resolve first:** the project's own [.github/copilot-instructions.md](../.github/copilot-instructions.md) set out to be *visually distinct* from the original ("custom color palette, avoid Microsoft's colors"). "Make it look more like the original" reverses that. Worth a deliberate decision on **light-and-matching vs. dark-and-distinct** before committing.
