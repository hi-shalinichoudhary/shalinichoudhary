---
title: "How to Track mParticle Organic Pipeline in GA4"
description: "A RevOps guide to integrating mParticle with Google Analytics 4 for closed-loop B2B organic attribution."
pillar: "Growth & Revenue Operations"
robots: index, follow
---

# Closed-Loop Attribution for mParticle

**Bottom Line Up Front:** Tracking mParticle events in GA4 allows enterprise brands to unify mobile and web organic search attribution.

If your growth engine relies on mParticle as your primary CDP & Data, tracking top-of-funnel organic traffic is no longer enough. To prove SEO ROI to the C-suite and protect your marketing budget, you must map the organic session directly to the mParticle conversion event in GA4.

## The mParticle Integration Architecture

| Metric | Setup Requirement |
|---|---|
| **Category** | CDP & Data |
| **Integration Difficulty** | High |
| **GA4 Custom Dimension** | `mparticle_audience_cohort` |
| **UTM Handling** | Use the mParticle GA4 integration to map custom organic events and user identities. |

## Step-by-Step Data Flow for mParticle

To bridge the gap between your website's organic traffic and your downstream revenue, follow this architecture:

1. **Capture the Client ID:** Ensure your Google tag is passing the GA4 Client ID into a hidden field within your mParticle capture points.
2. **Configure UTM Preservation:** Use the mParticle GA4 integration to map custom organic events and user identities.
3. **Set the Custom Dimension:** Inside your GA4 admin panel, map the incoming data to `mparticle_audience_cohort` so you can filter your pipeline and revenue reports strictly by organic acquisition.

> **RevOps Insight:** Never rely solely on GA4's default channel grouping when integrating CDP & Data tools like mParticle. Always pass the raw referring URL and timestamp into your database to protect against attribution data loss caused by cookie blockers and intelligent tracking prevention (ITP).

## Why This Matters for B2B Growth
Without this integration, organic search looks like a vanity metric. By connecting mParticle to GA4, you transition from reporting on "organic traffic" to reporting on "organic pipeline generated."
