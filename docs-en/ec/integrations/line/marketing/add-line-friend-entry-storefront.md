---
title: "Add LINE Friend Entry to Storefront"
description: "Add a LINE Official Account add-friend entry to your drag-and-drop template site, guiding visitors to add you as a friend through pop-ups, carousels, the footer, or the navigation menu."
created: 2026-02-24 00:00
last_modified: 2026-06-26 10:05
lang: en-US
permalink: "https://help.cyberbiz.io/ec/integrations/line/marketing/add-line-friend-entry-storefront/"
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
sites:
  - TW
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 在官網新增 LINE 加入好友入口
  - 提升品牌與 LINE 官方帳號會員黏著度
features:
  - 彈窗廣告
  - 輪播素材 (Banner)
  - 頁腳 ICON 設定
  - 選單導覽列設定
prerequisites:
  - 取得 LINE 官方帳號加入好友連結與素材
related:
  - ec/notifications/send-line-friend-invitation/
  - ec/website-appearance/theme-and-layout/setup-theme-page-settings/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/website-appearance/theme-and-layout/theme-editor/
tags:
  - LINE
  - "Add Friend"
  - "Traffic Referral"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 彈窗
  - 輪播
  - 頁腳
  - 導覽列
paths:
  - 網站外觀 > 套版主題管理 > 網站設定
  - 網站外觀 > 選單/導覽列設定
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7435
  - https://www.cyberbiz.io/support/?p=38439
comments: false
search:
  exclude: false
icon: lucide/external-link
hide: 
---

![LINE Official Account add-friend tool](../../../../assets/images/ec-第三方整合-line-官方加入好友工具.en.png){ .hero-page title="LINE Official Account add-friend tool" }

## Add-Friend Tool Guide for Drag-and-Drop Templates

Merchants can use several built-in features to display LINE OA invitation information (such as links, QR codes, and images) on the storefront, improving brand loyalty and member engagement.

The following guide explains how to set up the LINE OA add-friend tool for drag-and-drop templates:

## Prerequisites: Get the LINE Friend Link

Before you start, get the LINE Official Account add-friend link and promotional materials.

