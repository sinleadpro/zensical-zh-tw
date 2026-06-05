---
title: 配送方式分類對照表
description: ""
created: 2026-06-04 15:15
last_modified: 2026-06-04 15:23
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

本對照表彙整 CYBERBIZ 系統串接物流可產生的託運單類型，供出貨、搜尋與篩選等功能引用。自訂物流(自行配送、合作貨運)不在此列，以手動標示出貨並填寫單號的方式處理。

## 系統串接物流分類 { #shipping-methods }

| 分類 | 配送方式 | 說明 | 開通條件 |
| :-- | :-- | :-- | :-- |
| 宅配到府 | 黑貓宅急便 | 常溫宅配到收件地址 | 標準串接 |
| 宅配到府 | 宅配通 | 常溫宅配到收件地址 | 多數付費方案內建 |
| 宅配到府 | 新竹物流 | 常溫宅配到收件地址 | 標準串接 |
| 宅配到府 | 順豐速運 | 宅配到府，支援海外配送 | 海外配送需企業版 / 跨境方案 |
| 超商取貨 | 7-11、全家、萊爾富 | 顧客至超商門市取貨 | 標準串接 |
| 超商店到店 | 7-11 交貨便、全家店到店、萊爾富店到店 | 店到店寄件，顧客至門市取貨 | 標準串接 |
| 超商冷凍 / 冷鏈 | 全家冷鏈、全家冷凍店到店、萊爾富冷凍 | 低溫商品的超商取貨 | 標準串接 |
| 快速到店 | 黑貓快速到店-常溫 / 冷藏 / 冷凍 | 黑貓配送至超商門市取貨 | 標準串接 |
| 門市自取 | 到店取貨條碼單 | 顧客至商家門市自行取貨 | 需設定門市 |
| 即時配送 | Pandago、Uber Direct | 同城即時派送 | 加值功能 |
| 跨境 / 海外 | DHL、LINEX、順豐(海外) | 國際 / 跨境配送 | 企業版 / 跨境方案 |

!!! note "註釋"
    * 實際可選的配送方式會依您開通的物流與方案動態顯示，並非每間商店都具備上述全部選項。
    * 超商託運單若要使用熱感印，需 PLUS版 或企業版。
    * 自訂物流不在本表內；未串接的物流請以「自訂物流出貨」手動標示並填寫託運單號。
