import os
import re
import glob

def update_nav_links(base_dir):
    html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)
    
    # Catch any href ending with #impact-section pointing to Impact
    pattern1 = re.compile(r'<a href="[^"]*#impact-section"[^>]*>Impact</a>')
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = pattern1.sub(r'<a href="/about.html">About</a>', content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")

if __name__ == '__main__':
    update_nav_links('/Users/shalini/Documents/shalinichoudhary')

