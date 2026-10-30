---
title: "Edit Order Content"
description: "Use the Edit Order feature, including steps to add or remove products, add custom items or discounts, and add shop notes."
created: 2026-04-29 12:14
last_modified: 2026-07-13 11:01
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules:
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: "beginner"
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 編輯訂單內容
  - 增減或移除商品
  - 新增商品到訂單
  - 新增自訂品項或折扣
  - 修改商家備註
features:
  - 編輯訂單
  - 自訂品項
  - 自訂折扣
  - 商家備註
prerequisites: []
related:
  - ec/products/create-and-manage/product-management-interface/
tags:
  - "Order Management"
  - "Edit Order"
  - "Product Changes"
  - "Custom Items"
  - "Shop Notes"
acoiv: "operation"
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 編輯訂單按鈕
  - 新增商品按鈕
  - 自訂品項表單
  - 自訂折扣表單
  - 商家備註文字框
paths:
  - 訂單 > 所有訂單 > 訂單編號 > 編輯訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12382
  - https://www.cyberbiz.io/support/?p=51419
  - https://www.cyberbiz.io/support/?p=50824
permalink: "https://help.cyberbiz.io/ec/orders/basics/edit-order-content/"
comments: ""
search:
  exclude: false
icon: lucide/square-pen
hide:
---

![Edit order content page](../../../assets/images/EC-訂單-編輯訂單頁面-hero.en.png){ title="Edit Order Content Page" .hero-page }

## About Editing Orders

The **Edit Order** feature lets you change product quantities and variants in an order before it ships, without asking the customer to cancel and reorder, which makes processing more efficient.

## Prerequisites and Limitations

Before editing, make sure the order meets the following conditions. Otherwise, editing isn't supported:

- [x] **Order Status**: Only "In Progress" orders. "Canceled" or "Completed" orders can't be edited (reopen a completed order manually first).
- [x] **Delivery Status**: Only "Unshipped" or "Preparing," and the return status must be "No Return Needed."  
- [x] **ERP integration**: Supported, but make sure the ERP pulls data after the edit so it syncs the latest information.
- [x] **Exclusions**:
    *   **Invoice integration**: If **CYBERBIZ issues invoices** for your store, editing orders isn't supported.
    *   **Warehouse shipping**: Orders shipped by **CYBERBIZ Warehouse (WMS)** can't be edited.
    *   **Order types**: Subscription, Quick Delivery, store pickup, Shop.com referral, and third-party commission orders, and orders using multiple "discount-type" coupons, aren't supported.

    !!! info "Coupon Rules"

        - Not supported: Multiple "discount-type" coupons in one order.
        - Supported: Orders using multiple "free shipping" or "gift" coupons can still be edited.

- [x] **Product limits**: Bundles, gifts, Bonus Mall items, LINE group-buy products, add-on items, e-tickets, POS products, and connected-warehouse products **can't** be edited or added.

## Steps

### Open the Edit Order Page { #edit-order-page }

1.  **Open the order**: In the admin, go to **Orders > All Orders**, select the order to edit, and click its "order number" to open the order details page.
2.  **Start editing**: Click **Edit Order** in the upper-right corner.

    ![Edit order button](../../../assets/images/EC-訂單詳情頁-編輯訂單按鈕.en.png){ title="Edit Order Button" }

