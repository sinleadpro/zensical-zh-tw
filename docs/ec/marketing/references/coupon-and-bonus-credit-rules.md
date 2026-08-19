---
title: 優惠券／紅利歸戶規則
description: 說明消費回饋的優惠券與紅利何時匯入會員帳戶，以及結案、退貨狀態與退貨流程如何影響歸戶。
created: 2026-08-19 12:35
last_modified: 2026-08-19 12:35
lang: zh-TW
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 行銷活動
  - 訂單
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 紅利何時入帳
  - 優惠券何時歸戶
  - 結案與退貨對紅利的影響
features: 
  - 紅利歸戶
  - 優惠券歸戶
  - 訂單結案
  - 退貨狀態
prerequisites: []
related:
  - "ec/marketing/bonus-and-gifts/setup-bonus-points.md"
  - "docs/ec/marketing/coupon/setup-coupons.md"
  - "docs/ec/payments-and-logistics/payments/order-settings.md"
  - "docs/ec/members/manage-member-profiles.md"
tags: 
  - 紅利
  - 優惠券
acoiv: operation
apis: []
devices: []
ui_components: []
paths: 
  - 訂單 > 訂單列表
  - 行銷活動 > 全館折扣-紅利 & 優惠券
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/marketing/references/coupon-and-bonus-credit-rules/"
comments: false
search:
  exclude: false
icon: lucide/wallet
hide: []
---

# 優惠券／紅利歸戶規則

說明消費回饋的優惠券與紅利何時匯入會員帳戶，以及結案、退貨狀態與退貨流程如何影響歸戶。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 全版本
{ .doc-badge }

## 使用須知
- **適用範圍**：因訂單消費而回饋至會員帳戶的紅利點數與優惠券。
- **不適用範圍**：
    - 註冊禮、生日禮、全館或手動立即發送的紅利／優惠券
    - [全館折扣送優惠券](../discounts/storewide-discounts.md)（優惠券於訂單成立時發送，訂單結案後方可啟用）
    - 顧客於結帳時折抵使用的紅利／優惠券

        > 折抵用紅利退貨時是否返還，請見 [設定紅利點數：退貨處理](../bonus-and-gifts/setup-bonus-points.md#退貨處理)


## 歸戶條件
消費回饋不會在付款成功當下入帳。系統會在商家確認訂單完成、且訂單沒有執行退貨後，才將紅利或優惠券寫入會員帳戶。

歸戶須 **同時** 符合下列條件：

- 訂單狀態：**已結案**
- 退貨狀態：**不需退貨**


## 商家常見情境

| 商家操作情境 | 結案當下的退貨狀態 | 系統結果 | 後續處理建議 |
| --- | --- | --- | --- |
| 正常出貨、顧客未申請退貨，過退換貨期後結案 | **不需退貨** | **會** 歸戶 | - |
| 顧客已申請退貨，訂單在退貨流程中就結案 | **退貨中** | **不會** 歸戶 | - |
| 包裹已取回、尚在驗貨／審核時結案 | **退貨審查** | **不會** 歸戶 | - |
| 驗貨判定不符條件，標記為 **拒絕退貨** 後結案 | **拒絕退貨** | **不會** 歸戶 | 如需發送請手動補送 |
| 訂單於 **已結案** 狀態後才執行退換貨流程 | **不需退貨** | **會** 歸戶（不自動扣回） | 如需收回請手動刪除 |

!!! tip "建議時機"
    建議等訂單過退換貨期間、確定已無退貨需求後，再按下 **結案訂單**，以確保紅利發放的準確性並減少事後手動調整的需求。

## 更多操作


<div class="grid cards" markdown>

- :lucide-coins:{ .lg }
  [__手動新增／刪除紅利__](../../members/manage-member-profiles.md#1-紅利點數派發與管理)
  補送或移除消費回饋紅利點數。

- :lucide-ticket-percent:{ .lg }
  [__手動新增／刪除優惠券__](../../members/manage-member-profiles.md#2-優惠券派發與管理)
  補送或移除會員專屬優惠券。

</div>

