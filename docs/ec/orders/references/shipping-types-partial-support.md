---
title: 物流類型部分出貨支援對照表
description: ""
created: 2026-06-05 12:13
last_modified: 2026-06-05 12:25
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

本對照表彙整 CYBERBIZ 各物流類型對「部分出貨」的支援情形，供搜尋、出貨、報表等功能引用。

## 各物流類型部分出貨支援 { #shipping-types-partial-support }

| 物流類型 | 後台直接部分出貨 | 開通條件 / 備註 |
| :-- | :-- | :-- |
| 黑貓宅急便 | 支援 | 標準宅配，需先開通黑貓物流 |
| 宅配通 | 支援 | 標準宅配，需先開通宅配通物流 |
| 新竹物流 | 支援 | 標準宅配，需先開通新竹物流 |
| 順豐速運 | 支援 | 標準宅配，需先開通順豐物流 |
| 自訂出貨方式 | 支援 | 自行填入快遞單號與物流公司 |
| 7-11 一般取貨 / 取貨付款 | 支援 (店到店) | 後台支援超商一般出貨；多次出貨需加購「API 超商部分出貨」 |
| 全家 一般取貨 / 取貨付款 | 支援 (店到店) | 同上 |
| 7-11 店到店 (C2C) | 支援 | — |
| 全家 店到店 (C2C) | 支援 | — |
| 萊爾富 店到店 (C2C) | 支援 | — |
| 萊爾富 B2C (一般取貨 / 取貨付款) | 不支援 | 萊爾富 B2C 不允許部分出貨 |
| 全家 冷鏈託運單 | 不支援 | 全家冷鏈規格限制，需一次寄出 |
| 黑貓 快速到店 (常溫 / 冷藏 / 冷凍) | 支援 | 仍走「選擇出貨方式」下拉操作 |
| 大宗寄倉 B2C | 不支援 | 大宗寄倉物流不允許部分出貨 |
| 快速到貨 CYBERBIZ NOW (Uber Direct / pandago) | 一次性 | 預設每筆訂單僅可出貨一次；多次出貨需加購「API 快速到貨部分出貨」 |
| Amazon FBA | 不支援 | 由 Amazon 倉庫端出貨，商家不在後台操作 |
| 串倉倉庫 (Cyberbiz 倉、SUDA 倉等) | 視加購情況 | 全部商品都來自串倉時不可部分出貨；混合自行出貨時需加購「部分串倉」 |

!!! note "註釋"
    * 「後台直接部分出貨」一欄指的是商家在訂單詳情頁的「出貨」區塊中，可以勾選部分商品執行出貨的能力。
    * 對於需要 API 操作的情境(超商多次出貨、快速到貨多次出貨)，請聯繫 CYBERBIZ 業務窗口加購對應的加值功能。
    * 下拉選單實際顯示的物流選項會依您店家已開通的物流組合動態變化。

