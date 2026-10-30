---
title: "Disable Right-Click to Protect Images and Text"
description: "Add CSS and JavaScript restrictions to your theme files to disable the right-click menu and text selection, reducing the risk of your images and text being copied or downloaded."
created: 2025-03-03 00:00
last_modified: 2026-07-06 09:13
lang: en-US
permalink: "https://help.cyberbiz.io/ec/website-appearance/site-settings/setup-right-click-protection/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
  - 行銷活動
sites: []
audiences:
  - developer
difficulty: advanced
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 防止網站圖片被另存下載
  - 禁止網頁文字被反白複製
  - 保護原創圖文版權
  - 設定 Windows 與 iOS 裝置鎖右鍵
  - 開啟一頁式商店防盜功能
  - 停用瀏覽器右鍵選單
features:
prerequisites: []
related:
  - ec/website-appearance/code-customization/restore-code-theme-editor/
tags:
  - "Copyright Protection"
  - CSS
  - JavaScript
  - "One-Page Store"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 一頁式商店
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3561
  - https://www.cyberbiz.io/support/?p=17072
comments: false
search:
  exclude: false
icon: lucide/lock
hide:
---

![Right-click protection settings](../../../assets/images/ec-網站外觀-樣板編輯器-theme-liquid.en.png){ title="Right-Click Protection Settings" .hero-page }

## About Right-Click Protection { #intro-right-click }

**"Right-click protection"** stops customers from downloading images or copying text from your web pages, protecting the originality of your images and copy.

How you set it up depends on your theme (default theme or drag-and-drop theme) and the page type (regular website or one-page store):

## Set Up a Default Theme <small>Standard Theme</small> { #operate-right-click-default }

For Windows/Android and iOS, add specific code in the code editor separately:

=== "Windows/Android"

	- **Admin path**: Go to **Website Appearance > Theme Setting > CSS/HTML Editor** > search for and open the "**theme.liquid**" file.
	- **Steps**:
	    1. Search the file for the `<body` tag.
	    2. Paste the following code after that tag (for example, after `column;"`):
	       ``` liquid
	       `ondragstart="return false" onselectstart="return false" onContextMenu="return false"`。
	       ```
	    3. When you finish, click Save.

			``` liquid title="theme.liquid" hl_lines="7"
			{{ content_for_header }}
		
		    {% section 'color_settings' %}
		
			  </head>
		
			  <body style="display: flex; flex-direction: column;" ondragstart="return false" onselectstart="return false" oncontextmenu="return false" class="{% if is_app %} is_app {% endif %}">
		    <!-- Navigation -->
		    {% section 'navbar' %}
		
		    <!-- template -->
		    <div id="template" style="flex:1 0 auto; background-color: var(--theme_bg);">
		      {{ content_for_layout }}
		    </div>
			```

    !!! note "What the Code Does"
    
        |**Attribute**|**Description**|
        |---|---|
        |**`ondragstart="return false"`**|**Disable dragging**: Stops users from moving text or images by clicking and dragging (often used to stop images from being dragged straight to the desktop).|
        |**`onselectstart="return false"`**|**Disable selection**: Stops users from highlighting or selecting text on the page.|
        |**`oncontextmenu="return false"`**|**Disable the right-click menu**: Turns off the right mouse button so users cannot open the menu to "Save image as" or "View page source."|

=== "iOS"

	- **Admin path**: Go to **Website Appearance > Theme Setting > CSS/HTML Editor** > search for and open the "**theme.liquid**" file.
	- **Steps**:
	
	    1. Paste the following CSS below `<head>`:
	        
	        ``` css title="theme.liquid"
			<style>	        
				*{
				    -webkit-touch-callout:none; /* Disable the system default menu */
			        -webkit-user-select:none; /* WebKit browsers */
			        -khtml-user-select:none; /* Older browsers */
			        -moz-user-select:none; /* Firefox */
			        -ms-user-select:none; /* IE10 */
			        user-select:none;
		        }
		        input, textarea {
			        -webkit-user-select:auto;
			        margin: 0px; padding: 0px; outline: none;
		        }
		    </style>
	        ```
	        
	    1. When you finish, click Save.

			``` liquid hl_lines="4-17" title="theme.liquid"
			<!DOCTYPE html>
			<html lang="zh-tw" style="height:100%;">
			    <head>
			        <style>	        
			            *{
			                -webkit-touch-callout:none; /* Disable the system default menu */
			                -webkit-user-select:none; /* WebKit browsers */
			                -khtml-user-select:none; /* Older browsers */
			                -moz-user-select:none; /* Firefox */
			                -ms-user-select:none; /* IE10 */
			                user-select:none;
			            }
			            input, textarea {
			                -webkit-user-select:auto;
			                margin: 0px; padding: 0px; outline: none;
			            }
			        </style>
			```

