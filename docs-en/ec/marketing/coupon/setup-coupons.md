---
title: "Set Up Coupon"
description: "Learn how to set up a coupon, including how to Send to all members (store-wide), send in bulk by import, and send to a single customer."
created: 2026-05-27 16:30
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
  - Marketing
  - 會員
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定優惠券
  - 發送折價券
  - 批次匯入優惠券
  - 贈送註冊禮
features: 
  - coupon
  - "Discount Coupon"
  - 消費回饋
  - 註冊贈禮
prerequisites: []
related:
  - ec/members/manage-member-profiles.en/
  - ec/marketing/coupon/multiple-coupons.en/
  - ec/marketing/purchase-restrictions/coupon-and-bonus-points-expiry-notification.en/
tags: 
  - 優惠券
  - 折價券
  - 行銷活動
  - "Member Engagement"
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 優惠券設定欄位
  - 會員列表
paths:
  - 行銷活動 > 全館折扣-紅利 & 優惠券
  - 會員 > 所有會員
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1779
  - https://www.cyberbiz.io/helpcenter/?p=3435
  - https://www.cyberbiz.io/helpcenter/?p=509
  - https://www.cyberbiz.io/helpcenter/?p=5686
  - https://www.cyberbiz.io/support/?p=11928
  - https://www.cyberbiz.io/support/?p=6207
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/setup-coupons.en/"
comments: false
search:
  exclude: false
icon: lucide/ticket-percent
hide: []
---

# Set Up Coupons
Learn how to set up coupons, including how to Send to all members (store-wide), send in bulk by import, and send to a single customer.
{ .subtitle }


!!! tip "Use Cases"
	- **First purchase**: Give a coupon at sign-up to make new customers more comfortable placing their first order.
	- **Spending rewards**: Give a discount coupon when customers reach a spending threshold, encouraging bigger orders for a discount next time.
	- **Targeted marketing**: Send exclusive coupons in bulk to specific member groups.
	- **Make-goods and surprises**: send manually a coupon to a single customer as service compensation or a holiday surprise.


## Before You Start

- **Deletion limit**: Once a coupon is in a customer's account (import members), you can only delete it [one by one from the member's page](../../members/manage-member-profiles.md#2-優惠券派發與管理). The system can't take coupons back in bulk.

### Cancellations And Returns

| Scenario | Rule |
| :--- | :--- |
| **Order canceled** | coupons used in the order are **returned automatically** to the customer's account |
| **Return** | coupons used in the order are **not returned automatically**<br>該訂單滿額所獲得的折價券，系統 **not** deducted from the customer's account |
| **Deduction on return** | Discount coupons earned by the order (Applicable only on orders that are) are **not deducted automatically from the customer's account** |


## Send Coupons In Bulk With Excel

1. Go to **Marketing > 全館折扣-紅利 & 優惠券** and select **Bulk send Member exclusive coupons**.
2. Click **Download Template**. Delete the sample content and keep only the blue header rows.
3. **Excel template fields**:

    | Field | Rules and Notes |
    | :--- | :--- |
    | **Customer Email (per recipient)** | Checked first. The phone number is checked only if this is blank<br>- Send to all members: enter `[all]` (half-width, lowercase)<br>- Send to specific members: enter their email |
    | **Customer Phone (per recipient)** | Checked only if the email field is blank <br>- Send to all members: enter `[all]` (half-width, lowercase)<br>- Send to specific members: enter their phone number |
    | **Discount name** | The name customers see on the storefront (required) |
    | **Coupon Code** | 8 uppercase letters and numbers (required) |
    | **Discount** | A fixed Amount or a Percentage (for 80% of list price, enter `80%`) |
    | **Total Uses** | Total number of times this code can be used (≥ 1) |
    | **Uses per Account** | Number of times one member can use it (≥ 1). Leave blank for unlimited<br>(PLUS and Enterprise only) |
    | **Minimum Spend** | The order Amount needed to use it (enter `0` for no minimum) |
    | **Valid Period** | Set the start and end time. Leave blank for no limit |
    | **Link to product tag** | Enter a tag name to limit the discount to products with that tag<br>(Advanced, Expert, PLUS, and Enterprise only) |
    | **Stacking with Promotions** | 規範優惠券與其他行銷活動（如紅配綠、滿額折）的疊加規則：<br><br>**1. [unrestricted] (fully stackable)**：優惠券可與所有活動疊加。不論商品是否已享有其他折扣，皆可進行折抵<br>- 後方活動欄位 [11]-[18] ：留空即可<br><br>**2. [restrict] (exclude products in specific promotions, item level)**: If a **single product** in the order already has a selected promotion applied, that product is **not included** 優惠券的折抵金額，但訂單內其他未參加活動的商品仍可正常折抵<br>- 後方活動欄位 [11]-[18] ：欲指定排除，填寫 `[true]排除`<br><br>**3. [forbidden] (block if any promotion item is present, order level)**: If the cart contains any product with a selected promotion, the **whole order** can't use the coupon<br>- Promotion fields [11]-[18]: to exclude, enter `[true]排除` |

    ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-批次-建立發送-優惠券碼05.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-批次-建立發送-優惠券碼06.png){ .screenshot }

4. Save the file, go back to the admin, and click **Upload File** to finish the import.


### Notification Rules For Bulk Coupons

- **Specific members**: After import, the system automatically sent an email or SMS notification to customers.
- **All members (all)**: The system adds coupons to the member center automatically but **doesn't** send notifications.
- **Who can receive them**: Only members registered on your store. Rows with emails not found in the system are skipped.


## Send Coupons In Bulk With Filters

Go to **Customer Management > All Customers** and use member filters, or [send manually or delete coupons](../../members/manage-member-profiles.md#2-優惠券派發與管理) for a specific person.


## More Actions

<div class="grid cards" markdown>

- :lucide-layers-2:{ .lg }
  [__Stack Multiple coupons (Codes)__](multiple-coupons.md)
  Set the maximum number of coupons per order.

- :lucide-bell-ring:{ .lg }
  [__Set Up coupon Expiry Notifications__](../purchase-restrictions/coupon-and-bonus-points-expiry-notification.md)
  Set up email, SMS, or LINE notifications automatically sent by the system to remind customers to use expiring offers.

</div>

