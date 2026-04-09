---
title: 設定 MBE 帳號授權與資產連結
description: ""
created: 2026-04-07 23:59
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
tnb: trunk
plans:
  - 專業
  - 進階
  - 高手
  - 專業 PLUS 
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2870
  - https://www.cyberbiz.io/support/?p=11341
permalink: ""
comments: ""
search:
  exclude: ""
icon: ""
hide:
---

{ .subtitle }

{ .doc-badge }

![第三方整合 FBE 設定](../../../../assets/images/ec-第三方整合-fbe.png){ .hero-page }

## Facebook Business Extension 說明

「**Facebook 商業擴充套件**」可一次串接 **Conversions API**、**Facebook 像素（Pixel）**、**商品目錄**、**Instagram Shopping** 及 **Facebook 粉絲專頁** 等資產，讓商家能快速將這些資產連結至官網後台，並在一站式管理廣告追蹤、受眾建立與商品推廣。

!!! info "FBE 已更名為 MBE"
    **Facebook Business Extension (FBE)** 已更名為 **Meta Business Extension (MBE)**，功能不變，只是因應 Meta 公司品牌名稱更新而重新命名。

## 設定路徑

1. 登入 CYBERBIZ 管理後台，點選「**第三方整合**」>「**臉書 Facebook 設定（廣告/註冊登入）**」。
2. 在頁面下方找到「Facebook 新版商業擴充套件」區塊，點擊「**開始設定**」啟動流程。

![FBE 開始設定](../../../../assets/images/ec-第三方整合-fb-fbe-開始設定.png)

## 操作步驟教學

1.  **登入 Facebook 帳號：** 瀏覽器若未登入，系統會要求您登入。請確保登入的帳號具備該 **Facebook [商家資產管理組合 :lucide-external-link:](https://www.facebook.com/business/help/486932075688253) (Business Manager, BM)** 相關資產的設定權限。

    ![FBE 登入帳號](../../../../assets/images/ec-第三方整合-fbe-登入fb帳號.png)

    !!! info "確認瀏覽器是否阻擋彈窗"
        若授權頁面未正常跳出，請確認瀏覽器是否已解除 「彈出視窗攔截」。設定教學：[Chrome 允許特定網站彈出視窗 :lucide-external-link:](https://support.google.com/chrome/answer/95472)

2.  **同意授權：** 點選授權以允許 CYBERBIZ 協助將電商官網資料與 Facebook 資料進行連結，這不會影響您原本 BM 的日常操作。

    ![FBE 同意授權](../../../../assets/images/ec-第三方整合-fbe-同意授權.png)

3.  **連結企業資產：** 選擇要串接的粉絲專頁、目錄、廣告帳號及像素 (Pixel)。
    *   **重要提醒：** 您選取的資產擁有權必須屬於該商家資產管理組合，否則無法正確選取。
    *   您也可以在此步驟直接建立新的資產。
    *   建議開啟「**自動進階配對**」，以發揮廣告的最佳成效。
4.  **確認獲得權限：** 此步驟若出現 UI 顯示必填等提示為系統呈現問題，直接點選「下一步」即可。
5.  **完成連結：** 等候連結完成後點選「完成」，系統會自動導回 CYBERBIZ 後台設定頁。

## 設定後的檢查與維護

*   **確認連結狀態：** 回到後台頁面後，可再次確認粉專、像素、目錄的連結結果。
*   **編輯或取消：** 若需重新設定或清空設定，可點選「編輯資產」或「取消連結」。**請注意：** 執行此操作必須登入 **最初設定時使用的同一個 Facebook 帳號**。
*   **轉換 API (CAPI)：** 設定完成後，系統會開始自動傳送伺服器端 (Server to Server) 的像素事件，您可至 Facebook 事件管理工具查看連結方式是否出現「伺服器」。

## 注意事項

*   若在設定過程中遇到權限問題，請務必確認您的帳號是否為該資產的擁有者或具備足夠管理權限。
*   完成初步設定後，建議接續進行 **Step 2：網域驗證與事件設定**，以確保廣告投放的穩定性。


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

