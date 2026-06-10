---
title: 商品群組類型對照表
description: ""
created: 2026-06-03 18:42
last_modified: 2026-06-04 11:03
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
modules:
  - 商品
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: trunk
plans:
  - 專業
  - 進階
  - 高手
  - 專業PLUS 
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - EC
  - 商品管理
  - 商品群組
  - 條件分類
  - 任選折扣
  - Smart Collections
  - Reference
  - 對照表
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

本對照表整理可在「全站商品列表群組排序」中排序的三種商品群組，說明各類型的商品加入方式、典型用途，以及要出現在排序清單(前台首頁「商品列表」)所需符合的條件。

## 可排序的商品群組類型 { #reference-collection-order-group-types }

| 群組類型 | 商品加入方式 | 典型用途 | 出現在排序清單的條件 |
| :-- | :-- | :-- | :-- |
| 自定群組(自訂分類) | 由商家手動逐一挑選商品加入 | 主打商品、精選清單、活動專區等需自行掌控內容的群組 | 狀態設為「公開」 |
| 商品條件分類(智慧群組) | 設定篩選條件(如標題、商品類型、廠商、價格、庫存數量、標籤等)，符合條件的商品自動歸入 | 商品數量多、希望依規則自動分類；新商品只要符合條件就會自動加入 | 狀態設為「公開」 |
| 任選折扣群組 | 設定任選折扣活動並指定參與商品，折扣方式包含任選固定金額、任選折數、任選折固定金額、任選每件折固定金額 | 「任選 N 件」的促銷活動 | 狀態設為「公開」、目前在活動期間內，且已設定有效的折扣規則 |

!!! note "註釋"
    * 「出現在排序清單的條件」指的是該群組要顯示在後台排序清單與前台首頁「商品列表」所需符合的條件；不符合條件的群組不會列入排序，也不會在前台顯示。
    * 自定群組與商品條件分類只要狀態為「公開」即會列入；任選折扣群組除了「公開」外，還需在活動期間內且有有效的折扣規則才會顯示。
    * 此頁僅排序「群組與群組之間」的順序；群組內部商品的排序需在各群組編輯頁另行設定。

