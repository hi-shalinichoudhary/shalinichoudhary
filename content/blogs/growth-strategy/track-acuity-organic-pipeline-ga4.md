---
title: "How to Track Acuity Organic Pipeline in GA4"
description: "A RevOps guide to integrating Acuity with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Acuity

**Bottom Line Up Front:** Connecting Acuity Scheduling to GA4 helps service-based businesses track organic search ROI through booked appointments.

If your growth engine relies on Acuity as your primary Scheduling, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Acuity conversion event in GA4.

## The Acuity Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Scheduling |
| **Integration Difficulty** | Low |
| **GA4 Custom Dimension** | `acuity_appointment_tier` |
| **UTM Handling** | Embed Acuity with GA tracking enabled or use a custom redirect after booking. |

## Step-by-Step Data Flow for Acuity

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Acuity capture points.
2. **Configure UTM Preservation:** Embed Acuity with GA tracking enabled or use a custom redirect after booking.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `acuity_appointment_tier` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Scheduling tools like Acuity. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Acuity to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
