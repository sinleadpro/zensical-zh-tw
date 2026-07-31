---
title: 建立 POS 商品
description: 了解如何將 EC 網站商品同步至 POS 商店，或為 POS 獨賣商店建立專屬商品，實現全通路庫存管理。
created: 2026-06-24 16:50
last_modified: 2026-06-24 16:50
lang: zh-TW
type: tutorial
status: update
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
  - POS
modules: 
  - 商品
  - POS 功能
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents: 
  - 同步 EC 商品至 POS
  - 建立 POS 獨賣商品
  - 管理 POS 門市商品
features: 
  - POS 商品同步
  - POS 獨賣商品
  - 庫存管理
prerequisites: 
  - "所有商品-新增商品"
related: 
  - "EXCEL大量匯入商品"
tags: 
  - POS
  - 商品建立
  - 同步
  - 門市管理
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 所有商品列表
  - 複製商品至 POS 商店
paths: 
  - 商品 > 所有商品
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=5138
permalink: "https://help.cyberbiz.io/pos/get-started/create-pos-products/"
search:
  exclude: false
icon: lucide/package-plus
hide: []
---

# 建立 POS 商品
了解如何將 EC 網站商品同步至 POS 商店，或為 POS 獨賣商店建立專屬商品，實現全通路庫存管理。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 智能 POS
{ .doc-badge }


## 使用須知

- **圖片重要性**：POS 商品圖片會直接顯示在 POS 前台操作畫面，協助店員快速辨識商品。建議在複製時開啟 **連帶複製商品所有圖片**。


## 操作流程

### 在 EC 後台建立商品

1. 建置POS門市商品的第一步，建議優先在 **EC 管理後台** 建立商品，再複製到 POS 商店，確保流程順暢與資訊完整。

    !!! tip "小建議"
        商品管理以EC網站為主作編輯，POS店主要作庫存管理使用。

2. EC網站商品建置方式，建議參考 [新增與更新商品](../../ec/products/create-and-manage/create-update-products/)。
3. 單筆建置熟悉後，若欲批次建置商品，建議參考 [Excel 大量匯入商品](../../ec/products/bulk-operations/excel-import-products/)。

### 複製 EC 商品至 POS 商店

將官網現有商品同步至指定門市。

1. 登入 CYBERBIZ 管理後台，前往 **商品 > 所有商品**，勾選欲同步的商品（可勾選「全選」進行批次操作）。
2. 點選 **複製商品至 POS 商店**。
3. 在彈窗中完成以下設定：
    - **選擇門市**：勾選欲複製到的 POS 門市（可複選）。
    - **複製圖片**：建議開啟 **連帶複製商品所有圖片**。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品建立1.png){ .screenshot }


### POS 獨賣商家建立商品

針對僅購買 POS 系統的商家，可在 **建立商品時直接指定門市**。

1. 前往 **商品 > 所有商品**，點擊 **新增商品**。
2. 在商品編輯頁面中，找到 **POS 商店設定** 區塊。
3. 勾選該商品要套用販售的 **POS 門市**。
4. 完成商品其他資訊填寫後，點擊 **儲存**。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-所有商品-POS獨賣商家建立商品時同步POS商店01.png){ .screenshot }

!!! warning "限制說明"
    - **不溯及既往**：此同步設定僅限 **新建立商品時** 使用。已建立的商品請使用上述「複製商品至 POS 商店」方式新增至門市。
    - **方案限制**：此功能僅限 POS 獨賣商家使用。若您同時使用 EC 與 POS，請統一使用複製功能以確保資料一致性。


