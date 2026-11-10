---
title: "E-Ticket Setup Guide"
description: "A complete guide to creating, selling, redeeming, and managing e-ticket products, covering admin settings, the customer purchase flow, and in-store operations."
created: 2026-01-20 00:00
last_modified: 2026-09-18 14:10
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
  - 商品
  - 管理中心
  - 訂單
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: 
  - optional
cyb_extensions:
  - TICKET
intents:
  - 如何建立電子票券
  - 如何販售電子票券
  - 如何核銷電子票券
  - 電子票券管理
features:
  - 電子票券
  - QR Code
  - 核銷
prerequisites:
  - 新版物流
related:
  - ec/e-ticket/setup-e-ticket-promotions/
  - ec/profit-sharing/
  - ec/e-ticket/setup-e-ticket-store-permissions/
  - ec/marketing/purchase-restrictions/purchase-limit/
tags:
  - E-Ticket
  - QR-Code
  - Redemption
  - "Ticket Splitting"
  - Reconciliation
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 電子票券列表 > 新增票券
  - 管理中心 > 顧客註冊設定
  - 商品 > 核銷票券頁
  - 商品 > 票券核銷列表
  - 管理中心 > 網站權限 > 管理者列表
  - 訂單 > 電子票券訂單
  - 訂單 > 所有訂單
  - 金物流 > 結帳頁&金物流設定 > 訂單相關設定 > 訂單自動結案設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5807
  - https://www.cyberbiz.io/support/?p=23413
permalink: "https://help.cyberbiz.io/ec/e-ticket/e-ticket-setup-guide/"
comments: false
search:
  exclude: false
icon: lucide/compass
hide: []
---
# E-Ticket Setup Guide
A complete guide to creating, selling, redeeming, and managing e-ticket products, covering admin settings, the customer purchase flow, and store operations.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    - On PLUS plans, "E-Ticket" is an optional module (choose 2 of 11). Make sure you have selected this module before using it. The Enterprise plan includes this feature.

![](../../assets/images/ec-e-ticket-hero.zh-tw.en.png){ .hero-page }


## E-Ticket Limits and Rules { #prerequisites-e-ticket }

- You can add e-tickets to a [purchase limit group](../marketing/purchase-restrictions/purchase-limit/) to limit how many tickets each customer can buy.  
- E-tickets support only [E-Ticket Discounts](setup-e-ticket-promotions.md) and [Profit Sharing](../profit-sharing/index.md). They can't be combined with other promotions.  
- The only supported payment method is **one-time credit card payment**.

!!! info "Ticket Issuer"
	The ticket issuer is Cyberbiz Corporation. The ticket face value is the actual selling price (including discounts) and is deposited in the issuer's "trust account" at Bank SinoPac. The funds are used only for this purpose to guarantee fulfillment.

## Create an E-Ticket { #operate-e-ticket-create }

Create an e-ticket product.

1. Log in to the CYBERBIZ admin and go to **Products > E-Ticket List > New E-Ticket**.
2. Fill in the information in order: basic settings, ticket images, and variant management.

	![](../../assets/images/ec-e-ticket-type.zh-tw.en.png)

3. Click **Save** to apply your changes. The system automatically creates a variant named **E-Ticket Option**.

    !!! info "Unlike regular products, e-ticket products don't have editable colors or sizes."

    ??? example "Ticket Type Examples"
      - Event tickets: such as *early bird tickets* and *group tickets*.
      - Product vouchers: such as a *Slam Dunk voucher set* and a *Dragon Ball voucher set*.

4. New e-tickets appear in the **E-Ticket List**.

## Buy E-Tickets <small>Customer Flow</small> { #operate-e-ticket-purchase }

1. The customer selects an e-ticket on the storefront.  

	![](../../assets/images/ec-e-ticket-notice-frontend.zh-tw.en.png)

    !!! info "The product page shows the ticket notes to remind customers how to use the ticket."

