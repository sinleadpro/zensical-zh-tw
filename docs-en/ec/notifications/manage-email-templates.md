---
title: "Set Up And Manage Email Notification Templates"
description: "Manage and edit the email notification templates the system sends automatically, including custom content, enabling templates, recipient settings, and multi-language versions."
created:
last_modified: 2026-07-01 21:55
lang: en-US
permalink: "https://help.cyberbiz.io/ec/notifications/manage-email-templates/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訊息推播
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
  - 管理 Email 樣板
  - 自訂 Email 通知
  - 設定商家提醒
  - 多國語系 Email 設定
features:
  - Email 通知
  - Email 樣板自訂
  - 收件者設定
  - 多國語系支援
  - 短網址功能
  - "Merchant notifications"
prerequisites: []
related:
  - ec/website-management/setup-store-basic-info/
  - ec/orders/home-delivery/shipping-status-tooltip/
  - ec/notifications/manage-sms-templates-v2/
  - ec/notifications/manage-line-oa-templates/
  - ec/website-management/setup-customer-email-phone-verification/
tags:
  - "Email notification templates"
  - "Email template management"
  - "Email settings"
  - "Email multi-language"
  - 商家通知
  - "Short URL"
  - "Notification management"
  - "Email automation"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=11195
  - https://www.cyberbiz.io/helpcenter/?p=2061
  - https://www.cyberbiz.io/support/?p=7709
  - https://www.cyberbiz.io/support/?p=7742
comments: false
search:
  exclude: false
icon: lucide/mails
hide:
---

![Email notification templates page](../../assets/images/ec-訊息推播-email 通知樣板.png){ .hero-page }

## About Email Notification Templates

**Email notification templates** let you customize the automated emails sent to customers or admins, and turn notifications for specific situations on or off to suit your operations.

## Path And Page Overview

- **Admin path**: Go to **Push Notifications > Email Notification Template**.

- **Template categories**: Emails are grouped into the following categories to make them easier to manage:

	- **Orders**: For example, order confirmation and payment success notifications.

	- **Shipping**: For example, shipment reminders and arrival-at-store reminders.

	- **Customers**: For example, account activation, password change, and birthday gift notifications.

	- **Returns**: For example, return request confirmation notifications.

	- **Subscription orders**: Order-created or skipped notifications for subscription orders.

!!! info "The email categories and templates available to you depend on your plan and feature settings."

## Edit An Email

1. **Open the editor**: In the list, click the **email title** you want to edit.

2. **Edit the content**:

	- You can freely edit the subject and body, in either **HTML template** or **plain text** format.

	- **Variables**: Tags in the body wrapped in **{{ }}** (such as `{{shop_name}}` and `{{order_number}}`) are system variables that are filled in with real data automatically. **Don't change them or their spelling**, or the email may fail to send.

	- **Symbols**: Don't use **emoji** or other special symbols when editing, or the email may display incorrectly.

3. **Preview and save**: When you're done, click **Preview** to see how the email looks, then click **Save** to apply it.

![](../../assets/images/ec-訊息推播-email 樣板編輯.gif)

## Key Settings

- **On/off switch**: Each template has an **ON/OFF** switch on the right, so you decide whether that notification is enabled.

- **Short links**: Click the **Short link** option to turn it on or off. **When it's on**, long links in the email body are automatically converted to short links, which keeps emails shorter and tidier.

	![](../../assets/images/ec-訊息推播-email 樣板設定-短網址與功能開關.png)

---

### Merchant Notification Settings

At specific triggers (such as an order being placed or a payment succeeding), you can also send system notifications to relevant staff or partners.

#### Permissions And The Main Email Address

- **Default recipient (main email address)**: By default, notifications go to the site admin's main email address.

