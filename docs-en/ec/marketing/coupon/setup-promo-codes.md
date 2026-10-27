---
title: "Set Up List Of Coupons"
description: "Set up List of Coupons (discount, free shipping, gift), including basic settings, usage thresholds, sending rules, and auto-apply at checkout."
created: 2026-05-27 13:55
last_modified: 2026-07-20 14:50
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
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定優惠碼
  - 建立贈品券
  - 自動套用優惠碼
  - 設定免運優惠碼
features: 
  - "List of Coupons"
  - "Gift Coupon"
  - 自動套用優惠
  - 免運折扣
prerequisites: []
related:
  - ec/marketing/coupon/multiple-coupons.en/
  - ec/marketing/purchase-restrictions/coupon-and-bonus-points-expiry-notification.en/
tags: 
  - 優惠碼
  - 贈品券
  - "Free Shipping"
  - Discount
  - 行銷活動
acoiv: configure
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 優惠碼輸入框
  - 贈品清單
paths: 
  - 行銷活動 > 優惠碼
  - 金物流 > 結帳頁 & 物流設定 > 結帳頁優惠券設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10457
  - https://www.cyberbiz.io/support/?p=1533
  - https://www.cyberbiz.io/support/?p=6228
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/setup-promo-codes.en/"
comments: false
search:
  exclude: false
icon: lucide/ticket
hide: []
---

# Set Up Promo Codes
Set up promo codes (discount, free shipping, and gift), including basic settings, usage thresholds, distribution rules, and automatic application at checkout.
{ .subtitle }


![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼01.png){ .hero-page }

!!! tip "Use Cases"
	- **Partnerships**: Give partners their own promo codes and track conversions by channel.
	- **Holiday promotions**: Create limited-time, limited-quantity discount codes to create urgency.
	- **Spend-threshold gifts**: Send gift codes so customers can pick a gift after reaching the threshold.
	- **Fewer abandoned carts**: Turn on automatic promo code application so customers see the discount at checkout.


## Before You Start

- **Not tied to accounts**: Promo codes aren't credited to member accounts. Any member with the code can apply it at checkout.
- **Not case-sensitive**: Promo codes ignore letter case, so they're easy to enter.
- **Calculation order**: Promo codes and coupons are at the same level. The system first applies a personal coupon with the same code.
- **Code format**: 8 uppercase letters and numbers. A member account can't hold two identical codes.


## Steps

### 1. Add A Promo Code

1. Log in to the CYBERBIZ admin and go to **Marketing > Coupons**.
2. Click **Create New Storewide Coupon**.
3. **Basic settings**:
    - **Coupon Title**: Enter a name (visible to members on the storefront).
    - **Period**: Set no end date or a specific period.
4. **Promotion details**: Choose the promo code type.

    === "Discount"

        Offer a fixed amount or percentage off.

        - **Discount**: Choose "Amount" or "Percentage" (for 90% of list price, enter 90%).
        - **Discount Code**: Enter your own code or let the system generate one.
        - **Maximum Discount**: For percentages, set the redemption cap per order. (Enterprise only)
        - **Minimum Spend**: The minimum order amount to use the code.
        - **Total Usage Limit**: The maximum number of times the code can be used across the store.
        - **Per-customer Limit**: The maximum number of times one member account can use the code. (PLUS and Enterprise only)
        - **Product Tags**: Limit this coupon to products with specific tags. (Advanced, Expert, PLUS, and Enterprise only)
        - **Combining with other promotions**: Choose how this coupon stacks with other promotions: `無限制`, `部分限制`, or `不可與優惠活動併用`.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼03.png){ .screenshot }

    === "Free Shipping"

        !!! note "Plan Availability"
            This feature is available on **PLUS and Enterprise** only.

        Offer free shipping to lower the cost of buying.

        - **Discount Code**: Enter your own code or let the system generate one.
        - **Minimum Spend**: The minimum order amount to use the code.
        - **Total Usage Limit**: The maximum number of times the code can be used across the store.
        - **Per-customer Limit**: The maximum number of times one member account can use the code.
        - **Product limits**: Offer free shipping only when specific products or tags are bought.
        - **Shipping methods**: Limit the offer to specific shipping methods (such as 7-Eleven pickup).

        ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼04.png){ .screenshot }

    === "Gift"

        !!! note "Plan Availability"
            This feature is available on **PLUS and Enterprise** only.

        Give a specific product once the threshold is met.

        - **Discount Code**: Enter your own code or let the system generate one.
        - **Minimum Spend**: The minimum order amount to use the code.
        - **Total Usage Limit**: The maximum number of times the code can be used across the store.
        - **Per-customer Limit**: The maximum number of times one member account can use the code.
        - **Gift Items**: Choose the products to give (by product only, not by variant).

            > **Stock**: The system sends variants in order until all variants are out of stock.


        ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼05.png){ .screenshot }




