# Agent Guidelines for zensical-zh-tw

This repository contains the source code and documentation for the CYBERBIZ Documentation Center (Traditional Chinese). It uses **Zensical**, a modern static site generator built on top of MkDocs and Material for MkDocs.

## 🛠 Build & Development

The project is managed using `uv`.

- **Serve local preview:** `uv run zensical serve` (Use this for live preview while editing)
- **Build site:** `uv run zensical build` (Only run when you need to verify the final result)

There are no separate unit tests for this documentation-only repository.

## 📝 Code Style & Conventions

### 1. Language & Naming
- **Primary Language:** Traditional Chinese (`zh-TW`).
- **File Names:** Use descriptive Chinese names for documentation files (e.g., `文字編輯器使用教學.md`).
- **Slugs (Permalink):** Use meaningful English slugs or descriptive paths in the frontmatter `permalink` field.

### 2. Frontmatter Schema
Every Markdown file **must** include frontmatter. Refer to `reference/frontmatter-skill-reference.md` for the full schema. Core fields include:
- `title`: H1/SEO Title (Required).
- `description`: Meta description (Max 160 chars).
- `created`: `YYYY-MM-DD HH:mm` (Do not change after creation).
- `last_modified`: `YYYY-MM-DD HH:mm` (Update on every edit).
- `type`: `tutorial`, `guide`, `reference`, `concept`.
- `products`: Array (e.g., `["EC"]`, `["POS"]`, `["WMS"]`).

### 3. Markdown Formatting
- **Headings:**
    - `# Title` (H1) should only appear once via the `title` frontmatter or the first line.
    - `## Section` (H2) for major sections (automatically gets a border-bottom).
    - `### Subsection` (H3) for nested topics.
    - `#### Sub-subsection` (H4) for detailed steps or phases.
- **Complex Steps Format Priority:**
    - **Use subheadings (####) first:** When steps have multiple phases, use `###` for main heading and `####` for each phase. This allows users to scan the table of contents and jump to specific stages.
    - **Use tabs only when needed (inside subheadings):** Only use tabs when each subheading's content is complex (3+ sub-steps) or users need to frequently switch between variants.
    - **Never skip heading levels:** Do not go from `##` directly to `####`, or from `###` directly to `=== tabs` (without `####`). Always maintain proper heading hierarchy.
    - **If unsure:** Prompt user with options to choose:
      - A) Subheadings (####)
      - B) Tabs (===)
      - C) Subheadings + Tabs
- **Icons:** Use Lucide icons via the `:lucide-<icon-name>:` syntax (e.g., `:lucide-rocket:`, `:lucide-settings:`).
- **Admonitions:** Use standard MkDocs admonitions: `!!! note`, `!!! info`, `!!! warning`, etc.
- **Tabs:** Use content tabs: `=== "Label"`.
- **Grid Layouts:** Use `<div class="grid cards" markdown>` for dashboard-style layouts.

### 4. Media & Assets
- **Screenshots:**
    - Apply the `.screenshot` class to images: `![Alt text](image.png){ .screenshot }`.
    - Images placed in folders named `images` get automatic rounded corners and shadows via CSS.
- **Storage:** Place images in local `assets/` or `images/` directories relative to the doc.

### 5. Navigation
- Navigation is defined in `zensical.toml` under the `nav` key. 
- When adding a new page, you **must** update `zensical.toml` to include it in the sidebar.

## 🗂 Project Structure
- `docs/`: Markdown source files.
- `zensical.toml`: Main configuration (Global settings, Navigation).
- `zensical.en.toml`: English localization overrides.
- `overrides/`: Custom Jinja2 templates.
- `reference/`: Internal guidelines and playbooks (e.g., `doc types.md`, `frontmatter-skill-reference.md`).
- `includes/`: Reusable snippets and abbreviations.

## 🤖 Rules for Agents
- **Consistency:** Always check `zensical.toml` before creating new paths to ensure they fit the information architecture.
- **Frontmatter:** Never omit the frontmatter. Ensure `last_modified` is updated.
- **Internal Links:** Use relative paths for internal links (e.g., `[Link](path/to/file.md)`) to enable `mkdocs-autorefs` validation.
- **Terminology:** Adhere to CYBERBIZ official terminology (e.g., 品牌官網, 智慧倉儲, 智能 POS).
