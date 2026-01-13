---
title: "網域設定 - HiNet"
last_modified: ""
categories: [網站設定>網域設定]
tags: []
permalink: "https://www.cyberbiz.io/helpcenter/?p=314"
id: "314"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/一般版3.png) **功能說明：**  

* 文件適用網域註冊於 Hinet，且 DNS 由其進行代管。

**操作目錄：**

* CNAME 設定
* 轉址設定

注意事項:  

* 完成或異動DNS代管設定。約24小時內生效 (約1小時之後，就可以在網站後填入網域囉～)   
若有其他網域問題，  
請洽： HiNet網域名稱服務小組  
Fax:02-3343-6809  
HiNet網域名稱服務小組專線 Tel:0800080365。



## CNAME 設定

1. 輸入網域名稱及密碼，登入HiNet。  
(請注意網域名稱 . 後面需額外選擇)  
[![hinet登入畫面](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet01.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet01.png)



2. 點擊 「HiNet DNS代管」的「更新 DNS 紀錄」。  
[![hinet dns紀錄](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet02.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet02.png)



3. 同意「同意條款聲明」。  
[![同意條款聲明](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet03.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet03.png)



4. 先將【紀錄 A】類型刪除，並 新增一列，填寫後按下「送出資料」  
【紀錄類型】 : CNAME  
【主機名稱/別名】 : www  
【 IP/主機名稱】 : 填入您在CYBERBIZ 的網址(例 : xxx.cyberbiz.co)。  
**請注意！** 網址後請不要加「.」。  
[![cname設定](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet04.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet04.png)



5. CNAME 設定完成。  
[![cname設定完成](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet05.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet05.png)





* * *

## 轉址設定

1. 點擊 「轉址服務」的「設定轉址」。   
[![轉址設定](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet06.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet06.png)



2. 進入轉址設定，完成設定後按「送出資料」  
【網頁標題】: 輸入網頁標題。(自訂)  
【來源網址】: 留空。  
【目的網址】: 輸入 CNAME 設定的網址。(可看 CNAME 第5步驟的 主機名稱/別名)  
【網址列顯示】: 選擇 目的網址。  
[![轉址設定](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet07.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet07.png)



3. 轉址設定完成。  
[![轉址設定完成。](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet08.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet08.png)



4. 回到「轉址列表」設定畫面，將下方「說明」的 主機IP 號碼複製起來。  
[![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet09.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet09.png)



5. 回到「DNS代管」→「更新DNS紀錄」頁面，點選「新增一列」，  
【紀錄類型】: A  
【IP/主機名稱】 : 填入剛剛複製的 主機IP。  
[![填入IP](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet10.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet10.png)



6. 設定完成後，則完成 HiNet 。   
[![完成設定](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet11.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet11.png)



7. 進入 CYBERBIZ 後台，新增設定完的 www 網域。(例 : www.網域名稱.com)，並點選「總是將顧客重新導向到這裡」。  
後台路徑 : 「管理中心」→「網域管理」  
[![完成設定](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet12.png)](https://www.cyberbiz.io/helpcenter/wp-content/uploads/網域設定-HiNet12.png)



