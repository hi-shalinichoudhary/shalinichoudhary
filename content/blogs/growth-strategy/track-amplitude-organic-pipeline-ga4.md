---
title: "How to Track Amplitude Organic Pipeline in GA4"
description: "A RevOps guide to integrating Amplitude with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Amplitude

**Bottom Line Up Front:** Tracking Amplitude alongside GA4 provides enterprise teams with the ultimate view of how organic search drives long-term retention.

If your growth engine relies on Amplitude as your primary Analytics & Heatmaps, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Amplitude conversion event in GA4.

## The Amplitude Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Analytics & Heatmaps |
| **Integration Difficulty** | High |
| **GA4 Custom Dimension** | `amplitude_retention_cohort` |
| **UTM Handling** | Use a CDP like Segment to unify the GA4 acquisition source with Amplitude product events. |

## Step-by-Step Data Flow for Amplitude

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Amplitude capture points.
2. **Configure UTM Preservation:** Use a CDP like Segment to unify the GA4 acquisition source with Amplitude product events.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `amplitude_retention_cohort` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Analytics & Heatmaps tools like Amplitude. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Amplitude to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
