---
title: "Cross-Border E-Commerce Return Process"
description: "When a member requests a return or you need to start a return manually, you can arrange reverse logistics and review returns in the admin."
created: 2026-02-23 00:00
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
  - 發送逆物流代碼
  - 執行退貨審核
  - 處理部分退貨
features:
  - 訂單退貨
  - 逆物流
prerequisites:
  - 建議先完成「設定與管理會員退貨申請」以利會員主動提交
related:
  - ec/orders/cross-border-refund-process/
tags:
  - "After-Sales Service"
  - "Reverse Logistics"
  - "Full Returns"
  - "Partial Returns"
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
permalink: "https://help.cyberbiz.io/ec/orders/cross-border-return-process/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# Cross-Border E-Commerce Return Process

When a member requests a return or you need to start a return manually, you can arrange reverse logistics and review returns in the admin.
{ .subtitle }

[:lucide-layers:{ title="Available Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (North America / Japan / Southeast Asia Sites)
[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }


!!! info "Key Rules"
    - **Request limit**: Each order accepts only **one** return and refund request. After a partial return is complete, the remaining items in the order can't be returned.
    - **Bonus points and coupons**: The system **doesn't automatically return** points or coupons used on the order, and **doesn't automatically deduct** points earned from the order. To change them, adjust them manually on the **member details page**.
    - **Profit sharing**: Profit sharing is calculated as soon as an order reaches **Completed**. Later returns **don't affect** profit sharing records already created.


## Step 1: Start the Return and Arrange Reverse Logistics

Depending on who starts the return, the **Return Status** in the order list shows differently:

- **Member request**: Automatically shows `Return Requested`.
- **Started by you**: Initially shows `No Return Needed`.

Steps:

1. Go to **Orders > All Orders**.
2. Select the orders, and then click **Returning** > **Reviewing Return**.

![](../../assets/images/EC-後台-訂單-所有訂單-操作退貨審查01.en.png)


### Amazon Reverse Logistics Pickup (Amazon FBA Orders Only)

If the order shipped with Amazon FBA, you can create a reverse logistics shipping label through Amazon. Follow the steps below.

1. Sign in to Amazon Seller Central and go to **Orders > Manage Orders**.
    ![](../../assets/images/Amazon-後台-申請Amazon逆物流01.en.jpg)
2. Click the order.
    ![](../../assets/images/Amazon-後台-申請Amazon逆物流02.en.jpg)
3. Select the **Returns** tab, and select the items to return in the **Create Returns** area.
    ![](../../assets/images/Amazon-後台-申請Amazon逆物流03.en.jpg)
4. In the **Returns** area, click the **RMA ID link**.
    ![](../../assets/images/Amazon-後台-申請Amazon逆物流04.en.jpg)
5. Click **Print label & instructions**, and save the **RMA label** and **Shipping Label**.
    ![](../../assets/images/Amazon-後台-申請Amazon逆物流05.en.jpg)
6. Give the **RMA label** and **Shipping Label** to the shopper, and ask them to stick both labels on the outside of the package and send it back.
7. After the Amazon warehouse receives the package, it inspects and restocks the items.







## Step 2: Review the Return


=== "Full Return"

    > Use Cases<br>
        - All items in the order must be returned<br>
        - The full order amount is refunded

    1. Go to **Orders > All Orders**.
    2. Select the orders, and then click **Reviewing Return** > **Returned**.
    3. After the status changes, continue with the [refund](cross-border-refund-process.md).

    ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)

=== "Partial Return"

    > Use Cases<br>
        - Only some items in the order are returned<br>
        - Part of the order amount is refunded

    1. Go to **Orders > All Orders**.
    2. Select the orders, click **Reviewing Return**, and then open the order details page.
    3. In the **Partial Refund** section, select the approved items and enter the refund quantities.
    4. Enter the **Refund Amount** (the system fills in the total at original prices, and you can adjust it manually).
    5. Click **Confirm Refund**. `Return Status` changes to `Partially Returned`.
    6. After the status changes, continue with the [refund](cross-border-refund-process.md).

    ![](../../assets/images/EC-後台-訂單-所有訂單-指定部分退款金額與數量.en.gif)

=== "Reject Return"

    > Use Cases<br>
        - The return doesn't meet your return criteria, such as damaged items or a passed deadline

    1. Go to **Orders > All Orders**.
    2. Select the orders, and then click **Reviewing Return** > **Return Refused**.
    3. The process ends here.

    ![](../../assets/images/EC-後台-訂單-所有訂單-操作已退貨拒絕退貨01.en.png)




## FAQ

??? quote "Why does the order status change automatically when I use reverse logistics?"
    With system-integrated reverse logistics, after the member hands the package to the carrier, the system receives the carrier's signal and automatically updates the status from `Returning` to `Reviewing Return`, so you can track progress.

??? quote "Do I refund shipping fees for partial returns?"
    It depends on your store policy. The refund amount the system fills in is only the total of the items' original prices. To refund part of the shipping fee, increase the refund amount manually. To deduct a refurbishing fee, decrease it manually.

??? quote "If I click the wrong option during return review, can I start over?"
    Each order can go through the return process only once. As soon as the status changes to **Returning**, the system treats the process as finished. Double-check before you click.

