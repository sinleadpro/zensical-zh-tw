---
title: 訂單分析
description: 使用訂單分析頁面查看銷售趨勢、金物流偏好與業績報表
created: 2026-06-15
last_modified: 2026-06-15 21:22
lang: zh-TW
type: tutorial
status: ""
author: Jase
version: ""
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
difficulty: beginner
tnb: ""
plans:
  - 專業
  - 進階
  - 高手
intents:
  - 查看訂單銷售趨勢
  - 分析付款與出貨偏好
  - 下載業績明細報表
features:
  - 訂單總體分析
  - 訂單金物流分析
  - 訂單報表
prerequisites:
  - 已開通 CYBERBIZ 商店後台
devices:
  - desktop
apis: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/business-intelligence/order-analysis/"
icon: lucide/bar-chart-3
hide:
---

![訂單分析頁](../../../assets/images/ec-bi-order-hero.png){ .hero-page }

## 訂單分析說明 { #intro-order-analysis }

「訂單分析」是商店掌握經營成效的報表頁面，從宏觀的銷售趨勢到細部的取消率、退貨率、導購來源，協助您快速看懂訂單的整體健康度。

整個頁面分為三個分頁： **訂單總體分析** 看整體銷售趨勢與健康度指標、 **訂單金物流分析** 看付款與出貨的偏好、 **訂單報表** 提供可下載的業績明細表。部分方案僅會看到「訂單總體分析」，詳見 [使用前提與限制][prerequisites]{ data-preview }。

---

## 頁面功能總覽 { #overview-order-analysis }

| 分頁 | 用途 |
| :-- | :-- |
| 訂單總體分析 | 總訂單數、近 30 日訂單數、訂單金額與商品數分布，以及取消率、退貨率等趨勢。 |
| 訂單金物流分析 | 依付款方式、出貨方式、第三方導購拆解的訂單數、占比、平均客單價與退貨率。 |
| 訂單報表 | 日期區間對比、各時段業績、每日業績三張可下載成 Excel 的表格。 |

完整的分頁顯示條件與方案差異，請見 [訂單分析分頁與方案對照][reference-order-analysis-tabs]{ data-preview }。

---

## 使用前提與限制 { #prerequisites-order-analysis }

### 認列訂單定義 { #prerequisites-order-analysis-recognized-order }

訂單分析的數據並非把所有訂單都算進去，而是只計算「認列訂單」。認列訂單需同時符合兩個條件：

- [x] **訂單狀態**：為「非取消訂單」。
- [x] **退貨狀態**：為「不需退貨或拒絕退貨」。

也就是說，已取消的訂單，以及退貨成立的訂單，都不會被算進銷售數據。

---

### 方案差異 { #prerequisites-order-analysis-plan }

「訂單金物流分析」與「訂單報表」兩個分頁，只在部分方案開放。若您只看得到「訂單總體分析」一個分頁，代表您目前的方案不含另外兩個分頁。

??? plan "哪些方案只看得到「訂單總體分析」？"
    以下四種方案 **只會顯示「訂單總體分析」**，不會出現「訂單金物流分析」與「訂單報表」分頁：

    * 高手版
    * 高手plus版
    * 專業plus版
    * 進階plus版

    其餘方案(例如進階版、專業版、達人級、尊爵版、企業版等)可看到完整三個分頁。如需升級方案以解鎖完整報表，請洽詢您的開店顧問。

---

### 第三方導購圖表的顯示條件 { #prerequisites-order-analysis-third-party }

「訂單金物流分析」中的 **第三方導購** 圖表，需要商店已串接導購平台才會出現。只要符合以下任一條件即會顯示：

* 已設定「美安夥伴商店」
* 已串接「通路王」
* 已串接「LINE購物」

三者皆未啟用時，整組第三方導購圖表不會顯示。

---

## 操作步驟 { #operate-order-analysis }

### 進入訂單分析 { #operate-order-analysis-enter }

1. 於後台左側選單點選 **「分析報表」**。
2. 點選 **「訂單分析」**，即進入訂單分析頁面，預設停在「訂單總體分析」分頁。

---

### 切換分析分頁 { #operate-order-analysis-switch-tab }

頁面上方有分頁標籤，點選即可切換不同的分析角度：

1. 點選 **「訂單總體分析」**，查看整體銷售趨勢與健康度指標。
2. 點選 **「訂單金物流分析」**，查看付款方式、出貨方式與第三方導購的表現。
3. 點選 **「訂單報表」**，查看並下載業績明細表。

