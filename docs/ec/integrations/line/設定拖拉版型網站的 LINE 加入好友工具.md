---
title: 設定拖拉版型網站的 LINE 加入好友工具
version: ""
last_modified: 2026-02-24
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
lang: en-US
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

[:lucide-toggle-right:{ title="適用功能" }](../../resources/conventions#適用功能) | 拖拉版型
{ .doc-badge }

![](../../../assets/images/ec-第三方整合-line-官方加入好友工具.png){ .hero-page }

## 拖拉版型加入好友工具說明

商家可以透過多種內建功能，將 LINE OA 官方帳號的邀請資訊（如連結、QR Code、圖片等）呈現於官網中，以提升品牌與會員的黏著度。

以下為針對拖拉版型設定 LINE OA 增加好友工具的詳細教學：

## 前置準備：取得 LINE 好友連結

- [x] 請確保已自行設置好品牌官網的 LINE OA 帳號。
- [x] 在進行官網設定前，請先至 **LINE Official Account Manager** 取得宣傳素材：

	1. 登入 [**LINE Official Account Manager** :lucide-external-link:](https://manager.line.biz)，進入 **主頁 > 增加好友人數 > 增加好友工具**。
	2. 在此處您可以選擇 複製 **「網址」**、下載 **「行動條碼 (QR Code)」** 或複製 **「加入好友按鈕」** 的語法。

## 官網應用方式設定

### 右側彈窗廣告 (彈跳視窗)

這是最直接引導顧客加入好友的方式。

- **後台路徑**：前往 **網站外觀 > 套版主題管理 > 網站設定 > 彈窗廣告**。
- **設定步驟**：
    1. 新增一個圖片區塊。

		![](../../../assets/images/ec-網站外觀-彈窗廣告-圖片.gif)

    2. **上傳圖片**：建議在電腦/平板/手機版圖片中上傳「加入好友行動條碼」圖片或貼上 URL 連結。

		![](../../../assets/images/ec-網站外觀-彈窗廣告-圖片-line-oa-qrcode.gif)

    3. **縮圖設定**：商家可自行製作縮圖，並根據前台畫面調整縮圖大小。
    4. **圖片連結**：選擇外部連結，貼上從 LINE Official Account Manager [複製的「好友網址」](../../notifications/發送 LINE 加入好友邀請.md#get-line-oa-add-friend-link){ data-preview }。

		![](../../../assets/images/ec-網站外觀-彈窗廣告-圖片連結.png)

    5. **儲存設定**。
    
- **完成設定畫面**：

	![](../../../assets/images/ec-網站外觀-彈窗廣告-line 加入好友.gif)

---

### 輪播素材 (Banner)

利用首頁的大型橫幅廣告進行視覺推廣。

- **後台路徑**：前往「網站外觀」>「套版主題管理」>「網站設定」>**「輪播素材」**。
- **設定步驟**：
    1. 點選「新增區塊」並點擊編輯。
    2. **上傳圖片**：上傳設計好的 LINE 推廣圖（電腦版圖片為必傳）。
    3. **SEO 優化**：務必填寫「圖片替代文字」以優化搜尋引擎功能。
    4. **停留設定**：在「其他版面設定」中可 [調整素材停留秒數與邊距](../../website-appearance/拖拉版型網站設定#版面細節設定-其他版面設計)。

	![](../../../assets/images/ec-網站外觀-輪播素材-新增.gif)

- **完成設定畫面**：

	![](../../../assets/images/ec-網站外觀-輪播素材-前台畫面.gif)

!!! note "更多輪播素材相關設定，請參閱 [輪播素材設定說明](../../website-appearance/拖拉版型網站設定#輪播素材)。"

---

### 頁腳 ICON 設定 (Footer)

在網站底部固定放置 LINE 的社群圖示。

- **後台路徑**：前往「網站外觀」>「套版主題管理」>「網站設定」>**「頁腳」**。
- **設定步驟**：
    1. 點選「其他版面設計」。
    2. 找到 **「社群媒體設定」**，將 **LINE 開啟** 並貼上好友邀請連結。

![](../../../assets/images/ec-網站外觀-頁腳-line.gif)

---

### 選單/導覽列設定

將加入好友的功能直接放進網站的主選單中。

- **後台路徑**：前往「網站外觀」>**「選單/導覽列設定」**。
- **設定步驟**：
    1. 先至 [LINE Official Account Manager :lucide-external-link:](https://manager.line.biz/) 複製 **「建立按鈕」** 的語法。
    2. 在 CYBERBIZ 選單設定介面最底部點選**「新增連結」**。
    3. **新增選單項目**：貼上剛才複製的按鈕語法。
    4. **連結項目**：選擇**「外部連結」**，並貼上 LINE 好友邀請網址。
    5. 儲存選單後，前台導覽列即可出現加入好友的圖片連結。

---

## 相關操作

<div class="grid cards" markdown>

- :lucide-grip-vertical:{ .lg }   
  [__拖拉版型設定__](../../website-appearance/拖拉版型網站設定.md){ data-preview }  
  拖拉版型的詳細功能跟設定說明。

- :lucide-ban:{ .lg }     
  [____]()  
  。

</div>

---

## 常見問題

??? quote ""