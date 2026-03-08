---
title: 設定轉貼連結縮圖 (OG Image)
description: 於商品、分類、文章或全站設定中指定 Open Graph（OG）分享圖片，控制社群平台轉貼連結時顯示的縮圖與預覽資訊。
created: 2025-03-03
last_modified: 2026-03-05 12:15
lang: zh-TW
type: tutorial
status: ""
version: ""
author: Jase
reviewers: []
notes:
  - verify 一般版型 og image 設定路徑
  - inform 商品自訂分類群組圖片上傳 編輯器 URL 遺失問題
  - verify faq test weight
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
  - 商品
sites: []
audiences:
  - admin
difficulty: beginner
tnb: trunk
plans:
  - 專業
  - 進階
  - 高手
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents:
  - 設定社群分享縮圖
  - 自訂商品轉貼圖片
  - 解決 Facebook 縮圖不更新問題
  - 優化 LINE 分享預覽
  - 更新全站 OG Image
  - 修正部落格文章分享圖
features:
  - OG Image
  - 商品圖片
  - 部落格文章縮圖
  - 商品群組縮圖
  - 全站縮圖
  - 社群分享快取解決方案
prerequisites: []
related: []
tags:
  - OG Image
  - 社群分享
  - 縮圖設定
  - Facebook
  - LINE
  - 快取更新
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3843
  - https://www.cyberbiz.io/support/?p=19718
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/image-plus
hide:
---

於商品、分類、文章或全站設定中指定 Open Graph（OG）分享圖片，控制社群平台轉貼連結時顯示的縮圖與預覽資訊。
{ .subtitle }

![](../../../assets/images/ec-網站外觀-og-image.png){ .hero-page }

## 轉貼連結預設圖片說明

**轉貼連結預設圖片（OG Image）** 是指當您將網站連結貼到 Facebook 或 LINE 等平台時，系統自動抓取並顯示的縮圖。妥善設定 OG image 能提升品牌專業度，增加客戶點擊連結的意願。

以下是針對不同頁面類型的設定教學：

## 各頁面類型縮圖設定方式

### 商品頁

- **設定路徑**：登入 CYBERBIZ 管理後台，前往 **商品 > 所有商品**，點擊欲設定商品名稱，進入商品編輯頁面。
- **操作步驟**：切換至 **商品資訊** 頁籤，在 **商品圖片** 區塊上傳連結預設圖片。
- **自動設定**：系統會自動將該商品的 **第一張商品圖片** 設為轉貼連結的縮圖。

![](../../../assets/images/ec-商品-商品編輯頁-商品圖片-第一張.gif)

---

### 商品群組頁（自訂分類）
    
- **設定路徑**：登入 CYBERBIZ 管理後台，前往 **商品 > 商品自訂分類 >** 點選欲設定群組的 **編輯 :lucide-square-pen:** 按鈕 。
- **操作步驟**：
	- 切換至 **群組描述** 頁籤，上傳圖片。
	- 切換至 **影像資訊** 頁籤，點擊 **瀏覽伺服器**，選擇所上傳的圖片。
	- 點擊 **儲存** 套用變更。這張圖片會同時作為群組頁的視覺圖以及轉貼時的縮圖。

![](../../../assets/images/ec-網站外觀-商品自訂分類-群組圖片.gif)

---

### 部落格文章
    
- **設定路徑**：登入 CYBERBIZ 管理後台，前往 **網站外觀 > 部落格管理(文章/分類) > 選擇文章**。
- **操作步驟**：在文章設定中選擇圖片，此圖片會影響前台部落格主題封面以及分享連結時的縮圖。

![](../../../assets/images/ec-網站外觀-部落格文章圖片.gif)

---

### 其他網站頁面 / 全站通用設定
    
