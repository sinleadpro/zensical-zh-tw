---
title: "Set up the Store Chat Widget"
description: "Learn how to add LINE and Facebook Messenger chat entry points to your online store and manage customer messages in one place with CHAT BOX."
created: 2026-06-25 10:10
last_modified: 2026-09-10 14:20
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - APP MARKET
sites: 
  - TW
  - MY
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: 
  - "CHAT BOX"
intents: 
  - 整合官網對話入口
  - 設定 LINE 對話按鈕
  - 設定 Messenger 對話按鈕
  - 集中管理顧客訊息
features: 
  - 官網整合對話入口
  - CHAT BOX
  - LINE 整合
  - Messenger 整合
prerequisites:
  - ec/app-market/chatbox/connect-chat-box-to-line-oa/
  - ec/app-market/chatbox/connect-chat-box-to-facebook-page/
related:
  - ec/app-market/chatbox/connect-chat-box-to-line-oa/
  - ec/app-market/chatbox/connect-chat-box-to-facebook-page/
tags: 
  - "Chat Entry Point"
  - CHAT BOX
  - LINE
  - Messenger
  - "Customer Service Integration"
  - Multi-Country
acoiv: configure
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 對話小工具
  - 外觀設定
  - 功能設定
paths:
  - APP MARKET > 我的擴充服務 > CHAT BOX
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/integrated-chat-widget/"
search:
  exclude: false
icon: lucide/message-square-plus
hide: []
---

# Set up the Store Chat Widget
Learn how to add LINE and Facebook Messenger chat entry points to your online store and manage customer messages in one place with CHAT BOX.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHAT BOX
{ .doc-badge }

!!! tip "Use Cases"
	- **Manage Messages in One Place**: When customers contact you from your store through LINE or Messenger, all messages go into CHAT BOX so nothing is missed.
	- **Turn More Inquiries into Sales**: Put a live contact option in a visible spot on your store to make it easier for customers to ask questions.
	- **Stay on Brand**: Customize the look and position of the chat button so the widget matches your brand style.


## Before You Start { #prerequisites-chat-widget }

- **Connect First**: Before you use this feature, connect your [**LINE Official Account**](connect-chat-box-to-line-oa/) or [**Facebook Page**](connect-chat-box-to-facebook-page/).
- **Account Status**: Only accounts with a working connection appear in the menu. If an account has a connection problem, check its binding status again.
- **Activation Requirement**: You must enable at least one chat channel (LINE or Messenger) before you can turn on the store chat entry master switch.


## Setup Steps { #operate-chat-widget }

### Step 1: Enable Chat Channels { #operate-chat-widget-step-enable }

Choose which contact tools to show on your store.

1. Log in to the CYBERBIZ admin and go to **APP MARKET > My Apps > CHAT BOX**.
2. Open **Store Chat Entry** and click the **Feature Settings** tab.
3. **LINE**: Select the account from the drop-down menu and switch the toggle to `開啟 (ON)`.
4. **Facebook Messenger**: Select the Page from the drop-down menu and switch the toggle to `開啟 (ON)`.

![](../../../assets/images/EC-後台-APPMARKET-chatbox-整合對話入口01.en.png){ .screenshot }

### Step 2: Customize the Appearance { #operate-chat-widget-step }

Adjust how the chat widget looks on your store.

1. Switch to the **Appearance Settings** tab.
2. **Title Text**:
    - **Main Title**: Enter the title shown at the top of the chat window (required).
    - **Subtitle**: Enter the greeting shown below the title (required).
3. **Colors**: Set the **Theme Color** and **Title Color**. We recommend using your brand colors.
4. **Button Tooltip Text**:

    - Under **Show Button Tooltip Text**, select **Yes** or **No**.
    - If you select **Yes**, enter the text to show next to the floating button in the **Button Tooltip Text** field, such as "Need help?".
    - When enabled, a tooltip bubble appears next to the floating chat button as customers browse your store. The bubble hides automatically when the customer opens the chat window, and customers can also click **✕** on the bubble to close it.

    ![](../../../assets/images/EC-後台-APPMARKET-chatbox-整合對話入口07.en.png){ .small-image }

5. **Button Position**:
    - Choose to show it in the **bottom-right** or **bottom-left** corner of the site.
    - Set the distance from the page edge for **Desktop** and **Mobile** separately (required).

![](../../../assets/images/EC-後台-APPMARKET-chatbox-整合對話入口02.en.png){ .screenshot }

### Step 3: Preview and Turn On { #operate-chat-widget-section }

Check your settings in the live preview and publish.

1. Use the **Live Preview** on the right side of the admin.
    - The preview updates after you save the appearance settings.
    - If no channel is turned on, the preview shows "No channels enabled yet".

    ![](../../../assets/images/EC-後台-APPMARKET-chatbox-整合對話入口03.en.png){ .screenshot }

2. When everything looks right, turn on **Enable Chat Entry** at the top of the page.

    ![](../../../assets/images/EC-後台-APPMARKET-chatbox-整合對話入口04.en.png){ .screenshot }

3. Click **Save**. The chat entry now appears on your store.

    ![](../../../assets/images/EC-後台-APPMARKET-chatbox-整合對話入口05.en.png){ .screenshot }

## Multilingual Settings { #operate-settings }

Set the multilingual names for the Bonus Mall so the storefront shows the right text for each language.

!!! warning "Notes"
	- To change the English text, **switch to English** first, then make your changes.
	- The storefront text changes with the language only for fields that show a **language tag**. For example: **Group Name** Bonus Mall `繁體中文`.
	- If a field is left blank for another language, the storefront shows the **Traditional Chinese** content by default for that language.

### Steps { #operate-settings-operate-step }

1. In the language menu, switch to the language you want to edit (for example, Traditional Chinese or English).
2. Click the title name field to edit it, then press ++enter++ to save your changes.



## Customer Experience { #intro-chat-widget }

When customers click the chat button on your store, the system opens the matching messaging app based on their device:

| Channel | Desktop | Mobile |
| :--- | :--- | :--- |
| **Facebook Messenger** | Opens Messenger on the web in a new tab | Opens the Messenger app and goes to the chat |
| **LINE** | Opens a new tab showing the LINE Official Account QR code | Opens the LINE app and goes to the chat |


