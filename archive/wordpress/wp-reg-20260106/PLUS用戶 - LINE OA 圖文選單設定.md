---
title: "PLUS用戶 - LINE OA 圖文選單設定"
last_modified: ""
categories: [第三方平台整合>LINE相關設定,PLUS版適用]
tags: [LINE,LINE OA,PLUS版專用]
permalink: "https://www.cyberbiz.io/helpcenter/?p=5858"
id: "5858"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**功能說明：**  

* 如何設定圖文選單與文字引導，達成透過LINE OA推廣商品目的。
* 透過 LINE 官方帳號 設定 關鍵字快速尋找商品。

**操作目錄：**

* 建立圖文選單
* 設定圖文選單內容【動作】

注意事項:  

* 請先確認您目前使用的 LINE OA 方案是否支援API串接。
* 請先設定完 [LINE Messaging API 串接設定](https://www.cyberbiz.io/helpcenter/?p=5855)。 
* LINE推播服務將在LINE OA產生費用，相關計費標準，可參考官方說明的 [加購訊息價目表](https://tw.linebiz.com/service/account-solutions/line-official-account/)，手動推播訊息、自動傳送訂單通知訊息皆屬付費項目。 
* 圖文選單的連結請勿使用短網址，而造成代碼失效。 
* 網址設定狀態 : 
1. 顧客綁定 LINE OA帳戶與官網會員  
https://你的網址/customer/auth/line?line_action=代號2. 顧客不綁定LINE OA 帳戶與官網會員，直接瀏覽網頁  
A : https://你的網址/代號B : 直接複製指定頁面



## 📌 建立圖文選單



1. 進入 [LINE Official Account Manager](https://account.line.biz/login) ，選擇官方帳號，  
左側選單選擇「聊天室相關」→「圖文選單」，點選「建立圖文選單」  
[![line圖文選單01](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定01.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定01.png)



2. 設定圖文選單資訊  
【標題】 : 圖文選單名稱，顧客不會看到此名稱。  
【使用期間】 : 設定此圖文選單執行時間。  
【選單列顯示文字】: 顯示於聊天室下方選單列中的文字，顧客會看到此名稱。  
【預設顯示方式】 : 預設顯示/隱藏。(若選擇隱藏，顧客需點選選單，才會彈出)  
[![line圖文選單02](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定02.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定02.png)



3. 設定圖文選單內容，  
【版型】、【圖片】  
[![line圖文選單03](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定03.png)



4. 設定【版型】、【圖片】 
* 格式：JPG、JPEG、PNG。
* 容量：1 MB 以下。
* 圖片尺寸：2500 x 1786、2500 x 843、1200 x 810、1200 x 405、800 x 540、800 x 270 共六種。(單位px)


[![line圖文選單04](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定04.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定04.png)

[![line圖文選單05](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定05.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定05.png)



* * *

## 📌 設定圖文選單內容【動作】



1. 設定 LINE 圖文選單常見功能  
【類型】: 連結 。  
【動作標籤】: 在適用的情況下朗讀此處文字，在不支援的情況下只會顯示文字。  
**連結可自行設定 或 透過下方相關代號 自行設定。  
[![line圖文選單06](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定06.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定06.png)



2. 設定相關代號  
CYBERBIZ 提供商家幾個常用代碼可讓您快速連接 LINE 官方帳號以及官網，  
也可以直接貼入您想指定的頁面做連結。(其他相關應用請各商家自行設計操作)  
*(建議您若是使用下述該代號進行設定，  
皆可使用 https://你的網址/customer/auth/line?line_action=代號，進行設定 )  

[![line圖文選單07](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定07.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定07.png)



3. 設定完成後前台即可開始使用此功能。  

[![line圖文選單07](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定07-1.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-圖文選單設定07-1.png)



4. 建議您 可先讓顧客先將 LINE OA帳號綁定官網會員，詳細方法 請至 [LINE OA 官方帳號 綁定 官網會員](https://www.cyberbiz.io/support/?p=32679)  
顧客綁訂流程只會出現一次，之後就都會直接導到該頁面，  
*只要您設定的連結為   
https://你的網址/customer/auth/line?line_action=代號 ，皆可觸發顧客綁定動作。  


範例 : (代號不論是哪個都可觸發該綁定)

連結 : https://你的網址/customer/auth/line?line_action=blogs 。  


顧客點擊後 :

尚未綁定的顧客，會先進行綁定動作，並連結到官網 blog 頁面。  
綁定過的顧客，會直接進入官網 blog 頁面。 (狀態為已登入)





