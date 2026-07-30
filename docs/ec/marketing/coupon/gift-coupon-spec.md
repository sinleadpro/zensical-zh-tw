---
title: 贈品券規格
description: 說明 CYBERBIZ 贈品券的規格、商品限制、建立方式及結帳流程。
created: 2026-06-17 10:39
last_modified: 2026-07-06 17:00
lang: zh-TW
type: reference
status: update
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
tnb: branch
plans:
    - 專業PLUS
    - 進階PLUS
    - 高手PLUS
    - 企業
cyb_extensions: []
intents: 
    - 瞭解贈品券規格
    - 設定贈品券
    - 處理贈品券庫存問題
features: 
    - 贈品券
    - 優惠券
    - 庫存管理
prerequisites: 
    - [[setup-coupons]]
    - [[setup-promo-codes]]
related: 
    - [[setup-coupons]]
    - [[setup-promo-codes]]
    - [[multiple-coupons]]
tags:
    - 贈品券
    - 優惠券
    - 行銷活動
    - 贈品贈送
acoiv: configure
apis: []
devices: 
    - desktop
    - mobile
ui_components:
    - 結帳頁面
    - 優惠券輸入框
paths: 
    - 行銷活動 > 優惠券設定
    - 會員 > 所有會員
layouts: []
wp_url: 
    - https://www.cyberbiz.io/support/?p=41796
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/gift-coupon-spec/"
comments: false
search:
  exclude: false
icon: lucide/gift
hide: []
---
# 贈品券規格
說明 CYBERBIZ 贈品券的規格、商品限制、建立方式及結帳流程。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有PLUS / 企業
{ .doc-badge }

!!! info "版本差異說明"
    - 「贈品券」在 PLUS 方案中屬於選配模組（11 選 2），商家需確認已選配該模組方可使用。企業版則直接內建此功能。

## 使用須知

- **商品限制**：贈品券不支援組合品。
- **上架限制**：贈品券僅支援與「已上架」的一般商品進行綁定。
- **下架觸發**：若綁定的主商品變更為「下架」狀態，該贈品券將自動失效並同步下架，使用者無法於前台購物車中搜尋、檢視或折抵該贈品券。
- **通路限制**：贈品券不支援 POS、定期定額及 CYBERBIZ NOW! 快速到貨。
- **串倉物流限制**：串倉商家使用贈品券時，贈送商品必須填寫 SKU 碼，否則會套用失敗。
- **API 串接**：
    - API / webhook 的訂單商品裡會出現。
    - 支援透過 API 方式，新增贈品券。

        > VIP 生日禮/升等禮/會員日發送之贈品券，則無法透過 API 的方式新增。

- **空購物車判定**：系統不支援「購物車內僅有贈品券商品」的情境。若購物車中未包含任何一般付費商品，系統將判定該購物車為「空購物車」，進而無法執行後續結帳流程。


## 建立贈品券

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__會員列表發送優惠券__](../../members/manage-member-profiles.md#2-優惠券派發與管理)
    使用會員篩選器批次發送優惠券。

- :lucide-hash:{ .lg }
    [__互動遊戲發送優惠券__](../other-tools/interactive-games.md)
    建立互動遊戲，透過輪盤或抽獎遊戲發送贈品券。

- :lucide-hash:{ .lg }
    [__建立贈品優惠碼__](setup-promo-codes.md)
    建立不歸戶全館優惠碼，會員於結帳時輸入優惠碼後可獲得贈品。

- :lucide-hash:{ .lg }
    [__建立 VIP 優惠__](../../members/vip/setup-exclusive-vip-discounts/)
    VIP 生日/升等/會員日時，發送贈品券。


</div>


## 贈品券使用規則

### 庫存檢查順序

當訂單成立時，系統會依以下順序檢查庫存，若贈品券商品庫存不足，系統將提示消費者刪除該券後再結帳：

1. 組合品
2. 一般商品
3. 首購禮商品
4. 滿額/件贈商品
5. **贈品券商品**

### 數據分析

贈品券屬於優惠券的一種，其成效可於後台 **圖表分析 > 行銷活動分析 > 優惠券分析** 中查看。若是由會員列表發送的贈品券，系統將視為「會員專屬優惠券」。

### 特殊情境處理

1. **套用失效**：若在套用贈品券後發生「重整購物車」、「更新購物車商品」或「贈品庫存不足」等情況，可能導致贈品券無法套用或顯示錯誤。此時消費者需刪除該券後重新結帳。
2. **最低消費限制**：即使贈品券門檻設為 0 元，購物車內仍須包含至少一個一般商品（非贈品）。若購物車為空，消費者將被導回首頁或會員頁面。
3. **門檻與庫存判定順序**：若同時觸發「未達消費門檻」與「贈品庫存不足」，系統會優先判斷消費門檻。

## 結帳流程

1. 消費者在結帳頁點擊「選擇優惠券或輸入優惠碼」。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定03.png){ .screenshot }

2. 若「全館優惠碼」與「個人優惠券」序號相同，系統優先套用 **個人優惠券**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼08.png){ .screenshot }

3. 若贈品庫存足夠，消費者可選擇套用該贈品券。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼09.png){ .screenshot }


## 常見問題

??? quote "為什麼我的贈品券無法套用？"
    請檢查以下幾點：
    1. 贈品商品是否有庫存。
    2. 贈品商品是否已填寫 SKU（針對串倉商家）。
    3. 購物車內是否已有其他商品（購物車不能僅有贈品）。