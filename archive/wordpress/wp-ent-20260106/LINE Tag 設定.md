---
title: "LINE Tag 設定"
last_modified: ""
categories: [行銷活動>行銷工具,第三方整合>LINE相關設定]
tags: [LINE OA,LINE推播,LINE行銷]
permalink: "https://www.cyberbiz.io/support/?p=28602"
id: "28602"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/全版本.png) **功能說明：**  

* LINE Tag為LINE LAP(成效型廣告)埋設之追蹤碼，類似於Pixel和Facebook Ad之間的關係。
* 您可於**LINE OA Manager 官方帳號後台** 或**LINE Ad Manager 廣告後台** 建立欲使用的LINE Tag，前者追蹤OA訊息推播轉換，後者追蹤廣告投放轉換，兩後台LINE Tag可共享，LINE Tag搜集之數據可於LINE後台打包成「網站流量受眾」，詳情請見操作目錄「LINE Tag應用」。 
**操作目錄：**

* CYBERBIZ 完成的LINE Tag event
* 設定步驟LINE OA Manager官方帳號後台用於訊息推播轉換追蹤
* 設定步驟LINE Ad Manager廣告後台用於廣告轉換追蹤
* 如何檢查 LINE Tag 是否追蹤成功
* LINE Tag 應用
注意事項:  

* 請先建立LINE OA 官方帳號
* 若要於LINE Ad Manager廣告後台使用LINE Tag，請先建立LINE廣告帳號
* 若您的瀏覽器有安裝adblock，請先將該套件關閉。

CYBERBIZ 完成的LINE Tag event EVENT | 解釋  
---|---  
CompleteRegistration | 完成註冊  
Search | 搜尋商品  
PageView (每一頁) | 瀏覽頁面  
ViewContent (商品頁) | 瀏覽商品頁  
AddToCart | 加入購物車  
InitiateCheckout | 進入結帳頁  
Purchase | 訂單完成  

* * *

設定步驟(LINE OA Manager)用於訊息推播轉換追蹤  

1. 進入[LINE OA Manager](https://manager.line.biz/)，點選欲設定之官方帳號  
[![LINETAG設定01](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定01.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定01.png)



2. 進入OA頁面，於左側欄選擇「追蹤(LINE Tag)」   
[![LINETAG設定02](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定02.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定02.png)



3. 使用 ctrl+F 快速搜尋tagid，複製tagid   
[![LINETAG設定03](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定03.png)



4. 後台「新增Tag ID」，類型選擇 account ，將已複製之tagId填入「Tag ID」欄位。  
後台路徑 : 「第三方」→「LINE Tag 設定」  
[![LINETAG設定04](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定04.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定04.png)



* * *

設定步驟(LINE Ad Manager)用於廣告轉換追蹤  

1. 進入[Ad Manager](https://manager.line.biz/)，點選欲設定之「廣告帳號名稱」，進入設定頁面  
[![LINETAG設定05](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定05.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定05.png)



2. 進入OA頁面，於左側欄選擇「追蹤(LINE Tag)」   
[![LINETAG設定06](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定06.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定06.png)



3. 使用 ctrl+F 快速搜尋tagid，複製tagid   
[![LINETAG設定07](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定07.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定07.png)



4. 後台「新增Tag ID」，類型選擇 lap ，將已複製之tagId填入「Tag ID」欄位。  
後台路徑 : 「第三方」→「LINE Tag 設定」  
[![LINETAG設定08](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定08.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定08.png)



* * *

如何檢查 LINE Tag 是否追蹤成功  
【方法一】  
打開EC前台，至前台操作 CYBERBIZ 埋設追蹤碼的動作事件 (**每個** 事件都需執行才會顯示)，執行後重新整理「LINE OA Manager」
/ 「LINE Ad Manager」查看事件名稱是否出現於狀態。  
例如 : 若您要檢查「CompleteRegistration完成註冊」事件是否埋設成功，請先到您的官網進行會員註冊，完成後刷新後台LINE
Tag頁面，檢查該事件是否出現於狀態列表。  
[![LINETAG設定09](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定09.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定09.png)  

【方法二】  
下載[LINE Tag Helper](https://chrome.google.com/webstore/detail/line-tag-helper/jgnholagndjghcjedffhinifilbjmklg?hl=zh-TW) (Chrome擴充功能)  
[![LINETAG設定10](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定10.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定10.png)  


* * *

LINE Tag 應用  
【LINE OA Manager官方帳號後台】

1. 受眾建立(用途-可用來發送訊息，精準行銷)  
進入 LINE OA， 點進資料管理「受眾」，  
選擇網站流量受眾 ，並設定目標。  
[![LINETAG設定11](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定11.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定11.png)  

2. 分析 - 群發訊息 - 自訂轉換 (用途：分析該訊息的轉換表現)  
[![LINETAG設定12](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定12.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定12.png)  
[![LINETAG設定13](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定13.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定13.png)  


【LINE Ad Manager 廣告帳號】建立廣告受眾

1. 點選您的廣告帳號。  
[![LINETAG設定14](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定14.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定14.png)



2. 點選受眾。  
[![LINETAG設定15](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定15.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定15.png)



3. 建立受眾，並點選「網站流量受眾」。  
[![LINETAG設定16](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定16.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定16.png)



4. 點選您的廣告帳號  
[![LINETAG設定17](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定17.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定17.png)



5. 新增受眾，選擇 LINE Tag 並選擇想要設定的事件，完成設定後，投放廣告則可選擇設定好的受眾。  
[![LINETAG設定18](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定18.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINETAG設定18.png)

