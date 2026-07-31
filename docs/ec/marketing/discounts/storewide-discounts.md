---
title: 設定全館折扣
description: 了解如何建立全站促銷活動，包含金額折扣、百分比折抵及滿額贈送優惠券，提升官網客單價與回購率。
created: 2026-06-26 18:30
last_modified: 2026-06-26 18:30
lang: zh-TW
type: guide
status: update
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 行銷活動
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定全館折扣活動
  - 建立滿額折抵優惠
  - 設定滿額送優惠券
features: 
  - 全館折扣
  - 滿額贈券
  - 累計折抵
prerequisites: []
related: 
  - "ec/marketing/coupon/setup-coupons"
  - "ec/marketing/discounts/mix-and-match-discounts"
tags: 
  - 全館折扣
  - 促銷活動
  - 滿額折抵
  - 滿額贈
acoiv: configure
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 舉辦全館活動
  - 新增全館活動
paths: 
  - 行銷活動 > 全館折扣-紅利 & 優惠券 > 舉辦全館活動
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=1165
  - https://www.cyberbiz.io/support/?p=30011
permalink: "https://help.cyberbiz.io/ec/marketing/discounts/storewide-discounts/"
search:
  exclude: false
icon: lucide/percent
hide: []
---

# 設定全館折扣
了解如何建立全站促銷活動，包含金額折扣、百分比折抵及滿額贈送優惠券，提升官網客單價與回購率。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 全方案
{ .doc-badge }

!!! tip "應用情境"
	- **節慶促銷**：舉辦「全站結帳 85 折」或「全站消費滿千享 8 折」活動。
	- **滿額折現**：設定「滿千折百」活動，直接折抵當次消費金額。
	- **引導回購**：設定「滿額送優惠券」，顧客完成訂單後獲得折扣供下次使用。


## 使用須知

- **最優折扣判定**：若同時存在多個「金額」與「百分比」全館活動，系統將自動選擇折價金額最高的優惠套用。
- **優惠券啟用時機**：滿額贈送的優惠券於「訂單成立」時匯入顧客帳戶，但必須等「訂單結案」後方可正式啟用。
- **退貨限制**：若訂單狀態為「已退貨」、「部分退貨」、「逾期未取」或「已退款」，結案後系統將不會啟用該筆贈送的優惠券。


## 操作流程

### 建立金額或百分比折扣
針對當次消費直接進行金額減免。

1. 登入 CYBERBIZ 管理後台，前往 **行銷活動 > 全館折扣-紅利 & 優惠券**。
2. 點擊 **新增全館活動**。

	![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動01.png){ .screenshot }

3. 設定活動基本資訊：
    - **活動名稱**：輸入活動名稱。
    - **消費金額**：設定觸發優惠的最低消費門檻。
    - **起始/終止日期**：設定活動效期。留空則表示立即開始且不限期。
4. 選擇活動種類：

    === "金額"

        輸入折抵金額。可勾選 **是否累計折抵**（如：滿千折百，滿兩千折兩百）。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動02.png){ .screenshot }

    === "百分比"

        輸入折抵比例（如：85 折輸入 85%）。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動02.png){ .screenshot }

    === "優惠券"

        !!! info "適用版本"
            此功能僅支援 **高手版**、**高手 PLUS**、**企業版** 使用。

        1. 設定優惠券規格：
            - **優惠券金額**：設定贈送的折扣面額。
            - **活動期間**：設定券的起始時間與終止時間。
            - **最低消費限制**：設定顧客下次使用此券時的最低門檻。
        2. 配置限制規則：
            - **綁定商品標籤**：限制此券僅能折抵特定標籤商品。
            > 此功能不支援 **專業版** 使用。
            - **併用限制**：設定此券與其他行銷活動的堆疊規則。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-全館活動03.png){ .screenshot }



## 系統判定邏輯

### 多門檻贈送規則

當商家設定多個不同門檻的「滿額贈券」活動時，系統僅會選擇 **符合條件的最高門檻** 贈送一張，不會累計贈送。

!!! example "範例：多門檻判定"
    - **門檻一**：滿 1,000 送 50 元券。
    - **門檻二**：滿 1,500 送 100 元券。
    - **結果**：
        - 顧客消費 1,200：符合門檻一，獲贈 50 券一張。
        - 顧客消費 1,600：符合門檻二，獲贈 100 券一張（不會同時獲得 50 券）。
