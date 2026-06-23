---
title: OMO 分析報表共用定義
description: OMO 分析報表各頁籤共用的統計基準與名詞定義，供教學文件以連結引用。
created: 2026-06-23 10:00
last_modified: 2026-06-23 10:00
lang: zh-TW
type: reference
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - ec
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans: []
cyb_extensions: []
feature_badges: []
intents: []
features: []
prerequisites: []
related:
  - "[[omo-analysis-report]]"
tags:
  - OMO
  - 全通路
  - 有效訂單
  - 回購率
  - 平均訂單金額
  - AOV
  - 營收熱點圖
  - 比較區間
  - POS
  - 參考資料
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: https://help.cyberbiz.io/ec/business-intelligence/references/omo-definitions-reference/
comments: false
search:
  exclude: false
icon: lucide/table
hide:
---

# OMO 分析報表共用定義

OMO 分析報表各頁籤共用的統計基準與名詞定義，集中整理於此，供教學以連結引用。
{ .subtitle }

### 有效訂單定義 { #reference-omo-valid-order }

報表上方標示了「有效訂單定義」，OMO 分析報表的所有數字皆以有效訂單為計算基礎。有效訂單須同時符合下列兩個條件：

- [x] **訂單狀態**：為非取消訂單。
- [x] **退貨狀態**：為不需退貨或拒絕退貨。

也就是說，已取消、已退貨的訂單 **不會** 計入報表的各項數字。這也是報表數字可能與訂單列表總金額不一致的主要原因。

---

### 數據更新時間 { #reference-omo-update-time }

報表的數字並非即時統計，而是定時批次更新：

- **流量、轉換率數據**：於隔日下午五點半更新。
- **其餘數據（含營收、訂單、會員等）**：於隔日凌晨零點更新；取消及退貨訂單會定時更新排除。

!!! note "註釋"
    因為是隔日更新，本報表數字通常反映到「前一天」為止，當天剛成立的訂單與剛註冊的會員不會立即出現，屬正常現象。

---

### 比較區間選項對照表 { #reference-omo-compare }

設定分析區間時，可選擇一個比較基準，報表會將所選時間區間的數字與比較區間並列對比：

| 選項 | 說明 |
| :-- | :-- |
| 前一年 | 與所選區間的「去年同期」比較 |
| 前一時段 | 與所選區間往前推一段「相同長度」的時段比較 |
| 前一月 | 與所選區間的「前一個月」比較 |
| 自訂區間 | 自行指定另一段日期作為比較基準 |

!!! note "註釋"
    比較區間預設為「前一年」。選擇「自訂區間」時，需另外指定比較用的起訖日期。

---

### 名詞定義對照表 { #reference-omo-glossary }

| 名詞 | 說明 |
| :-- | :-- |
| 營收 / 營業額 | 指定時間 EC、POS 的營業額，並與比較區間對比 |
| 訂單數 | 指定時間 EC、POS 的訂單數量，並與比較區間對比 |
| 註冊會員數 | 指定時間於各通路（EC、POS）的新註冊會員數，並與比較區間對比 |
| 平均訂單金額（AOV）| 指定時間的「總營業額 ÷ 總訂單數」，並與比較區間對比 |
| 回購率 | 指定時間內回頭客的百分比，計算為「該期間回頭客數 ÷ 該期間有消費客戶總數」 |
| POS快速登入會員完成註冊率 | 由 POS 快速註冊的會員，完成填寫資料、註冊流程的比率；若商店設定不需驗證帳號即可註冊、結帳，則直接視為完成註冊 |
| 營收熱點圖 | 以顏色深淺呈現各時段營收高低，顏色越深代表該時段訂單營收越高，可作為安排行銷操作時段的參考 |
| 門市取貨 / POS門市取貨 | 顧客選擇至門市取貨的訂單，用於掌握線上線下導購轉單的成效 |
| 會員購買 / 回購狀況 | 以會員「首次註冊來源」區分 EC、POS 會員，比較其在各通路的購買與回購表現 |
| 紅利使用數 | 指定時間於 EC、POS 使用（折抵）的紅利點數 |

!!! note "註釋"
    「會員購買狀況」與「會員回購狀況」皆以會員的首次註冊來源（EC 或 POS）作為分群依據，而非以下單通路區分。
