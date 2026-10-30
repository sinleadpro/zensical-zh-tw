---
title: "Order Return and Refund Process"
description: "When a member requests a return or you need to start a return manually, you can arrange reverse logistics and review returns in the admin."
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
  - 金物流
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
  - 發送逆物流代碼
  - 執行退貨審核
  - 處理部分退貨
features:
  - 訂單退貨
  - 逆物流
prerequisites:
  - "設定與管理會員退貨申請"
related:
  - ec/payments-and-logistics/payments/order-settings/
  - wms/returns-and-vehicle-dispatch/
  - ec/orders/member-return-request-feature/
  - ec/orders/returns-refunds/cvs-c2b-return/
  - ec/orders/returns-refunds/7-11-c2c-return/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
  - ec/payments-and-logistics/setup-pelican-waybill-v2/
  - ec/payments-and-logistics/setup-hct-waybill-v2/
  - ec/orders/order-refund-process/
  - ec/orders/returns-refunds/cvs-unclaimed-order/
tags:
  - "After-Sales Service"
  - "Reverse Logistics"
  - "Full Returns"
  - "Partial Returns"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 結帳頁 & 物流設定
  - 訂單 > 所有訂單
  - 金物流 > XX 託運單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=200
  - https://www.cyberbiz.io/helpcenter/?p=5254
  - https://www.cyberbiz.io/helpcenter/?p=5259
  - https://www.cyberbiz.io/helpcenter/?p=6911
  - https://www.cyberbiz.io/helpcenter/?p=7016
  - https://www.cyberbiz.io/support/?p=1756
  - https://www.cyberbiz.io/support/?p=1758
  - https://www.cyberbiz.io/support/?p=51896
permalink: "https://help.cyberbiz.io/ec/orders/order-return-process/"
comments: false
search:
  exclude: false
icon: lucide/package-minus
hide: []
---
# Order Return and Refund Process

When a member requests a return or you need to start a return manually, you can arrange "reverse logistics" and "return review" in the admin.
{ .subtitle }


## Before You Start { #prerequisites-order-return }

### Refund Rules

- **Request limit**: Each order accepts **only one** return and refund request. If a partial return has been completed, the remaining items in the order can't be requested again.
- **Partial refunds**:
    - Installment orders can't use partial returns (refunds).
    - If the shopper paid today, partial returns can be processed starting the next day.
    - Each order accepts only one partial return request.

### Marketing Campaign Rules

