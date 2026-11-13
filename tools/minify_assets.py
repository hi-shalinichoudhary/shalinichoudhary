#!/usr/bin/env python3
import os
import re
import subprocess
import sys

# Paths
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_DIR = os.path.join(REPO_ROOT, 'css')
JS_DIR = os.path.join(REPO_ROOT, 'js')
TOOLS_DIR = os.path.join(REPO_ROOT, 'tools')

# --- 1. CSS Minification Engine ---
def minify_css(css: str) -> str:
    # Remove comments
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    
    # Extract and protect strings, url(), and calc()
    tokens = []
    
    def repl_token(m):
        tokens.append(m.group(0))
        return f'___CSS_TOKEN_{len(tokens)-1}___'
    
    # Save strings and url(...)
    css = re.sub(r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|url\([^)]+\))', repl_token, css)
    
    # Save calc(...) with balanced parens
    res = []
    i = 0
    n = len(css)
    while i < n:
        if css[i:i+5].lower() == 'calc(':
            count = 1
            j = i + 5
            while j < n and count > 0:
                if css[j] == '(':
                    count += 1
                elif css[j] == ')':
                    count -= 1
                j += 1
            calc_str = css[i:j]
            tokens.append(calc_str)
            res.append(f'___CSS_TOKEN_{len(tokens)-1}___')
            i = j
        else:
            res.append(css[i])
            i += 1
    css = ''.join(res)
    
    # Collapse whitespace
    css = re.sub(r'\s+', ' ', css)
    
    # Remove space around delimiters
    css = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', css)
    css = re.sub(r'\s*([\+\~])\s*', r'\1', css)
    
    # Remove trailing semicolons before closing brace
    css = re.sub(r';\}', '}', css)
    
    # Restore tokens in reverse order
    for idx in range(len(tokens) - 1, -1, -1):
        css = css.replace(f'___CSS_TOKEN_{idx}___', tokens[idx])
        
    return css.strip()