- **Where to change it**: To [change the main email address](../website-management/setup-store-basic-info.md#operate-general-preferences-company-info){ title="設定網站基本資訊" }, go to **Website Management > General**.

#### Recipient Types

After you click **Add recipient**, you can choose recipients in three ways:

|**Type**|**Description**|**Rules**|
|---|---|---|
|**Store email**|The default.|Uses the main email address entered in General settings.|
|**Custom**|Enter external email addresses manually.|Separate multiple addresses with a **half-width comma (`,`)**.|
|**Admin users**|Choose from existing admin accounts.|Select an existing account name from the menu.|

![](../../assets/images/ec-訊息推播-email 樣板設定.png)

## Common Scenarios And Notification Types

System notifications are either customer notifications or internal merchant notifications. Here's how each is sent and through which channels:

### Automated Customer Notifications

These notifications keep customers up to date on their orders and accounts.

|**Notification type**|**When it's sent**|**Channels**|
|---|---|---|
|**Shipping notification**|**Sent only when the delivery status changes to "Shipped (in transit)"**, so the package is already with the carrier. See [Shipping status notes](../orders/home-delivery/shipping-status-tooltip.md#shipping-status-text-type){ title="出貨狀態物流提示文字說明" data-preview }  .|Email, SMS, LINE|
|**Order status changes**|Sent when an order is placed, paid, or canceled.|Email, SMS, LINE|
|**Member benefit notifications**|Includes account activation, password reset, birthday gift credits, and more.|Email, SMS|

!!! tip "Multi-channel sending"
	If you turn on several channels (such as email and LINE), the system sends through all of them based on your settings. For important messages such as shipping notifications, we recommend turning on more than one channel so they get through.

---

### Internal Admin Notifications

These notifications go only to the addresses set in Merchant notification settings (such as warehouse or finance staff), never to customers.

- **Order management**: New orders and customer return requests.

- **Safety stock reminders**: When a product's stock falls below the set level, the system emails your purchasing staff.

- **Job results**: Success or failure reports after bulk Excel imports (products, members).

- **Billing and reconciliation**: Payment charges, statement generation, and other financial information.


## Multilingual Settings <Small>Optional</small>

If your site has multiple languages turned on, set up each email template separately for each language:

1. In the editor, click the **:lucide-globe: language icon** to switch to the language you want to edit (such as English).

2. Save each language separately. If a language's fields are left empty, the system usually shows the Traditional Chinese content instead.

## Next Steps

<div class="grid cards" markdown>

- :lucide-message-square-text:{ .lg }
  [__Manage SMS notification templates__](manage-sms-templates-v2.md){ title="設定與管理簡訊通知樣板" }
  Set up and manage SMS notification templates, including editing rules and blocking risks.

- :simple-line:{ .lg }
  [__Manage LINE OA message templates__](manage-line-oa-templates.md){ title="設定與管理 LINE OA 通知樣板" }
  Set up and manage automated LINE OA templates, including prerequisites, setup, and supported scenarios.

</div>

## FAQ

??? quote "When is the "Shipping information change reminder" email sent? Is it sent when I change an order's delivery address?"
	No, changing the delivery address doesn't trigger this email. It's sent to the customer only when the order's delivery status is "Shipped", "Arrived at store", "Picked up", or "Store closed".

??? quote "If I turn on "Order canceled reminder (admin)", will it notify me about orders automatically canceled for nonpayment?"
	No. Admins are notified only about orders that customers cancel.

??? quote "Why didn't the merchant or customer receive the notification email?"

	- **Spam filtering**: The email may have gone to spam. Ask merchants and customers to check their Gmail spam folder and add `support@cyberbiz.io` and `noreply@cyberbiz.co` to their contacts.

	- **Gmail filters**: To make sure emails arrive, create a Gmail filter that sets the official domains above to "Never send it to Spam".

	- **Hinet mailboxes**: Hinet (msa.hinet.net) blocks more aggressively, so members who register with it are more likely to miss emails or not get "password reset" emails. We recommend asking these customers to use Gmail or Outlook instead.

??? quote "Why didn't the merchant or customer receive system notification emails?"

    This is usually caused by the email provider's filtering. Try these steps:

    - **Check the spam folder**: The email may have been flagged as advertising or risky. Check the spam folder in Gmail or another email service, and add `support@cyberbiz.io` and `noreply@cyberbiz.co` to your contacts.

    - **Set up a Gmail filter**: To avoid missing future emails, create a Gmail filter that sets the official domains to "Never send it to Spam".

    - **Switch email providers (ISPs)**: Telecom mailboxes such as Hinet (`msa.hinet.net`) block more aggressively and often stop "password reset" or "order notification" emails. If this happens often, ask customers to switch to Gmail or Outlook for reliable delivery.

??? quote "When is the "Shipping notification" sent?"

	The email is sent only when the order's delivery status changes to "**Shipped (in transit)**". This makes sure the carrier has actually picked up the package, so customers don't get a premature notice when you've only created a shipping label (awaiting pickup).

??? quote "How are "Unpaid reminders" sent?"

	You can set reminders to be automatically sent *N* days after an order is placed. If the customer pays within the set interval, the remaining reminders for that order are canceled automatically so they aren't sent again.

??? quote "Can store managers (or staff other than the main account) receive safety stock notifications?"

	Yes. Store managers can only see their own store's information, so to receive "safety stock" or other store-wide notifications, the **site owner (Owner)** must manually add their email to the recipient list in Merchant notification settings.

??? quote "Why does checkout still show "Send verification code" when members log in, even though the notification template is off?"

    Whether "Send verification code" appears depends on whether **email verification** is turned on, not on the notification template. Once verification is on, checkout shows the option; if the matching notification template is off, no verification email is sent.

    [Set up two-step email and mobile verification for customers :lucide-arrow-right:](../website-management/setup-customer-email-phone-verification/)
