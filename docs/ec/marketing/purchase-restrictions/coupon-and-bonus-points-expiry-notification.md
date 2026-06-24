---
title: 優惠券（碼）與紅利點數到期通知
description: 商家可設定優惠券（碼）/ 紅利點數的到期提醒，透過 Email、簡訊或 LINE OA 通知消費者盡早使用，有效提升行銷活動的回購率。
created: 2026-05-27 18:04
last_modified: 2026-06-04 17:59
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
  - 行銷活動
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定優惠券到期通知
  - 設定紅利點數到期提醒
  - 提升行銷活動回購率
features: 
  - 優惠券到期通知
  - 紅利點數到期通知
  - 訊息推播
prerequisites: []
related: []
tags: 
  - 優惠券
  - 紅利點數
  - 到期通知
  - 行銷自動化
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: []
paths: 
  - 行銷活動 > 全館折扣 – 紅利&優惠券 > 優惠券/紅利點數到期通知
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=11115
permalink: https://help.cyberbiz.io/ec/marketing/purchase-restrictions/coupon-and-bonus-points-expiry-notification
comments: false
search:
  exclude: false
icon: lucide/bell
hide: []
---
# 優惠券（碼）與紅利點數到期通知
商家可設定優惠券（碼）/ 紅利點數的到期提醒，透過 Email、簡訊或 LINE OA 通知消費者盡早使用，有效提升行銷活動的回購率。
{ .subtitle }

## 設定到期天數

1. 登入 CYBERBIZ 管理後台，前往 **行銷活動 > 全館折扣 – 紅利&優惠券 > 優惠券/紅利點數到期通知**。
2. 設定於到期前 **N 天** 發送通知訊息。
    > 若需調整設定，請於發送前一天的 23:59 前完成，以確保系統能正確排查名單。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知01.png){ .screenshot }

## 系統發送邏輯

- **到期時間**：
    - **優惠券(碼)**：截止日當天的 23:59:59。
    - **紅利點數**：建立紅利點數時所設定的具體時間。
- **排程時間**：系統於每日 **凌晨 3 點** 檢查符合條件的會員，並於 **中午 12 點** 統一發送通知。


    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知07.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知08.png){ .screenshot }

    </div>

## 開啟通知管道

請務必前往以下路徑開啟對應的通知開關：

=== "Email"

    後台路徑：訊息推播 > Email 通知樣板 > 顧客相關

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知02.png){ .screenshot }   

=== "簡訊"

    後台路徑：訊息推播 > 簡訊通知樣板 > 顧客相關

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知03.png){ .screenshot }   

=== "LINE OA"

    後台路徑：訊息推播 > LINE OA 通知樣板 > 顧客相關

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知04.png){ .screenshot }