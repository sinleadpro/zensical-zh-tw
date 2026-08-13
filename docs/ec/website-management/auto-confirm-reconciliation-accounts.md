---
title: 自動確認對帳帳款設定
description: 當商家使用 CYBERBIZ PAYMENTS 金流服務時，系統預設需由商家手動確認帳款後方可撥款。啟用「帳款自動確認」功能後，系統將在帳款累計達設定門檻時，於帳期截止日自動完成確認，確保撥款流程不中斷。
created: 2026-06-01 16:06
last_modified: 2026-06-01 16:06
lang: zh-TW
type: guide
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
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - 專業
  - 進階
  - 高手
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents: 
  - 設定自動確認帳款
  - 避免漏確認撥款
  - 自動化對帳流程
features: 
  - 自動確認帳款
  - 對帳中心
  - CYBERBIZ PAYMENTS
prerequisites: 
  - "需開通 CYBERBIZ PAYMENTS 金流服務"
related: 
  - "對帳中心管理指南"
  - "ec/website-management/auto-deduction-of-arrears"
tags: 
  - 自動對帳
  - 撥款流程
  - 帳務自動化
  - 對帳中心
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 對帳中心
  - 自動確認帳款彈窗
paths: 
  - 管理中心 > 對帳中心
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=4507
permalink: "https://help.cyberbiz.io/ec/website-management/auto-confirm-reconciliation-accounts/"
comments: false
search:
  exclude: false
icon: lucide/circle-check
hide: []
---

# 自動確認對帳帳款設定
當商家使用 CYBERBIZ PAYMENTS 金流服務時，系統預設需由商家手動確認帳款後方可撥款。啟用「帳款自動確認」功能後，系統將在帳款累計達設定門檻時，於帳期截止日自動完成確認，確保撥款流程不中斷。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 專業 / 進階 / 高手 / 所有 PLUS 版
[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | CYBERBIZ PAYMENTS
{ .doc-badge }

!!! warning "版本限制"
    此功能僅限 **一般版** 與 **PLUS 版** ，且 **使用 CYBERBIZ PAYMENTS** 金流服務商家使用。**企業版** 商家因涉及請款發票開立流程，不適用此自動確認功能。



## 為什麼需要啟用帳款自動確認？

在 CYBERBIZ PAYMENTS 的撥款流程中，商家必須進入 **對帳中心** 確認撥款金額無誤，系統才會執行撥款。

若商家因忙碌而漏掉手動確認，將導致該期款項延遲撥付。啟用此功能後，只要符合您設定的金額門檻，系統將在 **每期最後確認日的 23:59** 自動為您完成確認。


## 啟用步驟


1. 登入 CYBERBIZ 管理後台，前往 **管理中心 > 對帳中心**。
1. 在對帳中心頁面，點擊 **帳款自動確認** 按鈕。
2. 在彈出的視窗中完成以下配置：
    - **開啟開關**：將 **自動確認帳款** 切換為開啟狀態。
    - **設定金額門檻**：輸入欲自動確認的累計金額（例如：3,000 元）。
    - **填寫帳務信箱**：設定接收自動確認紀錄與提醒的電子郵件。
3. 閱讀並勾選責任條款後，點擊 **確認** 即可啟用。

![](https://www.cyberbiz.io/support/wp-content/uploads/自動確認帳款02.png){ .screenshot }



## 自動確認邏輯說明

### 1. 金額門檻判定

系統會計算 **所有未確認帳期** 的總累計金額。

- **達門檻**：若累計金額已達設定門檻，系統將自動確認。
- **未達門檻**：若累計金額未達設定門檻，系統會等待後續帳期累加，直到達標後才在下一個截止日自動確認。

!!! example "範例"
    門檻設為 3,000 元。若目前有兩期未確認帳款共 2,500 元，系統不會自動確認；待第三期產生使總額達 3,000 元以上時，系統才會執行自動確認。

### 2. 自動確認時機

系統會在 **每個帳期的最後確認日 23:59** 執行判定與確認。

!!! example "範例"
    若您的撥款週期為週週撥，最後確認期限為每週二，系統則會在週二深夜執行。

### 3. 通知規則

- **功能異動**：每次啟用或關閉此功能，系統皆會寄送通知至帳務信箱。
- **執行紀錄**：每次系統成功執行自動確認後，皆會寄送明細郵件供商家核對。