- **Bonus points and coupons**:
    - The system **doesn't automatically return** points or coupons used in the order.

        !!! info "Return-Related Bonus Point Settings"
            **PLUS and Enterprise plans** can go to **Payment and Logistics > Checkout Page & Logistics** and manually set the bonus point refund policy in [**Order Cancellation and Return Bonus Point Settings**](../payments-and-logistics/payments/order-settings.md#operate-order-settings-return-bonus){ data-preview }.

    - If a return and refund is processed after the order is **Completed**, the bonus points earned from the order **aren't automatically deducted**. To change them, adjust them manually on the **member details page**.

- **Commissions**: Commissions are calculated once an order reaches **Completed**. Later returns **don't affect** commission records already created.

### Returns for Warehouse-Integrated Website Orders

If you use CYBERBIZ e-commerce warehousing, see [Returns and Pickup Dispatch](../../wms/returns-and-vehicle-dispatch.md) for the return process.

### Return Status Differences { #prerequisites-order-return-status }

Depending on who starts the return, the **Return Status** in the order list shows differently:

- **Member request**: Automatically shows `Return Requested`.
    - To let shoppers request returns on the storefront, see [Member Return Request Feature](member-return-request-feature.md).
- **Merchant-initiated**: Initially shows `No Return Needed`.

After checking the order's current status, follow the steps below for your return scenario.

## Step 1: Arrange Reverse Logistics { #operate-order-return-reverse }

### Notes

- Outbound and reverse logistics work independently, so they **don't need to use the same carrier**.

    > For example, if the original order was shipped by home delivery, you can still arrange a convenience store Return Service (C2B) for the return.

- After the return is collected through system reverse logistics, the order's **Return Status** changes to **Reviewing Return**.

### Reverse Logistics Options

=== "7-Eleven Return (C2B)"

    1. Go to **Orders > All Orders**.
    2. Select the orders and click **Send 7-Eleven Bulk Return Service Code (C2B) and Change Status to Returning**. The system texts the code to the member.

    !!! warning "Convenience Store Return Service Requirements"
        - **Available plans**: Expert PLUS and Enterprise.
        - **Supported logistics**: Only sites with **convenience store B2C** turned on. Not available for convenience store C2C.

    ![](../../assets/images/EC-訂單-所有訂單-發送7-11-c2c退貨便代碼.en.png)

    <div class="grid cards" markdown>

    - :lucide-dollar-sign:{ .lg }  
      [__Use Convenience Store Return Service C2B__](returns-refunds/cvs-c2b-return.md)  
      Set 7-Eleven Return Service fees, send codes, and follow the drop-off process.

    </div>


=== "7-Eleven Return (C2C)"

    1. Go to **Orders > All Orders**.
    2. Select the orders and click **Send 7-Eleven Store-to-Store Return Code (C2C) and Change Status to Returning**. The system texts the code to the member.

    ![](../../assets/images/EC-訂單-所有訂單-發送7-11-c2c退貨便代碼.en.png)

    <div class="grid cards" markdown>

    - :lucide-dollar-sign:{ .lg }  
      [__Use Convenience Store Return Service C2C__](returns-refunds/7-11-c2c-return.md)  
      Turn on 7-Eleven C2C returns, set the recipient, and send codes.

    </div>

=== "Home Delivery Reverse Logistics"

    1. Select the orders and click **Returning**.

        ![](../../assets/images/EC-訂單-所有訂單-更多操作-退貨中.en.png)

    2. Go to **Payment and Logistics > XX Shipping Labels**.
      > Choose the page for your carrier (EZCAT, Pelican Express, HCT Logistics): EZCAT Shipping Labels, Pelican Express, or HCT Logistics Shipping Labels.
    3. Enter the order number to create a reverse logistics tracking number.

        ![](../../assets/images/EC-後台-金物流-黑貓託運單-建立逆物流託運單01.en.png)

    <div class="grid cards" markdown>

    - :lucide-dollar-sign:{ .lg }  
      [__Create EZCAT Reverse Logistics__](../payments-and-logistics/setup-print-tcat-waybill-v2.md#ezcat-shipping-note-reverse)  
      Set EZCAT sender information, add tracking numbers, and create reverse logistics.

    - :lucide-dollar-sign:{ .lg }  
      [__Create Pelican Express Reverse Logistics__](../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-reverse)  
      Set Pelican Express sender information, add tracking numbers, and create reverse logistics.

    - :lucide-dollar-sign:{ .lg }  
      [__Create HCT Logistics Reverse Logistics__](../payments-and-logistics/setup-hct-waybill-v2.md#operate-hct-setup-reverse)  
      Set HCT Logistics sender information, add tracking numbers, and create reverse logistics.

    </div>

=== "Shopper Sends It Back"

    1. Select the orders and click **Returning**.

        ![](../../assets/images/EC-訂單-所有訂單-更多操作-退貨中.en.png)

    2. Contact the customer and ask them to send the returned items back themselves.

=== "No Reverse Logistics Pickup Needed"

    Select the orders and click **Returning**.

    ![](../../assets/images/EC-訂單-所有訂單-更多操作-退貨中.en.png)


## Step 2: Review the Return and Refund { #operate-order-return-review }

After you receive the package and check the items, choose a review result based on the situation.

=== "Full Return/Refund"

    Use this when all items in the order are returned.

    1. Go to **Orders > All Orders**.
    2. Select the orders and click **Reviewing Return** > **Returned**.

        !!! danger "Don't Click "Returned" for Partial Refunds"
            If you use **CYBERBIZ PAYMENTS** and the order qualifies for automatic refunds, clicking **Returned** makes the system issue a **full refund** automatically. To refund only part of the amount, don't click **Returned**. Click **Reviewing Return** instead, then go to the order details page to select the returned items and enter the refund amount.

            For details, see the **Partial Return/Refund** tab.

        ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)

    3. If CYBERBIZ refunds the order manually, fill in the **Manual Refund Information** using the refund details the customer provided.

        ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/CYBERBIZ-PAYMENTS-退貨退款09.png){ .small-image }

    4. After the return review, go to [Refund Methods and Operations](order-refund-process.md) to find and follow the refund process for your plan and the order's payment method.



=== "Partial Return/Refund"

    Use this when only some items in the order are returned.

    1. Go to **Orders > All Orders**.
    2. Select the orders, click **Reviewing Return**, and then open the order details page.

        !!! danger "Don't Click "Returned" for Partial Refunds"
            If you use **CYBERBIZ PAYMENTS** and the order qualifies for automatic refunds, clicking **Returned** makes the system issue a **full refund** automatically. To refund only part of the amount, don't click **Returned**. Click **Reviewing Return** instead, then go to the order details page to select the returned items and enter the refund amount.


    3. In the **Partial Refund** section, select the approved items and enter the **refund quantity** and **refund amount** (the system fills in the original price total, which you can change).

        > Make sure the **total refund amount** matches the approved refund amount, then click **Confirm Refund**.

        ![](../../assets/images/EC-後台-訂單-所有訂單-指定部分退款金額與數量.en.gif)

    4. If CYBERBIZ refunds the order manually, fill in the **Manual Refund Information** using the refund details the customer provided.

        ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/CYBERBIZ-PAYMENTS-退貨退款09.png){ .small-image }

    5. Click **Confirm**, and the `Return Status` changes to `Partially Returned`.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/部分退貨退款08.png){ .small-image }

    6. After the return review, go to [Refund Methods and Operations](order-refund-process.md) to find and follow the refund process for your plan and the order's payment method.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/部分退貨退款09.png){ .small-image }





=== "Reject Return/Refund"

    Use this when items don't meet return standards, such as damaged items or returns past the deadline.

    1. Go to **Orders > All Orders**.
    2. Select the orders and click **Reviewing Return** > **Return Refused**.
    3. The process ends here.

    ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)




## FAQ { #faq-order-return }

??? quote "Why does the order status change automatically when I use reverse logistics?"
    With system-integrated reverse logistics, after the member hands the package to the carrier, the system receives the carrier's update and automatically changes the status from `Returning` to `Reviewing Return`, so you can track progress.

??? quote "If I click the wrong return review option, can I start over?"
    Each order can go through the return process only once. Once the status changes to **Returning**, the system treats the process as finished. Double-check before you click.

---

## Next Steps { #next-steps-order-return }

<div class="grid cards" markdown>

- :lucide-dollar-sign:{ .lg }  
  [__Refund Methods and Operations__](order-refund-process.md)<br>
  Learn how to complete the final payout or card refund for each payment channel.

- :lucide-clipboard-check:{ .lg }  
  [__Manage Unclaimed Convenience Store Orders__](../orders/returns-refunds/cvs-unclaimed-order.md)
  Learn the reconciliation process for automatic returns caused by packages not picked up.

</div>
