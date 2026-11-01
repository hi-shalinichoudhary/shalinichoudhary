# Repo Audit: shalinichoudhary.in

_Audit date: 2026-11-01. Read-only inspection. Supersedes the 2026-10-30 version (which pre-dated the homepage enhancements commit and had several count errors, corrected below)._

---

## 1. Hosting and deployment

| Item | Detail |
|---|---|
| Platform | GitHub Pages, static, no server-side processing |
| Deployment | `.github/workflows/static.yml`: push to `main` runs `actions/deploy-pages@v4`; the entire repo root is uploaded, so scratch files, Python scripts and `data/` are all publicly reachable |
| Domain | `shalinichoudhary.in` (from canonicals and sitemap) |
| `.htaccess` | Inert on GitHub Pages. The `index.html` de-duplication is an inline `history.replaceState` script in the homepage `<head>` |
| Build tooling | None. No `package.json`, bundler, Sass or PostCSS. Do not add any |

---

## 2. File structure

```
/
+-- index.html, about.html, work.html, contact.html, blogs.html
+-- seo-strategy-consultant.html, growth-marketing-strategy.html,
|   marketing-analytics-ga4-consultant.html, conversion-optimisation-strategy.html
+-- preview-components.html          Scratch (disallowed in robots.txt, no canonical)
+-- generated_cards.html, temp_cards.html   Scratch (disallowed, no canonical)
+-- blogs/
|   +-- 9 category hubs: ai-search.html, analytics-measurement.html,
|   |   conversion-performance.html, google-analytics.html, growth-strategy.html,
|   |   seo-industry.html, seo-strategy.html, seo-tips.html, strategy.html
|   +-- 9 category folders holding 50 posts:
|       ai-search 8, analytics-measurement 4, conversion-performance 2,
|       google-analytics 3, growth-strategy 10, seo-industry 4,
|       seo-strategy 6, seo-tips 5, strategy 8
+-- css/   bundle.min.css, style.css, style-v2.css, footer.css,
|          sc-components.css, home-enhancements.css
+-- js/    script.js, antigravity.js, scroll-reveal.js, prototype.js,
|          backToTop.js, gsap.min.js, home-enhancements.js, js.svg
+-- images/  103 entries (102 files + blog-images/ subfolder)
+-- data/    linkedin-posts.json, proof-points.md, repo-audit.md
+-- robots.txt, sitemap.xml, llms.txt, README.md, .htaccess
+-- unused_assets/   14 legacy JS libraries (jQuery, Bootstrap, Owl etc.)
+-- Python helpers (not site code): generate_blog2.py, generate_blog3.py,
    generate_cards.py, generate_sitemap.py, inject_cards.py, fix_links.py,
    debug_regex.py, replace_featured.py, resize_images.py, update_blogs.py,
    update_nav.py
```

Total HTML: 12 root-level files, 59 under `blogs/` (9 hubs + 50 posts).

---

## 3. CSS organisation

| File | Role | Linked by pages? |
|---|---|---|
| `css/bundle.min.css` | The production stylesheet. Hand-assembled, not minified in practice (it starts with a readable "Prototype CSS (v2)" comment and `:root` tokens) | Every real page, with relative paths: `css/`, `../css/` (hubs), `../../css/` (posts) |
| `css/style.css`, `css/style-v2.css`, `css/footer.css` | Source files that were manually merged into the bundle | No |
| `css/sc-components.css` | Reusable component CSS from an earlier step | Only `preview-components.html` |
| `css/home-enhancements.css` | Homepage hero, ticker and stat bar enhancements (added in the last commit) | Only `index.html` |

Existing tokens (in the bundle): `--text #0b1220`, `--muted-text #475569`, `--border #e5e7eb`, `--card #f8fafc`, `--radius 18px`, `--font-heading` and `--font-body` both Poppins. Brand green `#57c021` is hard-coded in many places rather than tokenised. **This palette is the opposite of the target identity** (ivory, charcoal, stone, terracotta), so the bundle's tokens and many hard-coded colours will need replacing.