- **設定路徑**：

	<!--
	- **一般版型**：「網站外觀」>「套版主題管理」>「網站設定」>「細部設定(首頁設定)」>「轉貼連結預設圖片(OG image)」。
	-->
	
	- **拖拉版型**：登入 CYBERBIZ 管理後台，前往 **網站外觀 > 套版主題管理 > 網站設定 > 全站設定 >「圖示設定」中的「轉貼分享圖片 OG image**。
	- 
- **功能**：若分享的頁面不屬於上述商品、群組或文章（例如首頁、分頁），則會顯示此處設定的通用縮圖。

![](../../../assets/images/ec-網站外觀-全站設定-og-image.png)

## 分享連結時縮圖無法即時更新的解決方案

當您更新了網頁圖片，但在 Facebook 或 LINE 上分享時仍顯示舊資訊，這是因為平台會暫存（Cache）一份舊的快取紀錄。

### 手動更新 Facebook 連結資訊步驟

1. 確保網頁上的新圖片已更新完成。
2. 開啟 **[Facebook 分享偵錯工具 :lucide-external-link:](https://developers.facebook.com/tools/debug/)**，貼入欲更新的連結後點選「偵錯」。
3. 若畫面仍顯示舊資訊，請點擊 **「再次抓取」** 按鈕，強制 Facebook 重新讀取網頁資料。
4. 更新成功後，再次於 Facebook 發布連結即可看到正確的縮圖與資訊。

![](../../../assets/images/ec-fb-share-debugger-再次抓取.png)

<!--

### 手動更新 LINE 連結資訊

- 可使用 LINE 官方提供的 **[LINE Page Poker](https://poker.line.biz/)** 工具，輸入網址並點選「Clear」來清除快取紀錄。

-->

## 常見問題

??? quote "為什麼我上傳了圖片，但在 LINE 或 Facebook 分享時還是看不到縮圖？"

	這通常有兩個原因：

	1. **快取問題**：社群平台會暫存舊的資料。請參考本文件 [分享連結時縮圖無法即時更新的解決方案](#分享連結時縮圖無法即時更新的解決方案) 使用偵錯工具強制更新。
	
	2. **圖片尺寸不符**：若圖片檔案過大（超過 8MB）或解析度過低，平台可能會抓取失敗。建議使用建議規格。

??? quote "推薦的 OG Image 圖片尺寸是多少？"

	為了確保在各社群平台（FB、LINE、Instagram）都能完美呈現不被裁切，建議規格如下：

	- **建議尺寸**：300 x 300 像素 (px)。
	
	- **比例**：1:1。
	
	- **檔案格式**：JPG、PNG 或 GIF。
	
	- **檔案大小**：建議控制在 **1MB** 以內，以利平台快速抓取。

??? quote "如果我沒有設定商品的 OG Image，系統會顯示什麼？"

	系統會依照以下優先順序抓取：
	
	1. 該商品的 **第一張商品圖片**。
	
	2. 若商品無圖片，則抓取 **[全站通用設定](#其他網站頁面--全站通用設定)** 中上傳的 OG Image。
	
	3. 若全站皆未設定，則由社群平台隨機抓取頁面中的圖片（通常效果較不理想，建議至少完成全站設定）。

??? quote "為什麼商品群組（自訂分類）的圖片在編輯器中失效了？"

	若您在編輯「群組描述」時發現 URL 遺失或圖片無法正常顯示，請確認：
	
	* 圖片是否已先透過「影像資訊」頁籤成功上傳至伺服器。
	
	* 避免直接從外部網站貼上圖片連結，建議一律點選 **瀏覽伺服器** 選擇站內檔案，以確保連結穩定性。

??? quote "更新了全站 OG Image，首頁的縮圖還是舊的怎麼辦？"

	首頁的權重最高，快取也最頑固。除了使用 Facebook 偵錯工具外，建議可以嘗試在網址後方加上隨機參數（例如：`https://yourstore.com/?v=1`）進行測試，若帶參數的網址顯示正確，則代表純網址的快取尚待平台系統自動更新（通常需 24-48 小時）。