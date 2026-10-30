---
title: "Refund Methods and Operations"
description: "After an order completes the return process, the final step is refunding the shopper. The system starts an automatic or manual refund, depending on your payment service and the shopper's payment method."
created: 2026-02-23 00:00
last_modified: 2026-10-02 11:00
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
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 確認退款判定邏輯
  - 執行自動退款
  - 執行人工退款流程
  - 處理發票作廢與折讓
features:
  - 訂單退款
  - CYBERBIZ PAYMENTS
  - 金流退刷
prerequisites:
  - "商家執行訂單退貨流程"
related: []
tags:
  - "Refund Process"
  - "After-Sales Service"
  - "Automatic Refunds"
  - "Manual Refunds"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=200
  - https://www.cyberbiz.io/helpcenter/?p=5254
  - https://www.cyberbiz.io/helpcenter/?p=5259
  - https://www.cyberbiz.io/helpcenter/?p=6911
  - https://www.cyberbiz.io/helpcenter/?p=7016
  - https://www.cyberbiz.io/support/?p=1756
  - https://www.cyberbiz.io/support/?p=1758
  - https://www.cyberbiz.io/support/?p=51911
permalink: "https://help.cyberbiz.io/ec/orders/order-refund-process/"
comments: false
search:
  exclude: false
icon: lucide/coins
hide: []
---
# Refund Methods and Operations

After an order completes the return process, the last step is refunding the shopper. Depending on your payment service and the shopper's payment method, the system starts an automatic or manual refund process.
{ .subtitle }


## Before You Start { #prerequisites-order-refund }

- **Request limit**: Each order accepts only **one** refund request.
- **Payment timing**:
    - **ECPay credit cards**: Orders paid today can't be refunded right away. You can refund them after the system settles them the **next day**.
- **Invoices**:
    - **Issued by CYBERBIZ**: After the refund is complete, the system automatically creates an invoice allowance.
    - **Others (ECPay/Sing Yi Hsin)**: Based on the refund date, the invoice is **voided** before the 5th of the month and an **allowance** is issued after the 5th.

## Refund Methods { #specs-order-refund }


=== "Enterprise/PLUS"

    | Payment Method | Automatic System Refund | Manual System Refund | Notes |
    | ------- | ----------- | ----------- | -----|
    | **Credit card** | ✓ | After 180 days from payment | |
    | **Apple Pay<br>Google Pay<br>UnionPay** | ✓ | ✕ | |
    | **AFTEE** | ✓ | ✕ | Automatically refunded to the AFTEE account |
    | **Virtual ATM<br>Convenience Store Barcode<br>Convenience Store Payment Code<br>Cash on Delivery** | ✕ | ✓ | If the member hasn't provided account information, ask the member for it first |
    | **LINE Pay** | ✓ | **✕** | :lucide-triangle-alert: After **60 days** from payment, refunds can't go through the payment provider, and you need to **transfer the refund yourself** to the shopper |
    | **PayPal** | ✓ | **✕** | :lucide-triangle-alert: After **180 days** from payment, refunds can't go through the payment provider, and you need to **transfer the refund yourself** to the shopper |
    | **JKOPAY** | ✓ | **✕** | JKOPAY co-branded card: refunded to the card<br>Bank account debit: refunded to the JKOPAY account<hr>:lucide-triangle-alert: More than **180 days** after payment, refunds can't go through the payment provider, and you need to **transfer the refund yourself** to the shopper |
    | **iPASS** | ✓ | **✕** | :lucide-triangle-alert: After **60 days** from payment, refunds can't go through the payment provider, and you need to **transfer the refund yourself** to the shopper |

    !!! warning "**Manual System Refund** Important Notes"
        - **Required**: Ask the customer for their refund account details, and CYBERBIZ processes the refund manually.
        - **Processing fee**: Each manual refund has an accounting processing fee of **NT$30**.

