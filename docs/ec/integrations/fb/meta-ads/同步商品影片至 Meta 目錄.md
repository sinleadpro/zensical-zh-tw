---
title: 同步商品影片至 Meta 目錄
description: ""
created: 2026-04-21 14:27
last_modified: 2026-04-23 11:40
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
tnb: branch
plans:
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
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
  - https://www.cyberbiz.io/helpcenter/?p=7886
  - https://www.cyberbiz.io/support/?p=2175
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/play
hide:
---

{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 專業 PLUS / 進階 PLUS / 高手 PLUS / 企業
{ .doc-badge }

{ .hero-page }


## 同步商品影片至 Meta 目錄說明

此功能使商家能夠將 CYBERBIZ 平台上的產品數據（包含資訊、庫存、價格，以及最重要的 **商品影片**）自動同步到 Meta 的產品目錄中。設定完成後，後續在建立 Meta 廣告時若選擇「[**目錄型廣告**](設定 Meta 廣告活動.md#廣告呈現效果){ data-preview }」，廣告投放時商品影片與商品圖即會輪播展示。

## 設定前提與功能限制

在進行同步前，請務必確認滿足以下條件與規格：

- [x] **商品影片上傳：** 商家必須已於 CYBERBIZ 後台完成[商品影片上傳](../../../products/creation/設定商品影片.md){ data-preview }。
- [x] **擴充套件串接：** 商家必須具備並已串接「[Facebook 新版商業擴充套件](../mbe/設定 FBE 帳號授權與資產連結.md){ data-preview }」功能。
- [x] **版型限制**：商品影片功能目前僅支援 **拖拉版型**，非此版型之商店將無法上傳並同步影片。

## 同步設定步驟

1.  **進入功能：** 登入 CYBERBIZ 管理後台，前往「第三方整合」>「臉書 Facebook 設定（廣告/註冊登入）」，點擊 Facebook 新版商業擴充套件區塊中的「**編輯資產**」，開啟設定視窗。

    ![FBE-編輯資產](../../../../assets/images/ec-第三方整合-fb-基本設定-fbe-編輯資產.png)

2.  **選擇/建立目錄：** 於連結資產頁面中選擇欲同步的商品目錄。

    ![FBE-連結目錄](../../../../assets/images/ec-第三方整合-fb-基本設定-fbe-連結目錄.png)

    *   **💡 專家建議：** 建議點選「**建立新資產**」建立一個全新的目錄。若使用舊目錄，容易因舊有商品資料衝突導致影片資料無法順利更新。

3.  **完成流程：** 依序完成彈窗中的其他設定並點擊「完成」，系統會自動導回 CYBERBIZ 後台頁面。

## 於 Meta 端確認同步狀態

1.  前往 Meta 企業管理平台後台，進入「資料來源」>「目錄」，選擇剛才綁定的目錄。
2.  點擊「**在商務管理工具中開啟**」。
3.  在「目錄」>「資料來源」中，可查看目錄是否已自動同步並更新官網上的商品資料。
    *   **注意 1：** 若有多份資料來源導致新增失敗，請先刪除舊的資料來源再重新更新。
    *   **注意 2：** 在**尚未投放廣告前**，商務管理工具可能看不到影片預覽。您可以嘗試建立廣告，在審核階段暫停，Meta 隨即會幫您載入影片資料。

## 投放 Meta 目錄型廣告 (進階應用)

同步完成後，您可進一步設定 **CPV 廣告 (Catalog Product Video)**，以影片生動展示產品亮點：

1.  **建立活動：** 在 Meta 廣告管理員中點擊「建立」，選擇「**銷售**」目標與「高效速成 + 購物行銷活動 (ASC)」。
2.  **設定創意來源：** 在廣告層級的「廣告創意來源」選擇「**目錄**」，並選取已同步影片的目錄。
3.  **關鍵開關：** 在「高效速成 + 廣告創意」區塊點擊編輯，確保「**活用型影音素材**」選項已開啟，如此廣告才會以商品影片格式呈現。

**💡 溫馨提醒：**
若需重新編輯或取消連結，必須登入**最初設定時使用的同一個 Facebook 帳號**方可操作。完成上述步驟後，請確認已儲值足夠廣告金（門檻為 NT$15,000）以開始投放。

您是否需要我為您進階說明，如何針對特定的「目錄商品組合」來規劃更具效益的影片廣告投放策略？

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

