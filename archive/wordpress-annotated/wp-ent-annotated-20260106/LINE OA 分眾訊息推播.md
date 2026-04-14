【文件標題】LINE OA 分眾訊息推播
【適用版本】企業版, region_jp
【來源連結】https://www.cyberbiz.io/support/?p=25964
【章節路徑】LINE OA 分眾訊息推播

---

[圖片說明：適用站別]
[[圖片說明：台灣站]](https://www.cyberbiz.io/support/?page_id=2490)
[]() **功能說明：**

- 透過後台發送 LINE推播訊息給 LINE快速登入會員 或 LINE會員綁定官網會員
- 可發送文字訊息或是圖片訊息。
- 以顧客標籤分層推播顧客信息。
**操作目錄：**

- LINE OA 發送訊息
注意事項:

- 請先完成 LINE Messaging API 設定後再進行此項操作。
- 綁定LINE & 綁定LINE@都可以用 (LINE快速登入會員& LINE會員綁定官網會員)
- 透過 「LINE快速登入會員」 或 「LINE會員綁定官網會員」皆會在官網留下 UID，得以作為發送訊息的資料。但僅有 LINE OA好友(官方帳號)，才可以收到LINE OA訊息。
- LINE推播服務將在LINE OA產生費用，相關計費標準，可參考官方說明的[加購訊息價目表](https://tw.linebiz.com/service/account-solutions/line-official-account/)，手動推播訊息、自動傳送訂單通知訊息皆屬付費項目。 (僅有發送成功的訊息會被LINE收取訊息費。)
- 如果有存UID但是沒收到訊息，可能有幾個原因
1. 會員不是LINE OA 好友(官方帳號)
2. 你的LINE OA被會員封鎖。

📌 LINE OA 發送訊息

1. 設定好 Messaging API功能，詳情請至 [LINE Messaging API 設定](https://www.cyberbiz.io/support/?p=706) 文件設定。

2. 使用 CYBERBIZ LINE 功能，需商家請顧客透過 LINE OA官方帳號，進行 [LINE OA 官方帳號 綁定 官網會員設定](https://www.cyberbiz.io/support/?p=32679)

3. 進入 CYBERBIZ 後台，設定 LINE OA 訊息。
【後台路徑】訊息推播→「LINE OA發送訊息」

【顧客標籤】:
設定標籤後發送給符合篩選標籤的顧客。(訊息僅會發送給完成 LINE快速登入會員 或 LINE會員綁定官網會員 的顧客)

【發送類型】:
文字訊息 : 支援換行及emoji，不限制字元數，點擊送出，立即排程發送。
圖片訊息 : 上傳單張圖片，圖片尺寸建議：1MB，1000x1000px，可上傳 JPG/PNG/JPEG/GIF 格式，並設定圖片導轉的連結。
*顧客標籤為必填。
*文字/圖文訊息，一次僅能選擇一種訊息模式。

文字 [[圖片說明：文字訊息]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-傳送訊息設定01.png) 圖片 [[圖片說明：圖片訊息]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-傳送訊息設定02.png)

4. 發送後，顧客即可收到 LINE 推播訊息。(圖片訊息範例)
[[圖片說明：推播畫面]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-傳送訊息設定03.png)