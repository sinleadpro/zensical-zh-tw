---
title: 超商託運單逾期重新取號
description: 超商託運單逾期且尚無配送記錄時，重新取得託運單號並下載新託運單。
created: 2026-08-26 15:42
last_modified: 2026-08-26 15:42
lang: zh-TW
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules:
  - 訂單
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 重新取得超商託運單
  - 處理逾期託運單
  - 處理部分出貨託運單
features: 
  - 超商託運單
  - 逾期重新取號
  - B2C_大宗寄倉
  - C2C_店到店
  - 部分出貨
prerequisites: 
  - 原託運單已完成取號並操作出貨
  - 原託運單已逾期且沒有配送記錄
related: 
  - "docs/ec/orders/cvs-shipping/cvs-b2c-bulk-shipping"
  - "docs/ec/orders/cvs-shipping/cvs-c2c-shipping"
  - "docs/ec/orders/cvs-shipping/cvs-partial-shipment"
  - "docs/ec/orders/cvs-shipping/setup-family-mart-frozen-b2c"
  - "docs/ec/orders/cvs-shipping/family-mart-frozen-c2c"
tags: 
  - 超商託運單
  - 重新取號
  - 逾期託運單
acoiv: operation
apis: []
devices: []
ui_components: []
paths: 
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/renew-waybill-after-expiration/"
comments: false
search:
  exclude: false
icon: lucide/refresh-cw
hide: []
---


## 使用須知 { #prerequisites-renew-waybill-after-expiration }

- **使用情境**：原託運單已超過出貨（補印）期限，無法再用於交寄，需要重新取得託運單。

- **適用物流**：
    - [超商 B2C 大宗寄倉](cvs-shipping/cvs-b2c-bulk-shipping/)
    - [超商 C2C 店到店](cvs-shipping/cvs-c2c-shipping/)
    - [全家冷凍寄倉 B2C](../payments-and-logistics/setup-family-mart-frozen-b2c/)
    - [全家冷凍店到店 C2C](cvs-shipping/family-mart-frozen-c2c/)

    > 黑貓快速到店不支援本功能。

- **訂單配送狀態**：僅適用於 **已出貨** 或 **[部分出貨](cvs-shipping/cvs-partial-shipment.md)** 訂單。

    > 超商部分出貨訂單，其超商託運單同樣支援託運單逾期後重新取號。

- **託運單狀態**：原託運單必須已逾期，且無配送記錄。

    !!! tip "系統判斷邏輯"
        - 託運單尚未逾期：於期限內使用 **補印託運單**，取得原託運單。
        - 託運單已逾期且沒有配送記錄：使用 **重新取號並下載新託運單**，取得新的託運單。



## 操作流程 { #operate-renew-waybill-after-expiration }

1. 登入 CYBERBIZ 管理後台，前往 **訂單 > 所有訂單**。
2. 勾選訂單後選擇 **重新取號並下載新託運單**。
3. 系統將重新取得託運單號。下載新託運單，依原超商物流流程完成交寄。

![](../../assets/images/EC-後台-訂單-所有訂單-託運單重新取號01.png)

!!! warning "重新取號前請確認配送記錄"
    若原託運單已有配送記錄，請勿重新取號。請先確認實際出貨狀態，再執行重新取號。


<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__查詢各超商託運單失效期限__](references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  查看各超商物流的補印期限與失效判定時間。

</div>