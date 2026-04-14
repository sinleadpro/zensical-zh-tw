【文件標題】PLUS版功能 - 自訂擴充服務 : 串接API/Webhook
【適用版本】進階PLUS版, 專業PLUS版, 高手PLUS版
【來源連結】https://www.cyberbiz.io/helpcenter/?p=7875
【章節路徑】PLUS版功能 - 自訂擴充服務 : 串接API/Webhook

---

**功能說明：**

- 電商系統商後台提供商家自訂擴充服務，支援 API 與 Webhook 串接功能，讓使用者輕鬆整合外部資源，實現更彈性、個人化的商務應用。

**操作目錄：**

- API、Webhook 說明
- 後台建立自訂應用程式
- API scope
- API 包含哪些資料格式可以怎麼查？
- 如何用 token 串接 API 取得資料？
- Webhook 設定
- 網站權限設定

注意事項:

- API及Webhook串接，僅提供給企業版、PLUS版選配API的客戶。
- 串接 API及Webhook皆須有工程人員來完成程式串接設定，CYBERBIZ 不提供技術服務，請廠商評估後再操作。
- 若有需要開通請透過系統客服提出需求。
- 限制補充：
1. 每秒至多 5 個 Request
2. 每個請求上限為 2 MB (測試帳號 apidemo 上限為 2 KB)


---

## 📌 API、Webhook 說明

CYBERBIZ 提供客戶免費的 API、Webhook 服務
**【API說明】**
當貴公司想要從我們伺服器取得、建立、更新、刪除以上四種系統資訊，皆可讓其自動化相互串聯執行，是一種雙向的資訊拋接功能。

**【Webhook說明】**
Webhook就像是訂閱資訊一樣，由我們提供您鎖定的資訊到您一個您所設定的網址，它將總是即時提供最新系統資訊給您以利後續執行判斷。

- * *


---

## 📌 後台建立自訂應用程式

【後台路徑】APP MARKET→「我的擴充服務」

1. 切到「自訂」的分頁，點擊「建立自訂應用程式」
[[圖片說明：新增頁面]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook01.png)

2. 設定應用程式的名稱跟 API scope （API scope 參考 API scope），
scope 裡面的 API 分別有哪些資料可以參考 🖇️建立自訂擴充服務串接 API/webhook
[[圖片說明：api scopes 設定]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook02.png)

3. 到設定頁中設定 Webhook events。
[[圖片說明：webhook]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook03.png)

4. 設定完成後，就可以用後台提供的 APP Secret & API Token 進行 API 的串接以及 Webhook 的接收了。
[[圖片說明：webhook]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook04.png)

- * *


---

## 📌 API scope

scope 與支援 API

- read scope 可使用 HTTP 方法為 Get 的 API
- write scope 可使用 HTTP 方法為 Post、Put、Delete 的 API

參考 API 文件內的 API 類型，例如 `read_customers` 可使用 `customers` 類型底下所有 Get
API（文件如何使用可以參考 API 包含哪些資料格式可以怎麼查？）

Scope| zh-TW| en| description
---|---|---|---
public| 公開資料| public| GET https://app-store-api.cyberbiz.io/v2/product_feedsapp 預設會有的 scope
read_products| 讀取商品| read products| read :
products, custom_collections, smart_collections, inventory_sync_groups
write_products| 修改商品| write products| write :
products, custom_collections, smart_collections, inventory_sync_groups
read_customers| 讀取會員| read customers| read :
orders,
periodic_orders,
einvoices
write_customers| 修改商品| write customers| write :
orders,
periodic_orders,
einvoices
read_orders| 讀取會員| read orders| read :
orders,
periodic_orders,
einvoices
write_orders| 修改商品| write orders| write :
orders,
periodic_orders,
einvoices
read_affiliates| 讀取分潤訂單| read affiliates| [GET] /v2/affiliate_vendor_orders
read_discounts| 讀取促銷| read discounts| read :
discounts , add_buy_collections , shop_coupons , special_collections ,
vip_groups
write_discounts| 修改促銷| write discounts| write :
discounts , add_buy_collections , shop_coupons , special_collections ,
vip_groups
read_pos| 讀取 POS| read POS| read :
pos_shops , stock_adjustments , stock_invoices , stock_receipts ,
stock_requisitions
write_pos| 修改 POS| write POS| write :
pos_shops , stock_adjustments , stock_invoices , stock_receipts ,
stock_requisitions
read_branch_stores| 讀取門市|
read branch stores| read :
branch_stores
write_branch_stores| 修改門市| write branch stores| write :
branch_stores
read_edms| 獲取 EDM 資訊

