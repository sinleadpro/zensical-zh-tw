---
title: 金流申請：PAYPAL
last_modified: ""
categories:
  - 網站設定>金物流設定
tags: []
permalink: https://www.cyberbiz.io/helpcenter/?p=2553
id: "2553"
---

# 設定 PayPal

串接 PayPal 金流，讓海外信用卡消費者於結帳時可使用 PayPal 支付。
{ .subtitle }

![](../../assets/images/ec-金物流-paypal.png){ .hero-page }

## PayPal 說明

### 注意事項

- PayPal 台灣商家僅能用於跨境交易，台灣境內無法使用。
- 若遇收款或金流問題，請聯絡 PayPal 客服或參考官方常見問答：
    
    - [PayPal 常見問答](https://www.paypal.com/tw/smarthelp/home)
    - [PayPal 客服中心](https://www.paypal.com/tw/smarthelp/contact-us)

**功能說明：**  

* 串接 PayPal 付款，持海外信用卡消費者於結帳時可選用 PayPal 進行支付。

**操作目錄：**

* PayPal 申請流程
* 如何找到 client ID 與 secret？

注意事項:  

1. 法規限制， PayPal 台灣商家僅能在跨境進行交易，不能於台灣境內使用，若您是台灣的賣家申請 PayPal 金流，只有國外信用卡可以使用信用卡付款。
2. 若有收款或是其他金流問題請洽 PayPal 客服，或參考相關常見問答。 
* 點我前往 [PayPal 常見問答](https://www.paypal.com/tw/smarthelp/home)
* 點我前往 [PayPal 客服中心](https://www.paypal.com/tw/smarthelp/contact-us)



## 📌 PayPal 申請流程



1. 若您沒有申請過 PayPal 金流服務，請先至 PayPal 官網註冊申請，點我前往 [PayPal 註冊頁面](https://www.paypal.com/tw/webapps/mpp/account-selection)。  
請點選使用 PayPal 接受交易款項。 ![PayPal1](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請01.png)



2. 此電子郵件地址為後續串接 CYBERBIZ 後台時所使用，請填寫常用的電子郵件。  
![PayPal2](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請02.png)



3. 密碼長度須超過8碼，且須含有英文大小寫以及數字。  
![PayPal3](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請03.png)



4. 填寫相關資料。  
![PayPal4](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請04.png)



5. 請依照公司狀態點選。  
![PayPal5](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請05.png)



6. 於產品或服務關鍵字輸入文字後即可出現相關選項，例如:服飾。  
![PayPal6](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請06.png)



7. 負責人相關資料填寫後提交即可完成申請，提交後須等待 PayPal 審核通過後才可進行後續串接。  
![PayPal7](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請07.png)



8. 收到 PayPal 審核通過後，  
請至 「CYBERBIZ 後台」→「 金物流」→「結帳頁&金物流設定」→找到 PayPal 的選項，  
將選項開啟後， 填入稍早申請所填寫的電子郵件至【Pay Pal帳號】，請特別留意填入時請勿帶有空格，以免無法順利啟用。  
*設定畫面分為 是否使用CYBERBIZ PAYMENTS。   
![PayPal8](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08.png)

[適用 : PLUS版、一般版(CYBERBIZ PAYMENTS)]

![PayPal8](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08-1.png)

[適用 : 一般版(未使用CYBERBIZ PAYMENTS)]

![PayPal8](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08-2.png)



9. 請特別留意，若是新增了金流選項，  
請設置完後至「金物流」→「 宅配運費設定」中的付款方式中  
將新增的付款方式勾起，如此才是完成完整設置。  

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/綠界金流串接15.png)

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/綠界金流串接16.png)

* * *



## 如何取得 PayPal Client ID 與 Secret

!!! tip "CYBERBIZ PAYMENTS 自動退款"
	開通 CYBERBIZ PAYMENTS 商家，可以在 PayPal 金流設定頁面中輸入 PayPal `Client ID` 與 `Secret` 啟用自動退款功能。

### 步驟

1. 登入 PayPal 帳號。
2. 點擊右上角「開發人員」 → 進入 [Developer Dashboard](https://developer.paypal.com/developer/applications)  
    ![點選開發人員](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay%E9%87%91%E6%B5%81%E7%94%B3%E8%AB%8B09.png)
    
3. 點選「App & Credentials」。  
    ![點選 App&Credentials](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay%E9%87%91%E6%B5%81%E7%94%B3%E8%AB%8B11.png)
    
4. 將右上角切換由 Sandbox → Live。
    
5. 點選您的 App（如尚未創建 → Create App）
    
6. 複製 Client ID 與 Secret，並填入 CYBERBIZ 後台：  
    **路徑**：「金物流」→「結帳頁 & 金物流設定」→「PayPal」  
    ![PayPal8](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay%E9%87%91%E6%B5%81%E7%94%B3%E8%AB%8B08-1.png)

## 後續步驟

<div class="grid cards" markdown>

- :lucide-banknote-arrow-down:{ .lg }   
  [__退貨退款__](一般退貨退款)     
  退貨退款操作。

- :lucide-circle-question-mark:{ .lg }   
  [__PayPal 官方 FAQ__](https://www.paypal.com/tw/cshelp/personal)  
  PayPal 官方彙整的常見問題。

</div>
