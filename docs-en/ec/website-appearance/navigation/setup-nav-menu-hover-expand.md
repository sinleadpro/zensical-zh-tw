---
title: "Expand Navigation Menus on Hover"
description: "Edit the template code so storefront navigation menus expand their second-level lists automatically on hover."
created: 2025-03-03 16:40
last_modified: 2026-06-30 11:01
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules:
  - 網站外觀
sites:
  - TW
audiences:
  - developer
difficulty: advanced
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 修改樣板程式碼以實現導覽選單自動展開
  - 提升網站導覽選單的使用者體驗
features:
  - 導覽選單自動展開
  - 程式碼修改
  - 網頁前端設定
prerequisites: []
related:
  - ec/website-appearance/code-customization/restore-code-theme-editor/
tags:
  - "Navigation Menu"
  - "Auto Expand"
  - Code
  - Liquid
  - CSS
  - "CSS/HTML Editor"
  - "Drag-and-Drop Themes"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 網站外觀 > 套版主題管理 > CSS/HTML 編輯器
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/support/?p=28145
permalink: "https://help.cyberbiz.io/ec/website-appearance/navigation/setup-nav-menu-hover-expand/"
comments: ""
search:
  exclude: false
icon: lucide/mouse-pointer-click
hide: 
---

![Navigation menu auto-expand](../../../assets/images/ec-網站外觀-樣板編輯器-main_nav-liquid.en.png){ title="Navigation Menu Auto-Expand" .hero-page }

## About Navigation Menu Auto-Expand { #intro-nav-hover }

If you want a link list (menu) to **expand its second-level items automatically** when shoppers hover over it, without clicking, you can edit the code in the template editor.

## Steps <small>Using a Drag-and-Drop Theme as an Example</small> { #operate-nav-hover }

!!! warning  "Editing template files is an advanced task. Back up a version before you make changes."

1. **Go to:** Sign in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting**.
2. **Open the editor:** On the theme you are using, click "Actions" and open the **CSS/HTML Editor**.
3. **Find the file:** In the search box at the top left of the editor, type **`main_nav.liquid`** and click the file to open it.
4. **Paste the code:** Paste the following code on **line 2** of the file:

	``` html title="main_nav.liquid" linenums="2"
	<style>
	  .dropdown:hover .dropdown-menu {
	    display: block;
	  }
	</style>
	```

5. **Save:** Click "**Save**," and then check the result on your storefront.

	![Menu auto-expand on the storefront](../../../assets/images/ec-網站外觀-樣板編輯器-選單自動展開-前台.en.png){ title="Menu Auto-Expand on the Storefront" }

## Notes and Recovery { #prerequisites-nav-hover }

- **Responsibility:** CYBERBIZ gives merchants open access to edit code for their own customization. However, CYBERBIZ **does not provide coding tutorials, editing guidance, or code-writing services beyond the existing documentation**. Have a professional engineer make these changes.
- **Recovery:** If the layout breaks or shifts after your changes, use the **View Previous Versions** button in the template editor to [roll back to an earlier version](../code-customization/restore-code-theme-editor.md#operate-restore-theme){ title="Restore a Template Editor Version" }.

## FAQ { #faq-nav-hover }

??? quote "Why does nothing happen after I set it up?"
	Check that the code is correctly wrapped in the `<style> ... </style>` tag. Also, if your theme uses custom CSS class names (not the standard `.dropdown`), ask an engineer to confirm the correct selector name.

??? quote "Will the expanded menu cover the banner below it?"
	Yes. When the drop-down menu expands, it overlays the content below. Keep your second-level menus at a moderate length so they do not cover a large area when shoppers hover over them, which can make the page hard to read.

??? quote "How do I adjust how fast the drop-down menu appears?"
	To make the expand motion smoother, add the `transition` property to the code, but this requires more advanced CSS knowledge. In general, keep `display: block;` to ensure an instant response.
