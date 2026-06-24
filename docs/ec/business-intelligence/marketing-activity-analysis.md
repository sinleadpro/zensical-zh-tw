---
title: 行銷活動分析
description: 一次掌握折扣、優惠券與紅利的成效，了解哪些行銷活動真正帶動訂單與營收
created: 2026-06-16
last_modified: 2026-06-23 21:03
lang: zh-TW
type: tutorial
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 分析報表
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: branch
plans:
  - 高手
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
feature_badges: []
intents:
  - 查看行銷活動成效
  - 分析折扣活動與優惠券表現
  - 比較各折扣種類的貢獻
  - 檢視紅利使用情形
features:
  - 折扣活動分析
  - 優惠券分析
  - 紅利分析
  - 折扣活動排名
  - 優惠券種類分析
prerequisites:
  - 方案已包含行銷活動分析功能
related:
  - "[[設定紅利點數]]"
  - "[[設定優惠碼]]"
tags:
  - 行銷活動分析
  - 折扣活動
  - 優惠券
  - 紅利
  - 經營分析
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 日期選擇器
  - 下拉選單
  - 頁籤
  - 數字卡
  - 圓餅圖
  - 長條圖
  - 排名表格
  - 分頁切換
paths:
  - 經營分析 > 行銷活動分析
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/business-intelligence/marketing-activity-analysis/"
comments: false
search:
  exclude: false
icon: lucide/tag
hide: []
---

![行銷活動分析頁面](../../../assets/images/ec-bi-marketing-activity-analysis-hero.png){ .hero-page }

## 行銷活動分析說明 { #intro-marketing-activity }

這個頁面位於後台左側選單「**經營分析**」之下，整合了三個分析分頁，協助您回答「這檔活動到底有沒有效」這類問題：

- **折扣活動分析**：看全站折扣訂單的整體概況、各折扣種類的貢獻，以及單檔折扣活動的成效排名。
- **優惠券分析**：看各類優惠券與單張優惠券的使用狀況、營收與使用週期。
- **紅利分析**：看全館紅利的使用情形，並可匯出紅利報表。

