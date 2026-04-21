import sys
import re

file_path = "/Users/shalini/Documents/shalinichoudhary/blogs.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'(<section class="section-wrapper featured-insight">.*?</section>)', re.DOTALL)
match = pattern.search(content)

if not match:
    print("Could not find featured insight section")
    sys.exit(1)

old_section = match.group(1)

new_section = '''<section class="section-wrapper featured-insight">
            <div class="featured-card">
                <div class="featured-image-panel">
                    <a href="blogs/growth-strategy/what-eight-years-in-marketing-actually-taught-me-about-strategy.html"
                        class="featured-image-link">
                        <img src="images/blog-images/strategy/Blog_image_marketing_202604211718.jpeg" alt="Marketing Strategy Lessons"
                            class="featured-image">
                        <span class="featured-image-tag">Growth Strategy</span>
                    </a>
                </div>
                <div class="featured-copy">
                    <span class="eyebrow">FEATURED INSIGHT</span>
                    <div class="featured-meta-row">
                        <span class="read-time">
                            <svg viewBox="0 0 24 24" aria-hidden="true">
                                <path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-linecap="round"
                                    stroke-linejoin="round" stroke-width="1.6" />
                                <circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6" />
                            </svg>
                            4 min read
                        </span>
                        <span class="featured-date">Apr 2026</span>
                    </div>
                    <h2><a href="blogs/growth-strategy/what-eight-years-in-marketing-actually-taught-me-about-strategy.html">What Eight Years in Marketing Actually Taught Me About Strategy</a></h2>
                    <p class="section-description">Not a career retrospective; a series of hard-won lessons from agency life at Ogilvy, GroupM and beyond. What experience actually teaches you, and what it can't.</p>
                    <div class="featured-metrics">
                        <div class="featured-metric-card">
                            <span class="metric-label">Focus</span>
                            <span class="metric-value">Strategy</span>
                        </div>
                        <div class="featured-metric-card">
                            <span class="metric-label">Outcome</span>
                            <span class="metric-value">Lessons</span>
                        </div>
                    </div>
                    <div class="featured-author-row">
                        <div class="featured-author">
                            <img src="images/author-me.webp" alt="Shalini Choudhary" class="featured-author-avatar">
                            <span class="featured-author-name">Shalini Choudhary</span>
                        </div>
                        <div class="featured-actions">
                            <button class="icon-button" aria-label="Save insight">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <path
                                        d="M12 21s-7.5-4.35-9.7-8.6C.9 9.3 2.2 6.4 5.3 5.6c2-.6 4 .1 5.4 1.7 1.4-1.6 3.4-2.3 5.4-1.7 3.1.8 4.4 3.7 3 6.8C19.5 16.7 12 21 12 21z"
                                        fill="currentColor" />
                                </svg>
                            </button>
                            <button class="icon-button" aria-label="Share insight">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <path
                                        d="M18 8a3 3 0 1 0-2.8-4H15a3 3 0 0 0 0 .5L8.4 8.1a3 3 0 0 0-2.4-1.1 3 3 0 1 0 0 6c.9 0 1.7-.3 2.3-1l6.6-3.6A3 3 0 0 0 18 8z"
                                        fill="currentColor" />
                                </svg>
                            </button>
                            <a href="blogs/growth-strategy/what-eight-years-in-marketing-actually-taught-me-about-strategy.html"
                                class="text-link read-link">Read
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <path d="M7 12h9m0 0-4-4m4 4-4 4" fill="none" stroke="currentColor"
                                        stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old_section, new_section)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated featured insight section successfully!")
