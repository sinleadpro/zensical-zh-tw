---
title: 大量填補商品 SKU
description: 了解如何透過 Excel 批次匯出與匯入功能，快速為現有商品補齊 SKU 碼，以利開通 POS 功能與進行精準的庫存管理。
created: 2026-06-24 17:25
last_modified: 2026-06-24 17:25
lang: zh-TW
type: guide
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
  - 批次更新商品 SKU
  - 補齊 POS 商品 SKU
  - 大量編輯商品資訊
features: 
  - Excel 大量匯入
  - SKU 管理
  - POS 串接
prerequisites: 
  - "[[所有商品-新增商品]]"
related: 
  - "[[EXCEL大量匯入商品]]"
  - "[[建立 POS 商品]]"
tags: 
  - SKU
  - 批次更新
  - Excel 匯入
  - POS
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 所有商品列表
  - Excel 大量匯入商品
paths: 
  - 商品 > 所有商品
  - 商品 > Excel 大量匯入商品
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=3296
permalink: "https://help.cyberbiz.io/pos/get-started/bulk-update-product-skus/"
search:
  exclude: false
icon: lucide/file-spreadsheet
hide: []
---

# 大量填補商品 SKU
了解如何透過 Excel 批次匯出與匯入功能，快速為現有商品補齊 SKU 碼，以利開通 POS 功能與進行精準的庫存管理。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 智能 POS
{ .doc-badge }

## 使用須知

- **POS 開通限制**：商品必須具備 SKU 碼方可開通並使用 POS 系統功能。
- **SKU 唯一性**：每個商品款式應具備唯一的 SKU 碼，避免庫存計算混淆。
- **覆蓋邏輯**：從商品列表匯出的檔案包含「商品 ID」與「款式 ID」。修改此類檔案並匯入時，系統會 **覆蓋** 原有的商品資訊，而非新增商品。
- **備份建議**：在進行大量匯入前，建議先保留原始匯出的 Excel 檔案，以便在操作失誤時進行還原。



## 操作流程

### 步驟一：匯出現有商品資料

取得包含商品 ID 的完整清單。

1. 登入 CYBERBIZ 管理後台，前往 **商品 > 所有商品**。
2. 勾選欲更新的商品，或點選列表上方的 **全選** 勾選所有商品。
3. 點擊 **Select** 下拉選單，選擇 **匯出商品**。
4. 系統將自動產生商品清單 Excel 檔，並發送至您的管理員登入信箱。

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學1.png){ .screenshot }

### 步驟二：在 Excel 中填補 SKU

利用 Excel 的篩選功能快速定位缺失資料。

1. 至電子信箱下載並開啟商品 Excel 檔案。
2. 找到 **商品款式 SKU碼** 欄位。
3. 使用 Excel 的 **篩選** 功能，僅勾選 **(空格)** 項目，即可列出所有未填寫 SKU 的商品。
4. 填入正確的 SKU 碼後，取消篩選並儲存檔案。

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學4.png){ .screenshot }

### 步驟三：匯入更新檔案

將修改後的資料上傳回系統。

1. 回到管理後台，前往 **商品 > Excel 大量匯入商品**。
2. 點擊 **上傳檔案**，選擇剛才儲存的 Excel 檔案。
3. 點擊 **確定上傳**。系統將開始排程處理更新。

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學5.png){ .screenshot }

### 步驟四：確認更新結果

系統將透過 Email 通知處理進度。

- **失敗**：系統將提示失敗原因，請更正後重新上傳。
- **成功**：請稍待完成信件，未完成重複上傳將導致資訊混亂，請務必耐心等候。
- **完成**：匯入已確認完成，可查看更新成果或再次更新其他內容。

確認 SKU 補齊後，**即可聯繫線上客服或 LINE@ 專員** 協助申請開通 POS 功能。

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學6.png){ .screenshot }

## 更多操作

<div class="grid cards" markdown>

- :lucide-arrow-right:{ .lg }   
  [__判斷 Excel 上傳商品是新增還是更新__](../../ec/products/bulk-operations/Excel%20大量匯入商品/#判斷-excel-上傳商品是新增還是更新)       
  認識「新增商品」與「覆蓋既有商品」差異。

</div>