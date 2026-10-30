# Repo Audit: shalinichoudhary.in

_Audit date: 2026-10-30. Read-only. No files were modified._

---

## 1. Hosting and deployment

| Item | Detail |
|---|---|
| Platform | GitHub Pages (static, no server-side processing) |
| Deployment | `.github/workflows/static.yml` pushes to `main` trigger `actions/deploy-pages@v4`; entire repo root is uploaded as the artifact |
| Custom domain | `shalinichoudhary.in` (inferred from canonicals and sitemap) |
| `.htaccess` | Present but inert: file contains a comment acknowledging GitHub Pages does not support `.htaccess`; the 301 de-duplicate logic for `index.html` is handled via inline `<script>` in `index.html` |

---

## 2. File structure

```
/
+-- index.html                          Homepage
+-- about.html                          About page
+-- blogs.html                          Blog hub (123 KB, card-heavy)
+-- work.html                           Capabilities / results page
+-- contact.html                        Contact page
+-- seo-strategy-consultant.html        Service page
+-- growth-marketing-strategy.html      Service page
+-- marketing-analytics-ga4-consultant.html  Service page
+-- conversion-optimisation-strategy.html    Service page
|
+-- blogs/
|   +-- ai-search/          (8 blog posts as .html files)
|   +-- analytics-measurement/  (3 blog posts)
|   +-- conversion-performance/ (1 blog post)
|   +-- growth-strategy/    (10 blog posts)
|   +-- seo-strategy/       (5 blog posts)
|   +-- [stub .html files at category level]
|
+-- css/
|   +-- bundle.min.css      Primary stylesheet loaded by every page (91 KB)
|   +-- style.css           Source stylesheet (57 KB, not loaded directly)
|   +-- style-v2.css        Secondary source stylesheet (25 KB, not loaded directly)
|   +-- footer.css          Footer styles (4.5 KB, bundled into bundle.min.css)
|
+-- js/
|   +-- script.js           Main JS: hamburger nav, counter, lightbox, testimonial slider, dark mode, back-to-top
|   +-- antigravity.js      Canvas particle swarm on hero section
|   +-- scroll-reveal.js    IntersectionObserver reveal for .reveal elements
|   +-- prototype.js        Smooth scroll for anchors; secondary reveal pass; accordion one-open logic
|   +-- backToTop.js        Back-to-top button (possible overlap with script.js)
|   +-- gsap.min.js         GSAP library (71 KB, vendored; usage unconfirmed)
|   +-- js.svg              SVG icon stored inside js/ directory
|
+-- images/                 102 files + 1 subdirectory (blog-images/)
+-- data/
|   +-- linkedin-posts.json  LinkedIn post data (used by blogs.html)
|
+-- robots.txt
+-- sitemap.xml
+-- llms.txt                LLM-readable site summary
|
+-- [Python helper scripts, not deployed]
|   generate_blog2.py, generate_blog3.py, generate_cards.py,
|   generate_sitemap.py, inject_cards.py, fix_links.py,
|   debug_regex.py, replace_featured.py, resize_images.py,
|   update_blogs.py, update_nav.py
|
+-- generated_cards.html    Scratch output (disallowed in robots.txt)
+-- temp_cards.html         Scratch output (disallowed in robots.txt)
+-- unused_assets/          Superseded assets
+-- README.md               One-line placeholder
```

---

## 3. CSS organisation

| File | Role | Loaded by pages? |
|---|---|---|
| `css/bundle.min.css` | Single production stylesheet. All pages load this via `<link rel="stylesheet" href="css/bundle.min.css">` | Yes, every page |
| `css/style.css` | Human-readable source (Poppins, high-contrast minimalist grid). `:root` tokens, base, nav, hero, sections, modals, dark mode, testimonials, contact, footer | Not directly (bundled) |
| `css/style-v2.css` | Secondary source stylesheet (v2 design-system tokens and utilities) | Not directly (bundled) |
| `css/footer.css` | Footer-specific styles (`tj-footer-area`, `footer-grid`, `footer-brand`, `footer-nav`) | Not directly (bundled) |

Inline `<style>` blocks are used on individual pages for page-specific overrides: stat bar, impact cards, positioning block, mobile footer fixes on `index.html`; the entire results section and reading-card hover styles on `work.html`. This is the current pattern for page-level CSS.

No CSS preprocessor or build tool is present. No Webpack, Vite, Sass, or PostCSS config. The bundle appears to have been assembled manually.

---

## 4. JavaScript organisation

