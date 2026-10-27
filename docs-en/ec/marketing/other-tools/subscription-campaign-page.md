---
title: "Subscription Campaign Page"
description: "Learn how to create a subscription campaign page, including basic settings, per-cycle discounts, payment restrictions, and preparation time, to help your brand build steady revenue."
created: 2026-05-29 18:01
last_modified: 2026-07-20 18:50
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
  - Marketing
  - 金物流
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: branch
plans: 
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents: 
  - 建立定期定額活動頁
  - 設定訂閱制優惠
  - 配置定期定額備貨期
features: 
  - "Recurring Payments"
  - Subscription
  - 指定期數優惠
prerequisites: 
  - "需選配定期訂購.en"
related: []
tags: 
  - 定期定額
  - 訂閱制
  - 行銷活動
  - "Automatic Billing"
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 定期定額活動頁
  - 進階優惠設定
paths:
  - 金物流 > 結帳頁 & 物流設定 > 定期定額購物車設定
  - 行銷活動 > 定期訂購活動頁
  - 金物流 > 宅配物流
  - 金物流 > 超商物流
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=53869
  - https://www.cyberbiz.io/support/?p=16465
  - https://www.cyberbiz.io/support/?p=1618
permalink: "https://help.cyberbiz.io/ec/marketing/other-tools/subscription-campaign-page.en/"
comments: false
search:
  exclude: false
icon: lucide/calendar
hide: []
---

# Subscription Campaign Page
Learn how to create a subscription campaign page, including basic settings, installment discounts, payment limits, and preparation time, to help your brand build steady revenue.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

![Subscription Campaign Event Page](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁03.png){ .hero-page }

!!! info "Version Differences"
    - On PLUS plans, Subscriptions is an add-on module (choose 2 of 11). Make sure you have selected this module before using it. Enterprise includes it by default.

!!! tip "Use Cases"
    - **Repeat purchases**: Set up monthly delivery for consumables (such as probiotics or tissues) so customers don't need to reorder.
    - **Long-term discounts**: Use "Installment Discounts" to keep customers subscribed, such as 90% of list price from the 3rd installment.
    - **Member rewards**: After a subscription order is completed, bonus points can be automatically sent to build loyalty.



## Before You Start

Before you begin, understand these system rules and limits:

- **NT$1 card authorization**: On the first order, the system shows a NT$1 card authorization to verify the card. This amount is **never actually charged**, so you don't need to refund it.
- **No other promotions**: Subscription Campaign Event Pages **can't use** other marketing promotions or commission features.
- **Shipping limits**: Convenience Store Logistics only supports the room-temperature temperature zone.
- **Payment limits**:
    - Supported: CYBERBIZ PAYMENTS, cash on delivery, Aftee, GMO 3D Secure, and background authorization.
    - Not supported: Installment payments.
    - Special case: If you don't use CYBERBIZ PAYMENTS, connect your own payment gateway (such as ECPay or NewebPay) and apply for cash on delivery with Custom Logistics.
- **Theme dependency**: The page uses your current theme. If you change your website theme, you need to create the campaign page again.


## Step 1: Regular Installment Shopping Cart Setup

This setting controls the default product quantity when customers open the campaign page.

1. Log in to the CYBERBIZ admin and go to **Payment and Logistics > Checkout Page & Logistics > 定期定額購物車設定**.

| Option | Description | What Customers See |
| :--- | :--- | :--- |
| **Default quantity 1** | Each product quantity starts at 1 | Customers can only increase quantities and must buy every product |
| **Default quantity 0** | Each product quantity starts at 0 | Customers can freely choose which products to buy |

> **Note**: The setting applies to all campaign pages right away but doesn't affect existing orders.

![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁19.png){ .screenshot }


## Step 2: Create A Subscription Campaign Page


1. Log in to the CYBERBIZ admin and go to **Marketing > Subscription Campaign Event Page**.
2. Click **Add Page** in the top-right corner.
    ![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁01.png){ .screenshot }
3. Enter the **Title** (shown on the storefront) and the **URL Title** (a custom URL suffix).
    ![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁02.png){ .screenshot }
4. Save to open the detailed settings page.
    ![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁03.png){ .screenshot }



## Step 3: Configure The Campaign

### 1. Basic Settings

