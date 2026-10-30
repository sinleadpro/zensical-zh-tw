---
title: "Text Editor Reference"
description: "A summary of the text editor's slash commands, YouTube video options, and image specifications for quick reference while editing content."
created: 2026-06-30 15:19
last_modified: 2026-07-02 16:02
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans: []
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related:
  - ec/website-appearance/code-customization/text-editor/
tags:
  - "Text Editor"
  - "Slash Commands"
  - YouTube
  - "Image Specifications"
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-appearance/references/text-editor-toolbar/"
comments: false
search:
  exclude: false
icon: lucide/table
hide: []
---

This page collects the reference tables for the text editor. Content-editing docs such as "[Text Editor](../code-customization/text-editor.md)" link to it.

### Slash Commands Reference { #reference-text-editor-slash-commands }

In the new text editor, type "/" in the body to open a shortcut menu, and type a keyword to filter it quickly.

| Command | Purpose |
| :-- | :-- |
| Body text | Changes the paragraph back to the normal body style |
| Heading 1 to Heading 6 | Applies a heading style at different levels |
| Table | Inserts a table. You can also type something like `3x4` to set the number of rows and columns |
| Numbered list | Inserts a numbered list |
| Bulleted list | Inserts an unnumbered bulleted list |
| Quote | Inserts a quote block |
| Horizontal line | Inserts a horizontal divider line |
| Image | Opens the image insert window |
| YouTube video | Opens the YouTube video embed window |
| Special characters | Inserts special characters such as arrows, currency, and math symbols |
| Emoji | Inserts emoji |

!!! note "Note"
    * This feature is only in the new text editor. In the legacy editor, use the matching buttons on the toolbar above.
    * After typing "/", keep typing (for example, the English word `table`) to quickly filter the command you want.

### YouTube Video Settings Reference { #reference-text-editor-youtube-options }

Options you can set when inserting a YouTube video:

| Option | Description |
| :-- | :-- |
| Paste YouTube video URL | The video source link. Only YouTube URLs are supported |
| Width / Height | The display size of the video (applies when responsive scaling is not selected) |
| Start time | Starts playback at a set time, in the format `ss`, `mm:ss`, or `hh:mm:ss` |
| Playlist ID | Fill in to embed a whole playlist |
| Use responsive scaling mode | Ignores the set width and height and scales automatically based on width, keeping the aspect ratio on phones and other devices |
| Autoplay | Plays automatically when the page opens (works only if "Mute" is also selected) |
| Loop | Replays the video automatically when it ends |
| Mute | Plays the video muted by default |
| Show player controls | Whether to show the play/pause control bar |
| Show suggested videos when the video ends | Whether to show YouTube's recommended videos after playback |
| Enable privacy-enhanced mode | Embeds the video in privacy-enhanced mode |

!!! note "Note"
    * Under YouTube's rules, "Autoplay" works only together with "Mute."
    * When you select "Responsive scaling," the fixed width and height are ignored and the video scales based on width.

### Image Specs Reference { #reference-text-editor-image-specs }

| Item | Spec |
| :-- | :-- |
| Supported formats | JPG, JPEG, PNG, GIF, TIFF, WebP |
| Maximum size | Width 5000px and height 7000px. Larger images cannot be uploaded |
| Automatic optimization | After upload, a version up to 1280px wide is generated automatically to speed up storefront loading |
| GIF handling | Kept as the original image without compression |
| Storage space | Limited by your plan's storage space. You cannot upload when the space is full |

!!! note "Note"
    * When an image exceeds the maximum size, the system shows "The maximum image width is 5000px and the maximum height is 7000px."
    * Tips for long product images: For a single long image, use a width of 1000px with any length. For multiple stitched images, make each one 1000px × 1000px.
