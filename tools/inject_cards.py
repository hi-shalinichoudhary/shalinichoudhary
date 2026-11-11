import sys

BLOGS_FILE = '/Users/shalini/Documents/shalinichoudhary/blogs.html'
CARDS_FILE = '/Users/shalini/Documents/shalinichoudhary/generated_cards.html'

with open(BLOGS_FILE, 'r') as f:
    lines = f.readlines()

start_line = -1
end_line = -1

for i, line in enumerate(lines):
    if 'id="latest-posts-grid"' in line:
        start_line = i
    
    if start_line != -1 and i > start_line:
        # Look for closing div. Check context.
        # We expect:
        # </div>
        # (empty line)
        # <div class="blog-library-actions">
        
        if i + 2 < len(lines):
            if 'class="blog-library-actions"' in lines[i+2]:
                if '</div>' in line:
                    end_line = i
                    break

if start_line == -1 or end_line == -1:
    print(f"Could not find bounds. Start: {start_line}, End: {end_line}")
    sys.exit(1)

print(f"Injecting between line {start_line+1} and {end_line+1}")

with open(CARDS_FILE, 'r') as f:
    new_cards = f.readlines()

# start_line is the index of <div id="latest-posts-grid"...>. We keep it.
# end_line is the index of </div>. We keep it.
# We replace everything textually between them.

final_lines = lines[:start_line+1] + new_cards + lines[end_line:]

with open(BLOGS_FILE, 'w') as f:
    f.writelines(final_lines)

print("Successfully injected cards.")
