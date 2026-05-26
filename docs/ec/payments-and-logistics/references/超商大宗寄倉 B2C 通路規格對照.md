---
title: 超商大宗寄倉B2C通路規格
description: ""
created: 2026-05-25 21:42
last_modified:
lang: zh-TW
type: tutorial
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
icon: lucide/ruler
hide:
---

{ .subtitle }

{ .doc-badge }

{ .hero-page }

# 超商大宗寄倉 B2C 通路規格對照

各通路的重量 / 材積上限與申請時必填欄位差異。供「設定超商大宗寄倉 B2C」與「使用超商大宗寄倉 B2C 出貨」兩篇主文共同引用。
{ .subtitle }

## 重量與材積限制 { #reference-cvs-b2c-channels-specs }

| 通路 | 重量上限 | 三邊總和 | 最長邊 |
| :-- | :-- | :-- | :-- |
| 7-ELEVEN 超商取貨 | 10 kg | ≤ 105 cm | ≤ 45 cm |
| 全家超商取貨 | 5 kg | ≤ 120 cm | 依官方公告 |
| 全家冷凍超商取貨 | 5 kg | ≤ 105 cm | 依官方公告 |
| 萊爾富超商取貨 | 5 kg | ≤ 105 cm | ≤ 45 cm |

!!! note "註釋"
    * 商品建檔時若填寫的重量 / 材積超過上限，前台會自動阻擋消費者選擇此配送方式。
    * 實際上限以申請當下各超商官方公告為準。

---

## 申請時必填欄位 { #reference-cvs-b2c-channels-fields }

各通路於「商家資訊申請頁」需填寫的欄位差異：

| 欄位 | 7-ELEVEN | 全家 | 全家冷凍 | 萊爾富 |
| :-- | :--: | :--: | :--: | :--: |
| 公司名稱 | ✅ | ✅ | ✅ | ✅ |
| 聯絡人名稱 | ✅ | ✅ | ✅ | ✅ |
| 聯絡電郵 | ✅ | ✅ | ✅ | ✅ |
| 退貨地址 | ✅ | ✅ | ✅ | ✅ |
| 公司電話 | ✅ | ✅ | ✅ | ✅ |
| 退貨方式 | ✅ | ✅ | — | ✅ |
| 退貨頻率 | ✅ | ✅ | — | ✅ |
| 商家別名 | ✅ | — | — | — |
| 統一編號 | ✅ | — | — | — |
| 公司網站 | ✅ | — | — | — |
| 商品類型 | ✅ | — | — | — |
| 指定回收日 | — | — | ✅ | — |
| 倉庫門市名稱 | — | — | ✅ | — |
| 營業時間 | — | — | ✅ | — |
| 休業日 | — | — | ✅ | — |

!!! note "註釋"
    * 7-ELEVEN 因額外要求公司基本資料與商品類型驗證，必填欄位最多。
    * 全家冷凍因涉及冷鏈倉儲，需額外填寫倉庫資訊。
    * 欄位送出後將同步至各超商系統，請務必填寫正確。

---



## 後續操作

<div class="grid cards" markdown>

- :lucide-import:{ .lg }
  [____]()
  。

- :lucide-ban:{ .lg }
  [____]()
  。

</div>

## 常見問題

??? quote ""

