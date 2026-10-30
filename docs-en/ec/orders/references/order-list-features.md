---
title: "Order List Actions"
description: "Explains the order list actions, including changing order status and delivery status, batch processing, and filter groups."
created: 2026-02-10 22:11
last_modified: 2026-06-29 21:30
lang: en-US
type: reference
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
tnb: ""
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 批次處理訂單
  - 管理訂單狀態
  - 管理配送狀態
  - 管理退貨流程
features:
  - 結案訂單
  - 取消訂單
  - 更改配送狀態
  - 更改退貨狀態
  - 列印訂單明細
  - 列印揀貨單
  - 綁定訂單標籤
  - 補印託運單
  - 再次購買
prerequisites: []
related: []
tags:
  - "Order Management"
  - "Order Status"
  - "Delivery Status"
  - "Return Status"
  - "Order List"
  - "Batch Processing"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/order-list-features/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide: []
---

=== "Change Order Status"

	Use this section to manage the order lifecycle.

	- **Close Order**: Formally closes the order. **After closing, the system automatically issues bonus points, activates coupons, and calculates profit sharing**.
	- **Open Order**: Changes a Completed order back to In Progress so you can edit or adjust it.
	- **Cancel Order**: Available only for **Unshipped** orders. After you cancel, the system automatically returns the bonus points and coupons used on the order.

	!!! info "Closing an order isn't directly related to financial reconciliation. Reconciliation is based on the delivery status "Received" or "Shipped"."

=== "Change Delivery Status"

	You can update the shipment status manually or through the system based on actual logistics progress.

	- **Unshipped**: The initial status after an order is placed.

	- **Preparing**: Items are being prepared. At this point, shoppers **can't cancel the order themselves** on the storefront.

	- **Shipped**:

		- **Custom logistics**: If you use logistics not integrated with the system, switch to this status manually.

		- **Integrated logistics**: With the **Download Shipping Labels and Change Status to Shipped** option, the system requests tracking numbers from the carrier and generates shipping labels, and the status changes to Shipped automatically.

		- **Status Stalled Too Long, Change to Received**: A feature only for **cross-border e-commerce (FBA)**. For orders whose status has stalled for more than 14 days, you change the status manually after confirming, so the payment can be settled.

=== "Change Return Status"

	Handle shoppers' after-sales return requests.

	- **Returning**: You've accepted and are processing the return. You can generate a reverse logistics code at this point (such as for a convenience store return service).

	- **Reviewing Return**: The stage where you inspect the items after receiving the return package.

	- **Returned**: Confirm the return and issue the refund. For automatic payment services, the system starts the card refund at this point.

	- **Return Rejected**: If the return doesn't meet your return criteria, switch to this status manually to end the process.

=== "Print Order Information"

	Batch generate the documents you need for warehousing or packing.

	- **Print Order Details**: Generates a PDF with the order's products, amounts, and delivery information.

	- **Print Pick List**: Combines the product items from multiple orders so shipping staff can pick them in one pass.

=== "Assign Order Tags"

	- **Add Tags**: Create your own tag categories (such as VIP customers or rush orders) and tag orders to make filtering easier.

	- **Remove Tags**: Batch remove tags you no longer need.

=== "Advanced and Special Actions"

	- **Reprint Shipping Label**: If a shipping label file is lost or damaged, download the file for the original tracking number again.

	- **Buy Again**: Provides a button to add products from a past order (excluding gifts and add-on deals) to the cart again.

	- **Edit Order**: **Before the order ships**, you can change product variants or quantities on the details page. This isn't available if CYBERBIZ issues invoices on your behalf.

---

