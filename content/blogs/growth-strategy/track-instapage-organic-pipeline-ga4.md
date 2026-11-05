---
title: "How to Track Instapage Organic Pipeline in GA4"
description: "A RevOps guide to integrating Instapage with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Instapage

**Bottom Line Up Front:** Tracking Instapage in GA4 allows enterprise marketers to optimize landing page experiences for organic traffic.

If your growth engine relies on Instapage as your primary Landing Pages, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Instapage conversion event in GA4.

## The Instapage Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Landing Pages |
| **Integration Difficulty** | Low |
| **GA4 Custom Dimension** | `instapage_conversion_type` |
| **UTM Handling** | Enable the native GA4 integration and ensure UTMs are passed to downstream CRMs. |

## Step-by-Step Data Flow for Instapage

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Instapage capture points.
2. **Configure UTM Preservation:** Enable the native GA4 integration and ensure UTMs are passed to downstream CRMs.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `instapage_conversion_type` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Landing Pages tools like Instapage. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Instapage to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
