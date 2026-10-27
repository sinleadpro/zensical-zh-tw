---
title: "Set Up And Manage LINE OA Notification Templates"
description: "Set up and manage automated notification templates for your LINE Official Account (LINE OA), including prerequisites, template setup, supported scenarios, and billing rules."
created: 2026-02-13 23:26
last_modified: 2026-06-26 06:12
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify the inclusion of 日本台灣站 table
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - "Push notifications"
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定 LINE OA 通知樣板
  - 管理 LINE OA 訊息
  - 自訂 LINE OA 提醒
  - LINE OA 自動化通知
features:
  - LINE OA 通知
  - Flex Message 樣板
  - 純文字樣板
  - "Order notifications"
  - 物流更新通知
  - 到店通知
  - 定期訂單通知
  - 未付款提醒
  - 行銷通知
prerequisites:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
related:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
tags:
  - 訊息推播
  - "LINE OA"
  - 訂單通知
  - "Subscription orders"
  - "Shipping notifications"
  - Automation
  - "Template management"
acoiv: configure
apis:
  - LINE Messaging API
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訊息推播 > LINE OA 通知樣板
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8156
  - https://www.cyberbiz.io/support/?p=728
permalink: "https://help.cyberbiz.io/ec/notifications/manage-line-oa-templates/"
comments: false
search:
  exclude: false
icon: lucide/message-circle-more
hide: []
---

![LINE OA template settings page](../../assets/images/ec-訊息推播-line oa 樣板.png){ .hero-page }

## About LINE OA Message Templates

**LINE OA message reminder templates** automatically push messages to customers in specific situations involving orders, returns, shipping, customers, and subscription orders.

Here's how to set up and use LINE OA message reminder templates:

## Before You Start

Complete the following setup before you use templates:

- [x] [**Connect the Messaging API**](../integrations/line/account-integration/connect-line-messaging-api.md){ title="串接 LINE Messaging API" }  : Connect your LINE Official Account to the admin through the API.

- [x] **Collect LINE UIDs**: Turn on **LINE Login** or guide members through [**linking their LINE Official Account to their website membership**](../integrations/line/account-integration/bind-line-oa-store-members.md){ title="綁定 LINE 官方帳號與官網會員" }  , so the system can collect their LINE UIDs and send them messages.

- [x] **Check friend status**: Customers must be **friends** with your official account and must not have blocked it, or they won't receive messages.

- [x] **Message quota**: Make sure your LINE Official Account has enough message quota. Message fees are charged according to your LINE Official Account plan.

## Set Up A Message Template

1. **Open the page**: Log in to the admin and go to **Push Notifications > LINE OA Message Templates**.

2. **Choose a template**: In the list, click the title of the reminder template you want to turn on to open its editor.

3. **Set the content**:

	- **Status**: Switch the toggle to **ON** to turn on the template.

	- **Notification type**: Choose a **Flex Message template** (rich format) or **Text**.

	- **Edit the text**: You can add to or remove parts of the default content.

	- **Variables**: Tags in the body wrapped in **{{ }}** (such as `{{shop_name}}` and `{{order_number}}`) are system variables that pull in order data automatically. **Don't change them or their spelling**, or the message won't send correctly.

4. **Save**: When you're done, click confirm to apply the changes right away.

![](../../assets/images/ec-推播訊息-line oa 樣板-編輯.png)

## Supported Message Types And When They're Sent

The system supports many automated notification scenarios, including:

- **Shipment reminder**: Sent when the order's delivery status changes to "**Shipped (in transit)**" (only for orders that use integrated shipping and a downloaded shipping label).

- **Arrival-at-store reminder**: Sent when the package arrives at a convenience store (such as FamilyMart, Hi-Life, or T-Cat store pickup).

- **7-Eleven arrival reminder**: Sent when the package arrives at a 7-Eleven store.

- **Subscription order notifications**: A confirmation when the first "parent order" is placed, and a shipping reminder each time a "child order" is created after that.

- **Unpaid reminder**: For orders that haven't been paid, the system automatically sends notifications at the interval you set.

- **Marketing notifications**: For example, reminders that a coupon or reward points are about to expire.


<!--

|**Message type**|**When it's sent**|**Taiwan site**|**Japan site**|
|---|---|---|---|
|**Shipment reminder**|Order status changes to "Shipped".<br>_(only for orders with system shipping labels)_|:lucide-check:|:lucide-check:|
|**Standard arrival reminder**|Package arrives at a FamilyMart, Hi-Life, or T-Cat pickup store.|:lucide-check:|:lucide-x:|
|**7-Eleven arrival reminder**|Package arrives at a 7-Eleven store.|:lucide-check:|:lucide-x:|
|**Store arrival reminder**|Sent when the package arrives at your own physical store.|:lucide-check:|:lucide-x:|
|**Subscription order confirmation**|Sent when a member places the first "parent order".|:lucide-check:|:lucide-x:|
|**Subscription order shipment**|Sent each time a "child order" is created.|:lucide-check:|:lucide-x:|


-->


## Important Notes

- **Billing**: LINE push messages are paid (charged by LINE), including manual pushes and automatic order notifications. Only messages that are **sent successfully** are charged.

- **Tracking limits**: If you don't ship with system-generated shipping labels (for example, with custom shipping), the system can't track the shipment and won't send shipping-related LINE notifications.

- **Timing**: Shipping notifications aren't sent when you download the shipping label. The LINE message goes out only after the carrier **reports the "In transit" status**.

<!--
## Next Steps

<div class="grid cards" markdown>

- :lucide-import:{ .lg }
  [____]()
  .

- :lucide-ban:{ .lg }
  [____]()
  .

</div>
-->

## FAQ

??? quote "Why do customers say they didn't get a LINE notification?"
	Check the following in order:

	1. **Linking**: Has the customer [linked their LINE Official Account to their website membership](../integrations/line/account-integration/bind-line-oa-store-members.md){ title="綁定 LINE 官方帳號與官網會員" }? The system needs their LINE UID to send messages.
	2. **Friend status**: Has the customer blocked your official account?
	3. **Message quota**: Has your LINE Official Account (Manager) reached its message quota?
	4. **Sending conditions**: Does the order meet the sending conditions (for example, did it use integrated shipping and generate a shipping label)?

??? quote "Can I customize the variables in a message (such as {{order_number}})?"
	**No.** Variables inside `{{ }}` are fixed system variables that fill in order information automatically. You can change the text around them, but don't change the spelling or format inside the braces, or the variable will stop working and the message will show the raw code or fail to send.

??? quote "Is the "Shipping notification" sent as soon as I click Ship?"
	**No.** To keep the information accurate, the system doesn't send it when you click "Ship" or "Print shipping label". It waits until the carrier (such as 7-Eleven, FamilyMart, or T-Cat) reports the **"In transit"** status.

??? quote "If I manually change an order's status to "Shipped", is a notification sent?"
	It depends on how you ship:

	- **Integrated shipping**: Notifications are triggered by the carrier's actual tracking status, so changing the status manually usually doesn't send shipping notifications.
	- **Custom shipping**: The system can't track third-party shipments, so automatic shipping notifications aren't supported for these orders.

??? quote "Do LINE notifications use up my message quota?"
	**Yes.** All notifications sent through the Messaging API (including automated template messages) count toward your LINE Official Account's monthly message quota, and fees follow your LINE Official Account plan.
