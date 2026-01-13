---
title: "PLUS用戶 - LINE直播申請開通流程與設定"
last_modified: ""
categories: [第三方平台整合>LINE相關設定,PLUS版適用]
tags: [PLUS版專用]
permalink: "https://www.cyberbiz.io/helpcenter/?p=7458"
id: "7458"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**功能說明：**  

* 您可以於品牌自身的LINE官方帳號上進行購物直播活動。讓消費者可在直播中(邊看邊買模式)導購至官網進行下單訂購。 

**操作目錄：**

* 直播申請開通與上線流程
* 後台設定
* 商品串接邏輯及相關設定提醒
* 更多資訊

注意事項:  

* LINE 直播供商家於 LINE 官方帳號中執行直播，現場且即時與官方帳號好友進行互動。  
詳情請見 [LINE LIVE](https://tw.linebiz.com/service/account-solutions/line-live/)。

* 消費者必須是官方帳號好友，已綁定官方帳號 LINE OA，方可進入直播間並下單。
* 確認已經擁有品牌LINE 官方帳號 (LINE OA = Official Account)。
* 確認已完成LINE 官方帳號認證(藍色盾牌，常簡稱藍盾)。 
* 一般帳號（灰色盾牌）-目前不開放申請直播功能
* 認證帳號（藍色盾牌）-開放申請直播功能 （相關申請流程請見 [LINE官方文件](https://tw.linebiz.com/column/line-lac-id-0418/)） 
* 企業帳號（綠色盾牌）-專案特殊帳號 （為LINE邀請制 謝絕一般申請) 
(若還未申請認證帳號，可以參考以下說明與直播同步申請： [文件](https://tw.linebiz.com/column/lac-verified/))

* 建議官方帳號好友數1000人以上 - 因為直播對象即是官方帳號好友，好友數會直接影響觀看成效。
* 建議每月直播4場以上 - 養成直播習慣，與好友培養觀看默契。
* 透過 LINE 直播導購的訂單可於「訂單」→「LINE OA訂單」查看。



## 📌 直播申請開通與上線流程

步驟流程

1. 若商家有興趣使用LINE購物直播功能。  
請填寫 [申請表單](https://forms.gle/KmBWNvvGggZR1PsYA) 申請直播資格開通。



2. 如申請確認，CYBERBIZ 將協助開啟後台串接，並請LINE核發參數 (需約30天)


3. 設定參數 : 請開啟後台小幫手權限，CYBERBIZ 會直接協助完成後台設定參數   
請至後台「管理中心」→「網站權限/續約管理」→「管理者列表」開啟設定



4. LINE官方會發信通知商家開通程序皆完成，才算正式開通，可以開始直播！  
LINE亦會引導商家報名直播後台教學課程



* * *

## 📌 後台設定


若您已收到CYBERBIZ後台參數信件(上方流程第10步)，請至後台完成回填儲存：  


1. 設定位置：左側欄選單「第三方整合」→「LINE購物設定」→ 頁面下半區塊「LINE OA導購」


2. 請填入CYBERBIZ提供之「SHOP_ID」以及「AUTHKEY」
[![後臺畫面](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定02.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定02.png)



* * *

## 📌 相關設定提醒及商品串接邏輯：



【設定提醒】 :  

商品必須符合以下三個條件才會成功出現在產品目錄  

[![公開](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定03-1.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定03-1.png)

1. 公開狀態。(如上圖)  

2. 上架狀態為已上架。(如上圖) 
3. 該商品標籤欄位不得設有「贈品」及「排除product feed」。 



【商品串接邏輯】 :  

商家於EC後台上架商品 → CYBERBIZ 系統自動產出產品目錄 → LINE同步產品目錄資訊 至 LINE直播後台 → 商家於直播後台搜尋商品加入直播
→ 進行直播導購  


1. CYBERBIZ 後台產品目錄固定於每日 4:45AM 及 4:45PM 兩個時段自動更新；  
LINE 則是固定於每日 5:00AM 同步產品目錄資訊到直播後台。



2. 如商家已過了 CYBERBIZ 自動更新目錄的時段，需要臨時修改商品資訊，請於修改商品資訊後，  
於「第三方整合」→「LINE購物設定」點擊「手動更新目錄」按鈕。  
*請注意此按鈕一個小時僅可點擊一次。


3. 因應上述提及的更新時間，請商家最晚務必1天前完成直播商品所有相關設定(不要直播當天才在EC後台上架商品，直播後台會搜尋不到商品喔) 


4. 商家於直播後台搜尋商品建議使用“Product ID”(LINE會簡稱為PID)進行搜尋最精準！  
知道商品的 Product ID 有以下2個方式：  


* Product ID 就是後台點開商品頁面的網址最後的數字(如圖範例)  
[![後臺畫面id](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定03.png)



* 匯出商品列表，將原本預設隱藏的A欄-商品id取消隱藏(如圖範例)。商品 id 即是 Product ID  
[![後臺畫面id](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定04.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE直播申請開通流程與設定04.png)



* * *



## 📌 更多資訊



想了解更多直播應用內容❓❓❓  
歡迎來下載直播攻略手冊❗❗❗

