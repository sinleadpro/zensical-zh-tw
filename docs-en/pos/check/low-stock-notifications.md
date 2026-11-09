---
title: "Low-Stock Notifications"
description: "Merchants can flexibly configure how the POS front end alerts staff when products or gifts are low in stock, keeping sales smooth and reducing the risk of overselling."
created: 2026-04-17 11:30
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有 POS 商店
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定庫存不足提醒
  - POS 庫存通知設定
  - 調整 POS 提醒形式
features:
  - 庫存不足提醒通知
  - POS 商店設定
prerequisites: []
related: []
tags:
  - "Stock Alerts"
  - "POS Settings"
  - "Inventory Management"
  - "Store Settings"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 所有 POS 商店
  - 庫存不足提醒通知
  - 蓋板彈窗
  - 限時提示
paths:
  - POS 功能 > 所有 POS 商店 > [店名]
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/pos/check/low-stock-notifications/"
comments: false
search:
  exclude: false
icon: lucide/archive-x
hide: []
---

# Low-Stock Notifications
Merchants can flexibly configure how the POS front end alerts staff when products or gifts are low in stock, keeping sales smooth and reducing the risk of overselling.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Strict stock control**: Select "Overlay Pop-up" to require store staff to confirm before proceeding, preventing overselling.
    - **Smooth operations**: Select "Timed Alert" for visual reminders only, without interrupting checkout.

## Set up the Alert Style { #operate-low-stock }

1. Log in to the CYBERBIZ admin dashboard and go to **POS > POS Store List**.
2. In the **POS Store List**, click the **POS store name** you want to set up.
3. Scroll down to the **Low-Stock Alert Notifications** section.
4. Based on your store's needs, select one of the following three alert styles:

    | Alert Style | Display Description | Use Case |
    | :--- | :--- | :--- |
    | **Overlay Pop-up (Default)** | A pop-up appears on the front end and requires you to click **Confirm** to close it. | Best for stores that must force stock confirmation to prevent overselling. |
    | **Timed Alert** | A floating alert appears at the top of the front end and disappears automatically after 3 seconds without interrupting operations. | Best for stores that want to keep operations smooth. |
    | **No Alert** | No alerts are shown, so staff must monitor stock status on their own. | Best for stores with a separate inventory control process. |

5. Click **Save** at the bottom of the page.

![](../../assets/images/POS-後台-POS功能-所有POS商店-庫存不足提醒通知01.en.png){ .screenshot }


## Front-End Display Style Reference { #intro-low-stock }

The following shows how each alert style appears when product or gift stock is low:

| Alert Style | Low Product Stock | Low Gift Stock |
| :--- | :--- | :--- |
| **Overlay Pop-up** | ![](../../assets/images/POS-前台-結帳頁-庫存不足蓋板彈窗01.en.png){ .screenshot } | ![](../../assets/images/POS-前台-結帳頁-庫存不足蓋板彈窗02.en.png){ .screenshot } |
| **Timed Alert** | ![](../../assets/images/POS-前台-結帳頁-庫存不足限時提醒01.en.png){ .screenshot } | ![](../../assets/images/POS-前台-結帳頁-庫存不足限時提醒02.en.png){ .screenshot } |
| **No Alert** | No notification | No notification |