- **Search products**: Add products to the page. Each page can have **up to 10 products**.

    ![](../../../assets/images/EC-後台-行銷活動-定期訂購活動頁-建立活動01.png){ .screenshot }

- **Campaign Title**: A custom campaign name shown as the storefront page Title.
- **URL Title**: A custom URL suffix for the campaign page.
- **Image upload**: Upload the campaign banner.
- **Campaign period**: Set the start and End date. After it ends, members can't see the page, but **existing sub-orders stay active** unless you or the member cancel them.

    ![](../../../assets/images/EC-後台-行銷活動-定期訂購活動頁-建立活動02.png){ .screenshot }

- **Pending order settings (preparation time)**:
    - For example, with 3 days: if the shipping date is 10/31, the system creates the order and charges payment on 10/27 (the order date and shipping date don't count toward preparation time).

    ![](../../../assets/images/EC-後台-行銷活動-定期訂購活動頁-建立活動03.png){ .screenshot }

- **Main order cancellation on the storefront**:
    - Let customers cancel the main order on the storefront only after installment N. If this is off, customers can only cancel individual sub-orders, and you must cancel the main order in the admin.

        !!! info "Quick Tip"
            This counts **subscription installments** (delivery rounds), not **actual orders** (successful orders). Even if an order fails (for example, the payment fails), that round still counts as an installment.

            Example:
            If set to **1**, customers can cancel after **installment 2**. Even if the installment 1 order fails, customers can cancel the main order once the 2nd delivery round arrives.


    ![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁07.png){ .screenshot }

- **Combine with VIP discount**: If on, the system checks whether the main order gets VIP discounts or free shipping.


- **Delivery interval**: Ship by "Month," "Week," or "Specific Date" (you can select more than one).
    ![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁08.png){ .screenshot }


### 2. Variant Settings

Set campaign-specific prices for products and choose whether to show them in the cart.

![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁10.png){ .screenshot }


### 3. Edit Content

Advanced code Editing lets technical staff customize the layout of the Subscription Campaign Event Page.

!!! danger "Important"
    CYBERBIZ doesn't provide guidance on changing or restoring this section. Have your own technical staff make any code changes, and back up the original code first.

![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁11.png){ .screenshot }


### 4. Advanced Discount Settings

- **Gift on specific period**: Send a specific product as a gift on **Specific Number of Periods** or within a **Specific Period Range**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁14.png){ .screenshot }



- **Discount on specific period**: Give an extra discount on **Specific Number of Periods** or within a **Specific Period Range**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額活動頁16.png){ .screenshot }

!!! warning "Notes"
    - **No overlapping discounts**: An installment that already has a discount can't get another discount of the same type.
    - **Excluded orders**: "Canceled" or "Returned" orders don't count toward the number of deliveries.


!!! example "How Returns Affect Installment Counting"
    When a subscription order is returned, the system recounts valid orders but skips gifts that were already received.

    **Example settings**:

    - **Installment 1**: Gift A
    - **Installment 2**: Gift B
    - **Installment 3**: Gift C

    **How orders are counted**:

    | Order | System Logic | Gift Result |
    | :--- | :--- | :--- |
    | **1st order** | Installment 1 | ✅ **Gift A sent** |
    | **2nd order** | Installment 2 | ✅ **Gift B sent** |
    | **Return** | **First 2 orders both returned** | - |
    | **3rd order** | Recounted as "Installment 1" | ✕ **No gift**<br>(Reason: Gift A already received) |
    | **4th order** | Recounted as "Installment 2" | ✕ **No gift**<br>(Reason: Gift B already received) |
    | **5th order** | Recounted as "Installment 3" | ✅ **Gift C sent**<br>(Reason: Gift C not yet received) |

    > The system checks the full history. If returns cause installments to be recounted, a gift already shipped with this subscription won't be sent again.


### 5. Payment Settings

Select the Payment Methods available for this campaign.

![](https://www.cyberbiz.io/support/wp-content/uploads/定期定額金流設定-1024x528.jpg){ .screenshot }


!!! tip "Tip"
    If you don't see a payment option, turn on the payment method in **Payment and Logistics > Payment Settings**, or turn on the shipping method in **Payment and Logistics > 宅配物流 / 超商物流**. It will then appear in this list.

## FAQ

??? quote "Why haven't customers received their bonus points?"
    Subscription bonus points are added to the customer's account only after the **sub-order is completed**.