=== "Standard Plan with CYBERBIZ PAYMENTS"

    | Payment Method | Automatic System Refund | **Merchant Transfer :lucide-triangle-alert:** | Notes |
    | ------- | ----------- | ----------- | -----|
    | **Credit card** | ✓ | After 180 days from payment | |
    | **Apple Pay<br>Google Pay<br>UnionPay** | ✓ | ✕ | |
    | **AFTEE** | ✓ | ✕ | Automatically refunded to the AFTEE account |
    | **Virtual ATM<br>Convenience Store Barcode<br>Convenience Store Payment Code<br>Cash on Delivery** | ✕ | ✓ | If the member hasn't provided account information, ask the member for it first |
    | **LINE Pay** | ✓ | After 60 days from payment |  |
    | **PayPal** | ✓ | After 180 days from payment | |
    | **JKOPAY** | ✓ | After 180 days from payment | JKOPAY co-branded card: Refunded directly to the card<br>Bank account debit: Refunded to the JKOPAY account |
    | **iPASS** | ✓ | After 60 days from payment | |


=== "Standard Plan without CYBERBIZ PAYMENTS"

    | Payment Method | Payment Provider Dashboard | Merchant Transfer | Notes |
    | ------- | ---------- | ------- | --- |
    | **Credit card** | ✓ | ✕ | |
    | **Virtual ATM<br>Convenience Store Barcode<br>Convenience Store Payment Code<br>Cash on Delivery** | ✕ | ✓ |
    | **LINE Pay** | ✓ | ✕ | |
    | **PayPal** | ✓ | ✕ |  |
    | **JKOPAY** | ✓ | ✕ | |
    | **iPASS** | ✓ | ✕ | |


## Refund Process { #operate-order-refund }

Depending on the order's refund method, the refund is completed automatically or manually:

=== "Automatic System Refund"

    1. Change the order's `Return Status` to **Returned** or **Partially Returned**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)

    2. The system automatically updates `Payment Status` to **Pending Refund** or **Pending Partial Refund**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-訂單顯示待退款待部分退款01.en.png)

    3. Wait for the system to complete the payment refund.
    4. After the refund succeeds, `Payment Status` automatically updates to **Refunded** or **Partially Refunded**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-訂單顯示已退款01.en.png)


=== "Manual System Refund"

    1. Change the order's `Return Status` to **Returned** or **Partially Returned**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)

    2. The system automatically updates `Payment Status` to **Pending Refund** or **Pending Partial Refund**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-訂單顯示待退款待部分退款01.en.png)

    3. The CYBERBIZ finance team completes the payout within **7–10 business days**.
    4. After the payout, `Payment Status` automatically updates to **Refunded** or **Partially Refunded**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-訂單顯示已退款01.en.png)

    !!! warning "Manual Refund Processing Fee"
        If CYBERBIZ processes the refund manually for you, an accounting processing fee of **NT$30** is charged per refund.


=== "Payment Provider Dashboard"

    1. Change the order's `Return Status` to **Returned**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)

    2. The system automatically updates `Payment Status` to **Pending Refund**.
    3. Go to the payment provider's dashboard and complete the refund.
    4. Return to the admin and select the order.
    5. Click **Select Action** in the upper right > change the payment status to **Refunded**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退款01.en.png)

=== "Merchant Transfer"

    1. Change the order's `Return Status` to **Returned**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)

    2. The system automatically updates `Payment Status` to **Pending Refund**.
    3. Contact the shopper and complete the offline transfer.
    4. Return to the admin and select the order.
    5. Click **Select Action** in the upper right > change the payment status to **Refunded**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退款01.en.png)


## FAQ { #faq-order-refund }

??? quote "Why does the shopper say they didn't get the money after a credit card refund?"
    Credit card refunds usually take **7–14 business days** to appear on the shopper's credit card statement. If the refund crosses the statement closing date, the shopper may need to wait for next month's statement to see the charge and refund offset.

??? quote "What happens if my payment account balance is too low?"
    If your ECPay or third-party payment account balance can't cover the refund, the refund request fails. Top up the balance in the payment provider's dashboard first, or use **Merchant Transfer** and update the status manually.

??? quote "How is the refund amount calculated for returns?"
    It depends on the return type: a full return refunds the whole order amount, and a partial return refunds the approved amount you entered during **Reviewing Return**.

## More Tasks { #next-steps-order-refund }

<div class="grid cards" markdown>

- :lucide-package-minus:{ .lg }
  [__Process Order Returns and Refunds__](order-return-process.md)
  Learn how to start a return in the admin and complete a full or partial refund.

</div>

