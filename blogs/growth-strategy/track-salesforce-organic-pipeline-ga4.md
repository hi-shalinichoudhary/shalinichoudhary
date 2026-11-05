---
title: "How to Track Salesforce Organic Pipeline in GA4"
description: "A RevOps guide to integrating Salesforce with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for Salesforce

**Bottom Line Up Front:** Tracking Salesforce pipeline in GA4 ensures you can attribute closed-won enterprise revenue directly to organic search campaigns.

If your growth engine relies on Salesforce as your primary CRM, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the Salesforce conversion event in GA4.

## The Salesforce Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | CRM |
| **Integration Difficulty** | High |
| **GA4 Custom Dimension** | `sfdc_lead_status` |
| **UTM Handling** | Requires capturing GA client ID and passing UTMs via hidden web-to-lead form fields. |

## Step-by-Step Data Flow for Salesforce

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your Salesforce capture points.
2. **Configure UTM Preservation:** Requires capturing GA client ID and passing UTMs via hidden web-to-lead form fields.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `sfdc_lead_status` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating CRM tools like Salesforce. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting Salesforce to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