3.  **Make changes**: On the edit order page, you can:

    <div class="grid cards" markdown>

    - :lucide-minus-circle:{ .lg .middle }
      [Change or Remove Products](#edit-order-adjust-remove){ title="Change or Remove Products" }

    - :lucide-plus-circle:{ .lg .middle }
      [Add Products](#edit-order-add-product){ title="Add Products" }

    - :lucide-settings:{ .lg .middle }
      [Custom Items/Discounts](#edit-order-custom){ title="Custom Items/Discounts" }

    - :lucide-sticky-note:{ .lg .middle }
      [Shop Note](#edit-order-note){ title="Shop Note" }

    </div>

---

### Change or Remove Products { #edit-order-adjust-remove }

On the "[edit order page](#edit-order-page)," you can change the quantity of existing products in the order or remove products.

1. Change the quantity in the quantity field, or click delete :lucide-trash-2: to remove the product.
2. When you're done, click "Confirm Edit," then click "Confirm and Submit" in the confirmation dialog to apply the changes.

![Change or remove products](../../../assets/images/EC-訂單詳情頁-編輯訂單-增減或移除商品.en.png){ title="Change or Remove Products" }

---

### Add Products { #edit-order-add-product }

On the "[edit order page](#edit-order-page)," you can add new products to the order.

1. Click "Add Product," search in the dialog (see [product filters](../../products/create-and-manage/product-management-interface.md#篩選器使用邏輯){ title="Product Management Interface Overview" data-preview }), select products, and click **Confirm Add** to add them (only products with the same temperature zone and channel).

    ![Add products](../../../assets/images/EC-訂單詳情頁-編輯訂單-新增商品.en.png){ title="Add Products" }

2. Added products are marked with an "Added" label so you can tell them apart.

    ![Added product label](../../../assets/images/EC-訂單詳情頁-編輯訂單-已新增標籤.en.png){ title="Added Product Label" }

3. When you're done, click "Confirm Edit," then click "Confirm and Submit" in the confirmation dialog to apply the changes.

---

### Add Custom Items/Discounts { #edit-order-custom }

On the "[edit order page](#edit-order-page)," you can add custom items or discounts to charge extra shipping or give an extra discount.

=== "Custom Items"

    1. Click "Add Custom Item" to open the settings dialog.

        ![Add custom item dialog](../../../assets/images/ec-orders-edit-order-custom-item-popup.en.png)

    2. Fill in these required fields:
        - **Item Name**: Enter the custom item name (for example, extra shipping or packaging fee).
        - **Quantity**: Set the quantity (default 1).
        - **Unit Price**: Enter the unit price (NT$).

        ![Add custom item](../../../assets/images/EC-訂單詳情頁-編輯訂單-自訂品項.en.png){ title="Add Custom Item" }

    3. Click "Confirm" to add the item to the order.
    4. When you're done, click "Confirm Edit," then click "Confirm and Submit" in the confirmation dialog to apply the changes.

=== "Custom Discounts"

    1. Click the "Add Custom Discount" link to open the settings dialog.

        ![Add custom discount dialog](../../../assets/images/ec-orders-edit-order-custom-discount-popup.en.png)

    2. Fill in these required fields:
        - **Discount Name**: Enter the custom discount name (for example, member discount or clearance discount).
        - **Discount Amount**: Enter the discount amount (NT$).

        ![Add custom discount](../../../assets/images/EC-訂單詳情頁-編輯訂單-自訂折扣.en.png){ title="Add Custom Discount" }

    3. Click "Confirm" to apply the discount to the order.
    4. When you're done, click "Confirm Edit," then click "Confirm and Submit" in the confirmation dialog to apply the changes.


---

### Shop Note {#edit-order-note}

On the "[edit order page](#edit-order-page)," you can add an internal note (up to 1,000 characters) for your team's reference.

1. Enter the note in the "Shop Note" text box at the bottom of the edit page.
2. You must also change at least one product (add, delete, or change quantity).
3. When you're done, click "Confirm Edit," then click "Confirm and Submit" in the confirmation dialog to apply the changes.

![Shop note](../../../assets/images/EC-訂單詳情頁-編輯訂單-商家備註.en.png){ title="Shop Note" }

!!! warning "Important Limitation"
    Edit order mode **doesn't support saving note changes alone**. To change only the note, use the "order details page." In edit mode, you must also change products to save.

## Amount Calculation and Differences { #edit-order-payment-adjsutment }

Amounts change after editing as follows:

* **Pricing**: Original products keep the price at the time of order; newly added products use the current price at the time of editing.
* **Promotions**: When you change quantities or remove products, the system **doesn't recalculate** store-wide discounts or spend-threshold discounts.

### Payment and Differences {: #handling-methods }


| Payment Type | Amount Collected by the System | How Differences Are Handled |
| :--- | :--- | :--- |
| **Cash on Delivery** | Amount after editing | The system collects the new amount automatically. |
| **Not cash on delivery** | **Original amount** | Whether paid or not, the system payment link keeps the original price. Arrange additional payments or refunds with the customer yourself and [track them](#非貨到付款訂單差額處理). |


!!! warning "Important Limitations: Refunds and Invoices"
    * **Refunds**: If the amount changes after editing, **automatic refunds aren't supported**. After canceling or returning the order, refund offline and manually change the status to "Refunded."
    * **Invoices**: Issue an allowance or a new invoice yourself based on the actual changes.
    * **Reconciliation**: For merchants using CYBERBIZ PAYMENTS, the original order amount is settled as usual, and you can see the difference before and after editing on the statement.

---

### Handle Differences for Non-Cash-on-Delivery Orders

If a "non-cash-on-delivery" order's amount changes after editing, the system payment link doesn't update the amount. Arrange the additional payment or refund offline with the customer, then update the status manually in the admin.

1. **Check the amount**: In the "Payment Status" field on the order details page, check:
    - **Amount paid**: The total the customer originally paid.
    - **Amount to collect / refund**: The difference created by editing the order.

    ![Order details page: additional payment not received](../../../assets/images/EC-訂單詳情頁-付款狀態-尚未收到補款.en.png){ title="Order Details Page: Additional Payment Not Received" }

2. **Mark it**: After you and the customer complete the additional payment or refund privately, click the matching button:
    - For additional payment: click "Additional Payment Received."
    - For a refund: click "Amount Refunded."

    ![Order details page: confirm additional payment received](../../../assets/images/EC-訂單詳情頁-已收到補款按鈕.en.png){ title="Order Details Page: Confirm Additional Payment Received" }

3. **Check the result**: The "Payment Status" updates to Additional Payment Received or Amount Refunded, which means the difference for this order has been handled.

    ![Order details page: additional payment received](../../../assets/images/EC-訂單詳情頁-已收到補款.en.png){ title="Order Details Page: Additional Payment Received" }

## FAQ

??? quote "Why does the order discount change after I remove a product variant?"
	When you remove an "entire product variant" from the order, the discount allocated to that product is removed too, so the total discount decreases.

	If you only "change the quantity" (without removing the variant entirely), the allocated discount doesn't change.

??? quote "Does product inventory update in real time when editing an order?"
	Yes. The system checks inventory in real time before you submit the edit and updates it to the latest quantity.

??? quote "If inventory is insufficient, how does the system handle existing and added products?"
	It depends on the product:

	1. **Existing products:**
	   The quantity in the original order is kept. If you increase the quantity beyond available inventory, the system shows an "Exceeds inventory limit" message and resets it to the original quantity.

	2. **Added products:**
	   If the product is sold out or exceeds the inventory limit, the system shows a message, and you need to remove it or change it to an available quantity. The system doesn't reserve inventory automatically.

??? quote "Why does an edited order appear on different statements?"
	If you edit an order after it's placed, creating a difference, and the edit happens after the original order's settlement cycle, the difference is settled in a later statement.

	So you may see the "original order amount" and the "difference" on different statements.

??? quote "Does the system reapply promotions after editing an order?"
	No. When you edit an order, the system doesn't recalculate or apply any new promotions (such as spend-threshold discounts, member discounts, or bonus points).

	The matching discount is removed only when you "remove a product that had a discount applied."

??? quote "Does the system notify customers after an order is edited?"
	No. The system doesn't send any email to customers.

	If the order changes, contact the customer to explain the changes and avoid disputes.

??? quote "If the order's package size changes after editing, does the system adjust the logistics settings?"
	No. The system doesn't recalculate or adjust delivery settings.

	You need to handle shipping yourself, for example:

	- Print an additional shipping label in the EC admin
	- Or make the changes in the carrier's system

??? quote "Why doesn't the sum of discount items match the total discount shown on the order?"
	When discounts exceed the product subtotal (for example, products are NT$100 but the discount is NT$120), the system still shows each discount's original amount.

	However, the order total is capped at no less than NT$0 to avoid a negative amount.

??? quote "Can I change only the shop note without changing products?"
	No. When using "Edit Order," you must make at least one product change (such as adding products, changing quantities, or removing products) to save.

	To change only the "Shop Note," do it on the "order details page."

