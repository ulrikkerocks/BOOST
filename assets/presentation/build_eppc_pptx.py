#!/usr/bin/env python3
"""
Build EPPC Agent Academy Workshop Presentation
Based on EPPC26_SpeakerPPT_TemplateA_Styled.pptx template
Improved: uses all 9 available layout types, BIT mascot on visual slides
"""

import io, os, zipfile as _zip, sys
sys.stdout.reconfigure(encoding='utf-8')
from pptx import Presentation
from pptx.util import Pt, Inches, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

TEMPLATE   = r'c:\Source\BOOST\assets\presentation\EPPC26_SpeakerPPT_TemplateA_Styled.pptx'
COLOR_CLOUD = r'c:\Source\BOOST\assets\presentation\Agent Academy Workshop - Nick and Ulrikke - Color Cloud 2026.pptx'
IMG_DIR    = r'c:\Source\BOOST\assets\presentation\extracted_images'
OUTPUT     = r'c:\Source\BOOST\assets\presentation\EPPC26_AgentAcademy_Workshop_v2.pptx'
OUTPUT_TMP = r'c:\Source\BOOST\assets\presentation\EPPC26_AgentAcademy_Workshop_v2_tmp.pptx'

BIT_IMG    = os.path.join(IMG_DIR, 'image63.png')   # BIT mascot (on all Let's go! slides)

# Mission QR code images (from Color Cloud): small ~17KB images mapped per mission
# Ordering matches Color Cloud "Let's go!" slide sequence
MISSION_QR = {
    '05': os.path.join(IMG_DIR, 'image74.png'),   # Pre-Built Agent
    '03': os.path.join(IMG_DIR, 'image80.png'),   # Declarative Agent
    '04': os.path.join(IMG_DIR, 'image85.png'),   # Creating a Solution
    '06': os.path.join(IMG_DIR, 'image87.png'),   # Custom Agent
    '07': os.path.join(IMG_DIR, 'image89.png'),   # Topics
    '08': os.path.join(IMG_DIR, 'image91.png'),   # Adaptive Cards
    '09': os.path.join(IMG_DIR, 'image94.png'),   # Agent Flow
    '10': os.path.join(IMG_DIR, 'image97.png'),   # Event Triggers
    '11': os.path.join(IMG_DIR, 'image99.png'),   # Publish
    '12': os.path.join(IMG_DIR, 'image101.png'),  # Licensing
    '13': os.path.join(IMG_DIR, 'image74.png'),   # Badge (reuse)
}

# ── layout lookup ──────────────────────────────────────────────────────────────

def get_layout(prs, name):
    for master in prs.slide_masters:
        for layout in master.slide_layouts:
            if layout.name == name:
                return layout
    raise KeyError(f"Layout not found: {name}")

# Layout name shortcuts
L_SPLASH       = "Splash Screen"
L_SECTION      = "Section Break Slide"
L_TITLE_TEXT   = "Main Content : Title + Text Box"
L_DARK_TEXT    = "1_Main Content : Title + Text Box"
L_DUAL         = "Main Content : Title + Dual Text Box"
L_DARK_DUAL    = "Main Content - Dark BKG : Title + Dual Text Box"
L_TITLE_VIS    = "Main Content : Title + Visual Data"
L_DARK_VIS     = "Main Content - Dark BKG : Title + Visual Data"
L_VIS_TEXT     = "Main Content : Visual Data + Text"
L_VIS_ONLY     = "Main Content : Visual Data"
L_DUAL_VIS     = "Main Content : Title + Dual Visual Data"
L_END          = "Dark Content (White Background)"

def add_slide(prs, layout_name):
    return prs.slides.add_slide(get_layout(prs, layout_name))

# ── text helpers ───────────────────────────────────────────────────────────────

def set_ph(slide, idx, lines, bold=None, size=None, italic=None, indent=None):
    """
    Set text on a placeholder.
    lines: str (split on \\n) or list of str/tuple.
    tuple form: (text, level, bold, size)  — level 0=first, 1=sub-bullet
    """
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            tf = ph.text_frame
            tf.word_wrap = True
            if isinstance(lines, str):
                lines = lines.split('\n')
            paras = tf.paragraphs
            for i, line in enumerate(lines):
                p = paras[i] if i < len(paras) else tf.add_paragraph()
                p.clear()
                # Support (text, level, bold, size) tuples
                if isinstance(line, tuple):
                    text  = line[0]
                    level = line[1] if len(line) > 1 else 0
                    b     = line[2] if len(line) > 2 else bold
                    sz    = line[3] if len(line) > 3 else size
                else:
                    text  = line
                    level = indent or 0
                    b     = bold
                    sz    = size
                p.level = level
                run = p.add_run()
                run.text = text
                if b is not None:     run.font.bold   = b
                if sz is not None:    run.font.size   = Pt(sz)
                if italic is not None: run.font.italic = italic
            return ph
    raise ValueError(f"PH idx={idx} not found")

def add_pic(slide, img_path, left, top, width, height):
    """Add a picture to a slide at exact EMU coordinates."""
    if not os.path.exists(img_path):
        return None
    return slide.shapes.add_picture(img_path, Emu(left), Emu(top), Emu(width), Emu(height))

# ── slide-type builders ────────────────────────────────────────────────────────

def section_break(prs, title, size=32):
    s = add_slide(prs, L_SECTION)
    set_ph(s, 10, title, bold=True, size=size)
    return s

def content(prs, title, lines, size=20):
    s = add_slide(prs, L_TITLE_TEXT)
    set_ph(s, 0, title, bold=True, size=28)
    set_ph(s, 11, lines, size=size)
    return s

def content_dark(prs, title, lines, size=20):
    s = add_slide(prs, L_DARK_TEXT)
    set_ph(s, 0, title, bold=True, size=28)
    set_ph(s, 11, lines, size=size)
    return s

def dual(prs, title, left_lines, right_lines, dark=False, size=20):
    layout = L_DARK_DUAL if dark else L_DUAL
    s = add_slide(prs, layout)
    set_ph(s, 0, title, bold=True, size=28)
    set_ph(s, 11, left_lines, size=size)
    set_ph(s, 12, right_lines, size=size)
    return s

def title_visual(prs, title, text_lines, img_path, dark=False, size=20):
    """
    Title + text on left, image on right.
    PH0=title (left half), PH12=text (left half), PH13=image area (right half).
    Coordinates from layout: PH13 at (6157913, 757238) size (5372100, 5200650)
    """
    layout = L_DARK_VIS if dark else L_TITLE_VIS
    s = add_slide(prs, layout)
    set_ph(s, 0, title, bold=True, size=28)
    set_ph(s, 12, text_lines, size=size)
    if img_path and os.path.exists(img_path):
        add_pic(s, img_path, 6157913, 757238, 5372100, 5200650)
    return s

