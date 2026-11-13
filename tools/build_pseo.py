import csv
import os
import re

# --- Helper Functions ---
def slugify(text: str) -> str:
    """
    Format a string into a clean, lowercase, hyphen-separated slug:
    - Lowercases text
    - Strips whitespace
    - Replaces spaces and underscores with hyphens
    - Removes characters other than a-z, 0-9, and hyphens
    - Collapses consecutive hyphens and trims edges
    """
    text = str(text).lower().strip()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^a-z0-9\-]', '', text)
    return re.sub(r'-+', '-', text).strip('-')


# --- Configuration ---
# Resolve paths relative to this script so it runs reliably from any working directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(SCRIPT_DIR, 'data.csv')
template_file_path = os.path.join(SCRIPT_DIR, 'template.html')
# Output directory matching where growth strategy posts live
output_directory = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'blogs', 'growth-strategy'))

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Read the template
with open(template_file_path, 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()

# Read the CSV and generate files
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    # Use csv.DictReader to automatically map headers to dictionary keys
    reader = csv.DictReader(csv_file)
    
    count = 0
    for row in reader:
        # Create a fresh copy of the template for this row
        page_content = template_content
        
        # Apply lowercasing, space/underscore replacement, and character sanitization
        clean_slug = slugify(row.get('slug') or row.get('tool_name', ''))
        
        # Construct the internal URL strictly matching the clean file name
        internal_url = f"/blogs/growth-strategy/track-{clean_slug}-organic-pipeline-ga4.html"
        
        # Construct the dynamic self-referencing canonical URL
        canonical_url = f"https://shalinichoudhary.in{internal_url}"
        
        # Map dynamic URL variables to template placeholders
        page_content = page_content.replace("{clean_slug}", clean_slug)
        page_content = page_content.replace("{internal_url}", internal_url)
        page_content = page_content.replace("{canonical_url}", canonical_url)
        
        # Replace placeholders {column_name} with actual row data
        for key, value in row.items():
            placeholder = "{" + key + "}"
            page_content = page_content.replace(placeholder, str(value))
        
        # Catch and normalize any legacy unslugified URL patterns that might be present
        page_content = re.sub(
            r'/blogs/growth-strategy/how-to-track-[^"\'\s>]+-organic-pipeline-in-ga4\.html',
            internal_url,
            page_content,
            flags=re.IGNORECASE
        )
        
        # Define the output filename matching the clean slugified structure
        output_filename = f"track-{clean_slug}-organic-pipeline-ga4.html"
        output_path = os.path.join(output_directory, output_filename)
        
        # Write the new HTML file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(page_content)
            
        count += 1

print(f"✅ Success! Generated {count} RevOps pSEO pages.")
