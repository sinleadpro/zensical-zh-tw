---
title: VIP 功能運作指南
description: 深度解析新版 VIP 系統的滾動式計算、即時觸發判定以及升降等回溯邏輯，協助商家建立精準的會員營運觀念。
created: 2026-01-23 00:00
last_modified: 2026-06-22 11:15
lang: zh-TW
type: guide
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 會員
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 規劃 VIP 制度
  - 理解 VIP 計算邏輯
features:
  - VIP 制度
  - 會員分級
prerequisites: []
related: []
tags: []
acoiv: activate
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > VIP 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7505
  - https://www.cyberbiz.io/support/?p=11860
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/crown
hide: []
---

# VIP 功能運作指南

透過靈活的分級制度與自動化運算引擎，協助您精準識別高價值顧客，並提供差異化的尊榮待遇，建立長期的顧客忠誠度。

## 選擇您的會員體系

根據您的營運策略，您可以選擇建立適用於全站的通用制度，並針對特定客群設計專屬的門檻與權益。

<div class="grid cards" markdown>

- :lucide-users:{ .lg }
  [__全館 VIP 制度__](setup-store-wide-vip-system.md)
  建立全站統一的階層體系，讓所有會員都能透過消費累積逐步晉升。

- :lucide-tag:{ .lg }
  [__專屬 VIP 群組__](create-exclusive-vip-groups.md)
  針對特定標籤會員（如：KOL、員購、大戶）設定獨立的等級規則與門檻。

</div>

## 哪些消費會被計入

並非所有訂單都會計入 VIP 累計金額。系統僅計算「實質完成交易」且「無退貨疑慮」的訂單：

### 會計入 VIP 的「有效訂單」

*   **已付款訂單**：付款狀態為 **已付款**。
*   **貨到付款已收貨訂單**：付款狀態為 **貨到付款**，配送狀態為 **已收貨**。(自訂貨到付款訂單則為 **已出貨**)。
*   **已出貨之結案訂單**：訂單狀態為 **已結案**，且配送狀態為 **未出貨、準備出貨** 以外訂單。

> 以上3種訂單，訂單狀態不可為 **已取消**，退貨狀態需為 **不需退貨**，否則視為無效訂單。

*   **拒絕退貨訂單**：若該筆訂單曾有退貨爭議，但最終標記為 **拒絕退貨**。

### 不計入 VIP 的「無效訂單」

*   **已取消訂單**：訂單狀態為 **已取消**。
*   **退貨訂單**：退貨狀態非 **拒絕退貨** 或 **不需退貨** 的訂單。
*   **部分退貨訂單**：若訂單發生 **部分退貨**，系統預設會排除該整筆訂單金額。

## 系統何時更新等級

### 1. 觸發判定時機

每當會員發生以下行為時，系統會立即針對「該位會員」重新計算等級：

*   **訂單狀態異動**：有效訂單成立、無效訂單成立。
*   **資料變動**：新會員註冊、商家手動修改會員標籤、商家手動增減會員的「其他通路有效訂單」。
*   **版本生效**：當商家發佈了新的 VIP 制度版本並到達生效日。

### 2. 滾動式回溯計算法

系統不看「日曆年」，而是以「觸發當下」往前回溯一段特定的效期。

*   **移動式區間**：想像一個固定寬度（例如 365 天）的時間區間，每當重新計算會員等級時，會以當下時間點往回追溯時間區間內的所有訂單。
*   **新陳代謝**：新訂單成立時會「進入區間」，增加總額；365 天前的舊訂單則會「移出區間」，不再計入總額。

!!! info "為什麼會員累積消費金額會減少？"
    如果一年前的「大額訂單」剛好過期移出計算區間，而新訂單的金額較小，會員看到的累積消費總額就可能下降。

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }
  [__升等 / 降等 / 續會規則__](vip-upgrade-downgrade-renewal-rules.md)
  瞭解 VIP 升等效期計算、降等回溯重計與續會判定時機。

</div>


## 規則生效與版本管理

為了保護消費者權益並給予商家公告緩衝，系統對核心規則的變動設有生效限制。

*   **基本設定（D+2 規範）**：修改層級名稱、升等/續會門檻等核心邏輯後，需於 **2 天後** 才會生效（首次發佈除外）。
*   **優惠設定（即時生效）**：修改折扣折數、贈送點數等回饋內容，儲存後可立即生效。
*   **版本管理**：透過「複製版本」功能，您可以在不影響當前運行版本的情況下，預先規劃下一階段的會員策略。

## VIP 專屬權益應用
將 VIP 制度轉化為實質的行銷推動力，透過專屬優惠與差異化定價，提升會員的客單價與回購率。

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }
  [__VIP 專屬優惠__](setup-exclusive-vip-discounts.md)
  設定整筆訂單折扣、專屬免運門檻、紅利倍數回饋，以及發放 VIP 生日禮與升等禮。

- :lucide-banknote:{ .lg }
  [__會員專屬價格__](../../products/pricing/設定%20VIP%20會員專屬價格.md)
  針對特定商品設定不同 VIP 等級的專屬售價，讓高階會員享有最直接的價格優勢。

</div>
