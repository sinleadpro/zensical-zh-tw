---
title: 前台可退貨天數對照表
description: 彙整退貨時間調整設定中各出貨方式的預設可退貨天數與計算起點，供結帳頁與金物流相關設定引用。
created: 2026-06-16
last_modified: 2026-07-06T17:33:13+08:00
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
  - 退貨天數
  - 出貨方式
  - 可退貨天數
  - 參考資料
permalink: https://help.cyberbiz.io/ec/payments-and-logistics/references/return-eligible-days-reference/
icon: lucide/table
hide:
---

# 前台可退貨天數對照表

本對照表彙整「退貨時間調整設定」中各出貨方式的預設可退貨天數與計算起點,供結帳頁與金物流相關設定引用。

## 各出貨方式可退貨天數 { #return-eligible-days }

| 出貨方式 | 設定欄位 | 預設天數 | 計算起點 |
| :-- | :-- | :-- | :-- |
| CYBERBIZ 宅配、超商取貨 | CYBERBIZ 宅配、超取的可退貨天數 | 10 天 | 物流狀態為「已收貨」後 |
| 其他出貨方式(含自訂物流) | 其他出貨方式的可退貨天數 | 14 天 | 物流狀態為「已出貨」後 |

!!! note "註釋"
    * 欄位 **留空** 代表使用上述系統預設天數。
    * 欄位填入 **0** 代表不開放顧客在前台自行申請退貨。
    * 「前台部分退貨申請」為另一項開通功能，開啟後顧客可在退貨申請頁勾選欲退貨的商品,部分退貨的退款金額仍由商家決定。
