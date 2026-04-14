---
title: POD 列表
description: 在電商倉儲（WMS）中利用 POD 列表追蹤「專車派車」訂單的派車狀態。
created: 2026-03-19 00:00
last_modified: 2026-03-25 12:08
lang: zh-TW
type: tutorial
status:
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: ["WMS"]
modules: ["POD列表"]
sites: ["TW"]
audiences: []
difficulty:
tnb: trunk
plans: []
cyb_extensions: []
intents: ["查詢回單狀態", "追蹤出貨派車憑證", "核對訂單交付進度"]
features: ["POD 列表", "回單管理", "收貨證明", "訂單追蹤"]
prerequisites: ["需已開通 CYBERBIZ 電商倉儲服務", "僅適用於開通專車派車配送模式"]
related: []
tags: ["WMS", "收貨證明", "回單", "出貨管理"]
acoiv: venture
apis: []
devices: ["desktop"]
ui_components: ["POD 列表頁面", "訂單篩選區塊"]
paths: ["POD 列表"]
layouts: []
wp_url: ["https://www.cyberbiz.io/support/?p=39973"]
permalink:
comments: false
search:
  exclude: false
icon: lucide/file-check
hide: []
---

# POD 列表
在電商倉儲（WMS）中利用 POD 列表追蹤「專車派車」訂單的派車狀態。
{ .subtitle }

![](../assets/images/WMS-後台-POD列表-畫面總覽01.png){ .hero-page }

## 使用須知

- **專車派車出貨**：專車派車為 **加值服務**，將另行將酌收費用，若有需求請洽詢倉儲經理，取得專屬報價。開通服務後，您即可於此處追蹤專車派車狀態。


## POD 列表功能概覽
介面分為「篩選區」與「結果列表」，提供精確的訂單追蹤能力。

1. 進入 CYBERBIZ 電商倉儲（WMS）管理後台，點選 **POD 列表**。
2. **篩選條件配置**：
    - **時間區間**：選擇特定時段（不可超過 **30 天**），亦可不限時間進行全量查詢。
    - **回單狀態**：
        - **已完成**：物流端已回傳簽收證明，且系統已完成紀錄。
        - **未完成**：貨件可能尚在配送中，或回傳憑證尚未歸檔。
3. 點擊 **搜尋**。


## 查詢結果應用

在列表顯示後，商家可透過列表執行以下操作：

- **追蹤回單進度**：透過 **回單狀態** 欄位，快速識別訂單的派送狀態。
- **查看訂單詳情**：點擊列表中的 **訂單編號**，系統將自動連結至該訂單的詳細資訊頁面，方便核對品項與收件人資訊。
- **異常識別**：若貨態顯示已送達但 POD 狀態長期處於 **未完成**，請聯繫倉庫客服或物流商確認。