def visual_text(prs, title, text_lines, img_path, size=20):
    """
    Image on left, title + text on right.
    PH0=title (right), PH12=text (right), PH13=image (left).
    Coordinates: PH13 at (742951, 757238) size (5243512, 5200650)
    """
    s = add_slide(prs, L_VIS_TEXT)
    set_ph(s, 0, title, bold=True, size=28)
    set_ph(s, 12, text_lines, size=size)
    if img_path and os.path.exists(img_path):
        add_pic(s, img_path, 742951, 757238, 5243512, 5200650)
    return s

def lets_go(prs, mission_num, label, codename, time_str, products, tags, url_note):
    """
    'Let's Go!' slide: dark, left=mission metadata, right=BIT + QR.
    Uses Main Content - Dark BKG : Title + Dual Text Box.
    BIT and QR code images are added as pictures overlaid on the right column area.
    """
    s = add_slide(prs, L_DARK_DUAL)
    set_ph(s, 0, f"Let's Go!  —  {label}", bold=True, size=26)
    # Left column: mission metadata as structured list
    left = [
        ('CODENAME:', 0, True, 17),
        (codename, 0, False, 16),
        ('', 0, False, 12),
        ('TIME:', 0, True, 17),
        (time_str, 0, False, 16),
        ('', 0, False, 12),
        ('PRODUCTS:', 0, True, 17),
        (products, 0, False, 15),
        ('', 0, False, 12),
        ('TAGS:', 0, True, 17),
        (tags, 0, False, 16),
    ]
    set_ph(s, 11, left)
    # Right column: URL note (image added separately below)
    right = [
        ('Scan the QR code or visit:', 0, False, 16),
        ('', 0, False, 12),
        (url_note, 0, True, 14),
    ]
    set_ph(s, 12, right)
    # Add BIT mascot into the right column area (lower portion)
    # Right column PH12 is at (6372597, 1700213) size (5143128, 4235450)
    # Place BIT in the lower-right of that area
    bit_h = 3000000
    bit_w = 2800000
    add_pic(s, BIT_IMG,
            6372597 + 5143128 - bit_w - 200000,  # right-aligned within right col
            1700213 + 4235450 - bit_h - 100000,  # bottom-aligned
            bit_w, bit_h)
    # Add QR code above BIT
    qr = MISSION_QR.get(mission_num, BIT_IMG)
    if qr and os.path.exists(qr):
        qr_size = 1400000
        add_pic(s, qr,
                6372597 + (5143128 - qr_size) // 2,  # centered horizontally
                1700213 + 200000,
                qr_size, qr_size)
    return s

def debrief(prs, num, questions, right_text=None):
    """Mission debrief: dark dual column. Left: questions, right: reflection prompt."""
    left_lines = [(f'Mission Debrief #{num}', 0, True, 22), ('', 0, False, 10)] + \
                 [(q, 0, False, 20) for q in questions]
    right_lines = right_text or [
        ('Pair up:', 0, True, 20),
        ('Share what you built with the person next to you.', 0, False, 19),
        ('', 0, False, 12),
        ('Take turns demoing — 2 minutes each.', 0, False, 19),
    ]
    s = add_slide(prs, L_DARK_DUAL)
    set_ph(s, 0, f'Mission Debrief #{num}', bold=True, size=28)
    set_ph(s, 11, left_lines)
    set_ph(s, 12, right_lines)
    return s

# ══════════════════════════════════════════════════════════════════════════════
# BUILD THE PRESENTATION
# ══════════════════════════════════════════════════════════════════════════════

prs = Presentation(TEMPLATE)

# Clear ALL existing template example slides
xml_slides = prs.slides._sldIdLst
for sldId in list(xml_slides):
    rId = sldId.get(qn("r:id"))
    xml_slides.remove(sldId)
    try:
        del prs.slides._sldIdLst.part._rels[rId]
    except Exception:
        pass

# ──────────────────────────────────────────────────────────────────────────────
# SLIDE 1 — EPPC Splash Screen
# ──────────────────────────────────────────────────────────────────────────────
add_slide(prs, L_SPLASH)

# ──────────────────────────────────────────────────────────────────────────────
# TITLE SLIDE (Section Break used as title card)
# ──────────────────────────────────────────────────────────────────────────────
s = add_slide(prs, L_SECTION)
set_ph(s, 10,
       "Build Your First AI Agents\nwith Microsoft's Agent Academy\n\n"
       "Nick Doelman & Ulrikke Akerbæk\n"
       "European Power Platform Conference 2026  •  #EPPC26",
       size=22)

# ──────────────────────────────────────────────────────────────────────────────
# SPEAKER BIOS  — use Visual Data + Text (image left, bio right)
# ──────────────────────────────────────────────────────────────────────────────
nick_img = os.path.join(IMG_DIR, 'image55.png')
ulli_img = os.path.join(IMG_DIR, 'image56.jpeg')

visual_text(prs, "Nick Doelman",
            [('Independent Power Platform Architect', 0, True, 20),
             ('', 0, False, 10),
             ('Canada', 0, False, 18),
             ('nick@readyxrm.com', 0, False, 18),
             ('@readyxrm', 0, False, 18),
             ('www.nickdoelman.com', 0, False, 18),
             ('', 0, False, 10),
             ('Power Platform BOOST Podcast', 0, True, 18)],
            nick_img, size=18)

visual_text(prs, "Ulrikke Akerbæk",
            [('Power Platform Practice Lead, Itera', 0, True, 20),
             ('', 0, False, 10),
             ('Norway', 0, False, 18),
             ('me@ulrikke.rocks', 0, False, 18),
             ('@ulrikkeakerbk', 0, False, 18),
             ('ulrikke.akerbak.com', 0, False, 18),
             ('', 0, False, 10),
             ('Power Platform BOOST Podcast', 0, True, 18)],
            ulli_img, size=18)

content(prs, "Power Platform BOOST Podcast",
        [('Co-hosted by Nick Doelman and Ulrikke Akerbæk', 0, True, 20),
         ('', 0, False, 10),
         ('Weekly conversations on Power Platform, Copilot Studio,', 0, False, 18),
         ('AI agents, and everything in between.', 0, False, 18),
         ('', 0, False, 10),
         ('Find us wherever you get your podcasts.', 0, False, 18)],
        size=18)

# ──────────────────────────────────────────────────────────────────────────────
# OPENING / LOGISTICS
# ──────────────────────────────────────────────────────────────────────────────
content(prs, "Who Are You?",
        [('What is your name?', 0, False, 22),
         ('Where are you from?', 0, False, 22),
         ('What is your background?', 0, False, 22),
         ('What do you expect from today?', 0, False, 22)])

content(prs, "Housekeeping",
        [('Workshop environments are ready — credentials on your handout', 0, True, 20),
         ('Install Microsoft Authenticator if you haven\'t already', 0, False, 19),
         ('Set up a dedicated browser profile for the workshop tenant', 0, False, 19),
         ('Environments will expire 30 days after the workshop', 0, False, 19),
         ('', 0, False, 10),
         ('Lab guide:  microsoft.github.io/agent-academy/recruit/', 0, True, 19)],
        size=19)