| File | Purpose |
|---|---|
| `script.js` | Core: hamburger nav toggle, counter animation (`.stat-number`), portfolio lightbox, testimonial slider (`#testimonialsSlider`), dark-mode toggle, back-to-top, portfolio filter |
| `antigravity.js` | Canvas-based particle swarm that follows the cursor on `.hero` sections |
| `scroll-reveal.js` | IntersectionObserver: adds `.is-visible` to `.reveal` elements as they enter the viewport; 500 ms fallback |
| `prototype.js` | Smooth anchor scroll; secondary reveal pass for legacy card selectors; accordion one-open-at-a-time |
| `backToTop.js` | Standalone back-to-top handler (may overlap with `script.js`) |
| `gsap.min.js` | GSAP animation library, vendored locally; no confirmed usage in current HTML |

Load order on `index.html` (end of body, no defer/async): `script.js` then `prototype.js` then `antigravity.js` then `scroll-reveal.js`.

Load order on `work.html` (end of body): `scroll-reveal.js` then `script.js` then an inline filter script.

No module bundler. No `package.json`. Pure vanilla JS.

---

## 5. Images and fonts

### Fonts

- Poppins (Google Fonts CDN) is loaded on every page via `<link href="https://fonts.googleapis.com/css2?family=Poppins:...">`.
- `index.html` and `work.html` use `<link rel="preconnect">` to `fonts.googleapis.com` and `fonts.gstatic.com` before the font link. `about.html` omits the preconnect.
- Font Awesome 6.0.0 (cdnjs CDN) is used for icons. `index.html` and `work.html` use the print-media lazy-load pattern (`media="print" onload="this.media='all'"`) with a `<noscript>` fallback. `about.html` loads Font Awesome synchronously without the lazy-load pattern.

### Images

- Stored in `/images/` (102 files) and `/images/blog-images/`.
- Format strategy: `.webp` files exist alongside `.jpg` and `.png` originals. Pages reference `.webp` where available (logo strips, hero, portfolio cards).
- Hero image on homepage: `images/test_shalini.jpg` (LCP candidate) is preloaded via `<link rel="preload" as="image">` in `index.html`.
- Logo: `images/logo-image.webp` used in nav across all pages.
- Favicon: `images/android-icon-36x36.png` (apple-touch-icon and shortcut icon).
- Below-fold images use `loading="lazy"`.
- Testimonial author images: `images/Leighann.png`, `images/Krys.jpeg`, `images/Mayur.jpeg`, `images/Juhi.jpeg`.
- A video file (`images/shalini team meet.mp4`) is present and used on `about.html`.
- CV PDF: `images/Shalinicv.pdf` (disallowed in `robots.txt`).

---

## 6. JSON-LD structured data

### index.html

- **ProfilePage** wrapping a **Person** entity (`@id: https://shalinichoudhary.in/#person`) with `name`, `url`, `jobTitle`, `description`, `image`, `email`, `sameAs` (LinkedIn, Twitter, Medium, Crunchbase, Wikidata), `alumniOf` (Leeds, HJU), `worksFor` (GUS Global), `knowsAbout` (20 topics), and an inline `review` array (Leighann Follis, Krzysztof Saganski).
- **WebSite** entity with `name`, `url`, `description`, `author` referencing `#person`.

### about.html

- **ProfilePage** wrapping **Person** (same `@id`): same fields but a slightly different `description`; different `review` authors (Mayur Sharma, Dr. Juuhi Rai).

### Other pages

- `work.html` has no JSON-LD in the inspected markup.
- Service pages and blog posts were not individually inspected for schema.

---

## 7. robots.txt

```
User-Agent: *
Allow: /
Disallow: /*.pdf$
Disallow: /temp_cards.html
Disallow: /generated_cards.html

Sitemap: https://shalinichoudhary.in/sitemap.xml
```

All canonical HTML pages are crawlable. PDFs are blocked (covers `images/Shalinicv.pdf`). Two scratch HTML files are blocked.

---

## 8. sitemap.xml

49 URLs total: 14 top-level pages (priority 1.00 or 0.80) and 35 blog-post URLs (priority 0.64).

Top-level pages included:

- `/` (priority 1.00)
- `/about.html`, `/blogs.html`, `/contact.html`, `/work.html` (0.80)
- `/blogs/ai-search.html`, `/blogs/analytics-measurement.html`, `/blogs/conversion-performance.html`, `/blogs/growth-strategy.html`, `/blogs/seo-strategy.html` (0.80)
- `/conversion-optimisation-strategy.html`, `/growth-marketing-strategy.html`, `/marketing-analytics-ga4-consultant.html`, `/seo-strategy-consultant.html` (0.80)

