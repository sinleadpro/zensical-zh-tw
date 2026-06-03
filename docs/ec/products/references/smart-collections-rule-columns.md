---
title: 條件分類篩選欄位對照表
description: ""
created: 2026-06-03 21:50
last_modified: 2026-06-03 22:11
lang: zh-TW
type: reference
status: ""
author: Jase
version: ""
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans:
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/table
hide:
---

本對照表彙整「商品條件分類」可用的篩選欄位,以及每個欄位可搭配的比對條件,供條件分類設定參考。

## 篩選欄位對照表 { #smart-collections-rule-columns }

| 篩選欄位 | 從哪個商品資料比對 | 欄位類型 | 可搭配的條件 |
| :-- | :-- | :-- | :-- |
| 商品名稱 | 商品的名稱 | 文字 | 等於、以此開頭、以此結束、包含、不包含 |
| 商品類型 | 商品的「商品類型」欄位 | 文字 | 等於、以此開頭、以此結束、包含、不包含 |
| 商品廠商 | 商品的「廠商」欄位 | 文字 | 等於、以此開頭、以此結束、包含、不包含 |
| 款式名稱 | 商品款式(規格)的名稱 | 文字 | 等於、以此開頭、以此結束、包含、不包含 |
| 商品標籤 | 商品上設定的標籤 | 文字 | 等於、以此開頭、以此結束、包含、不包含 |
| 商品價格 | 商品的售價 | 數值 | 等於、大於、小於 |
| 定價 | 商品的原價(劃線價) | 數值 | 等於、大於、小於 |
| 庫存現貨 | 商品目前的庫存數量 | 數值 | 等於、大於、小於 |

!!! note "註釋"
    * **文字欄位**(商品名稱、商品類型、商品廠商、款式名稱、商品標籤)可使用文字類條件(等於、以此開頭、以此結束、包含、不包含)。
    * **數值欄位**(商品價格、定價、庫存現貨)只能使用數值類條件(等於、大於、小於),且比對值請輸入數字。
    * 各條件的詳細意義請見[篩選條件對照表](smart-collections-rule-relations.md)。

