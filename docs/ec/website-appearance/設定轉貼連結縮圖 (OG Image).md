---
title: 設定轉貼連結縮圖 (OG Image)
version: ""
last_modified: 2026-02-28
description: ""
product:
  - EC
modules: []
activ: ""
paths: []
surfaces: []
ends: []
devices:
  - desktop
  - mobile
apis: []
type: tutorial
intents: []
features: []
tnb: ""
plans: []
prerequisites: []
lang: zh-TW
sites: []
status:
tags: []
difficulty: ""
audiences: []
wp_url: []
notes: []
comments: ""
search:
  exclude: ""
icon: ""
---

{ .subtitle }

{ .doc-badge }

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
- **操作步驟**：切換至 **群組描述** 頁籤，上傳圖片並儲存。這張圖片會同時作為群組頁的視覺圖以及轉貼時的縮圖。



### 部落格文章
    
- **設定路徑**：「網站外觀」>「部落格管理(文章/分類)」> 選擇文章。
- **操作步驟**：在文章設定中選擇圖片，此圖片會影響前台部落格主題封面以及分享連結時的縮圖。

### 其他網站頁面 / 全站通用設定
    
- **設定路徑**：
	- **一般版型**：「網站外觀」>「套版主題管理」>「網站設定」>「細部設定(首頁設定)」>「轉貼連結預設圖片(OG image)」。
	- **拖拉版型**：「網站外觀」>「套版主題管理」>「網站設定」>「全站設定」>「圖示設定」中的「轉貼分享圖片 OG image」。
- **功能**：若分享的頁面不屬於上述商品、群組或文章（例如首頁、分頁），則會顯示此處設定的通用縮圖。

## 分享連結時縮圖無法即時更新的解決方案

當您更新了網頁圖片，但在 Facebook 或 LINE 上分享時仍顯示舊資訊，這是因為平台會暫存（Cache）一份舊的快取紀錄。

### 手動更新 Facebook 連結資訊步驟

1. 確保網頁上的新圖片已更新完成。
2. 開啟 **[Facebook 分享偵錯工具](https://developers.facebook.com/tools/debug/)**，貼入欲更新的連結後點選「偵錯」。
3. 若畫面仍顯示舊資訊，請點擊 **「再次抓取」** 按鈕，強制 Facebook 重新讀取網頁資料。
4. 更新成功後，再次於 Facebook 發布連結即可看到正確的縮圖與資訊。

### 手動更新 LINE 連結資訊

- 可使用 LINE 官方提供的 **[LINE Page Poker](https://poker.line.biz/)** 工具，輸入網址並點選「Clear」來清除快取紀錄。

您是否需要我協助您確認目前使用的版型，以提供更精確的「全站設定」路徑說明？

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