content(prs, "Tips for Labs",
        [('Open the lab guide on your phone, tablet, or a second screen', 0, False, 20),
         ('Or use Windows split-screen alongside the browser', 0, False, 20),
         ('', 0, False, 10),
         ('Ask your neighbours — collaboration is encouraged!', 0, True, 20),
         ('', 0, False, 10),
         ('Raise your hand if you need help — we\'re here.', 0, False, 20)])

# ──────────────────────────────────────────────────────────────────────────────
# FOUNDATIONS
# ──────────────────────────────────────────────────────────────────────────────
section_break(prs, "Foundations")

content(prs, "What Is Agent Academy?",
        [('Microsoft\'s hands-on curriculum for building agents with Copilot Studio', 0, True, 21),
         ('', 0, False, 10),
         ('Three tiers of training:', 0, False, 20),
         ('Recruit  →  Operative  →  Commander', 1, True, 20),
         ('', 0, False, 10),
         ('Today: Recruit — 13 lessons from zero to deployed agent', 0, False, 20),
         ('', 0, False, 10),
         ('Course site:', 0, False, 18),
         ('microsoft.github.io/agent-academy', 1, True, 18)])

# BIT mascot slide — Visual Data + Text (image left)
visual_text(prs, "Meet BIT!",
            [('BIT is the Agent Academy mascot.', 0, True, 20),
             ('', 0, False, 10),
             ('He guides us through the missions and lessons today.', 0, False, 19),
             ('', 0, False, 10),
             ('Recruit  →  Operative  →  Commander', 0, False, 18),
             ('', 0, False, 10),
             ('Your goal today:', 0, True, 19),
             ('Complete all missions and claim your Recruit badge!', 1, False, 18)],
            BIT_IMG)

content(prs, "What Are Agents?",
        [('LLMs — the AI engine behind conversational agents', 0, True, 20),
         ('Reason over language, generate contextual responses', 1, False, 18),
         ('', 0, False, 8),
         ('RAG — grounding responses in your organisation\'s data', 0, True, 20),
         ('Retrieval-Augmented Generation: retrieve then generate', 1, False, 18),
         ('', 0, False, 8),
         ('Orchestration — coordinating knowledge, skills, and actions', 0, True, 20),
         ('Decides which tool to call, when, and how', 1, False, 18),
         ('', 0, False, 8),
         ('Agents combine all three to understand, reason, and act.', 0, True, 20)])

# Declarative vs. Autonomous — dual column comparison
dual(prs, "Declarative vs. Autonomous Agents",
     [('Declarative Agents', 0, True, 22),
      ('', 0, False, 8),
      ('You write the rules.', 0, False, 19),
      ('The agent follows your prompts', 0, False, 19),
      ('and instructions precisely.', 0, False, 19),
      ('', 0, False, 8),
      ('Predictable and controlled.', 0, True, 18),
      ('Great for specific, repeatable tasks.', 0, False, 18),
      ('', 0, False, 8),
      ('Built in Module 03 today.', 0, False, 17)],
     [('Autonomous Agents', 0, True, 22),
      ('', 0, False, 8),
      ('The agent decides how to act.', 0, False, 19),
      ('Uses AI reasoning to choose actions,', 0, False, 19),
      ('respond to events, and adapt.', 0, False, 19),
      ('', 0, False, 8),
      ('More powerful, less predictable.', 0, True, 18),
      ('Best for proactive, event-driven work.', 0, False, 18),
      ('', 0, False, 8),
      ('Introduced in Module 10 today.', 0, False, 17)])

# Building blocks — dual column
dual(prs, "Copilot Studio: The Four Building Blocks",
     [('Knowledge', 0, True, 22),
      ('What your agent knows.', 0, False, 18),
      ('SharePoint, Dataverse, websites, files.', 1, False, 17),
      ('', 0, False, 8),
      ('Tools', 0, True, 22),
      ('What your agent can do.', 0, False, 18),
      ('Connectors, Agent Flows, APIs.', 1, False, 17)],
     [('Instructions', 0, True, 22),
      ('How your agent behaves.', 0, False, 18),
      ('Persona, tone, rules, and focus.', 1, False, 17),
      ('', 0, False, 8),
      ('Triggers', 0, True, 22),
      ('When your agent acts.', 0, False, 18),
      ('Conversation-started or event-driven.', 1, False, 17),
      ('', 0, False, 8),
      ('All visible on the Overview page.', 0, True, 17)])

# Overview Page — use Title + Visual Data (text left, image right for screenshot)
title_visual(prs, "The Copilot Studio Overview Page  ★ New",
             [('Every agent lands on the Overview page — your main workspace.', 0, True, 18),
              ('', 0, False, 8),
              ('What you\'ll find (scroll down):', 0, False, 18),
              ('Instructions  — system prompt, up to 8,000 chars', 1, False, 17),
              ('Triggers  — event-based activation', 1, False, 17),
              ('Knowledge  — SharePoint, files, websites', 1, False, 17),
              ('Tools  — connectors, Agent Flows, APIs', 1, False, 17),
              ('Topics  — conversational entry points', 1, False, 17),
              ('', 0, False, 8),
              ('Channels is under the +8 overflow tab — not on the canvas!', 0, True, 17),
              ('Test pane always visible on the right.', 0, False, 17)],
             os.path.join(IMG_DIR, 'image62.png'),  # lab tips screenshot
             size=17)

content(prs, "Agenda",
        [('09:00  Intro and foundations', 0, False, 20),
         ('10:00  Mission #1 — Your first agent', 0, False, 20),
         ('10:45  Mission #2 — Build (Declarative, Solutions, Custom)', 0, False, 20),
         ('12:00  Lunch', 0, True, 20),
         ('13:00  Mission #3 — Enhance (Topics, Cards, Flows)', 0, False, 20),
         ('14:30  Mission #4 — Deploy (Triggers, Publishing)', 0, False, 20),
         ('15:30  Mission Complete (Licensing, badge, wrap-up)', 0, False, 20),
         ('16:00  All done!', 0, True, 20)])

# Mission briefing overview — dual column
dual(prs, "Mission Briefing",
     [('Mission #1: Your First Agent', 0, True, 18),
      ('Lesson 05: Using a Pre-Built Agent', 1, False, 16),
      ('', 0, False, 8),
      ('Mission #2: Build', 0, True, 18),
      ('Lesson 03: Declarative Agents', 1, False, 16),
      ('Lesson 04: Creating a Solution', 1, False, 16),
      ('Lesson 06: Custom Agent from Conversation', 1, False, 16),
      ('', 0, False, 8),
      ('Mission #3: Enhance', 0, True, 18),
      ('Lesson 07: Add Topics With Triggers', 1, False, 16),
      ('Lesson 08: Add Adaptive Cards', 1, False, 16),
      ('Lesson 09: Add an Agent Flow', 1, False, 16)],
     [('Mission #4: Deploy', 0, True, 18),
      ('Lesson 10: Add Event Triggers', 1, False, 16),
      ('Lesson 11: Publish Your Agent', 1, False, 16),
      ('', 0, False, 8),
      ('Mission Complete', 0, True, 18),
      ('Lesson 12: Understanding Licensing', 1, False, 16),
      ('Lesson 13: Claim Your Recruit Badge', 1, False, 16),
      ('Plan your first real agent', 1, False, 16),
      ('', 0, False, 8),
      ('Free Play Challenge', 0, True, 18),
      ('Between missions — build your own variation!', 1, False, 16)])

