---
title: 在自訂頁面中嵌入 Google 表單
description: 將 Google 表單嵌入 CYBERBIZ 自訂頁面，並針對手機版進行響應式寬度與高度優化。
created: 2024-05-23
last_modified: 2026-03-05 14:51
lang: zh-TW
permalink: ""
type: tutorial
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
sites:
  - TW
tnb: trunk
plans:
  - 專業
  - 進階
  - 高手
  - 企業
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 嵌入 Google 表單至自訂頁面
  - 優化表單行動版顯示比例
  - 調整嵌入表單的顯示高度
  - 解決 Google 表單權限存取問題
features:
  - 自訂頁面
  - 自訂 HTML 區塊
  - Google 表單嵌入
prerequisites:
  - 已製作完成的 Google 表單
related: []
tags:
  - Google表單
  - 嵌入代碼
  - 響應式設計
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 網站外觀 > 自訂頁面管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3688
  - https://www.cyberbiz.io/support/?p=18247
comments: false
search:
  exclude: false
icon: ""
---

將 Google 表單嵌入 CYBERBIZ 自訂頁面，並針對手機版進行響應式寬度與高度優化。
{ .subtitle }

![](../../../assets/images/ec-網站外觀-自訂頁面-嵌入google表單.png){ .hero-page }

## 嵌入 Google 表單說明

透過在 CYBERBIZ 頁面中崁入 Google 表單，商家可以輕鬆達成 **預約、諮詢、問卷調查或保固登記** 等功能，讓客戶直接在網頁上完成回覆。

以下為詳細的操作教學：

## 前置作業：取得表單代碼

1. 請至 Google 表單完成製作。
2. 按一下右上方的「更多」選單 :lucide-ellipsis-vertical: 
3. 切換至「崁入」分頁（圖示為 `< >`）。
4. 複製系統產生的 **HTML 崁入程式碼**。

![](../../../assets/images/google-forum-embed-html.png)

!!! note "詳細操作步驟，請參閱 [官方說明文件 :lucide-external-link:](https://support.google.com/docs/answer/2839588#zippy=%2C%E5%8F%96%E5%BE%97%E8%A1%A8%E5%96%AE%E9%80%A3%E7%B5%90%2C%E5%9C%A8%E7%B6%B2%E7%AB%99%E6%88%96%E7%B6%B2%E8%AA%8C%E4%B8%AD%E5%B5%8C%E5%85%A5%E8%A1%A8%E5%96%AE)。"

## 後台操作步驟

!!! warning "CYBERBIZ 提供程式碼修改權限，但不提供語法教學或代碼撰寫服務，建議由貴公司技術人員執行。"

1. **進入編輯頁面：** 登入 CYBERBIZ 管理後台，前往 **網站外觀 > 自訂頁面管理**，選擇欲加入表單的頁面。
2. **新增區塊：** 點擊 **新增區塊**，選擇 **自訂 HTML** 並點擊進入編輯頁面。
3. **貼入代碼：** 點擊 **編輯** 打開編輯器，將複製的 Google 表單程式碼貼入空白處。
4. **響應式優化（重要）：** 在貼上的程式碼中找到 `width` 屬性，將其數值（如 640）更改為 **`100%`**，這可以確保表單在手機與電腦版上都能自動適應螢幕寬度並完整顯示。
5. **儲存與預覽：** 完成後點擊儲存，即可在官網頁面上直接看到並填寫 Google 表單。

![](../../../assets/images/ec-網站外觀-自訂頁面-嵌入google表單.gif)


## 常見問題

??? quote "為何表單在手機版顯示時右側會被裁切？" 
	這通常是因為 `width`（寬度）被設定為固定的像素值（如 `width="640"`）。 
	
	**解決方法：** 請檢查嵌入代碼，將 `width` 的數值改為 `100%`。這樣表單就會根據使用者裝置的螢幕寬度自動縮放。

??? quote "嵌入後的表單高度太短，出現內部捲軸怎麼辦？" 
	Google 表單預設的嵌入高度可能不足以顯示完整問題。 
	
	**解決方法：** 在 HTML 代碼中找到 `height` 屬性，手動增加其數值（例如改為 `height="1200"` 或更高），直到表單內容能完整呈現而不產生內部捲軸。

??? quote "為什麼客戶反映看到「您需要權限」而無法填寫？" 
	這是因為 Google 表單的隱權設定限制了存取對象。 
	
	**解決方法：** 
	
	1. 回到 Google 表單編輯頁面。 
	2. 點擊「設定」分頁。 
	3. 在「回覆」區塊下，關閉 **「僅限限制 (您的組織名稱) 使用者」** 的選項。 
	4. 確保「限制每人僅能回覆 1 次」也是關閉狀態（除非您要求客戶必須登入 Google 帳號）。

??? quote "可以在表單提交後，自動導回我的官網特定頁面嗎？" 
	原生嵌入的 Google 表單不支持在提交後「自動跳轉」外部網址。 
	
	
	**替代方案：** 您可以在 Google 表單的「設定」>「呈現方式」>「確認訊息」中，貼上您的官網連結，引導填表者手動點擊返回。