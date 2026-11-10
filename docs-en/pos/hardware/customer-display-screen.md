---
title: "Customer Display Screen"
description: "The POS customer display is an auxiliary device that lets customers view purchase details, transaction amounts, and brand advertising in real time at checkout."
created: 2026-03-25 15:30
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：訂單加價購
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有 POS 商店
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 如何設定 POS 客顯螢幕
  - POS 廣告牆設定教學
  - POS 加價購如何顯示在客顯
  - 解決客顯影片無法播放問題
features:
  - POS 客戶顯示器
  - 廣告牆
  - 互動遊戲
  - 結帳加價購
  - 顧客資訊確認
prerequisites: []
related:
  - pos/software/drivers/
  - pos/check/customer-display-interactive-games/
  - ec/marketing/upsells/setup-order-upsell/
tags:
  - "POS Customer Display"
  - "Digital Signage"
  - "YouTube Copyright Exclusion"
  - "Store Marketing"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 客顯行銷
  - 廣告牆設定
  - 同步客顯設定
  - 客顯行銷設定
paths:
  - POS 功能 > 所有 POS 商店 > 選擇 POS 商店 > 客顯行銷頁籤
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=5578
permalink: "https://help.cyberbiz.io/pos/hardware/customer-display-screen/"
comments: false
search:
  exclude: false
icon: lucide/monitor-play
hide: []
---

# Customer Display Screen
The POS customer display is an auxiliary device for the POS system. It lets customers view their itemized purchases, transaction totals, and brand advertisements in real time during checkout.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Brand promotion**: Play brand image videos or the latest promotional images on the checkout screen to turn the customer display into digital signage.
    - **Boost spending**: Show add-on purchase offers at checkout to prompt additional purchases just before the customer pays, raising AOV.
    - **Interactive fun**: Use interactive games (such as spin wheels or prize draws) to make checkout more enjoyable and increase member loyalty.
    - **Information confirmation**: Guide customers to verify their member details and itemized purchases, reducing manual communication errors.


## Before You Start { #prerequisites-display-screen }

- **Hardware requirements**: Prepare an external monitor and connect it to the POS host (we recommend setting the projection mode to **Extend**).
- **Software requirements**: Install the [POS APP Driver](../software/drivers.md) on the POS host, and open the POS APP.
- **How changes take effect**: After you configure settings in the admin, run **Sync Customer Display Settings** in the POS front end to update the display content.
- **Video requirements**: Ad wall videos support YouTube URLs only. If a video contains copyrighted music, the customer display may fail to play it.


## Operation Steps { #operate-display-screen }

### Step 1: Set up Customer Display Marketing Content in the Admin { #operate-display-screen-step-a-admin }

1. Log in to the CYBERBIZ admin, go to **POS > POS Store List**, select the store you want to configure, and click **Customer Display Marketing**.
    ![](../../assets/images/POS-後台-所有POS商店-客顯行銷-開啟設定01.en.png){ .screenshot }
2. On the page, select the **POS Terminal** you want to apply the settings to.
3. Turn on the **Customer Display Settings** toggle, and select the information to display:
    - **Add Buy**: When turned on, the system automatically applies the existing **Order Add-on Purchase** campaign. If the conditions are met, an add-on purchase dialog appears before checkout.
    - **Ad Wall**: When turned on, you can set the ad layout and content below.
    - **Customer Display Game**: Select one of the existing interactive games to display.
4. To have customers confirm their member information, turn on the information confirmation toggle in **Other Settings**.
    ![](../../assets/images/POS-後台-所有POS商店-客顯行銷-開啟設定02.en.png){ .screenshot }

!!! info "Default Customer Display Screen Content"
    Whether or not marketing settings are turned on, the right side of the customer display screen shows the following in real time by default:

    - **Itemized purchases**: Product name, quantity, and subtotal.
    - **Transaction details**: Discount breakdown and checkout total.
    - **Carrier information**: Shows the carrier number provided by the customer.



