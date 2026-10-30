---
title: "Set Up Unpaid Reminders"
description: "How to set up automatic unpaid reminders sent through email, SMS, and LINE OA to guide customers to complete payment and improve order conversion."
created:
last_modified: 2026-07-01 12:00
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/unpaid-reminder-settings/"
type: guide
author: Jase
reviewers: []
notes:
  - LINE OA 樣板設定版本限制確認
  - add doc link 串接 LINE OA Messaging API
  - add doc link 串接 LINE 官方帳號與官網會員系統
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
  - 自動提醒顧客付款
  - 提升訂單付款率
  - 自訂提醒頻率
  - 多管道通知
features:
  - 未付款提醒
  - 功能啟閉設定
  - 發送間隔設定
  - 自動停止提醒
  - Email 提醒樣板
  - 簡訊提醒樣板
  - LINE OA 提醒樣板
  - 樣板變數
  - 短網址功能
prerequisites:
  - 完成 LINE OA Messaging API 串接
  - 顧客完成 LINE 帳號綁定並加入商家官方帳號好友
related:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
tags:
  - "Unpaid Reminders"
  - "Unpaid Orders"
  - "Automated Reminders"
  - "Email Reminders"
  - "SMS Reminders"
  - "LINE OA Reminders"
  - "Payment Reminders"
  - "Order Conversion Rate"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 結帳頁 & 物流設定 > 訂單相關設定 > 訂單未付款提醒設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=158
  - https://www.cyberbiz.io/support/?p=2321
comments: false
search:
  exclude: false
icon: lucide/timer
hide:
---

![Unpaid reminder settings](../../../assets/images/ec-訂單-未付款提醒.en.png){ title="Unpaid Reminder Settings" .hero-page }


## About Unpaid Reminders

In CYBERBIZ, **unpaid reminders** automatically notify customers whose orders haven't been paid yet (excluding Cash on Delivery) and guide them to complete payment, improving conversion.

## Turn the Feature On or Off and Set the Interval

You can set how often reminders are sent. The system sends up to **3** reminders.

!!! path "Settings path: **Payment and Logistics > Checkout Page & Logistics > Order Settings > Unpaid Order Reminder Settings**."

**Rules**:

- **Turn on**: Set the **interval in days** (for example, send once every 1 day).
- **Turn off**: Set the interval to **0** to turn it off.
- **Automatic stop**: If the customer pays during the reminder period, the system stops sending further reminders.

---

## Set Up the Three Notification Channels

Unpaid reminders support email, SMS, and LINE OA. You can set up and edit the template for each channel as needed.

!!! warning "Template Editing Notes"

    - **Template variables**: When editing the content, don't change the template variables inside **{{ }}** braces (such as `{{shop_name}}` and `{{customer_name}}`). These codes automatically fill in the site name, customer name, or order number.
    - **Avoid blocked words**: In SMS, avoid words carriers tend to block (such as "claim," "link," and "LINE"), or the message may fail but still be charged.
    - **Short URLs**: We recommend turning on short URLs to automatically shorten links in reminders, saving SMS characters (up to 70 characters per message) and keeping emails concise.

### Email Reminders <small>On by Default</small>

!!! path "**Path:** Push Notifications > Email Notification Template > Customer > **Unpaid Order Reminder Email**."

- Click the title to edit the email subject and body (HTML or plain text), and click "Preview" in the upper-right corner to see how it looks.
- If you make changes, click **Save** to apply them.

![Unpaid reminder email template](../../../assets/images/ec-訊息推播-email 樣板-顧客訂單未付款提醒信.en.gif){ title="Unpaid Reminder Email Template" }

---

### SMS Reminders <small>Turn On Manually</small>

!!! path "**Path:** Push Notifications > SMS Templates > Customer > **Unpaid Order Notification**."

- **Settings**: Switch "Status" to **On (ON)** to turn on automatic SMS reminders.
- **Prerequisite**: Make sure your account has enough credit (merchants not on PLUS / Enterprise plans need to top up in advance).

![Unpaid reminder SMS template](../../../assets/images/ec-訊息推播-簡訊樣板-顧客訂單未付款通知.en.gif){ title="Unpaid Reminder SMS Template" }

---

### LINE OA Reminders <small>Turn On Manually</small>

!!! plan "This feature is available only on PLUS / Enterprise plans."

