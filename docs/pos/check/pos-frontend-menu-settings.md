---
title: POS 前台選單設定
description: 說明如何設定 POS 前台的圖形化商品選單，透過多層級分類提升店員結帳效率，特別適用於無條碼商品（如食品、散裝品）。
created: 2026-06-01 16:22
last_modified: 2026-06-01 16:22
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: 
  - 內部連結
ga_views: 0
feedback: 0
products: 
  - POS
modules: 
  - POS 前台
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: branch
plans:
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents: 
  - 設定 POS 前台選單
  - 建立商品多層級分類
  - 提升 POS 結帳效率
features: 
  - POS 選單
  - 商品多層級分類
  - 圖形化介面
prerequisites: 
  - "建議先完成「自訂群組」或「商品類型」設定"
related: []
tags: 
  - POS
  - 商品選單
  - 多層級分類
  - 結帳優化
acoiv: configure
apis: []
devices: 
  - tablet
  - desktop
ui_components: 
  - POS 選單設定
  - 商品多層級分類
paths: 
  - 商品 > 商品多層級分類
  - POS 功能 > 所有 POS 商店
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=11224
permalink:
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# POS 前台選單設定
透過 POS 前台的圖形化選單，店員可以快速點選商品加入購物車，無需逐一掃描條碼。此功能特別適用於食品、散裝商品，或使用平板進行流動結帳的場景。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 智能 POS
{ .doc-badge }

!!! tip "應用情境"
    - **無條碼商品**：如麵包、蛋糕、散裝蔬果等無法貼標的商品。
    - **快速結帳**：針對熱銷商品建立捷徑選單，縮短店員搜尋時間。
    - **平板操作**：在流動攤位或展場使用平板結帳時，圖形化介面更直觀。


## 使用須知

- **前置作業**：建議先完成 **[自訂群組](../../ec/products/categories-and-tags/custom-collections.md)** 或 **[商品類型](../../ec/products/create-and-manage/edit-product-description-settings.md#商品設定)** 的設定，以便在建立選單時直接連結。
- **圖片規範**：
    - 建議尺寸：`80 x 80 px`。
    - 檔案大小：請勿超過 `2 MB`。
- **選單架構**：系統支援三層式架構（大類別 > 中分類 > 商品項目）。


## 步驟一：建立商品多層級分類

在設定 POS 選單前，需先定義商品的分類邏輯。


1. 登入 CYBERBIZ 管理後台，前往 **商品 > 商品多層級分類**。
2. 點選 **POS 設定** 頁籤。
3. 點擊 **新增類別/分類**：此為選單的第一層（大類別，如：蛋糕、飲品）。
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單2.png){ .screenshot }
4. **新增第二層分類**：
    - 點擊第一層分類旁的 **+** 號。
    - 選擇連結方式：可連結至已建立的 **自訂群組** 或 **商品類型**。
    - 編輯分類名稱並上傳代表圖片。
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單3.png){ .screenshot }



## 步驟二：啟用並配置 POS 選單

完成分類定義後，需將其加入 POS 前台選單並排序。


1. 登入 CYBERBIZ 管理後台，前往 **POS 功能 > 所有 POS 商店**。
1. 前往指定門市，點選 **商品選單設定** 頁籤。
2. 開啟 **啟用功能** 開關。
3. 點擊 **新增分類**，勾選您在步驟一建立好的多層級分類。
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單4.png){ .screenshot }
4. **調整排序與移除**：
    - 拖過拖曳圖示可調整選單在前台顯示的先後順序。
    - 若不再需要顯示，可點擊垃圾桶圖示移除。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單5.png){ .screenshot }


## 前台成果展示

設定完成後，店員在 POS 前台即可看到如下圖的選單結構：

1. **第一層**：大類別（如：蛋糕）。
2. **第二層**：中分類（如：長條蛋糕）。
3. **第三層**：具體商品項目（點擊即可加入購物車）。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單1.png){ .screenshot }

