---
title: "How to Track Insightly Organic Pipeline in GA4"
description: "A RevOps guide to integrating Insightly with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Insightly

**Bottom Line Up Front:** Integrating Insightly with GA4 allows B2B teams to track the organic journey from initial session to project delivery.

If your growth engine relies on Insightly as your primary CRM, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Insightly conversion event in GA4.

## The Insightly Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | CRM |
| **Integration Difficulty** | Medium |
| **GA4 Custom Dimension** | `insightly_lead_grade` |
| **UTM Handling** | Use hidden fields in Insightly web-to-lead forms to capture organic UTMs. |

## Step-by-Step Data Flow for Insightly

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Insightly capture points.
2. **Configure UTM Preservation:** Use hidden fields in Insightly web-to-lead forms to capture organic UTMs.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `insightly_lead_grade` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating CRM tools like Insightly. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Insightly to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
