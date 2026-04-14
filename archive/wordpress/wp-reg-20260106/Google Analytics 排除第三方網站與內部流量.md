---
title: "Google Analytics 排除第三方網站與內部流量"
last_modified: ""
categories: [第三方平台整合>Google相關設定,PLUS版適用]
tags: [GA,GOOGLE]
permalink: "https://www.cyberbiz.io/helpcenter/?p=6791"
id: "6791"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/一般版3.png)
![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**功能說明：**  

* 為了讓您在 Google Analytics 4（GA4）中獲得更準確的數據，建議您排除來自公司內部的流量，以及結帳流程中不適用的第三方網站來源，以避免影響轉換分析與流量評估。

**操作目錄：**

1. GA4 代碼設定
2. 定義與排除內部流量
3. 列出不適用的參照連結網址

注意事項:  

* 因 Google Analytics(GA3) 將在  2023 年 7 月 1 日停止更新資料，此篇教學文件為 GA4 設定教學。
* 詳細相關設定、疑問請至 [Analytics(分析)說明](https://support.google.com/analytics/?hl=zh-Hant#topic=10737980)。



## 📌 GA4 代碼設定


後台路徑 : 「管理」→「資源設定」→「資料收集和修改」→「資料串流」→ 點選您的串流  


1. 進入 GA4 點進您後台的資料串流。  
![點進串流頁](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-：串接教學11.png)



2. 點選進行代碼設定。  
![進行代碼設定](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除02.png)



3. 在設定點開「全部顯示」。  
![全部顯示](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除03.png)



4. 即可看到 GA4 相關功能，以下簡單說明兩種設定，商家可依需求操作。  

📍定義內部流程  
📍列出不適用的參照連結網址  
![設定](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除04.png)





* * *

## 📍 定義與排除內部流量


後台路徑 :  「管理」→「資料設定」→「資料收集和修改」→「資料串流」→ 點選您的串流 →「進行代碼設定」→「定義內部流程」  


說明 :  
內部流量是指來自公司內部網路的使用者，例如開發、客服或行銷人員在使用官網時所產生的瀏覽行為。這類流量通常來自固定的 IP 位址，可透過 GA4
排除設定，避免干擾實際的訪客分析。  
如要篩除內部流量，請先建立規則，定義代表內部流量的 IP 位址或 IP 位址範圍。 詳細說明可至
[Analytics(分析)說明](https://support.google.com/analytics/answer/10104470?hl=zh-Hant) 查看。




1. 點進「定義內部流量」，並點選「建立」。  
![定義內部流量](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除05.png)



2. 設定「規則名稱」、「IP 位址」，可同時新增多個 IP位址。  
![進行IP設定](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除06.png)



3. 定義好內部流量後，還需要透過 資料篩選器 排除內部流量。  

後台路徑 : 「管理」→「資源設定」→「資料收集和修改」→「資料篩選器」→ 預設好的 Internal Traffic  
![設定篩選器](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除07.png)



4. 確認以下資訊後按下「儲存」  
【篩選器作業】: 排除  
【篩選器狀態】: 有效  
![編輯篩選器](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除08.png)



5. 點選「啟用篩選器」，排除內部流量設定即完成。   
![確認啟用篩選器](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除09.png)





* * *

## 📍 列出不適用的參照連結網址


後台路徑 :  
「管理」→「資源設定」→「資料收集和修改」→「資料串流」→ 點選您的串流 →「進行代碼設定」→「列出不適用的參照連結網址」  


說明 :  
若您的網站在結帳流程中使用第三方金物流服務（如綠界、藍新、超商地圖等），顧客在付款或配送選擇時會被導向這些外部頁面。這些中介頁面常會被 GA4
判斷為新的參照來源，並計算為一個工作階段，導致轉換來源分析不準確。


![定義內部流量](https://www.cyberbiz.io/support/wp-content/uploads/Google-Analytics-第三方金物流-流量排除10.png) 分類 | 第三方 | 連結  
---|---|---  
金流 | CYBERBIZPAY | cyberbizpay.com  
金流 | 綠界 | pay.ecpay.com.tw、payment.ecpay.com.tw  
金流 | 第三方支付 | web-pay.line.me、onlinepay.jkopay.com  
金流 | 藍新 | core.newebpay.com   
物流 | 7-11 | ec.shopping7.com.tw、emap.pcsc.com.tw   
物流 | 全家 | mfme.map.com.tw、mfme2.map.com.tw   
物流 | 萊爾富 | ecmap.hilife.com.tw  
物流 | 黑貓宅到店 | appservice.ezcat.com.tw 

