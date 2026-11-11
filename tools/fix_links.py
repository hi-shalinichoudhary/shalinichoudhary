import os
import re

def fix_links(directory):
    # Regex to match href="...index.html..." variants
    # hooks:
    # 1. match relative prefixes: (?:(\.\./|\./)*)?
    # 2. match index.html
    # 3. match optional anchor: (#[\w-]*)?
    
    # We want to replace mainly:
    # href="index.html" -> href="/"
    # href="./index.html" -> href="/"
    # href="../index.html" -> href="/"
    # href="../../index.html" -> href="/"
    # href="index.html#foo" -> href="/#foo"
    
    # Pattern: href=["']((?:\.\./|\./)*)index\.html(#[\w-]*)?["']
    # We need to preserve the quote style.
    
    pattern = re.compile(r'href=(["\'])((?:\.\./|\./)*)index\.html(#[\w-]*)?\1')
    
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Function to pass to re.sub to handle the match
                def replacer(match):
                    quote = match.group(1) # " or '
                    anchor = match.group(3) if match.group(3) else ""
                    # If it's a link to index.html (with or without anchor), replace with / + anchor
                    return f'href={quote}/{anchor}{quote}'
                
                new_content, n = pattern.subn(replacer, content)
                
                if n > 0:
                    print(f"Updating {filepath}: {n} changes")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += n

    print(f"Total replacements: {count}")

if __name__ == "__main__":
    fix_links(".")
