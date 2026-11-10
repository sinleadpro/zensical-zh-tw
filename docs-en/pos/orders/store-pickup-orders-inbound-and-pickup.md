---
title: "Store Pickup Orders (Inbound/Pickup)"
description: "Learn how to handle inbound arrivals, customer pickups, and overdue orders at the POS front end for website orders, enabling OMO operations where orders are placed online and picked up in store."
created: 2026-04-27 14:15
last_modified: 2026-05-28 14:48
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
  - 訂單
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 處理門市取貨到店
  - 辦理客戶到店取貨
  - 處理逾期未取訂單
features:
  - POS 門市取貨
  - 下載到店條碼
  - 包裹入庫
  - 會員條碼取貨
prerequisites:
  - ec/orders/store-pickup-orders/
related:
  - ec/orders/store-pickup-orders/
  - pos/store/pos-store-pickup-staff-commission/
  - ec/orders/order-return-process/
  - ec/orders/returns-refunds/cvs-c2b-return/
  - ec/orders/returns-refunds/7-11-c2c-return/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
  - ec/payments-and-logistics/setup-pelican-waybill-v2/
  - ec/payments-and-logistics/setup-hct-waybill-v2/
  - pos/inventory/inbound-orders/
tags:
  - "POS Store Pickup"
  - "Store Arrival Inbound"
  - "Customer Pickup"
  - "Overdue Handling"
acoiv: operation
apis: []
devices:
  - tablet
  - desktop
ui_components:
  - 門市取貨訂單
  - 商品到店入庫
  - 客戶到店取貨
  - 申請退貨
paths:
  - 訂單 > 所有訂單
  - 金物流 > 結帳頁與物流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=10488
permalink: "https://help.cyberbiz.io/pos/orders/store-pickup-orders-inbound-and-pickup/"
comments: false
search:
  exclude: false
icon: lucide/package-check
hide: []
---

# Store Pickup Orders (Inbound/Pickup)
Learn how to handle inbound arrivals, customer pickups, and overdue order management for storefront orders at the POS front end. This supports OMO operations, where orders are placed online and picked up in store.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Scope and Comparison"
    This document applies only to shipping management for **POS store orders**. For **regular store orders**, see [store pickup order shipping](../../ec/orders/store-pickup-orders.md).


## Before You Start { #prerequisites-store-pickup }

- **Prerequisites**: This feature is available only if **POS Store Pickup** is enabled.
- **Order Condition**: Orders marked as **Shipped** in the admin panel.
- **Commission Linkage**: If the merchant has set up [store pickup staff commission](../store/pos-store-pickup-staff-commission.md), the system calculates commission based on the **Receiving Staff** selected during the workflow.
- **Full-Order Return Limit**: POS store pickup orders support only **full-order returns**, and partial item returns are not available.

## Shipping Process { #operate-store-pickup }

### Step 1: Ship the Order { #operate-store-pickup-step-a-order }

1. Log in to the CYBERBIZ admin panel and go to **Orders > All Orders**.

    > Use the order filter and select `POS 商店取貨` under **Delivery Method** to find orders to process.

2. Select the orders to process. You can select a single order, or select multiple orders with the same delivery method at once.
3. Click **Select Action** in the upper-right corner, then select **Download In-Store Barcode and Mark as Shipped**.

    ![](../../assets/images/POS-後台-訂單-所有訂單-門市訂單出貨01.en.png){ .screenshot }

    !!! info "POS Store Arrival Barcode"
        - **Use Case**: Store receiving staff use it to **scan for inbound**, and it is used at pickup to **verify and check out** the customer's order.
        - **When Generated**: When an order is marked as **Shipped**, the system automatically generates the barcode document, deducts EC inventory, and sends a notification to the corresponding POS store.

            ![](../../assets/images/POS-前台-公告-門市取貨訂單出貨通知01.en.png){ .small-image }
        - **How to Use**: Print the downloaded PDF store arrival barcode sheet and attach it to the outer box of the package.
        - **Notes**: This barcode is for **internal management and in-store verification** only. It does **not** support delivery or tracking through third-party logistics providers (such as Black Cat or Pelican Express).

        ![](../../assets/images/EC-後台-訂單-門市訂單-到店條碼01.en.png){ .small-image }



### Step 2: Receive Packages at the Store { #operate-store-pickup-step-b }