2. If the cart also contains regular products, the system requires a split checkout.
3. Select **Agree to the e-ticket terms**. Checkout can be completed only after this is selected. You can ignore the **Delivery Time** in the cart.

	![](../../assets/images/ec-e-ticket-contract-agreement.zh-tw.en.png)

4. Complete checkout.

## View Purchased E-Tickets { #overview-e-ticket-purchased }

After payment is complete, customers can view the QR code (redemption code) in these ways:

- **Member account**: My Account > E-Ticket Order Inquiry  
- **Email**: The system sends an e-ticket confirmation email

=== "E-Ticket Order Inquiry"

	1. Go to **My Account > E-Ticket Order Inquiry**.  
	2. Click **Show ticket QR code**.

		<div class="grid cards" markdown>

		- ![](../../assets/images/ec-customer-e-ticket-order-search.zh-tw.en.png)
		- ![](../../assets/images/ec-e-ticket-click-to-view-qr-code.zh-tw.en.png)

		</div>

=== "E-Ticket Confirmation Email"

	!!! note "Member Email Required"
		Make sure "Email" is required in the customer registration settings so the QR code can be sent. If a member hasn't provided an email address, the system can't send it.

	1. Log in to the CYBERBIZ admin and go to **Website Management > Member Registration Setting**.  
	2. Select **Email: Required**.

		![](../../assets/images/ec-member-registration-settings-registration-fields.zh-tw.en.png)

		![](../../assets/images/ec-e-ticket-email-confirm.zh-tw.en.png)


## Redeem E-Tickets <small>Store Operations</small> { #operate-e-ticket-redeem }

There are several ways to redeem e-tickets: entering the code on a computer, scanning with a phone, and looking it up in the admin.

!!! info "To redeem split e-tickets, see how to [redeem codes after ticket splitting](#operate-e-ticket-split-redeem)."

=== "Enter the QR Code on a Computer"

	1. Log in to the CYBERBIZ admin and go to **Products > Redemption Page**.  
	2. Enter the redemption code or scan it with a barcode scanner.  
	3. Enter the redemption quantity and click **Redemption Confirm**.  
	4. Check the information in the dialog and click **Redemption Confirm**.  

	![](../../assets/images/e-ticket-redemption-computer.en.gif)

=== "Scan the QR Code With a Phone"  

	1. Open the camera and scan the QR code.  
	2. Open the web page in a browser. After you log in, you're redirected to the **Redemption Page**.  
	3. Enter the redemption quantity and click **Redemption Confirm**.  
	4. Check the information in the dialog and click **Redemption Confirm**.  

	![](../../assets/images/e-ticket-reconciliation-mobile.en.gif)

=== "Admin E-Ticket Redemption List"
	If a customer forgets to bring the QR code or can't show it for some reason, you can look up the redemption code by name or phone number.

	1. In the CYBERBIZ admin, go to **Products > E-Ticket Redemption List**.
	2. In "Select search category", you can filter tickets by these fields:
	    - Ticket name  
	    - Redemption code  
	    - Order recipient name  
	    - Order recipient phone  
	    - Order number  

	3. After you find the ticket, click **Go to Redeem** to open the **Redemption Page**. The redemption code is filled in automatically.
	4. Enter the redemption quantity and click **Redemption Confirm**.  
	5. Check the information in the dialog and click **Redemption Confirm**.

	![](../../assets/images/ec-e-ticket-redemption-list-filter.zh-tw.en.png)

	![](../../assets/images/ec-e-ticket-redemption-list.en.gif)

=== "Redeem Manually on the Admin Redemption Page"

	1. Log in to the CYBERBIZ admin and go to **Products > Redemption Page**.
	2. Enter the **ticket redemption code** in the redemption field and click **View E-Ticket**.
	3. After you confirm the ticket information is correct, enter the **redemption quantity** for this redemption.
	4. Click **Redemption Confirm** to complete the redemption.

