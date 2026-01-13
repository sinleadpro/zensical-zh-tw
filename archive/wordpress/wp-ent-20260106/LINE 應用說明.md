---
title: "LINE 應用說明"
last_modified: ""
categories: [第三方整合>LINE相關設定]
tags: []
permalink: "https://www.cyberbiz.io/support/?p=21985"
id: "21985"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/wp-主視覺bar-1024x321.png) ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/08/全版本.png) **功能說明：**  
以下為LINE官方帳號與 CYBERBIZ 系統的多種運用方式及設定辦法 建議依推薦步驟依序完成，並可自行取捨設定項目。  

**一般版/企業版適用：**  
一、客戶可透過 Line 快速登入，成為網站會員。  
二、邀請客戶加入 LINE 官方帳號的幾種方法。  
三、加入 LINE 官方帳號取得優惠券；A-加入好友的歡迎訊息優惠券、B-綁定優惠券（限企業版）。  
四、如何設定 LINE 官方帳號圖文選單，讓消費者快速查找會員資料/商品/部落格...等。  
五、LINE 官方帳號聊天機器人與聊天模式差異說明。  

**企業版適用：**  
六、透過 LINE 官方帳號圖文選單與Messaging API串聯，達成通知消費者訂單、退貨、物流、顧客、定期訂單等相關資訊的目的。  
七、開啟 LINE 官方帳號會員條碼功能，提供消費者在門市結帳的會員認證。  **操作目錄：**

* 網站透過 Line 登入會員
* 引導客戶加入 LINE 官方帳號
1.右側活動廣告 Event  
2.頁腳社群媒體 ICON  
3.連結列表、外掛程式  
4.GetButton 免費客服

* 加入 LINE 官方帳號 發送優惠券(提供優惠券序號)
* 綁定LINE 官方帳號會員 贈送優惠券(綁定會員)
* LINE官方帳號 圖文選單設計
* LINE 官方帳號聊天機器人與聊天模式差異說明
* 串接 LINE Messaging API
* LINE 官方帳號 訊息樣板通知
* LINE 官方帳號 會員條碼（使用 POS 系統客戶可使用）
注意事項:  

