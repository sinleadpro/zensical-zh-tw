---
title: "Order Management Interface"
description: "Explains the management features of the All Orders page, helping merchants handle core operations from filtering orders and tracking shipment status to editing order details."
created:
last_modified: 2026-07-13 09:32
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/basics/order-management-interface/"
type: guide
author: Jase
reviewers: []
notes:
  - verify 重開訂單功能
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
  - 管理訂單
  - 訂單篩選
  - 訂單查詢
  - 訂單出貨
  - 訂單編輯
features:
  - 訂單列表
  - 訂單明細
  - 訂單篩選
  - 訂單搜尋
  - 訂單出貨
  - 批次操作
prerequisites: []
related:
  - ec/orders/references/order-list-columns/
  - ec/orders/references/order-filter-status-reference/
  - ec/orders/basics/search-filter-orders/
  - ec/orders/order-settings/manual-order-close/
  - ec/orders/basics/cancel-order/
  - ec/orders/basics/edit-order-content/
  - ec/orders/order-settings/provide-payment-link/
  - ec/orders/home-delivery/shipping-status-tooltip/
  - ec/website-management/member-security-settings/
  - ec/orders/references/order-list-features/
  - ec/orders/reports/export-order-report/
  - ec/orders/order-return-process/
  - ec/orders/order-refund-process/
tags:
  - "Order Management"
  - "Order List"
  - "Order Filters"
  - "Order Search"
  - "Order Fulfillment"
  - "Order Details"
  - "Batch Actions"
  - "Order Actions"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10999
  - https://www.cyberbiz.io/helpcenter/?p=34
  - https://www.cyberbiz.io/helpcenter/?p=10
  - https://www.cyberbiz.io/support/?p=45545
  - https://www.cyberbiz.io/support/?p=624
  - https://www.cyberbiz.io/support/?p=622
comments: false
search:
  exclude: false
icon: lucide/panels-top-left
hide:
---

![Order management interface](../../../assets/images/ec-訂單-所有訂單.en.png){ title="Order Management Interface" .hero-page }

## About the Order Interface { #orders }

The **All Orders** page is the core interface for managing sales records, processing shipments, and tracking delivery status.

!!! warning "Notes on Order Actions"

    - **Irreversible:** Once an order is completed or canceled, some statuses can't be reverted. Confirm before you proceed.
    - **Shipping limit:** After the order's delivery status changes to "Shipped," the delivery address can no longer be changed.
    - **Subscription orders:** For subscription orders, you can show the "Parent Order Number" and "Delivery Period" columns in the list to see which period a sub-order belongs to.

## Order List Features

!!! path "Admin path: **Orders > All Orders**."

### Edit Columns and Order