content_dark(prs, "FRAGO (Fragmentary Order)",
             [('FRAGO communicates only what has changed:', 0, True, 22),
              ('new tasks, updated objectives, shifted conditions', 1, False, 19),
              ('', 0, False, 10),
              ('In this workshop, a FRAGO slide means:', 0, False, 20),
              ('the UI changed after the lab guide was written, OR', 1, False, 18),
              ('there is a known glitch — here\'s the fix', 1, False, 18),
              ('', 0, False, 10),
              ('FRAGO overrides the lab guide for that step.', 0, True, 20)])

# ══════════════════════════════════════════════════════════════════════════════
# MISSION #1 — YOUR FIRST AGENT
# ══════════════════════════════════════════════════════════════════════════════
section_break(prs, "Mission #1:\nYour First Agent")

content(prs, "Lesson 05: Using a Pre-Built Agent",
        [('Use a prebuilt template to get your first agent running.', 0, True, 22),
         ('', 0, False, 10),
         ('Browse the template gallery in Copilot Studio', 0, False, 20),
         ('Pick a template, customise it, and test it', 0, False, 20),
         ('', 0, False, 10),
         ('Your first win of the day!', 0, True, 20)])

dual(prs, "Lesson 05: Step by Step",
     [('1. Open Copilot Studio', 0, True, 20),
      ('Navigate to your environment → Create', 1, False, 17),
      ('', 0, False, 8),
      ('2. Browse Templates', 0, True, 20),
      ('Explore the prebuilt gallery → pick one', 1, False, 17),
      ('', 0, False, 8),
      ('3. Customise', 0, True, 20),
      ('Adjust the agent name, greeting, instructions', 1, False, 17)],
     [('4. Orchestration Setting', 0, True, 20),
      ('Agent Settings → ensure Generative AI is ON', 1, False, 17),
      ('(Yes — Responses will be dynamic...)', 1, False, 16),
      ('', 0, False, 8),
      ('5. Test', 0, True, 20),
      ('Open the test pane', 1, False, 17),
      ('Have a conversation with your agent', 1, False, 17),
      ('', 0, False, 8),
      ('🕐  ~30 minutes', 0, True, 17)])

content_dark(prs, "FRAGO: Generative AI Orchestration",
             [('In Agent Settings → Orchestration, ensure this is selected:', 0, True, 20),
              ('', 0, False, 10),
              ('● Yes — Responses will be dynamic, using available', 1, False, 19),
              ('  tools and knowledge as appropriate.', 1, False, 19),
              ('', 0, False, 10),
              ('If set to "No — Use classic orchestration" your agent', 0, False, 18),
              ('will not use knowledge sources effectively.', 0, False, 18),
              ('Switch it to Yes and Save.', 0, True, 18)])

content_dark(prs, "FRAGO: Force Newest Version Dialog",
             [('When publishing you may see a "Force newest version" checkbox.', 0, False, 20),
              ('', 0, False, 10),
              ('This is a new feature (ignore it for this lab).', 0, True, 20),
              ('', 0, False, 10),
              ('Click Publish without checking the box.', 0, False, 20)])

content_dark(prs, "FRAGO: Open Teams in the Browser",
             [('If asked to open the Teams desktop app:', 0, False, 20),
              ('', 0, False, 10),
              ('→  Click "Use the web app instead"', 0, True, 22),
              ('', 0, False, 10),
              ('If Teams desktop opens, simply close it.', 0, False, 20),
              ('We use the Teams web app for all publishing steps.', 0, False, 20)])

lets_go(prs, '05',
        "Mission 05: Using a Pre-Built Agent",
        "OPERATION SAFE TRAVELS",
        "~30 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  Microsoft 365  •  Microsoft Teams",
        "Prebuilt Agents",
        "microsoft.github.io/agent-academy/recruit/mission-05")

debrief(prs, 1,
        ['Q1: What are the four building blocks in Copilot Studio?',
         'Q2: Declarative vs. autonomous — key difference?',
         'Q3: What did you customise in your prebuilt agent?'])

# ══════════════════════════════════════════════════════════════════════════════
# MISSION #2 — BUILD
# ══════════════════════════════════════════════════════════════════════════════
section_break(prs, "Mission #2: Build\nCreating & Packaging Agents")

content(prs, "Lesson 03: Create a Declarative Agent",
        [('Build an agent grounded in a system prompt.', 0, True, 22),
         ('', 0, False, 10),
         ('You write the instructions — the agent\'s personality and purpose', 0, False, 20),
         ('Connect it to Microsoft 365 Copilot', 0, False, 20),
         ('', 0, False, 10),
         ('Key skill: prompt engineering for agents', 0, True, 20)])

dual(prs, "Lesson 03: Step by Step",
     [('1. Create a new agent', 0, True, 20),
      ('Start from blank → name your agent', 1, False, 17),
      ('', 0, False, 8),
      ('2. Write the system prompt', 0, True, 20),
      ('Define purpose, tone, and boundaries', 1, False, 17),
      ('', 0, False, 8),
      ('3. Add to M365 Copilot', 0, True, 20),
      ('Configure the declarative agent channel', 1, False, 17)],
     [('4. Test in Copilot', 0, True, 20),
      ('Verify the agent responds correctly', 1, False, 17),
      ('within M365 Copilot', 1, False, 17),
      ('', 0, False, 8),
      ('Good prompting principles:', 0, True, 18),
      ('Be specific about scope and tone', 1, False, 16),
      ('Define what the agent should NOT do', 1, False, 16),
      ('Set the knowledge grounding rules', 1, False, 16),
      ('', 0, False, 8),
      ('🕐  ~60 minutes', 0, True, 17)])

content_dark(prs, "FRAGO: Publish to Teams — Modal Failure",
             [('If publishing to Teams shows an error modal:', 0, False, 20),
              ('', 0, False, 10),
              ('→  Close the modal using the X (top-right corner)', 0, True, 20),
              ('→  Wait 1–2 minutes for Teams to catch up', 0, True, 20),
              ('→  Publish again from Copilot Studio', 0, True, 20),
              ('', 0, False, 10),
              ('Teams propagation takes a few minutes. Be patient!', 0, False, 18)])

