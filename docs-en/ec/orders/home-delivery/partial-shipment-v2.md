---
title: "Set Up Partial Shipment for Orders"
description: "Set up partial shipment for orders, including steps and special cases for different logistics providers."
created: 2026-05-12 15:11
last_modified: 2026-07-01 22:30
lang: en-US
type: guide
author: Jase
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
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 如何設定部分出貨
  - 訂單缺貨分批出貨
features:
  - 部分出貨
  - 加印託運單
prerequisites: []
related:
  - wms/enable-partial-warehouse-integration-and-order-splitting/
  - ec/orders/order-settings/manual-order-close/
  - ec/orders/home-delivery/custom-logistic-shipping/
  - ec/orders/out-of-stock-partial-shipping-or-cancellation/
tags:
  - "Partial Shipment"
  - "Order Management"
  - "Logistics Settings"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=93
  - https://www.cyberbiz.io/support/?p=43635
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/partial-shipment-v2/"
comments: false
search:
  exclude: false
icon: lucide/package-check
hide: []
---

![Order details page - partial shipment](../../../assets/images/EC-訂單-訂單詳情頁-部分出貨-hero.en.png){ title="Order Details Page: Partial Shipment" .hero-page }

## About Partial Shipment

When only some items in an order are in stock, "partial shipment" lets you ship those items to the customer first and ship the rest later under the same order, so the customer waits less.

In the "Shipping" section of the order details page, select only **the items you're shipping now** instead of all items. The system automatically changes the order's delivery status to "Partially Shipped" and keeps the unshipped items for you to handle later.

!!! info "Tip"
    Each time you ship, the system sends the customer a shipping notification email **based on your selection** (selected by default), so the customer may receive several notifications.

---

## Requirements and Limitations

Before a partial shipment, check the following requirements. If any isn't met, the "Shipping" section won't show selectable items or shipping methods.

### Order Requirements

- [x] **Order Status**: Open.
- [x] **Payment Status**: Paid, Cash on Delivery, Pending Partial Refund, Partially Refunded, or "Awaiting Payment" for a custom payment method.
- [x] **Delivery Status**: Unshipped, Partially Shipped, Preparing, or Shipping Exception.

??? info "When Partial Shipment Isn't Supported"

    In these cases, the "Shipping" section is hidden, or the drop-down doesn't list the matching logistics option.

    * **B2C bulk shipping orders** (convenience store orders through ECPay B2C bulk shipping logistics)
    * **Hi-Life B2C orders** (Hi-Life standard pickup / Cash on Delivery, not store-to-store)
    * **FamilyMart Cold Chain shipping labels** (select all items at once)
    * **CYBERBIZ NOW Quick Delivery orders** whose status is past "Preparing" (see "Special Cases" below)
    * **Returned in-store pickup orders**
    * **Amazon FBA warehouse-integrated orders**
    * **Orders entirely from an integrated warehouse**, when you haven't purchased the "[Partial Warehouse Integration](../../../wms/enable-partial-warehouse-integration-and-order-splitting.md){ title="Enable Partial Warehouse Integration and Order Splitting" }" add-on

## Steps { #fuilfillment-partial-operate }

The following uses "EZCAT Shipping Label" as an example. The steps for other carriers (such as Pelican Express, SF Express, HCT Logistics, or custom shipping) are largely the same.

1. **Open the order details page:** Go to "Orders" > "All Orders" in the admin and click the "Order Number" of the order to partially ship.
2. **Select the items to ship now:** In the "Shipping" section, select the items to send first. To select all items at once, click "Select All"; to start over, click "Deselect All."

    ![Order details page - partial shipment](../../../assets/images/EC-訂單-訂單詳情頁-部分出貨.en.png){ title="Order Details Page: Partial Shipment" }

    !!! warning "Home Delivery Cash on Delivery (COD) Limitation"
          For "Cash on Delivery" orders, the partial shipment option isn't shown. To ship in multiple boxes, use "Print Extra Shipping Labels" instead so the collected amount is correctly split across tracking numbers.

3. **Choose a shipping method:** In the "Select Shipping Method" drop-down below, choose the logistics service to use (such as "EZCAT Shipping Label").

    !!! note "The drop-down shows only activated logistics methods and options available for this order."

4. **Choose a shipping fee option:** In the "Select a fee" drop-down, choose the matching shipping label option (such as a weight or size range).

    !!! note "After the shipping label is created, the system automatically deducts the matching logistics points."

5. **Confirm terms and package attributes**:
    - **Agree to the terms**: Select "I agree to the CYBERBIZ Logistics Integration Terms of Service and..." (required).
    - **Fragile label**: If the items are fragile, select "Fragile item?" so the carrier provides the matching delivery service.
6. **Confirm the shipment:** Click **"Confirm Shipment."** The system creates the shipping label, deducts the shipping points, and marks those items as shipped.
7. **Check the shipping record**:
    - **Item shipping record**: The shipping time and "Tracking Number" appear below shipped items.

      ![Order details page - partially shipped](../../../assets/images/EC-訂單-訂單詳情頁-部分已出貨.en.png){ title="Order Details Page: Partially Shipped" }

    - **Order delivery status**: The delivery status at the top of the order changes to "Partially Shipped."

      ![Order list - delivery status - partially shipped](../../../assets/images/EC-訂單-所有訂單-配送狀態-部分出貨.en.png){ title="Order List: Delivery Status Partially Shipped" }

    !!! info "Cancellation Limitation"
        You can't delete created shipping labels yourself in the admin. If you make a mistake (such as the wrong logistics service or items), contact CYBERBIZ customer service to cancel it.