### Step 2: Set up the Ad Wall Layout and Content { #operate-display-screen-step-b-settings }

In the **Ad wall settings** section on the same page, you can customize the visual content to display. The ad wall appears in the **left** column of the POS checkout screen.

1. **Select a Layout**: The system provides 3 layouts to choose from.
    - **Layout 1**: Images only.
    - **Layouts 2 and 3**: Combination of images and videos.
2. **Upload Assets**:
    - **Image**: Upload assets in JPG or PNG format.
    - **Video**: Paste a YouTube video URL (YouTube only).

![](../../assets/images/POS-後台-所有POS商店-客顯行銷-開啟設定03.en.png){ .screenshot }

!!! warning "Troubleshooting Video Playback"
    If "Unable to Play Video" appears on the customer display, the YouTube video usually contains copyrighted music. Go to YouTube Studio to replace the background music or mute that segment, or refer to the [YouTube Official Guide](https://support.google.com/youtube/answer/2902117) to remove the copyright claim.

    ![](../../assets/images/POS-前台-客顯螢幕-無法播放YouTube影片01.en.png){ .small-image }


### Step 3: Connect and Sync the POS Front End { #operate-display-screen-step-c-pos }

After you finish the back-office setup, complete the final connection steps on the POS terminal.

1. Make sure the POS host has downloaded and is running the [POS APP Driver](../software/drivers.md), then click **Open Front End**.
2. Enter the POS front end, and click **Others > Settings and Connection Test**.
3. In the **Switch POS Terminal** field, confirm that the correct terminal is selected.
4. Find the **Sync Customer Display Settings** field, and click **Sync**.
5. Confirm that the external monitor is set to **Extend** projection mode. The display will then appear correctly.

![](../../assets/images/POS-前台-其他功能-同步客顯螢幕裝置01.en.png){ .screenshot }

## Customer Display Screen Preview { #intro-display-screen }

=== "Add-on Purchase"

    ![](../../assets/images/POS-前台-客顯螢幕-加價購01.en.png){ .medium-image }

=== "Ad Wall"

    ![](../../assets/images/POS-前台-客顯螢幕-結帳頁面01.en.png){ .medium-image }

=== "Interactive Games"

    ![](../../assets/images/POS-前台-客顯螢幕-互動遊戲01.en.png){ .medium-image }

=== "Checkout Information Confirmation Prompt"

    ![](../../assets/images/POS-前台-客顯螢幕-顧客資訊確認01.en.png){ .medium-image }

## FAQ { #faq-display-screen }

??? quote "Why didn't the customer display screen update after I changed the back-office settings?"
    After you save settings in the admin, the POS front end does not pull updates automatically. Be sure to click **Sync Customer Display Settings** on the **Settings and Connection Test** page of the POS front end. If the display still does not update, restart the POS APP.

??? quote "What should I do if **Unable to Play Video** appears on the customer display screen?"
    This is usually due to copyright restrictions on the YouTube video. We recommend uploading a video without copyrighted music. Alternatively, set the video to "Unlisted" when uploading it to YouTube, and make sure the video allows embedding on external websites.

??? quote "Why are the add-on purchase products shown on the customer display incorrect?"
    Customer display add-on purchases pull their settings from **Marketing > PWP-By Order**. Check that the campaign's effective period, applicable stores, and product inventory are all normal.

## More Actions { #next-steps-display-screen }

<div class="grid cards" markdown>

- :lucide-banknote:{ .lg }   
[__Create a POS Interactive Game__](../check/customer-display-interactive-games.md)     
Design a POS-exclusive spin wheel or prize draw campaign.

- :lucide-banknote:{ .lg }   
[__Create an Order Add-on Purchase Campaign__](../../ec/marketing/upsells/setup-order-upsell.md)     
Plan the eligible add-on items and trigger thresholds in advance.

</div>

