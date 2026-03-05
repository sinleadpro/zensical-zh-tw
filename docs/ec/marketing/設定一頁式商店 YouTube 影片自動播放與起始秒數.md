---
title: "設定一頁式商店 YouTube 影片自動播放與起始秒數"
description: "調整 YouTube 影片網址參數，在一頁式商店中設定自動播放、循環播放與指定播放起始秒數。"
created: "2024-05-23 11:30"
last_modified: 2026-03-05 11:51
lang: "zh-TW"
type: "tutorial"
status: ""
version: ""
author: Jase
reviewers: []
notes:
  - verify youtube embed url 限制 autoloop 是不是只能從頭開始，CYB 支援程度。
ga_views: 
feedback:
products:
  - EC
modules:
  - 行銷活動
  - 一頁式商店
sites:
  - TW
audiences:
  - merchant
difficulty: "advanced"
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
  - 設定 YouTube 影片自動播放
  - 設定 YouTube 影片開始秒數
features:
  - YouTube 影片嵌入
  - 自動播放
  - 循環播放
  - 指定播放時間
prerequisites:
  - 登入 CYBERBIZ 管理後台
related: []
tags:
  - YouTube
  - 影片
  - 自動播放
  - 一頁式商店
  - 循環播放
  - 起始秒數
acoiv: "configure"
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 一頁式商店頁面
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3838
  - https://www.cyberbiz.io/support/?p=19650
permalink: ""
comments: ""
search:
  exclude: ""
icon: ""
---

調整 YouTube 影片網址參數，在一頁式商店中設定自動播放、循環播放與指定播放起始秒數。
{ .subtitle }

![](../../../assets/images/ec-行銷活動-一頁式商店-影片設定.png){ .hero-page }

## 一頁式商店影片自動播放功能說明

您可以針對一頁式商店設定 **YouTube 影片自動播放** 或 **設定特定的播放開始時間**，以增加商品展示的動態效果與精準度。

以下為一頁式商店影片設定的詳細教學：

## 基礎影片置入步驟

1.  **進入路徑：** 登入 CYBERBIZ 管理後台，前往 **行銷活動 > 一頁式商店頁面 > 選擇您要設定的活動頁**。
2.  **銷售內容設定：** 點選「銷售內容設定」分頁，在下方新增區塊處點擊「插入影片」。
3.  **嵌入連結：** 貼上您想要嵌入的 **YouTube 影片網址**，並點選「新增」。

![](../../../assets/images/ec-行銷活動-一頁式商店-插入影片-舊版.png)

---

## 設定影片自動播放

若希望消費者進入頁面時影片即自動開始播放，請執行以下操作：

1.  **編輯影片：** 在已新增的影片區塊點擊「編輯影片」。
2.  **修改語法：** 在原網址後方加上以下程式碼參數：

	```
	?rel=0&playlist=此影片的ID&loop=1&autoplay=1&mute=1
	```

	??? info "快速取得 YouTube 影片 ID"
    
	    請從影片網址 (URL) 中尋找 **`v=`** 後面的 **11 位字元**。
	    
	    - **範例網址**：`https://www.youtube.com/watch?v=dQw4w9WgXcQ`
	    - **影片 ID**：<code style="color: #c7254e; background-color: #f9f2f4; padding: 2px 4px; border-radius: 4px;">dQw4w9WgXcQ</code>

1.  **重要規範：** 根據 YouTube 的規範，開啟自動播放功能時 **必須設定為「靜音 (mute=1)」**，否則自動播放將無法生效。
2.  **儲存：** 完成語法修改後按下儲存，即可在預覽畫面確認自動播放效果。

![](../../../assets/images/ec-行銷活動-一頁式商店-youtube影片-自動播放-設定-舊版.gif)

## 設定影片指定開始播放秒數

如果您希望影片從特定秒數開始播放（例如跳過前奏直接進入介紹），請參考以下設定：

1.  **單純指定時間：** 在影片網址後方新增 `?start=秒數`。
    *   **計算範例：** 若想於 1 分 20 秒開始，請設定為 80 秒（60+20=80），語法即為 `?start=80`,。