* 訂單推播功能需先設定完成  創建圖文選單 及 Messaging API。
* 當 Facebook 與 LINE 為同一組 Email 時，帳號會相互綁定，反之若為不同 Email 時，則登入帳號無法合併。
* 此教學文件僅提供操作步驟做為參考，詳細操作步驟及規範請洽 LINE 官方做詢問
* LINE推播服務將在LINE OA產生費用，相關計費標準，可參考[官方說明](https://tw.linebiz.com/service/account-solutions/line-official-account/)的[加購訊息價目表](https://vos.line-scdn.net/lbstw-static/images/uploads/download_files/3f6edc69fe6c023898ed38a21c86c02d/%E5%AE%98%E6%96%B9%E5%B8%B3%E8%99%9F%E9%AB%98%E7%94%A8%E9%87%8F%E6%9C%88%E8%B2%BB%E6%96%B9%E6%A1%88%E5%8A%A0%E8%B3%BC%E8%A8%8A%E6%81%AF%E5%83%B9%E7%9B%AE%E8%A1%A8.pdf)，手動推播訊息、自動傳送訂單通知訊息皆屬付費項目。

一、網站透過 Line 登入會員  
CYBERBIZ 提供透過 LINE 快速登入網頁會員。  
透過 LINE 登入，必須綁定 Email，所以當 Facebook 與 LINE 為同一組 Email 時，帳號會相互綁定，反之若為不同 Email
時，則登入帳號無法合併。  
LINE 登入詳細操作說明請至[LINE 登入教學](https://www.cyberbiz.io/support/?p=675) 查看  

[![LINE_application_description14](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description14.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description14.png)

* * *

二、引導客戶加入 LINE 官方帳號  
【設置LINE官方帳號加入連結，供客戶自行加入】  
提供四種方法 :  
1.右側活動廣告 Event  
2.頁腳社群媒體 ICON  
3.連結列表、外掛程式  
4.GetButton 免費客服  

進入「LINE Official Account Manager」→「主頁」→「增加好友人數」→「加入好友指南」，可自行複製「網址」、「行動條碼」等連結。  

[![LINE_application_description01](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description01.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description01.png)  

**方法一 : 右側活動廣告 Event**  


* 透過網站右側活動廣告 Event，新增粉絲團行動條碼。  
**請注意！** 此方法僅供預設版型使用。  
[![LINE_application_description02](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description02.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description02.png)  

* 後台路徑: 「網站外觀」→ 「套版主題管理」→ 「網站設定」→ 「右側活動廣告Event」 即可將上述複製的網址及行動條碼填入。  

[![LINE_application_description03](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description03.png)  

* 更改右側活動廣告 Event 文字及底色  
後台路徑: 「網站外觀」→「套版主題管理」→「程式碼編輯器」→「fast_events.liquid」  
[![LINE_application_description04](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description04.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description04.png)


**方法二 : 頁腳社群媒體 ICON**  


* 透過網站頁腳的社群媒體設定，新增粉絲團的連結  

[![LINE_application_description05](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description05.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description05.png)  

* 後台路徑 :「網站外觀」→「網站設定」→「頁腳Footer」→「社群媒體設定」  
即可將上述複製的網址及行動條碼填入。  

[![LINE_application_description06](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description06.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description06.png)


**方法三 : 連結列表**  


* 連結列表新增加入 LINE 官方帳號 圖示連結  

[![LINE_application_description07](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description07.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description07.png)  

* 複製條碼步驟 : 「LINE Official Account Manager」→「主頁」→「增加好友人數」→「加入好友指南」→「在網站設置連結鍵」裡的程式代碼，並編輯選單項目。  
新增連結列表 :  
後台路徑 :「網站外觀」→「選單/導覽列設定」→「主選單」→「新增選單項目」→ 貼上複製的程式代碼  
[![LINE_application_description08](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description08.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE_application_description08.png)


**方法四 : 外掛程式 GetButton 免費客服**  


* 透過外掛程式 GetButton 免費客服插件，也可埋入 LINE@ 官方帳號行動條碼。  
詳細設定請至 [客服視窗設定](https://www.cyberbiz.io/support/?p=16750/#c)。



【主動邀請網站會員加入LINE官方帳號】(限企業版客戶)  
商家想讓未加入 LINE 官方帳號的"網站會員"收到加入 LINE 官方帳號的簡訊或 Email 訊息，  
詳細設定請至 [LINE@ 透過簡訊和 EMAIL 發送加入好友邀請](https://www.cyberbiz.io/support/?p=739) 。  
*輸入完內容後按下立即傳送會跳出彈跳視窗做二次提醒。   

[![LINE_application_description15](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description15.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description15.png)

* * *

三 - 1、加入 LINE 官方帳號 發送優惠券(提供優惠券序號，不需綁定會員即可領取)  
透過 LINE 官方帳號 加入好友的歡迎訊息優惠券，  
可至「LINE Official Account Manager」→「主頁」→「加入好友的歡迎訊息」貼上優惠券序號及相關文字。  
優惠券製作方式請至[ 優惠序號(優惠碼)](https://www.cyberbiz.io/support/?p=6228)查看  
[![LINE_application_description09](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description09.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description09.png)

* * *

三 - 2、綁定LINE 官方帳號會員 贈送優惠券(綁定會員)  
透過贈送優惠券的誘因，來提升客戶加入 LINE 官方帳號的意願，以利增加客戶對品牌的黏著度，也可以依商家促銷的商品而做進階的設定。  
詳細設定請至[ LINE@綁定會員送優惠券](https://www.cyberbiz.io/support/?p=763) 設定。  


* * *

四、LINE官方帳號 圖文選單設計  
消費者可直接在 LINE
聊天視窗輸入關鍵字，系統會自動出現搜尋字眼，但消費者一開始並不知道可以直接輸入關鍵字搜尋，因此可以透過圖文選單來引導消費者輸入關鍵字，來快速搜尋
"官網"、"會員資料"、"部落格總覽"、"特殊商品"、"會員卡"...等相關內容。  
LINE 官方帳號 圖文選單有多種款式，可設定門市資訊、官網、會員資訊、最新優惠商品（任選折扣）  
*需先設定完成後，後續提醒相關設定才可以進行操作。  
詳細設定請至[ LINE@自動回覆商品訊息+1對1客服設定](https://www.cyberbiz.co/support/?p=855) 。  

[![LINE_application_description05](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description11.jpg)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description11.jpg)

* * *

五、LINE 官方帳號聊天機器人與聊天模式差異說明  
【聊天機器人】 : 可使用自動回應訊息、圖文選單及 Webhook 功能。  
完全系統化的方式回應訊息，無法進行人工客服，通常運用於無法隨時有人力即時回覆的廠商。  

【聊天模式】: 可使用聊天、自動回應訊息、圖文選單及智慧聊天功能  
一般運用於客服諮詢需人工判斷的廠商，也可搭配自動回應訊息解決非營運時間的制式回答。

* * *

六 - 1、串接 LINE Messaging API  
廠商可以透過 LINE 的 API 服務連接商家現有的官方帳號，實現各種系統與 LINE@
官方帳號做「串接」整合的動作，透過這樣的架構，讓商家的顧客服務有更多元的應用。  
詳細設定請至[ 串接MESSAGING API設定](https://www.cyberbiz.io/support/?p=706) 。  

* * *

六 - 2、LINE 官方帳號 訊息樣板通知  
Cyberbiz 提供  
【訂單相關】、【退貨相關】、【物流相關】、【顧客相關】、【定期訂單相關】等五種類別，當消費者執行設定的條件後會透過 LINE 官方帳號
自動回覆狀態訊息，可依照商家自身需求來做設定。  
詳細設定請至 [ LINE@訊息提醒樣板功能](https://www.cyberbiz.co/support/?p=728)。  

[![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description12-528x1024.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description12.png)[
](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description12.png)

* * *

七、LINE 官方帳號 會員條碼（使用 POS 系統客戶可使用）  
提供消費者在門市結帳時，直接使用 LINE 官方帳號 會員條碼進行會員認證。  
掃會員條碼登入會員資料，即可進行紅利、優惠券折抵功能。  
詳細設定請至 [ LINE@顯示會員條碼功能(POS專用功能)](https://www.cyberbiz.co/support/?p=748)。  
*需先設定完1對1客服(圖文選單)，才可開啟此功能。  

[![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description13.png)](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/LINE_application_description13.png)

* * *

