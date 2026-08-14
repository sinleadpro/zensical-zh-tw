---
title: 基本報表計算規則對照表
description: 認識基本報表四項核心區塊的計算規則：訂單數量、總銷售額、商品銷售排行、近七日瀏覽人次。
created: 2026-06-21 00:00
last_modified: 2026-07-09 15:55
lang: zh-TW
type: reference
author: Jase
reviewers: []
notes: []
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
tags:
  - 報表分析
  - 基本報表
  - 訂單數量
  - 總銷售額
  - 商品銷售排行
  - 瀏覽人次
  - 計算規則
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/basic-chart-metrics-reference/"
icon: lucide/table
hide:
---

## 基本報表各區塊計算規則 { #reference-basic-chart-metrics }

| 報表 | 統計內容 | 計入 / 認列方式 | 更新方式 |
| :-- | :-- | :-- | :-- |
| 訂單數量 | 所選區間內，每個月份的有效訂單筆數 | 排除已取消、已退貨訂單 | 即時 |
| 總銷售額 | 所選區間內，每個月份有效訂單的金額加總 | 排除已取消、已退貨訂單 | 即時 |
| 商品銷售排行 | 指定日期區間內銷售額前 10 名的商品 | 只計入未退貨的有效訂單；金額＝售出數量 × 成交單價 | 即時(匯出當下計算) |
| 近七日瀏覽人次 | 過去七天，店家首頁每日的進站次數 | 每進入首頁一次即計一次，不去除重複 | 每日彙整前一日數據 |

!!! note "註釋"
    * 「即時」代表查看或匯出當下即依最新訂單計算；「每日彙整」代表需到隔日才會看到前一天的數據。
    * 「商品銷售排行」的時間區間由該區塊的開始 / 結束日期決定，與頁面右上角的時間區間選單(半年 / 一年 / 三年 / 五年)是各自獨立的。
