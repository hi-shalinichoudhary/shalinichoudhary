import os
import re

# Base directory for blogs
BLOGS_DIR = "/Users/shalini/Documents/shalinichoudhary/blogs"
# Output file
OUTPUT_FILE = "generated_cards.html"

# Categories mapping - adjusted to match probable button filters
# I will confirm these after reading the file, but for now I use the folder names 
# which are likely the slugs.
CATEGORIES = {
    "google-analytics": "analytics", # Assuming button is 'analytics' or 'google-analytics'
    "seo-industry": "seo-industry",
    "seo-tips": "seo-tips",
    "strategy": "strategy",
    "social-impact": "social-impact"
}

# Category Display Names
CAT_DISPLAY = {
    "google-analytics": "GOOGLE ANALYTICS",
    "seo-industry": "SEO INDUSTRY",
    "seo-tips": "SEO TIPS",
    "strategy": "STRATEGY",
    "social-impact": "SOCIAL IMPACT"
}

def extract_meta(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Title: <h1>...</h1>
        title_match = re.search(r'<h1>(.*?)</h1>', content, re.DOTALL)
        title_text = title_match.group(1).strip() if title_match else "Untitled Post"
        
        # Description: <meta name="description" content="...">
        desc_match = re.search(r'<meta name="description" content="(.*?)"', content, re.DOTALL)
        desc = desc_match.group(1).strip() if desc_match else ""
        
        # Image extraction: robust method
        img_src = ""
        # Find all img tags
        img_tags = re.findall(r'<img\s+[^>]*?>', content, re.DOTALL)
        for tag in img_tags:
            # Check if this tag has the class
            if "post-feature-image" in tag:
                # Extract src
                src_match = re.search(r'src=["\'](.*?)["\']', tag)
                if src_match:
                    img_src = src_match.group(1)
                    img_src = img_src.replace('../../', '')
                    break
        
        # Date: Inside <p class="post-meta">...| Month Year |...</p>
        date_text = "May, 2024" # Default
        meta_match = re.search(r'<p class="post-meta">(.*?)</p>', content, re.DOTALL)
        if meta_match:
            meta_text = meta_match.group(1)
            parts = meta_text.split('|')
            for part in parts:
                p = part.strip()
                if any(y in p for y in ['2023', '2024', '2025']):
                    date_text = p
                    # Clean up &nbsp;
                    date_text = date_text.replace('&nbsp;', '').strip()
        
        return {
            "title": title_text,
            "description": desc,
            "image": img_src,
            "date": date_text
        }

html_output = []
total_count = 0

for folder in sorted(CATEGORIES.keys()):
    cat_slug = CATEGORIES[folder]
    folder_path = os.path.join(BLOGS_DIR, folder)
    if not os.path.exists(folder_path):
        continue
        
    files = [f for f in os.listdir(folder_path) if f.endswith('.html')]
    files.sort()
    
    for filename in files:
        if "Copy" in filename: 
            continue
            
        file_path = os.path.join(folder_path, filename)
        meta = extract_meta(file_path)
        
        if meta['title'] == "Untitled Post":
            continue

        # Heuristic for generic Focus/Outcome based on category
        focus = "Strategy"
        outcome = "Growth"
        if cat_slug == "analytics":
            focus = "Measurement"
            outcome = "Clarity"
        elif cat_slug == "seo-tips":
            focus = "Optimization"
            outcome = "Visibility"
        elif cat_slug == "seo-industry":
            focus = "Impact"
            outcome = "Rankings"
        elif cat_slug == "social-impact":
            focus = "Awareness"
            outcome = "Change"

        card_html = f"""
                <!-- POST {total_count + 1} ({cat_slug}) -->
                <article class="blog-card" data-category="{cat_slug}">
                    <a href="blogs/{folder}/{filename}" class="blog-image-link">
                        <img src="{meta['image']}" alt="{meta['title']}" class="blog-image" loading="lazy">
                    </a>
                    <div class="blog-content-area">
                        <div class="blog-card-meta">
                            <span class="blog-meta-category">{CAT_DISPLAY.get(folder, 'BLOG')} | {meta['date']}</span>
                            <span class="blog-meta-reading">5 min read</span>
                        </div>
                        <h3><a href="blogs/{folder}/{filename}">{meta['title']}</a></h3>
                        <p class="blog-excerpt">{meta['description'][:120]}...</p>
                        <div class="blog-card-foot">
                            <span class="blog-card-signal">Focus: {focus}</span>
                            <span class="blog-card-signal">Outcome: {outcome}</span>
                        </div>
                        <div class="blog-card-footer">
                            <div class="blog-author">
                                <img src="images/author-me.webp" alt="Shalini Choudhary" class="blog-author-avatar">
                                <span class="blog-author-name">Shalini Choudhary</span>
                            </div>
                            <a href="blogs/{folder}/{filename}" class="blog-card-read">Read <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
                        </div>
                        <div class="blog-card-actions">
                            <button class="action-btn" aria-label="Like"><i class="far fa-heart"></i></button>
                            <button class="action-btn" aria-label="Share"><i class="fas fa-share-alt"></i></button>
                            <button class="action-btn" aria-label="Bookmark"><i class="far fa-bookmark"></i></button>
                        </div>
                    </div>
                </article>"""
        html_output.append(card_html)
        total_count += 1

# Write to output file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(chr(10).join(html_output))

print(f"Generated {total_count} cards.")