Page-level CSS lives in inline `<style>` blocks (homepage stat bar, impact cards, skills cards, mobile footer overrides; the results section on `work.html`) and in many inline `style=""` attributes (the homepage skills cards are almost entirely inline).

---

## 4. JavaScript organisation

| File | Purpose |
|---|---|
| `script.js` | Hamburger nav, `.stat-number` counters, portfolio lightbox and filter, testimonial slider, dark mode, back-to-top |
| `antigravity.js` | Canvas particle swarm on `.hero` |
| `scroll-reveal.js` | IntersectionObserver adding `.is-visible` to `.reveal` |
| `prototype.js` | Smooth anchor scroll, secondary reveal pass, accordion |
| `backToTop.js` | Possible overlap with `script.js` |
| `gsap.min.js` | Vendored, no HTML page references it (dead weight) |
| `home-enhancements.js` | Count-up for `.stat-figure` (homepage only) |

Homepage load order (end of body, no defer): `script.js`, `prototype.js`, `antigravity.js`, `scroll-reveal.js`, `home-enhancements.js`. Plain vanilla JS, no modules. Swiper (jsDelivr CDN CSS) is referenced on one page.

---

## 5. Images and fonts

**Fonts.** Poppins from Google Fonts CDN on every page, with three different weight sets: `400;700;900` (30 pages), `400;600;700;800;900` (7), `400;500;600;700;800;900` (2). No self-hosted fonts, no `/fonts` folder. `preconnect` is missing on `about.html`, `contact.html`, the scratch pages and many posts. Font Awesome comes from cdnjs, version 6.0.0 on 44 references and 6.4.0 on 7. The homepage and `work.html` lazy-load it (`media="print" onload`), other pages load it synchronously.

**Images.** `/images/` holds webp alongside jpg/png originals, plus `blog-images/`. Homepage hero portrait is `images/test_shalini.jpg` (preloaded as the LCP image). Logo is `images/logo-image.webp`; favicon is `images/android-icon-36x36.png`. Logo strip uses `logo1.webp` and `test_logo2/5/6.png`. Below-fold images use `loading="lazy"`. `images/shalini team meet.mp4` (2.4 MB) exists. **CV: `images/Shalinicv.pdf`** (blocked for crawlers by `robots.txt`; the homepage "Download CV" link points here and must keep that path).

---

## 6. JSON-LD

| Page | Blocks | Types |
|---|---|---|
| `index.html` | 2 | ProfilePage > Person (`@id #person`, `worksFor` GUS Global, `alumniOf`, `knowsAbout`, `review` x2), WebSite |
| `about.html` | 2 | ProfilePage > Person, FAQPage (Question/Answer), Organization, Review |
| `blogs.html` | 1 | ProfilePage > Person |
| Four service pages | 1 each | BreadcrumbList only |
| `work.html`, `contact.html` | 0 | none |
| Blog posts | 28 of 50 | BlogPosting, WebPage, SpeakableSpecification, Person, Organization, ImageObject, BreadcrumbList |
| Other 22 posts | 0 | none (also have no nav or footer, see section 9) |

---

## 7. robots.txt

```
User-Agent: *
Allow: /
Disallow: /*.pdf$
Disallow: /temp_cards.html
Disallow: /generated_cards.html
Disallow: /preview-components.html

Sitemap: https://shalinichoudhary.in/sitemap.xml
```

---

## 8. sitemap.xml

**41 URLs** (the earlier audit said 49, which was wrong): 9 top-level pages plus 32 blog URLs. It is generated by `generate_sitemap.py` (comment in the file says "dynamically generated"). lastmod values are all between 2026-07-28 and 2026-07-29, so they pre-date recent edits.

Top-level: `/`, `/about.html`, `/blogs.html`, `/contact.html`, `/work.html`, and the four service pages.

**Not in the sitemap but live on disk (27 files):** 4 category hubs (`blogs/google-analytics.html`, `blogs/seo-industry.html`, `blogs/seo-tips.html`, `blogs/strategy.html`) and 23 posts, concentrated in `google-analytics/`, `seo-industry/`, `seo-tips/` and `strategy/`. Several are among the 22 posts with no nav or footer. These URLs must be preserved as they are; this is flagged only. Nothing in the sitemap points to a missing file.

