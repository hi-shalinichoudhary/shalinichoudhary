---
title: "How to Track Brevo Organic Pipeline in GA4"
description: "A RevOps guide to integrating Brevo with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Brevo

**Bottom Line Up Front:** Mapping Brevo data in GA4 allows growth teams to see how organic traffic converts into active subscribers.

If your growth engine relies on Brevo as your primary Marketing Automation, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Brevo conversion event in GA4.

## The Brevo Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | Marketing Automation |
| **Integration Difficulty** | Low |
| **GA4 Custom Dimension** | `brevo_engagement` |
| **UTM Handling** | Use hidden fields in Brevo subscription forms to capture acquisition source. |

## Step-by-Step Data Flow for Brevo

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Brevo capture points.
2. **Configure UTM Preservation:** Use hidden fields in Brevo subscription forms to capture acquisition source.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `brevo_engagement` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating Marketing Automation tools like Brevo. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Brevo to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
