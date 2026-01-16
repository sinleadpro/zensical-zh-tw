---
title: "LINE OA 建立/Messaging API 串接設定"
last_modified: ""
categories: [第三方整合>LINE相關設定]
tags: [LINE,LINE OA,LINE推播,LINE直播,LINE行銷]
permalink: "https://www.cyberbiz.io/support/?p=706"
id: "706"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/適用站別.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/台灣站.png)

**功能說明：**  

* 本教學為串接 Messaging API ，廠商可以透過 LINE 的 API 服務連接商家現有的官方帳號， 實現各種系統與 LINE 官方帳號做「串接」整合的動作，透過這樣的架構，讓商家的顧客服務有更多元的應用。 

**操作目錄：**

* 建立官方帳號 
* 設定 Messaging API
* Messaging API 串接 CYBERBIZ
* 開啟 Webhook 功能

注意事項:  

* 若要設定LINE登入可以加 LINE OA 好友，必須需要使用自己的 LINE login channel，及需要有自己的 LINE OA 帳號且有使用 Message API。
* 務必將 LINE 登入 及 Messaging API 設定於同一 Provider 中。
* LINE Messaging API channel與LINE Provider(服務提供者)綁定後便無法修改，請務必連動到正確的LINE Provider(服務提供者)。
* LINE推播服務將在LINE OA產生費用，相關計費標準，可參考官方說明的加購訊息價目表，手動推播訊息、自動傳送訂單通知訊息皆屬付費項目。
* 此教學文件僅提供操作步驟做為參考，詳細認證以及驗證請洽 LINE 官方做詢問。 
![OA/Developer比較](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定01.png)



## 📌 建立官方帳號



1. 若您沒有官方帳號請依照步驟前往 [ LINE Official Account Manager ](https://manager.line.biz/?status=success&status=success) 建立。  
*若已經擁有帳號請直接點選您的帳號名稱，並跳至 Message API 啟用。 ![建立帳號](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定02.png)


2. 【建立】  
依照步驟填寫您公司的資料 ，  
*請確保 國家/地區 選擇 台灣。  

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定03.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定04.png)



3. 完成建立後點選下方「稍後進行認證(前往管理頁面)」，進入後台。  
*若未來仍需申請認證帳號，可之後再進行申請。  
![建立帳號](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定05.png)



4. 同意 Line 事項及相關功能。  

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定06.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定07.png)





* * *

## 📌 設定 Messaging API




1. 進入[ LINE Official Account Manager ](https://manager.line.biz/?status=success&status=success) 後台，選擇「設定」→「Messaging API」→「啟用 Messaging API」  
*教學影片 [如何連動你的 LINE OA 和 LINE Provider](https://www.awesomescreenshot.com/video/18731397?key=f8d19d8913645bd40a7d7cec93269c4a)   
![建立provider](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定08.png)



2. 若您已有在 LINE Developers 建立過 Provider 即可選擇您相對應的服務提供者。  
(若已先設定 LINE登入，請選擇同一個 Provider進行串接)  
若尚未執行任何 LINE服務 請依照下列步驟進行，點選「建立服務提供者」並按下同意。  
![建立provider](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定09.png)



3. 可將您網頁的 隱私權政策 及 服務條款網址 複製貼上，並確認啟用 Message API。  

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定10.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定11.png)





* * *

## 📌 Messaging API 串接 CYBERBIZ




1. 進入[  LINE Developers ](https://developers.line.biz/en/?status=success) 後台，選擇設定好的 Admin/行政。   
![建立provider](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定13.png)



2. 點進建立完成的 Messaging API 帳號進入設定頁面，設定串接相關資料。   
![建立provider](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定14.png)



3. 選擇頁籤「Basic settings」，往下複製「Channel ID」、「Channel secret」貼至 CYBERBIZ 後台。(步驟5)   

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定16.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定17.png)



4. 選擇頁籤「Messaging API」，往下滑點擊 Issue 並複製「Channel access token」貼至 CYBERBIZ 後台。(步驟6)   
![建立provider](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定18.png)



5. 將步驟 3、4複製的「Channel ID」、「Channel secret」、「Channel access token」貼至 CYBERBIZ 後台，按下儲存後即可完成設定。  
後台路徑 :「第三方整合」→「LINE OA 設定」  
![建立provider](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定19.png)



6. 則完成設定。

* * *



## 📌 開啟 Webhook 功能



* 若您想讓 LINE 好友可以在 LINE 官方帳號中直接搜尋商品(自動回覆)，則需至 LINE Official Account Manager / LINE Developer 填入 Webhook網址。
* 若您有多個系統(如：第三方客服平台)需要 LINE API 的資料，可先將 LINE Webhook 串接至 CYBERBIZ，並將外部系統串接至 CYBERBIZ 後，由 CYBERBIZ 將資料拋至外部系統。(至多五組系統)



📍【搜尋商品】

![產品搜尋圖](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定20.png)  


1. 可至後台 複製 Webhook url，並貼至 LINE Official Account Manager / LINE Developer 。   

後台路徑 :「第三方整合」→「LINE OA 設定」  

![產品搜尋圖](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定21.png)



2. LINE Official Account Manager  
路徑 : 「設定」→「Messaging API」→「Webhook網址」
![建立帳號](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定12.png)




3. LINE Developer  
路徑 :  「Messaging API」，往下至「Webhook settings」編輯 Webhook URL。  
![建立帳號](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定15.png)



4. 設定完成後，可決定是否要開啟該功能。 ![後台開關](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定22.png)


📍【串接外部系統】

1. 點選「新增轉拋系統」可串接外部系統。  
![外部轉拋](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定23.png)



2. 設定完成畫面。  
![外部轉拋2](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Messaging-API-設定24.png)



