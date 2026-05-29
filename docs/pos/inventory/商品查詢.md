---
title: 商品查詢
description: 門市人員可透過 POS 前台快速檢索商品資訊與庫存狀態，支援多種搜尋模式以滿足不同情境下的查找需求。
created: 2026-04-10 10:30
last_modified: 2026-05-28 14:48
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 庫存
sites:
  - TW
audiences:
  - clerk
difficulty: beginner
tnb: branch
plans:
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents:
  - 查詢商品庫存
  - 搜尋商品資訊
  - POS 前台商品搜尋
features:
  - 商品查詢
  - 模糊搜尋
prerequisites: []
related: []
tags:
  - 商品查詢
  - POS 前台
  - 庫存查詢
  - 搜尋模式
acoiv: operation
apis: []
devices:
  - desktop
  - tablet
ui_components:
  - 庫存
  - 商品查詢
  - 開頭符合搜尋
  - 模糊搜尋
paths:
  - POS 前台 > 庫存 > 商品查詢
layouts: []
wp_url: []
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/file-search
hide: []
---

# 商品查詢
門市人員可透過 POS 前台快速檢索商品資訊與庫存狀態，支援多種搜尋模式以滿足不同情境下的查找需求。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 進階 PLUS / 高手 PLUS / 企業
{ .doc-badge }

![](../../assets/images/POS-前台-庫存-商品查詢-畫面總覽01.png){ .hero-page }

!!! tip "應用情境"
    - **顧客詢價**：快速查找特定商品的價格與規格。
    - **庫存確認**：即時確認門市內或全通路的剩餘庫存量。

## 操作流程


1. 在 POS 前台選單點選 **庫存 > 商品查詢**。
2. 在搜尋框中手動輸入 **商品名稱**，或使用掃碼槍 **掃描商品條碼**。

    > 建議優先以 **掃碼槍掃描條碼**，較為快速準確。

3. 根據需求選擇搜尋模式：

    | 模式 | 說明 | 適用情境 | 搜尋時間 | 
    | :--- | :--- | :--- | :--- |
    | **開頭符合搜尋** | 僅顯示關鍵字位於開頭的搜尋結果 | 已知商品編號或名稱開頭時 | 速度較快 |
    | **模糊搜尋** | 顯示包含關鍵字的所有結果 | 僅記得商品部分關鍵字時 | 搜尋時間較長 | 

    !!! warning "效能提醒"
        若門市商品品項眾多，使用 **模糊搜尋** 可能會產生較長的讀取時間，建議優先使用 **開頭符合搜尋** 或以掃碼槍輸入完整 SKU 以提升效率。


4. 點擊搜尋後，系統將列出符合條件的商品清單。

![](../../assets/images/POS-前台-庫存-商品查詢-搜尋01.png){ .screenshot }