# --- 2. JavaScript Minification Engine (Crockford's JSMin) ---
class JavascriptMinifier(object):
    def __init__(self):
        self.the_a = ''
        self.the_b = ''
        self.lookahead = None
        self.input = ''
        self.output = []
        self.index = 0

    def is_alphanumeric(self, c):
        return ((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9') or
                (c >= 'A' and c <= 'Z') or c == '_' or c == '$' or c == '\\' or (c is not None and ord(c) > 126))

    def get(self):
        c = self.lookahead
        self.lookahead = None
        if c is None:
            if self.index < len(self.input):
                c = self.input[self.index]
                self.index += 1
            else:
                c = ''
        if c >= ' ' or c == '\n' or c == '':
            return c
        if c == '\r':
            return '\n'
        return ' '

    def peek(self):
        self.lookahead = self.get()
        return self.lookahead

    def next(self):
        c = self.get()
        if c == '/':
            p = self.peek()
            if p == '/':
                while True:
                    c = self.get()
                    if c <= '\n':
                        return c
            elif p == '*':
                self.get()
                while True:
                    c = self.get()
                    if c == '*':
                        if self.peek() == '/':
                            self.get()
                            return ' '
                    elif c == '':
                        raise Exception("Unterminated comment.")
        return c

    def action(self, d):
        if d <= 1:
            self.output.append(self.the_a)
        if d <= 2:
            self.the_a = self.the_b
            if self.the_a == "'" or self.the_a == '"' or self.the_a == '`':
                quote = self.the_a
                while True:
                    self.output.append(self.the_a)
                    self.the_a = self.get()
                    if self.the_a == quote:
                        break
                    if self.the_a == '\\':
                        self.output.append(self.the_a)
                        self.the_a = self.get()
                    if self.the_a == '':
                        raise Exception("Unterminated string literal.")
        if d <= 3:
            self.the_b = self.next()
            if self.the_b == '/' and self.the_a in '(,=:[!&|?{};~+-/\n':
                self.output.append(self.the_a)
                if self.the_a in '/*+-':
                    self.output.append(' ')
                self.output.append(self.the_b)
                while True:
                    c = self.get()
                    if c == '[':
                        while True:
                            self.output.append(c)
                            c = self.get()
                            if c == ']':
                                break
                            if c == '\\':
                                self.output.append(c)
                                c = self.get()
                            if c == '':
                                raise Exception("Unterminated set in Regular Expression literal.")
                    elif c == '/':
                        break
                    elif c == '\\':
                        self.output.append(c)
                        c = self.get()
                    elif c <= '\n':
                        raise Exception("Unterminated Regular Expression literal.")
                    self.output.append(c)
                self.the_b = self.next()

    def minify(self, text):
        self.input = text
        self.index = 0
        self.output = []
        self.the_a = '\n'
        self.action(3)
        while self.the_a != '':
            if self.the_a == ' ':
                if self.is_alphanumeric(self.the_b):
                    self.action(1)
                else:
                    self.action(2)
            elif self.the_a == '\n':
                if self.the_b in '{[(+-~!':
                    self.action(1)
                elif self.the_b == ' ':
                    self.action(3)
                else:
                    if self.is_alphanumeric(self.the_b):
                        self.action(1)
                    else:
                        self.action(2)
            else:
                if self.the_b == ' ':
                    if self.is_alphanumeric(self.the_a):
                        self.action(1)
                    else:
                        self.action(3)
                elif self.the_b == '\n':
                    if self.the_a in '}]+-)"\'`':
                        self.action(1)
                    else:
                        if self.is_alphanumeric(self.the_a):
                            self.action(1)
                        else:
                            self.action(3)
                else:
                    self.action(1)
        return ''.join(self.output).strip()


def run():
    print("=== 1. Minifying CSS Assets ===")
    stats = []

    # bundle.min.css (strict minification of existing file)
    bundle_path = os.path.join(CSS_DIR, 'bundle.min.css')
    with open(bundle_path, 'r', encoding='utf-8') as f:
        orig_bundle = f.read()
    min_bundle = minify_css(orig_bundle)
    with open(bundle_path, 'w', encoding='utf-8') as f:
        f.write(min_bundle)
    stats.append(('css/bundle.min.css', len(orig_bundle), len(min_bundle)))

    # home-enhancements.css -> home-enhancements.min.css
    home_src = os.path.join(CSS_DIR, 'home-enhancements.css')
    home_min_dest = os.path.join(CSS_DIR, 'home-enhancements.min.css')
    with open(home_src, 'r', encoding='utf-8') as f:
        orig_home = f.read()
    min_home = minify_css(orig_home)
    with open(home_min_dest, 'w', encoding='utf-8') as f:
        f.write(min_home)
    stats.append(('css/home-enhancements.min.css', len(orig_home), len(min_home)))

    print("=== 2. Minifying JS Assets ===")
    js_minifier = JavascriptMinifier()
    js_files = [
        'components.js',
        'script.js',
        'prototype.js',
        'antigravity.js',
        'scroll-reveal.js'
    ]

    for jf in js_files:
        src_path = os.path.join(JS_DIR, jf)
        min_name = jf.replace('.js', '.min.js')
        dest_path = os.path.join(JS_DIR, min_name)

        with open(src_path, 'r', encoding='utf-8') as f:
            orig_js = f.read()
        min_js = js_minifier.minify(orig_js)
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(min_js)

        # Validate with node -c
        check = subprocess.run(['node', '-c', dest_path], capture_output=True, text=True)
        if check.returncode != 0:
            print(f"ERROR: {min_name} failed node syntax check!\n{check.stderr}")
            sys.exit(1)
        stats.append((f'js/{min_name}', len(orig_js), len(min_js)))

    print("=== 3. Updating HTML Asset References ===")
    # Update all .html files
    updated_files = 0
    total_html_files = 0

    for root, dirs, files in os.walk(REPO_ROOT):
        if '.git' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                total_html_files += 1
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as fh:
                    orig_content = fh.read()

                new_content = orig_content
                # Update CSS: home-enhancements.css -> home-enhancements.min.css
                new_content = re.sub(r'(?<![a-zA-Z0-9_-])home-enhancements\.css(?:\?[^"\'\s>]+)?', 'home-enhancements.min.css', new_content)
                
                # Update JS references
                new_content = re.sub(r'(?<![a-zA-Z0-9_-])components\.js(?:\?[^"\'\s>]+)?', 'components.min.js', new_content)
                new_content = re.sub(r'(?<![a-zA-Z0-9_-])script\.js(?:\?[^"\'\s>]+)?', 'script.min.js', new_content)
                new_content = re.sub(r'(?<![a-zA-Z0-9_-])prototype\.js(?:\?[^"\'\s>]+)?', 'prototype.min.js', new_content)
                new_content = re.sub(r'(?<![a-zA-Z0-9_-])antigravity\.js(?:\?[^"\'\s>]+)?', 'antigravity.min.js', new_content)
                new_content = re.sub(r'(?<![a-zA-Z0-9_-])scroll-reveal\.js(?:\?[^"\'\s>]+)?', 'scroll-reveal.min.js', new_content)

                if new_content != orig_content:
                    with open(fpath, 'w', encoding='utf-8') as fh:
                        fh.write(new_content)
                    updated_files += 1

    print(f"Updated asset references across {updated_files} of {total_html_files} HTML files.")

    # Re-run pSEO generator to keep growth-strategy directory synchronized
    print("=== 4. Re-running pSEO Generation ===")
    pseo_script = os.path.join(TOOLS_DIR, 'build_pseo.py')
    subprocess.run(['python3', pseo_script], check=True)

    print("\n=== MINIFICATION SUMMARY ===")
    print(f"{'Asset':<32} {'Original':>10} {'Minified':>10} {'Reduction':>10}")
    print("-" * 65)
    for name, orig, minified in stats:
        pct = (1 - minified / orig) * 100
        print(f"{name:<32} {orig:>8} B {minified:>8} B {pct:>9.1f}%")

if __name__ == '__main__':
    run()
