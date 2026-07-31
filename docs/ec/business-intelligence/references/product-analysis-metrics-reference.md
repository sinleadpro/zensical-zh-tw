---
title: 商品分析欄位對照表
description: 商品分析各區塊的欄位與指標定義，包含銷量排名、回購頻率、無銷量商品與期間別購買狀況。
created: 2026-06-15
last_modified: 2026-07-12 19:43
lang: zh-TW
type: reference
status: update
author: Jase
version: ""
reviewers: []
notes: []
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
plans: []
tags:
  - 報表分析
  - 商品分析
  - 銷量排名
  - 回購率
  - 回購頻率
  - 欄位對照
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/product-analysis-metrics-reference/"
icon: lucide/table
hide:
---

# 商品分析欄位對照表

本頁集中說明「商品分析」各區塊的欄位與指標定義，供 [商品分析](../product-analysis.md) 等文件以跳轉方式引用。

### 商品銷量 TOP 10 / LAST 10 { #reference-product-analysis-sales-rank }

| 項目 | 說明 |
| :-- | :-- |
| 產品名稱 | 商品(含規格)名稱，圖表中過長會以「…」省略，滑鼠移上可看完整名稱 |
| 銷量 | 該商品在查詢期間內的 **銷售數量**(件數)加總 |

!!! note "註釋"
    * 僅計算有效訂單(非取消、不需退貨或拒絕退貨)。
    * 已排除加購類商品。
    * TOP 10 由高至低、LAST 10 由低至高，各取 10 項。

### 商品回購頻率 { #reference-product-analysis-repurchase }

| 欄位 | 說明 |
| :-- | :-- |
| 商品 SKU | 商品的庫存編號 |
| 商品名稱 | 商品(含規格)名稱 |
| 回購次數 | 查詢期間內，所有顧客重複購買此商品的總次數(同一顧客第 2 次起的每次購買各算一次) |
| 平均回購間隔天數 | 顧客兩次購買此商品之間的平均相隔天數 |

!!! note "註釋"
    * 僅列出回購次數達 **10 次以上** 的商品。
    * 依「平均回購間隔天數」由小到大排序，間隔越短代表回購越頻繁。

### 近90天內更新且近30天內無銷量之產品 { #reference-product-analysis-no-sales }

| 欄位 | 說明 |
| :-- | :-- |
| 商品 SKU | 商品的庫存編號 |
| 商品名稱 | 商品(含規格)名稱 |
| 售價 | 商品目前的售價 |
| 更新日期 | 商品資料最後一次更新的日期 |

!!! note "註釋"
    * 系統以查詢當下的「今日」為基準，自動列出近 90 天內有更新、但近 30 天內無任何銷售的商品。
    * 此表不提供自訂日期，商品較多時以翻頁方式瀏覽。

### 商品期間別購買狀況 { #reference-product-analysis-period }

| 欄位 | 說明 |
| :-- | :-- |
| 商品名稱 | 商品(含規格)名稱 |
| 訂單數量 | 查詢期間內含此商品的訂單筆數 |
| 銷售數量 | 查詢期間內此商品的銷售件數加總 |
| 產品銷售總金額 | 查詢期間內此商品的銷售金額加總 |

!!! note "註釋"
    * 表格最後一列為所有商品的「合計」。
    * 可用商品多選篩選器只看特定商品，並支援匯出 Excel。
    * 僅計算有效訂單(非取消、不需退貨或拒絕退貨)。