content_dark(prs, "FRAGO: Developer Mode Delay",
             [('If your declarative agent doesn\'t appear in M365 Copilot:', 0, False, 20),
              ('', 0, False, 10),
              ('→  Wait 2–3 minutes and refresh', 0, True, 20),
              ('→  Publish the agent again from Copilot Studio', 0, True, 20),
              ('→  Try in a fresh browser tab or incognito window', 0, True, 20),
              ('', 0, False, 10),
              ('Known delay in tenant propagation. Not a failure!', 0, False, 18)])

lets_go(prs, '03',
        "Mission 03: Deploy a Declarative Agent",
        "OPERATION COPILOT EXTENSION",
        "~60 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  Microsoft 365  •  Teams",
        "Declarative Agents",
        "microsoft.github.io/agent-academy/recruit/mission-03")

content(prs, "Lesson 04: Creating a Solution",
        [('Solutions package your agent for reuse and deployment.', 0, True, 22),
         ('', 0, False, 10),
         ('Move agents between environments  (dev → test → production)', 0, False, 20),
         ('Manage dependencies and version control', 0, False, 20),
         ('', 0, False, 10),
         ('Think of it as the shipping container for your agent.', 0, True, 20)])

dual(prs, "Lesson 04: Step by Step",
     [('1. Create a new solution', 0, True, 20),
      ('Power Apps maker portal → Solutions → New', 1, False, 17),
      ('', 0, False, 8),
      ('2. Add your agent', 0, True, 20),
      ('Add → Existing → Bot → your agent', 1, False, 17),
      ('Include all dependencies', 1, False, 17),
      ('', 0, False, 8),
      ('3. Set as preferred solution', 0, True, 20),
      ('Settings → Advanced → Preferred solution', 1, False, 17)],
     [('4. Review components', 0, True, 20),
      ('Agent, topics, connections, flows', 1, False, 17),
      ('Everything that travels together', 1, False, 17),
      ('', 0, False, 8),
      ('5. Export (optional)', 0, True, 20),
      ('Managed or unmanaged ZIP', 1, False, 17),
      ('Managed = no customisation in target env', 1, False, 16),
      ('', 0, False, 8),
      ('🕐  ~45 minutes', 0, True, 17)])

lets_go(prs, '04',
        "Mission 04: Creating a Solution",
        "OPERATION CTRL-ALT-PACKAGE",
        "~45 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  Microsoft Power Platform",
        "Solutions  •  ALM",
        "microsoft.github.io/agent-academy/recruit/mission-04")

content(prs, "Lesson 06: Create Agent from Conversation",
        [('Build an agent grounded in knowledge sources.', 0, True, 22),
         ('', 0, False, 10),
         ('Connect SharePoint, files, or websites as knowledge', 0, False, 20),
         ('The agent uses RAG to retrieve and generate answers', 0, False, 20),
         ('', 0, False, 10),
         ('This is where agents get smart.', 0, True, 20)])

content_dark(prs, "FRAGO: Set the AI Model to GPT-4.1",
             [('During agent creation, verify the AI model is GPT-4.1:', 0, True, 20),
              ('', 0, False, 10),
              ('Overview page → Details → "Select your agent\'s model"', 1, False, 18),
              ('Choose GPT-4.1 from the dropdown', 1, False, 18),
              ('', 0, False, 10),
              ('GPT-4o was retired in October 2025.', 0, False, 18),
              ('GPT-4.1 is the current default — verify it is selected.', 0, True, 18)])

dual(prs, "Lesson 06: Step by Step",
     [('1. Home → describe your agent', 0, True, 20),
      ('Type what you want it to do in natural language', 1, False, 17),
      ('AI provisions name, instructions, knowledge', 1, False, 17),
      ('', 0, False, 8),
      ('2. Review AI suggestions', 0, True, 20),
      ('Accept or dismiss each suggestion', 1, False, 17),
      ('Suggestions are session-only — don\'t dismiss accidentally', 1, False, 16)],
     [('3. Add knowledge sources', 0, True, 20),
      ('Knowledge → + Add knowledge → SharePoint', 1, False, 17),
      ('Enter your SharePoint site URL', 1, False, 17),
      ('', 0, False, 8),
      ('4. Test with real questions', 0, True, 20),
      ('Ask something only in your SharePoint data', 1, False, 17),
      ('Check sources cited in the response', 1, False, 17),
      ('', 0, False, 8),
      ('🕐  ~75 minutes', 0, True, 17)])

lets_go(prs, '06',
        "Mission 06: Create a Custom Agent",
        "OPERATION AGENT FORGE",
        "~75 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  SharePoint  •  Microsoft Learn",
        "Declarative Agents  •  Knowledge Grounding",
        "microsoft.github.io/agent-academy/recruit/mission-06")

debrief(prs, 2,
        ['Q1: What is the role of a system prompt in a declarative agent?',
         'Q2: Why package an agent into a solution?',
         'Q3: How does knowledge grounding change agent answers?'],
        right_text=[('Share your IT Help Desk agent:', 0, True, 20),
                    ('Ask it something only answerable', 0, False, 18),
                    ('from the SharePoint knowledge source.', 0, False, 18),
                    ('', 0, False, 10),
                    ('Did it cite a source? Did it get it right?', 0, True, 18)])

# ══════════════════════════════════════════════════════════════════════════════
# MISSION #3 — ENHANCE
# ══════════════════════════════════════════════════════════════════════════════
section_break(prs, "Mission #3: Enhance\nTopics, Cards & Flows")

content(prs, "Lesson 07: Add Topics With Triggers",
        [('Topics let you control exactly how the agent responds.', 0, True, 22),
         ('', 0, False, 10),
         ('Define custom question-and-answer paths', 0, False, 20),
         ('Triggers detect when a user asks about a subject', 0, False, 20),
         ('', 0, False, 10),
         ('When AI alone isn\'t enough — Topics give you precision.', 0, True, 20)])

dual(prs, "Lesson 07: Step by Step",
     [('1. Topics tab → + Add a topic → From blank', 0, True, 20),
      ('', 0, False, 8),
      ('2. Name it and add trigger phrases', 0, True, 20),
      ('Phrases the user might say to start this topic', 1, False, 17),
      ('', 0, False, 8),
      ('3. Build the conversation flow', 0, True, 20),
      ('Message nodes, Question nodes, Conditions', 1, False, 17),
      ('Add branching logic by user response', 1, False, 17)],
     [('4. Add Power Fx filter (Adaptive Card lab)', 0, True, 18),
      ('Concatenate("Status eq \'Available\'', 1, False, 14),
      (' and AssetType eq \'", Topic.VarDeviceType, "\'")', 1, False, 14),
      ('', 0, False, 8),
      ('5. Test your topic', 0, True, 20),
      ('Trigger the topic from the test pane', 1, False, 17),
      ('Walk through the full conversation path', 1, False, 17),
      ('', 0, False, 8),
      ('🕐  ~60 minutes', 0, True, 17)])

