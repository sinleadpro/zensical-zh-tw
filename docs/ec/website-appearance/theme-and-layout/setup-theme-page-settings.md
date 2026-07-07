---
title: 各頁面設定指南
description: 依頁面類型說明拖拉版型的各項設定，包含首頁區塊、商品頁面、部落格、客服頁等。
created:
last_modified: 2026-07-07 22:16
lang: zh-TW
permalink: https://help.cyberbiz.io/ec/website-appearance/theme-and-layout/setup-theme-page-settings
type: tutorial
status:
version:
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
  - 套版主題管理
  - 商品管理
  - 部落格管理
  - 會員
  - 金物流
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: trunk
plans:
  - 企業
  - 專業
  - 專業PLUS
  - 進階
  - 進階PLUS
  - 高手
  - 高手PLUS
cyb_extensions: []
intents:
  - 設定各頁面顯示
  - 新增首頁區塊
  - 編輯商品頁面
  - 設定部落格頁面
  - 設定客服頁
  - 管理404頁面
  - 設定快速到貨頁
  - 設定搜尋頁面
features:
  - 頁面區塊編輯
  - 商品頁面設定
  - 部落格頁面設定
  - 客服與404頁設定
  - 快速到貨
  - 搜尋頁設定
  - 響應式設計
prerequisites:
  - 已使用拖拉版型
  - 後台管理員權限
  - 商品多層級分類架構 (設定)
  - 客服功能開通 (商品評論)
  - 門市設定 (快速到貨)
related: []
tags:
  - 拖拉版型
  - 首頁區塊
  - 商品頁面
  - 部落格
  - 客服頁
  - 404頁面
  - 快速到貨
  - 搜尋頁
devices:
  - desktop
  - tablet
  - mobile
ui_components: []
paths:
  - 網站外觀 > 套版主題管理
layouts:
  - 拖拉版型
wp_url: []
icon: lucide/panel-top
hide:
comments: false
---

## 各頁面設定說明 { #page-settings }

拖拉版型透過上方工具列的 **頁面下拉選單** 切換不同頁面。除了首頁、自訂頁面、單頁式頁面以「新增區塊」的方式自由組合外，其餘頁面的版面由系統固定，僅提供各自的設定項目。

各頁面設定需在拖拉版型編輯器中進行，請先參閱 [拖拉版型網站設定](theme-editor.md){ title="拖拉版型網站設定" } 了解如何進入編輯器。

!!! note "註釋"
    下拉選單實際出現的頁面，會依您安裝的版型與已開通的功能而不同，請以編輯器內顯示的為準。

## 使用前提與限制 { #prerequisites-page-settings }

開始之前，請先確認以下條件：

