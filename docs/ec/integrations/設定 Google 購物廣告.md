---
title: 設定 Google 購物廣告
description: 串接 Google Merchant Center、同步商品資料至 Google 搜尋與購物廣告。
module:
  - 第三方整合
tasks:
  - Google Merchant Center
type: quest
product:
  - EC
plans:
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
surfaces:
  - 第三方整合 > 谷歌 Google 設定 > Google Merchant Center
  - 商品 > 所有商品 > 設定
system:
  - 後台
lang: zh-TW
sites: 台灣
status: ""
activ: configure
tags:
  - Google
note:
  - verify FAQ
  - update internal links
---

# 設定 Google 購物廣告
串接 Google Merchant Center (GMC)、同步商品資料至 Google 搜尋與購物廣告。
{ .subtitle }

![](../../assets/images/ec-integrations-gmc.zh-tw.png){ title="串接 GMC：第三方整合 > Google > Google Merchant Center" .hero-page }


## 什麼是 Google Merchant Center

Google Merchant Center (GMC) 是 Google 提供的商品資料上傳與管理平台，可將商家商品資訊整合至 Google 生態系統（如 Google 搜尋與 Google 購物廣告），以提升商品曝光、廣告成效與轉換效率，並支援自動化管理。

- 提升商品曝光：商品會出現在 Google 搜尋結果的「購物」區塊，增加潛在顧客瀏覽量。
- 精準投放廣告：搭配 Google Ads 推廣商品，鎖定目標受眾，提高轉換率。
- 自動化管理：自動同步商品庫存、價格與圖片，減少手動維護工作。
- 數據追蹤與優化：收集使用者互動與廣告成效資料，支援後續分析與優化。


## 操作流程
### 設定商品資料同步方式

串接 Google Merchant Center 前，請先於 CYBERBIZ 後台設定相關欄位，以確保商品資料能正確傳送至 GMC。

1. 登入 CYBERBIZ 管理後台，前往 **第三方整合 > 谷歌 Google 設定 > Google Merchant Center**。
2. 在 **Google Merchant Center** 區塊，設定商品同步選項：
	- 依款式展開商品：選擇是否將每個商品款式都傳送至 GMC。
		- 開啟 (ON)：適合需要讓每一種款式都單獨曝光（例如：不同顏色或尺寸的服飾、鞋款）。 
		- 關閉 (OFF)：適合僅需展示主要商品圖片的品項（例如：電子產品、家電、筆電）。
	
		!!! tip "最佳做法"
			若您的商品有多種變化屬性，建議開啟此功能，能讓每個選項都在 Google 上被個別展示，提升曝光機會。
			
	- 商品圖片選擇方式：設定 GMC 抓取哪一張圖片作為商品圖（可選第一張圖或最後一張圖）。
	> 為確保廣告正常投放，請確認商品圖片符合 [Google 產品資料規格](https://support.google.com/merchants/answer/6324350)。
	
1. 更新動態饋給。
> 系統將於每天凌晨 1:30 更新動態饋給。您也可依需求點選 **手動更新目錄** 主動更新。


=== ":material-numeric-2-circle: 配置商品同步選項"

![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC02-1024x490.png){ .screenshot }


=== "商品圖片選擇方式"

	設定 GMC 抓取哪一張圖片作為商品圖（可選第一張圖或最後一張圖）。
	
	!!! warning "商品圖片規範：必須無價格、無宣傳標語、無浮水印"
		為確保廣告正常投放，請確認商品圖片符合 [Google 產品資料規格](https://support.google.com/merchants/answer/6324350)。

		<div class="grid cards two-columns borderless" markdown>
		
		:material-check-circle: 符合規範：無浮水印
		![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC03-1.png){ .screenshot }

		:material-close-circle: 不符合規範：有浮水印 
		![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC02-1.png){ .screenshot }

		</div>

=== ":material-numeric-3-circle: 更新動態饋給"

    系統將於每天凌晨 1:30 更新動態饋給。您也可依需求點選「手動更新目錄」。

### 設定 Google 商品類別

為了讓商品能出現在更合適的搜尋結果中，建議您手動設定 Google 商品類別。透過自行選擇分類，可讓廣告投放與成效追蹤更加精準。

??? warning "Google 商品類別設定限制"

    | 項目       | 限制說明                                                                 | 支援狀態 |
    |------------|------------------------------------------------------------------------|----------|
    | 未設定處理 | 若未手動設定，Google 會自動指定分類，但可能無法精確對應商品特性。           | :material-check: |
    | 類別自訂   | 可從 Google 提供的既有類別清單中選擇，無法自訂名稱或新增分類。              | :material-alert: |
    | 修改限制   | 選擇後可進行修改，但無法刪除，只能更換其他類別。                           | :material-alert: |
    | 批次套用   | 需逐筆商品設定商品類別，目前無法批次套用。                                 | :material-close: |

=== ":material-numeric-1-circle: 進入商品設定頁面"

    登入 CYBERBIZ 電商後台，前往「商品」→「所有商品」→ 點選欲設定的商品 → 進入「設定」分頁。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC22-1024x428.png){ .screenshot }

=== ":material-numeric-2-circle: 選擇產品類別"

    點開「Google 產品類別」欄位，選擇適用的產品類別。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC23.png){ .screenshot }

=== ":material-numeric-3-circle: 查看動態饋給連結"
    
    更新完畢後，可前往「第三方整合」→「谷歌 Google 設定」→「Google Merchant Center」，下載 Google Merchant Center 「產品動態饋給連結」查看。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC25-1024x686.png){ .screenshot }


### 申請 Google Merchant Center 帳號

