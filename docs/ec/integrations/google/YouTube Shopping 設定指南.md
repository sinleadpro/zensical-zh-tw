---
title: YouTube Shopping 設定指南
description: 透過 YouTube Shopping 在影片、直播、短影音中植入商品資訊與連結，提升商品曝光與流量變現。
created: 2026-03-27 10:49
last_modified: 2026-03-30 12:35
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
  - 第三方整合
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: branch
plans:
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents:
  - 設定 YouTube Shopping
  - 在 YouTube 銷售商品
  - YouTube 直播購物
features:
  - YouTube Shopping
  - Google Merchant Center
  - 產品動態饋給
  - YouTube 合作夥伴計畫
prerequisites:
  - "[[設定 Google Merchant Center 並同步 CYBERBIZ 商品]]"
  - "[[建立並串接 Google Analytics]]"
related:
  - "[[設定 GMC 重要事件來源追蹤與自動標記]]"
acoiv: integration
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 谷歌 Google 設定 > Google Merchant Center
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10552
  - https://www.cyberbiz.io/support/?p=6118
  - https://www.cyberbiz.io/helpcenter/?p=10555
  - https://www.cyberbiz.io/support/?p=1979
  - https://www.cyberbiz.io/helpcenter/?p=10556
  - https://www.cyberbiz.io/support/?p=6149
permalink: ""
comments: ""
search:
  exclude: false
icon: lucide/youtube
hide: []
---

透過 YouTube Shopping 在影片、直播、短影音中植入商品資訊與連結，提升商品曝光與流量變現。
{ .subtitle }

## 什麼是 YouTube Shopping

