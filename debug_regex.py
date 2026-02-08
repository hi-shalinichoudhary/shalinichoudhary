import re

filepath = "/Users/shalini/Documents/shalinichoudhary/blogs/strategy/technical-seo-foundations-building-a-strong-house-for-your-content.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File content length: {len(content)}")

# Test the regex
# match = re.search(r'(<div class="author-cta-box"[^>]*>.*?</div>\s*</div>\s*</div>)', content, re.DOTALL)
pattern = r'(<div class="author-cta-box"[^>]*>.*?</div>\s*</div>\s*</div>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    print("Match found!")
    print(match.group(1)[:100] + "..." + match.group(1)[-100:])
else:
    print("No match found.")
    
    # Let's start with finding the start tag
    start_tag = re.search(r'<div class="author-cta-box"[^>]*>', content)
    if start_tag:
        print(f"Start tag found: {start_tag.group(0)}")
        start_pos = start_tag.start()
        # Print the next 500 chars from start_pos
        print(f"Context after start tag:\n{content[start_pos:start_pos+500]}")
    else:
        print("Start tag NOT found.")
