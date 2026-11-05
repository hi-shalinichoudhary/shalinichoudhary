---
title: "How to Track Pardot Organic Pipeline in GA4"
description: "A RevOps guide to integrating Pardot with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Pardot

**Bottom Line Up Front:** Connecting Pardot with GA4 allows B2B marketers to align organic search traffic with Salesforce-driven lead scoring.

If your growth engine relies on Pardot as your primary Marketing Automation, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Pardot conversion event in GA4.

## The Pardot Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Marketing Automation |
| **Integration Difficulty** | High |
| **GA4 Custom Dimension** | `pardot_score` |
| **UTM Handling** | Use Pardot form handlers to capture UTM data from the referring URL. |

## Step-by-Step Data Flow for Pardot

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Pardot capture points.
2. **Configure UTM Preservation:** Use Pardot form handlers to capture UTM data from the referring URL.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `pardot_score` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Marketing Automation tools like Pardot. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Pardot to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
