import os
from pathlib import PurePosixPath

from jinja2 import pass_context

# Same labels as overrides/partials/content.html.
# updated_at belongs to the last_update() macro; the page footer uses updated.
BADGE_COPY = {
    "zh-TW": {
        "plans": "適用方案",
        "extensions": "適用擴充",
        "features": "適用功能",
        "themes": "適用版型",
        "all_plans": "全版本",
        "standard": "標配",
        "optional": "選配",
        "plan_options": "標配／選配",
        "draggable": "拖拉版型",
        "classic": "預設版型",
        "updated_at": "更新時間：",
    },
    "en": {
        "plans": "Applicable plans",
        "extensions": "Applicable extensions",
        "features": "Applicable features",
        "themes": "Applicable themes",
        "all_plans": "All plans",
        "standard": "Standard",
        "optional": "Optional",
        "plan_options": "Standard / Optional",
        "draggable": "Drag-and-drop theme",
        "classic": "Default theme",
        "updated_at": "Updated:",
    },
}

BADGE_ANCHORS = {
    "plans": "conventions-plans",
    "extensions": "conventions-extensions",
    "features": "conventions-features",
    "themes": "conventions-themes",
    "plan_options": "conventions-plan-options",
}

BADGE_ICONS = {
    "plans": "lucide-tag",
    "extensions": "lucide-grid-2x2-plus",
    "features": "lucide-bolt",
    "themes": "lucide-layout-dashboard",
    "plan_options": "lucide-puzzle",
}


def badge_language(config):
    theme = config.get("theme") if isinstance(config, dict) else None
    lang = theme.get("language") if isinstance(theme, dict) else None
    if lang in BADGE_COPY:
        return lang
    return "zh-TW"


def conventions_target(page_path, anchor):
    """Link relative to the source file. The links extension adds one more
    '../' for non-index pages when directory URLs are on."""
    normalized = (page_path or "").replace("\\", "/")
    parent = PurePosixPath(normalized).parent if normalized else PurePosixPath(".")
    ups = 0 if parent.as_posix() in ("", ".") else len(parent.parts)
    prefix = "../" * ups
    return f"{prefix}resources/conventions.md#{anchor}"


def _badge_mark(icon, title, href):
    body = f':{icon}:{{ title="{title}" }}'
    if not href:
        return body
    return f"[{body}]({href})"


def _join_values(values, mapping=None):
    labels = []
    for value in values:
        if mapping and value in mapping:
            labels.append(mapping[value])
        else:
            labels.append(str(value))
    return " / ".join(labels)


def render_badge(meta, language, page_path):
    if not isinstance(meta, dict):
        meta = {}
    text = BADGE_COPY.get(language) or BADGE_COPY["zh-TW"]
    link = language == "zh-TW"

    def href(key):
        if not link:
            return ""
        return conventions_target(page_path, BADGE_ANCHORS[key])

    parts = []
    if meta.get("tnb") == "trunk":
        parts.append(
            f'{_badge_mark(BADGE_ICONS["plans"], text["plans"], href("plans"))} | {text["all_plans"]}  '
        )
    elif meta.get("tnb") == "branch" and meta.get("plans"):
        plans_text = _join_values(meta["plans"])
        parts.append(
            f'{_badge_mark(BADGE_ICONS["plans"], text["plans"], href("plans"))} | {plans_text}  '
        )

    if meta.get("cyb_extensions"):
        ext_text = _join_values(meta["cyb_extensions"])
        parts.append(
            f'{_badge_mark(BADGE_ICONS["extensions"], text["extensions"], href("extensions"))} | {ext_text}  '
        )

    if meta.get("feature_badges"):
        fb_text = _join_values(meta["feature_badges"])
        parts.append(
            f'{_badge_mark(BADGE_ICONS["features"], text["features"], href("features"))} | {fb_text}  '
        )

    if meta.get("layouts"):
        layout_text = _join_values(
            meta["layouts"],
            {"draggable": text["draggable"], "classic": text["classic"]},
        )
        parts.append(
            f'{_badge_mark(BADGE_ICONS["themes"], text["themes"], href("themes"))} | {layout_text}  '
        )

    if meta.get("plan_options"):
        labels = []
        for value in meta["plan_options"]:
            if value == "standard":
                labels.append(text["standard"])
            elif value == "optional":
                labels.append(text["optional"])
        if labels:
            po_text = " / ".join(labels)
            po_md = (
                f'{_badge_mark(BADGE_ICONS["plan_options"], text["plan_options"], href("plan_options"))} | {po_text}  '
            )
            if parts:
                parts[-1] = parts[-1].rstrip() + "  " + po_md
            else:
                parts.append(po_md)

    if parts:
        parts.append("{ .doc-badge }")

    return "\n".join(parts)


def render_last_update(date, language):
    text = (BADGE_COPY.get(language) or BADGE_COPY["zh-TW"])["updated_at"]
    try:
        return f"> {text} {date.strftime('%Y-%m-%d')}"
    except Exception:
        return ""


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
    # to confirm the gate status during 'uv run zensical serve'.
    # ASCII only: Windows cp950 cannot encode lock emojis and 0.0.62+
    # surfaces that UnicodeEncodeError as a fatal Python error.
    status = "open" if is_internal else "closed"
    print(f"--- Zensical Macro: Internal Gate is {status} ({is_internal}) ---")

    # =========================================================
    # Metadata renderer (plans / extensions / function)
    # =========================================================

    @env.macro
    @pass_context
    def badge(context, meta):
        config = context.get("config") if context is not None else env.conf
        page = context.get("page") if context is not None else None
        page_path = getattr(page, "path", "") or ""
        return render_badge(meta, badge_language(config), page_path)

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
    @pass_context
    def last_update(context, date):
        config = context.get("config") if context is not None else env.conf
        return render_last_update(date, badge_language(config))

