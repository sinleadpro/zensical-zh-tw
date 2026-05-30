import os

def define_env(env):
    """
    Hook for Zensical Macros to define variables and logic.
    """
    # =========================================================
    # Internal docs gate (environment variable)
    # ========================================================= 
    # 1. Grab the environment variable from your shell/Cloudflare
    # Defaulting to 'false' ensures your public build is always safe.
    raw_value = os.getenv('INTERNAL_DOCS', 'false').lower()
    
    # 2. Convert the string to a real Python Boolean
    is_internal = (raw_value == 'true')
    
    # 3. Register the variable for use in your Markdown files
    # This allows you to use {% if is_internal %}
    env.variables['is_internal'] = is_internal

    # 4. (Optional) Debugging: This prints in your terminal 
    # to confirm the gate status during 'uv run zensical serve'
    status_icon = "🔓" if is_internal else "🔒"
    print(f"--- Zensical Macro: Internal Gate is {status_icon} ({is_internal}) ---")

    # =========================================================
    # Metadata renderer (plans / extensions / function)
    # =========================================================

    @env.macro
    def badge(meta):

        parts = []
        # =====================================================
        # 1. Plans (tnb == branch)
        # =====================================================
        if meta.get("tnb") == "branch" and meta.get("plans"):
            plans_text = " ".join(meta["plans"])

            parts.append(
                f'[:lucide-tag:{{ title="適用方案" }}](../../../resources/conventions#適用方案) | {plans_text}  '
            )

        # =====================================================
        # 2. Extensions
        # =====================================================
        if meta.get("cyb_extensions"):
            ext_text = " ".join(meta["cyb_extensions"])

            parts.append(
                f'[:lucide-grid-2x2-plus:{{ title="適用擴充" }}](../../resources/conventions#適用擴充) | {ext_text}  '
            )

        # =====================================================
        # 3. Layout
        # =====================================================
        if meta.get("layouts"):
            layout_text = " ".join(meta["layouts"])

            parts.append(
                f'[:lucide-bolt:{{ title="適用功能" }}](../../resources/conventions#適用功能) | {layout_text}  '
            )

        # =====================================================
        # IMPORTANT: CSS wrapper class
        # =====================================================
        if parts:
            parts.append("{ .doc-badge }")

        return "\n".join(parts)

    # =========================================================
    # Subtitle renderer
    # =========================================================
    @env.macro
    def subtitle(description):

        if not description:
            return ""

        return f"{description}\n{{ .subtitle }}"


    # =========================================================
    # Git last update formatter
    # =========================================================
    @env.macro
    def last_update(date):
        try:
            return f"> 更新時間： {date.strftime('%Y-%m-%d')}"
        except:
            return ""

def on_post_build(config):

    # =========================================================
    # Output directory
    # =========================================================
    site_dir = config["site_dir"]

    # =========================================================
    # LLM.txt content
    # =========================================================
    lines = []

    lines.append("# CYBERBIZ DOCS\n")
    lines.append(
        "> 官方線上技術文件與操作指南，供 AI 程式助手與 LLM 快速理解系統架構。\n\n"
    )

    lines.append("## 技術文件地圖 (Documentation Map)\n\n")

    # =========================================================
    # Iterate all documentation pages
    # =========================================================
    for file in config["files"]:

        # Only markdown docs
        if not file.is_documentation_page():
            continue

        page = file.page

        if not page:
            continue

        # Skip homepage if desired
        if page.url == "":
            continue

        # -----------------------------------------------------
        # Metadata
        # -----------------------------------------------------
        meta = getattr(page, "meta", {}) or {}

        title = meta.get("title") or page.title or "CYBERBIZ 指南"

        desc = meta.get(
            "description",
            "官方線上技術文件與操作指南"
        )

        clean_desc = str(desc).replace("\n", " ").strip()

        abs_url = f"https://help.cyberbiz.io/{page.url}"

        lines.append(
            f"- [{title}]({abs_url}): {clean_desc}\n"
        )

    # =========================================================
    # Write llm.txt
    # =========================================================
    output_path = os.path.join(site_dir, "llm.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("INFO - [LLM] Generated llm.txt")