lets_go(prs, '07',
        "Mission 07: Add a Topic with Triggers",
        "OPERATION STAY ON TOPIC",
        "~60 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  SharePoint",
        "Topics & Dialogs  •  Triggers  •  Power Fx",
        "microsoft.github.io/agent-academy/recruit/mission-07")

content(prs, "Lesson 08: Add Adaptive Cards",
        [('Adaptive Cards give your agent a rich, interactive UI.', 0, True, 22),
         ('', 0, False, 10),
         ('Display forms, buttons, and data inside the chat', 0, False, 20),
         ('Use Power Fx to bind card data to SharePoint lists', 0, False, 20),
         ('Collect structured input — not just free text', 0, False, 20),
         ('', 0, False, 10),
         ('This is where your agent starts looking professional.', 0, True, 20)])

dual(prs, "Lesson 08: Step by Step",
     [('1. Design the Adaptive Card', 0, True, 20),
      ('Use Adaptive Card Designer or build in Copilot Studio', 1, False, 17),
      ('', 0, False, 8),
      ('2. Bind to SharePoint data', 0, True, 20),
      ('Power Fx to pull list items into the card', 1, False, 17),
      ('', 0, False, 8),
      ('3. Add card to your topic', 0, True, 20),
      ('Insert as a Message node in your conversation flow', 1, False, 17)],
     [('4. Handle user input', 0, True, 20),
      ('Capture what the user submits via the card', 1, False, 17),
      ('Store in topic variables for downstream use', 1, False, 17),
      ('', 0, False, 8),
      ('Timing note:', 0, True, 18),
      ('This lab typically takes 60–90 min.', 0, False, 17),
      ('Allocate buffer time — new to JSON? Longer.', 0, False, 17),
      ('', 0, False, 8),
      ('🕐  ~45 min  (allow up to 90)', 0, True, 17)])

lets_go(prs, '08',
        "Mission 08: Enhance with Adaptive Cards",
        "OPERATION INTERFACE UPLIFT",
        "~45–90 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  SharePoint",
        "Adaptive Cards  •  Power Fx",
        "microsoft.github.io/agent-academy/recruit/mission-08")

content(prs, "Lesson 09: Add an Agent Flow",
        [('Agent Flows connect your agent to back-end automation.', 0, True, 22),
         ('', 0, False, 10),
         ('Trigger Power Automate directly from a conversation', 0, False, 20),
         ('Pass Adaptive Card input to a flow for processing', 0, False, 20),
         ('', 0, False, 10),
         ('Your agent can now do things — not just talk.', 0, True, 20)])

# Agent Flows vs. Workflows — dark dual comparison (new 2026 content)
dual(prs, "What's New: Agent Flows vs. Workflows",
     [('Agent Flows  ✅  GA — use these today', 0, True, 20),
      ('', 0, False, 8),
      ('Power Automate-style canvas', 0, False, 18),
      ('Available in all environments', 0, False, 18),
      ('Tightly integrated with topic nodes', 0, False, 18),
      ('Billed within Copilot Studio', 0, False, 18),
      ('', 0, False, 8),
      ('Left sidebar → Flows → New Agent flow', 0, True, 17)],
     [('Workflows  🔬  Preview — early release only', 0, True, 20),
      ('', 0, False, 8),
      ('New redesigned visual canvas', 0, False, 18),
      ('Agent nodes + Prompt nodes', 0, False, 18),
      ('Node-level testing', 0, False, 18),
      ('Early-release environments only', 0, False, 18),
      ('', 0, False, 8),
      ('If you see it: explore after the lab!', 0, True, 17)],
     dark=True)

dual(prs, "Lesson 09: Step by Step",
     [('1. In the topic: + → Add a tool → New Agent flow', 0, True, 20),
      ('Agent Flows designer opens', 1, False, 17),
      ('', 0, False, 8),
      ('2. Add a Send Email action', 0, True, 20),
      ('Use the Office 365 Outlook connector', 1, False, 17),
      ('Configure recipients, subject, body', 1, False, 17),
      ('', 0, False, 8),
      ('3. Publish the flow', 0, True, 20),
      ('Save, publish, return to Copilot Studio', 1, False, 17)],
     [('4. Connect flow to topic', 0, True, 20),
      ('Add a tool → select your published flow', 1, False, 17),
      ('Map Adaptive Card variables to flow inputs', 1, False, 17),
      ('', 0, False, 8),
      ('5. Test end-to-end', 0, True, 20),
      ('Chat → Card → Submit → Flow → Email', 1, False, 17),
      ('The full loop!', 1, True, 17),
      ('', 0, False, 8),
      ('🕐  ~30 minutes', 0, True, 17)])

lets_go(prs, '09',
        "Mission 09: Add an Agent Flow",
        "OPERATION AUTOMATION POWERHOUSE",
        "~30 min  •  Difficulty: ★☆☆",
        "Copilot Studio  •  Power Automate  •  Outlook  •  SharePoint",
        "Automation  •  Agent Flows",
        "microsoft.github.io/agent-academy/recruit/mission-09")

debrief(prs, 3,
        ['Q1: What is a Topic trigger, and when would you use one?',
         'Q2: How do Adaptive Cards improve the user experience?',
         'Q3: What connects a card submission to a back-end action?'],
        right_text=[('Demo your end-to-end flow:', 0, True, 20),
                    ('Chat → Card → Submit → Email sent.', 0, False, 18),
                    ('', 0, False, 10),
                    ('2 minutes each — show your neighbour!', 0, True, 18)])

# ══════════════════════════════════════════════════════════════════════════════
# MISSION #4 — DEPLOY
# ══════════════════════════════════════════════════════════════════════════════
section_break(prs, "Mission #4: Deploy\nEvents, Publishing & Going Rogue")

content(prs, "Lesson 10: Add Event Triggers",
        [('Event triggers make your agent act on its own.', 0, True, 22),
         ('', 0, False, 10),
         ('Respond to things that happen — not just questions', 0, False, 20),
         ('A new SharePoint item, a schedule, an external event', 0, False, 20),
         ('', 0, False, 10),
         ('The agent doesn\'t wait to be asked — it acts.', 0, True, 20)])

content_dark(prs, "FRAGO: Author / Created By Column",
             [('When testing the trigger, the flow may fail:', 0, False, 20),
              ('"Author Display Name" is not available in the SharePoint list view.', 0, True, 19),
              ('', 0, False, 10),
              ('Fix: Add "Created By" to the All Items list view.', 0, True, 20),
              ('', 0, False, 10),
              ('Open the Tickets list → All Items view → Edit columns', 1, False, 17),
              ('→  Add "Created By"  →  Save', 1, False, 17),
              ('Then re-test your trigger.', 0, False, 18)])

