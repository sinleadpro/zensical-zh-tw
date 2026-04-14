【文件標題】PLUS版功能 - LINE OA訊息提醒樣板設定
【適用版本】進階PLUS版, 專業PLUS版, 高手PLUS版
【來源連結】https://www.cyberbiz.io/helpcenter/?p=8156
【章節路徑】PLUS版功能 - LINE OA訊息提醒樣板設定

---

**功能說明：**

- CYBERBIZ 設定 LINE推播，開啟「訂單」、「物流」、「顧客」、「定期訂單」樣板，在指定情境下自動回覆顧客相關的訊息。

**操作目錄：**

- 訊息樣板設定
- 支援訊息類別

注意事項:

- LINE OA 訊息會依LINE官方訊息方案費用計費 詳細收費請參考 [相關連結](https://tw.linebiz.com/column/budget-auto-count/)。
- 此功能需先串接好 Messaging API 功能，前往 [相關文件](https://www.cyberbiz.io/support/?p=706)。
- 使用此功能前需請商家先進行 LINE OA 綁定官網會員 ，才可使用，前往 [相關文件](https://www.cyberbiz.io/support/?p=32679)。
- 綁定LINE & 綁定LINE@都可以用 (LINE快速登入會員& LINE會員綁定官網會員)
- 透過 「LINE快速登入會員」 或 「LINE會員綁定官網會員」皆會在官網留下 UID，得以作為發送訊息的資料。但僅有 LINE OA好友(官方帳號)，才可以收到LINE OA訊息。


---

## 訊息樣板設定

1. 設定好 Messaging API功能，詳情請至 [LINE Messaging API](https://www.cyberbiz.io/support/?p=706) 文件設定。

2. 進入 CYBERBIZ 後台 ，可設定及開關相關功能。
【後台路徑】訊息推播→「LINE OA 通知樣板」 [[圖片說明：訊息提醒樣版功能01]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-訊息提醒樣板功能01.png)

3. 點選欲啟用的提醒樣板。
【Flex Message 樣板】

- 設定是否啟用 : ON/OFF。
- 通知類型 : Flex Message 樣板/純文字。
- 文字訊息 : 公版內容，可自行新增刪減內容。
*若需更改內文，請注意 {{ }} 中的內容，不要自行更動。(為自動抓取 CYBERBIZ 設定資料)
**支援所有【訂單事件】&【物流事件】
[[圖片說明：訊息提醒樣版功能02]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-訊息提醒樣板功能02.png)

【純文字】 : 設定方法同上

[[圖片說明：訊息提醒樣版功能02]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-訊息提醒樣板功能03.png)

- * *


---

## 📌 支援訊息類別

訊息類別 | 發送時機
---|---
**貨物發送提醒** | 出貨時發送
(支援使用系統託運單出貨之訂單)
(若您不使用系統託運單出貨，恕無法追蹤貨態)
**貨物到店提醒** | 貨物透過非 7-11 物流，寄送至「超商」時發送
(包含官網萊爾富、全家、黑貓快速到店物流)
(包含倉儲所有超商物流)
**7-11 貨物到店提醒** | 貨物透過7-11 物流，寄送至「超商」時發送
(包含官網7-11物流)
**貨物到門市提醒** | 貨物到達「商家自己的門市」時發送
**定期訂單確認提醒** | 會員成立第一筆訂單時發送(母訂單)
**定期訂單出貨提醒** | 每筆訂單成立時發送(子訂單)