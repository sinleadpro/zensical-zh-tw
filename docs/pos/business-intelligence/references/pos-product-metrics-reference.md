---
title: POS 商品分析對照表
description: POS 商品分析三張排名報表的欄位與指標定義對照，供主文引用。
created: 2026-06-23 15:40
last_modified: 2026-06-23 21:53
lang: zh-TW
type: reference
status: update
version: ""
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
  - "pos/business-intelligence/pos-product-analysis"
tags:
  - POS
  - 商品分析
  - 參考資料
  - 商品銷售排名
  - 商品回購排名
  - 商品退貨排名
  - 期間商品回購率
  - 期間商品退貨率
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/pos/business-intelligence/references/pos-product-metrics-reference/"
comments: false
search:
  exclude: false
icon: lucide/table
hide:
---

# POS 商品分析對照表

本頁集中放置「POS 商品分析」三張排名報表的欄位與指標對照表，供主文引用。

## 共同欄位對照表 { #reference-pos-product-common }

| 欄位 | 說明 |
| :-- | :-- |
| 排名 | 商品在該報表中的名次。 |
| SKU | 商品的庫存單位編號，用來唯一辨識品項。 |
| 商品名稱 | 商品的名稱。 |
| 商品類型 | 商品所屬的分類。 |
| 廠商 | 商品的供應廠商。 |
| 商品售價 | 商品的銷售單價。 |
| 商品銷售額 | 該商品在所選期間內的銷售總金額。 |
| 商品銷售量 | 該商品在所選期間內的銷售總數量。 |
| 購物人次 | 期間內購買該商品的訂單人次，數字越高代表越多顧客買單。 |

!!! note "註釋"
    * 上述欄位為三張報表（商品銷售排名、商品回購排名、商品退貨排名）共同顯示的欄位。
    * 所有數字僅計入非取消訂單；被取消的訂單會從取消當日的營業額扣除。

## 各報表專屬指標對照表 { #reference-pos-product-special }

| 報表 | 專屬欄位 | 說明 |
| :-- | :-- | :-- |
| 商品銷售排名 | 期間營業額占比 | 該商品銷售額占所選期間總營業額的百分比。 |
| 商品回購排名 | 期間商品回購率 | 購買此商品兩次以上之顧客數 ÷ 購買過此商品之顧客數。 |
| 商品回購排名 | 平均回購次數 | 期間內購買過此商品的顧客，平均重複購買此商品的次數，數字越高代表黏著度越強。 |
| 商品退貨排名 | 期間商品退貨數 | 該商品在所選期間內被退貨的數量。 |
| 商品退貨排名 | 期間商品退貨率 | 該商品在所選期間內的退貨比率，比率越高代表退貨情形越需留意。 |

!!! note "註釋"
    * 含百分比的欄位(期間營業額占比、期間商品回購率、期間商品退貨率)在報表中以「%」顯示。
    * 商品銷售排名以「商品銷售額」由高至低排名。