!!! note "Additional Notes"  
    - If you don't have the redemption code yet, go to **Products > E-Ticket Redemption List** to look up the ticket's redemption code.  
    - After redemption, the system immediately updates the ticket's redeemed quantity and status.

    ![](../../assets/images/ec-e-ticket-redemption-page.zh-tw.en.png)

## Create E-Ticket Store Clerk Accounts { #operate-e-ticket-staff-account }

!!! warning "Permission Limits"
    Store clerks can only use the **E-Ticket Redemption List** and the **Redemption Page**. They can't change ticket settings or other permissions.

1. Log in to the CYBERBIZ admin and go to **Website Management > User Account Settings > Manager List**.
2. Click **New Branch Store Manager**.
3. Under the **Branch Store** type, select **E-Ticket Store**. E-ticket store clerk permissions are system defaults and can't be changed[^permission-notice].

4. Enter the store clerk's user information. **Store staff** and **e-ticket store staff** are different roles. Create a separate account for each[^separate-accounts].
5. Click **Add** to finish.

[^permission-notice]: If you try to change the permissions and save, the system shows the message "Branch store user permissions cannot be changed".
[^separate-accounts]: Use a different account and password.

![](../../assets/images/ec-new-branch-store-manager.zh-tw.en.gif)

!!! info "For more e-ticket store permission settings, see [Set Up E-Ticket Store Permissions](setup-e-ticket-store-permissions.md){ title="Set Up E-Ticket Store Permissions" }."

## E-Ticket Refunds { #operate-e-ticket-refund }

### Refund Notes { #prerequisites-e-ticket-refund }

#### Core Ticket Refund Rules { #specs-e-ticket-refund-rules }

- **One-time operation**: Each order supports only **one** return and refund operation.
- **No refunds after redemption**: Tickets that have been redeemed can't be refunded.
- **No partial quantity**: You must refund **all unredeemed tickets** under the ticket code. The system doesn't support refunding a specific partial quantity.
- **Proportional fee refund**: Fees are automatically refunded in proportion to the amount.

#### Ticket Structure and Refund Scenarios { #specs-e-ticket-refund-scenarios }

Based on the number of tickets in a ticket code, refunds are determined as follows:

| Ticket structure | Redemption status | Refundable? | Notes and limits |
| :--- | :--- | :--- | :--- |
| **One code with a single ticket** | Not redeemed | ✅ **Refundable** | Full refund through the standard process |
| | Redeemed | ✕ **Not refundable** | Tickets can't be refunded once redeemed |
| **One code with multiple tickets** | None redeemed | ✅ **Refundable** | All tickets under the code are fully refunded at once |
| | Partly redeemed | ✅ **Partial refund** | **All remaining unredeemed tickets are refunded** |
| | All redeemed | ✕ **Not refundable** | Everything has been redeemed, so no refund is possible |

!!! example "Multi-Ticket Refund Example"
    Suppose one e-ticket code contains **10** tickets:

    - **3** have been redeemed so far, and **7** remain unredeemed.
    - When the merchant processes the ticket refund, the system refunds **all 7 remaining tickets**.
    - **Limit**: The merchant can't choose to "refund only 2". The entire remaining balance must be processed.

### Ticket Refund Process { #operate-e-ticket-refund-flow }

#### 1. Customer Requests a Ticket Refund { #operate-e-ticket-refund-request }

- When a customer wants to request a ticket refund, direct them to the **E-Ticket Order Inquiry** page.
- The customer submits the refund request to the merchant through the order's **Inquiry Record** feature.

![](../../assets/images/ec-e-ticket-list-search-ask-record.zh-tw.en.png)

---

#### 2. Merchant Receives and Confirms the Refund Request { #operate-e-ticket-refund-receive }

- The merchant receives the customer's refund message on the admin **Order List** page.
- Check that the order number, customer information, and refund request are correct.

---

#### 3. Check the Refund Scenario and Ticket Status { #operate-e-ticket-refund-confirm }

Before you process the refund, check the following:

- The **number of ticket types** in the order
- The **redemption status** of each ticket

