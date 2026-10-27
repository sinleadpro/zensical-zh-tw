---
title: "Inspect Returns Yourself"
description: "Merchants who use the e-commerce warehouse can handle return parcels themselves instead of sending them back to the main warehouse. Ask customers to ship items to your address, inspect them yourself, and then process the return and refund in the store admin panel."
created: 2026-03-19 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部流程：ec 退貨退款
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
modules:
  - 金物流
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定自行退貨地址
  - 執行退貨審查
  - 處理人工退款
features:
  - 自行驗收
  - 退貨管理
  - 手動退款
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 僅限使用拖拉版型之商家
  - 需使用新版訂單列表介面
related:
  - ec/orders/order-return-process/
  - ec/orders/order-refund-process/
tags:
  - "Self-Handled Returns"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 官網管理後台
paths:
  - 金物流 > 結帳頁&物流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10497
  - https://www.cyberbiz.io/support/?p=4414
permalink: "https://help.cyberbiz.io/wms/merchant-self-inspection-of-returns/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Inspect Returns Yourself
Merchants who use the e-commerce warehouse can handle return parcels themselves instead of sending them back to the main warehouse. Ask customers to ship items to your address, inspect them yourself, and then process the return and refund in the online store admin panel.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing
{ .doc-badge }

## When to Use { #intro-return-inspection }

Use this self-inspection mode if returned items need special handling (such as repair, reprocessing, or your own condition check), or if you want to save on warehouse inspection fees.


## Preparation: Turn off Automatic Returns { #prerequisites-return-inspection-close-auto }

To stop the system from creating WMS return orders or default shipping routes automatically, control return requests manually first.

1. Log in to the online store admin panel and go to **Payment and Logistics > Checkout Page & Logistics**.
2. Open **訂單相關設定 > 顧客取消訂單、申請退貨設定**.
3. Turn off **Customers can request returns**.

![](../assets/images/EC-後台-結帳頁&物流設定-倉儲商家開啟自行驗貨01.en.png){ .screenshot }

## Inspection and Refunds { #operate-return-inspection-process }

1. Give customers your return address and shipping method yourself.
2. After you receive the parcel and inspect it, do the following in the order list.

    - [Review the return](../ec/orders/order-return-process/#operate-order-return-reverse)
    - [Process the refund](../ec/orders/order-refund-process.md)

!!! info "Manage Return Shipping Yourself"
    If you inspect returns yourself, you must contact the carrier and arrange the return pickup yourself. **Reverse logistics cannot be created through the CYBERBIZ platform.**


## Next Steps { #next-steps-return-inspection }

<div class="grid cards" markdown>

- :lucide-chart-bar-increasing:{ .lg }
  [__Order Return and Refund Process__](../ec/orders/order-return-process.md)
  Learn the return policy, what to know before you start, and related rules.

- :lucide-square-chart-gantt:{ .lg }
  [__Refund Methods and Processing__](../ec/orders/order-refund-process.md)
  Learn the refund review timeline, amount calculation, and accounting notes.


</div>
