---
title: "How to Track Crazy Egg Organic Pipeline in GA4"
description: "A RevOps guide to integrating Crazy Egg with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Crazy Egg

**Bottom Line Up Front:** Connecting Crazy Egg to GA4 helps CRO teams visualize exactly how organic search visitors interact with high-value pages.

If your growth engine relies on Crazy Egg as your primary Analytics & Heatmaps, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Crazy Egg conversion event in GA4.

## The Crazy Egg Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Analytics & Heatmaps |
| **Integration Difficulty** | Low |
| **GA4 Custom Dimension** | `crazyegg_scroll_depth` |
| **UTM Handling** | Ensure both scripts run simultaneously; use GA4 data to segment Crazy Egg heatmaps by organic traffic. |

## Step-by-Step Data Flow for Crazy Egg

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Crazy Egg capture points.
2. **Configure UTM Preservation:** Ensure both scripts run simultaneously; use GA4 data to segment Crazy Egg heatmaps by organic traffic.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `crazyegg_scroll_depth` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Analytics & Heatmaps tools like Crazy Egg. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Crazy Egg to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
