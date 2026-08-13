---
title: 匯入顧客門市推薦人
description: 總部管理員可透過批次匯入功能，快速為現有會員綁定指定門市與店員，確保業績精準歸因。
created: 2026-05-07 18:35
last_modified: 2026-06-18 18:35
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
  - APP MARKET
  - 門市助理
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents:
  - 批量綁定門市推薦人
  - 更換會員推薦人
  - 批次刪除綁定關係
features:
  - 門市助理
  - 批量匯入
  - 推薦人綁定
  - 業績歸因
prerequisites: []
related: []
tags:
  - 門市助理
  - 批量匯入
  - 推薦人綁定
  - 業績歸因
acoiv: configure
apis: []
devices: []
ui_components:
  - 匯入
  - 上傳檔案
  - 錯誤明細
paths:
  - 門市助理後台 > 門市管理 > 匯入 > 顧客門市推薦人
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=3865
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/bulk-import-customer-referrers/"
comments: false
search:
  exclude: false
icon: lucide/file-up
hide: []
---

# 匯入顧客門市推薦人
總部管理員可透過批次匯入功能，快速為現有會員綁定指定門市與店員，確保業績精準歸因。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | 門市助理
{ .doc-badge }


## 功能說明

總部管理員可透過此功能批次設定會員與門市推薦人之相關設定，包括 **更換門市推薦人** 與 **綁定期間**，以及 **刪除綁定關係**。


## 使用須知

-  **會員身份限制**：系統僅支援對 **已在官網 (EC) 註冊** 的會員進行綁定。若顧客尚未成為會員，請先至 **會員 > 所有會員** 進行 [會員資料匯入]()。
-  **LINE 官方帳號關聯**：透過後台批次綁定的會員 **不會** 自動加入 LINE 官方帳號好友。建議引導會員後續於門市再次掃描店員專屬 QRcode 以完成 LINE 連結。
-  **業績計算**：有綁定匯入顧客門市推薦人的訂單資訊將呈現於 **業績歸因報表**。
- **功能權限**：僅限 **總部管理員** 於門市助理管理後台操作。


## 操作流程

### 上傳與執行匯入

1. 登入門市助理管理後台，前往 **門市管理**，點擊頂端選單 **匯入 > 顧客門市推薦人**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人01.png){ .screenshot }
    
2. 點擊 **下載範本**，根據範本格式填寫會員手機、指定門市 ID、店員 ID 等資訊。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人02.png){ .screenshot }

    !!! info "使用限制"
        - 檔案格式限 `.xlsx`。
        - 單次上傳上限為 **3,000 筆**。
        - 必須使用系統提供的最新版範本。

3. 點擊 **上傳檔案**，選取填寫完成的 `.xlsx` 檔。
4. 系統將開始執行匯入，您可以在下方的 **上傳作業進度** 區域即時查看狀態。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人03.png){ .screenshot }

### 確認進度與錯誤排除

1. **成功完成**：狀態顯示為 **已完成** 後，綁定關係將即時生效。
2. **錯誤處理**：
    - 若狀態顯示為 **失敗** 或 **部分成功**，請點擊右側的 **錯誤明細**。
    - 根據提示（如：格式錯誤、查無此會員、門市 ID 不存在）修改原始檔案。
    - **修正後需整檔重新上傳**。在上傳成功完成前，資料不會有任何更新。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人04.png){ .small-image }


## 常見問題

??? quote "匯入後，之前的舊訂單會自動歸因到新綁定的推薦人嗎？"
    不會。業績歸因僅適用於 **綁定關係建立後** 產生的官網有效訂單。已結案或已產生的歷史訂單不會溯及既往。

??? quote "如果我想刪除某個會員的綁定關係，也可以用匯入的嗎？"
    可以。在匯入範本中，您可以透過特定的指令欄位（依範本說明）設定刪除或解除綁定關係，再次執行上傳即可完成批量更新。

