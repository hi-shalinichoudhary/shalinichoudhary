---
title: "How to Track Tidio Organic Pipeline in GA4"
description: "A RevOps guide to integrating Tidio with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Tidio

**Bottom Line Up Front:** Tracking Tidio in GA4 helps small to mid-market B2B brands attribute lead generation from chatbots to organic search.

If your growth engine relies on Tidio as your primary Live Chat & Support, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Tidio conversion event in GA4.

## The Tidio Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Live Chat & Support |
| **Integration Difficulty** | Low |
| **GA4 Custom Dimension** | `tidio_lead_captured` |
| **UTM Handling** | Use Tidio's native GA4 event pushing for new lead capture. |

## Step-by-Step Data Flow for Tidio

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Tidio capture points.
2. **Configure UTM Preservation:** Use Tidio's native GA4 event pushing for new lead capture.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `tidio_lead_captured` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Live Chat & Support tools like Tidio. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Tidio to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