- [x] Make sure you have set up the LINE OA account for your brand storefront.
- [x] Before you set up the storefront, go to **LINE Official Account Manager** to get promotional materials:

	1. Log in to [**LINE Official Account Manager** :lucide-external-link:](https://manager.line.biz), and go to **Home > Increase Friends > Add Friend Tools**.
	2. Here, you can copy **URL**, download the **QR Code**, or copy the syntax for the **Add Friend Button**.

## Storefront Setup Methods

### Right-Side Pop-up Ad <small>Pop-up Window</small>

This is the most direct way to guide customers to add you as a friend.

- **Admin Path**: Go to **Website Appearance > Theme Setting > Detail Settings > Pop-up Ad**.
- **Setup Steps**:
    1. Add an image block.

		![Pop-up Ad - Add Image](../../../../assets/images/ec-網站外觀-彈窗廣告-圖片.en.gif){ title="Pop-up Ad - Add Image" }

    2. **Upload image**: We recommend uploading the Add Friend QR Code image in the desktop, tablet, and mobile image fields, or pasting a URL link.

		![Pop-up Ad - Upload QR Code](../../../../assets/images/ec-網站外觀-彈窗廣告-圖片-line-oa-qrcode.en.gif){ title="Pop-up Ad - Upload QR Code" }

    3. **Thumbnail Setting**: Merchants can create their own thumbnails and resize them to fit the storefront display.
    4. **Image Link**: Select External Link, and paste the [Friend URL copied from LINE Official Account Manager](../../../notifications/send-line-friend-invitation.md#get-line-oa-add-friend-link){ title="Send LINE add-friend invitation" }.

		![Pop-up Ad - Image Link](../../../../assets/images/ec-網站外觀-彈窗廣告-圖片連結.en.png){ title="Pop-up Ad - Image Link" }

    5. **Save Settings**.

- **Completed Setup Screen**:

	![Pop-up Ad - Add Friend Completed](../../../../assets/images/ec-網站外觀-彈窗廣告-line 加入好友.en.gif){ title="Pop-up Ad - Add Friend Completed" }

---

### Carousel Assets <small>Banner</small>

Use large homepage banner ads for visual promotion.

- **Admin path**: Go to **Website Appearance > Theme Management > Detail Settings** >**Carousel Assets**.
- **Setup Steps**:
    1. Click **Add Block** and then click Edit.
    2. **Upload image**: Upload your designed LINE promotional image (the desktop image is required).
    3. **SEO Optimization**: Be sure to fill in the **Image Alt Text** to improve search engine performance.
    4. **Display Duration**: In **Other Layout Settings**, you can [adjust the asset display seconds and margins](../../../website-appearance/theme-and-layout/setup-theme-page-settings.md#section-main-slider){ title="Page Settings Guide" }.

	![Carousel Asset - Add](../../../../assets/images/ec-網站外觀-輪播素材-新增.en.gif){ title="Carousel Asset - Add" }

- **Completed Setup Screen**:

	![Carousel Asset - Storefront View](../../../../assets/images/ec-網站外觀-輪播素材-前台畫面.en.gif){ title="Carousel Asset - Storefront View" }

!!! note "For more carousel asset settings, see [Carousel Asset Settings](../../../website-appearance/theme-and-layout/setup-theme-page-settings.md#section-main-slider){ title="Page Settings Guide" }."

---

### Footer ICON Settings <small>Footer</small>

Display the LINE social icon fixed at the bottom of your website.

- **Admin path**: Go to **Website Appearance > Theme Management > Detail Settings** >**Footer**.
- **Setup Steps**:
    1. Click **Other Layout Design**.
    2. Find **Social Media Settings**, turn on **LINE**, and paste the friend invitation link.

![Footer LINE Settings](../../../../assets/images/ec-網站外觀-頁腳-line.en.gif){ title="Footer LINE Settings" }

---

### Menu / Navigation Bar Settings

Add the add-friend feature directly to the main menu of your website.

- **Admin path**: Go to Website Appearance > **Menu / Navigation Bar Settings**.
- **Setup Steps**:
    1. Go to [LINE Official Account Manager :lucide-external-link:](https://manager.line.biz/) and copy the syntax for **Create Button**.

		![LINE OA Create Button](../../../../assets/images/ec-第三方整合-line-oa-建立按鈕.en.gif){ title="LINE OA Create Button" }

    2. In the CYBERBIZ menu settings, click the menu you want to configure to open its edit page, then click **Add Link**.
    3. **Add Menu Item**: Paste the button syntax you copied earlier.
    4. **Link Item**: Select **External Link**, and paste the [copied Friend URL](../../../notifications/send-line-friend-invitation.md#get-line-oa-add-friend-link){ title="Send LINE add-friend invitation" }.

		![Menu Navigation Bar - Add Friend](../../../../assets/images/ec-網站外觀-選單導覽列-line-加入好友.en.gif){ title="Menu Navigation Bar - Add Friend" }

    5. After you save the menu, the add-friend image link appears in the storefront navigation bar.

		![Menu Navigation Bar - Add Friend Storefront](../../../../assets/images/ec-網站外觀-選單導覽列-line-加入好友-前台.en.png){ title="Menu Navigation Bar - Add Friend Storefront" }

!!! note "For more menu and navigation bar settings, see [Menu / Navigation Bar Settings](../../../website-appearance/navigation/setup-menus-navigation.md){ title="Set Up Menu and Navigation Bar" }  ."

---

## Related Actions

<div class="grid cards" markdown>

- :lucide-grip-vertical:{ .lg }   
  [__Drag-and-Drop Template Settings__](../../../website-appearance/theme-and-layout/theme-editor.md){ title="Drag-and-Drop Template Site Settings" }  
  Detailed features and setup instructions for drag-and-drop templates.

</div>

---

## Frequently Asked Questions

??? quote "Why does the icon look wrong on the storefront after I paste the button syntax into Menu / Navigation Bar?"

	Storefront display issues are usually caused by incomplete copied content. Follow these steps to troubleshoot:

	1. **Confirm Complete Copy**: Be sure to click the **Copy** button in the LINE back end, and avoid selecting text manually (manual selection can easily miss key HTML tags).
	2. **Do not modify the code**: Paste the original syntax directly. **Do not manually delete** any symbols or spaces.
	3. **Remove Leading and Trailing Spaces**: After pasting, check that there are no extra spaces or line breaks before or after the text in the input box.

??? quote "Will the LINE app open directly when mobile users click the Add Friend link?"
	Yes. If users click the link in a mobile browser, the system automatically detects it and triggers a **Deep Link** to open the LINE app and go to the Add Friend page. If users click the link on a desktop, they are guided to scan the QR Code or log in to the LINE web version.

??? quote "If I change my LINE OA account, will the storefront links update automatically?"
	**No.** The LINE friend invitation link is bound to a specific account ID. If you change your official account, you must manually go back to Pop-up Ad, Carousel Assets, Footer, and Menu, and replace each with the new invitation link and QR Code image.
