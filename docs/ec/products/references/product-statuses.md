---
title: 商品狀態對照表
description: ""
created: 2026-06-05 13:40
last_modified: 2026-07-06 19:08
lang: zh-TW
type: reference
status: update
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
  - merchant
difficulty: ""
tnb: ""
plans:
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - 商品管理
  - 商品狀態
  - 上架狀態
  - 公開狀態
  - 站內搜尋
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/references/product-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

商品是否能在前台被看到、被搜尋到、被購買,由三組各自獨立的狀態決定。下表說明各狀態的意義與顯示位置。

### 商品上架與公開狀態對照表 { #reference-product-statuses }

| 狀態類別 | 顯示文字 | 說明 |
| :-- | :-- | :-- |
| 上架狀態 | 已上架 | 目前在販售期間內(已到上架時間、未到下架時間),前台正常販售。 |
| 上架狀態 | 未上架 | 已設定 **上架時間** 但尚未到,商品在前台暫不顯示,時間到自動上架。 |
| 上架狀態 | 已下架 | 已超過設定的 **下架時間**,商品自動從前台下架。 |
| 公開狀態 | 公開 | 商品可在前台正常陳列與販售。 |
| 公開狀態 | 不公開 | 商品在前台隱藏,連結也無法購買,常用於暫時停售或尚在準備中的商品。 |
| 商品搜尋 | 開啟搜尋 | 顧客可在站內搜尋找到此商品。 |
| 商品搜尋 | 排除搜尋 | 商品不出現在站內搜尋結果,但您仍可提供商品連結讓特定顧客購買,且不影響 Google 搜尋。 |

!!! note "註釋"
    * **上架狀態** 由上架時間 / 下架時間自動計算;兩者皆留空代表「立即上架、永不下架」。
    * **上架狀態** 與 **公開狀態** 互相獨立:即使在上架期間內,設為「不公開」仍不會顯示於前台。
    * POS 門市商品無法設定為「公開」,僅供門市端使用。
