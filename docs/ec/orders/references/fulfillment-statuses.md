---
title: 配送狀態對照表
description: "彙整 CYBERBIZ 新版訂單列表的配送狀態(未出貨、已出貨、已收貨等)與出現時機，供搜尋、篩選與出貨引用。"
created: 2026-06-04 15:06
last_modified: 2026-07-02 08:53
lang: zh-TW
type: reference
author: Jase
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
  - merchant
difficulty: ""
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - 配送狀態
  - 訂單列表
  - 出貨管理
  - 已到店
  - 逾期未取
  - 運送異常
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/fulfillment-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

本對照表彙整 CYBERBIZ 新版訂單列表的配送狀態，供搜尋、篩選、出貨等功能引用。

## 配送狀態一覽 { #fulfillment-statuses-table }

| 配送狀態 | 說明 | 出現時機 |
| :-- | :-- | :-- |
| 未出貨 | 訂單尚未安排出貨 | 訂單成立後的預設狀態 |
| 準備出貨 | 已開始備貨，尚未產生託運單 | 商家手動標示，或串接倉儲開始作業 |
| 部分出貨 | 訂單中部分商品已寄出，仍有商品未出 | 在訂單詳情頁逐項勾選出貨後 |
| 已出貨 | 託運單已產生或已標示出貨 | 下載託運單、自訂物流出貨或匯入單號後 |
| 已到店 | 超商取貨商品已送達指定門市 | 超商取貨類物流的到店回報 |
| 已收貨 | 顧客已取貨或簽收 | 物流回報，或商家手動標示 |
| 逾期未取 | 超商取貨包裹超過保留期未領取 | 超商取貨逾期回報 |
| 運送異常 | 配送過程發生問題 | 物流回報異常 |
| 已退貨 | 商品已退回 | 退貨流程完成後 |
| 取消出貨 | 已取消原本的出貨 | 商家取消出貨動作 |
| 不需出貨 | 該訂單無實體配送需求 | 純數位商品、電子票券等 |

!!! note "註釋"
    * 實際可見的配送狀態會依商品類型與所用物流而定，並非每筆訂單都會經歷上述所有狀態。
    * 「已到店」「逾期未取」僅適用於超商取貨類物流，一般宅配不會出現。
    * 數位商品、電子票券等無需配送的訂單會顯示「不需出貨」。
