---
title: "Store-wide Discounts"
description: "Apply one Discount to every product in the store. This promotion supports both EC and POS, and depending on your plan you can enable it online, offline, or across all channels."
created: 2026-06-24 16:30
last_modified: 2026-06-24 16:30
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
    - EC
    - POS
modules: 
    - Marketing
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
    - 了解全館折扣規格
    - 搜尋與篩選全館折扣活動
    - 自定義全館折扣列表欄位
    - 建立全館折扣活動
    - 編輯全館折扣活動
    - 查看全館折扣編輯紀錄
features: 
    - "Store-wide Discounts"
    - 折扣門檻
    - 折扣累積
    - 優惠券折扣
    - 編輯紀錄
    - 活動通路設定
prerequisites: []
related: []
tags: 
    - 全館折扣
    - 行銷活動
    - Promotions
    - EC
    - POS
acoiv: configure
apis: []
devices: []
ui_components: 
    - 編輯欄位
    - 篩選
    - 搜尋
    - 編輯紀錄
paths: 
    - 行銷活動 > 全館折扣
layouts: []
wp_url:
    - https://www.cyberbiz.io/helpcenter/?p=1165
    - https://www.cyberbiz.io/support/?p=30011
permalink: "https://help.cyberbiz.io/ec/marketing/discounts/storewide-discounts-v2.en/"
comments: false
search:
  exclude: false
icon: lucide/percent
hide: []
---
# New Store-wide Discounts
Apply one Discount to every product in the store. This promotion supports both EC and POS, and depending on your plan you can enable it online, offline, or across all channels.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | Online Store / Smart POS
[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | Enterprise
{ .doc-badge }

!!! tip "New Interface"
    **Store-wide Discounts** has a new interface, currently available only on the **Enterprise** plan. It will roll out to other plans over time.

## Store-wide Discounts Specs

A store-wide promotion is a specific promotion in the marketing module. Once set up, it applies one Discount to **every product in the store**.

This promotion supports both EC and POS. The channels you can choose depend on your plan:


| Plan | Channel |
| ------- | ------- |
| **EC only (online store)** | Online store only |
| **POS only (physical stores)** | Physical store POS only |
| **EC + POS** | 可指定活動通路<br>- **Online**：僅限官方購物網站使用<br>- **Offline**：僅限實體門市 POS 端使用<br>- **All channels**: The offer is active online and offline at the same time |


## Manage The List

### Search

Go to **Marketing > Shop-wide Discount** to search for a promotion by name.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-搜尋01.png){ .screenshot }

### Filter

You can filter promotions by:


*   **Channel**: Online, Offline, All Channels

    > Available only for stores with both EC and POS. EC-only or POS-only stores don't Display this filter.

*   **Status**: Scheduled, Active, Ended

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-篩選01.png){ .screenshot }

### Customize List Columns

You can adjust the list columns and their order to suit how you work.

**How to**

1.  Click **Edit Columns** on the right.
2.  In the menu, select the columns to Display and clear the ones you don't need to Display.
3.  Click :lucide-grip-vertical: and drag to reorder columns.
4.  The list updates right away to Display your selections.

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯列表欄位01.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯列表欄位02.png){ .screenshot }

    </div>


## Create Store-wide Discounts

### Step 1: Fill In Basic Settings

Go to **Marketing > Shop-wide Discount** and fill in these fields:

*   Discount promotion name
*   Period: Choose **No End Date** or **Set Period**
*   Channel: If your store has both EC and POS, choose the Channel for the promotion.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-基本設定01.png){ .screenshot }

### Step 2: Fill In Discount Settings

Set the fields for the **Discount Type** you chose:

=== "Amount"

    *   **Threshold**: Enter the minimum spend that triggers the Discount.
    *   **Discount Amount**: Set the discount amount.
    *   **Accumulate Discount**: Choose whether the Discount repeats each time the threshold is reached again.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-金額設定01.png){ .screenshot }

=== "Percentage"

    *   **Threshold**: Enter the minimum spend that triggers the Discount.
    *   **Discount Percentage**: Set the Discount percentage.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-百分比設定01.png){ .screenshot }

=== "coupon"

    *   **Threshold**: Enter the minimum spend to get the coupon.
    *   **coupon Amount**: Enter the coupon discount amount.
    *   **Usage Days**: Set how long the coupon stays valid.
    *   **Coupon Usage Threshold**: The order amount needed to apply the coupon at checkout.
    *   **Bind Product Tags**: Only products with the specified tags can use the coupon.
    *   **Campaign Combination Restrictions**: Set whether this coupon can be used with other promotions.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-優惠券設定01.png){ .screenshot }




## Edit Store-wide Discounts

You can edit promotions you've created. What you can edit depends on the **promotion Status**:


| Promotion Status | Edit Columns |
| ------- | ---------- |
| **Scheduled** | All fields |
| **Active** | - Discount Name<br>- End time `註一`<br>- coupon valid days `註二` |

Click a promotion name to open the edit page. Before making changes, check the promotion's current Status and which fields you can edit.
![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯活動01.png){ .screenshot }

- `註一`:
    - The end time can't be earlier than the time you save the edit.
    - If you chose **No End Date** when creating the promotion, you can't edit the Period later.
    - If you chose **Specified Period** when creating the promotion, you can edit the end time.
- `註二`: This field is editable only when the Discount Type is **coupon**.


## View Edit History

You can see the edit history at the bottom of the promotion edit page. Whether a record is created depends on the promotion Status:

| Promotion Status | Edit History Recorded |
| -------- | -------------- |
| Scheduled | ✕ |
| Active | ✓ |


Changes to scheduled promotions aren't recorded. Changes to active promotions are kept for reference.
![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯紀錄01.png){ .screenshot }


## Remaining Amount Reminder At Checkout

!!! info "Before You Start"
    - **Plan**: This feature is available only on the **Enterprise** plan.
    - **Supported promotion types**: The system can Display reminders for **Amount** and **Percentage** store-wide promotions. It can't Display them for the **coupon** type.

At checkout, customers can see in the cart how much more they need to spend to qualify for the store-wide promotion.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-結帳頁-未達全館活動優惠差額01.png){ .screenshot }