!!! info "提示"
    本頁所有數據都以「**有效訂單**」為計算基準。有效訂單的定義請見 [重要規範與限制](#specs-marketing-activity-valid-order){ title="重要規範與限制" }。

## 頁面功能總覽 { #overview-marketing-activity }

進入頁面後，上方有三個分頁可切換，各分頁的內容如下：

| 分頁 | 主要看什麼 | 內含區塊 |
| :-- | :-- | :-- |
| **折扣活動分析** | 全站折扣訂單成效 | 折扣訂單概況、折扣種類分析、折扣活動排名 |
| **優惠券分析** | 優惠券使用與營收 | 優惠券種類分析、特定優惠券分析 |
| **紅利分析** | 全館紅利使用情形 | 紅利分析圖表、匯出紅利報表 |

!!! note "註釋"
    三個分頁彼此獨立，各自有自己的日期區間與篩選條件，切換分頁時不會互相影響。

## 使用前提與限制 { #prerequisites-marketing-activity }

[](){ #prerequisites-marketing-activity-plan }

### 方案開通條件 { #prerequisites-marketing-activity-plan-tier }

- [x] **需要方案支援**：「行銷活動分析」屬於「經營分析」的進階報表，部分入門方案不提供。若您在左側選單的「經營分析」中找不到「行銷活動分析」，代表目前方案未包含此功能[^plan]，可升級方案或洽詢客服。

[^plan]: 專業級、進階版不提供本功能；高手版(含)以上方案才會顯示。

---

### 紅利報表匯出的額外條件 { #prerequisites-marketing-activity-bonus-export }

- [x] **匯出紅利圖表加值功能**：「紅利分析」分頁右上角的 **「匯出紅利圖表」** 按鈕，只有在您的方案或加值功能包含「紅利報表匯出」時才會出現。若按鈕未顯示，仍可正常瀏覽紅利分析的圖表，只是無法匯出報表。

## 操作步驟 { #operate-marketing-activity }

### 折扣活動分析 { #operate-marketing-activity-discount }

進入頁面後預設停留在「**折扣活動分析**」分頁，由上而下分為三個區塊。

#### 查看折扣訂單概況 { #view-discount-overview }

1. **選擇日期區間：** 在「**折扣訂單概況**」區塊上方的日期選擇器挑選要分析的時間範圍。

    ![選擇日期區間](../../../assets/images/ec-bi-mkt-act-date-range.png)

2. **檢視四項關鍵數字：** 系統會顯示 **使用折扣訂單數**、**使用折扣訂單金額**、**總訂單數**、**總訂單金額** 四張數字卡。

    ![檢視四項關鍵數字](../../../assets/images/ec-bi-mkt-act-key-metrics.png)

3. **檢視佔比圖：** 下方兩個圓餅圖分別呈現 **折扣訂單數佔比** 與 **折扣訂單金額佔比**，讓您一眼看出折扣訂單在整體中的比重。

    ![檢視佔比圖](../../../assets/images/ec-bi-mkt-act-pie-chart.png)

??? info "折扣訂單概觀指標定義"

    | 指標 | 說明 |
    | :--- | :--- |
    | 使用折扣訂單數 | 「有效訂單」中有使用折扣的訂單總數量 |
    | 使用折扣訂單金額 | 「有效訂單」中有使用折扣的訂單總金額 |
    | 總訂單數 | 「有效訂單」的總數量 |
    | 總訂單金額 | 「有效訂單」的總訂單金額 |
    | 折扣訂單數佔比 | 已套用折扣的有效訂單數量 ÷ 總訂單數（一般訂單：未套用折扣 ÷ 總訂單數） |
    | 折扣訂單金額佔比 | 已套用折扣的有效訂單金額 ÷ 總訂單金額（一般訂單：未套用折扣 ÷ 總訂單金額） |

---

#### 分析各折扣種類的貢獻 { #discount-category-contribution }

1. **設定條件：** 在「**折扣種類分析**」區塊選擇日期區間，並於 **「請選擇折扣種類」** 下拉中勾選想比較的折扣種類(可複選，預設為全部折扣種類)。

    ![設定條件](../../../assets/images/ec-bi-mkt-act-discount-condition.png)

2. **切換衡量指標：** 透過區塊內的 **「訂單數」** 與 **「訂單金額」** 切換頁籤，決定長條圖要以訂單數還是訂單金額呈現。

    ![切換衡量指標](../../../assets/images/ec-bi-mkt-act-switch-metric.png)

3. **判讀長條圖：** 長條圖會列出各折扣種類在選定期間的表現，協助您找出最受歡迎的折扣類型。

    ![判讀長條圖](../../../assets/images/ec-bi-mkt-act-bar-chart.png)

??? info "折扣分析指標定義"

    | 指標 | 說明 |
    | :--- | :--- |
    | 訂單數 | 選取期間套用到該「折扣種類」的有效訂單數（目前後台只提供5種折扣種類） |
    | 訂單數占比 | 選取期間套用到該「折扣種類」的有效訂單數 ÷ 使用折扣訂單數 |
    | 訂單金額 | 選取期間套用到該「折扣種類」的有效訂單金額 |
    | 訂單金額占比 | 選取期間套用到該「折扣種類」的有效訂單金額 ÷ 使用折扣訂單金額 |

??? note "折扣種類佔比加總可能超過 100%"
    由於一個訂單可套用多個折扣種類，將各折扣種類的訂單數／訂單金額佔比相加，有可能會超過 100%。完整範例請見 [常見問題](#faq-marketing-activity-over-100)。

---

#### 查看折扣活動排名並下載 { #discount-ranking }

1. **設定條件：** 在「**折扣活動排名**」區塊選擇日期區間與折扣種類。

    ![設定排名條件](../../../assets/images/ec-bi-mkt-act-ranking-condition.png)

2. **檢視排名表格：** 表格會依名次列出各檔折扣活動的 **折扣活動名稱**、**折扣種類**、**總訂單金額**、**總訂單數**、**平均訂單金額**。

    ![檢視排名表格](../../../assets/images/ec-bi-mkt-act-ranking-table.png)

3. **調整排序：** 點擊 **總訂單金額**、**總訂單數** 或 **平均訂單金額** 欄位標題，即可依該欄位重新排序。

    ![調整排序](../../../assets/images/ec-bi-mkt-act-adjust-sort.png)

4. **下載報表：** 點擊區塊右上角的 **下載** 圖示，系統會匯出目前的折扣活動排名檔案。

    ![下載報表](../../../assets/images/ec-bi-mkt-act-download-report.png)

5. **翻頁查看：** 資料較多時，可用表格下方的分頁切換查看其餘名次。

    ![翻頁查看](../../../assets/images/ec-bi-mkt-act-pagination.png)

??? info "折扣活動排名指標定義"

    | 指標 | 說明 |
    | :--- | :--- |
    | 總訂單金額 | 指定時間內，套用該折扣活動之折扣的有效訂單之總金額（有效訂單：訂單狀態為非取消、非退貨訂單） |
    | 總訂單數 | 指定時間內，套用該折扣活動之折扣的有效訂單數量 |
    | 平均訂單金額 | 指定時間內，套用該折扣活動之折扣的平均訂單金額，即總訂單金額 ÷ 總訂單數 |

!!! note "註釋"
    折扣活動排名 **不包含紅利折扣**。紅利相關的成效請改至「紅利分析」分頁查看。

---

### 優惠券分析 { #operate-marketing-activity-coupon }

切換到「**優惠券分析**」分頁，可從「種類」與「單張」兩個角度分析優惠券。

#### 依優惠券種類分析 { #coupon-category }

1. **選擇日期區間：** 在「**優惠券種類分析**」區塊選擇要分析的時間範圍[^coupon-category-days]。

    ![選擇日期區間](../../../assets/images/ec-bi-mkt-act-coupon-date-range.png)

2. **選擇優惠券種類：** 於 **「請選擇優惠券種類」** 下拉選擇一種優惠券種類。

    ![選擇優惠券種類](../../../assets/images/ec-bi-mkt-act-coupon-category.png)

3. **切換分析圖表：** 透過圖表上方頁籤在 **「使用狀況分析」** 與 **「優惠券營收分析」** 之間切換。

    === "使用狀況分析"

        此頁籤顯示優惠券的 **發放數量**[^coupon-distribution-count] 與 **已使用數量**[^coupon-used-count] 趨勢圖，數字卡則呈現各項指標。

        ![使用狀況分析](../../../assets/images/ec-bi-mkt-act-coupon-usage.png)

    === "優惠券營收分析"

        ![優惠券營收分析](../../../assets/images/ec-bi-mkt-act-coupon-revenue.png)

4. **檢視指標數字卡：** 區塊會顯示該種類優惠券的平均折扣金額、折扣金額、平均折扣比例、使用次數、營業額等數字卡。各指標的精確算法請見 [優惠券指標定義對照表](references/marketing-activity-coupon-metrics-reference.md#reference-marketing-activity-coupon-metrics-category){ data-preview }。

    ![檢視指標數字卡](../../../assets/images/ec-bi-mkt-act-coupon-metrics.png)

[^coupon-category-days]: 優惠券種類分析的日期區間最長不得超過 100 天。

---

#### 分析單張特定優惠券 { #coupon-specific }

1. **選擇日期區間：** 在「**特定優惠券分析**」區塊選擇時間範圍[^coupon-specific-days]。

    ![選擇日期區間](../../../assets/images/ec-bi-mkt-act-specific-date-range.png)

2. **篩選優惠券：** 先於 **「請選擇優惠券種類」** 選擇種類，再於 **「優惠券名稱」** 欄位搜尋並選定要分析的那一張優惠券。

    ![篩選優惠券](../../../assets/images/ec-bi-mkt-act-filter-coupon.png)

3. **切換分析圖表：** 透過頁籤在 **「使用狀況分析」**、**「使用率分析」**、**「營收分析」**、**「AOV分析」** 之間切換。

    === "使用狀況分析"

        ![使用狀況分析](../../../assets/images/ec-bi-mkt-act-specific-usage.png)

    === "使用率分析"

        ![使用率分析](../../../assets/images/ec-bi-mkt-act-specific-usage-rate.png)

    === "營收分析"

        ![營收分析](../../../assets/images/ec-bi-mkt-act-specific-revenue.png)

    === "AOV分析"

        ![AOV分析](../../../assets/images/ec-bi-mkt-act-specific-aov.png)

4. **檢視指標數字卡：** 區塊會顯示該張優惠券的折扣金額、平均折扣比例、平均訂單金額、優惠券訂單營業額、優惠券使用次數、使用率、平均使用週期、目標客群數、目標客群總營業額等數字卡。各指標的精確算法請見 [優惠券指標定義對照表](references/marketing-activity-coupon-metrics-reference.md#reference-marketing-activity-coupon-metrics-specific){ data-preview }。

    ![檢視指標數字卡](../../../assets/images/ec-bi-mkt-act-specific-metrics.png)

[^coupon-specific-days]: 特定優惠券分析的日期區間最長不得超過 180 天。

---

### 紅利分析 { #operate-marketing-activity-bonus }

切換到「**紅利分析**」分頁，可檢視全館紅利的使用情形，並在符合條件時匯出紅利報表。

!!! info "提示"
    本分頁的「**紅利訂單**」是指 **有折抵紅利的訂單**（訂單結帳時使用了紅利點數），而非「有回饋紅利的訂單」。

#### 檢視紅利分析圖表 { #bonus-chart }

1. **切換至分頁：** 點選上方 **「紅利分析」** 分頁，頁面即會載入全館紅利使用相關的分析圖表。
2. **檢視頂部紅利點數概況：** 分頁上方有 **紅利點數總計使用率** 與 **紅利點數總計** 兩張數字卡，呈現目前會員手上紅利的整體狀況。

    ![檢視頂部紅利點數概況](../../../assets/images/ec-bi-mkt-act-bonus-summary.png)

    !!! note "註釋"
        兩張數字卡（紅利點數總計使用率、紅利點數總計）反映的是 **會員目前持有紅利的即時狀況**，為當下快照、**不受日期區間影響**；其餘圖表則是依所選日期區間統計的訂單數據。

3. **檢視各項分析圖表：** 數字卡下方依序為 **紅利營業額**、**營業額占比**、**紅利訂單**、**訂單數占比**、**AOV（客單價）**、**退貨率**、**紅利折扣額**、**紅利折扣比率** 等分析圖表，每張圖表皆可 **各自選擇日期區間**。

    === "紅利營業額"

        ![紅利營業額](../../../assets/images/ec-bi-mkt-act-bonus-revenue.png)

    === "營業額占比"

        ![營業額占比](../../../assets/images/ec-bi-mkt-act-bonus-revenue-ratio.png)

    === "紅利訂單"

        ![紅利訂單](../../../assets/images/ec-bi-mkt-act-bonus-orders.png)

    === "訂單數占比"

        ![訂單數占比](../../../assets/images/ec-bi-mkt-act-bonus-order-ratio.png)

    === "AOV（客單價）"

        ![AOV](../../../assets/images/ec-bi-mkt-act-bonus-aov.png)

    === "退貨率"

        ![退貨率](../../../assets/images/ec-bi-mkt-act-bonus-return-rate.png)

    === "紅利折扣額"

        ![紅利折扣額](../../../assets/images/ec-bi-mkt-act-bonus-discount-amount.png)

    === "紅利折扣比率"

        ![紅利折扣比率](../../../assets/images/ec-bi-mkt-act-bonus-discount-ratio.png)

??? info "紅利分析指標定義"

    | 指標 | 說明 |
    | :--- | :--- |
    | 紅利點數總計使用率 | 會員已使用的紅利點數 ÷ 已發出的紅利點數 × 100%。僅計算尚未過期的紅利點數 |
    | 紅利點數總計 | 會員目前 **尚未使用且尚未過期** 的紅利點數總和 |
    | 紅利營業額 | 依「紅利訂單／一般訂單」區分的有效訂單總營業額（趨勢圖按月呈現，占比圖為選取期間合計） |
    | 營業額占比 | 紅利訂單與一般訂單各自營業額佔總營業額的比例 |
    | 紅利訂單 | 依「紅利訂單／一般訂單」區分的有效訂單數量 |
    | 訂單數占比 | 紅利訂單與一般訂單各自訂單數佔總訂單數的比例 |
    | AOV（客單價） | 平均每筆訂單的金額，即訂單總金額 ÷ 訂單數，分「紅利訂單／一般訂單」呈現 |
    | 退貨率 | 已退貨訂單數 ÷ 訂單數 × 100%，分「紅利訂單／一般訂單」呈現 |
    | 紅利折扣額 | 選取期間內，所有紅利訂單折抵掉的紅利金額總和 |
    | 紅利折扣比率 | 紅利折抵金額 ÷（訂單實付金額 ＋ 紅利折抵金額）× 100%，即紅利折抵佔折抵前金額的比率 |

    !!! warning "退貨率的計算範圍"
        「退貨率」是本分頁唯一 **將已退貨訂單納入計算** 的指標（否則退貨率恆為 0）；其餘指標皆僅計算 [有效訂單][specs-marketing-activity-valid-order]{ title="重要規範與限制" }（不含已退貨、已取消訂單）。

---

#### 匯出紅利報表 { #bonus-export }

1. **點擊匯出：** 點擊分頁右上角的 **「匯出紅利圖表」** 按鈕[^bonus-export-plugin]，開啟匯出視窗。

    ![點擊匯出](../../../assets/images/ec-bi-mkt-act-click-export.png)

2. **設定匯出區間：** 於 **「匯出起始時間」** 與 **「匯出結束時間」** 選擇紅利發送的時間範圍[^bonus-export-days]。

    ![設定匯出區間](../../../assets/images/ec-bi-mkt-act-export-range.png)

3. **勾選報表項目：** 在「**匯出圖表選項**」勾選 **「全館紅利報表」**。

    ![勾選報表項目](../../../assets/images/ec-bi-mkt-act-export-items.png)

4. **送出匯出：** 點擊 **「確認」**，系統會在背景產製報表，完成後寄送至您的後台帳號信箱。

[^bonus-export-plugin]: 此按鈕僅在方案或加值功能包含「紅利報表匯出」時顯示。
[^bonus-export-days]: 匯出起訖時間以紅利發送時間計算，且區間不得超過 180 天。

## 重要規範與限制 { #specs-marketing-activity }

[](){ #specs-marketing-activity-valid-order }

- **有效訂單定義：** 全頁數據皆以「有效訂單」計算。有效訂單指「**訂單狀態為非取消訂單**」且「**退貨狀態為不需退貨或拒絕退貨**」的訂單。頁面標題旁的問號圖示也可隨時查看此定義。
- **折扣種類佔比可能超過 100%：** 在「折扣種類分析」中，單張訂單可能同時套用多個折扣活動，因此各折扣種類的訂單數佔比、金額佔比加總可能超過 100%，屬正常現象。
- **資料起算時間：** 系統自固定起始時間開始記錄行銷活動數據，起始時間之前的訂單不納入統計。
- **日期區間上限：** 優惠券種類分析最長 100 天、特定優惠券分析與紅利報表匯出最長 180 天，超過上限系統會提示縮短區間。

## 後續操作 { #next-steps-marketing-activity }

<div class="grid cards" markdown>

- :lucide-tag:{ .lg }  
  [__行銷活動設定__](../marketing/index.md){ title="行銷推廣" }  
  根據分析結果，調整或新增折扣、加價購等行銷活動。

- :lucide-ticket:{ .lg }  
  [__優惠券設定__](../marketing/coupon/setup-coupons.md){ title="設定優惠券" }  
  針對成效好的優惠券種類，建立新的優惠券發放給顧客。

- :lucide-gift:{ .lg }  
  [__紅利點數設定__](../marketing/setup-bonus-points.md){ title="設定紅利點數" }  
  依紅利使用情形，調整紅利回饋與兌換規則。

</div>

## 常見問題 { #faq-marketing-activity }

??? quote "為什麼左側選單找不到「行銷活動分析」？"
    [](){ #faq-marketing-activity-menu-missing }
    「行銷活動分析」屬於「經營分析」的進階報表，部分入門方案不提供。

    - 請確認您的方案是否包含此功能，必要時升級方案或洽詢客服。
    - 若方案包含此功能，請確認是在左側選單的「經營分析」分類下尋找。

??? quote "為什麼折扣種類分析的佔比加總會超過 100%？"
    [](){ #faq-marketing-activity-over-100 }

    由於一個訂單可套用多個折扣種類，因此將各折扣種類的訂單數／訂單金額佔比相加，有可能會超過 100%。

    例如：A 店家在 2023/12/01 – 2023/12/12 共成立了 3 張訂單；其中有 1 張訂單使用了商品加價購、優惠券與滿額贈折扣優惠，1 張訂單使用了紅利折扣優惠，1 張訂單無套用任何優惠。

    | 項目 | 數值 |
    | :--- | :--- |
    | 使用折扣訂單數 | 2 |
    | 總訂單數 | 3 |
    | 使用折扣訂單占比 | 2 ÷ 3 = 67% |
    | 商品加價購訂單數 | 1（33%） |
    | 優惠券折扣訂單數 | 1（33%） |
    | 滿額贈訂單數 | 1（33%） |
    | 紅利折扣訂單數 | 1（33%） |
    | 各折扣種類佔比加總 | 33% × 4 = 132% |

    因為同一筆訂單可同時被計入多個折扣種類，所以佔比加總超過 100% 是正常現象。

??? quote "折扣活動排名裡為什麼找不到紅利折扣？"
    [](){ #faq-marketing-activity-no-bonus-in-rank }
    折扣活動排名不包含紅利折扣。紅利相關的成效請改至 [紅利分析][operate-marketing-activity-bonus]{ data-preview } 分頁查看。

??? quote "有些折扣種類在下拉選單裡看不到，怎麼辦？"
    [](){ #faq-marketing-activity-missing-category }
    部分折扣種類需要先啟用對應的行銷活動功能才會出現。

    - 各折扣種類的開通條件請見 [折扣種類對照表](references/marketing-activity-discount-categories-reference.md){ data-preview }。

??? quote "「匯出紅利圖表」按鈕沒有出現？"
    [](){ #faq-marketing-activity-bonus-export-missing }
    此按鈕只在方案或加值功能包含「紅利報表匯出」時才會顯示。若未顯示，您仍可正常瀏覽紅利分析的圖表，只是無法匯出報表。

??? quote "什麼是「有效訂單」？為什麼數字和我實際的訂單數對不起來？"
    [](){ #faq-marketing-activity-valid-order }
    本頁所有數據都只計算「有效訂單」，定義為訂單狀態非取消、且退貨狀態為不需退貨或拒絕退貨。因此已取消或已退貨的訂單不會被計入，數字會與訂單列表的總數不同。

[^coupon-distribution-count]: 指當日官網「可供使用」的優惠券張數。系統每日會自動統計以下來源：今天發放的優惠券、今天之前發放但到今天仍然有效的優惠券。

[^coupon-used-count]: 指當日官網「於有效期內且被認列為已使用」的優惠券數量。當消費者於優惠券有效期間內成功使用該券時，從使用日開始直到優惠券到期前的每一天，皆會計入當日已使用數量（數量為 1）。一旦優惠券到期，不再計入後續日期的已使用數。

## 參考資料 { #reference-marketing-activity }

- [折扣種類對照表](references/marketing-activity-discount-categories-reference.md)
- [優惠券指標定義對照表](references/marketing-activity-coupon-metrics-reference.md)
