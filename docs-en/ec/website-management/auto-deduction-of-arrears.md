---
title: "Set up Automatic Deduction of Arrears"
description: "When you use the CYBERBIZ PAYMENTS service and the current statement balance is negative, the system charges the credit card you linked through the automatic arrears deduction mechanism so that your store keeps working normally."
created: 2026-06-01 15:54
last_modified: 2026-06-26 16:29
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents: 
  - 設定欠款自動扣繳
  - 解決帳單負值問題
  - 綁定對帳信用卡
features: 
  - 欠款自動扣繳
  - 對帳中心
  - CYBERBIZ PAYMENTS
prerequisites: 
  - "需開通 CYBERBIZ PAYMENTS 金流服務"
related: []
tags: 
  - "Automatic Deduction"
  - "Credit Card Binding"
  - "Arrears Handling"
  - Reconciliation
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 對帳中心
  - 新增信用卡
paths: 
  - 管理中心 > 對帳中心
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=969
  - https://www.cyberbiz.io/support/?p=46501
permalink: "https://help.cyberbiz.io/ec/website-management/auto-deduction-of-arrears/"
comments: false
search:
  exclude: false
icon: lucide/credit-card
hide: []
---

# Set up Automatic Deduction of Arrears
If you use the CYBERBIZ PAYMENTS service and your current statement balance is negative, the system charges your linked credit card through automatic arrears deduction. This keeps your store working normally.
{ .subtitle }

[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ PAYMENTS
{ .doc-badge }

!!! tip "Why Turn On This Feature?"
    When a statement shows a negative payout amount, you owe the system money. If you don't pay on time, your access to store features may be affected. Automatic deduction saves you from paying manually and keeps your business running.


## How to Turn It On { #operate-arrears }

**Admin panel path**: `Website Management` > `Reconciliation Center`

1. Log in to the CYBERBIZ admin panel and go to **Website Management > Reconciliation Center**.
2. On the Reconciliation Center page, click **Auto Payment for Unpaid Amounts** to turn on the feature.
3. Click **Add New Credit Card**, enter your card information, and finish linking the card.
4. Confirm your accounting email address and select **Agree**.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-啟用欠款自動扣繳01.png){ .screenshot }


## When Charges Are Made and Notifications { #specs-arrears }

The system makes the deduction at different times depending on your plan and how invoices are issued:

| Merchant type | When the charge is made |
| :--- | :--- |
| **Enterprise (consumer invoices issued by CYB on your behalf)** | The system charges automatically **the next day** after you click **Confirm Payment** |
| **Standard / PLUS / Enterprise (you issue your own invoices)** | The system charges automatically **the day after** the **statement confirmation deadline** of each period |

### Charge Notification Rules { #specs-arrears-notify }

- **Result notifications**: Whether the charge succeeds or fails, the system sends a notification to your **system accounting email**.
- **Retries after failure**: If the charge fails (for example, the card is over its limit or has expired), the system tries again every day. It stops when the charge succeeds or your store's system plan ends.

