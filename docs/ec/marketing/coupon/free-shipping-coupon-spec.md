---
title: 免運券規格
description: 說明 CYBERBIZ 免運券的規格、建立方式及結帳流程。
created: 2026-06-17 10:39
last_modified: 2026-06-17 10:39
lang: zh-TW
type: reference
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
tnb: branch
plans: 
    - 專業 PLUS
    - 進階 PLUS
    - 高手 PLUS
    - 企業
cyb_extensions: []
intents: 
    - 瞭解免運券規格
    - 設定免運券
    - 處理免運券結帳問題
features: 
    - 免運券
    - 優惠券
    - 紅利商城
prerequisites: 
    - [[setup-coupons]]
    - [[setup-promo-codes]]
related: 
    - [[setup-coupons]]
    - [[setup-promo-codes]]
    - [[multiple-coupons]]
tags: 
    - 免運券
    - 優惠券
    - 行銷活動
    - 運費折抵
acoiv: configure
apis: []
devices: 
    - desktop
    - mobile
ui_components: 
    - 結帳頁面
    - 優惠券輸入框
paths: 
    - 行銷活動 > 優惠券
layouts: []
wp_url: 
    - https://www.cyberbiz.io/support/?p=28947
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---
# 免運券規格
說明 CYBERBIZ 免運券的規格、建立方式及結帳流程。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有PLUS / 企業
{ .doc-badge }

## 使用須知

- **編輯限制**：免運券設定完成後即無法編輯。若需更新內容，必須刪除並重新新增。
- **紅利商城適用性**：紅利商城若使用免運券，將不受該券的「消費使用門檻」限制，皆可直接折抵運費。

## 建立贈品券

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__會員列表發送優惠券__](../../members/manage-member-profiles.md#2-優惠券派發與管理)
    使用會員篩選器批次發送優惠券。

- :lucide-hash:{ .lg }
    [__建立贈品優惠碼__](setup-promo-codes.md)
    建立不歸戶全館優惠碼，會員於結帳時輸入優惠碼後可免運。


</div>


## 結帳流程

1. 消費者在結帳頁點擊「選擇優惠券或輸入優惠碼」。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定03.png){ .screenshot }

2. 若「全館優惠碼」與「個人優惠券」序號相同，系統優先套用 **個人優惠券**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼08.png){ .screenshot }

3. 未使用免運券前，系統顯示原始運費。

    - 選擇或輸入免運券代碼。
    - 套用後，運費欄位將更新為 **（優惠券免運）**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/免運券05.png){ .screenshot }

