---
title: 條件分類篩選條件對照表
description: ""
created: 2026-06-03 21:55
last_modified: 2026-07-02 10:07
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
tags:
  - 商品管理
  - 條件分類
  - 篩選條件
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/references/smart-collections-rule-relations/"
comments: ""
search:
  exclude: ""
icon: lucide/table
hide:
---

本對照表說明「商品條件分類」中每個篩選條件(運算子)的意義，供設定規則時參考。
  
## 篩選條件對照表 { #smart-collections-rule-relations }

| 篩選條件 | 意義 | 適用欄位類型 | 範例 |
| :-- | :-- | :-- | :-- |
| 等於 | 欄位的值與您輸入的內容完全相同 | 文字、數值皆可 | 商品廠商「等於」CYBERBIZ |
| 包含 | 欄位文字中含有您輸入的字 | 文字 | 商品名稱「包含」夏季 |
| 不包含 | 欄位文字中不含您輸入的字 | 文字 | 商品名稱「不包含」福袋 |
| 以此開頭 | 欄位文字以您輸入的字開頭 | 文字 | 商品名稱「以此開頭」2024 |
| 以此結束 | 欄位文字以您輸入的字結尾 | 文字 | 款式名稱「以此結束」L |
| 大於 | 數值大於您輸入的數字 | 數值 | 商品價格「大於」1000 |
| 小於 | 數值小於您輸入的數字 | 數值 | 庫存現貨「小於」10 |

!!! note "註釋"
    * 「大於」「小於」只會在您選擇數值欄位(商品價格、定價、庫存現貨)時出現，比對值請輸入數字。
    * 文字欄位的比對不分大小寫差異以外的格式，建議輸入與商品資料一致的字詞。
    * 哪些欄位屬於文字、哪些屬於數值，請見[篩選欄位對照表](smart-collections-rule-columns.md){ title="條件分類篩選欄位對照表" }。
