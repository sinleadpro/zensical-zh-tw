---
title: "如何在Google Ads建立轉換追蹤"
last_modified: ""
categories: [第三方整合>Google相關設定,TW台灣站,跨境電商>北美站,常見問題]
tags: [ads,GOOGLE,廣告]
permalink: "https://www.cyberbiz.io/support/?p=232"
id: "232"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/適用站別.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/台灣站.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/北美站.png)

此文件指導商家如何在Google Ads分析網站流量、追蹤廣告成效。

看完此文件，您可以

* 初步了解 Google Ads。
* 初步了解 轉換追蹤。
* 建立轉換追蹤，查看Google廣告的成效。
* 設定要觀測的用戶行為。

CYBERBIZ 僅提供 Google 轉換代碼串接及基礎設定教學，詳細設定與應用敬請洽詢 Google 廣告官方網站或您的廣告代理商。

## 什麼是Google Ads

Google Ads（前身為 Google AdWords）是一個由 Google 提供的廣告平台，允許商家在 Google
的搜尋引擎、YouTube、以及其他 Google
相關網站上投放廣告。商家可以使用這個平台創建和管理各種廣告類型，吸引潛在客戶並推廣官網品牌及商品。詳情可參考 [Google官方文件：您的 Google
Ads 指南](https://support.google.com/google-ads/answer/6146252)。

## 為什麼要設置轉換追蹤

設置轉換追蹤後，商家可於Google Ads觀測廣告成效，了解客戶行為，並可優化廣告效果並提高廣告精準度。詳情可參考
[Google官方文件：轉換追蹤簡介](https://support.google.com/google-ads/answer/1722022?hl=zh-Hant)。

## 我該如何開始

1. 登入Google Ads，點擊「開始使用」。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤01-1024x490.png)
2. 請先建立第一個 Google 廣告活動，方可建立轉換追蹤。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤02-1024x486.png)



## 我該如何建立轉換追蹤

1. 於側邊欄點擊「目標」→「摘要」，點擊「新增轉換動作」。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤03-1024x486.png)
2. 選擇「網站」。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤04-1024x486.png)
3. 輸入官網網址，點擊「掃描」。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤05-1024x486.png)
4. 點擊「手動新增轉換動作」。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤06-1024x486.png)
5. 進入「轉換動作詳細資料頁」，設定以下欄位： 
* 「目標和動作最佳化」：依需求選擇要追蹤的動作事件。
* 「轉換名稱」：依需求命名此轉換。
* 「價值」：
* 若「目標類別」選擇「購買」，請選擇「為每次轉換指定不同的價值」。
* 若「目標類別」選擇其他類型，請選擇「為每次轉換指定相同的價值」。
* 「計算方式」：依需求選擇；若無其他需求，可選擇「每次」。
![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤07-1024x717.png)

6. 其他欄位可依需求調整，設定完成後點擊「完成」。
7. 若有多個用戶行為想要追蹤，請再次點擊「手動新增轉換動作」，選擇要追蹤的動作事件，並完成設定。

✅ 於此處新增所有想觀測的用戶行為

![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤06-1024x486.png)

❌ 不要於此個別新增想觀測的用戶行為

![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤03-1024x486.png)

8. 設定完成，點擊「同意並繼續」。
9. 選擇「使用Google 代碼管理工具」，查看「轉換ID」與「轉換標籤」。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads01-1024x486.png)
10. 建立轉換追蹤後請將代碼安插至官網後台。

## 如何將轉換追蹤代碼安插至官網後台

後台路徑：第三方整合→ 谷歌Google設定

1. 於「Google Ads再行銷」區域，將「使用Google 代碼管理工具」頁面的「轉換ID」輸入至「再行銷編號僅數字」欄位。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤08-1024x490.png)
2. 於「Google Ads轉換追縱」區域，點擊「新增轉換追蹤事件」。 ![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤09-1024x490.png)
3. 於「新增Google Ads轉換追蹤」頁面中設定以下參數。 
* 「轉換追蹤事件」：請根據在 Google「目標和動作最佳化」欄位設定的「目標類別」，選擇對應的後台追蹤事件。 
* CYBERBIZ 提供6種轉換追蹤事件供商家選擇，可依下方表格，查看與「目標類別」對應的追蹤事件。

Google目標類別| 對應後台可追蹤事件  
---|---  
網頁瀏覽| 顧客造訪商店內任何頁面  
網頁瀏覽| 顧客造訪商店首頁  
開始結帳| 顧客造訪結帳頁  
完成註冊| 顧客註冊會員  
購買| 顧客完成訂單  
加入購物車| 顧客將商品加入購物車  

![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤10-1024x715.png)



* 「轉換追蹤編號」：將「使用Google 代碼管理工具」頁面的「轉換ID」貼上。
* 「轉換追蹤標籤」：將「使用Google 代碼管理工具」頁面的「轉換標籤」貼上。
![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤11-1024x486.png)

* ⚠️ 之前若有透過 GTM 設定追蹤 Google 廣告轉換，使用後台進行追蹤後要記得將GTM中的設定移除，否則會因重複埋設造成 Code碼打架，廣告數據不準確。
* Google Ads 的轉換追蹤功能也會使用 Cookie。為方便您追蹤廣告所帶來的銷售和其他轉換，只要有人點擊廣告或產品資訊，這項功能就會將 Cookie 存在對方的電腦上。
* 若有「事件」沒有收集到顧客的任一基本資料欄位，則系統不會傳送資料給 Google。 

## 轉換代碼無法追蹤到官網的消費者行為，該如何排解

![](https://www.cyberbiz.io/support/wp-content/uploads/google-ads轉換追蹤12-1024x490.png)

* 請確認 EC後台中，「再行銷編號僅數字」與「轉換追蹤編號」代碼相同，如有不同，請確認是否按照步驟7新增轉換動作。

## 自動化廣告可以設置轉換追蹤嗎

* 不行，自動化廣告由CYBERBIZ帳號代管，恕無法透過Google Ads查看數據，商家可前往後台查看數據。
* 詳情可參閱 [自動化廣告系統](https://www.cyberbiz.io/support/?p=34930#track)。

