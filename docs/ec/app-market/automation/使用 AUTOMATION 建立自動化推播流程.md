---
title: 使用 AUTOMATION 建立自動化推播流程
description: ""
created: 2026-03-09 14:48
last_modified:
lang: ""
type: tutorial
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: branch
plans:
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions:
  - AUTOMATION
intents: []
features: []
prerequisites: []
related: []
tags: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/zap
hide:
aliases: []
id: 使用 AUTOMATION 建立自動化推播流程
---

# 使用 AUTOMATION 建立自動化推播流程


{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 專業 PLUS / 進階 PLUS / 高手 PLUS / 企業  
[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | AUTOMATION
{ .doc-badge }

{ .hero-page }

**CYBERBIZ AUTOMATION** 是專為商家設計的自動化流程工具，能簡化行銷與營運設定，提高經營效率。

以下為 AUTOMATION 發送簡訊、EDM 及 LINE OA 訊息的詳細教學：

## 前置作業：自訂會員篩選分群

在建立自動化流程前，需先定義受眾對象。系統僅會推播給**勾選訂閱電子報/商家優惠**的會員。
1.  **後台路徑**：「會員」→「所有會員」。
2.  **設定條件**：點選「新增篩選條件」或使用「範本」（如：忠誠、沉睡或購物車未結帳會員）。
3.  **儲存分群**：確認名單後點擊「儲存」，設定分群名稱與描述。若篩選內容包含 LINE 登入或綁定，可勾選同步上傳受眾至 LINE 後台。

## AUTOMATION 操作流程 (簡訊/EDM/LINE OA)
進入設定介面的路徑為：「**APP MARKET**」→「**我的擴充服務**」→「**CYBERBIZ AUTOMATION**」。

### 簡訊發送設定

*   **建立流程**：點擊「建立流程」，選擇預設分眾流程（如：發送簡訊給 VIP 或沉睡客戶）。
*   **內容編輯**：
    *   **排程觸發**：可設定為「一次」或「週期」（如：每週發送一次）。
    *   **會員篩選**：選擇預先設定好的會員分群。
    *   **簡訊內容**：輸入文字，連結務必使用 **CYBERBIZ 站內網址**以利追蹤成效，並點擊「預覽簡訊」確認字數（上限 70 字）。
*   **重複發送設定**：可選擇「允許」、「不允許」或「指定天數內不重複」發送給相同對象。

### EDM 發送設定

*   **必要前提**：必須先完成 EDM 基礎設定。
*   **操作步驟**：
    1.  選擇 EDM 預設模板（如：發送 EDM 給 VIP 或自訂分群）。
    2.  設定排程與會員篩選。
    3.  **EDM 發送元件**：挑選已編輯好的 EDM 樣板，並完成重複發送設定。

### LINE OA 訊息發送設定

*   **必要條件**：會員需完成 **LINE 登入或綁定**，且必須是 **LINE OA 好友**，商家需確保 LINE OA 訊息額度充足。
*   **操作步驟**：
    1.  選擇 LINE OA 預設模板（如：未結帳購物車提醒）。
    2.  **訊息模組**：可選擇「圖片」或「文字」，一次最多可發送 **3 組**。
    3.  **網址追蹤**：同樣建議使用站內網址以進行成效分析。

## 流程啟用與追蹤

1.  **開始流程**：設定完成後點擊「開始流程」，系統會提示預計花費的 CYBER 幣或發送人數。
2.  **狀態監控**：
    *   **草稿 (Draft)**：可隨時編輯或刪除。
    *   **已排程/執行中**：若要修改，需點選「暫停流程」。
    *   **已完成/執行失敗**：發送後系統會將紀錄傳送至設定的「通知信箱」（上限 10 人）。
3.  **成效追蹤**：可在流程介面點選「成效追蹤」或「查看流程紀錄」，數據約於 **12 小時內更新**。


## 後續操作

<div class="grid cards" markdown>

- :lucide-import:{ .lg }   
  [____]()     
  。

- :lucide-ban:{ .lg }     
  [____]()  
  。

</div>

## 常見問題

??? quote ""

