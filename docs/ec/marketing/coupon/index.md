---
title: 了解優惠券與優惠碼
description: 協助商家區分優惠券與優惠碼的定義、發送方式與使用情境，以選擇最合適的行銷工具。
created: 2026-06-11 12:20
last_modified: 2026-06-22 11:15
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
  - 行銷活動
  - 金物流
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 了解優惠券與優惠碼的差異
  - 選擇合適的行銷工具
features: 
  - 優惠券
  - 優惠碼
prerequisites: []
related:
  - ec/marketing/bonus-and-gifts/setup-registration-gift/
  - ec/marketing/bonus-and-gifts/setup-birthday-gift/
  - ec/marketing/bonus-and-gifts/limited-time-first-purchase-gift/
  - ec/marketing/other-tools/interactive-games/
  - ec/marketing/conditional-send/send-coupons-for-specific-products/
  - ec/marketing/coupon/setup-coupons/
  - ec/marketing/coupon/setup-promo-codes/
  - ec/marketing/coupon/free-shipping-coupon-spec/
  - ec/marketing/coupon/gift-coupon-spec/
  - ec/marketing/purchase-restrictions/coupon-and-bonus-points-expiry-notification/
  - ec/marketing/coupon/multiple-coupons/
tags: 
  - 優惠券
  - 優惠碼
  - 行銷工具
acoiv: configure
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 結帳頁面
  - 會員中心
paths:
  - 金物流 > 結帳頁 & 物流設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/"
search:
  exclude: false
icon: lucide/split
hide: []
---

# 了解優惠券與優惠碼
協助商家根據營運需求，在「歸戶式優惠券」與「通用式優惠碼」之間選擇最合適的行銷工具。
{ .subtitle }

## 功能概述

優惠券與優惠碼是官網行銷活動中核心的折扣工具，**優惠碼為優惠券的一項分支**，兩者在結帳層級中屬於同等地位，皆可用於折抵訂單金額。

- 優惠券讓商家能將折扣精準歸戶至會員帳號。
- 優惠碼則讓商家能透過一組通用代碼進行廣泛傳播。


## 核心差異比對

下表說明優惠券與優惠碼在系統定位與使用方式上的主要差異：

| 比較項目 | 優惠券 | 優惠碼 |
| :--- | :--- | :--- |
| **系統定位** | **歸戶式**（綁定會員帳號） | **通用式**（不綁定帳號） |
| **可見性** | 會員可於 **會員中心 > 專屬優惠券** 查看 | 會員中心不顯示，由商家對消費者推廣 |
| **發送方式** | 系統自動發送或商家手動派發至帳戶 | 商家提供序號，由顧客自行輸入 |
| **使用方式** | 結帳時直接從 **可用優惠** 清單中點選 | 結帳時需手動輸入正確的 **優惠序號** |


## 使用場景

### 優惠券

- **自動化獎勵**：透過系統支援的行銷活動，在特定時機點（如註冊、生日、首購）觸發寄送優惠券。

    <div class="grid cards" markdown>

    - :lucide-user-plus:{ .lg }
      [__註冊禮__](../bonus-and-gifts/setup-registration-gift.md)
      於顧客完成會員註冊時自動發送。

    - :lucide-cake:{ .lg }
      [__生日禮__](../bonus-and-gifts/setup-birthday-gift.md)
      於會員生日月份自動派發專屬折扣。

    - :lucide-shopping-cart:{ .lg }
      [__首購禮__](../bonus-and-gifts/limited-time-first-purchase-gift.md)
      針對完成首筆訂單的顧客提供獎勵。

    - :lucide-gamepad-2:{ .lg }
      [__互動遊戲__](../other-tools/interactive-games.md)
      透過轉盤、抽紅包等遊戲化機制發放獎項。

    - :lucide-package-plus:{ .lg }
      [__指定商品送優惠券__](../conditional-send/send-coupons-for-specific-products.md)
      購買特定商品後自動送券。

    </div>

- **特定對象回饋**：針對指定會員名單發送專屬回饋券。

    <div class="grid cards" markdown>

    - :lucide-ticket:{ .lg }
      [__設定優惠券__](setup-coupons.md)
      了解如何建立歸戶式優惠券、設定發送條件。

    </div>

### 優惠碼

- **不歸戶優惠代碼**：全館通用且不限領取對象，消費者於結帳頁面輸入代碼即可輕鬆享有優惠。

    <div class="grid cards" markdown>

    - :lucide-hash:{ .lg }
      [__設定優惠碼__](setup-promo-codes.md)
      了解如何產生優惠序號、設定使用次數限制。

    </div>
    

## 各類型優惠券規格

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__免運券規格__](free-shipping-coupon-spec.md)
    掌握免運券限制與結帳流程。

- :lucide-hash:{ .lg }
    [__贈品券規格__](gift-coupon-spec.md)
    瞭解贈品券限制與庫存規則。

</div>

## 結帳順序

優惠券與優惠碼的折抵順序相同，在計算「折扣活動」、「加價購」及「滿額贈」之後。若優惠券（碼）設有金額門檻，須在上述折扣計算後仍符合門檻才可套用。

![](https://www.cyberbiz.io/support/wp-content/uploads/2020/03/結帳順序-優惠券.png){ .screenshot }

## 啟用結帳頁優惠券（碼）折抵功能

若要讓顧客在結帳時能使用優惠券（碼），必須先開啟前台顯示開關。

1. 登入 CYBERBIZ 管理後台，前往 **金物流 > 結帳頁 & 物流設定**。
2. 找到 **結帳頁優惠券設定** 區塊，將功能切換為 `開啟`。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼13.png){ .screenshot }
    

## 優惠券（碼）共同設定

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }
  [__優惠券（碼）與紅利點數到期通知__](../purchase-restrictions/coupon-and-bonus-points-expiry-notification.md)
  設定系統自動發送 Email、簡訊或 LINE 通知，提醒顧客及時使用即將到期的優惠券與紅利點數。

- :lucide-hash:{ .lg }
  [__多優惠券（碼）__](multiple-coupons.md)
  設定單筆訂單可使用的優惠券（碼）數量上限，並了解多重折扣的折抵邏輯。

</div>



## 常見問題

??? quote "為什麼會員反應在後台看不到我發布的優惠碼？"
    優惠碼屬於「不歸戶」性質，系統不會自動顯示在會員中心。商家需透過 Email、簡訊、官網橫幅或社群媒體將序號告知顧客。