!!! info "提示"
    若您只看得到「訂單總體分析」一個分頁，屬於方案差異，請見 [方案差異][prerequisites-order-analysis-plan]{ data-preview }。

---

### 調整圖表與報表的日期區間 { #operate-order-analysis-date-range }

每張圖表與報表都有各自獨立的日期選擇器，可單獨調整想觀察的期間：

1. 點選圖表(或報表)上的 **日期欄位**。
2. 選擇預設區間(最近 7 日、最近 30 日、這個月、上個月)或選「自訂」自行框選起訖日期。
3. 點選 **「套用」**，該圖表即依新的區間重新整理。

!!! note "註釋"
    日期格式為 MM/DD/YYYY。每張圖表是獨立調整的，調整其中一張不會影響其他圖表。

---

### 下載訂單報表為 Excel { #operate-order-analysis-download }

「訂單報表」分頁的三張表格都可以下載成 Excel 進一步分析：

1. 切換到 **「訂單報表」** 分頁。
2. 找到要下載的表格(日期區間對比、時間別業績狀況、每日業績狀況)。
3. 點選該表格右上角的 **「下載為Excel」** 按鈕，檔案即會下載。

各表的欄位意義請見 [訂單報表欄位對照][reference-order-analysis-report-compare]{ data-preview }。

!!! tip "技巧"
    圖表類的區塊(訂單總體分析、訂單金物流分析)本身不提供下載；若需匯出資料，請使用「訂單報表」分頁的三張表格。

---

## 重要規範與限制 { #specs-order-analysis }

* **只計算認列訂單**：所有數據都以 [認列訂單][prerequisites-order-analysis-recognized-order]{ data-preview } 為基礎，已取消與退貨成立的訂單不列入。
* **數據為定時更新、非即時**：報表數據為定時批次計算，並非即時；系統會定時把已取消、已退貨的訂單排除後重新統計，因此與即時的「所有訂單」列表可能略有落差。
* **退貨率以排除取消後計算**：計算退貨率時，會先排除已取消的訂單，再以認列訂單為母數統計。
* **圖表各自獨立**：每張圖表的日期區間是分開設定的，看數據時請留意各圖表目前套用的期間是否一致。

---

## 常見問題 { #faq-order-analysis }

??? quote "為什麼訂單分析的數字和「所有訂單」列表對不起來？"
    [](){ #faq-order-analysis-data-mismatch }
    有兩個主要原因：

    * 訂單分析只計算 [認列訂單][prerequisites-order-analysis-recognized-order]{ data-preview }，已取消與退貨成立的訂單不會被算進去。
    * 報表數據是定時批次更新的，並非即時，因此會比「所有訂單」列表略有延遲。

??? quote "為什麼我看不到「訂單金物流分析」或「訂單報表」分頁？"
    [](){ #faq-order-analysis-missing-tabs }
    這是方案差異。高手版、高手plus版、專業plus版、進階plus版這四種方案只會顯示「訂單總體分析」。如需完整三個分頁，請洽詢開店顧問升級方案，詳見 [方案差異][prerequisites-order-analysis-plan]{ data-preview }。

??? quote "卡片上的「變動值」是什麼意思？"
    [](){ #faq-order-analysis-variation }
    「變動值」比較的是 **過去 30 日** 與 **長期平均** 兩個數值。正值代表近期表現高於長期平均(成長)，負值代表低於長期平均(下滑)，用來快速判斷近期的成長性。

??? quote "為什麼看不到「第三方導購」的圖表？"
    [](){ #faq-order-analysis-no-third-party }
    第三方導購圖表需要商店已串接導購平台才會出現。請確認是否已設定「美安夥伴商店」、串接「通路王」或「LINE購物」其中之一，詳見 [第三方導購圖表的顯示條件][prerequisites-order-analysis-third-party]{ data-preview }。

??? quote "訂單分析的資料可以匯出嗎？"
    [](){ #faq-order-analysis-export }
    可以，但僅限「訂單報表」分頁的三張表格，點選表格右上角的「下載為Excel」即可。圖表類的區塊(訂單總體分析、訂單金物流分析)本身不提供下載。

---

## 參考資料 { #reference-order-analysis }

* [訂單分析分頁與方案對照](references/order-analysis-tabs-reference.md)
* [訂單總體分析指標對照](references/order-analysis-overview-metrics-reference.md)
* [訂單金物流分析圖表對照](references/order-analysis-finance-logistics-reference.md)
* [訂單報表欄位對照](references/order-analysis-report-fields-reference.md)
