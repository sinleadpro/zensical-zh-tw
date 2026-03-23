---
title: "PLUS版專用功能 - 商品評論"
last_modified: ""
categories: [PLUS版適用]
tags: [PLUS版專用]
permalink: "https://www.cyberbiz.io/helpcenter/?p=7894"
id: "7894"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**功能說明：**  

* 顧客評論是顧客購買商品前強大的誘因，從其他客戶獲得真實意見。
* 評論可使您的品牌變得更值得信賴。

**操作目錄：**

* 設定商品評論
* 顧客發表商品評論
* 商家審核商品評論
* 隱藏商品評論功能

注意事項:  

* 顧客皆須登入會員才可進行留言。
* 需使用商品評論功能請至 CYBERBIZ 後台洽客服申請開通。
* 若自行移除樣版編輯器，需自行保留程式碼，CYBERBIZ 不提供恢復功能等操作。
* FB分享功能 : 需至「第三方整合」→「臉書Facebook設定」→「設定 應用程式ID (APP ID) 及 應用程式密鑰 (App Secret)」填寫完畢，才可以使用。



## 設定商品評論

![](https://www.cyberbiz.io/support/wp-content/uploads/商品評論00.png)  

後台路徑 :「網站外觀」→「管理商品評論」  


1. 使用商品評論功能請至 CYBERBIZ 後台洽客服申請開通。


2. 可至後台設定 商品評論相關功能。  
【預設審核留言】:  顧客留言後商家是否需要審核留言。  
【預設隱藏部分姓名】:  顧客留言是否部分隱藏姓名。  
【Google reCAPTCHA】 :  可依照 [建立 reCAPTCHA
安全驗證機制](https://www.cyberbiz.io/helpcenter/?p=12371) 進行設定。  
【審核後贈送 紅利點數】 :  顧客評論，商家審核後即贈送紅利點數。  
![商品評論設定](https://www.cyberbiz.io/support/wp-content/uploads/商品評論01.png)



3. 留言板列表   
所有商品皆可在此細部設定，按下「檢視」可進行編輯。  
![商品評論設定02](https://www.cyberbiz.io/support/wp-content/uploads/商品評論02.png)



4. 可各別設定，並可刪除商品評論。  
![商品評論設定03](https://www.cyberbiz.io/support/wp-content/uploads/商品評論03.png)

* * *

## 顧客發表商品評論

* 顧客點選「發表評論」，跳出彈跳視窗即可填寫評論。  
(顧客需登入才可評論)  
![發表商品](https://www.cyberbiz.io/support/wp-content/uploads/商品評論04.png)

* * *



## 商家審核商品評論


後台路徑 : 「會員」→「商品待審核評論」  


1. 點選待審核評論，並按下「審核」即可審核成功，也可進行「刪除」動作。


2. 點選「編輯」，商家可編輯該評論部分內容。

![審核評論](https://www.cyberbiz.io/support/wp-content/uploads/商品評論05.png)

![審核評論-2](https://www.cyberbiz.io/support/wp-content/uploads/商品評論06.png)

* * *



## 隱藏商品評論功能



說明 :  
若暫時不想顯示商品評論功能，可先透過程式碼編輯將其隱藏起來，  
若商家自行刪除程式碼，CYBERBIZ不提供協助恢復功能動作。




【拖拉版型】

後台路徑 : 「網站外觀」→ 「套版主題管理」→「選擇操作 : CSS/HTML編輯器」→「區塊 」  


* 點選「新增區塊」，直接輸入 board_comments.liquid。  
![隱藏商品評論-拖拉](https://www.cyberbiz.io/support/wp-content/uploads/商品評論08.png)

* 新增區塊後，右方留空即可。   
*若要恢復商品評論功能，刪除此區塊即可。  
![隱藏商品評論-拖拉2](https://www.cyberbiz.io/support/wp-content/uploads/商品評論09.png)

【一般版型】

後台路徑 : 「網站外觀」→「套版主題管理」→「選擇操作 : CSS/HTML編輯器」→「product.liquid」  


* 找到「shop.plugins.board_comments」，將整段標示起來即可隱藏起來。(請看圖片範例)  
![隱藏商品評論](https://www.cyberbiz.io/support/wp-content/uploads/商品評論07.png)

