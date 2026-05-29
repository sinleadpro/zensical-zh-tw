import os
import re

# --- CONFIGURATION ---
MD_FOLDER = "../input"  # <-- change this to your folder

# Regex to match [![alt](image_url)](any_url) pattern
# Captures the inner alt and image_url, ignores the outer link
pattern = re.compile(r'\[\!\[(.*?)\]\((.*?)\)\]\((?:.*?)\)')

# --- PROCESS FILES ---
for root, dirs, files in os.walk(MD_FOLDER):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace wrapped image with plain image
            new_content = pattern.sub(r'![\1](\2)', content)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {file_path}")
