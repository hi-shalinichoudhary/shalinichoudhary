import os
import re

# Define the new HTML blocks
SOCIAL_SIDEBAR_HTML = """
                <!-- NEW: Social & Interaction Sidebar -->
                <aside class="blog-interactions">
                    <div class="interaction-bar">
                        <button class="interaction-btn" aria-label="Like this post">
                            <i class="far fa-heart"></i>
                        </button>
                        <button class="interaction-btn" aria-label="Bookmark this post">
                            <i class="far fa-bookmark"></i>
                        </button>
                        <div class="interaction-divider"></div>
                        <a href="#" class="interaction-btn" aria-label="Share on Twitter">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="#" class="interaction-btn" aria-label="Share on LinkedIn">
                            <i class="fab fa-linkedin-in"></i>
                        </a>
                        <button class="interaction-btn" aria-label="Copy Link">
                            <i class="fas fa-link"></i>
                        </button>
                    </div>
                </aside>
"""

NEW_AUTHOR_BOX_HTML = """
                    <div class="author-cta-box">
                        <div class="author-box-content">
                            <div class="author-image-placeholder">
                                <img src="../../images/author-me.webp" alt="Author Shalini Choudhary">
                            </div>

                            <div class="author-details">
                                <div class="author-header">
                                    <h4 style="margin:0;">Shalini Choudhary</h4>
                                    <span class="author-badge">Strategy Expert</span>
                                </div>
                                <p class="author-bio">
                                    Senior SEO Manager specializing in performance-led digital growth. Decoding search complexities to drive meaningful organic results for global brands.
                                </p>
                                <div class="author-actions">
                                    <a href="../../contact.html" class="cta-button small-btn">Work with me</a>
                                    <div class="author-socials">
                                        <a href="https://twitter.com/shalinihooda" target="_blank"><i class="fab fa-twitter"></i></a>
                                        <a href="https://in.linkedin.com/in/shalini-choudhary" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
"""

# Regex to find the author box (flexible for style attributes and whitespace)
AUTHOR_BOX_REGEX = re.compile(r'<div class="author-cta-box".*?>(.*?)</div>\s*</div>', re.DOTALL)
# Simpler regex to match the outer div and replace everything inside/including it
AUTHOR_BOX_OUTER_REGEX = re.compile(r'<div class="author-cta-box".*?</div>\s*</div>\s*</div>', re.DOTALL)

# Target directory
BLOGS_DIR = "/Users/shalini/Documents/shalinichoudhary/blogs"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if it's a category listing page (usually shallower structure or different content)
    # Heuristic: Check for "reading-layout-wrapper" which is specific to posts
    if "reading-layout-wrapper" not in content:
        print(f"Skipping {filepath} (Not a blog post)")
        return

    updated = False

    # 1. Inject Social Sidebar if missing
    if "blog-interactions" not in content:
        target_str = '<div class="toc-sidebar-container">'
        if target_str in content:
            # Insert before toc-sidebar-container
            replacement = SOCIAL_SIDEBAR_HTML + "\n                " + target_str
            content = content.replace(target_str, replacement)
            print(f"Added Social Sidebar to {filepath}")
            updated = True
        else:
            print(f"WARNING: Could not find insertion point for Sidebar in {filepath}")

    # 2. Update Author Box
    # We'll search for the div class="author-cta-box" and replace its entire block
    # Finding the end of the div can be tricky with regex. 
    # Let's use a simpler string replacement if the layout is consistent, 
    # or a robust regex if we expect variations.
    
    # Since we know the previous structure was fairly consistent, let's try to match the old image src as a marker
    if "author-me.png" in content or "author-me.webp" in content:
        # Check if it already has the new structure (e.g., "Strategy Expert" badge)
        if "Strategy Expert" in content:
             print(f"Author Box already updated in {filepath}")
        else:
            # It has the old box or an intermediate state.
            # Let's try to identify the block. 
            # The pattern <div class="author-cta-box" style="padding: 0;"> is common in old files.
            
            # Pattern A: Old style with padding: 0
            old_start = '<div class="author-cta-box" style="padding: 0;">'
            # Pattern B: Just class
            old_start_b = '<div class="author-cta-box">'
            
            # Find the start
            start_idx = content.find(old_start)
            if start_idx == -1:
                start_idx = content.find(old_start_b)
                
            if start_idx != -1:
                # Find the closing sequence. In the old file it ends with </div>\n                    </div> (closing content, closing box)
                # But it's safer to just look for the next <div class="reading-layout-wrapper"> closing if it's at the end?
                # No, let's look for "Need help adapting" which is unique to old text? 
                
                # BETTER APPROACH:
                # The author box is usually the last thing before the closing </div> of article-content-container
                # Let's use Regex to match the known old content structure if possible.
                
                # Old content snippet unique to old box:
                # We previously checked for "Need help adapting your strategy" but that varies.
                # Now we just try the broad regex directly.
                
                # Regex approach limited to this specific block structure
                # Matches <div class="author-cta-box"...> ... </div></div></div>
                # We use a greedy match for the content but restricted by the closing sequence
                match = re.search(r'(<div class="author-cta-box"[^>]*>.*?</div>\s*</div>\s*</div>)', content, re.DOTALL)
                if match:
                     old_block = match.group(1)
                     content = content.replace(old_block, NEW_AUTHOR_BOX_HTML.strip())
                     print(f"Updated Author Box in {filepath}")
                     updated = True
                else:
                     # Fallback check
                     print(f"WARNING: Could not regex match Author Box in {filepath}")
    
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    for root, dirs, files in os.walk(BLOGS_DIR):
        for file in files:
            if file.endswith(".html"):
                # Exclude the category list pages if they are in the root of BLOGS_DIR
                if root == BLOGS_DIR:
                    # These are likely list pages like strategy.html
                    # We'll peek at them, but likely skip based on "reading-layout-wrapper" check in update_file
                    pass
                
                filepath = os.path.join(root, file)
                update_file(filepath)

if __name__ == "__main__":
    main()
