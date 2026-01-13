---
title: "Google Analytics 進階資料分析設定"
last_modified: ""
categories: [第三方整合>Google相關設定,TW台灣站]
tags: [GA,GA4,Google信號,第三方,資料設定]
permalink: "https://www.cyberbiz.io/support/?p=36980"
id: "36980"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/適用站別.png)

[![](https://www.cyberbiz.io/support/wp-content/uploads/台灣站.png)](https://www.cyberbiz.io/support/?page_id=2490)

### 文章目錄

* 功能說明
* 加強型評估
* Google 信號
* 加強型評估與 Google 信號的功能差異為何
* 資料保留
* 報表識別資訊

## 功能說明

* 完成 GA4 與網站的串接後，GA4 即會開始記錄基本流量資訊。
* 若您希望深入分析網站流量與使用者輪廓，建議可依照以下設定項目進行調整。這些設定可協助您依據實際需求，補強分析面向，提升決策依據的完整性與準確度。

* * *

## 加強型評估

加強型評估是 GA4 內建的自動追蹤功能，開啟後可自動記錄網站上的特定互動行為，例如：

* 網頁瀏覽
* 使用者捲動頁面
* 點擊外部連結
* 使用站內搜尋功能
* 填寫表單
* 觀看影片
* 下載檔案

透過啟用加強型評估，商家無需額外設定，即可掌握使用者在網站上的行為輪廓，有助於觀察使用者參與程度與內容互動表現，進一步優化網頁結構與行銷策略。

若商家建立GA4帳戶時沒有選擇開啟，可手動開啟功能。

1. **路徑：「管理」→「資料收集與修改」→「資料串流」→ 選擇串流 →「事件」→「加強型評估」**
[![](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-：串接教學11-1024x486.png)](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-：串接教學11.png)

2. 點擊開啟加強型評估。
[![](https://www.cyberbiz.io/support/wp-content/uploads/Snipaste_2025-04-22_11-23-45-1024x575.png)](https://www.cyberbiz.io/support/wp-content/uploads/Snipaste_2025-04-22_11-23-45.png)

3. 可點擊⚙️，依需求開啟評估事件。
[![](https://www.cyberbiz.io/support/wp-content/uploads/GA4-進階資料分析設定04-1024x486.png)](https://www.cyberbiz.io/support/wp-content/uploads/GA4-進階資料分析設定04.png)

* * *

## Google 信號

Google 信號是 GA4 中的一項進階數據功能，當使用者登入 Google
帳戶並開啟「廣告個人化」時，系統就能透過這些登入訊號，取得跨裝置、跨平台的使用行為資料。

⚠️ Google 信號雖為強化資料分析的利器，但受限於使用者是否登入 Google 及廣告個人化設定，因此資料涵蓋率可能會有所差異。

商家可於 GA4 後台手動開啟此功能。

1. **路徑：「管理」→「資源設定」→「資料收集與修改」→「資料收集」**
2. 於「Google 信號資料收集」區域點擊「啟用」。
[![](https://www.cyberbiz.io/support/wp-content/uploads/Snipaste_2025-04-07_10-54-54-1024x486.png)](https://www.cyberbiz.io/support/wp-content/uploads/Snipaste_2025-04-07_10-54-54.png)

### 加強型評估與 Google 信號的功能差異為何

雖然加強型評估與 Google 信號都能強化 GA4 的數據收集能力，但兩者的用途與資料來源有所不同，適用情境也不盡相同：

功能| 加強型評估| Google 信號  
---|---|---  
資料來源| 網站本身的使用者互動行為| 登入 Google 帳戶的使用者行為（跨裝置）  
收集對象| 所有訪客| 登入 Google 並啟用廣告個人化設定的使用者  
收集內容| 頁面瀏覽、捲動、搜尋、影片互動等行為| 性別、年齡、興趣、裝置使用偏好、跨裝置互動  
使用情境| 網站內容優化、使用者參與分析| 跨裝置轉換追蹤、再行銷名單建立、目標客群輪廓描繪  

兩者可同時啟用，互為補充。加強型評估聚焦在「網站內互動」，而 Google
信號則補足「跨平台、跨裝置」的使用者視角。建議商家視行銷需求與隱私政策條款評估是否啟用 Google 信號。

* * *

## 資料保留

GA4 預設會保留使用者資料 2 個月，若您希望觀察更長期的使用趨勢或建立再行銷名單，建議可將資料保留期限延長至 14
個月。若您的業務需要更長時間的資料保存與完整歷史數據分析，可進一步評估 GA4 付費版本所提供的進階資料儲存選項。

1. **路徑：「管理」→「資源設定」→「資料收集與修改」→「資料保留」**
[![](https://www.cyberbiz.io/support/wp-content/uploads/GA4-進階資料分析設定01-1024x486.png)](https://www.cyberbiz.io/support/wp-content/uploads/GA4-進階資料分析設定01.png)

* * *

## 報表識別資訊

GA4 採用「識別資訊空間」的方式處理使用者資料，系統會綜合多種可用訊號（如 Google 帳號、裝置
ID、行為模式等），自動判斷同一使用者在不同裝置或時間的行為，並將其統整為一筆完整紀錄。

這項技術可協助商家排除重複計算的使用者資料，提升報表準確度。例如，同一位顧客先用手機瀏覽、再用電腦下單，GA4 可辨識為同一使用者，完整描繪其轉換歷程。

透過識別資訊的整合，GA4 不僅能提供更精確的使用者分析，也能減少資料重複與誤判，有助於商家更全面掌握顧客旅程與數據意義。

1. **路徑：「管理」→「資源設定」→「資料顯示」→「報表識別資訊」**
2. 商家可依需求選擇模式。
[![](https://www.cyberbiz.io/support/wp-content/uploads/GA4-進階資料分析設定02-1024x486.png)](https://www.cyberbiz.io/support/wp-content/uploads/GA4-進階資料分析設定02.png) 模式| 說明| 特點  
---|---|---  
**混合**|  報表會綜合使用者所有可用的識別方式進行統整（User ID、Google Signals、裝置 ID）|
可提供最完整的跨裝置分析體驗，提升資料品質與精準度  
**已列為觀察項目**|  僅使用實際觀察到的裝置或平台資訊（不會自動整合或推論）| 避免誤判或推測，報表結果更保守但更貼近原始紀錄  

* * *

