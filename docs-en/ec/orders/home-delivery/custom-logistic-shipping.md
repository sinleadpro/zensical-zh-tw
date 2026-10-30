---
title: "How to Ship with Custom Logistics"
description: "Three ways to ship with custom logistics: batch mark as shipped, bulk import tracking numbers with Excel, and manually ship a single order, plus notes and follow-up actions."
created: 2026-05-11 21:44
last_modified: 2026-06-30 10:12
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
  - 如何使用自訂物流出貨
  - 批次標記訂單為已出貨
  - Excel 大量匯入託運單號
features:
  - 自訂物流出貨
  - 批次出貨
  - Excel 匯入託運單號
  - 單筆訂單手動出貨
prerequisites: []
related:
  - ec/orders/order-settings/manual-order-close/
  - ec/orders/order-settings/auto-close-order-settings/
  - ec/orders/order-return-process/
tags:
  - "Custom Logistics"
  - Shipping
  - "Tracking Numbers"
  - "Batch Shipping"
  - Logistics
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單管理 > 訂單列表
  - 設定 > 訂單設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=105
  - https://www.cyberbiz.io/support/?p=982
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/custom-logistic-shipping/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

![Custom logistics shipping](../../../assets/images/EC-訂單-所有訂單-更多操作-已出貨-hero.en.png){ title="Ship with Custom Logistics" .hero-page }

## About Custom Logistics Shipping { #custom-logistics-shipping-intro }

"Custom logistics" is for logistics not integrated with the CYBERBIZ system, such as freight companies you work with directly (Ta Rong Logistics, Kerry TJ Logistics, third-party couriers), your own delivery, or customer pickup. You can manually specify the freight company on the order (tracking number optional). The system changes the order's delivery status to "Shipped," and you can choose whether to send the customer a notification email.

??? info "Differences from Integrated Logistics"
    Unlike system-integrated logistics (such as EZCAT, HCT Logistics, SF Express, and Pelican Express), custom logistics:

    - Doesn't generate shipping labels automatically
    - Doesn't sync delivery progress
    - Doesn't update tracking history

## Prerequisites and Limitations { #custom-logistics-shipping-prerequisites }

Before shipping, the order must meet all of the following:

- [x] **Delivery Status**: Must be "Unshipped" or "Preparing." Orders that are Shipped, Received, Returning, or Returned can't use this action.
- [x] **Payment Status**: Must be "Payment Received." "Custom Logistics Cash on Delivery" orders can also ship directly.
- [x] **Whole-order shipment only**: Shipping only some items isn't supported. To ship in batches, handle each order on its order details page.
- [x] **Delivery method**: Must be "Home Delivery." Convenience store pickup orders (both prepaid and Cash on Delivery) and home delivery Cash on Delivery orders **can't use** this process; use the matching logistics process instead.

!!! warning "Irreversible Action"

    Once an order's delivery status changes to "Shipped," it can't be changed back to "Unshipped." To cancel, you can only use the return or refund process, so make sure the information is correct before proceeding.

## How to Ship { #custom-logistics-shipping-operate }

There are three ways to ship, depending on shipment volume and whether you need to enter tracking numbers:

<div class="grid cards" markdown>