### 2. Create Promo Codes In Bulk

To create many storewide promo codes at once (**discount or free shipping only**), use bulk import.

!!! note "Plan Availability"
    This feature is available on **Enterprise Plan** only.

1. On the **Marketing > Coupons** page, click **Batch Import of Coupons**.
2. Download the CSV template.
3. Fill in the promo code details using the template (such as name, code, threshold, and validity).
4. Upload the file and choose the type to import (discount or free shipping). The system creates the codes.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼17.png){ .screenshot }

## Advanced Settings

### Supported Promo Code Types

These settings apply only to **storewide promo codes**, not to **member-only promo codes** or **coupons**:

| Type | Description | Auto-Apply |
| :--- | :--- | :--- |
| **Storewide promo code** | Added in **Marketing > Coupons**; treated as a storewide promo code | **Supported** |
| **Member-only promo code** | Sent to selected members in **Customer Management > All Customers** | Not supported |
| **coupon** | Added in **Marketing > 全館折扣-紅利&優惠券** | Not supported |


### Auto-Apply Promo Codes At Checkout

This feature applies promo codes to qualifying orders automatically, so customers don't have to enter them.


!!! note "Plan Availability"
    Auto-apply is available on **Expert PLUS** and **Enterprise Plan** only.


=== "Expert PLUS"

    - **One code**: You can link only **1** promo code.
    - **Trigger**: If the cart already has a promo code, auto-apply **won't** trigger.

=== "Enterprise"

    - **Multiple codes**: Link up to **5** promo codes and drag to set the order they apply in.
    - **Trigger**: Auto-apply still triggers even if the cart already has a promo code.
    - **Quantity limit**: The number of codes applied is limited by the "Coupon usage limit per order" setting.

#### Before You Start

- This feature only works on the online store checkout page, **not one-page stores**.
- Supports discount, free shipping, and gift codes.
- Works with both "Quick Checkout and Register" and "Registration Required" sign-up methods.

#### Steps

1. Go to **Payment and Logistics > Checkout Page & Logistics > 結帳頁優惠券設定**.
2. Turn on **Auto-Apply Promo Codes**.
3. Enter the **storewide promo code** to apply automatically.
4. When a customer reaches checkout and meets the threshold, the system applies the offer automatically.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼16.png){ .screenshot }



### Edit An Active Promo Code { #edit-ongoing-coupon }

#### Before You Start

- This feature is for **EC promo codes** only, not POS promo codes.

!!! note "Plan Availability"
    This feature is available on **Enterprise Plan** only.

#### Editable Fields

- Promo code name
- Promotion end time
- Total usage limit / uses per account

    !!! info "Editing Rules"
        - **Allowed**:
            - **Increase quantity**: If the promotion is popular, raise the limit at any time (for example, from 1,000 to 2,000).
        - **Not allowed**:
            - **Decrease quantity**: You can't lower the total.
            - **Change "Unlimited" to a set quantity**: Once a promotion is unlimited, you can't add a limit.


#### View Edit History

See the edit history at the bottom of the edit page:

- **Details**: Who made the change, when, and which fields.
- **Time range**: Only the past year of history is shown.
- **Promo code types**: Only shows history for **active** promo codes.

![](../../../assets/images/EC-後台-行銷活動-優惠碼-編輯紀錄01.png){ .screenshot }



## FAQ

??? quote "Can I limit a promo code to new members only?"
    Promo codes aren't tied to accounts, so you can't limit them to new or existing members. To target specific customers, send a "personal coupon" to their member accounts.



## More Actions

<div class="grid cards" markdown>


- :lucide-layers-2:{ .lg }
  [__Use Multiple coupons (Codes) Together__](multiple-coupons.md)
  Set the maximum number of coupons per order.

- :lucide-bell-ring:{ .lg }
  [__Set Up coupon Expiration Notifications__](../purchase-restrictions/coupon-and-bonus-points-expiry-notification.md)
  Have email, SMS, or LINE notifications automatically sent to remind customers to use offers before they expire.

</div>