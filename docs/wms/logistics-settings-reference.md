---
title: 串倉宅配物流設定位置對照
description: 針對不同串倉模式，系統對「倉庫出貨」與「商家自行出貨」的宅配物流設定路徑有所不同。本表彙整各情境下的設定位置，協助您快速完成配置。
created: 2026-07-13 12:00
last_modified: 2026-07-13 12:00
lang: zh-TW
type: reference
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
modules:
  - 電商倉儲
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
cyb_extensions: []
intents: 
features:
  - 電商倉儲
  - 建立物流選項
prerequisites: []
related: []
tags:
  - WMS
acoiv: activate
apis: []
devices:
  - desktop
ui_components:
  - 自訂物流頁籤
  - 串接物流頁籤
paths:
  - EC：金物流 > 宅配物流 > 自訂物流
  - EC：金物流 > 宅配物流 > 串接物流
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/logistics-settings-reference"
comments: false
search:
  exclude: false
icon: ""
hide: []
---
# 串倉宅配物流設定位置對照
針對不同串倉模式，系統對「倉庫出貨」與「商家自行出貨」的宅配物流設定路徑有所不同。本表彙整各情境下的設定位置，協助您快速完成配置。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 電商官網 / 智慧倉儲
{ .doc-badge }

## 設定位置一覽表

根據配送方與付款方式，前往 **金物流 > 宅配物流** 後，請至對應的頁籤建立物流選項：

| 配送方 | 付款方式 | 全部串倉 | 部分串倉 |
| :--- | :--- | :--- | :--- |
| **倉庫出貨** | 貨到付款 | 自訂物流頁籤 | 自訂物流頁籤 |
| | 貨到不付款 | 自訂物流頁籤 | 自訂物流頁籤 |
| **商家自行出貨** | 貨到付款 | - | **串接物流頁籤** |
|  | 貨到不付款 | - | 自訂物流頁籤 |

## 關鍵差異說明

- **全部串倉**：所有商品均由倉庫發貨，僅需在 **自訂物流** 中定義對應的倉庫出貨選項。
- **部分串倉**：
    - **倉庫出貨項目**：統一於 **自訂物流** 頁籤設定。
    - **商家自出項目**：若支援 **貨到付款**，需透過 **串接物流** 頁籤設定；若為 **貨到不付款**，則維持在 **自訂物流** 頁籤設定。

## 參考資料

- [串倉申請流程與開通](application-process-and-activation.md)
- [啟用部分串倉與混單](enable-partial-warehouse-integration-and-mixed-orders.md)
- [啟用部分串倉與拆單](enable-partial-warehouse-integration-and-order-splitting.md)