-   :lucide-package-open:{ .lg }
    [Quick batch shipment (no tracking numbers)](#custom-logistics-shipping-batch)

-   :lucide-file-spreadsheet:{ .lg }
    [Bulk import tracking numbers with Excel](#excel-bulk-import)

-   :lucide-pencil:{ .lg }
    [Ship a single order manually](#single-order-manual-ship)

</div>

---

### Mark Orders as Shipped in Bulk { #custom-logistics-shipping-batch }

Use this to quickly change multiple orders to "Shipped" without entering tracking numbers one by one.

!!! example "When to Use"

    - You deliver orders yourself
    - A driver delivers orders together
    - You'll add tracking numbers later

**Steps**


1. **Go to the order list**: Go to "Orders" > "All Orders."
2. **Select orders**: Select the orders to ship. You can select multiple orders for batch processing.
3. **Ship**: Click "More Actions" > "Shipped" above the list.

    === "New Order List"

        ![Mark orders as shipped](../../../assets/images/EC-訂單-所有訂單-更多操作-已出貨.en.png){ title="Mark Orders as Shipped" }

    === "Legacy Order List"

        ![Mark orders as shipped - legacy](../../../assets/images/EC-訂單-所有訂單-更多操作-已出貨-舊版.en.png){ title="Mark Orders as Shipped (Legacy)" }

    !!! note "Orders That Don't Meet the Requirements"
          If the selected orders include any that don't meet the requirements above, the system shows "Includes orders that need no further action. Please select again." Deselect those orders before proceeding.

4. **Select a freight company**: In the "Select a freight company" window, choose the carrier you actually use.

    === "New Order List"

        ![Select a freight company](../../../assets/images/EC-訂單-所有訂單-更多操作-已出貨-選擇貨運公司.en.png){ title="Select a Freight Company" }

    === "Legacy Order List"

        ![Select a freight company - legacy](../../../assets/images/EC-訂單-所有訂單-更多操作-已出貨-選擇貨運公司-舊版.en.png){ title="Select a Freight Company (Legacy)" }

    !!! info "The freight company list is provided by the system and can't be extended. If your carrier isn't listed, choose the closest option and add details in the order note."

5. **Set the notification email**: Turn "Send email notification to customer" on or off as needed.
6. **Complete the shipment**: After you confirm, the order status changes to "Shipped."

---

### Bulk Import Custom Logistics Tracking Numbers <small>Excel</small> { #excel-bulk-import }

Use this when you need to **enter many different tracking numbers at once**.

!!! example "When to Use"

    - Batch shipments through third-party logistics
    - Adding tracking numbers together after delivery

**Steps**

1. **Go to the order list**: Sign in to the admin and go to "Orders" > "All Orders."
2. **Download the template**: Click "Bulk Import Custom Logistics Tracking Numbers" and download the Excel template.

    ![Bulk import custom logistics tracking numbers](../../../assets/images/EC-訂單-所有訂單-大量匯入自訂物流託運單號.en.png){ title="Bulk Import Custom Logistics Tracking Numbers" }

3. **Fill in the information**:
    - Order number (required): Must exactly match the admin (including symbols).
    - Tracking number (optional): Enter the number from the carrier.
    - Carrier name (optional): Must be a name that exists in the system.

    ![Custom tracking number bulk import template](../../../assets/images/大量匯入自訂託運單範本.en.png){ title="Custom Tracking Number Bulk Import Template" }

    !!! info "Excel Tips"

        - If one order ships in multiple packages, join the tracking numbers in the "Tracking Number" column with a half-width semicolon `;`. For example: `1000;2561;333`
        - Each import can include up to **10,000 orders**.
        - After upload, the system processes the file on a schedule and emails you the import results.
        - Only "Home Delivery" orders are supported, and partial shipment isn't supported.

4. **Upload the file**: Upload the completed Excel file.
5. **Wait for processing**: The system processes the batch and emails the import results.

    ??? success "Import Results"

        After the import completes, the system:

        - **Updates the delivery status**: The order's delivery status changes to "Shipped" automatically.
        - **Sends notifications**: The system sends a "shipping notification email" to the customer.

---

### Ship a Single Order from the Details Page { #single-order-manual-ship }

!!! example "When to Use"
    - Entering tracking numbers precisely one by one
    - Editing shipping notes
    - Handling special logistics needs individually

**Steps**

1. **Open the order details page**: Click the order number in the order list.
2. **Choose a shipping method**: In the "Shipping Method" drop-down in the "Shipping" section, select "Custom Shipping Method."
3. **Enter logistics information**: Enter the "Courier Company" and "Tracking Number."
4. **Set the notification email**: Choose whether to send a shipping notification email.
5. **Complete the shipment**: After you confirm, the order status changes to "Shipped."

![Order details page - custom shipping](../../../assets/images/EC-訂單-訂單詳情頁-出貨方式-自訂出貨.en.png){ title="Order Details Page: Custom Shipping" }

## Special Cases

- **Customer pickup**: Still use the "custom logistics" process. For "Tracking Number," enter a pickup number or text such as "Customer pickup."
- **Self-delivery**: Use [batch shipment](#custom-logistics-shipping-batch) and add delivery details in the note.
- **Handwritten waybills**: If you use a handwritten waybill, enter the actual handwritten number.

    !!! warning "Don't enter your CYBERBIZ customer code, or it may cause billing errors."

- **Multiple packages per order**: We recommend Excel import, joining the tracking numbers with a half-width semicolon `;`.

## Next Steps

Custom logistics doesn't sync delivery progress automatically, so you need to move the order forward yourself.

<div class="grid cards" markdown>

- :lucide-check-circle:{ .lg }  
  [__Manually Complete Orders__](../order-settings/manual-order-close.md){ title="How to Manually Close Orders" }  
  After the customer receives the order, click "Complete Order" on the order details page to change it to "Completed."

- :lucide-clock:{ .lg }  
  [__Turn On Automatic Completion__](../order-settings/auto-close-order-settings.md){ title="Set Up Order Auto-Close" }  
  Go to "Settings" > "Order Settings" and turn on "Automatically complete orders N days after shipping."

- :lucide-rotate-ccw:{ .lg }  
  [__Returns / Exchanges__](../order-return-process.md){ title="Order Return and Refund Process" }  
  If the customer needs a return or exchange, create a return on the order details page and process it.

</div>

## FAQ

??? quote "Why can't I find my carrier in the drop-down?"

    The custom logistics freight company list is maintained by the system to keep reconciliation and categories consistent. If your carrier isn't listed, choose the closest option and note the actual carrier in the order note. To request a specific carrier, contact CYBERBIZ for evaluation.

??? quote "Can I change the tracking number after shipping?"

    Yes. Open the order details page, edit the "Tracking Number" or "Courier Company" in the logistics section, and save. Changes don't resend the notification email; notify the customer separately if needed.

??? quote "Can I change an order back to "Unshipped" after marking it shipped?"

    Not directly. To void a shipment record, use the return or refund process. Double-check the freight company and tracking number before shipping.

??? quote "If I didn't select "Send email notification to customer," can I send the notification later?"

    The system doesn't resend shipping notification emails automatically. To notify the customer, contact them through the order note or send a custom notification email for the order in the admin.

??? quote "Can convenience store pickup orders use custom logistics?"

    No. Convenience store pickup orders (both prepaid and Cash on Delivery) must use the matching convenience store logistics process. The system blocks ineligible orders and shows "Includes orders that need no further action. Please select again."

??? quote "What can cause an Excel import to fail?"

    Common causes include:

    - **Order number mismatch**: Must exactly match the admin (including symbols).
    - **Convenience store pickup not supported**: Only "Home Delivery" orders are supported.
    - **Over the limit**: Each import can include up to 10,000 orders.

??? quote "Why weren't marketing campaign reward points or coupons issued?"

    If a marketing campaign offers reward points for purchases or coupons for store-wide spending thresholds, they're issued when the order status becomes "Completed." Custom logistics orders only reach "Shipped," so you need to complete them manually to issue the reward points and coupons.

??? quote "When are custom logistics orders recognized on the statement?"

    Statement recognition works as follows:

    - **System-integrated logistics (EZCAT, Pelican Express, convenience store pickup)**: The system can track the final delivery status, so the order is included on the statement when it's "Received."
    - **Custom logistics**: The system can't track delivery status, so the order is recognized on the statement once it's "Shipped."
