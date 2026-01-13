---
title: "網站使用 Cookie 提示彈窗設定"
last_modified: ""
categories: [網站設定>語法教學,常見問題]
tags: []
permalink: "https://www.cyberbiz.io/support/?p=24351"
id: "24351"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/wp-主視覺bar-1024x321.png) ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/08/企業版.png) **功能說明：**  
· 為因應 GDPR 隱私權條款以及歐盟即Cookie法，除了要在網站新增隱私權政策頁面外，也必須主動告知使用者，該網站將使用 Cookie，並將會如何使用
Cookie。  
· 消費者進入網站後，需要跳出一個訊息視窗，提醒使用者該網站會使用 Cookie ，並徵求使用者同意。  
![Cookie提示彈窗設定](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/Cookie提示彈窗01.png)  
注意事項:  

* 此文件僅提供基礎設定，相關問題及進階設定請自行詢問貴司技術人員。

前往下方網站，並設定完1~5項後，複製程式碼至網站後台貼上  

Step1. 前往[“Create a cookie consent
banner”](https://www.websitepolicies.com/create/cookie-consent-banner)。  
· 選擇彈窗顯示位置/版面/文字內容/彈窗顏色等等。  
![Cookie提示彈窗設定](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/Cookie提示彈窗02.png)  
Step2. 複製程式碼。  
· 設定好上面的內容後，點擊展開程式碼欄位，並複製程式碼。  
![Cookie提示彈窗設定](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/Cookie提示彈窗03.png)  
Step3. 至指定樣板貼上程式碼。  
· 位置：外觀設置 → 樣板編輯器。  
· 至 theme.liquid，並將程式碼貼在 的上面，點擊儲存即可。  
![Cookie提示彈窗設定](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/Cookie提示彈窗04.png)  
· 如果您有使用快速到貨，請將程式碼也複製到 express_delivery.liquid 的 上面，並儲存。  
![Cookie提示彈窗設定](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/Cookie提示彈窗05.png)  

