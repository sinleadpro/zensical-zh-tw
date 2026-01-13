---
title: "LINE 快速登入 : 取得會員手機號碼"
last_modified: ""
categories: [第三方平台整合>LINE相關設定,PLUS版適用,常見問題]
tags: []
permalink: "https://www.cyberbiz.io/helpcenter/?p=6674"
id: "6674"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/一般版3.png)
![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**功能說明：**  

* 此功能將協助商家在LINE快速登入時取得會員手機號碼授權，建立/更新會員資料。 

**操作目錄：**

1. 條件設定
2. LINE 後台資格確認
3. 會員帳號情境說明

注意事項:  

* 請確認您的 LINE Provider 已完成認證為 LINE Certified Provider。
* 請確認您的 LINE官方帳號 已完成認證為藍盾或綠盾。
* 請確認您已完成後台 LINE登入串接。
* 此功能不包含取得功能設定完成前，已進行過 LINE快速登入的會員手機號碼。



## 📌 條件設定



1. 完成後台 [LINE 快速登入](https://www.cyberbiz.io/helpcenter/?p=865) 功能。


2. LINE Provider 認證 
* 已完成認證為LINE Certified Provider。
* 若您尚未擁有LINE Certified Provider的資格，可洽詢您配合的 [LINE合作夥伴](https://tw.linebiz.com/partner/sales-partner/)，或依照下方文件流程，進行認證申請 [申請檔案下載](https://drive.google.com/file/d/1Tm15QlpkfYWUrQbSGESD3ggsnP4qJNC2/view)。 
*按照LINE規範，一間公司僅能申請一個 Certified Provider！若有重覆將無法申請通過


3. LINE 官方帳號認證  
官方帳號已完成認證為藍盾或綠盾。[(LINE認證官方帳號說明文件)](https://tw.linebiz.com/column/line-lac-id-0418/)



![](https://www.cyberbiz.io/support/wp-content/uploads/fountain-pen.png)

* 若上方 3 個條件，商家皆已符合條件，並且確認 LINE 後台畫面資格無誤，即可使用該功能。

* * *

## 📌 LINE 後台資格確認



1. 進入您的 [LINE Provider 首頁](https://developers.line.biz/en/)，確認您的 Provider 已為 LINE Certified Provider。  
[![確認provider是否有綠勾](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼01.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼01.png)



2. 點選您與 在CYBERBIZ 後台串接的LINE Login Channel。  
[![點選login](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼02.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼02.png)



3. 進入 Basic Settings 頁籤，移至「Permissions」設定位置，確認 Permissions 包含「OC_PHONE_NUMBER」  

[![basic](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼03.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼03.png)

[![確認 oc_phone_number](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼04.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼04.png)



* * *



## 📌 會員帳號情境說明



手機號碼已在 EC 官網註冊過會員  
*一般的 LINE快速登入僅會抓取會員 Email，使用該功能後，會先進行[手機]比對，再比對[Email] 


[![已註冊會員](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼05.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼05.png)  


手機號碼沒有在 EC 官網註冊過會員  
*一般的 LINE快速登入僅會抓取會員 Email，使用該功能後，會先進行[手機]比對，再比對[Email] 


[![未註冊會員](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼06.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/LINE-快速登入取得會員手機號碼06.png)

