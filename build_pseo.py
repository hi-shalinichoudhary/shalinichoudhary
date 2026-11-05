import csv
import os
import re

# --- Configuration ---
csv_file_path = 'data.csv'
template_file_path = 'template.md'
# Change this path to match exactly where your growth strategy posts live
output_directory = 'content/blogs/growth-strategy/' 

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
        
        # Replace placeholders {column_name} with actual row data
        for key, value in row.items():
            placeholder = "{" + key + "}"
            page_content = page_content.replace(placeholder, str(value))
            
        # Clean up the slug just in case there are weird spaces
        clean_slug = re.sub(r'[^a-z0-9\-]', '', str(row['slug']).lower().strip())
        
        # Define the output filename
        output_filename = f"track-{clean_slug}-organic-pipeline-ga4.md"
        output_path = os.path.join(output_directory, output_filename)
        
        # Write the new Markdown file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(page_content)
            
        count += 1

print(f"✅ Success! Generated {count} RevOps pSEO pages.")
