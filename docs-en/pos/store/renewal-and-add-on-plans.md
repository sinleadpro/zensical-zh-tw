---
title: "Renewal and Add-On Plans"
description: "Renew your POS system or add sub-terminals in the admin dashboard without contacting a consultant."
created: 2026-04-10 10:00
last_modified: 2026-06-30 21:55
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
  - 續約與加購方案
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
  - POS 續約
  - 加購 POS 子機
  - 查詢 POS 方案費用
features:
  - 續購與加購方案
  - POS 子機管理
prerequisites: []
related: []
tags:
  - "POS Renewal"
  - "Add-On Sub-Terminals"
  - "Contract Management"
  - "POS Plans"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 續約與加購方案
  - POS 列表
  - 續約
  - 加購子機
paths:
  - POS 功能 > 續約與加購方案
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=24441
permalink: "https://help.cyberbiz.io/pos/store/renewal-and-add-on-plans/"
comments: false
search:
  exclude: false
icon: lucide/circle-plus
hide: []
---

# Renewal and Add-On Plans
Renew your POS system or add sub-terminals directly in the admin dashboard, without contacting a consultant. This lets you quickly extend your contract and expand your equipment.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) |Smart POS
{ .doc-badge }

![](../../assets/images/POS-後台-續購與加購方案-畫面總覽01.en.png){ .hero-page }


!!! tip "Use Cases"
    - **Before the contract expires**: Renew on your own in the admin dashboard to keep your POS service running without interruption.
    - **Expand checkout counters**: If a single store needs multiple POS terminals operating at the same time, you can add sub-terminal licenses.

## Usage Notes { #prerequisites-renewal-plans }

- **Payment method**: When you renew or add sub-terminals, **no upfront payment is required**. The system collects payment through the **statement**.
- **Sub-terminal definition**: If a single POS store needs multiple checkout points operating at the same time, you must add **sub-terminal** licenses.

## Procedure { #operate-renewal-plans }

### Add a POS Store { #operate-renewal-plans-add-pos }

1. Log in to the admin dashboard, go to **POS > Renewal Plans**, and click the **Buy POS shop** tab.
2. Review the plan details and the expected charges.
3. Complete checkout. The system automatically records the transaction and adds it to the next statement.

![](../../assets/images/POS-後台-續購與加購方案-新增門市01.en.png){ .screenshot }

### Renew or Add Sub-Terminals { #operate-renewal-plans-subdevice }

1. Log in to the admin dashboard, go to **POS > Renewal Plans**, and click the **POS List** tab.
2. Find the store you want to manage, then click **Renew** or **Add sub machine** based on your needs.
3. Review the plan details and the expected charges.
4. Complete checkout. The system automatically records the transaction and adds it to the next statement.

![](../../assets/images/POS-後台-續購與加購方案-續購方案與子機01.en.png){ .screenshot }

### View Transaction Records { #operate-renewal-plans-transaction-history }

1. Log in to the admin dashboard, go to **POS > Renewal Plans**, and click the **Transaction details** tab.
2. View all transaction records in real time, including **Buyer**, **Transaction Time**, and **Fee**.
3. Click **Detailed Information** to view the **Associated Store** and the **Renewal Start and End Time**.

![](../../assets/images/POS-後台-續購與加購方案-交易明細01.en.png){ .screenshot }


## Sub-Terminal Features and Limits { #overview-renewal-plans }

- **Term alignment**: The term of added sub-terminals aligns with the first sub-terminal. The first-year fee for added sub-terminals is prorated based on the **remaining months** of the first sub-terminal.
- **Data sync**: All sub-terminals use the same store's marketing campaigns, inventory data, and chart analytics.
- **Independent operation**: Each sub-terminal must **run its own end-of-day close** and **record its inventory-in balance**.
- **Report filtering**: After you export the daily cash-out report and order summary report to Excel, filter and reconcile them by **sub-terminal name**.


## FAQ { #faq-renewal-plans }

??? quote "Can sub-terminals be used across stores?"
    No. Sub-terminal licenses are tied to a specific store. If another store needs one, it must be added separately under that store.
