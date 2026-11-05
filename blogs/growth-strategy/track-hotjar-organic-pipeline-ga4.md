---
title: "How to Track Hotjar Organic Pipeline in GA4"
description: "A RevOps guide to integrating Hotjar with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Hotjar

**Bottom Line Up Front:** Mapping Hotjar recordings in GA4 provides qualitative insights into why organic search visitors convert or bounce.

If your growth engine relies on Hotjar as your primary Analytics & Heatmaps, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Hotjar conversion event in GA4.

## The Hotjar Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Analytics & Heatmaps |
| **Integration Difficulty** | Low |
| **GA4 Custom Dimension** | `hotjar_feedback_score` |
| **UTM Handling** | Use the Hotjar-GA integration to fire events in GA4 when a user completes a survey or feedback poll. |

## Step-by-Step Data Flow for Hotjar

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Hotjar capture points.
2. **Configure UTM Preservation:** Use the Hotjar-GA integration to fire events in GA4 when a user completes a survey or feedback poll.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `hotjar_feedback_score` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Analytics & Heatmaps tools like Hotjar. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Hotjar to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
