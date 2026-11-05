---
title: "How to Track YouCanBookMe Organic Pipeline in GA4"
description: "A RevOps guide to integrating YouCanBookMe with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for YouCanBookMe

**Bottom Line Up Front:** Mapping YouCanBookMe in GA4 provides visibility into how organic content drives direct consultations.

If your growth engine relies on YouCanBookMe as your primary Scheduling, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the YouCanBookMe conversion event in GA4.

## The YouCanBookMe Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Scheduling |
| **Integration Difficulty** | Low |
| **GA4 Custom Dimension** | `ycbm_booking_value` |
| **UTM Handling** | Enable GA4 tracking in the YouCanBookMe integrations settings. |

## Step-by-Step Data Flow for YouCanBookMe

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your YouCanBookMe capture points.
2. **Configure UTM Preservation:** Enable GA4 tracking in the YouCanBookMe integrations settings.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `ycbm_booking_value` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Scheduling tools like YouCanBookMe. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting YouCanBookMe to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