dual(prs, "Lesson 10: Step by Step",
     [('1. Overview page → Triggers → + Add trigger', 0, True, 20),
      ('Search for "SharePoint"', 1, False, 17),
      ('Select "When an item is created"', 1, False, 17),
      ('', 0, False, 8),
      ('2. Configure the trigger', 0, True, 20),
      ('SharePoint site URL + list name', 1, False, 17),
      ('', 0, False, 8),
      ('3. Build the autonomous action', 0, True, 20),
      ('Send an email via Outlook connector', 1, False, 17)],
     [('4. Test the trigger', 0, True, 20),
      ('Add a new item to SharePoint list', 1, False, 17),
      ('Wait for email notification to arrive', 1, False, 17),
      ('"Test Trigger" icon on the trigger card', 1, False, 17),
      ('', 0, False, 8),
      ('Important:', 0, True, 18),
      ('Generative AI must be ON (Settings → Orchestration)', 1, False, 16),
      ('Cloud flow is created automatically behind scenes', 1, False, 16),
      ('', 0, False, 8),
      ('🕐  ~45 minutes', 0, True, 17)])

lets_go(prs, '10',
        "Mission 10: Add Event Triggers",
        "OPERATION GHOST ROUTINE",
        "~45 min  •  Difficulty: ★☆☆",
        "Copilot Studio  •  Power Automate  •  Outlook  •  SharePoint",
        "Automation  •  Triggers  •  Autonomous Agents",
        "microsoft.github.io/agent-academy/recruit/mission-10")

content(prs, "Lesson 11: Publish Your Agent",
        [('Ship it. Deploy to where your users are.', 0, True, 22),
         ('', 0, False, 10),
         ('Publish to Microsoft Teams — available in the Teams app store', 0, False, 20),
         ('Publish to M365 Copilot — integrated into the Copilot experience', 0, False, 20),
         ('', 0, False, 10),
         ('Your agent goes from prototype to production.', 0, True, 20)])

content_dark(prs, "FRAGO: Finding the Channels Tab",
             [('Channels is NOT on the Overview page canvas.', 0, True, 20),
              ('', 0, False, 10),
              ('To reach Channels:', 0, False, 20),
              ('1. Open your agent → Overview page', 1, False, 18),
              ('2. Click  +8  in the top tab bar', 1, True, 18),
              ('   (next to the "Overview" tab)', 1, False, 17),
              ('3. Select Channels from the dropdown', 1, False, 18),
              ('', 0, False, 10),
              ('The lab says "Select Channel in the top navigation" — correct.', 0, False, 17),
              ('The +8 overflow is where it lives in the new UI.', 0, True, 17)])

content_dark(prs, "FRAGO: 'This App Cannot Be Found'",
             [('When publishing to Teams you may see:', 0, False, 20),
              ('"This app cannot be found."', 0, True, 20),
              ('', 0, False, 10),
              ('→  Click Close', 0, True, 20),
              ('→  Wait 2–3 minutes (Teams propagation delay)', 0, True, 20),
              ('→  Return to Copilot Studio and publish again', 0, True, 20),
              ('', 0, False, 10),
              ('Trial environment: Publish requires the Copilot Studio Authors role.', 0, False, 17),
              ('If Publish is greyed out, ask your facilitator.', 0, False, 17)])

dual(prs, "Lesson 11: Step by Step",
     [('1. Publish the agent', 0, True, 20),
      ('Overview page → Publish button → Confirm', 1, False, 17),
      ('', 0, False, 8),
      ('2. Deploy to Microsoft Teams', 0, True, 20),
      ('Overview → +8 → Channels', 1, False, 17),
      ('→ Microsoft Teams → Add to Teams', 1, False, 17),
      ('', 0, False, 8),
      ('3. Deploy to M365 Copilot', 0, True, 20),
      ('Channels → M365 and Teams → publish', 1, False, 17)],
     [('4. Open Teams web app', 0, True, 20),
      ('Find your agent → test it live', 1, False, 17),
      ('', 0, False, 8),
      ('Admin approval:', 0, True, 18),
      ('In production, org admins approve agents', 1, False, 16),
      ('In your sandbox env, you have admin rights', 1, False, 16),
      ('', 0, False, 8),
      ('Free Play Challenge!', 0, True, 18),
      ('Once published: adapt your agent for', 1, False, 16),
      ('a real scenario from your organisation.', 1, False, 16),
      ('', 0, False, 8),
      ('🕐  ~30 minutes', 0, True, 17)])

lets_go(prs, '11',
        "Mission 11: Publish Your Agent",
        "OPERATION PUBLISH PUBLISH PUBLISH",
        "~30 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  Microsoft 365  •  Teams",
        "Publishing  •  Channels  •  Deployment",
        "microsoft.github.io/agent-academy/recruit/mission-11")

debrief(prs, 4,
        ['Q1: Event triggers vs. waiting for user input — when do you use each?',
         'Q2: What are the two main publishing channels?',
         'Q3: What is the "trick" to finding the Channels tab in the new UI?'],
        right_text=[('Who deployed to Teams?', 0, True, 22),
                    ('', 0, False, 10),
                    ('Show us your live agent', 0, False, 19),
                    ('in the Teams web app.', 0, False, 19),
                    ('', 0, False, 10),
                    ('Free Play results — share your twist!', 0, True, 18)])

# ══════════════════════════════════════════════════════════════════════════════
# MISSION COMPLETE
# ══════════════════════════════════════════════════════════════════════════════
section_break(prs, "Mission Complete\nWhat's Next")

dual(prs, "Lesson 12: Understanding Licensing",
     [('Copilot Credits  (June 2026)', 0, True, 22),
      ('Replaced "messages" in September 2025', 0, False, 17),
      ('', 0, False, 8),
      ('Pay-as-you-go:', 0, True, 18),
      ('$0.01 per credit', 1, False, 17),
      ('', 0, False, 6),
      ('Capacity pack:', 0, True, 18),
      ('$200/month for 25,000 credits', 1, False, 17),
      ('', 0, False, 6),
      ('M365 Copilot licensed users:', 0, True, 18),
      ('No credits consumed on internal channels (fair use)', 1, False, 16)],
     [('AI Models (June 2026):', 0, True, 22),
      ('Default: GPT-4.1', 0, False, 17),
      ('(GPT-4o retired Oct 2025)', 1, False, 15),
      ('New options: GPT-5, Claude Sonnet 4.5/4.6, Mistral 3.5', 0, False, 16),
      ('Premium AI tools = higher credit rate', 1, False, 15),
      ('', 0, False, 8),
      ('Trial (30 days, extendable):', 0, True, 18),
      ('Full capabilities except publishing', 1, False, 16),
      ('Publishing needs Copilot Studio Authors role', 1, False, 16),
      ('', 0, False, 8),
      ('June 2026: Teams classic chatbot app retired.', 0, True, 16),
      ('Create and manage agents via Copilot Studio web.', 1, False, 15)])

