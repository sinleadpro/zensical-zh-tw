---
title: 欠款自動扣繳設定
description: 使用 CYBERBIZ PAYMENTS 金流服務時，若當期帳單餘額為負值，系統將透過「欠款自動扣繳」機制從您綁定的信用卡中扣款，確保站台功能正常運作。
created: 2026-06-01 15:54
last_modified: 2026-06-26 16:29
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 管理中心
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents: 
  - 設定欠款自動扣繳
  - 解決帳單負值問題
  - 綁定對帳信用卡
features: 
  - 欠款自動扣繳
  - 對帳中心
  - CYBERBIZ_PAYMENTS
prerequisites: 
  - "需開通 CYBERBIZ PAYMENTS 金流服務"
related: []
tags: 
  - 自動扣繳
  - 信用卡綁定
  - 欠款處理
  - 對帳
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 對帳中心
  - 新增信用卡
paths: 
  - 管理中心 > 對帳中心
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=969
  - https://www.cyberbiz.io/support/?p=46501
permalink: "https://help.cyberbiz.io/ec/website-management/auto-deduction-of-arrears/"
comments: false
search:
  exclude: false
icon: lucide/credit-card
hide: []
---

# 欠款自動扣繳設定
使用 CYBERBIZ PAYMENTS 金流服務時，若當期帳單餘額為負值，系統將透過「欠款自動扣繳」機制從您綁定的信用卡中扣款，確保站台功能正常運作。
{ .subtitle }

[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | CYBERBIZ PAYMENTS
{ .doc-badge }

!!! tip "為什麼需要啟用此功能？"
    當對帳單顯示撥款金額為負值時，代表商家需補繳款項給系統。若未及時繳納，會影響站台的後續使用權限。啟用自動扣繳可省去手動繳費的麻煩，確保營運不中斷。


## 啟用步驟

**後台路徑**：`管理中心` > `對帳中心`

1. 登入 CYBERBIZ 管理後台，前往 **管理中心 > 對帳中心**。
2. 進入對帳中心頁面，點擊 **欠款自動扣繳**，開啟功能。
3. 點擊 **新增信用卡**，填寫卡片資訊並完成綁定。
4. 確認帳務郵件地址後勾選 **同意**。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-啟用欠款自動扣繳01.png){ .screenshot }


## 扣款時機與通知

系統會依據您的商家版本與發票開立方式，在不同的時間點執行扣繳：

| 商家類型 | 扣款時機 |
| :--- | :--- |
| **企業版（由 CYB 代開消費者發票）** | 當商家手動點擊 **確認帳款** 後，系統於 **隔日** 自動執行扣繳 |
| **一般 / PLUS 版 / 企業版（自開發票）** | 於每期 **確認帳款期限** 結束後的 **隔日** 自動執行扣繳 |

### 扣款通知規則

- **結果通知**：無論扣款成功或失敗，系統皆會寄送通知信至您的 **系統帳務信箱**。
- **失敗重試**：若扣繳失敗（如卡片額度不足、過期），系統每日會自動重新嘗試扣款，直到成功或商家系統到期為止。

