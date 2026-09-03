---
title: CHAT BOX AI 建議回覆
description: 透過 AI 助手自動學習您的品牌政策與商品資訊，為顧客諮詢提供即時、精準的回覆建議。
created: 2026-05-28 12:10
last_modified: 2026-05-28 12:08
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
cyb_extensions:
  - CHAT BOX
intents:
  - 啟用_AI_客服助手
  - 建立客服知識庫
  - AI_自動回覆建議
  - 提升客服效率
features:
  - CHAT BOX
  - AI 建議回覆
  - 知識庫管理
prerequisites:
  - ec/app-market/chatbox/
related: []
tags:
  - AI
  - 客服助手
  - 自動回覆
  - CHAT BOX
  - 知識庫
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - AI 中心
  - 上傳文件
  - AI 建議回覆按鈕
paths:
  - APP MARKET > CHAT BOX
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12968
  - https://www.cyberbiz.io/support/?p=53089
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/chat-box-ai-suggested-replies/"
comments: false
search:
  exclude: false
icon: lucide/bot
hide: []
---

# CHAT BOX AI 建議回覆
透過 AI 助手自動學習您的品牌政策與商品資訊，為顧客諮詢提供即時、精準的回覆建議。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業<br>
[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | CYBERBIZ CHAT BOX
{ .doc-badge }


!!! tip "應用情境"
    - **加速常見問題回覆**：將退換貨政策、運費說明上傳至資料庫，AI 即可自動擬稿，無需手動輸入重複內容。
    - **精準商品推薦**：AI 學習商品指南後，能根據顧客需求提供準確的規格說明或選購建議。
    - **維持服務品質**：即使是新進客服人員，也能透過 AI 建議產出符合品牌語調且資訊正確的回覆。


## 使用須知

- **資料品質決定回覆品質**：上傳的文件描述越詳細（如：常見問題集、內部 SOP），AI 生成的內容就越精準。
- **隱私與安全**：關閉功能或刪除檔案後，系統會立即從 AI 模型中移除對應資料，確保商業資訊安全。
- **人工審核原則**：AI 產出的內容僅供參考，發送前請務必進行人工微調與核實。


## 建立 AI 助手

前往 **APP MARKET > CHAT BOX**，點擊介面上的 **AI 中心** 進行設定。

### 1. 啟用功能

開啟「啟用 AI 建議回覆」開關。啟用後，每當接收到新訊息，聊天室對話框上方將出現 AI 觸發圖示。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-AI助手01.png){ .screenshot }

### 2. 建立客服資料庫

點擊 **上傳文件**，將您的品牌政策或產品說明書上傳至 AI 知識庫。

- **支援格式與限制**：
    - **TXT**：單一檔案上限 1 MB。
    - **PDF**：單一檔案上限 5 MB。
- **數量上限**：最多可上傳 20 個檔案。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-AI助手02.png){ .screenshot }

### 3. 追蹤檔案處理狀態

上傳後，AI 需時間閱讀並寫入模型。請留意檔案狀態：

- **處理中**：AI 正在學習內容，暫時無法點擊。
- **處理完成**：檔名變為藍色連結，代表已成功寫入，可點擊查看內容。
- **處理錯誤**：若檔案損毀或格式不符，請刪除後重新上傳。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-AI助手05.png){ .screenshot }



## 使用 AI 助手回覆問題

當顧客進線諮詢時，您可以透過以下步驟使用 AI 助手：

1. **觸發 AI 建議**：點擊對話框中的 AI 圖示，AI 會自動讀取對話紀錄並提取核心問題。
2. **生成草稿**：系統將即時產出一則回覆草稿。
3. **資訊核實**：若建議內容參考了特定資料來源（如前台商品頁），可點擊圖示跳轉核實。
4. **人工微調**：點擊編輯圖示，直接針對 AI 產出的文字進行修訂。
5. **發送訊息**：確認內容無誤後，點擊發送按鈕完成回覆。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-AI助手04.png){ .screenshot }



