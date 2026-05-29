import os
import re
import yaml
import requests
import tempfile
from PIL import Image
import pytesseract

# ---------------------
# CONFIG
# ---------------------
MD_FOLDER = "../input"  # folder containing your markdown files
REGULAR_TEXT_MARKERS = ["#", "*", "-", "+"]  # first line of normal content

# regex to match markdown image url: ![](URL)
image_url_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

# ---------------------
# FUNCTIONS
# ---------------------
def ocr_image_from_url(url):
    """Download image and run OCR using chi_tra."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(suffix=".png") as tmp_file:
            for chunk in response.iter_content(1024):
                tmp_file.write(chunk)
            tmp_file.flush()
            text = pytesseract.image_to_string(Image.open(tmp_file.name), lang="chi_tra")
            return text.strip()
    except Exception as e:
        print(f"Error OCR-ing {url}: {e}")
        return ""

def parse_ocr_text(ocr_text):
    """
    Parse OCR text for known keys:
    - 適用方案 → plans
    - 適用金流 → features
    - 適用站別 → sites
    """
    mapping = {
        "適用方案": "plans",
        "適用金流": "features",
        "適用站別": "sites"
    }
    result = {}
    for line in ocr_text.splitlines():
        for key, yaml_key in mapping.items():
            if key in line:
                value = line.split(key)[-1].strip()
                if value:
                    result[yaml_key] = value
    return result

def process_md_file(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # ---------------------
    # Separate YAML front matter
    # ---------------------
    yaml_start = None
    yaml_end = None
    if lines[0].strip() == "---":
        yaml_start = 0
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                yaml_end = i
                break

    yaml_data = {}
    body_lines = lines
    if yaml_start is not None and yaml_end is not None:
        yaml_content = "".join(lines[yaml_start+1:yaml_end])
        yaml_data = yaml.safe_load(yaml_content) or {}
        body_lines = lines[yaml_end+1:]

    # ---------------------
    # Split top section (before regular text)
    # ---------------------
    top_section = []
    rest_section = []
    hit_regular_text = False
    for line in body_lines:
        stripped = line.strip()
        if not hit_regular_text and any(stripped.startswith(marker) for marker in REGULAR_TEXT_MARKERS) and stripped != "":
            hit_regular_text = True
        if hit_regular_text:
            rest_section.append(line)
        else:
            top_section.append(line)

    # ---------------------
    # Process images in top_section
    # ---------------------
    processed_top = []
    for line in top_section:
        processed_top.append(line)
        match = image_url_pattern.search(line)
        if match:
            url = match.group(1)
            ocr_text = ocr_image_from_url(url)
            if ocr_text:
                processed_top.append(f"```ocr\n{ocr_text}\n```")
                # update YAML
                kv = parse_ocr_text(ocr_text)
                for k, v in kv.items():
                    yaml_data[k] = v

    # ---------------------
    # Reconstruct markdown file
    # ---------------------
    final_lines = []

    # YAML front matter
    if yaml_start is not None and yaml_end is not None:
        final_lines.append("---")
        final_lines += yaml.dump(yaml_data, allow_unicode=True, sort_keys=False).splitlines()
        final_lines.append("---")

    final_lines += processed_top
    final_lines += rest_section

    # Write back
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(final_lines) + "\n")

    print(f"Processed: {md_path}")

def process_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                process_md_file(os.path.join(root, file))

# ---------------------
# RUN
# ---------------------
if __name__ == "__main__":
    process_folder(MD_FOLDER)