Canonicals: every real page has a self-referencing `https://shalinichoudhary.in/...` canonical. Only the three scratch pages lack one.

---

## 9. Nav and footer markup

**Nav.** One identical block (`<header class="site-header">` > `.site-header-inner` > logo, `.menu-toggle`, `<nav class="site-nav" id="main-navigation">` with Work, SEO Strategy, Growth Strategy, About, Blog, and a "Get in touch" `.cta-button.small-btn`). Verified byte-identical across all 9 top-level pages. Inconsistency: `blogs.html` and `contact.html` links have no leading slash, the rest do. 28 blog posts share a second variant. **22 blog posts have no `site-nav` and no `tj-footer-area` at all.**

**Footer.** `<footer class="tj-footer-area">` with `.footer-grid` (brand/kicker/h2/CTA, one or two `.footer-links` columns, `.footer-contact` with LinkedIn, Twitter and email) and `.footer-meta` copyright. The kicker and headline copy varies by page. Hand-duplicated everywhere; `update_nav.py` is the existing pattern for bulk edits.

---

## 10. llms.txt

Present at `/llms.txt`, not blocked. It contains the identity summary and absolute URLs. It repeats "8+" and MSc wording that the proof-points file corrects.

---

## 11. Copy that conflicts with `proof-points.md` (found, not yet changed)

| Issue | Where |
|---|---|
| "Senior SEO Manager · GUS" (present tense) | `index.html` line 486, the portrait chip **I added in the previous step. This was my error and needs fixing** |
| "8+" years | `index.html` title/meta/JSON-LD/stat bar, `blogs.html`, `llms.txt`, and "8+ years" in 28 blog posts |
| "eight years" | `index.html`, `about.html`, 2 blog posts (one is the post URL `what-eight-years-in-marketing-actually-taught-me-about-strategy.html`, so its slug must be kept) |
| Present-tense job claims | `worksFor: GUS Global` in JSON-LD on `index`, `about`, `blogs`; "Senior SEO Manager" as `jobTitle`, title tag and H1-adjacent copy (employment ended Sep 2025) |
| Em dashes in copy | `index`, `about`, `work`, `blogs`, `seo-strategy-consultant`, `growth-marketing-strategy`, `llms.txt`, and 11 blog posts |
| MSc status wording | `about.html`, `blogs.html`, `llms.txt` mention the MSc; each needs a read to confirm it is not framed as in progress |
| Hero line | Currently "Fluent in search &amp; growth. Native to revenue." Matches the required line |
| Homepage stat figures | 65% and 50-60K match the file; "8+" does not |

---

## 12. Observations and risks for the revamp

1. **No build step.** All changes are hand-edited HTML/CSS/JS, deployed as-is. Nav and footer edits need a scripted bulk replace across 59+12 files.
2. **Palette change is large.** Green `#57c021` and navy `#0b1220` are hard-coded widely; moving to ivory, charcoal and terracotta means a token layer plus sweeping the bundle and inline styles.
3. **Contrast.** Terracotta `#A65F43` on ivory is about 4.3:1, so small text must use `#8F4F36`, per the file.
4. **Sitemap gap.** About 27 live files are absent from the sitemap, and lastmod dates are stale. Adding entries changes the sitemap, so only do it if you approve.
5. **22 posts without nav, footer or JSON-LD** are likely older or orphaned pages; a standardising pass would need your sign-off.
6. **Dead code:** `gsap.min.js`, `unused_assets/`, scratch HTML files and Python helpers are all publicly deployed.
7. **Relative asset paths** differ by depth (`css/`, `../css/`, `../../css/`); any new shared asset must be linked with the right prefix per level.
8. **`worksFor` and `jobTitle` JSON-LD** are out of date relative to the Sep 2025 end date.
9. The scroll `.reveal` animation depends on JS; content is hidden if `scroll-reveal.js` fails (it has a 500 ms fallback).
