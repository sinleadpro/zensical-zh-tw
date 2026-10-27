---
title: "Set up Automatic Confirmation of Reconciliation Statements"
description: "When merchants use the CYBERBIZ PAYMENTS payment service, merchants must confirm statements manually before payouts are made by default. After you turn on Automatic Statement Confirmation, the system confirms statements automatically on the statement closing date once the accumulated amount reaches the set threshold, so payouts are not interrupted."
created: 2026-06-01 16:06
last_modified: 2026-06-01 16:06
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 管理中心
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - Professional
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
plan_options: []
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents: 
  - 設定自動確認帳款
  - 避免漏確認撥款
  - 自動化對帳流程
features: 
  - 自動確認帳款
  - "Reconciliation Center"
  - CYBERBIZ PAYMENTS
prerequisites: 
  - "需開通 CYBERBIZ PAYMENTS 金流服務"
related: []
tags: 
  - "Automatic Reconciliation"
  - "Payout Process"
  - "Accounting Automation"
  - 對帳中心
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 對帳中心
  - 自動確認帳款彈窗
paths: 
  - 管理中心 > 對帳中心
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=4507
permalink: "https://help.cyberbiz.io/ec/website-management/auto-confirm-reconciliation-accounts/"
comments: false
search:
  exclude: false
icon: lucide/circle-check
hide: []
---

# Set up Automatic Confirmation of Reconciliation Statements
With the CYBERBIZ PAYMENTS payment service, you must confirm each statement by hand before you get paid. This is the default. If you turn on automatic statement confirmation, the system does it for you on the closing date once the total reaches your threshold. Your payouts keep coming on time.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Professional / Advanced / Expert / all PLUS plans
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ PAYMENTS
{ .doc-badge }

!!! warning "Plan Limits"
    This feature is only for merchants on **standard plans** and **PLUS plans** who **use the CYBERBIZ PAYMENTS** payment service. **Enterprise** merchants can't use it. Their process includes issuing billing invoices.



## Why Turn on Automatic Statement Confirmation? { #intro-auto-confirm }

With CYBERBIZ PAYMENTS, you must go to **Reconciliation Center** and check that the payout amount is right. Only then does the system pay you.

If you are busy and forget to confirm, the payout for that period is late. With this feature on, the system confirms for you at **23:59 on the last confirmation day of each period**. It does so as long as the amount meets your threshold.


## How to Turn It On { #operate-auto-confirm }


1. Log in to the CYBERBIZ admin panel and go to **Website Management > Reconciliation Center**.
1. On the Reconciliation Center page, click the **Statement automatic confirmation** button.
2. In the pop-up window, set the following:
    - **Turn on the switch**: Turn on **Automatically confirm statements**.
    - **Set the amount threshold**: Enter the total at which statements are confirmed for you (for example, NT$3,000).
    - **Enter the accounting email**: Set the email that gets confirmation records and reminders.
3. Read and accept the terms of responsibility, and then click **Confirm** to turn it on.

![](https://www.cyberbiz.io/support/wp-content/uploads/自動確認帳款02.png){ .screenshot }



## How Automatic Confirmation Works { #specs-auto-confirm }

### 1. Amount Threshold { #specs-auto-confirm-threshold }

The system adds up the amounts of **all unconfirmed statement periods**.

- **Threshold reached**: If the total reaches the threshold, the system confirms the statements.
- **Threshold not reached**: If the total is below the threshold, the system waits for later periods to add up. It confirms on the first closing date after the total reaches the threshold.

!!! example "Example"
    The threshold is set to NT$3,000. If two unconfirmed periods add up to NT$2,500, the system does not confirm automatically. When a third period brings the total to NT$3,000 or more, the system confirms automatically.

### 2. When Automatic Confirmation Runs { #specs-auto-confirm-timing }

The system checks and confirms at **23:59 on the last confirmation day of each statement period**.

!!! example "Example"
    If your payouts are weekly and the confirmation deadline is every Tuesday, the system runs late on Tuesday night.

### 3. Notification Rules { #specs-auto-confirm-notify }

- **Feature changes**: Each time you turn this feature on or off, the system emails the accounting address.
- **Run records**: Each time the system confirms for you, it sends an email with the details.
