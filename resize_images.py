from PIL import Image
import os

images_to_resize = [
    {"path": "images/Shalini.webp", "max_width": 800},
    {"path": "images/logo6.webp", "max_width": 500},
    {"path": "images/logo5.webp", "max_width": 500},
    {"path": "images/logo2.webp", "max_width": 500},
    {"path": "images/logo1.webp", "max_width": 500},
]

for item in images_to_resize:
    path = item["path"]
    max_width = item["max_width"]
    
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
        
    try:
        img = Image.open(path)
        original_width, original_height = img.size
        
        if original_width > max_width:
            ratio = max_width / original_width
            new_height = int(original_height * ratio)
            
            # Resize
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            img.save(path, "WEBP", quality=85)
            
            print(f"Resized {path}: {original_width}x{original_height} -> {max_width}x{new_height}")
        else:
            print(f"Skipped {path}: Width {original_width} <= {max_width}")
            
    except Exception as e:
        print(f"Error processing {path}: {e}")
