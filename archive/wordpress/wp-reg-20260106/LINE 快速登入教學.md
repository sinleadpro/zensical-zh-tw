---
title: "LINE 快速登入教學"
last_modified: ""
categories: [第三方平台整合>LINE相關設定]
tags: []
permalink: "https://www.cyberbiz.io/helpcenter/?p=865"
id: "865"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/一般版3.png)
![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**功能說明：**  

* 顧客可於「會員註冊」、「結帳頁」使用LINE快速登入，系統將自動抓取客戶LINE的「Email」做帳號比對。

**操作目錄：**

* 建立 LINE 登入資訊 
* 填入【帳號ID】、【應用程式密鑰】至 CYBERBIZ 後台
* LINE 快速登入導引會員加入LINE官方帳號好友(PLUS版專用)
常見問題

7. 無法於後台完成串接
8. LINE 快速登入頁面出現 400 Bad Request
9. iOS系統無法直接跳轉登入畫面

注意事項:  

* 請商家參照以下文件操作，並填入應用程式ID、應用程式密鑰並開啟【啟用LINE登入】，方可使用LINE登入。
* 消費者使用 Hinet信箱登入會員，若忘記密碼，會因為 Hinet 阻擋訊息而無法重新設定密碼，可建議客戶使用其他信箱註冊。 。
* 顧客的 LINE帳號 一定要綁定EMAIL，才可使用 LINE 登入。 
* LINE 相關設定有較多頁籤需來回跳轉，請注意文章中標示頁籤以便您的設定。



## 📌 建立 LINE 登入資訊

1. 請先至[LINE Developers](https://developers.line.biz/en/) 登入帳號（需要有LINE帳戶），若已經登入可按「console」進入。  
[![登入linedeveloper](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入01.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入01.png)



2. 進入畫面後，若您尚未有任何 Provider，請先按下方建立一個，  
[![選擇/建立provider](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入02-h.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入02-h.png)  
*若尚未建立過 Provider的客戶可自行建立一個。  
[![無provider](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入03.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入03.png)



3. 點選【Create a LINE Login channel】。  
[![新建loginchannel](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入04-h.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入04-h.png)



4. 選擇 LINE Login 功能。  
[![login畫面](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入05.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入05.png)



5. 填寫下方欄位。  

* 【Region to provide the service】: Taiwan 
* 【Company or owner’s country or region】 : Taiwan
[![新建channel](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入06.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入06.png)  

* 【Channel icon】: 上傳網站 Logo
* 【Channel name】: 輸入商店名稱
* 【Channel description】: 輸入商店簡述。(內容不可換行)
* 【App types】: 勾選 Web app
[![設定channel](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入07.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入07.png)  

* 【Email address】: 輸入 email
* 【Privacy policy URL】: 輸入網站隱私政策網址
* 【Terms of use URL】: 輸入網站服務條款網址
* 勾選條款後點擊 Creat 按鈕
[![設定channel2](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入08.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入08.png)  


6. 完成設定後，可先將狀態「Developing」轉至「Published」，  
選擇頁籤「Basic settings」滑至最下方至「OpenID Connect」。  
[![設定openID](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入09.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入09.png)



7. 點開 OpenID Connect 的「Apply」 
* 若無法於後台完成 LINE 快速登入串接，請檢查已完成此步驟。

[![openID connect](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入10.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入10.png)



8. 設定【OpenID Connect】欄位資訊，確認狀態為「Applied」，  
並勾選裡面的內容，依照需求上傳 商家Logo，並按下「Submit」。  
[![openID connect2](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入11.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入11.png)



9. 點選 頁籤「LINE Login」設定 Callback URL，點選「Edit」。   
[![callback](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入12.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入12.png)



10. 填入商家的 Callback URL。  
若您的商店網址為：https://2020test.cyberbiz.co/則填入：https://2020test.cyberbiz.co/customer/auth/line/callback  


* Callback URL 支援新增多個網域，**若您有購買自有網域，請務必將 CYBERBIZ 網域及自有網域都一併填入「Callback URL」。**
* 填入 CYBERBIZ 網域後，點擊 ENTER 鍵，即可新增自有網域。
* 若 LINE 快速登入頁面呈現 400 Bad Request，屆時顧客無法由 LINE 帳號登入或註冊會員，請商家確認此步驟網址填寫無誤。


![](https://www.cyberbiz.io/support/wp-content/uploads/fountain-pen.png)

* 跨境用戶填入網址不需加上 zh-TW 等，僅需填寫一般的網域即可。
* 自有網域及 CYBERBIZ 網域設定邏輯相同。


[![callbackURL設定](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入13.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入13.png)



* * *

## 📌 填入【帳號ID】、【應用程式密鑰】至 CYBERBIZ 後台



1. 請先至[LINE Developers](https://developers.line.biz/en/) 選擇頁籤「Basic settings」，複製【Channel ID】【Channel secret】。  
[![設定id，secret](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入14.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入14.png)



2. 至 CYBERBIZ 後台貼上並開啟「啟用LINE登入」  
後台路徑 :「第三方整合」「LINE 註冊登入」  
[![設定id，secret](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入15.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入15.png)



3. 設定完成後至商店前台即可使用「LINE 快速登入」  
[![前台登入畫面](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入16.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE快速登入16.png)



* * *

## 📌 LINE 快速登入導引會員加入LINE官方帳號好友(PLUS版專用)

1. 請先至[LINE Developers](https://developers.line.biz/en/) 選擇頁籤「Basic settings」，往下滑至「Linked OA」，選擇 Edit。  
[![linkoa](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入17.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入17.png)



2. 可選擇同個 Provider下的 LINE官方帳號。  
[![linkoa選擇](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入18.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入18.png)



3. 前台畫面，使用 LINE快速登入，並可出現「加入好友」按鈕。  
[![前台登入畫面19](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入19.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入19.png)  
*會員若點擊「取消」，仍可登入但就不會自動加入 LINE官方帳號。  
[![前台登入畫面20](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入20.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入20.png)

* * *

## 📌 常見問題：iOS系統無法直接跳轉登入畫面

若 iOS系統無法直接跳轉登入畫面，請依照下方指示進行登入。  


1. 建議使用 Safari 瀏覽器 進行操作。 


2. 若出現 『要在「LINE」中打開嗎？』 的彈窗，請選擇 打開。  
[![line打開](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入22.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入22.png)



3. 如果沒有出現彈窗，請點擊畫面下方 「使用 LINE 應用程式登入」。  
[![line登入](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入23.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入23.png)