Last-modified dates range from `2026-07-28` to `2026-07-30`. All URLs use `https://shalinichoudhary.in/` as the base.

---

## 9. Nav markup (hand-duplicated across pages)

Nav is duplicated in every HTML file. No templating engine or server-side includes. Structure is identical across all pages:

```html
<header class="site-header">
  <div class="site-header-inner">
    <a href="/" class="brand" aria-label="Go to homepage">
      <img src="images/logo-image.webp" alt="Shalini Choudhary Logo" class="logo-image" width="156" height="156">
    </a>
    <button class="menu-toggle" aria-controls="main-navigation" aria-expanded="false">
      <span class="hamburger"></span>
    </button>
    <nav class="site-nav" id="main-navigation" aria-label="Primary navigation">
      <a href="/work.html">Work</a>
      <a href="/seo-strategy-consultant.html">SEO Strategy</a>
      <a href="/growth-marketing-strategy.html">Growth Strategy</a>
      <a href="/about.html">About</a>
      <a href="blogs.html">Blog</a>
      <a href="contact.html" class="cta-button small-btn">Get in touch</a>
    </nav>
  </div>
</header>
```

Note: `blogs.html` and `contact.html` links use relative paths (no leading `/`), while other nav links use root-relative paths (with leading `/`). This is an existing inconsistency.

---

## 10. Footer markup (hand-duplicated across pages)

Footer is also duplicated in every HTML file. The tagline copy varies slightly page to page. Core structure:

```html
<footer class="tj-footer-area">
  <div class="footer-content footer-grid">
    <div class="footer-brand">
      <span class="footer-kicker">...</span>
      <h2>...</h2>
      <p class="footer-small">...</p>
      <a class="cta-button footer-cta-button" href="...">Get in touch</a>
    </div>
    <div class="footer-links"> <!-- Services or Explore nav --> </div>
    <div class="footer-links"> <!-- Explore nav (homepage only) --> </div>
    <div class="footer-contact">
      <!-- Social: LinkedIn, Twitter -->
      <!-- Email link -->
    </div>
  </div>
  <div class="footer-meta">
    <p class="copyright">2026 All rights reserved by Shalini Choudhary</p>
  </div>
</footer>
```

`index.html` footer has two `footer-links` columns (Services and Explore). `work.html` footer has one (Explore only). Footer is styled by `footer.css` (bundled) plus page-level `<style>` blocks for mobile alignment overrides.

---

## 11. llms.txt

Present at `/llms.txt`. Contains a structured plain-text summary of the site for LLM consumption: identity, key pages, service pages, and all blog posts with absolute URLs. Not disallowed by robots.txt.

---

## 12. Python helper scripts (not deployed)

| Script | Purpose |
|---|---|
| `generate_blog2.py`, `generate_blog3.py` | Blog HTML generation |
| `generate_sitemap.py` | Sitemap generation |
| `generate_cards.py`, `inject_cards.py` | Blog card HTML generation |
| `update_blogs.py` | Blog content update utility |
| `update_nav.py` | Nav update utility |
| `fix_links.py` | Link correction utility |
| `debug_regex.py` | Regex debugging helper |
| `replace_featured.py` | Featured content replacement |
| `resize_images.py` | Image resize utility |

---

## 13. Key observations for the revamp

1. **No build tool.** CSS is bundled manually; JS is loaded as separate end-of-body scripts. No `package.json`.
2. **Nav and footer are hand-duplicated** across every HTML file. Changes must be applied to all files individually or via the `update_nav.py` script pattern.
3. **Inline `<style>` blocks** on individual pages carry significant page-specific CSS; rationalising these into the bundle will be needed if the design system is standardised.
4. **`gsap.min.js`** is present but usage is unconfirmed in current templates; may be a legacy inclusion.
5. **Font Awesome loading is inconsistent**: lazy-loaded on `index.html` and `work.html`, synchronous on `about.html`.
6. **`worksFor` in JSON-LD** still points to `GUS Global`. This should be reviewed given the Sep 2025 end date from the proof-points file.
7. **Stat bar on homepage** shows "8+" years. The proof-points file uses "Since 2016" rather than a years figure; these will need aligning in a later revamp step.
8. **`work.html` has no JSON-LD** — a structured data gap on a high-value page.
9. **Blog category stub files** (`blogs/ai-search.html` etc.) are 687-747 bytes each, likely thin redirect or placeholder pages.
