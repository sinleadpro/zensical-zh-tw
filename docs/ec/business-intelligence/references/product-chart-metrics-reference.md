---
title: 商品圖表指標對照表
description: 認識商品圖表的三項核心指標：瀏覽數、購買數、成交率，以及計算方式與使用限制。
created: 2026-06-21 00:00
last_modified: 2026-07-12 20:49
lang: zh-TW
type: reference
status: update
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
  - 商品圖表
  - 瀏覽數
  - 購買數
  - 成交率
  - 指標對照
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/product-chart-metrics-reference/"
icon: lucide/table
hide:
---

# 商品圖表對照表

本頁集中放置「商品圖表」相關的指標對照表，供快速查閱。

## 商品圖表指標對照表 { #reference-product-chart-metrics }

| 指標 | 說明 | 計算方式 |
| :-- | :-- | :-- |
| 瀏覽數 | 期間內該商品頁被開啟的總次數。屬於原始數據，同一位顧客重複進入或重新整理頁面都會分別計算。 | 每日累計 |
| 購買數 | 期間內包含該商品的訂單成立筆數。記錄當日成立的訂單，不會因後續取消、退貨或付款狀態變動而調整。 | 每日累計 |
| 成交率 | 衡量商品頁將「瀏覽」轉換為「下單」的比率，用來評估商品頁文案、圖片或定價的轉單拉力。 | (購買數 ÷ 瀏覽數) × 100% |

!!! note "註釋"
    * 當瀏覽數為 0 時，成交率顯示為 0%。
    * 所有數據於每日凌晨 2 點更新前一日結果，當日的即時數據不會出現在報表中。
    * 系統僅保留近約 2 個月的每日數據，較早的數據將無法查詢。