| read EDMs| read :
edms

- * *


---

## 📌 API 包含哪些資料格式可以怎麼查？

如何查詢 CYBERBIZ 可串接 API項目？在 【username】：apidemo
【secret】：apidemo
進行登入
API串接項目參考文件，依照顏色簡單分類使用的方法。可請公司技術人員協助使用。

藍色【GET】: 取得

綠色【POST】: 建立

黃色【PUT】: 更新

紅色【DELETE】: 刪除

- 以 customers : 顧客相關 API 為例
[[圖片說明：customer]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook05.png)

- 點開後任一API皆可看到相關資訊。並可點選Model查看此API的中文對照名稱，以利您做選擇。
[[圖片說明：model]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook06.png)

V2 APIs

💡[GET] /v2/product_feeds

{
"product_feeds": [

{
"name": "facebook",
"url": "http://your-shop-domain.com/products/fbcatalog/512076f08d78013b11306a7b958f3ea1",
"mime_type": "text/csv"
},
{
"name": "google",
"url": "http://your-shop-domain.com/products/google_product_feed/512076f08d78013b11306a7b958f3ea1",
"mime_type": "text/csv"
},
{
"name": "shopdotcom",
"url": "http://your-shop-domain.com/shopdotcom.xml",
"mime_type": "text/xml"
},
{
"name": "line",
"url": "http://your-shop-domain.com/line_shopping/512076f08d78013b11306a7b958f3ea1/product_full.json",
"mime_type": "application/json"
}
]
}

💡[GET] /v2/affiliate_vendor_orders

16. 參數說明

帶在 query string

[[圖片說明：新增優惠券群組]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook07.png)

- * *


---

## 📌 如何用 token 串接 API 取得資料？

API endpoint: 每秒至多 5 個 Request

使用 Bearer Token Access API
在 Request Header 中帶入 Access Token
`Authorization: Bearer {access_token got from /admin/oauth/token}`

範例 :

curl https://app-store-api.cyberbiz.io/shop \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2ODkxMzI0ODksImV4cCI6MTY4OTEzOTY4OSwic2hvcF9pZCI6NzEwOSwic2NvcGVzIjoicHVibGljIHNob3BfYXBpIiwic2hvcF9kb21haW4iOiJkZW1vLmN5YmVyYml6LmNvIn0.VyW3B2wA1b6uhH9pDfbzRvPjOmSQD7VHy-IiRmnof9g" \
-H "Accept: application/json"

curl https://app-store-api.cyberbiz.io/v1/customers \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2ODkxMzI0ODksImV4cCI6MTY4OTEzOTY4OSwic2hvcF9pZCI6NzEwOSwic2NvcGVzIjoicHVibGljIHNob3BfYXBpIiwic2hvcF9kb21haW4iOiJkZW1vLmN5YmVyYml6LmNvIn0.VyW3B2wA1b6uhH9pDfbzRvPjOmSQD7VHy-IiRmnof9g" \
-H "Accept: application/json"

curl https://app-store-api.cyberbiz.io/v2/product_feeds \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2ODkxMzI0ODksImV4cCI6MTY4OTEzOTY4OSwic2hvcF9pZCI6NzEwOSwic2NvcGVzIjoicHVibGljIHNob3BfYXBpIiwic2hvcF9kb21haW4iOiJkZW1vLmN5YmVyYml6LmNvIn0.VyW3B2wA1b6uhH9pDfbzRvPjOmSQD7VHy-IiRmnof9g" \
-H "Accept: application/json"

- * *


---

## 📌 Webhook 設定

1. 應用程式的設定頁中，選擇欲訂閱的 webhook 事件。
[[圖片說明：webhook]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook08.png)

2. 設定接收事件用的 endpoint URL，填好後儲存即可開始接收 shop 的 webhook events了
[[圖片說明：url]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook09.png)

- * *


---

## 📌 網站權限設定

【後台路徑】管理中心→ 「網站權限」

使用者需要有「自訂應用程式」的權限才得以進到設定頁查看、新增、編輯「自訂應用程式」
[[圖片說明：權限]](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook10.png)