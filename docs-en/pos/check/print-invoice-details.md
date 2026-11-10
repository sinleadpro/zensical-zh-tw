---
title: "Print Invoice Details"
description: "You can enable the 'Auto Issue Invoice' setting in POS terminal settings and configure print preferences for invoices or transaction details based on store needs."
created: 2026-04-17 11:45
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
  - 設定自動列印明細
  - 開啟自動開發票
  - 調整 POS 發票列印模式
features:
  - 自動列印明細
  - 自動開發票
  - POS 子機設定
prerequisites: []
related: []
tags:
  - "Invoice Details"
  - "Auto Print"
  - "POS Settings"
  - "Invoice Settings"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 自動開發票
  - 自動列印發票設定
  - 自動列印明細
paths:
  - POS 功能 > 所有 POS 商店 > [店名] > POS 系統列表 > 修改 POS 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=27199
  - https://www.cyberbiz.io/support/?p=5231
permalink: "https://help.cyberbiz.io/pos/check/print-invoice-details/"
comments: false
search:
  exclude: false
icon: lucide/printer
hide: []
---

# Print Invoice Details
You can enable the "Auto Issue Invoice" setting in POS terminal settings and configure print preferences for invoices or transaction details based on store needs.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Faster checkout**: Invoices and details are generated automatically after checkout, so store staff do not need to select them manually. This keeps the line moving.
    - **Complete records**: Each completed transaction also generates a purchase list (details), so customers can reconcile their records easily.

## Before You Start { #prerequisites-invoice-details }

- **Device limitation**: **MYPAY invoice printer** does not support auto-print settings.
- **Format behavior**: If the invoice includes a **Unified Business Number (UBN)**, the detail content prints together with the invoice and is not truncated.

## Procedure { #operate-general-orders-invoice }


1. Log in to the CYBERBIZ admin and go to **POS > POS Store List**.
2. Select the **POS store name** you want to configure.
3. Scroll down to the **POS System List** section, then click **Edit POS Settings** for the terminal you want to adjust.
    ![](../../assets/images/POS-後台-所有POS商店-修改POS子機設定01.en.png){ .screenshot }
4. Turn the following feature switches on or off based on store needs:

    - **Auto Issue Invoice**: After checkout is complete, the system automatically issues an electronic invoice.
    - **Auto Print Invoice Setting**: After a successful checkout, the invoice printer automatically prints a paper invoice.
    - **Auto Print Details**: When a transaction is complete, the purchase list (details) is generated and printed automatically.

    ![](../../assets/images/POS-後台-所有POS商店-修改POS子機設定02.en.png){ .screenshot }

5. Click **Save** to complete the setup.