When a package shipped from the central warehouse arrives at the store, store clerks must complete the inbound step. The system sends an SMS or email notification to the customer at the same time.

1. On the POS front-end home page, click **Orders > Store Pickup Orders**.
2. Click **Store Arrival Inbound** in the upper-left corner.
3. In the dialog, click **Click, Then Scan Barcode**, and use a barcode scanner to scan the **store arrival barcode** on the package.
4. After the system loads the order information, select your name from the **Receiving Staff** dropdown list.
5. Click **Confirm Arrival**.

    > The order's delivery status changes from **Shipped** to **Arrived**.

![](../../assets/images/POS-前台-訂單-門市訂單到店01.en.png){ .screenshot }

### Step 3: Customer Pickup at the Store { #operate-store-pickup-step-c }

When the customer comes to the counter, store clerk must verify the information and complete the handover.

1. On the POS front-end home page, click **Orders > Store Pickup Orders**.
2. Click **Customer Pickup** in the upper-left corner.
3. Enter the customer's **mobile number** or **email** (or scan the member barcode in the APP), then click **Confirm Search**.
4. The system lists all **Arrived** orders for this customer. Select the order to pick up, then click **Pick Up**.
5. Follow the system prompt and scan the barcode on the package again to verify it.
6. Select **Receiving Staff**, click **Confirm**, and hand over the goods to the customer.

    > The order's delivery status changes to **Received**.

![](../../assets/images/POS-前台-訂單-門市訂單到店02.en.png){ .screenshot }


## Pickup by Member Barcode Only { #intro-store-pickup }

To verify the recipient's identity, go to **Payment and Logistics > Checkout Page and Logistics Settings** in the admin panel and turn on **Pickup by Member Barcode Only Setting**.

!!! warning "Risk Notice"
    This feature requires OMO_APP or LINE@ to generate member barcodes. (If you want to use LINE@ member barcodes, each customer must link a LINE@ membership and obtain a member barcode.)

    When this setting is on, store clerks can enter the pickup process only by scanning the customer's **member barcode** in the mobile APP. Staff cannot search by manually entering a phone number or email.

## Return Process { #operate-returns }

If a customer wants to return an item they picked up, choose the handling method that matches where the customer is.

### Scenario 1: Return at the Store During Pickup { #operate-returns-customer-store-returns }

If the customer asks to return an item right after opening the package at the store, store staff should handle it through the POS front end.

1. On the POS front-end **Store Pickup Orders** page, click the order.
2. Click **Request Return** in the lower-right corner.

    > The order status changes to **Returning**.