2.  **指定時間 + 自動播放（混合設定）：**
    若要兩者兼具，請先設定開始秒數，再接續自動播放代碼。範用語法為：
    
	```
	https://www.youtube.com/embed/此影片的ID?start=秒數&rel=0&playlist=此影片的ID&loop=1&autoplay=1&mute=1
	```

![](../../../assets/images/ec-行銷活動-一頁式商店-youtube影片-自動播放加起始秒數-舊版.png)

## 拖拉版型介面（新版）影片設定

若您使用的是拖拉介面，設定方式如下：

1.  **進入路徑：** 登入 CYBERBIZ 管理後台，前往 **行銷活動 > 一頁式商店頁面 > 選擇您要設定的新版活動頁 > 頁面設定**。
2.  **新增區塊：** 點擊「新增區塊」並選擇「影片」或在「自訂排版設計」中加入「影片」素材。
3.  **貼上網址：** 貼上影片的 YouTube 網址。目前此介面僅支援 YouTube 格式。
4. **影片設定：**

	- **自動播放**：開啟後，訪客瀏覽至頁面影片區塊時影片將自動播放。

	- **隱藏外框**：當影片開啟自動播放，且啟用隱藏外框，該 YouTube 無法暫停影片。
	
	- **重複播放**：開啟後，影片播放結束時將自動返回起始點重新播放，形成無間斷循環。
	
	- **版面外邊距**：可設定左右外邊距、底部外邊距。電腦版與手機版(手機版包含平板版)可分開設定。

![](../../../assets/images/ec-行銷活動-一頁式商店-影片設定.gif)

---

## 注意事項

*   **影片 ID 注意事項：** 每一部影片的 ID 皆不同，在貼上自動播放程式碼時，請務必確保 `playlist=` 後方的 ID 與您嵌入的影片 ID 一致,。
*   **YouTube 限制：** 目前系統僅支援 YouTube 網址格式，若您有自備影片檔案，須先上傳至 YouTube 後再行設定,。
*   **原始碼錯誤處理：** 若在編輯過程中發現影片後的圖片或文字消失，通常是因為影片語法標籤未正確閉合或被其他標籤包住，此時需點擊編輯器左上角的「原始碼」檢查並修正 `<div>` 或 `<p>` 標籤。
*   **恢復機制：** 若修改程式碼後導致頁面異常，可利用樣版編輯器內的 **查看之前版本** 按鈕 [回溯至先前版本](../website-appearance/使用樣板編輯器恢復網頁代碼.md#操作步驟){ data-preview }。

---

## 常見問題

??? quote "為什麼我設定了自動播放，但影片卻沒有聲音？" 
	根據 YouTube 與主流瀏覽器（Chrome, Safari）的安全性規範，為了避免干擾使用者，**「自動播放」功能必須與「靜音 (mute=1)」同時使用**。若您取消靜音參數，瀏覽器將會強制停止影片自動播放。

??? quote "為什麼在手機上無法自動播放影片？" 
	行動裝置（iOS/Android）為了節省使用者的行動數據流量，對自動播放有較嚴格的限制。請確保您的參數中包含 `mute=1`。此外，若手機開啟了「低耗電模式」，系統可能會為了省電而攔截所有自動播放行為。

??? quote "如果我想讓影片在 1 分 30 秒開始，並在 2 分 00 秒結束並循環，該如何設定？" 
	您可以結合 `start` 與 `end` 參數來定義播放區間。

	- **計算秒數**：1 分 30 秒 = 90 秒；2 分 00 秒 = 120 秒。
	    
	- **範例語法**：`?start=90&end=120&rel=0&playlist=影片ID&loop=1&autoplay=1&mute=1`
	    
	**重要技術限制：** 雖然上述設定能讓影片在「首次載入」時從 90 秒開始播放，但根據 YouTube 官方參數規範，嵌入播放器在觸發 `loop`（循環）重播時，會直接跳回影片的 **00:00** 位置，而不會保留 `start` 的設定值。

??? quote "我可以使用 YouTube 以外的平台（如 Vimeo 或 Facebook）影片嗎？" 
	目前 CYBERBIZ 一頁式商店的影片區塊與自動播放優化功能，**僅支援 YouTube 格式**。若您的影片在其他平台，建議先下載並上傳至 YouTube 頻道後，再依照本文件步驟進行設定。