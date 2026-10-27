---
title: "Send Coupon For Specific Products"
description: "Create a coupon group. When a member buys selected products and completes the order, the coupon is automatically sent to their account, boosting repeat purchases and loyalty."
created: 2026-01-21 00:00
last_modified: 2026-06-30 10:56
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
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - Enterprise
cyb_extensions: []
intents:
  - 設定指定商品送優惠券
features:
  - coupon
prerequisites: []
related:
  - ec/marketing/references/coupon-and-bonus-credit-rules.en/
tags:
  - 優惠券
  - "coupon Group List"
  - "Product Tags"
  - "Combining with Other Promotions"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 指定商品送優惠券
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=11460
permalink: "https://help.cyberbiz.io/ec/marketing/conditional-send/send-coupons-for-specific-products.en/"
comments: false
search:
  exclude: false
icon: lucide/ticket-percent
hide: []
---
# Send Coupons For Specific Products

Create a coupon group. When a member buys selected products and completes the order, the coupon is automatically sent to their account, boosting repeat purchases and loyalty.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | Enterprise
{ .doc-badge }

![](../../../assets/images/EC-後台-行銷活動-指定商品送優惠券-畫面總覽01.en.png){ .hero-page }

## About Sending Coupons For Specific Products

Send coupons for Specific Products (coupon groups) sends coupons automatically. You choose specific products or product tags, and members who buy them get a preset coupon. Use it to encourage repeat purchases, cross-sell, or clear inventory faster.

!!! tip "Use Cases"
    - **Drive repeat purchases with new arrivals**: Give a NT$100 discount coupon with "2024 Spring New Arrivals" to bring customers back.
    - **Cross-sell categories**: Give a makeup coupon with skincare purchases to get customers to try other categories.
    - **Clear inventory faster**: Give a high-value coupon with clearance items to motivate customers to buy slow-moving stock.

## Before You Start

- **Number of coupons**: Choose "Cumulative" (one coupon per item bought) or "Non-cumulative" (one coupon per order).
- **Multiple groups**: A product can be in more than one coupon group. After purchase, the system sends the coupons from every group the product belongs to.
- **Cross-channel use**: coupons that members get from online purchases can be used at checkout for POS store orders.
- **POS product limitation**: Only products sold online are eligible. POS-only products don't support automatic coupon sending.
- **Stacking limits**: In the settings, you can specify whether the coupon can be used with promotions such as store-wide discount and single-product discounts.

## Steps

### Step 1: Create A Coupon Group

1. Log in to the CYBERBIZ admin and go to **Marketing > Issue Coupon for Selected Product**.
2. Click **New Coupon Collection**.

### Step 2: Enter Basic Settings And Sending Rules

1. **Basic information**:
    - **Coupon Name**: A name to identify it in the admin (such as 2024 Spring Coupon Promotion).
    - **Period**: Select it and set the start and end dates. If you leave it unselected, the promotion starts right away and runs indefinitely.
2. **Coupon Give Rule Setting**:
    - **Cumulative Gift**: One coupon per item (the more customers buy, the more they get).
    - **Non-cumulative Gift**: One coupon per order (to control costs).

![](../../../assets/images/EC-後台-行銷活動-指定商品送優惠券-基本設定01.en.png)

### Step 3: Set The Coupon Rules

In the **coupon Rules** section, define the coupon to send:

1. **Types of Coupon**: Choose "Amount discount" or "Percentage discount" and enter a value.
2. **Expiration Date**:
    - **Validity Period in Days**: Counted from the date the coupon is sent (for example, `30` days).
    - **Validity Period Range**: A fixed date range. All coupons expire on the same date.
3. **Minimum Consumption Threshold**: The minimum order amount needed to use the coupon (for example, `500`).
4. **Link product tags** (optional): Limit the coupon to products with specific tags.

![](../../../assets/images/EC-後台-行銷活動-指定商品送優惠券-優惠券規則設定01.en.png)

### Step 4: Set Stacking Limits

1. Select **No Limit** (works with all promotions) or **Not applicable for selected promotions**.
2. If you choose the latter, select the promotion types that can't be combined (such as store-wide discount, single-product discounts, and VIP discounts).


## More Actions

<div class="grid cards" markdown>

- :lucide-wallet:{ .lg }
  [__coupon / Bonus Points Crediting Rules__](../references/coupon-and-bonus-credit-rules.md)
  Explains when purchase rewards are credited to accounts (import members), and how order completion and returns affect crediting of bonus points and coupons.

</div>