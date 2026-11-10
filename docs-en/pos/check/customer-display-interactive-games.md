---
title: "Customer Display Interactive Games"
description: "Learn how to set up interactive games on the POS customer display screen, such as roulette and red envelope draws, to attract customers with fun promotions and boost sales of specific products."
created: 2026-04-07 17:30
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 包含輪盤與抽紅包兩種遊戲類型
  - 需注意遊戲建立後無法刪除
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 互動遊戲
sites:
  - TW
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: 
  - optional
cyb_extensions: []
audiences:
  - merchant
difficulty: intermediate
intents:
  - 設定 POS 互動遊戲
  - 提高客顯螢幕互動率
  - 刺激商品銷售
features:
  - 客顯互動遊戲
  - 行銷活動
prerequisites:
  - 需具備 POS 客顯螢幕設備
related:
  - pos/hardware/customer-display-screen/
  - ec/marketing/other-tools/interactive-games/
tags:
  - POS
  - "Customer Display"
  - "Interactive Games"
  - Promotion
  - Roulette
  - "Prize Draw"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 客顯互動遊戲頁面
  - 客顯螢幕
paths:
  - POS 功能 > 客顯互動遊戲
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=7666
permalink: "https://help.cyberbiz.io/pos/check/customer-display-interactive-games/"
comments: false
search:
  exclude: false
icon: lucide/gamepad-2
hide: []
---

# Customer Display Interactive Games
Set up fun interactive games on the customer display screen to capture customer attention. Use them to run promotions and discounts on products with specific tags.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! info "Version Differences"
    - **[EC Storefront (EC)](../../ec/marketing/other-tools/interactive-games.md)** and **Physical Store (POS)** both support interactive game features. This document only covers how to set up **EC Storefront (POS)** interactive games.
    - In the PLUS plan, "Interactive Games" is an optional module under "Marketing B" (select 2 of 11). Merchants must confirm this module is selected before they can use it. The Enterprise plan includes this feature by default.

![](../../assets/images/POS-後台-互動遊戲-畫面總覽01.en.png){ .hero-page }

!!! tip "Use Cases"
	- **New Product Promotion**: Set up a "quantity-threshold draw" for newly listed products to increase customer purchase intent.
	- **Holiday Campaigns**: Change the game template (such as red envelope or capsule toy) to create a festive atmosphere in the store.
	- **Inventory Clearance**: Set products with specific tags as the game threshold to speed up inventory turnover.


## Before You Start { #prerequisites-display-games }

- **Non-Deletable**: Once a game is created and saved, the system cannot delete its record.
- **Time Requirement**: Fill in both the **Start** and **End** times before the game can be activated.
- **Editing Restrictions**: Once a game is saved, its **Prize Content** and **Starting Time** cannot be changed.
- **Image Limit**: The total size of all images uploaded for a single game (style images and prize images) must not exceed **10MB**.
- **Automatic End**: If all prizes are drawn during the campaign period, the game ends immediately.

## Game Status Descriptions { #specs-display-games }

| Status | Description |
| :--- | :--- |
| **Scheduling** | The game start time has not yet arrived, or the time settings are not complete. |
| **In Progress** | The game campaign is running. Its type, tags, start time, and prizes cannot be changed. |
| **Finished** | The campaign period has ended, or all prizes have been awarded. |
| **Paused** | The campaign is paused manually. Click "Resume Game" to resume it. |


## Operating Procedure { #operate-display-games }

### Step 1: Create a Game { #operate-display-games-step-a-create }

1. Go to the CYBERBIZ POS admin panel and click **POS > Interactive Games**.
2. Click **Add Game**.
3. **Basic Settings**:
    - **Campaign Name**: Enter an easy-to-identify campaign name.
    - **Game Type**: Select "Roulette Draw" or "Red Envelope Draw".
    - **Period**: Set the exact start and end times.
4. **Set Trigger Rules**:
    - **Buy two, second one on discount**: Each set of 2 items with the specified tag qualifies for one draw.
    - **Lottery with Purchase**: Qualify for a draw when the total amount of items with the specified tag meets the threshold (not cumulative).
    - **Lottery with Item**: Qualify for a draw when the total quantity of items with the specified tag meets the threshold (not cumulative).
5. **Select Product Tags**: Select the product tags to include in the campaign.

![](../../assets/images/POS-後台-互動遊戲-建立遊戲01.en.png){ .screenshot }

### Step 2: Style and Prize Settings { #operate-display-games-step-b-settings }

1. **Style Settings**:
    - Select a default template (red envelope, gift, or capsule toy) or upload a custom theme image.
2. **Prize Settings**:
    - Click **Add Prize**.

        > The roulette game supports up to 10 prizes.

    - **Prize Name**: Keep it within 10 characters for clear display on the screen.
    - **Prize Type**: Choose "No Prize", "Discount Amount", "Percentage", or "Gift" (only available for amount-threshold or quantity-threshold draws).
    - **Win Probability**: The probabilities of all prizes must add up to **100%**.

![](../../assets/images/POS-後台-互動遊戲-建立遊戲02.en.png){ .screenshot }

### Step 3: Link the Customer Display Device { #operate-display-games-step-c-bind }

After you finish the setup, enable the feature in Store Settings.

1. Go to the CYBERBIZ POS admin panel and click **POS > POS Store List**.
2. Select the target store, then click **Customer Display Marketing**.
3. Select the corresponding POS device, then click **Edit**.
4. Select **Enable Customer Display Marketing Feature**.
5. Select **Customer Display Game**, then select the game to run from the dropdown menu.
6. Click **Save**.

![](../../assets/images/POS-後台-互動遊戲-建立遊戲03.en.png){ .screenshot }

## Front-End Animation Effects { #intro-display-games }

=== "Roulette Draw"

    ![](../../assets/images/POS-前台-客顯螢幕-互動遊戲-轉蛋01.en.gif){ .small-image }

=== "Red Envelope Draw"

    ![](../../assets/images/POS-前台-客顯螢幕-互動遊戲-紅包01.en.gif){ .small-image }

## FAQ { #faq-display-games }

??? quote "After a customer wins **Gift**, will the system automatically add it to the cart?"
    No. After a customer wins a free gift, **staff must manually scan the gift barcode to add it to the cart**. The system will then automatically convert that item to NT$0.

??? quote "The game period has ended, but some prizes remain. Can I extend it?"
    Yes. Edit the game's **Ending Time** directly to extend the campaign.

??? quote "Why isn't the game showing on my customer display screen?"
    Check the following:
    1. The game status is **In Progress**.
    2. The game is selected under **Customer Display Marketing** in store settings.
    3. The items in the cart meet the configured **product tags** and **threshold**.

## More Actions { #next-steps-display-games }

<div class="grid cards" markdown>

- :lucide-layout-template:{ .lg }   
  [__Customer Display Setup and Layout__](../hardware/客顯螢幕){ data-preview }    
  Learn how to correctly connect the customer display screen and customize its display content and layout.

</div>
