---
title: Set up bonus points
description: Use bonus points to build a member rewards program that attracts first purchases and increases repeat orders.
created: 2026-05-27 15:20
last_modified: 2026-08-19 12:25
lang: zh-TW
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
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定紅利回饋
  - 手動發送紅利
  - 調整紅利兌換比例
  - 處理退貨紅利
features: 
  - 紅利點數
  - 消費回饋
  - 批次發送紅利
prerequisites: []
related: 
  - "ec/marketing/references/coupon-and-bonus-credit-rules.md"
  - "ec/marketing/bonus-and-gifts/setup-registration-gift.md"
  - "ec/marketing/bonus-and-gifts/setup-birthday-gift.md"
tags: 
  - 紅利點數
  - 購物金
  - 行銷活動
  - 會員經營
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 紅利設定欄位
  - 會員列表
paths: 
  - 行銷活動 > 全館折扣-紅利 & 優惠券 > 會員紅利點數
  - 金物流 > 結帳頁 & 物流設定 > 訂單相關設定 > 訂單取消退貨相關紅利設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3805
  - https://www.cyberbiz.io/helpcenter/?p=3807
  - https://www.cyberbiz.io/helpcenter/?p=3812
  - https://www.cyberbiz.io/support/?p=42367
  - https://www.cyberbiz.io/support/?p=6103
permalink: "https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-bonus-points/"
comments: false
search:
  exclude: false
icon: lucide/coins
hide: []
---

# Set up bonus points
Use bonus points to build a member rewards program that attracts first purchases and increases repeat orders.
{ .subtitle }


![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-設定會員紅利點數01.png){ .hero-page }

!!! tip "Use cases"
	- **Boost loyalty**: Set purchase rewards so customers earn points after each order and have a reason to return.
	- **Holiday promotions**: Send vouchers to every member to create urgency for limited-time shopping.
	- **Compensation or rewards**: send manually points to selected members as customer-service compensation or exclusive campaign rewards.


## Notes

- **Issuance basis**: bonus points per is calculated from the checkout Amount **excluding shipping**.
- **Effective time**: Changes to bonus issuance rules apply only to actions that occur **after you save**. Points already issued are not affected.
- **Import limits**: After bonus points are issued or Remove, the system cannot auto-recall or restore them. Confirm before you proceed.


### Order bonus crediting rules


Purchase-reward bonuses credit only when the order is **Closed** and the return status is **No return needed**. Bonuses are not credited during Return in progress, Return under review, or Return rejected.

See [coupon / bonus crediting rules](../references/coupon-and-bonus-credit-rules.en.md) for full conditions and scenarios.

## Setup steps

1. Log in to the CYBERBIZ admin and go to **Marketing store-wide discount-Bonus & Coupons**.
2. Scroll to the **Member Bonus Points (Vouchers)** section and switch it to `開啟`.
3. Set the core fields:
    - **bonus redemption conversion**: Set `X 點 = NT 1` (default 1:1).
    - **Minimum spend threshold**: The NT$ order total required before members can redeem bonus points.
    - **Apply spending bonus to valid orders from other channels**: Whether to issue bonus points when you manually add a [valid order from other channels](../../members/manage-member-profiles.en.md#2-其他通路訂單). **(Enterprise only)**
    - **Single Order Discount Limit**: Set a fixed Amount or the order Amount's Percentage. **(PLUS and Enterprise only)**
    - **Bonus point is valid for**: Set how many days points stay valid (0 means never expires).
    > This validity period also applies to bonus points issued with the registration gift.

   ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-設定會員紅利點數01.png){ .screenshot }

## How to issue bonus points

### A. Site-wide purchase rewards (automatically sent)

In the **Member Bonus Points (Vouchers)** section, set "Spend threshold" and "per points".

- **Example**: For every NT$100 spent, per 10 points.
- **Logic**: The system accrues points in proportion. Spend NT$1000 to earn 100 points; spend NT$999 to earn 90 points.

### B. Send to all members (store-wide) (all members)

1. On the same page, click **Send vouchers to every member** to expand the fields.
2. Enter the points, validity period, and issuance name, then click **Confirm Add**.
3. The system imports the points into every registered member account.

![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數2-1.png){ .screenshot }

### C. send manually (specific members)

> Go to **Members All Members**.

=== "Send to one member"

    Open the member profile. In the "bonus points" field, click **Add bonus points**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數-4.png){ .screenshot }

=== "Send to a filtered group"

    Use filters to select a group (for example, VIP members), then add points in bulk.

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數-7.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數-8.png){ .screenshot }

    </div>


### D. EXCEL bulk send

!!! info "Notes"
    - This feature is **Enterprise** only.
    - If **external bonus** is on, bulk import is not available. Issue bonuses from your external mid-office system instead.


1. Download the template and fill in the fields as specified.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-紅利優惠券-批次發送紅利點數01.png){ .screenshot }

2. Enter the member Email or mobile number, campaign name, points to issue, and the other template fields.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EXCEL範本-批次發送紅利點數01.png){ .screenshot }

3. Upload the Excel file. The system emails the import result and issues points to the listed members as soon as the import succeeds.



## Set a product-level redemption cap

You can set a bonus redemption cap on each product. **To allow bonus redemption on that product, enter the redeemable points value**. **If this field stays at 0, the product does not allow bonus redemption**.

1. Go to **Products All Products** and open the product.
2. Open **Variants** and enter the max redeemable "points" in **bonus redemption**.
> **How the system decides**: When both a store-wide redemption cap and a product redemption cap exist, the system uses the **stricter** (lower) cap.

