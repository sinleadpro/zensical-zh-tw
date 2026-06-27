---
title: 訂單自動結案類型對照表
description: 彙整訂單自動結案設定的各種結案類型、觸發條件與訂單狀態要求，供結帳頁與金物流相關設定引用。
created: 2026-06-16
last_modified: 2026-06-27 23:07
lang: zh-TW
type: reference
status: ""
author: Jase
version: ""
reviewers: []
notes: []
products:
  - ec
modules: []
sites:
  - TW
audiences:
  - admin
plans: []
tags:
  - 自動結案
  - 結案類型
  - 訂單狀態
  - 參考資料
permalink: https://help.cyberbiz.io/ec/orders/references/order-auto-close-types-reference/
icon: lucide/check-circle-2
hide:
---

# 訂單自動結案類型對照表

本對照表彙整「訂單自動結案設定」的各種結案類型、觸發條件與訂單狀態要求，供結帳頁與金物流相關設定引用。

## 自動結案類型 { #order-auto-close-types }

| 結案類型 | 觸發條件 | 訂單狀態要求 | 適用情境 |
| :-- | :-- | :-- | :-- |
| 當顧客取貨後 N 天 | 串接物流(超商、黑貓等)配送狀態為「已收貨」達 N 天 | 已付款 / 貨到付款、已取貨、不需退貨 | 使用串接物流，系統可得知顧客已取貨 |
| 當訂單出貨後 N 天 | 自訂物流配送狀態為「已出貨」達 N 天 | 已付款 / 貨到付款、已出貨、不需退貨 | 使用自訂物流，系統無法得知是否取貨 |
| 票券訂單(顧客付款後 N 天) | 顧客付款後達 N 天 | 已付款 | 票券型商品，結案後計算分潤 |

!!! note "註釋"
    * 「當顧客取貨後」與「當訂單出貨後」為二選一，請依您主要使用的物流類型擇一。
    * 範例：設定為 7 天，1 月 1 號取貨(或出貨)的訂單會在 1 月 8 號自動結案。
    * 票券訂單自動結案僅在開通票券功能時顯示。
    * 訂單結案後，系統即結算並發送消費紅利與分潤；退貨時是否返還紅利請另行於「訂單取消退貨相關紅利設定」設定。