!!! tip "最佳做法" 
    若您要投放 Google 自動化廣告，請直接在自動化廣告設定頁創建 [CYBERBIZ 代管 GMC 帳號](設定自動化廣告#cyberbiz-代管)並設定廣告，無須另外自行申請 GMC 帳號。如此可避免因人員操作 GMC 帳號造成權限變更造成廣告投遞異常。

=== ":material-numeric-1-circle: 前往 GMC 登入頁面" 

    - [ ] 進入 [Google Merchant Center :material-open-in-new:](https://www.google.com/retail/)，點擊「立即開始」。

    - [x] 您需要 Google 帳戶電子郵件地址和密碼才能建立 Merchant Center 帳戶，而且每個電子郵件地址僅限建立一個。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC01-1024x490.png){ .screenshot }

=== ":material-numeric-2-circle: 依序設定資訊"

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC05-1024x504.png){ .screenshot }

    === "新增商家地址"

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC03-1024x504.png){ .screenshot }

    === "確認網路商店"

        1.  輸入網路商店網址。
        2.  選擇「新增 HTML 標記或檔案」。
        3.  選擇「新增 HTML 標記」。
        4.  複製「系統為網路商店產生的 HTML 標記」。
        5.  至 CYBERBIZ 後台：「網站外觀」→「套版主題管理」→ 選擇操作「CSS/HTML 編輯器」→「theme.liquid」。
        6.  將 HTML 標記貼至 `</head>` 上方。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC06-1-1024x696.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC09-1-1024x508.png){ .screenshot }

    === "新增產品運送方式"

        依步驟輸入商家配送資訊。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC07-1024x486.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC08-1024x486.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC09-1-1024x485.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC10-1024x486.png){ .screenshot }

    === "新增退貨政策"

        依步驟輸入商家退貨政策。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC11-1024x504.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC12-1024x504.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC13-1024x504.png){ .screenshot }

    === "新增產品"

        === ":material-numeric-1-circle-outline: 選取國家/地區"
            
            選取商品適用的國家或地區。

            ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC14-1024x504.png){ .screenshot }

        === ":material-numeric-2-circle-outline: 複製產品動態饋給連結"
            
            前往 CYBERBIZ 後台：「第三方整合」→「谷歌 Google 設定」→「Google Merchant Center」，複製「產品動態饋給連結」。

            ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC16-1024x490.png){ .screenshot }

            !!! info "多國功能與手動更新"
                - 若有多國功能，Product Feed 的商品連結會帶有 `/zh-TW`。
                - 若要手動更新商品目錄，請點擊 **更新目錄** 按鈕。一小時僅能更新一次，重整畫面後可看到剩餘多久時間可更新目錄。

        === ":material-numeric-3-circle-outline: 貼上連結"
            
            - [ ] 回到 GMC 後台，選擇「透過檔案新增產品」。
            - [ ] 將「產品動態饋給連結」貼至「請輸入檔案連結」。

            ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC15-1024x504.png){ .screenshot }

=== ":material-numeric-3-circle: 查看上傳結果"

    待資料上傳後，可於產品頁查看完成畫面。上傳所需時間依產品數量而有所不同，請稍待片刻。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC17-1024x486.png){ .screenshot }

### 排除商品上傳至 Google 商品資料 (Product Feed)

系統會自動排除以下三種類型的商品，不會將其上傳至 Google Merchant Center。

| 商品類型      | 說明                          | 上傳至 GMC          |
| --------- | --------------------------- | ---------------- |
| 不公開的商品    | 商品顯示設定為「眼睛關起來」:material-eye-off:| :material-close: |
| 已達下架時間的商品 | 系統已設定下架時間，商品自動排除            | :material-close: |
| 標籤排除商品    | 標籤設定為 `贈品` 或 `排除 product feed`[^2] <br> :warning: 「排除」與「product」中間請勿添加空格 | :material-close: |

### Google Merchant Center 串接 Google Ads 帳戶

=== ":material-numeric-1-circle: 進入應用和服務設定"
    
    點選「設定」→「應用和服務」。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC18-1024x486.png){ .screenshot }

=== ":material-numeric-2-circle: 新增 Google 服務"
    
    於「Google 服務」區塊，點擊「新增服務」。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC19-1024x486.png){ .screenshot }

=== ":material-numeric-3-circle: 選擇 Google Ads"

    選擇「Google Ads」。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC20-1024x486.png){ .screenshot }

=== ":material-numeric-4-circle: 關聯 Google Ads 帳戶"

    選擇要關聯的 Google Ads 帳戶。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC21-1024x486.png){ .screenshot }

=== ":material-numeric-5-circle: 確認並關聯"

    確認串接資訊正確後，點選「關聯」。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC22-1024x486.png){ .screenshot }

## 常見問題

??? quote "CYBERBIZ 代管 GMC 帳號與自行申請 GMC 帳號有何差異？"
    若選擇由 CYBERBIZ 代管 GMC 帳號，系統會自動處理相關設定與維護，避免因手動操作導致的權限變更或廣告投放異常。若您已透過自動化廣告設定頁創建廣告並選擇代管，請勿自行另外申請 GMC 帳號。

??? quote "哪些商品不會上傳至 Google 商品資料 (Product Feed)？"
    系統會自動排除不公開的商品、已達下架時間的商品，以及標籤設定為「贈品」或「排除product feed」的商品。

??? quote "Google 商品類別可以批次設定嗎？"
    目前 Google 商品類別需逐筆商品設定，無法批次套用。

## 延伸閱讀


[^1]: 若您的商品有多種變化屬性，建議開啟此功能，能讓每個選項都在 Google 上被個別展示，提升曝光機會。
[^2]: 若您有商品不希望出現在 Google 搜尋引擎中，請將為商品加上 `排除product feed` 或 `贈品` 標籤。