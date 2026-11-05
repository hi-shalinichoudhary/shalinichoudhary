---
title: "How to Track Freshsales Organic Pipeline in GA4"
description: "A RevOps guide to integrating Freshsales with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Freshsales

**Bottom Line Up Front:** Attributing Freshsales data in GA4 bridges the gap between organic traffic and actual sales qualified leads (SQLs).

If your growth engine relies on Freshsales as your primary CRM, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Freshsales conversion event in GA4.

## The Freshsales Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | CRM |
| **Integration Difficulty** | Medium |
| **GA4 Custom Dimension** | `freshsales_sql_status` |
| **UTM Handling** | Pass referring URLs and UTMs into Freshsales custom fields upon form submission. |

## Step-by-Step Data Flow for Freshsales

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Freshsales capture points.
2. **Configure UTM Preservation:** Pass referring URLs and UTMs into Freshsales custom fields upon form submission.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `freshsales_sql_status` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating CRM tools like Freshsales. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Freshsales to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
