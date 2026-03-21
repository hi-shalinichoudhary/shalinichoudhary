import os
import datetime
from xml.sax.saxutils import escape

# Configuration
BASE_DIR = '/Users/shalini/Documents/shalinichoudhary'
BASE_URL = 'https://shalinichoudhary.in/'
OUTPUT_FILE = os.path.join(BASE_DIR, 'sitemap.xml')

# Files or directories to ignore
IGNORE_FILES = {'temp_cards.html', 'generated_cards.html', '404.html'}
IGNORE_DIRS = {'.git', '.github', 'unused_assets', 'css', 'js', 'images'}

def get_priority(rel_path):
    # Root index gets highest priority
    if rel_path == 'index.html':
        return '1.00'
    
    parts = rel_path.split('/')
    # Top level pages (blogs.html, contact.html)
    if len(parts) == 1:
        return '0.80'
    # Level 1 inside blogs (e.g. blogs/strategy.html)
    elif len(parts) == 2 and parts[0] == 'blogs':
        return '0.80'
    # Deeper level posts (e.g. blogs/strategy/post.html)
    else:
        return '0.64'

def generate_sitemap():
    urls = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Prevent walking into ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if not file.endswith('.html'):
                continue
            if file in IGNORE_FILES:
                continue
                
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            
            # Use forward slashes for URLs
            rel_url_path = rel_path.replace(os.sep, '/')
            
            # Avoid placing 'index.html' explicitly in the loc
            if rel_url_path == 'index.html':
                loc = BASE_URL
            else:
                loc = BASE_URL + rel_url_path
                
            loc = escape(loc)
            
            # File modification time
            mtime = os.path.getmtime(full_path)
            dt = datetime.datetime.fromtimestamp(mtime, tz=datetime.timezone.utc)
            lastmod = dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            
            priority = get_priority(rel_url_path)
            
            urls.append({
                'loc': loc,
                'lastmod': lastmod,
                'priority': priority,
                'rel_path': rel_url_path
            })
            
    # Sort urls for consistency:
    # 1. index.html first.
    # 2. Higher priority first.
    # 3. Alphabetical loc.
    urls.sort(key=lambda x: (
        not x['rel_path'] == 'index.html', 
        -float(x['priority']), 
        x['loc']
    ))

    xml_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset',
        '      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9',
        '            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
        '<!-- dynamically generated sitemap -->'
    ]
    
    for u in urls:
        xml_content.append('  <url>')
        xml_content.append(f"    <loc>{u['loc']}</loc>")
        xml_content.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        xml_content.append(f"    <priority>{u['priority']}</priority>")
        xml_content.append('  </url>')
        
    xml_content.append('</urlset>')
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_content) + '\n')
        
    print(f"Generated {OUTPUT_FILE} with {len(urls)} URLs.")

if __name__ == '__main__':
    generate_sitemap()
