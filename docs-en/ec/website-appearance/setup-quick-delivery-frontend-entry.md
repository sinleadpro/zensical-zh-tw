---
title: "Set Up the Express Delivery Storefront Entry and Section"
description: "Learn how to set up the storefront entry to the Express Delivery section, customize the navigation bar style, and improve how the section's content displays with the theme editor."
created: 2026-02-03 00:00
last_modified: 2026-09-18 14:10
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 提醒商家 POS 與電商倉儲串接限制。
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: 
  - optional
cyb_extensions:
  - NOW!
intents:
  - 設定首頁快速到貨入口
  - 自訂專區導覽列顏色
  - 新增快速到貨選單連結
  - 管理快速到貨頁面顯示選項
features:
  - CYBERBIZ NOW
  - 快速到貨
prerequisites:
  - 門市已開啟快速到貨功能
  - 已將商品複製到快速到貨門市
related: []
tags:
  - "Express Delivery"
  - "Website Interface"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 前台 > 快速到貨專區
  - 後台 > 網站外觀 > 連結列表
paths:
  - 主題版型 > 拖拉設定 > 快速到貨
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=12861
  - https://www.cyberbiz.io/support/?p=24278
permalink: "https://help.cyberbiz.io/ec/website-appearance/setup-quick-delivery-frontend-entry/"
comments: false
search:
  exclude: false
icon: lucide/layout-template
hide: []
---
# Set Up the Express Delivery Storefront Entry and Section

Use a dedicated entry button and a visual section to draw shoppers into the express delivery service, improve conversion, and reduce delivery confusion.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

![](../../../assets/images/EC-前台-首頁-快速到貨專區01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Eye-catching entry point**: Place a prominent express delivery button on the homepage so shoppers with urgent needs find the service right away.
    - **Extended brand visuals**: Customize the section's navigation bar colors so **Express Delivery** looks clearly different from your **regular online store**, reducing shopping confusion.
    - **Promotional content**: Add a dedicated campaign banner or carousel at the top of the express delivery page to highlight instant delivery offers.


## Before You Start { #prerequisites-qd-entry }

Before you set up the storefront page, note this system limitation:

- **Theme limitation**: The system offers two ways to build your site: **drag-and-drop themes** and **default themes**. Because they are built differently underneath, their feature specs and customization flexibility differ slightly.


## Set Up the Entry Point { #operate-qd-entry }

There are two ways to set this up. Choose based on your site's theme:

=== "Drag-and-Drop Theme"

    Turn on the site-wide button. It appears at the top right of your website pages, where it stands out the most.

    1. Sign in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > Theme Setting**.
    2. In the page menu at the top center, select **Express Delivery Setting**.
    3. Open the **Express Delivery Setting** module and select **Show Express Delivery Button**.

    ![](../../../assets/images/EC-後台-網站外觀-套版主題管理-開啟快速到貨前台按鈕01.en.png){ .screenshot }


=== "Default Theme"

    Add a navigation bar link manually so shoppers can click it in the navigation bar.

    1. Go to **Website Appearance > Menu Setting**.
    2. In the **Main Menu**, click **Add Menu Item**.
    3. **Item name**: Enter **Express Delivery Section**.
    4. **Link to**: Select **External Link**.
    5. **URL**: Enter your website's homepage URL followed by `/branch_stores/express_delivery`.

        > Example: `https://www.yourstore.com/zh-TW/branch_stores/express_delivery`
    
    ![](../../../assets/images/EC-後台-網站外觀-選單導覽列-預設版型新增快速到貨專區連結01.en.png){ .screenshot }


## Customize the Section's Look and Content { #operate-qd-entry-visual }

=== "Drag-and-Drop Theme"

    ### 1. Navigation Bar and Icon Colors { #operate-qd-entry-colors }
    Set a dedicated color scheme to set the section apart from regular products:

    - **Logo background color**: Sets the background color of the section's top navigation bar (ideally matching your brand's main color).
    - **Icon color**: Sets the line color of the navigation bar icons (such as the cart and search).

    ### 2. Add Section-Specific Blocks { #operate-qd-entry-blocks }
    The main layout is fixed, but you can still add engaging content at the top of the section:

    1. In the editor's **Custom Layout Settings** module, click **Add Block**.
    2. Select the type you want to add:
        - **Image**: Add a dedicated campaign banner.
        - **Scheduled carousel**: Show messages such as "Free shipping on orders over 1,000" or delivery area details.
        - **Products**: Manually pick 3–4 featured products for express delivery.
    3. Drag blocks to change their display order.

    !!! warning "Layout Structure"
        The express delivery page uses a fixed structure to ensure performance and consistency across devices. You can add blocks only at the **top of the page**. The rest cannot be dragged.

    ![](../../../assets/images/EC-後台-網站外觀-套版主題管理-自訂排版設計01.en.png){ .screenshot }

=== "Default Theme"

    Default themes do not support this feature.


## FAQ { #faq-qd-entry }

??? quote "Why can't I drag blocks on my express delivery page?"
    The express delivery page uses a fixed layout to provide the best loading speed and a consistent experience across devices (especially on mobile). You can only add custom content at the top of the page through **Custom Layout Settings**, or edit the **Footer**.

??? quote "Will changing the navigation bar color affect other pages on my website?"
    No. The **Logo background color** in the express delivery editor affects only the express delivery section pages. This is intended to help shoppers clearly recognize which section they are in. Note, however, that changes to the **Footer** apply site-wide.

??? quote "How do I keep out-of-stock products out of the section?"
    In the editor's **Express Delivery Setting** module, switch **Show Out-of-Stock Products** to `OFF`. The system automatically hides product copies with 0 inventory.