Different order scenarios affect the ticket refund process. Handle them by type: [single ticket type](#specs-e-ticket-single) or [multiple ticket types](#specs-e-ticket-multiple).

<div class="grid cards" markdown>

- ![](../../assets/images/ec-e-ticket-single-kind.zh-tw.en.png){ title="Single Ticket Type" }
- ![](../../assets/images/ec-e-ticket-multiple-kinds.zh-tw.en.png){ title="Multiple Ticket Types" }

</div>

### Orders with Only One Ticket Type { #specs-e-ticket-single }

- Not redeemed > Cancel the order directly  
- Redeemed > Use the partial refund process

=== "Ticket Not Yet Redeemed"
    If the ticket hasn't been redeemed, you can go straight to the order cancellation process.

    1. In the order list, find and click the order you want to cancel to open the order details page.
    2. Click **Cancel Order**, confirm the information is correct, and click **Cancel This Order**.

        ![](../../assets/images/ec-e-ticket-cancel-order.zh-tw.en.gif)

    3. Confirmation screen

        ![]( ../../assets/images/ec-e-ticket-order-cancelled.zh-tw.en.png)

=== "Ticket Already Redeemed"
    If the ticket has been redeemed, you must use the partial refund process. (If the customer paid today, a partial refund can be processed starting the next day.)

    1. In the CYBERBIZ admin, go to **Orders > E-Ticket Orders**. Select the order in the order list, click **Actions...**, and select **Returning**.
    2. Select the order, click **Actions...**, and select **Reviewing Return**.
    3. Click the order name to open the order edit page. Under partial refund, select the ticket product and click **Confirm Refund**.
    4. Check the refund information again and click **Confirm Refund**.

    ![](../../assets/images/ec-e-ticket-redemped-partial-return.zh-tw.en.gif)

### Orders with Multiple Ticket Types { #specs-e-ticket-multiple }

- None redeemed > Cancel the order  
- Partly redeemed > Partial refund process

=== "No Tickets Redeemed Yet"
    If none of the tickets in the order have been redeemed and the customer wants a full refund, you can use the [order cancellation process](#Orders-with-Only-One-Ticket-Type).

=== "Some Tickets Redeemed"
    If some tickets in the order have already been redeemed, or the customer wants to refund only certain ticket types, you must use the partial refund process.

    1. In the CYBERBIZ admin, go to **Orders > All Orders**. Select the order in the order list and click **Returning**.
    2. Select this order and click **Reviewing Return**.
    3. Open the order page. Under partial refund, select the ticket products to refund and click **Confirm Refund**.

        ![](../../assets/images/ec-e-ticket-multiple-kinds-redemped-partial-returen.zh-tw.en.png)

        !!! tip "If the customer wants to refund only “CYBER Music Festival - Single-Day Ticket”, select only that item."

    4. Click **Confirm** to complete the refund.
        !!! example "Example"
          The remaining 3 "CYBER Music Festival - Single-Day Ticket" tickets are fully refunded, and their QR code is voided. "Pikachu Experience Voucher - Early Bird" isn't refunded, so it can still be used as usual.

## Split E-Tickets <small>Customer Side</small> { #operate-e-ticket-split }

!!! note "Usage Notes"

	-   Ticket splitting can't be undone. (One QR code can be split into several, but several QR codes can't be merged into one.)
	-   After splitting, the original redemption code can no longer be used.
	-   E-tickets are bearer tickets. Anyone with the redemption code can use them, so keep them safe.
	-   A [refund](#operate-e-ticket-refund) can only be requested by the original customer. Remind customers not to split tickets for others casually, to avoid later disputes.

Split a ticket that can be redeemed multiple times into several separate QR codes (ticket splitting) for others to use.


1. Log in as a member on the storefront, click **My Account > E-Ticket Order Inquiry**, and click the **Split Ticket** button.

	![](../../assets/images/ec-e-ticket-split-button.zh-tw.en.png)

2. Check the notice and click **Confirm Split**.
3. After splitting, the QR code is split into several (swipe left or right to see the other QR codes).

    !!! note "Redemption codes are 10 characters before splitting and 25 characters after splitting."

    ??? example "Split QR Code Example"
        ![](https://www.cyberbiz.io/support/wp-content/uploads/電子票券設定35.png){ .screenshot }

### View Split Tickets { #operate-e-ticket-split-view }

1. Log in to the CYBERBIZ admin and go to **Products > E-Ticket Redemption List**.
2. Click **View** to open a dialog that shows all redemption codes for the ticket and their redemption status.

!!! note "For split tickets, the redemption code column shows a **View** button."

![](../../assets/images/ec-e-ticket-split-check.zh-tw.en.png)

---

### Redeem Codes After Ticket Splitting { #operate-e-ticket-split-redeem }

After splitting, the ticket no longer has a **Go to Redeem** button on the E-Ticket Redemption List page. Go to the **Redemption Page** and enter the redemption code to redeem it.

1. Log in to the CYBERBIZ admin and go to **Products > Redemption Page**.
2. Enter the redemption code to redeem it. (Split redemption codes are 25 characters. The redemption quantity defaults to 1 and can't be edited.)
3. Click "View E-Ticket", then click **Redemption Confirm**.

![](https://www.cyberbiz.io/support/wp-content/uploads/電子票券設定37.png){ .screenshot }

## E-Ticket Reconciliation { #reference-e-ticket-reconciliation }

When collected e-ticket payments are paid out, how fees are refunded, and where to view the statement.

### Reconciliation Rules { #reference-e-ticket-reconciliation-rules }

- Payout timing for collected payments: Collected e-ticket payments are paid out **when the ticket is redeemed**.

!!! example "Example"
    An order is placed and paid on 10/5. It contains one ticket type, 5 tickets at NT$200 each, for an order total of NT$1000. The customer redeems two tickets on 10/22, with a face value of NT$400. The payout for the second half of October then includes the two redeemed tickets, totaling NT$400.

- If tickets are refunded, ticket fees are refunded **proportionally**.

!!! example "Example"
    An order contains one ticket type with 5 tickets. 2 have been redeemed and the other 3 are refunded, so the fees for those 3 tickets are refunded.

### Where to Find the Statement { #reference-e-ticket-reconciliation-location }

See the image below for where to find the e-ticket statement.

![](https://www.cyberbiz.io/support/wp-content/uploads/電子票券設定31.png){ .screenshot }

## Ticket Profit Sharing and Automatic Order Completion { #specs-e-ticket-revenue-close }

!!! note "Usage Notes"

	-   Even if a ticket hasn't been redeemed, the order is still completed automatically and profit sharing is calculated.
	-   Returns or cancellations processed after the order is completed don't affect profit sharing that has already been recorded.
	-   Tickets can be used with referrer profit sharing. Profit sharing is calculated when the order is completed.

Set e-ticket orders to complete automatically and calculate profit sharing.

1. Log in to the CYBERBIZ admin and go to **Payment and Logistics > Checkout Page & Logistics > Order Settings > Automatic Order Completion Settings**.
2. Turn **Enable automatic completion of ticket orders** on (ON) or off (OFF).
3. Set ticket orders to **complete automatically N days after the customer pays** so that profit sharing for ticket orders is calculated automatically.

![](../../assets/images/ec-orders-auto-closing-e-ticket.png.zh-tw.en.png)

## Next Steps { #next-steps-e-ticket }

<div class="grid cards" markdown>

- :lucide-ticket-percent:{ .lg }  
  [__E-Ticket Promotions__](setup-e-ticket-promotions.md){ title="Set Up E-Ticket Promotions" }  
  Import an edited product Excel file to update product descriptions and delivery settings for multiple products at once.

- :lucide-key:{ .lg }  
  [__E-Ticket Store Permission Settings__](setup-e-ticket-store-permissions.md){ title="Set Up E-Ticket Store Permissions" }  
  Set the delivery conditions for products to limit which delivery methods appear and can be used at checkout.

</div>
