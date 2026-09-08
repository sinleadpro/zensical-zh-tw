---
title: POS 營收分析指標與欄位對照表
description: POS 營收分析頁面的營業指標定義與各分店比較器欄位對照，供主文引用。
created: 2026-06-23 16:00
last_modified: 2026-06-23 18:47
lang: zh-TW
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related:
  - pos/business-intelligence/pos-revenue-analysis/
tags:
  - POS
  - 營收分析
  - 參考資料
  - 營業額
  - 客單價
  - 消費人數
  - 人均消費額
  - 日均消費額
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/pos/business-intelligence/references/pos-revenue-metrics-reference/"
comments: false
search:
  exclude: false
icon: lucide/table
hide:
---

# POS 營收分析指標與欄位對照表

此頁集中說明「POS 營收分析」頁面上各比較器共用的營業指標，以及「各分店比較器」排名表的欄位意義，供其他文件引用。

### POS 營收分析指標對照表 { #reference-pos-revenue-metrics }

| 指標 | 代表意義 | 計算基礎 |
| :-- | :-- | :-- |
| 營業額 | 所選門市與區間內的銷售總額 | 認列訂單的訂單金額加總 |
| 訂單數 | 所選門市與區間內成立的訂單筆數 | 認列訂單的筆數加總 |
| 平均客單價 | 平均每一筆訂單的消費金額 | 營業額 ÷ 訂單數 |
| 消費人數 | 區間內實際消費的會員人數（不重複計算） | 區間內不重複的消費會員數 |
| 人均消費額 | 平均每一位顧客貢獻的金額 | 營業額 ÷ 消費人數 |

!!! note "註釋"
    * 「認列訂單」指訂單狀態為非取消訂單，且退貨狀態為不需退貨或拒絕退貨的訂單，詳見主文的[認列訂單定義](../pos-revenue-analysis.md#specs-pos-revenue-counted-orders){ title="認列訂單定義" data-preview }。
    * 「消費人數」與「人均消費額」僅統計有綁定會員的訂單；未綁定會員的散客訂單仍會計入營業額與訂單數，但不會計入消費人數。
    * 所有金額皆以整數呈現（小數會四捨五入）。

### 各分店比較器欄位對照表 { #reference-pos-revenue-store-columns }

| 欄位 | 說明 |
| :-- | :-- |
| 名次排行 | 依「銷售額」由高到低自動排名的名次 |
| 商店/門市 | POS 門市名稱 |
| 銷售額 | 該門市在所選區間內的營業額加總 |
| 訂單數 | 該門市在所選區間內成立的訂單筆數 |
| 消費人數 | 該門市在所選區間內不重複的消費會員數 |
| 日均消費額 | 該門市在所選區間內平均每日的營業額（銷售額 ÷ 區間天數） |
| 平均客單價 | 該門市平均每一筆訂單的消費金額（銷售額 ÷ 訂單數） |
| 人均消費額 | 該門市平均每一位顧客貢獻的金額（銷售額 ÷ 消費人數） |

!!! note "註釋"
    * 排名表預設以「銷售額」由高到低排序，協助您快速找出表現最佳與待加強的門市。
    * 各欄位的會員統計範圍與上方[指標對照表](#reference-pos-revenue-metrics){ title="POS 營收分析指標對照表" data-preview }一致。