---

## Set Up a Drag-and-Drop Theme { #operate-right-click-drag }

With a drag-and-drop theme, you don't need to edit code. Just turn it on with a toggle in the admin.

- **Admin path**: Go to **Website Appearance > Theme Setting > Theme Setting > Global Settings**.
- **Steps**: In "Global Settings," find the **Right-Click Protection** option and turn it on.

![Right-click protection in a drag-and-drop theme](../../../assets/images/ec-網站外觀-全站設定-網頁鎖右鍵.en.gif){ title="Right-Click Protection in a Drag-and-Drop Theme" }

---

## Right-Click Protection on One-Page Store Pages { #operate-right-click-onepage }

To disable right-click on a specific "one-page store" campaign page, paste the following code based on the interface version:

- **Code**:
    
    ```` html
	<style type="text/css">
	  *:not(input):not(textarea) {
	    -webkit-touch-callout: none;
	    -webkit-user-select: none;
	    -khtml-user-select: none;
	    -moz-user-select: none;
	    -ms-user-select: none;
	    user-select: none;
	  }
	</style>

	<script>
	  (function () {
	    function stopEvent(event) {
	      event.preventDefault();
	      event.stopPropagation();
	    }
	
	    ['dragstart', 'selectstart', 'contextmenu'].forEach(function (event) {
	      document.addEventListener(event, stopEvent);
	    });
	  })();
	</script>
    
    ````
    
- **Where to put it**:

    === "New Version (Drag-and-Drop Interface)"
    
	    1. Sign in to the CYBERBIZ admin, go to **Marketing > Event Page**, and select the one-page campaign page you want to edit.
	    2. In the campaign page's **Layout Settings**, add a **Custom HTML** block, click Edit, and paste the code.
	    3. Click **Save** to apply the changes.
	    
		![One-page store right-click protection (new version)](../../../assets/images/ec-行銷活動-拖拉版型一頁式商店-網頁鎖右鍵.en.gif){ title="One-Page Store Right-Click Protection (New Version)" }

    === "Legacy Interface"
    
	    1. Sign in to the CYBERBIZ admin, go to **Marketing > Event Page**, and select the one-page campaign page you want to edit.
	    2. Click **Sales Content Settings > Insert Text Editor**, click **Source Code** in the editor, and paste the code.
	    3. Click **Save** to apply the changes.

		![One-page store right-click protection (legacy)](../../../assets/images/ec-行銷活動-舊版一頁式商店-網頁鎖右鍵.en.gif){ title="One-Page Store Right-Click Protection (Legacy)" }

---

## Important Notes { #prerequisites-right-click }

- **Responsibility**: CYBERBIZ gives you open access to edit code, but **CYBERBIZ does not provide coding tutorials or code-writing services beyond the existing documentation**. Hire your own engineer for this work.
- **Recovery**: Before you edit code, note that if the layout breaks, you can use **View Previous Versions** in the editor to [roll back to an earlier version](../code-customization/restore-code-theme-editor.md#operate-restore-theme){ title="Restore Web Page Code with the Template Editor" data-preview }.
- **Theme limitation**: Some features support only certain themes. For example, the "Shopping Instructions and Notes" feature does not work with drag-and-drop themes.

## FAQ { #faq-right-click }

??? quote "Why can content still be copied in some browsers or on some devices after I turn on right-click protection?"
	Right-click protection works mainly through JavaScript and CSS, which are "front-end restrictions." If a user deliberately turns off JavaScript in the browser or uses developer tools (F12), they may still get around it. This feature mainly prevents accidental clicks and simple downloads by ordinary users. It cannot block 100% of technical attempts.

??? quote "Does right-click protection affect how search engines (SEO) crawl my website?"
	**No.** Crawlers from Google and other search engines read the HTML source returned by the server directly. They are not affected by CSS or JavaScript interaction limits, so your search ranking is not affected.

??? quote "Can customers still fill in the contact form or search for products after I turn this on?"
	Yes. The code in this article excludes `input` (input boxes) and `textarea` (text areas) (`user-select: auto`), so customers can still type and select text when filling in shipping information, using the search box, or signing in as members.

??? quote "What should I do if my website layout breaks or the page goes blank while I'm doing this?"
	Don't panic. Use **"View Previous Versions"** at the top of the CSS/HTML Editor and restore a point in time before your change. If you can't access the admin, contact your dedicated store consultant or CYBERBIZ customer support right away.
