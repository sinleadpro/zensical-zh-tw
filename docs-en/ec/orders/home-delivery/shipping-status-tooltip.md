---
title: "Shipment Status Tooltip Text"
description: "How the system automatically shows different Shipped tooltip text based on the carrier's shipment status after an integrated-logistics order ships, where the text appears, and when notifications are triggered."
created:
last_modified: 2026-06-30 10:54
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - add doclink for email, sms, line oa notification templates.
  - add contextuallink for email, sms, line oa templates.
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
  - 查詢物流狀態
  - 了解出貨進度
  - 追蹤訂單物流
features:
  - 物流提示文字
  - 出貨狀態顯示
  - 拖拉版型
prerequisites: []
related:
  - ec/notifications/manage-email-templates/
  - ec/notifications/manage-sms-templates-v2/
  - ec/notifications/manage-line-oa-templates/
tags:
  - "Logistics Status"
  - "Shipping Progress"
  - "Delivery Tracking"
  - "Logistics Tooltips"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12005
  - https://www.cyberbiz.io/support/?p=48029
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/shipping-status-tooltip/"
comments: false
search:
  exclude: false
icon: lucide/type
hide:
---

![Logistics hint on the order lookup page](../../../assets/images/ec-會員-訂單查詢頁-物流提示文字.en.png){ title="Logistics Hint on the Order Lookup Page" .hero-page }

In CYBERBIZ, the **shipped status logistics hint** gives you and your customers more precise delivery information, so both can see where the package is in real time.

Here's how the feature works:

## What It Is and What It Supports

- **Trigger**: When you ship an order with **integrated logistics** and click "Download Shipping Label and Change to Shipped," the system adds text next to "Shipped" based on the status returned by the carrier.
- **Supported**:

	- [x] **Integrated logistics orders only**: You must download the shipping label through the system. If you ship with custom logistics, the delivery status stays "Shipped" with no extra text.
	- [x] **Drag-and-drop themes only**: This feature doesn't support default themes.
	- [x] **Order types**: Regular orders and subscription orders.

## Important Notes

- **Shipping label expiration**: If a package isn't sent within **14 days** after the shipping label is created, the tracking number expires. The order list delivery status stays "Shipped," but the hint on the details page stays at "**Shipped (Awaiting Carrier Pickup)**."

- **Contacting carriers**: After you download the shipping label (status shows Awaiting Carrier Pickup), contact the driver according to each carrier's rules. The status changes to "In Transit" only after the driver picks up the package and updates the system.

## Logistics Hint Types { #shipping-status-text-type }

There are two types of hint text, each for a different logistics stage:

|Hint Text|Scenario and Logistics Information|
|---|---|
|**Shipped (Awaiting Carrier Pickup)**|You created a shipping label in the admin, but the carrier **hasn't picked up the package**, or picked it up but **hasn't returned a status yet**. The package hasn't officially entered delivery.|
|**Shipped (In Transit)**|You finished shipping and handed the package to the carrier, and **the carrier has returned a logistics status**. The package has officially entered delivery.|

## Where the Text Appears

!!! info "The logistics hint *doesn't* appear on the admin order list page or in filters."

The logistics hint appears on the following pages for you and your customers:

### Admin

- **Order details page** (path: Orders > All Orders > click the order number).

![Logistics hint on order details](../../../assets/images/ec-訂單明細-物流狀態提示文字.en.png){ title="Logistics Hint on Order Details" }

### Storefront Member Center

- **Order lookup page** (path: **:lucide-user: icon in the upper right of the website > Order Lookup**).

	![Storefront order lookup hint](../../../assets/images/ec-會員-訂單查詢頁-物流提示文字.en.png){ title="Storefront Order Lookup Hint" }

- **Order details page** (path: **:lucide-user: icon in the upper right of the website > Order Lookup > Order Details**).

	![Storefront order details hint](../../../assets/images/ec-會員-訂單明細頁-物流提示文字.en.png){ title="Storefront Order Details Hint" }


## When Automated Shipping Notifications Are Sent

If you turned on shipping notification templates for email, text message, or LINE OA, the system sends messages at the following time:

- **When**: The system sends the notification to the member only when the order delivery status updates to **Shipped (In Transit)**.

- **Why**: This makes sure the carrier actually has the package when the shopper is notified, avoiding inquiries about packages not yet picked up.

## Related Tasks

<div class="grid cards" markdown>

- :lucide-mail:{ .lg }  
  [__Email Notification Template Settings__](../../notifications/manage-email-templates.md)  
  Manage and set up email notification templates.

- :lucide-message-square-text:{ .lg }  
  [__Text Message Notification Template Settings__](../../notifications/manage-sms-templates-v2.md){ title="Set Up and Manage SMS Notification Templates" }  
  Set how text message reminders look.

- :simple-line:{ .lg }  
  [__LINE OA Notification Template Settings__](../../notifications/manage-line-oa-templates.md)  
  Set how LINE Official Account reminders look.

</div>

## FAQ

??? quote "Why does the admin still show "Shipped (Awaiting Carrier Pickup)" after I handed the order to the driver?"
	Usually the carrier hasn't finished scanning the package in, or there's a delay in the data the system receives. Wait 4–8 hours. After the carrier updates the status, the text automatically changes to "Shipped (In Transit)."

??? quote "If I clicked "Download Shipping Label" by mistake, can I change the status back to "Unshipped" manually?"
	As soon as you click "Download Shipping Label and Change to Shipped," the system treats the order as shipped. To undo it, cancel the shipping label first, and then the order status reverts. Note that if the tracking number was created more than 14 days ago, logistics tracking is no longer available.

??? quote "Why do some orders show only "Shipped" in the admin, with no hint text in parentheses?"
	Check whether the order uses integrated logistics. If you use custom logistics (such as delivering yourself or a carrier not integrated with the system), the system can't receive real-time statuses from third-party logistics, so it shows only the basic "Shipped" status.

??? quote "The shopper says they didn't get a shipping text message, but the order shows "Shipped (Awaiting Carrier Pickup).""
	Shipping notifications (email/text message/LINE) are triggered at the "In Transit" stage. If the status stays at "Awaiting Carrier Pickup," the carrier hasn't officially logged the package yet, and the notification is sent automatically when the status changes to "In Transit."
