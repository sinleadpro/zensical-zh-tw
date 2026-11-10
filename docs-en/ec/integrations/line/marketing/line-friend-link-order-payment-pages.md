---
title: "Set up LINE Friend Links on Order Confirmation and Payment Completed Pages"
description: "Edit Liquid template files to add LINE friend link components at key conversion points after checkout and improve member return rates."
created: 2026-02-24 00:00
last_modified: 2026-07-08 19:11
lang: en-US
permalink: "https://help.cyberbiz.io/ec/integrations/line/marketing/line-friend-link-order-payment-pages/"
type: guide
author: Jase
reviewers: []
notes:
  - code block can be improved with code annotation.
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
  - 第三方整合
sites:
  - TW
tnb: branch
plans:
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - developer
difficulty: advanced
intents:
  - 設定訂單成立頁顯示 LINE 加入好友連結
  - 設定付款完成頁顯示 LINE 加入好友連結
features:
  - Liquid 樣板編輯
  - LINE 導流元件
  - 訂單完成頁客製化
prerequisites:
  - 客服申請開通
related:
  - ec/website-appearance/code-customization/restore-code-theme-editor/
tags:
  - LINE
  - "Order Completion"
  - "Conversion Rate"
  - "Traffic Referral"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 網站外觀 > 套版主題管理 > 選擇操作 > CSS/HTML編輯器
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10871
  - https://www.cyberbiz.io/support/?p=30333
comments: false
search:
  exclude: false
icon: lucide/party-popper
hide:
---

![Order page LINE friend link](../../../../assets/images/ec-網站外觀-order-done-extra-content-liquid.en.png){ .hero-page title="Order page LINE friend link" }

## Guide to Displaying the LINE Friend Link on Order-Related Pages { #overview-line-order-link }

Merchants can edit the code to add a LINE friend link or image to the **Order Confirmation Page** and the **Order Payment Completed Page** after a customer submits an order.

## Prerequisite: Request Activation { #prerequisites-line-order-link }

- [x] **Request from Customer Service:** This feature is not enabled by default. Go to the admin and request activation from **CYBERBIZ Customer Service**.
- [x] **Theme Restriction:** After activation, this feature applies only to themes that are **currently published**. If you switch to a new theme in the future, you must request activation again from Customer Support.
- [x] **Supported Themes:** This feature supports **drag-and-drop themes**.

## Admin Steps { #operate-line-order-link }

1. **Open the Editor:** Log in to the admin and go to **Website Appearance > Theme Setting**.
2. **Actions** On the theme you are currently using, click "**Actions** > ** CSS/HTML Editor**".
3. **Search for the File:** In the editor search bar, enter the file name: **`order_done_extra_content.liquid`**.

	![Search template file](../../../../assets/images/ec-網站外觀-樣板編輯器-order-done-extra-content-liquid.en.gif){ title="Search template file" }

4. **Edit the Code:** After you finish editing, click **Save** to apply your changes.
5. **Storefront Example:**

	![Storefront order page friend link](../../../../assets/images/ec-網站外觀-訂單頁顯示 line 加入好友-前台.en.png){ title="Order page friend link on storefront" }

## Coding Tips { #intro-line-order-link }

Merchant engineers must write their own HTML/CSS code to design the page. To show different content on different pages, use the following logic to check which page is displayed:

- **Example Code for Page Detection:**

	{% raw %}
	``` liquid
	{% if page_title == '訂單成立' %}
	   <!-- 這裡放置要在「訂單成立頁」顯示的內容（如好友連結、圖片） -->
	{% else %}
	   <!-- 這裡放置要在「付款完成頁」顯示的內容 -->
	{% endif %}
	```
	{% endraw %}

	_(Note: If you do not need to distinguish between pages, simply place the content directly.)_

	![Order and payment confirmation pages](../../../../assets/images/ec-網站外觀-樣板-order-done-extra-content-liquid-訂單成立頁-付款完成頁.en.png){ title="Order and Payment Confirmation Pages" }

- **Recovery:** If an issue occurs after you make changes, see [Restore Template Editor](../../../website-appearance/code-customization/restore-code-theme-editor.md){ title="Restore web code with the template editor" }  Restores the file to a previous version.

!!! warning "Notes"
	- **No Code Writing Services:** CYBERBIZ **does not provide syntax tutorials or code writing services**. Merchants must assign this work to their in-house engineers or an external design firm.
	- **Use at Your Own Risk:** Merchants are responsible for any system issues or errors caused by code changes, and must bear all related risks and consequences.

## FAQ { #faq-line-order-link }


??? quote "Why don't I see changes on the page after editing `order_done_extra_content.liquid`?"

	- **Clear the Cache:** Try opening an incognito window, or clear your browser cache and refresh the page.
	- **Check Your Plan and Permissions:** Confirm that your plan is **Expert PLUS** or **Enterprise**, and that you have contacted Customer Support to activate this feature.
	- **Check Your Theme Type:** This feature only supports drag-and-drop themes. If you use a traditional legacy theme (not drag-and-drop), this feature will not work properly."

??? quote "Will my settings be kept after I change the theme?"
	**No.** The code is stored in the specific theme file. If you change or reinstall a theme, you must repeat the steps above and copy the code into the matching file in the new theme.
