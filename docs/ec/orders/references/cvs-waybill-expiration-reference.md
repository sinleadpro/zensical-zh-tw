---
title: 超商託運單有效期限
description: 彙整各超商 B2C 與 C2C 託運單改為重新取號的判定期限。
created: 2026-08-27 11:06
last_modified: 2026-08-27 11:21
lang: zh-TW
type: reference
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 訂單
sites: 
  - TW
audiences: 
  - merchant
difficulty: ""
tnb: ""
plans: []
cyb_extensions: []
intents: 
  - 查詢超商託運單失效期限
  - 確認重新取號時間
features: 
  - 超商託運單失效期限
  - 補印託運單
  - 逾期重新取號
prerequisites: []
related: []
tags: []
acoiv: ""
apis: []
devices: []
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/cvs-waybill-expiration-reference/"
comments: false
search:
  exclude: false
icon: lucide/calendar-clock
hide: []
---

## 各物流託運單期限 { #reference-cvs-waybill-expiration }

建立託運單後，請於有效期限內完成出貨；託運單僅可在有效期限內補印。若超過期限且尚無配送記錄，原託運單會自動失效，無法再補印，需重新取號取得新託運單。

下表列出各超商物流的託運單失效判定期限：

> 表中的 **D** 代表第一次列印託運單的當日


| 服務類型 | 超商 | 託運單失效日 |
| :--- | :--- | :--- |
| B2C | 7-11 | D+14 天 |
| B2C | 全家（常溫 / 冷凍） | D+6 天 |
| B2C | 萊爾富 | D+6 天 |
| C2C | 7-11 | D+8 天 |
| C2C | 全家（常溫 / 冷凍） | D+8 天 |
| C2C | 萊爾富 | D+8 天 |

## 相關操作


<div class="grid cards" markdown>

- :lucide-refresh-cw:{ .lg }
  [__處理託運單逾期重新取號__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  原託運單失效或超過補印期限時，重新取得託運單號並下載新託運單。

</div>