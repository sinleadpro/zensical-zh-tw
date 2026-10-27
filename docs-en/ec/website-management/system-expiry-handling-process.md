---
title: "System Expiry Handling Process"
description: "Explains the reminder rules for expiring system services, how to renew, and how data is handled if you do not renew, including domain transfer steps and emergency measures."
created: 2026-05-27 11:40
last_modified: 2026-06-30 08:02
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
  - POS
modules:
  - 官網設定
  - 管理中心
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
  - 了解系統到期通知規則
  - 執行網域移轉
  - 處理到期緊急應變
features: 
  - 系統到期提醒
  - "Domain Transfer"
  - 緊急網域切換
prerequisites: []
related:
  - ec/website-management/renewal-and-auto-subscription/
  - pos/store/renewal-and-add-on-plans/
tags: 
  - "System Expiry"
  - Renewal
  - 網域移轉
  - SSL
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: []
paths: 
  - 管理中心 > 網域管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3988
  - https://www.cyberbiz.io/support/?p=21601
permalink: "https://help.cyberbiz.io/ec/website-management/system-expiry-handling-process/"
comments: false
search:
  exclude: false
icon: lucide/calendar-clock
hide: []
---

# System Expiry Handling Process
Explains the reminder rules for expiring system services, how to renew, and how data is handled if you do not renew.
{ .subtitle }


!!! tip "Use Cases"
	- **Renew on time**: Know when the system sends expiry notices so you don't miss renewal information when you are busy.
	- **Transfer a domain**: Move a domain managed by CYBERBIZ to your own account so you can manage it yourself.
	- **Handle emergencies**: When an expired SSL certificate or domain makes your website unreachable, switch to a backup domain quickly to get back in business.


## Before You Start { #prerequisites-system-expiry }

- **Back up your data**: If you decide not to renew, export and save all system data (such as customers, orders, products, and images) before the service ends.
- **Admin panel access limits**: After your website expires, you can't enter the admin panel to save or change any data, and shoppers can't visit your website.
- **How reminders appear**: Renewal reminders are tracked per browser. If you select **Read** in one browser, the reminder appears again on the next reminder date. If you switch browsers or use incognito mode, it appears again.

## Steps { #operate-system-expiry }

### 1. Learn How to Renew Each Service { #operate-system-expiry-renew }

System services include the [website system and SSL certificate](renewal-and-auto-subscription.md), the [POS system](../../pos/store/renewal-and-add-on-plans.md), e-invoices ([Wixtar]()), and domains. You can renew them in the admin panel as needed.


### 2. Expiry Reminder Rules { #specs-system-expiry-remind }

The system sends reminders for the **website system**, **POS system**, **SSL certificate**, and **domains bought through CYBERBIZ**.

- **When reminders are sent**: **90, 60, 30, 15, 7, 3, and 1** days before expiry.
- **What to do**: When a reminder appears, select **I have read and agree to the above**.
- **Note**: If you have already asked to transfer the domain to your own management, the reminder may still appear. Just click **Read** or ignore it.

### 3. Transfer the Domain (From CYBERBIZ Management to Your Own) { #operate-system-expiry-transfer }

If CYBERBIZ currently manages your domain and you want to manage it yourself, transfer the domain.

> The example below uses GoDaddy.

1. Go to the **GoDaddy website** and create a personal account.
2. Give your GoDaddy **account email** and **customer number** to your CYBERBIZ renewal consultant.
3. Open the domain transfer confirmation email from GoDaddy, click the link, and select the option to **skip the review and approve all**.

    !!! warning "Important"
        Don't change the contact information at this stage. Otherwise, the transfer may take more than a month.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/系統到期通知說明02.png){ .screenshot }

4. Tell CYBERBIZ that you have confirmed. After the system releases the domain, accept the transfer in your GoDaddy account.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/系統到期通知說明03.png){ .screenshot }


### 4. Handle an Expired Domain or SSL Certificate { #operate-system-expiry-urgent }

When an expired SSL certificate or domain makes your website show as not secure or unreachable, take these emergency steps:

1. Log in to the CYBERBIZ admin panel and go to **Website Management > Domain**.
2. Set the **cyberbiz.co** domain as the primary domain.
3. This temporarily makes your website reachable again. After you renew, switch back to your own domain.

![](https://www.cyberbiz.io/support/wp-content/uploads/系統到期通知說明01.png){ .screenshot }