3. Store staff securely repack the package and ship it back to the central warehouse.
4. After the central warehouse administrator performs [return review](../../ec/orders/order-return-process.md#operate-order-return-reverse) in the admin panel, the return process is complete.

### Scenario 2: Return After the Customer Takes the Item Home { #operate-returns-customer-returns }

If the customer has already taken the item out of the store, the return must be handled through the website front end or by contacting customer service.

1. The customer logs in to the storefront **Member Center > My Order(s)** and clicks **Request Return**.
2. The administrator goes to the admin panel and changes order `Delivery Status` to `Returning`.
3. The administrator can arrange reverse logistics to collect the package.

    - [7-11 C2B Return Service](../../ec/orders/returns-refunds/cvs-c2b-return.md)
    - [7-11 C2C Return Service](../../ec/orders/returns-refunds/7-11-c2c-return.md)
    - [Black Cat Reverse Logistics](../../ec/payments-and-logistics/setup-print-tcat-waybill-v2.md#operate-ezcat-shipping-reverse)
    - [Pelican Express Reverse Logistics](../../ec/payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-reverse)
    - [HCT Reverse Logistics](../../ec/payments-and-logistics/setup-hct-waybill-v2.md#operate-hct-setup-reverse)

4. After the package returns to the warehouse, the administrator performs a [return review](../../ec/orders/order-return-process.md#operate-order-return-reverse) in the admin panel and processes the refund.


## Special Scenarios { #intro-special-cases }

### Reprint the Store Arrival Barcode Sheet { #intro-special-cases-barcode }

If the order has already been changed to **Shipped** but the barcode must be reprinted, select the order, then click **Reprint Store Arrival Barcode** in the **Select Action** menu.

![](../../assets/images/POS-後台-訂單-所有訂單-門市訂單出貨02.en.png){ .screenshot }

### Handle Overdue Uncollected Orders { #intro-special-cases-order }

If a package has been kept in the store longer than the specified number of days, you can handle it by following the steps below.

1. Go to **Store Pickup Orders** and click **Advanced Filter**.
2. Select **Overdue** as the order status, then click **Confirm**.
3. For the filtered orders, you can:
    - **Notify for Pickup**: After contacting the customer, complete pickup following the standard process.
    - **Request Return**: If you cannot reach the customer or the customer requests a return, click **Request Return** in the lower-right corner of the order details.
4. After you request a return, follow the instructions to change the item to **Return to Central Warehouse** or **Add to Store Inventory**.
    - For the process, see [Order Cancellation - Package Arrived at Store (Customer Not Yet Picked Up)](#operate-store-pickup-return-at-store).

!!! info "How to Enable This Feature"
    Log in to the CYBERBIZ admin panel, go to **Payment and Logistics > Checkout Page and Logistics Settings**, turn on the feature in **POS Store Pickup Overdue Settings**, and set the number of days.


### Cancel Orders and Return to Central Warehouse { #intro-special-cases-order-cancel }

Handle the order based on its current stage, as follows:

#### Stage 1: Before Shipment (Not yet Shipped) { #intro-special-cases-section-n }

=== "Merchant"

    If the delivery status is `Unshipped`, the administrator can click **Cancel Order** directly within the order.

    ![](../../assets/images/EC-後台-訂單-門市訂單-取消訂單01.en.png){ .screenshot }

=== "Customer"

    Customers can also click **Cancel Order** on the order details page on the front end.

    ![](../../assets/images/EC-前台-訂單查詢-取消訂單01.en.png){ .screenshot }

#### Stage 2: Shipped but Not yet Arrived at Store { #intro-special-cases-section-o }

To intercept a package that has already been shipped, perform the following steps:

1. Select the order in the order list, then click **Actions > Return to Central Warehouse** in the upper-right corner.
    ![](../../assets/images/POS-後台-訂單-所有訂單-門市訂單出貨03.en.png){ .screenshot }
2. The order status changes to `Returned`, and the system automatically creates an inbound order.

    > The source store is **Third Party**, and the status is **Pending Inbound**

    ![](../../assets/images/POS-後台-訂單-所有訂單-門市訂單出貨04.en.png){ .screenshot }


3. Go to **POS > Inventory Management > Inbound Orders** and complete the [receiving count](../inventory/inbound-orders/#operate-inbound-orders-receive) to restore EC inventory.

#### Stage 3: Arrived at Store (Customer Has Not Picked Up) { #operate-store-pickup-return-at-store }

When the package has arrived at the store but the customer requests a return, the administrator can choose **Add to Store Inventory** or **Return to Central Warehouse**:

=== "Add to Store Inventory"

    The administrator performs **Add to Store Inventory** in the admin panel, and the order changes to `Returning`. The system automatically creates an inbound order for that store. Store staff then complete the [receiving count](../inventory/inbound-orders/#operate-inbound-orders-receive), which converts the items to in-store inventory.

    ![](../../assets/images/POS-後台-訂單-所有訂單-門市訂單出貨05.en.png){ .screenshot }

=== "Return to Central Warehouse"

    Store clerks submit a return request on the POS, and the order changes to `Returning`. After the package is shipped back, the administrator performs **Reviewing Return** in the admin panel and changes it to `Returned`. If **Return to Central Warehouse** is selected, the order status changes to `Returned`, and then the refund process begins.

    ![](../../assets/images/POS-後台-訂單-所有訂單-門市訂單出貨03.en.png){ .screenshot }




## FAQ { #faq-store-pickup }

??? quote "Why does downloading the store arrival barcode show a failure message?"
    Check whether the order includes the "Cash on Delivery" option. POS store pickup currently supports only "Pay First, Pick Up Later." If Cash on Delivery is included, the store arrival barcode cannot be generated.

??? quote "How can a customer return an item after pickup?"
    - **In-Store Return**: Store staff can click "Request Return" on the POS front end. The status changes to `Returning`, and the review is then completed in the admin panel.
    - **Website Return**: Customers can request a return from the website front end. The process is the same as for regular EC orders.

??? quote "Does forgetting to select Receiving Staff affect commission?"
    Yes. Commission calculation depends on the staff member selected during the operation. If no staff member is selected, the system cannot automatically assign the commission for that order.