- [x] **已進入拖拉版型編輯器：** 需先開啟拖拉版型編輯器，請見 [進入拖拉版型編輯器](theme-editor.md#operate-theme-editor-enter){ title="進入拖拉版型編輯器" }。
- [x] **已使用拖拉版型：** 只有標示「拖拉設定」的版型才適用本文的設定。
- [x] **部分頁面需先完成前置設定：** 例如多層級分類、客服功能開通、門市設定等，請依各頁面章節的說明確認。

!!! plan "方案顯示差異"
     實際可編輯的頁面與區塊依您的方案與已開通功能而定。

## 操作步驟

依所需頁面類型快速跳轉：[首頁](#homepage)、[商品頁面](#product)、[商品群組頁面](#collection)、[商品多層級分類](#category)、[部落格頁](#blog)、[部落格文章頁](#article)、[客服頁](#contact)、[404 頁](#not-found)、[快速到貨頁](#express-delivery)、[搜尋頁](#search)。

### 首頁 { #homepage }

首頁可新增以下 13 種區塊。多數區塊的設定面板會提供一個 **其他版面設定** 展開面板，裡面除了各區塊的特有項目外，都包含一組共通的 **版面邊距**（單位 px），以下各區塊章節 **只列出其特有設定**，共通的版面邊距不再重複說明。

??? info "版面邊距設定"

    | 設定 | 說明 | 常見預設 |
    |------|------|----------|
    | 電腦版-版面左右外邊距 | **設 0px 即滿版**（貼齊左右螢幕邊緣） | 0 |
    | 電腦版-版面底部外邊距 | 與下方區塊的距離，設 0px 則兩區塊相連無間距 | 50 |
    | 手機版-版面左右外邊距 | 同上，套用於平板／手機 | 0 |
    | 手機版-版面底部外邊距 | 同上，套用於平板／手機 | 24 或 50 |

    ??? note-clean "特例"
        - **主打商品** 預設邊距較大（電腦左右 80px、手機左右 16px）。
        - **折疊內容** 用的是 **內邊距（padding）** 而非外邊距，且多一組上下內邊距。
        - **應用程式、CMS** 這類區塊沒有版面邊距設定。

通用操作方式：

1. 在頁面下拉選單中選擇「首頁」，可參考[切換編輯頁面與預覽](theme-editor.md#operate-theme-editor-preview){ title="切換編輯頁面與預覽" data-preview }了解預覽方式。
2. 在左側區塊列表點擊「新增區塊」，選擇要新增的區塊類型。
3. 點選區塊，在右側面板中編輯其內容與設定。
4. 完成後點擊「儲存」保存變更。

---

#### 輪播素材 { #section-main-slider }

可放入多張輪播「素材」的主視覺區塊。

1. 新增「輪播素材」區塊。
2. 在設定面板點擊 **其他版面設定**，展開後設定 **區塊層級** 屬性：

    - **圖片停留秒數**：每輪停留幾秒後切下一輪（預設 3 秒）。
    - **圖片切換速度**：切換動畫的速度，數值越大切換越慢（預設 0.3 秒）。

    ![輪播素材-共通設定](../../../assets/images/ec-website-appearance-slider-common-settings.png){ title="輪播素材-共通設定" }

    === "電腦版"

        - 版面左右外邊距（預設 0px，**設 0 即滿版**）、版面底部外邊距（預設 50px）。
        - **圖片數量**：每輪並排張數，**電腦版可選 1～8**（預設 1）。
        - **圖片間距**：張與張之間的距離（預設 12px，需 2 張以上才作用）。

        ![輪播素材-電腦版-版面邊距](../../../assets/images/ec-website-appearance-layout-margins-desktop.png){ title="電腦版-版面邊距" }

    === "平板版、手機版"

        - 版面左右外邊距（預設 0px）、版面底部外邊距（預設 50px）。
        - **圖片數量**：**手機版僅可選 1～3**（預設 1）。
        - **圖片間距**：預設 8px。

        ![輪播素材-手機／平板-版面邊距](../../../assets/images/ec-website-appearance-layout-margins-mobile.png){ title="手機／平板-版面邊距" }

3. 為 **每張素材** 設定圖片：

    - 上傳 **電腦版（建議寬 1920px）／平板版（960px）／手機版（480px）** 圖片，單張不超過 1MB，支援 JPG／PNG／JPEG／GIF。

        === "電腦版"

            ![輪播素材-電腦版-設定圖片](../../../assets/images/ec-website-appearance-image-desktop.png){ title="電腦版-上傳圖片" }
 
        === "平板版"

            ![輪播素材-平板版-設定圖片](../../../assets/images/ec-website-appearance-image-tablet.png){ title="平板版-上傳圖片" }

        === "手機版"

            ![輪播素材-手機版-設定圖片](../../../assets/images/ec-website-appearance-image-mobile.png){ title="手機版-上傳圖片" }

    - **僅上傳電腦版時，平板與手機會自動沿用同一張。**
    - 設定 **圖片連結**（可勾選「在新分頁開啟連結」）與 **圖片替代文字（alt）**（有助 SEO）。

        ![輪播素材-圖片連結](../../../assets/images/ec-website-appearance-image-link.png){ title="輪播素材-圖片連結" }

        ??? info "圖片連結可連往哪裡"
            **圖片連結** 為下拉選單，先選目的地類型再指定目標：商店首頁、全部商品、指定商品、商品群組（自訂／條件分類、任選折扣）、部落格、其它頁面、查詢頁面、客服表單，或選 **外部連結** 貼上站外網址。

            !!! warning-clean "使用前提"
                商品多層級分類、紅配綠組合優惠活動、紅利商城等選項，需先開通對應功能才會出現在下拉選單中。

4. 設定 **素材文字**（同樣是每張素材各自設定）：

    - **內容位置**：控制標題／內文／按鈕在圖片上的對齊方式，可選 **置左（預設）／置中／置右**。

        === "置左"

            ![輪播素材-內容位置-置左](../../../assets/images/ec-slider-left-align.png){ title="輪播素材內容位置-置左" }

        === "置中"

            ![輪播素材-內容位置-置中](../../../assets/images/ec-slider-central-align.png){ title="輪播素材內容位置-置中" }

        === "置右"

            ![輪播素材-內容位置-置右](../../../assets/images/ec-slider-right-align.png){ title="輪播素材內容位置-置右" }


    - **文字內容**：依序填入 **標題文字、內文文字、按鈕文字**（皆為選填，留空則該元素不顯示）。
    - **按鈕連結**：為 **連結欄位**，可勾選 **在新分頁開啟連結**。

        ![輪播素材-按鈕連結](../../../assets/images/ec-slider-button-link.png){ title="輪播素材-按鈕連結" }

        ??? info "按鈕連結可連往哪裡"
            按鈕連結為下拉選單，先選目的地類型再指定目標：商店首頁、全部商品、指定商品、商品群組（自訂／條件分類、任選折扣）、部落格、其它頁面、查詢頁面、客服表單，或選 **外部連結** 貼上站外網址。

            !!! warning-clean "使用前提"
                商品多層級分類、紅配綠組合優惠活動、紅利商城等選項，需先開通對應功能才會出現在下拉選單中。

    - **文字顏色**：分別設定四個元素的顏色（點色塊選色）。

        ![輪播素材-文字顏色](../../../assets/images/ec-slider-colors.png){ title="輪播素材-文字顏色" }

---

#### 橫幅廣告 { #section-banner } 

單張橫幅圖片，常用於活動入口。 

1. 新增「橫幅廣告」區塊。 
2. 上傳 **電腦版（建議寬 1920px）／平板版（960px）／手機版（480px）** 圖片，單張不超過 1MB，支援 JPG／PNG／JPEG／GIF。**僅上傳電腦版時，平板與手機會自動沿用同一張。** 

    === "電腦版"

        ![橫幅廣告-電腦版-設定圖片](../../../assets/images/ec-banner-image-desktop.png){ title="電腦版-上傳圖片" }

    === "平板版"

        ![橫幅廣告-平板版-設定圖片](../../../assets/images/ec-banner-image-tablet.png){ title="平板版-上傳圖片" }

    === "手機版"

        ![橫幅廣告-手機版-設定圖片](../../../assets/images/ec-banner-image-mobile.png){ title="手機版-上傳圖片" }

3. 設定 **圖片連結**（可勾選「在新分頁開啟連結」）與 **圖片替代文字（alt text）**。 

    ![橫幅廣告 - 圖片連結](../../../assets/images/ec-website-appearance-banner-link.png) 

    ![橫幅廣告 - 替代文字](../../../assets/images/ec-website-appearance-banner-alt.png) 

4. 可勾選 **顯示按鈕**，開啟後設定 **按鈕位置**(中上、置中、中下)、**按鈕文字**，以及按鈕的 **底色／文字色**。 

    ![橫幅廣告 - 顯示按鈕](../../../assets/images/ec-website-appearance-banner-button.png) 

5. 調整版面邊距（電腦左右／底部、手機左右／底部；**手機版底部外邊距預設 24px**）。 

    ![橫幅廣告 - 版面邊距](../../../assets/images/ec-banner-margins.png){ title="橫幅廣告-版面邊距"}

---

#### 商品分類 { #section-collection-blocks } 

從指定商品分類帶入商品的列表區塊。 

1. 新增「商品分類」區塊。 
2. 填寫 **標題**，點擊 **選擇商品分類** 挑選要顯示的分類。 
3. 設定 **商品數量上限**（每次顯示的商品數，預設 12）與 **商品展開** 方式。 

    === "左右滑動"

        ![商品分類-基本設定-左右滑動](../../../assets/images/ec-website-appearance-collection-basic-carousel.png) 

    === "往下展開"

        ![商品分類-基本設定-往下展開](../../../assets/images/ec-website-appearance-collection-basic-expand.png) 

4. 調整 **版面設定**： 

    - **商品欄數**：電腦版 **2～6 欄**（預設 4）、手機版 **1～3 欄**（預設 2）。 
    - **商品排列**：置左／置中／置右。 
    - **文字排列**：置左／置中／置右（預設置中）。 

    ![商品分類 - 版面設定](../../../assets/images/ec-website-appearance-collection-layout.png) 

5. 選擇 **樣式設定**： 

    - **電腦版商品分類樣式**：預設(商品圖) / 顯示部分內容(商品圖、名稱、價格) / 全顯示(商品圖、名稱、價格、購買按鈕)。

        === "預設"

            ![商品分類 - 分類樣式](../../../assets/images/ec-website-appearance-collection-category-style.png) 

        === "顯示部分內容"

            ![商品分類 - 分類樣式](../../../assets/images/ec-website-appearance-collection-category-style.png) 

        === "全顯示"

            ![商品分類 - 分類樣式](../../../assets/images/ec-website-appearance-collection-category-style.png) 

    - **商品圖游標懸停效果**：共 5 種 —— 快速加入購物車按鈕／圖片切換／陰影／邊框強調／放大效果。 
    - **商品圖圓角**（預設 15px）。 


    ![商品分類 - 懸停效果與圓角](../../../assets/images/ec-website-appearance-collection-hover-radius.png) 



#### 商品分類 { #section-collection-blocks }

從指定商品分類帶入商品的列表區塊。

1. 新增「商品分類」區塊。
2. 填寫 **標題**，點擊 **選擇商品分類** 挑選要顯示的分類。
3. 設定商品數量上限與商品展開方式。

    ![商品分類 - 基本設定](../../../assets/images/ec-website-appearance-collection-basic.png)

4. 在 **版面設定** 中調整電腦／手機版的商品欄數、商品排列、文字排列。

    ![商品分類 - 版面設定](../../../assets/images/ec-website-appearance-collection-layout.png)

5. 在 **樣式設定** 中選擇電腦版商品分類樣式、商品圖游標懸停效果、商品圖圓角。

    ![商品分類 - 分類樣式](../../../assets/images/ec-website-appearance-collection-category-style.png)

    ![商品分類 - 懸停效果與圓角](../../../assets/images/ec-website-appearance-collection-hover-radius.png)

---

#### 影片設定 { #section-video }

嵌入單支影片。

1. 新增「影片設定」區塊。
2. 填寫 **標題** 與 **影片連結**。
3. 設定自動播放、隱藏外框、重複播放等選項。

![影片設定介面](../../../assets/images/ec-website-appearance-video.png)

---

#### 分頁頁籤 { #section-blog-tabs }

以頁籤呈現多個部落格的文章。

1. 新增「分頁頁籤」區塊。
2. 在 **其他版面設定** 中填寫標題，設定文章欄數。

    ![分頁頁籤 - 基本設定](../../../assets/images/ec-website-appearance-blog-tabs-basic.png)

3. 在 **部落格** 小區塊中，各別選擇要顯示的部落格。

    ![分頁頁籤 - 部落格選擇](../../../assets/images/ec-website-appearance-blog-tabs-select.png)

---

#### 自訂排版設計 { #section-custom-blocks }

自由組合多種小區塊的彈性版面，可設定區塊間距與手機版排版。

1. 新增「自訂排版設計」區塊。
2. 點擊 **新增小區塊**，選擇要加入的元件類型：

=== "圖片"

    1. 上傳電腦／平板／手機版圖片。
    2. 填寫標題、圖片說明、連結、替代文字。
    3. 設定 **版面螢幕占比**（控制該區塊在橫列的寬度比例）。

    ![自訂排版設計 - 圖片](../../../assets/images/ec-website-appearance-custom-blocks-image.png)

=== "影片"

    1. 貼入影片連結。
    2. 設定自動播放／隱藏外框／重複播放。
    3. 設定 **版面螢幕占比**。

    ![自訂排版設計 - 影片](../../../assets/images/ec-website-appearance-custom-blocks-video.png)

=== "排程跑馬燈"

    1. 載入預先製作好的跑馬燈群組。
    2. 設定 **版面螢幕占比**。
    3. 詳見 [排程跑馬燈設定指南](configure-scheduled-carousels.md){ title="建立與管理排程跑馬燈" }。

    ![自訂排版設計 - 排程跑馬燈](../../../assets/images/ec-website-appearance-custom-blocks-carousel.png)

=== "自訂 HTML"

    1. 點擊「編輯」進入 HTML 編輯頁面。
    2. 貼入自訂 HTML／CSS 程式碼。
    3. 設定 **版面螢幕占比**。

    ![自訂排版設計 - 自訂 HTML](../../../assets/images/ec-website-appearance-custom-blocks-html.png)

=== "商品"

    1. 點擊「選擇商品」，使用進階篩選或關鍵字找出商品，點擊「確認新增」。僅能選擇單一商品。
    2. 設定電腦版商品分類樣式及 **版面螢幕占比**。

    ![自訂排版設計 - 選擇商品](../../../assets/images/ec-website-appearance-custom-blocks-product-select.png)

    ![自訂排版設計 - 分類樣式與版面占比](../../../assets/images/ec-website-appearance-custom-blocks-product-layout.png)

!!! tip "設計模組的版面比例"
    您可以透過設定「**版面螢幕占比**」來控制每個區塊在畫面中的寬度，讓多個區塊能在同一橫列中並排顯示。

    **排列邏輯說明：**

    - 區塊會由左至右依序排列。
    - 每一橫列的總占比上限為 100%。當區塊並排的占比超過 100%，系統會自動換行，將超出區塊及後續區塊顯示於下一列，以此類推。

    ??? example "常見排版範例"
        === "三欄式結構"
            建立 3 個區塊，每個區塊占比設為 33%，三者加總不超過 100% 即可並排。

            ![三欄式排版範例](../../../assets/images/ec-website-appearance-custom-blocks-layout-3col.png)

        === "雙欄式結構"
            建立 2 個區塊，可設定為 60% + 40%、50% + 50% 等加總為 100% 的組合。

            ![雙欄式排版範例](../../../assets/images/ec-website-appearance-custom-blocks-layout-2col.png)

        === "單欄式結構"
            如僅有一個區塊需滿版呈現，可設為 100%。

            ![單欄式排版範例](../../../assets/images/ec-website-appearance-custom-blocks-layout-1col.png)

---

#### 圖文介紹 { #section-graphic-intro }

圖片搭配文字與按鈕的介紹區塊。

1. 新增「圖文介紹」區塊。
2. 設定文字排版、文字色／背景色。
3. 上傳電腦／平板／手機版圖片，選擇圖片位置與電腦版版面占比。
4. 在 **小區塊** 中編輯標題（可設字級）、內文（可設字級）、按鈕（文字、底色／文字色、連結）。

![圖文介紹區塊設定](../../../assets/images/ec-website-appearance-graphic-intro.png)

---

#### 自訂 HTML { #section-custom-html }

直接貼入 HTML 程式碼，適合放第三方語法或自訂內容。

1. 新增「自訂 HTML」區塊。
2. 點擊「編輯」，在 HTML 編輯器中貼入程式碼。

![自訂 HTML 區塊設定](../../../assets/images/ec-website-appearance-custom-html.png)

---

#### 應用程式 { #section-app }

放入已安裝的應用程式元件。

1. 新增「應用程式」區塊。
2. 點擊 **選擇套件**，選取已安裝的應用程式。

![應用程式區塊設定](../../../assets/images/ec-website-appearance-app.png)

---

#### 文字編輯 { #section-text }

純文字編輯區塊，提供進階文字編輯器。

1. 新增「文字編輯」區塊。
2. 在進階文字編輯器中輸入內容，可使用標題、樣式、連結等功能。

![文字編輯區塊設定](../../../assets/images/ec-website-appearance-text-editor.png)

---

#### CMS `方案限定` { #section-cms }

進階自訂區塊，提供 HTML／CSS／JS／Import 程式碼編輯器，並可帶入指定商品分類與商品數量上限。

1. 新增「CMS」區塊（需開通 CMS 功能）。
2. 在程式碼編輯器中編寫或貼入 HTML／CSS／JS 程式碼。
3. 設定要帶入的商品分類與商品數量上限。

---

#### 主打商品 { #section-flagship }

聚焦呈現單一商品並提供購買操作。

1. 新增「主打商品」區塊。
2. 點擊 **選擇商品** 挑選要顯示的商品。
3. 選擇商品圖片位置。
4. 在 **小區塊** 中設定商品標題（字級、可帶商品連結）、文字、購買按鈕、價格、款式選單、數量選擇器。

![主打商品區塊設定](../../../assets/images/ec-website-appearance-flagship-product.png)

---

#### 折疊內容 { #section-collapsible }

可展開／收合的內容區塊，適合 FAQ 或購物須知。

1. 新增「折疊內容」區塊。
2. 填寫 **標題**，設定背景／容器／邊框／文字顏色、內外邊距。
3. 在 **折疊項目** 小區塊中，編輯項目標題、標題圖示、內容（進階文字編輯器）。

![折疊內容區塊設定](../../../assets/images/ec-website-appearance-collapsible.png)

---

### 商品頁面 { #product }

商品頁面主要由四個功能區塊組成，可依需求開啟或調整排序。

在頁面下拉選單選擇「商品頁面」，即可進行以下設定：

=== "基本設定"

    主要控管商品在前台呈現的庫存狀態、價格標籤顯示邏輯以及購買行為。

    1. 設定是否 **顯示商品價格(SKU)**。
    2. 啟用 **會員專屬價格標籤**：商品設定會員專屬價格時，未登入會員或訪客瀏覽時會在價格旁顯示此標籤。
    3. 勾選 **商品價格標籤**：可顯示「優惠售價」或「建議售價」文字。
    4. 設定 **多款式價格** 顯示方式。
    5. 選擇 **無庫存狀態** 時款式按鈕的行為（不可點選／可點選並顯示聯絡店家）。
    6. 勾選 **顯示優惠活動區**。

    ![商品頁面-基本設定](../../../assets/images/ec-網站外觀-拖拉版型-商品頁面-基本設定.png)

=== "商品介紹"

    設定商品介紹區塊的標題名稱，並決定是否在前台顯示該欄位。

    ![商品頁面-商品介紹](../../../assets/images/ec-網站外觀-拖拉版型-商品頁面-商品介紹.png)

=== "商品評論"

    此功能需先洽客服申請開通。開通後可設定是否需審核留言、隱藏部分姓名，並可搭配 Google reCAPTCHA 防止機器人攻擊。

    - [如何管理商品評論](../../products/engagement/manage-product-reviews.md){ title="管理商品評論" }
    - [如何啟用 reCAPTCHA](../customer-interaction/enable-comment-recaptcha.md){ title="啟用留言區 reCAPTCHA" }

    ![商品頁面-商品評論](../../../assets/images/ec-網站外觀-拖拉版型-商品頁面-商品評論.png)

=== "相關商品"

    選擇顯示「商品群組其他商品」(同分類隨機顯示)或「自訂關聯群組商品」。

    ![商品頁面-相關商品](../../../assets/images/ec-網站外觀-拖拉版型-商品頁面-相關商品.png)

---

### 商品群組頁面 { #collection }

針對群組頁面，可指定要套用哪一組導覽選單（需先在 [選單／導覽列設定](../navigation/setup-menus-navigation.md){ title="設定選單與導覽列" } 完成設置）。

1. 在頁面下拉選單選擇「商品群組頁面」。
2. 設定 **商品欄數**（每排顯示的商品數量）。
3. 設定 **商品數量上限**（每頁顯示的商品數量）。
4. 選擇 **更多商品顯示方式**（分頁跳轉或向下無限滾動）。

![商品群組頁面](../../../assets/images/ec-網站外觀-拖拉版型-商品群組頁面-商品分類設定.png)

---

### 商品多層級分類 { #category }

針對多層級分類頁面的呈現方式進行微調。需先 [建立商品多層級分類架構](../../products/categories-and-tags/multi-level-category-setup.md){ title="設定商品多層級分類" }。

![商品多層級分類](../../../assets/images/ec-網站外觀-拖拉版型-商品多層級分類頁面.png)

---

### 部落格頁 { #blog }

用於呈現多篇文章的摘要列表。

1. 在頁面下拉選單選擇「部落格頁」。
2. 設定 **每頁文章數量**。
3. 勾選 **顯示精選文章**，在部落格列表頁底部顯示特定精選文章。
4. 開啟精選文章後，選擇要顯示哪一個部落格群組作為精選內容。

![部落格頁](../../../assets/images/ec-網站外觀-拖拉版型-部落格頁-部落格設定.png)

---

### 部落格文章頁 { #article }

用於顯示單篇完整文章的詳細內容。

1. 在頁面下拉選單選擇「部落格文章頁」。
2. 設定 **文章標籤區標題**，系統會自動抓取該文章所屬群組內的所有文章標籤並在此區塊呈現。

![部落格文章頁](../../../assets/images/ec-網站外觀-拖拉版型-部落格文章頁-部落格文章設定.gif)

---

### 客服頁 { #contact }

客服頁面在前台主要以「聯絡我們」表單形式呈現，供訪客留言諮詢。

1. 在頁面下拉選單選擇「客服頁」。
2. 設定 **問題類型**：前往後台 **會員 > 客服問題分類** 自訂表單中的下拉式問題選單。
3. 建議在 **頁腳(Footer)** 區塊同步設定完整的公司電話、地址與 Email，增加品牌信任感。
4. 如需防止機器人攻擊，可 [啟用留言區 reCAPTCHA](../customer-interaction/enable-comment-recaptcha.md){ title="啟用留言區 reCAPTCHA" }。

![客服頁](../../../assets/images/ec-網站外觀-拖拉版型-客服頁面.png)

---

### 404 頁 { #not-found }

當消費者訪問到失效連結時的顯示畫面，可自訂視覺以緩解負面體驗。

1. 在頁面下拉選單選擇「404 頁」。
2. 上傳自訂圖片，建議設計符合品牌風格或有趣的引導圖。
3. 設定 **標題** 與 **返回首頁按鈕文字**。

![404 頁](../../../assets/images/ec-網站外觀-拖拉版型-404頁.png)

---

### 快速到貨頁 { #express-delivery }

用於自訂快速到貨專區的視覺與醒目入口。

1. 在頁面下拉選單選擇「快速到貨頁」。
2. 設定 **Logo 背景**（導覽列顏色），幫助消費者區分一般專區與快速到貨專區。
3. 勾選 **顯示快速到貨按鈕**，系統會在官網全站導覽列上方顯示明顯的專區入口。

![快速到貨頁](../../../assets/images/ec-網站外觀-拖拉版型-快速到貨頁面-快速到貨設定.gif)

---

### 搜尋頁 { #search }

1. 在頁面下拉選單選擇「搜尋頁」。
2. 指定搜尋頁面左側要套用的 **選單**（需先 [建立選單](../navigation/setup-menus-navigation.md){ title="設定選單與導覽列" }）。
3. 搜尋結果中的商品會同步套用「[全站共用設定](setup-global-theme-settings.md#shop-product-display){ title="全站共用設定" }」中的顯示規範（價格區間、商品標語、已銷售數量等）。
4. 搜尋結果頁支援顯示定期定額、特價、缺貨以及自定義標籤。

??? info "搜尋範圍與邏輯說明"
    - **搜尋範圍：** 不只查詢「商品名稱」，亦涵蓋 **商品群組名稱、商品廠商與商品介紹**。
    - **分詞邏輯：** 商品標題支援分詞搜尋，需完全符合分詞才會被搜到。例如以「空格」或「-」會將標題切分為單詞：標題為「ER-1410」時搜「1410」可找到；標題為「ER1410」時搜「1410」則找不到。
    - **排除搜尋：** 若部分商品不希望出現在搜尋頁，可於商品編輯頁的「基本設定」中關閉「商品搜尋功能」，該商品將無法在站內搜尋框、所有商品列表及外部 Google 搜尋中被檢索。

![搜尋頁](../../../assets/images/ec-網站外觀-拖拉版型-搜尋頁.png)

---

## 後續操作 { #next-steps-page-settings }

<div class="grid cards" markdown>

- :lucide-palette:{ .lg }   
  [__拖拉版型網站設定__](theme-editor.md){ title="拖拉版型網站設定" }     
  了解如何進入拖拉版型編輯器進行網站設定

- :lucide-settings-2:{ .lg }   
  [__全站共用設定__](setup-global-theme-settings.md){ title="全站共用設定" }     
  設定彈窗廣告、顏色、品牌識別、SEO、商品顯示行為與動態標籤

</div>

## 參考資料 { #reference-page-settings }

- [可新增區塊類型對照表](../references/theme-editor-sections.md)
- [可拖拉編輯的頁面對照表](../references/theme-editor-pages.md)


 --- 


 --- 


 --- 

 #### 影片設定 { #section-video } 

 嵌入單支影片。 

 1. 新增「影片設定」區塊。 
 2. 填寫 **標題** 與 **影片連結**。 
 3. 設定播放行為（皆為是／否）： 

     - **自動播放**（預設關閉）。 
     - **隱藏外框**（預設關閉）。 
     - **重複播放**（**預設開啟**）。 

 4. 在 **其他版面設定** 調整電腦／手機版面邊距（此區塊四組邊距預設皆為 0）。 

 ![影片設定介面](../../../assets/images/ec-website-appearance-video.png) 

 --- 

 #### 分頁頁籤 { #section-blog-tabs } 

 以頁籤呈現多個部落格的文章。 

 1. 新增「分頁頁籤」區塊。 
 2. 在 **其他版面設定** 中填寫 **標題**，並設定 **文章欄數**（**2～5 欄**，預設 4）。 

     ![分頁頁籤 - 基本設定](../../../assets/images/ec-website-appearance-blog-tabs-basic.png) 

 3. 在 **部落格** 小區塊中新增／管理頁籤，**每個小區塊各自選擇一個要顯示的部落格**（可加入多個小區塊形成多頁籤）。 

     ![分頁頁籤 - 部落格選擇](../../../assets/images/ec-website-appearance-blog-tabs-select.png) 

 --- 

 #### 自訂排版設計 { #section-custom-blocks } 

 自由組合多種小區塊的彈性版面。 

 1. 新增「自訂排版設計」區塊。 
 2. 在 **其他版面設定** 設定版面： 

     - 電腦版／手機版的 **版面邊距**。 
     - **區塊間距**：小區塊之間的距離，電腦版與手機版可各自設定（預設 10px）。 
     - **手機版排版**：控制小區塊在手機上的排列方式。 

 3. 點擊 **新增小區塊**，選擇要加入的元件類型。**每一種小區塊都可設定「版面螢幕占比」** 來控制寬度： 

 === "圖片" 

     1. 上傳電腦／平板／手機版圖片（僅傳電腦版時自動沿用）。 
     2. 填寫 **圖片標題、圖片說明（進階文字）、圖片連結（可新分頁開啟）、圖片替代文字**。 
     3. 設定 **版面螢幕占比**。 

     ![自訂排版設計 - 圖片](../../../assets/images/ec-website-appearance-custom-blocks-image.png) 

 === "影片" 

     1. 貼入 **影片連結**。 
     2. 設定 **自動播放／隱藏外框／重複播放**（重複播放預設開啟）。 
     3. 設定 **版面螢幕占比**。 

     ![自訂排版設計 - 影片](../../../assets/images/ec-website-appearance-custom-blocks-video.png) 

 === "排程跑馬燈" 

     1. 載入預先製作好的 **跑馬燈群組**。 
     2. 設定 **版面螢幕占比**。 
     3. 詳見 [排程跑馬燈設定指南](configure-scheduled-carousels.md){ title="建立與管理排程跑馬燈" }。 

     ![自訂排版設計 - 排程跑馬燈](../../../assets/images/ec-website-appearance-custom-blocks-carousel.png) 

 === "自訂 HTML" 

     1. 點擊「編輯」進入 HTML 編輯頁面。 
     2. 貼入自訂 HTML／CSS 程式碼。 
     3. 設定 **版面螢幕占比**。 

     ![自訂排版設計 - 自訂 HTML](../../../assets/images/ec-website-appearance-custom-blocks-html.png) 

 === "商品" 

     1. 點擊「選擇商品」找出商品（僅能選單一商品）。 
     2. 設定 **電腦版商品分類樣式** 及 **版面螢幕占比**。 

     ![自訂排版設計 - 選擇商品](../../../assets/images/ec-website-appearance-custom-blocks-product-select.png) 

     ![自訂排版設計 - 分類樣式與版面占比](../../../assets/images/ec-website-appearance-custom-blocks-product-layout.png) 

 !!! tip "設計模組的版面比例" 
     透過「**版面螢幕占比**」控制每個小區塊的寬度，讓多個小區塊在同一橫列並排。每列總占比上限 100%，超過即自動換行。 

 --- 

 #### 圖文介紹 { #section-graphic-intro } 

 圖片搭配文字與按鈕的介紹區塊。 

 1. 新增「圖文介紹」區塊。 
 2. 設定 **文字排版**（靠左／置中／靠右）、**文字色** 與 **背景色**。 
 3. 上傳電腦／平板／手機版圖片，選擇 **圖片位置**（左側／右側）與 **電腦版版面占比**（預設 50%）。 
 4. 在 **小區塊** 中編輯： 

     - **標題**：文字內容（預設「產品介紹」），可設 **字級**（預設 24px）。 
     - **內文**：進階文字編輯器，可設 **字級**（預設 14px）。 
     - **按鈕**：按鈕文字（預設「了解更多」）、按鈕底色／文字色、按鈕連結（可新分頁開啟）。 

 ![圖文介紹區塊設定](../../../assets/images/ec-website-appearance-graphic-intro.png) 

 --- 

 #### 自訂 HTML { #section-custom-html } 

 直接貼入 HTML 程式碼，適合放第三方語法或自訂內容。 

 1. 新增「自訂 HTML」區塊。 
 2. 點擊「編輯」，在 HTML 程式碼編輯器中貼入程式碼。 
 3. 在 **其他版面設定** 調整電腦／手機版面邊距（此區塊四組邊距預設皆為 0）。 

 ![自訂 HTML 區塊設定](../../../assets/images/ec-website-appearance-custom-html.png) 

 --- 

 #### 應用程式 { #section-app } 

 放入已安裝的應用程式元件。 

 1. 新增「應用程式」區塊。 
 2. 點擊 **選擇套件**，選取已安裝的應用程式（此區塊僅此一項設定，無版面邊距）。 

 ![應用程式區塊設定](../../../assets/images/ec-website-appearance-app.png) 

 --- 

 #### 文字編輯 { #section-text } 

 純文字編輯區塊，提供進階文字編輯器。 

 1. 新增「文字編輯」區塊。 
 2. 在進階文字編輯器中輸入內容，可使用標題、樣式、連結等功能。 
 3. 在 **其他版面設定** 調整電腦／手機版面邊距（四組邊距預設皆為 0）。 

 ![文字編輯區塊設定](../../../assets/images/ec-website-appearance-text-editor.png) 

 --- 

 #### CMS `方案限定` { #section-cms } 

 進階自訂區塊，提供程式碼編輯器並可帶入指定商品分類。 

 1. 新增「CMS」區塊（需開通 CMS 功能）。 
 2. 在程式碼編輯器中編寫，實際提供 **4 格**：**Root（HTML）／CSS／JS／Import**。 
 3. 設定要帶入的 **商品分類** 與 **商品數量上限**。 

 --- 

 #### 主打商品 { #section-flagship } 

 聚焦呈現單一商品並提供購買操作。 

 1. 新增「主打商品」區塊。 
 2. 點擊 **選擇商品** 挑選要顯示的商品，並選擇 **商品圖片位置**（左側／右側）。 
 3. 在 **小區塊** 中設定： 

     - **商品標題**：可設 **字級**（預設 24px），並可勾選「**帶入商品連結**」「**在新分頁開啟商品連結**」（皆預設開啟）。 
     - **文字**：進階文字編輯器，可設字級（預設 14px）。 
     - **購買按鈕**：可勾選「**顯示立即購買按鈕**」（預設開啟）。 
     - **價格／款式選單／數量選擇器**：為固定顯示的小區塊，無其他可調整設定。 

 4. 此區塊 **版面邊距預設較大**（電腦左右 80px／底部 50px、手機左右 16px／底部 24px）。 

 ![主打商品區塊設定](../../../assets/images/ec-website-appearance-flagship-product.png) 

 --- 

 #### 折疊內容 { #section-collapsible } 

 可展開／收合的內容區塊，適合 FAQ 或購物須知。 

 1. 新增「折疊內容」區塊。 
 2. 填寫 **標題**（預設「折疊內容」）。 
 3. 設定 **顏色**：背景、項目底色、項目外框、文字與圖示（共 4 色）。 
 4. 設定 **邊距**（此區塊用 **內邊距 padding**，非外邊距）： 

     - 電腦版：左右內邊距（預設 160px）、上下內邊距（預設 48px）、底部外邊距（預設 30px）。 
     - 手機版：左右內邊距（預設 16px）、上下內邊距（預設 24px）、底部外邊距（預設 10px）。 

 5. 在 **折疊項目** 小區塊中，編輯 **項目標題**、**標題圖示**（無／問號／圖釘／打勾／電燈泡，共 5 種）、**內容**（進階文字編輯器）。 

 ![折疊內容區塊設定](../../../assets/images/ec-website-appearance-collapsible.png) 