**YouTube Shopping** 可在 YouTube 影片、直播、短影音中植入官網商品資訊與連結。商家若有製作影片、經營 YouTube 頻道、在 YouTube 直播，可進一步設定以增加商品曝光、促進流量變現。[瞭解更多 :lucide-external-link:](https://support.google.com/youtube/answer/12257682?hl=zh-Hant)

!!! warning "適用對象"
    YouTube Shopping 為 **YouTube 合作夥伴計畫 (YPP)** 功能，適用於已有 YouTube 頻道並達到營利門檻（訂閱 1,000 人 + 觀看時數 4,000 小時）的創作者。

## YouTube Shopping 設定流程

```mermaid
graph LR
    %% --- 第一階段 ---
    subgraph S1 [第一階段：帳號建立]
        direction TD
        A1([建立並串接 GMC]) --> A2([建立並串接 GA4])
    end

    %% --- 第二階段 ---
    subgraph S2 [第二階段：YPP 資格申請]
        direction TD
        B1([確認資格]) --> B2{達到門檻}
        B2 -- 未達標 --> B3([累積訂閱/觀看])
        B2 -- 已達標 --> B4([直接線上申請])
        B4 --> B5([AdSense 驗證])
    end

    %% --- 第三階段 ---
    subgraph S3 [第三階段：連結與營運]
        direction TD
        C1([連結 GMC 與 GA4])
        C1 --> C2([YouTube 連結商店])
        C2 --> C3([上傳 Product Feed])
        C3 --> C4([28天更新與追蹤])
    end

    %% 跨階段連接
    S1 --> S2
    S2 --> S3
```

## **第一階段：帳號建立與後台綁定**

在申請 YouTube Shopping 之前，必須先完成 Google 兩大工具的串接。

<div class="grid cards" markdown>

-   :lucide-tags:{ .lg .middle } __建立並驗證 GMC 帳號__

    ---

    進入 Google Merchant Center (GMC) 完成商家基本資訊設定，並確認商店所有權完成驗證。

    [:lucide-arrow-right: 設定教學](設定 Google Merchant Center 並同步 CYBERBIZ 商品.md){ data-preview }    

-   :lucide-chart-no-axes-column-increasing:{ .lg .middle } __建立並串接 GA4 帳號__

    ---

    在 Google Analytics 後台取得 「評估 ID」，前往 CYBERBIZ 後台填入評估 ID 完成串接。

    [:lucide-arrow-right: 設定教學](ga/建立並串接 Google Analytics.md){ data-preview }

</div>

## **第二階段：YPP 資格申請**

商家頻道必須具備 [**YouTube 合作夥伴計畫 (YPP)** :lucide-external-link:](https://support.google.com/youtube/answer/72851?hl=zh-Hant&ref_topic=9153642) 的營利資格才能開啟購物功能。

1.  **確認資格**：登入 [YouTube Studio :lucide-external-link:](https://studio.youtube.com/)，點選左側選單的「營利」。若顯示綠色星星，代表尚未擁有資格。

    ![YouTube Studio 營利頁面](../../../assets/images/yt-ypp-營利頁面-blurred.png){ .screenshot }

2.  **線上申請**：當訂閱人數達 1,000 人且觀看時數達 4,000 小時（或 Shorts 觀看次數達 1,000 萬次）時，即可直接透過 YouTube Studio 申請 YPP 資格。資格與申請詳情，請參考[官方說明 :lucide-external-link:](https://support.google.com/youtube/answer/72851?hl=zh-hk&co=GENIE.Platform%3DDesktop)。
3.  **完成 AdSense 驗證**：申請通過後，在 YouTube Studio 後台點選「收取款項」並開始使用，填寫個人資訊以完成 AdSense 註冊。[瞭解詳情 :lucide-external-link:](https://support.google.com/youtube/answer/11602441?hl=zh-Hant&ref_topic=11449917&sjid=3703724191269892924-NC)。

## **第三階段：申請與連結商店**

當上述帳號與資格皆準備完成後，即可進行最後的連結步驟。

1.  **連結 GMC 與 GA4**：在 Merchant Center 設定中啟用自動標記，並將 [GA4 連結至 Merchant Center](設定%20GMC%20重要事件來源追蹤與自動標記.md#將-ga4-連結至-merchant-center){ data-preview }。
2.  **連結 YouTube 頻道與官網**：進入 [YouTube Studio :lucide-external-link:](https://studio.youtube.com/) 的「營利」>「購物」分頁，點選「連結商店」，並選擇「其他商店」後指定您的 GMC 帳號。設定詳情，看參考[官方說明 :lucide-external-link:](https://support.google.com/youtube/answer/12258186?sjid=15941351074417695736-NC#)

    ![YouTube Studio 連結商店 GIF](../../../assets/images/yt-第三階段-連結Youtube商店.gif){ .screenshot }

3.  **上傳產品動態饋給 (Product Feed)**：
    - **獲取連結**：登入 CYBERBIZ 管理後台，前往 第三方整合 > 谷歌 Google 設定 > Google Merchant Center，複製「產品動態饋給連結」。

        ![GMC CYB 產品動態饋給](../../../assets/images/ec-第三方整合-google-gmcproductfeed.png)

    - **匯入 GMC**：進入 GMC 後台，依序點擊 產品 > 所有產品 > 加入產品 > 新增其他產品來源，並貼入剛才複製的連結。

        ![GMC 新增產品來源](../../../assets/images/ec-gmc-新增產品來源.gif)

    - **啟用 YouTube 目的地**：在「行銷方式」設定中，務必勾選 YouTube 商店，並點擊儲存以確保商品能同步至 YouTube 平台。

        ![GMC 產品行銷方式 YouTube 商店](../../../assets/images/ec-gmc-產品行銷方式-youtube商店.png)
     
    - **完成與手動更新**：點擊「繼續」完成設定。進入來源詳情頁面後，點擊「更新」可強制系統抓取最新商品資訊。

        ![GMC 產品來源詳情](../../../assets/images/ec-gmc-來源詳情.png)

        !!! warning "商品自動下架機制"
            若動態饋給上的商品資訊 **超過 30 天** 未在 GMC 更新，將會從 YouTube 自動下架。建議商家 **每 28 天** 操作一次更新以維持狀態。

## 追蹤 YouTube Shopping 成效

透過 GA4 探索功能追蹤 YouTube Shopping 帶來的網站轉換成效。

1.  **建立新報告**：在 GA4 後台左側選單點選「探索」，點選「空白」。

2.  **加入總收益/工作階段指標**：點選「指標」>「收益」> 勾選「總收益」以及「工作階段」> 勾選「工作階段」，並點擊確認。

    ![GA4 指標-工作階段與總收益](../../../../assets/images/ec-ga4-探索-指標-工作階段與總收益.gif)

3.  **加入維度**：點選「維度」>「流量來源」> 勾選「工作階段手動字詞」> 「確認」。

    ![GA4 維度-工作階段手動字詞](../../../../assets/images/ec-ga4-探索-維度-工作階段手動字詞.png)

4.  **設定篩選條件**：
    - 「列」加入「工作階段手動字詞」
    - 「值」加入「工作階段」
    - 「值」加入「總收益」
    - 「篩選器」加入「工作階段手動字詞」，條件設定為「開頭為」「UC」

    ![GA4 探索-篩選條件設定](../../../../assets/images/ec-ga4-探索-篩選條件設定.gif)

6.  **設定期間**：點擊日期選單，可選擇時間區間查看指定時段資料。

    ![GA4 探索-日期選單](../../../../assets/images/ec-ga4-探索-日期選單.gif)

## **直播小秘訣**

在 YouTube 直播時，商家可以預先安排直播時間並產出網址進行宣傳。直播進行中，建議利用 **「直播置頂」** 功能，將預先建立好的商品頁面（如一頁式商店）網址釘選在留言區，讓消費者能更直觀地選購商品。

## 後續操作

<div class="grid cards" markdown>

- :lucide-play:{ .lg }   
  [__在影片內容中標記產品__:lucide-external-link:](https://support.google.com/youtube/answer/10191533)  
  在上傳的 YouTube 影片中標記商品，讓觀眾可直接點擊購買。

- :lucide-video:{ .lg }   
  [__在直播中標記產品__:lucide-external-link:](https://support.google.com/youtube/answer/12299016)  
  在 YouTube 直播時即時標記商品，即時推廣產品。

- :lucide-megaphone:{ .lg }   
  [__直播購物宣傳技巧__:lucide-external-link:](https://support.google.com/merchants/answer/12375318)  
  透過 YouTube 直播購物功能宣傳產品的最佳實踐與技巧。

</div>

## 常見問題

??? quote "申請 YouTube Shopping 需要什麼資格？"

    YouTube Shopping 為 **YouTube 合作夥伴計畫 (YPP)** 功能。商家需擁有 YouTube 頻道，並達到營利門檻（訂閱 1,000 人 + 觀看時數 4,000 小時，或 Shorts 觀看次數達 1,000 萬次）才能申請。

??? quote "如何將 CYBERBIZ 商品同步到 YouTube？"

    請依序執行以下步驟：

    1. 在 CYBERBIZ 後台取得「產品動態饋給連結」（第三方整合 > 谷歌 Google 設定 > Google Merchant Center）。
    2. 進入 GMC 後台，加入產品來源並貼入連結。
    3. 在「行銷方式」中勾選 YouTube 商店並儲存。

??? quote "商品為什麼會從 YouTube 自動下架？"

    若動態饋給上的商品資訊 **超過 30 天** 未在 GMC 更新，將會從 YouTube 自動下架。建議商家 **每 28 天** 操作一次更新以維持狀態。

