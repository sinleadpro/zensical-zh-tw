【文件標題】顧客可留言頁面建立 reCAPTCHA 安全驗證機制
【適用版本】進階PLUS版, 專業PLUS版, 高手PLUS版
【來源連結】https://www.cyberbiz.io/helpcenter/?p=12371
【章節路徑】顧客可留言頁面建立 reCAPTCHA 安全驗證機制

---

**看了此文件，您可以：**

- **完成 Google reCAPTCHA 申請流程，** 順利取得金鑰並填入後台。
- **啟用商品評論區與聯絡我們頁面的 reCAPTCHA 驗證，** 保護官網免受機器人與垃圾留言攻擊。

**操作目錄：**

- 為什麼需要設定 reCAPTCHA
- 如何申請 Google reCAPTCHA
- 如何將 reCAPTCHA 金鑰綁定商品評論
- 如何將 reCAPTCHA 金鑰綁定聯絡我們
- 綁定官網注意事項

注意事項:

- Google reCAPTCHA為第三方服務，詳細服務內容與最新資訊可洽 [Google reCAPTCHA 網站](https://developers.google.com/recaptcha?hl=zh-tw)。
- **此功能僅限拖拉版型網站使用。**

📌 為什麼需要設定 reCAPTCHA
官網部分頁面可供顧客留言，**為防止此類頁面遭受機器人攻擊與垃圾罐頭訊息，系統支援 Google reCAPTCHA 驗證機制**
，可有效識別非人類操作，增加防護層級。

官網可留言頁面：

- 商品詳情頁中的商品評論區
[[圖片說明：商品評論區建立 reCAPTCHA 安全驗證機制]](https://www.cyberbiz.io/support/wp-content/uploads/商品評論00.png)

- 聯絡我們頁面
[[圖片說明：商品評論區建立 reCAPTCHA 安全驗證機制]](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA01.png)

商家若想保護以上頁面免受機器人惡意攻擊，請依下方設定 Google reCAPTCHA。

- * *

📌 如何申請 Google reCAPTCHA

1. 進入 [reCAPTCHA admin console](https://www.google.com/recaptcha/admin/)，登入 Google 帳號，輸入以下欄位資訊：
- 「標籤」：依需求命名此 reCAPTCHA。
- 「reCAPTCHA 類型」：選擇「驗證問題」，選擇「隱形 reCAPTCHA 標記」。
- 「網域」：輸入官網網址。
- **請不要填入網址前綴`https://` 與後綴 `/...`**
- 範例網址：`https://_demo1234.cyberbiz.co_ /zh-TW`
- 請填入：` _demo1234.cyberbiz.co_`
- 「Google Cloud Platform」：依需求選擇專案。
[[圖片說明：商品評論區建立 reCAPTCHA 安全驗證機制]](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA02.png)

2. 點擊「提交」，取得 Google reCAPTCHA 金鑰。
[[圖片說明：商品評論區建立 reCAPTCHA 安全驗證機制]](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA03.png)

3. 請繼續將 Google reCAPTCHA 金鑰綁定官網。

- * *

📌 如何將 reCAPTCHA 金鑰綁定商品評論
【後台路徑】網站外觀→「管理商品評論」

1. 開啟「Google reCAPTCHA」。
2. 「reCAPTCHA sitekey」：將 Google reCAPTCHA「網站金鑰」填入。
3. 「reCAPTCHA secretkey」：將 Google reCAPTCHA「密鑰」填入。

[[圖片說明：商品評論區建立 reCAPTCHA 安全驗證機制]](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA04.png)

- 商品評論功能供企業版、PLUS 版商家使用，如有使用需求，請洽客服開通此功能。詳細設定可參考 [商品評論功能](https://www.cyberbiz.io/helpcenter/?p=7894)。

- * *

📌 如何將 reCAPTCHA 金鑰綁定聯絡我們
【後台路徑】會員→「顧客回饋&建議」

1. 開啟「啟動機器人阻擋」。
2. 「sitekey」：將 Google reCAPTCHA「網站金鑰」填入。
3. 「secret key」：將 Google reCAPTCHA「密鑰」填入。

[[圖片說明：可留言頁面建立 reCAPTCHA 安全驗證機制]](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-會員-顧客回饋建議-設定reCAPTCHA01.png)

- * *

📌 綁定官網注意事項

- 一組 Google reCAPTCHA 帳號可綁定多個網域，**您可使用同一組密鑰綁定商品評論與聯絡我們頁面** 。
- Google reCAPTCHA 有免費用量配額，達到免費用量上限前，Google 會透過電子郵件通知商家。若超出免費用量，顧客將無法進行留言，請自行向 Google 升級方案。詳情請洽 [reCAPTCHA-配額與限制](https://cloud.google.com/recaptcha/quotas?hl=zh-tw)。
- 請確保金鑰填寫正確，否則留言功能無法使用。如有錯誤訊息，請檢查金鑰是否填寫無誤。
[[圖片說明：可留言頁面建立 reCAPTCHA 安全驗證機制]](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)