## Ship the Remaining Items { #fulfillment-partial-resume }

When the out-of-stock items are restocked, go back to the same order and [repeat the steps above](#fuilfillment-partial-operate) to ship them:

1. **Open the order**: Go to "Orders" > "All Orders" and click the order number of an order with status `Partially Shipped`.
2. **Select items**: Select the remaining items to ship now.
3. **Ship**: Choose the shipping method and fee, then click **Confirm Shipment**.

!!! info "Important Rules"

    | Category | Description |
    | :--- | :--- |
    | **Status updates** | The status stays `Partially Shipped` until the last item ships, then changes to `Shipped`. |
    | **Automation limits** | Partially shipped orders **aren't completed automatically**. [Complete them manually](../order-settings/manual-order-close.md){ title="How to Manually Close Orders" } after everything ships. |
    | **Customer notifications** | Each shipment is a separate event, and the system sends a shipping notification each time based on your selection. |

## Special Cases by Logistics Type { #fuilfillment-partial-edge-case }

### Custom Shipping Method

When you use a third-party carrier you work with or deliver orders yourself (for details, see [How to Ship with Custom Logistics](custom-logistic-shipping.md){ title="How to Ship with Custom Logistics" }):

1. In the "Select Shipping Method" drop-down, choose "Custom Shipping Method."
2. The system shows a "Tracking Number" field and a carrier menu.
3. Enter the "Tracking Number" for these items and choose the matching carrier.
4. Click "Confirm Shipment."

---

### CYBERBIZ NOW Quick Delivery <small>Store Fulfillment</small>

- **Where to go**: Quick Delivery orders are handled in "Store Orders." Don't process them in the "All Orders" list.
- **Out-of-stock handling**: If the store doesn't have enough stock, select the items actually in stock and ship them first. For details, see [Partial Delivery or Cancellation for Out-of-Stock Orders](../../orders/out-of-stock-partial-shipping-or-cancellation.md){ title="Partial Delivery or Cancellation for Out-of-Stock Orders" }.

!!! warning "Shipment Limit"
    By default, Quick Delivery orders **can ship only once per order**. After you select items and confirm the shipment, the remaining items can't ship, and they must go through the **return and refund** process. Contact the customer and agree on a plan first, so repeated refunds don't hurt their experience.

---

### Partially Warehouse-Integrated Orders

When an order contains both "self-shipped items" and "warehouse items," and you've purchased the "[Partial Warehouse Integration](../../../wms/enable-partial-warehouse-integration-and-order-splitting.md){ title="Enable Partial Warehouse Integration and Order Splitting" }" add-on, you can ship the **self-shipped** items first using the steps above. Warehouse items are shipped by the warehouse and aren't part of this process.

## When to Use "Print Extra Shipping Labels" Instead

If you're splitting a shipment **not because items are out of stock**, but because "all items ship at once in multiple packages," use "Print Extra Shipping Labels" instead:

* Enter the order number within the same order to generate multiple tracking numbers for tracking each box.
* Cash on Delivery orders shipped in multiple boxes **must** use extra shipping labels, not partial shipment.

## FAQ

??? quote "Why don't I see the "Shipping" section on the order details page?"

    Check the following in order:

    - Whether the order status is "Open" (canceled orders can't ship)
    - Whether the payment status is "Paid," "Cash on Delivery," "Partially Refunded," or similar
    - Whether the delivery status is "Unshipped," "Partially Shipped," "Preparing," or "Shipping Exception"
    - Whether it's an unsupported logistics type such as B2C bulk shipping, Hi-Life B2C, or Amazon FBA
    - For warehouse-integrated orders, whether you've purchased the "Partial Warehouse Integration" add-on

??? quote "Can I cancel after shipping?"

    You **can't cancel** created shipping labels yourself in the admin. If you selected the wrong items or logistics service, or shipping points were deducted incorrectly, contact CYBERBIZ customer service.

??? quote "Does the order change to "Shipped" automatically after a partial shipment?"

    No. The order changes to "Shipped" automatically only after **all items have shipped**. Until then, it stays "Partially Shipped."

??? quote "How many shipping notifications will the customer receive?"

    By default, a notification email is sent each time you ship. If you don't want the customer to receive multiple notifications, **deselect** "Send email notification to customer" before clicking "Confirm Shipment."

??? quote "Can Cash on Delivery orders be partially shipped?"

    The collected amount is tied to the shipping label, so shipping in multiple batches spreads it across several labels and complicates reconciliation. Use **"Print Extra Shipping Labels"** instead to generate multiple tracking numbers under the same order.

??? quote "How do I ship the remaining items after a partial shipment?"

    Go back to the same order details page and repeat the partial shipment steps:

    1. Go to "Orders" > "All Orders" and click the order number of an order with status "Partially Shipped."
    2. Select the remaining items to ship now.
    3. Choose the shipping method and fee, then click "Confirm Shipment."

??? quote "Can Quick Delivery orders be partially shipped? What are the limits?"

    Quick Delivery orders can be partially shipped when the store is out of stock, but **only once per order by default**. After shipping, the remaining items can't ship and must go through the return and refund process.

??? quote "How are extra shipping labels different from partial shipment?"

    They're for different situations:

    - **Partial shipment**: Ship in batches because items are out of stock. After each shipment, the order stays "Partially Shipped" until everything ships.
    - **Print Extra Shipping Labels**: All items are in stock but need to ship at once in multiple packages, so you generate multiple tracking numbers under the same order. Cash on Delivery orders shipped in multiple boxes **must** use extra shipping labels.

