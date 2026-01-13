---
title: "於訂單成立頁和付款完成頁新增加入 LINE 好友連結"
last_modified: ""
categories: [第三方平台整合>LINE相關設定,PLUS版適用,網站設定>前台介面]
tags: []
permalink: "https://www.cyberbiz.io/helpcenter/?p=10871"
id: "10871"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版1.png)
**功能說明：**  

* 商家可在**訂單成立頁、訂單付款完成頁** 新增加入 LINE 好友連結、圖片。

**操作目錄：**

* 加入 LINE 好友連結

注意事項:  

* 請先至後台向 CYBERBIZ 客服申請開通。
* 功能開通後僅套用於已發布的版型上，若更換版型請至後台向 CYBERBIZ 客服重新申請開通。
* 此功能可用於拖拉版型。
* 若有更改需求，敬請委託自家工程師，**CYBERBIZ 不提供語法教學與代碼撰寫服務** ，敬請見諒。
* CYBERBIZ 對於商家修改程式碼後所產生的任何系統問題、錯誤或不可預見的狀況，恕不承擔責任。若商家選擇更動程式碼，將視為自行承擔所有風險及後果。請商家謹慎操作。
* 如有恢復樣版的需求，可參考 [恢復樣版編輯器](https://www.cyberbiz.io/helpcenter/?p=3474)。



## 📌 加入 LINE 好友連結



1. 請先至後台向 CYBERBIZ 客服申請開通。


2. 開通完成後，可至 CSS/HTML 編輯器中搜尋**order_done_extra_content.liquid** 。  

後台路徑 : 「網站外觀」→「套版主題管理」→「選擇操作」→「CSS/HTML編輯器」  
[![推播設定](https://www.cyberbiz.io/support/wp-content/uploads/LINE加入好友推播-訂單成立付款完成頁05.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE加入好友推播-訂單成立付款完成頁05.png)



3. 圖片中程式碼僅供參考，請商家工程師自行撰寫程式碼。若想區分「訂單成立頁」與「付款完成頁」的內容，請自行修改代碼。   



程式碼備註：  

{% if page_title == '訂單成立' %} 
訂單成立的內容... 
{% else %} 付款完成的內容... 
{% endif %}




[![程式碼](https://www.cyberbiz.io/support/wp-content/uploads/LINE加入好友推播-訂單成立付款完成頁02.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE加入好友推播-訂單成立付款完成頁02.png)  



4. 此為 CYBERBIZ 提供的範例，並非完成步驟 3 即可變成此畫面，請商家依需求設計畫面，恕 CYBERBIZ 不提供 HTML/CSS 語法教學與代碼撰寫。  
[![前台畫面](https://www.cyberbiz.io/support/wp-content/uploads/LINE加入好友推播-訂單成立付款完成頁03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE加入好友推播-訂單成立付款完成頁03.png)  

