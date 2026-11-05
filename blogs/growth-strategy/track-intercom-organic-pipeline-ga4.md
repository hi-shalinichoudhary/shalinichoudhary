---
title: "How to Track Intercom Organic Pipeline in GA4"
description: "A RevOps guide to integrating Intercom with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Intercom

**Bottom Line Up Front:** Tracking Intercom chats in GA4 allows you to attribute conversational marketing leads directly to organic search performance.

If your growth engine relies on Intercom as your primary Live Chat & Support, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Intercom conversion event in GA4.

## The Intercom Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Live Chat & Support |
| **Integration Difficulty** | Medium |
| **GA4 Custom Dimension** | `intercom_chat_type` |
| **UTM Handling** | Use Intercom's Google Analytics app to fire custom events on chat initiation. |

## Step-by-Step Data Flow for Intercom

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Intercom capture points.
2. **Configure UTM Preservation:** Use Intercom's Google Analytics app to fire custom events on chat initiation.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `intercom_chat_type` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Live Chat & Support tools like Intercom. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Intercom to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