lets_go(prs, '12',
        "Mission 12: Understanding Licensing",
        "OPERATION KNOW WHAT YOU OWE",
        "~15 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio  •  Microsoft 365",
        "Licensing  •  Copilot Credits",
        "microsoft.github.io/agent-academy/recruit/mission-12")

title_visual(prs, "Claim Your Recruit Badge!",
             [('You made it through all missions!', 0, True, 22),
              ('', 0, False, 10),
              ('Scan the QR code or visit:', 0, False, 20),
              ('aka.ms/agentacademy-live/graduate', 0, True, 20),
              ('', 0, False, 10),
              ('What\'s next?', 0, True, 20),
              ('Operative: deeper patterns and advanced scenarios', 1, False, 17),
              ('Commander: enterprise-scale architecture (coming soon)', 1, False, 17),
              ('Special Ops: YAML, MCP, CLI, and beyond', 1, False, 17)],
             os.path.join(IMG_DIR, 'image102.png'),  # Badge QR from Color Cloud
             size=18)

lets_go(prs, '13',
        "Mission 13: Secure Your Recruit Badge",
        "OPERATION COURSE COMPLETION",
        "~5 min  •  Difficulty: ★☆☆",
        "Microsoft Copilot Studio",
        "Course Completion  •  Badge",
        "aka.ms/agentacademy-live/graduate")

content(prs, "Plan Your First Real Agent",
        [('5 minutes. Think about next week.', 0, True, 22),
         ('', 0, False, 10),
         ('What will you build first when you\'re back at your desk?', 0, False, 20),
         ('Who is it for?', 0, False, 20),
         ('Which pieces from today will you use?', 0, False, 20),
         ('', 0, False, 10),
         ('Write it down. Share with the room if you\'re brave.', 0, True, 20)])

dual(prs, "Keep Building",
     [('Agent Academy', 0, True, 20),
      ('microsoft.github.io/agent-academy', 1, False, 17),
      ('', 0, False, 8),
      ('Copilot Studio Docs', 0, True, 20),
      ('learn.microsoft.com/copilot-studio', 1, False, 17),
      ('', 0, False, 8),
      ('What\'s New', 0, True, 20),
      ('.../whats-new (check monthly!)', 1, False, 17),
      ('', 0, False, 8),
      ('Trial Signup', 0, True, 20),
      ('aka.ms/TryCopilotStudio', 1, False, 17)],
     [('Usage Estimator', 0, True, 20),
      ('aka.ms/copilotstudioestimator', 1, False, 17),
      ('', 0, False, 8),
      ('M365 Developer Tenant (free)', 0, True, 20),
      ('developer.microsoft.com/microsoft-365', 1, False, 17),
      ('', 0, False, 8),
      ('BOOST Podcast', 0, True, 20),
      ('Weekly Power Platform community insights', 1, False, 17),
      ('with Nick and Ulrikke', 1, False, 17),
      ('', 0, False, 8),
      ('Power Platform Community', 0, True, 20),
      ('community.powerplatform.com', 1, False, 17)])

section_break(prs,
              "Don't be an expert.\n\nPlay, experiment, explore.\n\n"
              "— Nick & Ulrikke, Power Platform BOOST Podcast",
              size=24)

dual(prs, "What's Next in Agent Academy?",
     [('Recruit  ✅  You are here', 0, True, 20),
      ('13 lessons, zero to deployed agent', 1, False, 17),
      ('', 0, False, 8),
      ('Operative  →  Next level', 0, True, 20),
      ('Deeper agent patterns', 1, False, 17),
      ('Advanced knowledge & multi-agent', 1, False, 17),
      ('microsoft.github.io/agent-academy/operative', 1, False, 15),
      ('', 0, False, 8),
      ('Commander  (coming soon)', 0, True, 20),
      ('Enterprise architecture, governance, ALM', 1, False, 17)],
     [('Special Ops  —  Bonus missions', 0, True, 20),
      ('YAML Specialist', 1, False, 17),
      ('Microsoft Learn MCP Server', 1, False, 17),
      ('Copilot Studio + MCP', 1, False, 17),
      ('Power Platform CLI MCP Server', 1, False, 17),
      ('', 0, False, 8),
      ('Agent Academy on YouTube', 0, True, 20),
      ('Copilot Studio Agent Academy playlist', 1, False, 17),
      ('youtube.com/@mspowerplatform', 1, False, 15),
      ('', 0, False, 8),
      ('BOOST Podcast', 0, True, 20),
      ('Travelling Circus — wherever we go, we build!', 1, False, 16)])

content(prs, "Q&A",
        [('Questions?', 0, True, 28),
         ('', 0, False, 10),
         ('Nick Doelman', 0, False, 20),
         ('nick@readyxrm.com  •  @readyxrm', 1, False, 18),
         ('', 0, False, 8),
         ('Ulrikke Akerbæk', 0, False, 20),
         ('me@ulrikke.rocks  •  @ulrikkeakerbk', 1, False, 18),
         ('', 0, False, 10),
         ('#EPPC26  •  #AgentAcademy  •  #PowerPlatform', 0, True, 18)])

content(prs, "Thank You!",
        [('Thank you for building with us today.', 0, True, 26),
         ('', 0, False, 10),
         ('Please rate this session in the EPPC app.', 0, False, 22),
         ('Your feedback makes the next workshop better.', 0, False, 22),
         ('', 0, False, 10),
         ('#EPPC26  •  #AgentAcademy  •  #PowerPlatform', 0, True, 20)])

# ──────────────────────────────────────────────────────────────────────────────
# LAST SLIDE — End / Rate This Session
# ──────────────────────────────────────────────────────────────────────────────
add_slide(prs, L_END)

# ══════════════════════════════════════════════════════════════════════════════
# SAVE (with zip deduplication to remove orphaned template slides)
# ══════════════════════════════════════════════════════════════════════════════
buf = io.BytesIO()
prs.save(buf)
buf.seek(0)

data, order = {}, []
with _zip.ZipFile(buf, 'r') as zin:
    for info in zin.infolist():
        name = info.filename
        raw = zin.read(name)
        if name not in data:
            order.append(name)
        data[name] = raw  # last write wins (new slides beat template orphans)

import os as _os, shutil as _shutil
with _zip.ZipFile(OUTPUT_TMP, 'w', _zip.ZIP_DEFLATED) as zout:
    for name in order:
        zinfo = _zip.ZipInfo(name)
        zinfo.compress_type = _zip.ZIP_DEFLATED
        zout.writestr(zinfo, data[name])

# Atomically replace output file
if _os.path.exists(OUTPUT):
    _os.remove(OUTPUT)
_shutil.move(OUTPUT_TMP, OUTPUT)

print(f"Saved: {OUTPUT}")
print(f"Slides: {len(prs.slides)}")

# Layout usage breakdown
from collections import Counter
usage = Counter(s.slide_layout.name for s in prs.slides)
print("\nLayout usage:")
for name, count in usage.most_common():
    print(f"  {count:3d}x  {name}")
