---
title: 設定 Google Ads 轉換追蹤
description: ""
created: 2026-03-25 11:23
last_modified:
lang: zh-TW
type: tutorial
status: ""
author: Jase
version: ""
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans:
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=756
  - https://www.cyberbiz.io/support/?p=232
permalink: ""
comments: ""
search:
  exclude: ""
icon: ""
hide:
---

{ .subtitle }

{ .doc-badge }

{ .hero-page }

在 Google Ads 建立轉換追蹤，能協助商家觀測廣告成效、了解客戶行為，並進一步優化廣告精準度。CYBERBIZ 提供與 Google 轉換代碼的串接功能，以下為詳細的設定步驟：

## 開始前的準備

1.  **登入 Google Ads** 並點擊「開始使用」。
2.  **建立廣告活動**：商家必須先建立第一個 Google 廣告活動，方可開始建立轉換追蹤。

## 在 Google Ads 建立轉換動作

1.  **進入轉換頁面**：於側邊欄點擊「**目標**」>「**摘要**」，點擊「**新增轉換動作**」。
2.  **選擇來源**：選擇「**網站**」。
3.  **掃描網址**：輸入官網網址，點擊「**掃描**」。
4.  **手動新增**：點擊「**手動新增轉換動作**」。
5.  **設定轉換詳細資料**：
    *   **目標和動作最佳化**：依需求選擇要追蹤的動作事件（如：購買、加入購物車）。
    *   **轉換名稱**：依需求為此轉換命名。
    *   **價值**：若類別選擇「**購買**」，請選「**為每次轉換指定不同的價值**」；其餘類別建議選擇「為每次轉換指定相同的價值」。
    *   **計算方式**：若無特殊需求，建議選擇「**每次**」。
6.  **完成與取得代碼**：
    *   設定完成後點擊「完成」。若有多個行為要追蹤，請在此頁面**再次點擊「手動新增轉換動作」**，切勿分開建立。
    *   點擊「**同意並繼續**」。
    *   選擇「**使用 Google 代碼管理工具**」頁籤，即可查看並複製「**轉換 ID**」與「**轉換標籤**」。

## 將轉換代碼填入 CYBERBIZ 後台

**路徑：** 「**第三方整合**」 > 「**谷歌 Google 設定**」。

1.  **Google Ads 再行銷**：
    *   將 Google 提供的「**轉換 ID**」填入「**再行銷編號僅數字**」欄位。
2.  **Google Ads 轉換追蹤**：
    *   點擊「**新增轉換追蹤事件**」。
    *   **轉換追蹤事件**：根據您在 Google 端設定的「目標類別」，選擇後台對應的事件（如：購買對應「顧客完成訂單」）。
    *   **轉換追蹤編號**：貼上「**轉換 ID**」。
    *   **轉換追蹤標籤**：貼上對應事件的「**轉換標籤**」。
3.  **儲存設定**。

## 重要注意事項

*   **避免重複埋設**：若先前曾透過 GTM 設定 Google 廣告追蹤，在 CYBERBIZ 後台設定完成後，**必須移除 GTM 中的相關標籤**，以免發生 Code 碼衝突導致數據不準確。
*   **自動化廣告限制**：若商家使用的是由 CYBERBIZ 代管的「**自動化廣告系統**」，則**無法**透過上述方式在個人 Google Ads 帳號中查看數據，需前往 CYBERBIZ 後台查看。
*   **異常排除**：若無法追蹤行為，請檢查後台的「再行銷編號」與「轉換追蹤編號」是否一致，並確認是否為手動新增動作。

## 後續操作

<div class="grid cards" markdown>

- :lucide-import:{ .lg }
  [____]()
  。

- :lucide-ban:{ .lg }
  [____]()
  。

</div>

## 常見問題

??? quote ""

