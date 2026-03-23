【文件標題】金流申請：PAYPAL
【適用版本】進階, 進階PLUS版, 專業, 專業PLUS版, 高手, 高手PLUS版
【來源連結】https://www.cyberbiz.io/helpcenter/?p=2553
【章節路徑】金流申請：PAYPAL

---

**功能說明：**

- 串接 PayPal 付款，持海外信用卡消費者於結帳時可選用 PayPal 進行支付。

**操作目錄：**

- PayPal 申請流程
- 如何找到 client ID 與 secret？

注意事項:

1. 法規限制， PayPal 台灣商家僅能在跨境進行交易，不能於台灣境內使用，若您是台灣的賣家申請 PayPal 金流，只有國外信用卡可以使用信用卡付款。
2. 若有收款或是其他金流問題請洽 PayPal 客服，或參考相關常見問答。
- 點我前往 [PayPal 常見問答](https://www.paypal.com/tw/smarthelp/home)
- 點我前往 [PayPal 客服中心](https://www.paypal.com/tw/smarthelp/contact-us)


---

## 📌 PayPal 申請流程

1. 若您沒有申請過 PayPal 金流服務，請先至 PayPal 官網註冊申請，點我前往 [PayPal 註冊頁面](https://www.paypal.com/tw/webapps/mpp/account-selection)。
請點選使用 PayPal 接受交易款項。 [[圖片說明：PayPal1]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請01.png)

2. 此電子郵件地址為後續串接 CYBERBIZ 後台時所使用，請填寫常用的電子郵件。
[[圖片說明：PayPal2]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請02.png)

3. 密碼長度須超過8碼，且須含有英文大小寫以及數字。
[[圖片說明：PayPal3]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請03.png)

4. 填寫相關資料。
[[圖片說明：PayPal4]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請04.png)

5. 請依照公司狀態點選。
[[圖片說明：PayPal5]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請05.png)

6. 於產品或服務關鍵字輸入文字後即可出現相關選項，例如:服飾。
[[圖片說明：PayPal6]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請06.png)

7. 負責人相關資料填寫後提交即可完成申請，提交後須等待 PayPal 審核通過後才可進行後續串接。
[[圖片說明：PayPal7]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請07.png)

8. 收到 PayPal 審核通過後，
請至 「CYBERBIZ 後台」→「 金物流」→「結帳頁&金物流設定」→找到 PayPal 的選項，
將選項開啟後， 填入稍早申請所填寫的電子郵件至【Pay Pal帳號】，請特別留意填入時請勿帶有空格，以免無法順利啟用。
*設定畫面分為 是否使用CYBERBIZ PAYMENTS。
[[圖片說明：PayPal8]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08.png)

[適用 : PLUS版、一般版(CYBERBIZ PAYMENTS)]

[[圖片說明：PayPal8]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08-1.png)

[適用 : 一般版(未使用CYBERBIZ PAYMENTS)]

[[圖片說明：PayPal8]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08-2.png)

9. 請特別留意，若是新增了金流選項，
請設置完後至「金物流」→「 宅配運費設定」中的付款方式中
將新增的付款方式勾起，如此才是完成完整設置。

[[圖片說明：綠界金流串接15]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/綠界金流串接15.png)

[[圖片說明：綠界金流串接16]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/綠界金流串接16.png)

- * *


---

## 📌 如何找到 client ID 與 secret？

系統需要您提供您的 PayPal client ID 與 secret，才能幫您執行退款。
適用 : PLUS版、一般版(CYBERBIZ PAYMENTS)
您可以透過以下步驟找到您的 PayPal client ID 與 secret：

1. 進入您的 PayPal 帳號。
2. 點擊右上方「開發人員」
[[圖片說明：點選開發人員]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請09.png)

3. 點擊「Developer Dashboard」
[[圖片說明：點選DD]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請10.png)

4. 點擊「App & Credentials」
[[圖片說明：點選 App&Credentials]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請11.png)

5. 將右上角的開關由「Sandbox」轉為「Live」，
點擊您的 App 後，即可看到 client ID 與 secret（若您還沒創建 app，須先點擊「Create App」創建一個 app）。
[[圖片說明：paypay金流申請12]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請12.png)

6. 進入 CYBERBIZ 後台填寫 【Client ID】 和 【Secret】
【後台路徑】金物流→「結帳頁 & 金物流設定」→「金流設定」→「PayPal」
[[圖片說明：PayPal8]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08.png)

[適用 : PLUS版、一般版(CYBERBIZ PAYMENTS)]

[[圖片說明：PayPal8]](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PayPay金流申請08-1.png)