!!! path "**Path:** Push Notifications > LINE OA Message Templates > Customer > **Unpaid Order Reminder Email**"

**Prerequisites**: Before sending, make sure the following are set up:

- [x] Merchant: Complete the [**LINE OA Messaging API integration**](../../integrations/line/account-integration/connect-line-messaging-api.md){ title="Integrate the LINE Messaging API" }.

- [x] Customer: Members must complete **[LINE account linking](../../integrations/line/account-integration/bind-line-oa-store-members.md){ title="Link Your LINE Official Account with Website Members" }** and add your official account as a friend.

**Settings**:

- **Turn on**: Switch "Status" to **On (ON)**.

- **Edit content**: Edit the reminder text in the "Text Message" field. You can insert variables to fill in order information automatically.

- **Live preview**: Your edits appear in the preview window on the right so you can check how they look.

![Unpaid reminder LINE OA template](../../../assets/images/ec-訊息推播-LINE OA 樣板-顧客訂單未付款提醒信.en.gif){ title="Unpaid Reminder LINE OA Template" }

## Related Tasks

<div class="grid cards" markdown>

- :simple-line:{ .lg }  
  [__Integrate the LINE OA Messaging API__](../../integrations/line/account-integration/connect-line-messaging-api.md){ title="Integrate the LINE Messaging API" }  
 Create a LINE OA and integrate the Messaging API.

- :lucide-link-2:{ .lg }  
  [__LINE Member Linking__](../../integrations/line/account-integration/bind-line-oa-store-members.md){ title="Link Your LINE Official Account with Website Members" }  
  Set delivery conditions for products to limit which delivery types appear and can be used at checkout.

</div>

## FAQ

??? quote "The customer paid but still received a reminder"

	Check the following:

	1. Whether the customer received the reminder after paying (the scheduled reminder may have been created but not yet canceled).

	2. Whether the customer is signed in on multiple devices (such as a phone and a computer):

    - Unpaid reminders are based on the "order status."

    - If the customer pays on one device and the checkout on the other device hasn't been cleared yet, duplicate notifications may be sent for a short time.


	The system stops further reminders the next time it checks the order status.

	Check whether the customer is signed in on multiple devices (such as a phone and a computer). Abandoned cart reminders are usually tied to a device. If the customer checks out on one device and the cart on the other device isn't cleared, duplicate notifications may be sent.

??? quote "Automatic order cancellation and reminders"

	If you set "Automatic Order Cancellation Days" (for example, cancel after 3 days unpaid):

	- Unpaid reminders should be **sent before** the automatic cancellation period ends.

	- Once the system cancels the order automatically, no more unpaid reminders are sent.


	We recommend keeping the total of the reminder intervals shorter than the automatic cancellation period to avoid useless reminders.


??? quote "When does the system send the first unpaid reminder?"

	The system counts from the "order placed time" using the interval you set.

	For example:

	- Interval set to 1 day

	- Order placed on 12/01 at 15:00


	The first reminder is sent **around 12/02 at 15:00**.

??? quote "How many unpaid reminders are sent at most?"

	The system sends up to **3** reminders. If the customer pays after the 1st or 2nd reminder, the remaining reminders are canceled automatically.

??? quote "Which orders don't get unpaid reminders?"

	These don't trigger reminders:

	- Cash on Delivery (COD) orders

	- Orders already paid

	- Canceled or closed orders

	Unpaid reminders apply only to orders with "online payment not yet completed."

??? quote "Can I send reminders only for specific payment methods?"

	No. Unpaid reminders are currently a **store-wide setting** and can't be set by payment method (such as credit card or convenience store barcode).

??? quote "Why didn't LINE OA send a reminder?"

	Check these prerequisites:

	1. Whether you completed the LINE OA Messaging API integration.

	2. Whether the customer completed LINE account linking.

	3. Whether the customer added your official account as a friend.

	4. Whether the LINE OA template is turned on (status is ON).

	If any condition isn't met, the system can't send LINE OA reminders.

??? quote "What if an SMS reminder fails?"

	Whether an SMS is delivered ultimately depends on the carrier's result. If the content includes words likely to be blocked (such as "link," "free," "claim," and "LINE"), sending may fail.

	We recommend avoiding sensitive words and using short URLs to lower the risk.

