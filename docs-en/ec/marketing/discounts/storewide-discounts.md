---
title: "Set Up Store-wide Discount"
description: "Learn how to create store-wide promotions, including Amount discounts, Percentage discounts, and threshold coupon offers per order, to raise average order value and repeat purchases."
created: 2026-06-26 18:30
last_modified: 2026-06-26 18:30
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
  - Professional
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
cyb_extensions: []
intents: 
  - 設定全館折扣活動
  - 建立滿額折抵優惠
  - 設定滿額送優惠券
features: 
  - "store-wide discount"
  - 滿額贈券
  - 累計折抵
prerequisites: []
related: []
tags: 
  - 全館折扣
  - Promotions
  - "Threshold Discount"
  - "Threshold Gift"
acoiv: configure
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 舉辦全館活動
  - 新增全館活動
paths:
  - 行銷活動 > 全館折扣-紅利 & 優惠券
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=1165
  - https://www.cyberbiz.io/support/?p=30011
permalink: "https://help.cyberbiz.io/ec/marketing/discounts/storewide-discounts.en/"
search:
  exclude: false
icon: lucide/percent
hide: []
---

# Legacy Store-wide Discount
Learn how to create store-wide promotions, including Amount discounts, Percentage discounts, and threshold coupon offers (one coupon per qualifying order), to raise average order value and repeat purchases.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Professional / Advanced / Expert / All PLUS
{ .doc-badge }

!!! tip "New Interface"
    **store-wide discount** has a new interface, currently available only on the **Enterprise** plan. It will roll out to other plans over time.


!!! tip "Use Cases"
	- **Holiday sales**: Run promotions such as "Everything at 85% of list price at checkout" or "Spend NT$1,000 store-wide and pay 80% of list price."
	- **Spend and save**: Set up "NT$100 off every NT$1,000" to reduce the Amount of the current order.
	- **Drive repeat purchases**: Set up "Spend a threshold, get a coupon" so customers get a discount for next time after completing an order.


## Before You Start

- **Best discount wins**: If several "Amount" and "Percentage" store-wide promotions are active, the system automatically applies the one with the highest discount Amount.
- **When coupons activate**: Threshold coupons (one per order) are added to the customer's account when the order is placed, but activate only after the order is completed.
- **Return restriction**: If the order status is Returned, Partially Returned, Not Picked Up, or Refunded, the system won't activate the coupon (issued per order) after the order is completed.


## Steps

### Create An Amount Or Percentage Discount
Reduce the Amount of the current order directly.

1. Log in to the CYBERBIZ admin and go to **Marketing > 全館折扣-紅利 & 優惠券**.
2. Click **Add Store-Wide Promotion**.

	![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動01.png){ .screenshot }

3. Set the basic promotion information:
    - **Promotion Name**: Enter a name.
    - **Spending Amount**: Set the minimum spend that triggers the offer.
    - **Start/End Date**: Set the promotion period. Leave it blank to start right away with no end date.
4. Choose the promotion type:

    === "Amount"

        Enter the discount Amount. You can select **Cumulative Discount** (for example, NT$100 off NT$1,000 and NT$200 off NT$2,000).

        ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動02.png){ .screenshot }

    === "Percentage"

        Enter the discount rate (for 85% of list price, enter 85%).

        ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動02.png){ .screenshot }

    === "coupon"

        !!! info "Plan Availability"
            This feature is available only on the **Expert**, **Expert PLUS**, and **Enterprise** plans.

        1. Set up the coupon:
            - **coupon Amount**: Set the discount value (per coupon).
            - **Promotion Period**: Set the coupon's start and end time.
            - **Minimum Spend**: Set the minimum spend for the customer's next use of this coupon.
        2. Set the restrictions:
            - **Link to product tag**: Limit the coupon to products with specific tags.
            > This feature isn't available on the **Professional** plan.
            - **Stacking Limits**: Set how this coupon stacks with other promotions.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動03.png){ .screenshot }



## How The System Decides

### Multiple Threshold Rules (One Coupon Per Order)

When you set up several "spend and get a coupon" promotions with different thresholds, the system gives only one coupon for the **highest threshold met** (per order). Coupons don't stack (not one per threshold).

!!! example "Example: Multiple Thresholds"
    - **Threshold 1**: Spend 1,000, get a NT$50 coupon.
    - **Threshold 2**: Spend 1,500, get a NT$100 coupon.
    - **Result**:
        - A customer spends 1,200: meets Threshold 1 and gets one 50 coupon.
        - A customer spends 1,600: meets Threshold 2 and gets one 100 coupon (not the 50 coupon as well).
