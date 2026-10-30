---
title: "Cross-Border E-Commerce Refund Process"
description: "After an order completes the return process, the final step is refunding the shopper. The system triggers the refund automatically or manually, depending on your store plan and the shopper's payment method."
created: 2026-03-05 00:00
last_modified: 2026-05-28 14:48
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
  - 訂單
sites:
  - US
  - JP
  - SG
  - MY
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - Pro
  - Business
plan_options: []
cyb_extensions: []
intents:
  - 確認退款判定邏輯
  - 執行自動退款流程
features:
  - 訂單退款
  - 金流退刷
prerequisites:
  - 需先完成「商家執行訂單退貨流程」並將狀態切換為已退貨
related: []
tags:
  - "Refund Process"
  - "After-Sales Service"
  - "Automatic Refunds"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 後台 > 訂單 > 所有訂單
  - 前台 > 會員中心 > 訂單查詢
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=30948
permalink: "https://help.cyberbiz.io/ec/orders/cross-border-refund-process/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# Cross-Border E-Commerce Refund Process

After an order completes the return process, the last step is refunding the shopper. Depending on your site plan and the shopper's payment method, the refund is triggered automatically or manually.
{ .subtitle }

[:lucide-layers:{ title="Available Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (North America / Japan / Southeast Asia Sites)
[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | Pro / Business<br>
[:lucide-layers:{ title="Available Products" }](../../resources/conventions#適用產品) | Local Edition (Malaysia / Australia Sites)
{ .doc-badge }


!!! info "Key Refund Rules"
    - **Request limit**: Each order accepts only **one** refund request.
    - **When refunds are available**: Orders paid today can't be refunded right away. You can refund them after the system settles them the **next day**.

## Step 1: Determine the Refund Method

Choose the refund method based on your site plan and the order's payment method.


=== "North America Site"

    | Payment Provider | Payment Method | Refund Process | Refund Deadline | After the Deadline |
    | ------- | ------- | ------- | -------- | ---------------- |
    | CYBERBIZ PAYMENTS | Credit card | Automatic system refund | No deadline | - |
    | CYBERBIZ PAYMENTS | Apple Pay | Automatic system refund | No deadline | - |
    | CYBERBIZ PAYMENTS | Google Pay | Automatic system refund	| No deadline | - |
    | CYBERBIZ PAYMENTS | PayPal | Automatic system refund	| Within 180 days of payment | Process the refund yourself |


=== "Japan Site (Taiwan to Japan)"

    | Payment Provider | Payment Method | Refund Process | Refund Deadline | After the Deadline |
    | ------- | ------- | ------- | -------- | ---------------- |
    | CYBERBIZ PAYMENTS | Credit card | Automatic system refund | Within 365 days of payment | Transfer the refund yourself |
    | CYBERBIZ PAYMENTS	| Pay-Easy | Offline payment: You process the refund yourself<br>Other payment methods: Automatic system refund | No deadline | - |


=== "Japan to Taiwan"

    | Payment Provider | Payment Method | Refund Process | Refund Deadline | After the Deadline |
    | ------- | ------- | ------- | -------- | ---------------- |
    | Softbank | Credit card | Automatic system refund | Within 365 days of payment | Transfer the refund yourself |


=== "Southeast Asia Site"

    | Payment Provider | Payment Method | Refund Process | Refund Deadline | After the Deadline |
    | ------- | ------- | ------- | -------- | ---------------- |
    | CYBERBIZ PAYMENTS | Credit card | Automatic system refund | No deadline | - |
    | Fiuu(Malaysia) | FPX | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |
    | | BOOST | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |
    | | GrabPay | Automatic system refund | Within 90 days of payment | Refund yourself in the Fiuu wallet |
    | | Touch N Go | Automatic system refund | Within 30 days of payment | Refund yourself in the Fiuu wallet |
    | | ShoppePay | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |
    | | DuitNow QR | Automatic system refund | Within 60 days of payment | Refund yourself in the Fiuu wallet |
    | | Fiuu Cash(7-11) | Refund yourself | - | - |
    | Fiuu(Singapore) | PayNow | Automatic system refund | Within 30 days of payment | Refund yourself in the Fiuu wallet |
    | | GrabPay SG | Automatic system refund | Within 90 days of payment | Refund yourself in the Fiuu wallet |
    | | ShopeePay SG | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |

=== "Malaysia Local Edition"

    | Payment Provider | Payment Method | Refund Process | Refund Deadline | After the Deadline |
    | ------- | ------- | ------- | -------- | ---------------- |
    | Fiuu(Malaysia) | Credit card | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |
    | | FPX | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |
    | | BOOST | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |
    | | GrabPay | Automatic system refund | Within 90 days of payment | Refund yourself in the Fiuu wallet |
    | | Touch N Go | Automatic system refund | Within 30 days of payment | Refund yourself in the Fiuu wallet |
    | | ShoppePay | Automatic system refund | Within 180 days of payment | Refund yourself in the Fiuu wallet |
    | | DuitNow QR | Automatic system refund | Within 60 days of payment | Refund yourself in the Fiuu wallet |
    | | Fiuu Cash(7-11) | Refund yourself | - | - |


=== "Australia Local Edition"

    | Payment Provider | Payment Method | Refund Process | Refund Deadline | After the Deadline |
    | ------- | ------- | ------- | -------- | ---------------- |
    | Airwallex | Credit card | Automatic system refund | No deadline | - |
    | | Apple Pay | Automatic system refund | No deadline | - |
    | | Google Pay | Automatic system refund | No deadline | - |

## Step 2: Process the Refund

The refund process is triggered automatically when the **Return Status** changes.

=== "Automatic System Refund"

    1. Change the order's `Return Status` to **Returned** or **Partially Returned**.
    2. The system automatically updates `Payment Status` to **Pending Refund** or **Pending Partial Refund**.
        ![](../../assets/images/EC-後台-訂單-所有訂單-訂單顯示待退款待部分退款01.en.png)
    3. The system immediately sends a refund request to the payment provider.
    4. After the refund succeeds, `Payment Status` automatically updates to **Refunded** or **Partially Refunded**.
        ![](../../assets/images/EC-後台-訂單-所有訂單-訂單顯示已退款01.en.png)

=== "Manual Transfer / Fiuu Wallet Refund"

    1. Change the order's `Return Status` to **Returned** or **Partially Returned**.
    2. The system automatically updates `Payment Status` to **Pending Refund** or **Pending Partial Refund**.
    3. 
        - **Manual transfer**: Contact the shopper and complete the offline transfer.
        - **Fiuu wallet refund**: Go to the Fiuu dashboard and complete the refund.
    4. Return to the admin and select the order.
    5. Click **Actions...** in the upper right > change the payment status to **Refunded** or **Partially Refunded**.

    ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退款01.en.png)