!!! tip "How to bulk-edit this field"
    [Bulk-export the product Excel sheet](../../products/bulk-operations/batch-update-product-descriptions-shipping.en.md#匯出商品-excel-表格), edit the `商品款式紅利最高折抵` column, then [import the Excel file](../../products/bulk-operations/batch-update-product-descriptions-shipping.en.md#上傳-excel-檔案) to finish the bulk edit.

=== "Admin settings"

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明02.png){ .screenshot }

=== "Storefront checkout"

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/設定紅利購物金說明03.png){ .screenshot }

## Auto-apply bonus at checkout

The system **enables** Auto-apply Member Bonus on Checkout by default. Choose whether checkout auto-fills the member's current usable bonus points cap.

1. Go to **Payment and Logistics Checkout Page & Logistics**.
2. Expand **Shopping Cart Settings** and find **Auto-apply Member Bonus on Checkout**.
3. Choose the setting you need:
    - **Enable Auto-apply Member Bonus on Checkout** (system default): Checkout auto-fills the member's usable bonus cap. Members can still enter a different amount.
    - **Disable Auto-apply Member Bonus on Checkout**: After Close, checkout does not auto-fill usable member bonus. The "Enter member bonus redemption points" field defaults to `0`. Members must type the points they want to use.

=== "Admin settings"

    ![](../assets/images/EC-後台-金物流-結帳頁物流設定-結帳頁自動帶入紅利01.png){ .screenshot }

=== "Storefront checkout"

    ![](../assets/images/EC-前台-結帳頁-會員紅利折抵欄位01.png){ .screenshot }

## How the system works

### Discount order

bonus points are applied **after all other discounts**. The system calculates promotions and coupon first, then deducts bonus points last.

### Cancellations

Merchants or customers can cancel an order before it ships. Bonus handling for canceled orders:

| Scenario | Bonus used on the order | Bonus earned from the purchase |
| :--- | :--- | :--- |
| **Cancel order** | Returned to the customer account automatically | If the order is not yet Closed, no reward is issued<br>If the order is Closed and the points were used, the points are not clawed back |


### Returns

Customize how bonuses are handled on returns:

| Scenario | Bonus used on the order | Bonus earned from the purchase |
| ---- | -------------- | ------------- |
| **Returned order** | Choose whether to return the points (default: do not return) | Do not issue purchase bonus when Closed |
| **Partial return** | Choose whether to return the points (default: do not return) | Choose whether to issue points (default: do not issue) |

!!! info "Available plans"
    - The return-points toggle for **returned orders** is **PLUS and Enterprise** only.
    - The return-points toggle for **partial returns** is **Enterprise** only.

> Go to **Payment and Logistics Checkout Page & Logistics > Orders Settings** to set this.

![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明17.png){ .screenshot }

!!! warning "Linked-warehouse merchants"
    Auto-return is not supported for linked-warehouse merchants. Returns on linked-warehouse orders never auto-return or issue bonus points.

### Returns after the order is Closed

If the return happens after the order is Closed, earned bonus points are **not deducted from the member account automatically**.

!!! tip "Recommended action"
    - Go to the member profile and [manually Remove that bonus](../../members/manage-member-profiles.en.md#1-紅利點數派發與管理).
    - Wait until the return window has passed and no return is needed, then click **Close Order** so issuance stays accurate. See [coupon / bonus crediting rules](../references/coupon-and-bonus-credit-rules.en.md) for the full Closed and return-status rules.



## Manage and analyze

### Look up bonus points

=== "Admin"

    Look up, add, or Remove a member's bonus points in admin.

    1. Go to **Members All Members**, search for the member, and open the profile.
    2. On the profile, view the **bonus points list**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明08.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明09.png){ .screenshot }

=== "Member"

    Members can view their points history on the storefront.

    1. Go to **My Account bonus points**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/08/購買指定商品送紅利13.png){ .screenshot }

### bonus points conversion rate

The system converts and displays the matching Amount from the rate you set:

#### Notes

- This feature is **Enterprise** only.
- The conversion rate applies only during "bonus redemption".
- Changing the rate immediately changes the cash value of bonus points already in customer accounts.

#### Storefront examples

- **Member center**: Shows available points and the approximate Amount value.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明10.png){ .screenshot }

- **Product page**: Shows the max redeemable points for that product and the approximate Amount value.

    > When you set the product "bonus points redemption cap" in admin, enter **points**, not Amount.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明11.png){ .screenshot }

- **Checkout**: Shows redeemed points and the Amount actually deducted.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明12.png){ .screenshot }


#### Report export columns

[Export order report](../../orders/reports/export-order-report.en.md) includes detailed bonus redemption and Amount conversion columns:

- **bonus redemption**: Unit is bonus points.
- **Total product bonus discount Amount**: bonus points converted at the rate to the actual redeemed Amount.

![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明13.png){ .screenshot }



### View and export reports

1. Go to **Analytics Marketing Campaign Analytics > Bonus Analytics**.

2. Click **Export Bonus Chart**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明14.png){ .screenshot }

3. The system emails the Excel report to the admin inbox.

    > The export range cannot exceed 180 days.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明16.png){ .screenshot }


## More actions

<div class="grid cards" markdown>

- :lucide-bell-ring:{ .lg }
  [__Set bonus points expiry notifications__](../purchase-restrictions/coupon-and-bonus-points-expiry-notification.en.md)
  Set bonus points expiry reminders so customers return to the storefront and redeem points before they expire.

</div>