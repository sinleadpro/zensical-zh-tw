---
title: "Whole-Order Discounts"
description: "Store staff can flexibly adjust prices for an entire order at checkout, while administrators control staff access and track notes for each manual adjustment."
created: 2026-04-27 15:00
last_modified: 2026-04-27 15:00
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
    - POS
modules:
  - 結帳
  - 訂單
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
    - 設定 POS 整筆訂單折扣
    - POS 前台彈性改價
    - 管理 POS 店員改價權限
features: 
    - POS 整筆訂單折扣
    - 店長改價權限
    - 改價備註記錄
prerequisites: []
related:
  - ec/orders/reports/export-order-report/
  - pos/store/staff-permissions-and-account-management/
tags: 
    - POS_Discounts
    - Whole_Order_Pricing
    - Permission_Management
    - Checkout_Discounts
acoiv: operation
apis: []
devices: 
    - desktop
    - tablet
ui_components: 
    - 新增整筆訂單折扣
    - 改價備註
    - POS 權限管理
paths:
  - 訂單 > 訂單報表匯出
layouts: []
wp_url: 
    - https://www.cyberbiz.io/support/?p=35401
permalink: "https://help.cyberbiz.io/pos/check/storewide-order-discounts/"
comments: false
search:
  exclude: false
icon: lucide/badge-percent
hide: []
---

# Whole-Order Discounts
Store staff can flexibly adjust prices for an entire order during checkout. Administrators can decide whether to grant this permission to regular staff, and can track the notes recorded for each manual price adjustment.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **In-Store Special Offers**: When a customer meets special promotion conditions or a loyal customer visits the store, staff can manually apply a discount.
    - **Rounding Off**: When the checkout total has a remainder, use the whole-order price adjustment feature to round it off.
    - **Manager-Approved Pricing**: When a staff member does not have permission, a store manager can step in and enter the discount to tighten control over price adjustments.



## Usage Notes { #prerequisites-order-discount }

- **Permission Restrictions**: This feature is available only to users with the **Store Manager** role by default. Regular staff must be granted permission by an administrator in the back office.
- **Adjustment Records**: Every whole-order discount requires an **Adjustment Note**. The system saves the note for future reconciliation and auditing.
- **Quick Note Selection**: The system automatically saves the 5 most recent adjustment notes so staff can select them quickly.


## Workflow { #operate-order-discount }

### Task 1: Apply a Whole-Order Discount on the POS Front End { #operate-order-discount-task-a-pos }

During checkout, staff can adjust the cart total at any time.

1. On the **Checkout** page of the POS front end, choose where to make the adjustment based on the adjustment type:
    - **Whole-Order Price Adjustment**: Select an item, open the dropdown menu, and click the **Manager Price Adjustment** field.
    - **Item-Specific Price Adjustment**: Click **Add Whole-Order Discount** on the right side of the list.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS前台-整筆訂單折扣01.png){ .screenshot }

2. Select a discount type and enter a value:

    - **Frequently Used Discounts**: The system automatically records the 5 most recent discounts entered by staff so store personnel can apply them quickly.

    === "Amount"

        Enter the fixed amount to deduct.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台-結帳-整筆訂單折扣01.png){ .screenshot }

    === "Percentage"

        Enter the discount percentage (for example, enter 10 for 90% of list price).

        ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台-結帳-整筆訂單折扣01.png){ .screenshot }

3. Enter the reason for the adjustment in the **Adjustment Note** field (for example, rounding off or a store manager special offer).
4. Click **Confirm** to apply the discount.
    - To make changes, click the **Edit** icon next to the discount amount to reconfigure it.

!!! tip "How to Review Order Adjustment Records"
    To view records of manual price adjustments, log in to the back office, go to **Orders > [Order Data Export](../../ec/orders/reports/export-order-report.md)**, and select the **Whole-Order Discount** and **Whole-Order Discount Note** fields to export. You can then view the information.



### Task 2: Enable Staff Adjustment Permissions in the Back Office { #operate-order-discount-task-b-admin }

If you want regular staff to be able to make price adjustments, an administrator must complete the setup in the back office.

1. Log in to the CYBERBIZ back office and go to **POS > Authorization Management**.
2. Click **Set Role Permissions**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS前台-店長改價06.png){ .screenshot }

3. Select the job title or role of the target employee.
4. Find the **Whole-Order Discount** option and switch the toggle to `On`.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS前台-整筆訂單折扣06.png){ .screenshot }

5. Click **Update Role** to complete the authorization.

## More Actions { #next-steps-order-discount }

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__Staff Permissions and Account Management__](../store/staff-permissions-and-account-management.md)
    Learn the complete setup and management process for store staff feature permissions.

</div>
