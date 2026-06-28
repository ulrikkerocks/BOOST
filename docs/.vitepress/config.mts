import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

// BOOST — Agent Academy Recruit Course
// Rebuilt with VitePress to mirror the original Microsoft Agent Academy site.
export default withMermaid(defineConfig({
  title: 'Agent Academy Recruit',
  description:
    'Build production-ready AI agents with Microsoft Copilot Studio — updated for the 2026 UI.',
  base: '/BOOST/',
  cleanUrls: true,
  lastUpdated: true,
  // TODO: tighten to link-checking once internal links are audited post-migration
  ignoreDeadLinks: true,

  // Internal worklists — keep the files, exclude from the built site
  srcExclude: ['**/screenshot-*.md'],

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/BOOST/favicon.svg' }],
    // Unlisted preview phase — keep the site out of search results.
    // Remove this line to "go public" (make it indexable).
    ['meta', { name: 'robots', content: 'noindex, nofollow' }],
  ],

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Modules', link: '/modules/' },
      { text: 'Facilitator Guide', link: '/facilitator-guide' },
      {
        text: 'Original Course',
        link: 'https://microsoft.github.io/agent-academy/recruit/',
      },
    ],

    sidebar: [
      {
        text: 'Recruit Course',
        collapsed: false,
        items: [
          { text: 'Overview', link: '/modules/' },
          { text: '00 · Course Setup', link: '/modules/00-course-setup/' },
          { text: '01 · Introduction to Agents', link: '/modules/01-introduction-to-agents/' },
          { text: '02 · Copilot Studio Fundamentals', link: '/modules/02-copilot-studio-fundamentals/' },
          { text: '03 · Declarative Agent for M365 Copilot', link: '/modules/03-declarative-agent-m365/' },
          { text: '04 · Creating a Solution', link: '/modules/04-creating-a-solution/' },
          { text: '05 · Using Pre-Built Agents', link: '/modules/05-prebuilt-agents/' },
          { text: '06 · Build a Custom Agent', link: '/modules/06-build-custom-agent/' },
          { text: '07 · Add a Topic with Triggers', link: '/modules/07-add-topic-with-triggers/' },
          { text: '08 · Enhance with Adaptive Cards', link: '/modules/08-enhance-with-adaptive-cards/' },
          { text: '09 · Automate with Agent Flows', link: '/modules/09-automate-with-agent-flows/' },
          { text: '10 · Add Event Triggers', link: '/modules/10-add-event-triggers/' },
          { text: '11 · Publish Your Agent', link: '/modules/11-publish-your-agent/' },
          { text: '12 · Understanding Licensing', link: '/modules/12-understanding-licensing/' },
          { text: '13 · Securing Your Recruit Badge', link: '/modules/13-securing-recruit-badge/' },
        ],
      },
      {
        text: 'For Facilitators',
        collapsed: false,
        items: [
          { text: 'Facilitator Guide', link: '/facilitator-guide' },
          { text: 'Participant Reference Card', link: '/participant-reference-card' },
        ],
      },
    ],

    search: { provider: 'local' },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/ulrikkerocks/BOOST' },
    ],

    editLink: {
      pattern: 'https://github.com/ulrikkerocks/BOOST/edit/wip/rig/vitepress-rebuild/docs/:path',
      text: 'Edit this page on GitHub',
    },

    footer: {
      message:
        'Adapted from the <a href="https://microsoft.github.io/agent-academy/recruit/">Microsoft Agent Academy</a> (MIT).',
      copyright: 'Copyright © 2026 Ulrikke Rocks',
    },
  },
}))