- Click **Edit Columns** and select the [order list columns](../references/order-list-columns.md#orders-columns){ title="Order List Columns Reference" data-preview } to show (such as member, product details, order tags, order date, payment method, and delivery date).
- Drag the :lucide-grip-vertical: icon to change the order and set up the list the way you like.

??? tip "Track Subscriptions"
	If you sell subscriptions, turn on the `Parent Order Number` and `Delivery Period` columns to quickly see which plan each sub-order belongs to.

![Edit columns and order](../../../assets/images/ec-訂單-所有訂單-編輯欄位.en.gif){ title="Edit Columns and Order" }

---

### View Groups { #order-filter-group }

With "View Groups," you can save frequently used [filters](../references/order-filter-status-reference.md#orders-v2-filters){ title="Order Filters and Statuses Reference" data-preview }  (such as a specific carrier, payment status, or delivery status) as custom tabs and switch with one click to process orders in bulk more efficiently.

**Steps**

1. **Set filters:** Click **Add Filter** and select conditions based on order, payment, delivery, or return status.
2. **Save the group:** Click **Save** and name the group (for example, "To Ship"). The system adds a matching tab at the top of the page.
3. **Manage groups:** Click the :lucide-chevron-down: icon next to a tab to "rename" or "delete" the group.

??? example "Common Filter Examples"

    | View Group Name | Suggested Filters |
    | :--- | :--- |
    | **Orders to ship** | **Delivery status**: `Unshipped`, `Preparing`<br>**Payment status**: `Cash on Delivery`, `Payment Received` |
    | **Specific carrier orders** | **Delivery method**: Select specific carriers (such as EZCAT or FamilyMart) |
    | **Returns in progress** | **Order status**: `In Progress`<br>**Return status**: `Return Requested`, `Returning`, `Reviewing Return` |

![View groups](../../../assets/images/ec-所有訂單-檢視群組.en.gif){ title="View Groups" }

---

### Search and Keywords

- Search by name, phone, email, address, order number, tracking number, product name, delivery method, or coupon code.
- Some fields, such as customer email and tracking number, require an **exact match**.

![Order search](../../../assets/images/ec-訂單列表-搜尋.en.png){ title="Order Search" }

<div class="grid cards" markdown>

- :lucide-search:{ .lg .middle } [__How to Search and Filter Orders__](search-filter-orders.md){ title="How to Search and Filter Orders" }

</div>

---

### Order Details Preview

**Hover** over an order number to open a **preview window** with the product details and recipient information.

![Order details preview](../../../assets/images/ec-所有訂單-明細預覽.en.png){ title="Order Details Preview" }

---

### Product Details Preview

- **Quick preview:** In the "Product Details" column, click **Preview** to open a window with the order's product list.

- **Browse in sequence:** In the preview window, click the left and right arrows to view the products of the previous or next order without closing the window.

![Product details preview](../../../assets/images/ec-訂單列表-商品詳情預覽.en.gif){ title="Product Details Preview" }

---

### Change Rows per Page

Use the rows-per-page menu below the list to change how many orders are shown per page (such as 10, 25, 50, or 100). Pagination adjusts automatically.

![Change rows per page](../../../assets/images/ec-所有訂單-顯示筆數.en.png){ title="Change Rows per Page" }

---

## Order Details Page

The **"order details page"** is the core interface for handling a single order, viewing transaction records, and contacting the customer. In the admin, go to **Orders > All Orders** and click an **order number** to open it.

### Main Action Buttons

These are in the upper right of the page and change the order's lifecycle:

<div class="grid cards" markdown>

-   :lucide-printer:{ .lg .middle } __Print__

- :lucide-check:{ .lg .middle } [__Complete Order__](../order-settings/manual-order-close.md){ title="How to Manually Close Orders" }

-   :lucide-ban:{ .lg .middle } [__Cancel Order__](cancel-order.md){ title="How to Cancel an Order" }

-   :lucide-edit:{ .lg .middle } [__Edit Order__](edit-order-content.md){ title="Edit Order Content" }

</div>

![Order details page action buttons](../../../assets/images/EC-訂單詳情頁-核心按鈕.en.png){ title="Order Details Page Action Buttons" }

---

### Payment and Shipping

- **Payment information:** Shows the payment method and status (such as Awaiting Payment or Payment Received).

	- If the customer hasn't paid, copy the ["payment link"](../order-settings/provide-payment-link.md){ title="Send Customers a Payment Link" }  here and send it to the customer to pay again.
	- If a member pays by **bank transfer**, click "Confirm Payment" once you've received the payment to change the payment status to Payment Received.

- **Shipping actions:**

	- **Delivery date:** The delivery date the customer chose. Before shipping, you can change the estimated shipping time (not for connected-warehouse merchants).
	- **Delivery time:** The delivery time the customer chose.
	- **Delivery method:** The shipping method the customer chose (can't be changed).
	- **Select items to ship:** Select the items to ship (**ship all** or **partial shipment**).

	- **Select a shipping method:** Integrated logistics (generate labels directly) or a custom shipping method (enter the tracking number manually).

	- **Logistics tooltip text:** For integrated logistics, details such as "**Awaiting Carrier Pickup**" or "**In Transit**" appear after shipping. For details, see [Logistics Tooltip Text](../home-delivery/shipping-status-tooltip.md){ title="Shipment Status Tooltip Text" }  

=== "Unshipped"

	![Unshipped section](../../../assets/images/ec-訂單明細頁-貸款與出貨區塊-未出貨.en.png){ title="Unshipped Section" }

=== "Shipped"

	![Shipped section](../../../assets/images/ec-訂單明細頁-貸款與出貨區塊-已出貨.en.png){ title="Shipped Section" }

---

### Buyer and Recipient Information

- **Billing information:** The buyer's information, which **can't be changed** after the order is placed.

- **Contact information:** The recipient's information. The name, phone, and address can be edited only while the order is **"Unshipped."**

	<!-- - **Standard Plan:** For convenience store pickup, go to the ECPay backend to make changes. -->
	<!---->
	<!-- - **Enterprise:** FamilyMart pickup can't be changed directly; **place a new order**. -->

- **Invoice:** Invoice information.

- **Masked personal data:** If [partial masking of member data](../../website-management/member-security-settings.md#operate-security-pdpa){ title="Protect Admin Accounts and Customer Data" } is turned on in the admin, the system masks part of the member's name, mobile number, and address when printing details to protect privacy.

![Buyer and recipient information](../../../assets/images/ec-訂單明細頁-訂購人與收貨人資訊.en.png){ title="Buyer and Recipient Information" }

---

### Notes and Other Information

- **Order note:** A note **the customer entered on the checkout page**, for special delivery or packaging requests
- **Shop Note:** This is **for internal use by store admins only and is never visible to customers**.
- **Additional information:** Custom fields you add to the checkout page to collect information for specific campaigns, such as "gift style confirmation" or "tax ID needed."
- **Logistics messages:** System messages from the carrier.

![Notes and logistics messages](../../../assets/images/ec-訂單明細頁-備註與物流訊息.en.png){ title="Notes and Logistics Messages" }

---

### Order Conversation and Notes

- **Customer messages:** Questions customers send from "Order Lookup" on the storefront.
- **Store messages:** Your replies. Messages **can't be recalled** once sent.
- **Admin notes:** Notes visible only to admins, **not visible to customers**.
- **Customer's other open orders**: The customer's other orders that aren't completed yet, to help you decide whether to ship.

![Order conversation and open orders](../../../assets/images/ec-訂單明細頁-訂單對話與未結案訂單.en.png){ title="Order Conversation and Open Orders" }

---

### Order Activity Log <small>Key History</small> { #order-history }

At the bottom of the page, this is the most important tool for troubleshooting orders. It records the time and operator for these events:


- Time the **order was created**.

- Time and payment gateway response when **payment was received**.

- Time **you clicked ship** and when the carrier returned delivery statuses.

- History of **order completion or cancellation**.

- For a **return request**, click "Customer requested return" in the activity log to see the items and quantities the member requested to return.

![Order activity log](../../../assets/images/ec-訂單明細頁-訂單操作紀錄.en.png){ title="Order Activity Log" }

!!! tip "Contacting Customer Service"
    When reporting an order issue to customer service, include a screenshot of this section.

---

### Return Review Section <small>Shown in Certain Statuses</small>

When an order is "Reviewing Return," a **"Partial Refund"** section appears on the details page. Select the items to return, enter the refund amount, and click "Confirm Refund" to complete the process.

![Partial refund section](../../../assets/images/ec-訂單明細頁-部分退款.en.png){ title="Partial Refund Section" }

## Bulk Actions

After selecting multiple orders in the order list, use the **"More Actions"** menu to process them in bulk (for each action, see [Order List Actions](../references/order-list-features.md){ title="Order List Actions" data-preview }).

- **Change orders/statuses:** Change order, delivery, or return status in bulk. For example, change orders to "Preparing" or run "Download shipping labels and change to Shipped."
- **Print documents:** Generate order details or pick lists in bulk to speed up picking and packing.
- **Manage tags:** Add or remove custom tags for selected orders in bulk.

!!! tip "View Groups + Bulk Tags"
    Use "[View Groups](#order-filter-group)" to filter a specific customer group, then use "Manage Tags" to tag them in one click.

![Bulk actions](../../../assets/images/ec-訂單列表-更多操作.en.png){ title="Bulk Actions" }


## Next Steps

<div class="grid cards" markdown>

- :lucide-download:{ .lg }  
  [__Export Order Reports__](../reports/export-order-report.md){ title="Export Order Reports" }  
  Export the current search results to Excel/CSV for accounting reconciliation or customer service.

- :lucide-reply:{ .lg }  
  [__Order Return and Refund Process__](../order-return-process.md){ title="Order Return and Refund Process" }  
  Learn the full process and notes for starting a return from an order.

- :lucide-rotate-ccw:{ .lg }  
  [__Refund Methods and Operations__](../order-refund-process.md){ title="Refund Methods and Operations" }  
  Learn the refund scenarios and steps.

</div>



## FAQ

??? quote "Why can't I click "Edit Order" to change items?"
	There are two main reasons:

	1. **Invoice limit:** If CYBERBIZ issues invoices for your store, the system locks editing so the invoice amount always matches the order.
	2. **Delivery status:** If the order is "Preparing" or "Shipped," its items can no longer be changed.

	**Recommendation:** To change the order, cancel it and have the customer place a new order, or contact customer service about manual adjustments.

??? quote "Can a completed order be returned?"
	Yes. Completing an order only means the transaction is done and points are issued; it doesn't affect returns. If the customer asks within the cooling-off period, you can still start the "return process" for the order in the admin. Note that after the return is complete, the system automatically deducts the bonus points earned from the order.

??? quote "Why can't I find an order by entering the customer's email or tracking number?"
	This is usually because of the "matching method." For performance and accuracy:

	- **Email, recipient address, tracking number:** Enter the **complete, exact** value (case-sensitive).
	- **Name, order number:** Partial matches are supported (enter part of the text). Also check for an extra "space" accidentally copied after the keyword.

<!-- ??? quote "What's the difference between a Shop Note and a customer message?"  -->
<!---->
<!-- 	- **Shop Note:** In the middle of the order details, for internal records only (such as style confirmed by phone). **Customers can't see it**.  -->
<!-- 	- **Store message:** In the conversation area at the bottom of the page. Once sent, it also appears in "Order Lookup" on the storefront, and **customers are notified and can see it**. -->
