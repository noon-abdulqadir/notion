import os
import re
import json

images_dir = 'images'
pattern = re.compile(r'^[0-9].*\.jpeg$', re.IGNORECASE)

files = [f for f in os.listdir(images_dir) if pattern.match(f)]
files.sort()

# Write the list to images.json for use in notion.html
with open('images.json', 'w') as f:
	json.dump(files, f)

print(f"Wrote {len(files)} image filenames to images.json")
