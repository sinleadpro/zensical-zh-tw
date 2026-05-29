from pathlib import Path
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


# =========================================================
# Config
# =========================================================

SITE_DIR = Path("site")

BASE_URL = "https://help.cyberbiz.io"

LLMS_TXT = Path("llms.txt")
LLMS_FULL_TXT = Path("llms-full.txt")

SITEMAP_PATH = SITE_DIR / "sitemap.xml"


# =========================================================
# Read sitemap
# =========================================================

tree = ET.parse(SITEMAP_PATH)
root = tree.getroot()

namespace = {
    "ns": "http://www.sitemaps.org/schemas/sitemap/0.9"
}

urls = []

for url in root.findall("ns:url", namespace):

    loc = url.find("ns:loc", namespace)

    if loc is not None:
        urls.append(loc.text)


# =========================================================
# Generate llms.txt
# =========================================================

llms_lines = []

llms_lines.append("# CYBERBIZ DOCS\n")
llms_lines.append(
    "> 官方線上技術文件與操作指南，供 AI 程式助手與 LLM 快速理解系統架構。\n\n"
)

llms_lines.append("## Documentation Map\n\n")


# =========================================================
# Generate llms-full.txt
# =========================================================

full_lines = []

full_lines.append("# CYBERBIZ DOCS FULL\n\n")


# =========================================================
# Process each page
# =========================================================

for abs_url in urls:

    # -----------------------------------------------------
    # Convert URL to local HTML path
    # -----------------------------------------------------

    relative = abs_url.replace(BASE_URL, "").strip("/")

    if relative == "":
        html_path = SITE_DIR / "index.html"
    else:
        html_path = SITE_DIR / relative / "index.html"

    if not html_path.exists():
        continue

    # -----------------------------------------------------
    # Parse HTML
    # -----------------------------------------------------

    soup = BeautifulSoup(
        html_path.read_text(encoding="utf-8"),
        "lxml"
    )

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    title = soup.title.string.strip() if soup.title else "Untitled"

    # -----------------------------------------------------
    # Description
    # -----------------------------------------------------

    meta_desc = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    description = ""

    if meta_desc:
        description = meta_desc.get("content", "").strip()

    # -----------------------------------------------------
    # Main content
    # -----------------------------------------------------

    main = soup.find("main")

    content = ""

    if main:
        content = main.get_text(
            separator="\n",
            strip=True
        )

    # =====================================================
    # llms.txt entry
    # =====================================================

    llms_lines.append(
        f"- [{title}]({abs_url}): {description}\n"
    )

    # =====================================================
    # llms-full.txt entry
    # =====================================================

    full_lines.append(f"# {title}\n\n")
    full_lines.append(f"URL: {abs_url}\n\n")

    if description:
        full_lines.append(
            f"Description: {description}\n\n"
        )

    full_lines.append(content)
    full_lines.append("\n\n---\n\n")


# =========================================================
# Write outputs
# =========================================================

LLMS_TXT.write_text(
    "".join(llms_lines),
    encoding="utf-8"
)

LLMS_FULL_TXT.write_text(
    "".join(full_lines),
    encoding="utf-8"
)

print(f"Generated: {LLMS_TXT}")
print(f"Generated: {LLMS_FULL_TXT}")

