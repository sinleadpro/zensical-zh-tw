---
title: 設定 Facebook 快速登入
description: ""
created: 2026-03-31 11:23
last_modified: 2026-04-08 16:35
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
modules:
  - 第三方整合
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
wp_url: []
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/log-in
hide:
---

{ .subtitle }

![第三方整合-FB](../../../assets/images/ec-第三方整合-fb整合.png){ .hero-page }

## Facebook 快速登入說明

**Facebook 快速登入** 功能可讓顧客於「會員註冊」或「結帳頁面」直接使用 Facebook 帳號登入，系統會自動抓取其 Facebook 綁定的信箱作為帳號，並將資料與官網顧客列表關聯，方便商家後續篩選受眾。

## 設定前的注意事項

- **網址安全性：** 官網網址必須具備 **SSL 憑證**（即 https:// 開頭）。
- **企業驗證：** 所使用的 Facebook 企業管理平台（BM）需先完成驗證。
- **網域重新導向：** 請確認後台「網域管理」中，「總是將顧客重新導向到這裡」勾選的是 Facebook 所設定的網域。
- **信箱限制：** 若消費者使用 Hinet 信箱，可能會因 Hinet 阻擋訊息而無法收到忘記密碼等系統通知，建議引導使用其他信箱。
- **帳號合併機制：** 若顧客的 Facebook 信箱與 Google 或 LINE 登入使用的信箱相同，系統會自動將其判定為同一會員並進行 **帳號合併**。

## 快速登入功能設定

商家可以根據需求選擇使用「預設圖示」或「自訂圖示」來設定登入畫面中顯示的商家 logo：

=== ":lucide-zap: 預設圖示"

    ![FB 快速登入預設圖示](../../../assets/images/ec-第三方整合-fb-預設圖示-前台.png)

=== ":lucide-wrench: 自訂圖示"

    ![FB 快速登入自訂圖示](../../../assets/images/ec-第三方整合-fb-自訂圖示-前台.png)

!!! note "自訂圖示、預設圖示，僅在前台顯示圖示會有差異。"

### 使用預設圖示（最快速）

*   **後台路徑：** 「第三方整合」>「臉書 Facebook 設定 (廣告/註冊登入)」。
*   **操作步驟：** 開啟「**啟用 Facebook 登入**」並點擊「儲存設定」即可完成，前台會顯示系統預設的登入按鈕。

![FB 快速登入設定](../../../assets/images/ec-第三方整合-fb快速登入開啟.png)

---

### 使用自訂圖示（需建立 Meta 應用程式）

此方法需透過 **Meta for Developers** 建立應用程式，適合希望自訂登入圖示與蒐集更完整受眾資訊的商家。

!!! warning "前置條件：註冊 Meta 開發者帳號"
    在建立應用程式之前，您需要先完成 [**Meta for Developers 開發者帳號註冊** :lucide-external-link:](https://developers.facebook.com/docs/development/register)。完成註冊後，即可前往應用程式頁面建立應用程式。

#### 建立應用程式

1. 前往 [Meta for Developers :lucide-external-link:](https://developers.facebook.com/apps/)，確認已登入開發者帳號。
2. 點擊「**建立應用程式**」。
3. 輸入「顯示名稱」（顧客登入時看到的店家名稱）並點擊「**繼續**」。
4. 選擇「**使用 Facebook 登入，驗證用戶並索取資料**」作為使用案例。
5. 選擇是否連結「[商家資產管理組合 :lucide-external-link:](https://www.facebook.com/business/help/486932075688253)」（如無可選選項，可選擇「我還不想連結商家資產管理組合」）。
6. 按照畫面提示，完成[商家驗證](#商家驗證-business-verification)與[應用程式審查](#應用程式審查-app-review)要求。
7. 檢視總覽並點擊「**建立應用程式**」完成建立。

![建立應用程式流程](../../../assets/images/ec-第三方整合-mbe-建立fb登入應用程式.gif){ .screenshot }

---

#### 設定 Facebook 登入產品

1. 應用程式建立完成後，會自動進入應用程式主控台。
2. 在「應用程式自訂和要求」區塊，點擊「自訂使用 Facebook 登入以驗證用戶並索取資料的使用案例」。

    ![應用程式主控台](../../../assets/images/ec-第三方整合-fb-應用程式主控台.png){ .screenshot }

3. 進入「權限和功能」頁籤，點擊 `email` 和 `public_profile` 旁邊的「新增」按鈕以建立相關權限。

    ![權限和功能](../../../assets/images/ec-第三方整合-fb-權限和功能.png){ .screenshot }

4. 切換到「設定」頁籤，設定有效的 OAuth 重新導向 URL，其他設定可使用預設值。

    !!! tip "先確認網域類型"

        請先確認您的網域類型，以組合正確的 **OAuth 重新導向 URL**。後台路徑：**管理中心 > 網域管理**。

        請根據您的網域類型，將 `/customer/auth/facebook/callback` 接在網域後方：

        - **自有網域：** `https://www.你的網域.com/customer/auth/facebook/callback`
        - **CYBERBIZ 網域：** `https://你的店名.cyberbiz.co/customer/auth/facebook/callback`

    !!! warning "網址輸入完成後（請按 ++enter++ ），請確認該網址是否已自動轉換為 **藍色方塊標籤** 格式。若未轉換，該網址將無法生效。"

    ![設定 OAuth URL](../../../assets/images/ec-第三方整合-fb-oauth設定.png){ .screenshot }

5. 點擊 **儲存** 以套用變更。

---

#### 填寫應用程式基本資料

1. 在左側選單點擊「應用程式設定」>「基本資料」。
2. 填寫以下欄位：
    - **隱私政策網址：** 填入官網隱私權政策頁面網址（需在首頁有連結）。例如：`https://test.cyberbiz.co/pages/privacy`
    - **服務條款網址：** 填入官網服務條款頁面網址（需在首頁有連結）。例如: `https://test.cyberbiz.co/pages/terms`
    - **資料刪除指示網址：** 選擇「資料刪除指示網址」，通常填入隱私權政策網頁。
    - **應用程式圖示：** 上傳商店 Logo（建議 1024x1024 像素）。
    - **類別：** 選擇應用程式類別，如商業與粉絲專頁。
3. 點擊「儲存變更」。

!!! warning "檢查必要資訊"
    若有缺少必要資訊，目前不符合提交資格的提示訊息中會顯示缺少資訊，請確認皆已符合。

![基本資料設定](../../../assets/images/ec-第三方整合-fb-基本資料.png){ .screenshot }

---

#### 取得權限與驗證

完成基本資料設定後，需完成「商家驗證」與「應用程式審查」才能發佈應用程式。在應用程式主控板可查看「商家驗證」與「應用程式審查」的狀態。

![應用程式主控板-驗證與審查狀態](../../../assets/images/ec-第三方整合-fb-應用程式-主控台.png){ .screenshot }

---

##### 商家驗證（ Business Verification）

1. 在主控板頁面點擊「商家驗證」，系統會引導你連結「商家資產管理組合」以完成商家驗證。

    ![商家驗證頁面-連結商家資產管理組合](../../../assets/images/ec-第三方整合-fb-商家驗證-商家資產管理組合連結.gif){ .screenshot }

2. 如果你還沒有商家資產管理組合，需先建立一個。點擊「建立商家資產管理組合」並依序填寫：
    - **商家名稱**：輸入你的品牌或公司名稱
    - **聯絡資料**：填入姓名及電子郵件（Email），以建立企業管理平台（Meta Business Suite）的管理員帳戶。

    ![商家驗證頁面-建立商家資產管理組合](../../../assets/images/ec-第三方整合-fb-商家驗證-建立商家資產管理組合.png)

3. 選擇已建立的商家資產管理組合，點擊 **connect** 建立連結，若該資產管理組合尚未經驗證，頁面會引導至驗證畫面。

    ![商家驗證畫面-連結商家資產管理組合](../../../assets/images/ec-第三方整合-fb-商家驗證-連結商家資產管理組合.png)

4. 點擊 **開始驗證** 進入相關驗證流程，請依照畫面提示操作。完成驗證後，你的商家資產管理組合狀態會顯示為「已驗證」。

    ![商家驗證畫面-驗證商家資產管理組合](../../../assets/images/ec-第三方整合-fb-商家驗證-驗證商家資產管理組合.png)

5. 回到應用程式頁面，點擊「連結商家資產管理組合」，選擇已驗證的商家資產管理組合並確認連結。

---

##### 應用程式審查（ App Review）

7. 完成商家驗證後，點擊「應用程式審查」提交應用程式審查。
8. 根據你需要的權限（如 `email`、`public_profile`），填寫相關的資料使用說明：
    - 說明你的應用程式為何需要存取這些資料
    - 提供隱私政策網址
    - 說明資料的儲存方式與使用目的
9. 提交審查後，等待 Meta 審核通過（通常需要 1-3 個工作天）。

!!! tip "驗證與審查狀態查詢"
    在主控板可以隨時查看「商家驗證」與「應用程式審查」的狀態，確保兩者都顯示「已完成」或「已核准」後，即可發佈應用程式。

---

#### 串接資料至 CYBERBIZ

1. 在「基本資料」頁面取得「**應用程式編號**」（App ID）與「**應用程式密鑰**」（App Secret，點擊「顯示」查看）。
2. 回到 CYBERBIZ 後台「第三方整合」>「臉書 Facebook 設定 (廣告/註冊登入)」。
3. 將兩組編號貼入對應欄位並點擊「儲存設定」。

![CYBERBIZ 後台設定](../../../assets/images/ec-第三方整合-fb-快速登入-後台設定.png){ .screenshot }

!!! info "應用程式編號與密鑰位置"
   - **應用程式編號 (App ID)**：位於應用程式儀表板頂部或「設定」>「基本資料」
   - **應用程式密鑰 (App Secret)**：位於「設定」>「基本資料」> 點擊「顯示」

---

## （舊版）使用自訂圖示（舊版介面）

此方法需透過 **Meta for Developers** 建立應用程式，適合希望自訂登入圖示與蒐集更完整受眾資訊的商家。

1.  **建立應用程式：**
    *   前往 [Meta for Developers :lucide-external-link:](https://developers.facebook.com/apps)，使用您的個人 Facebook 帳號登入或建立新帳戶，點擊「建立應用程式」。
    *   選擇應用程式類型為「**消費者**」。
2.  **設定 Facebook 登入產品：**
    *   在應用程式內新增「Facebook 登入」產品，並選擇「**www 網站**」。
    *   輸入商店首頁網址（需為 https）並儲存。
3.  **填寫應用程式基本資料：**
    *   **顯示名稱：** 顧客登入時看到的店家名稱。
    *   **隱私政策與服務條款：** 需填入官網對應的頁面網址。
    *   **用戶資料刪除：** 選擇「資料刪除指示網址」，通常填入隱私權政策網頁。
    *   **應用程式圖示：** 上傳商店 Logo（建議 1024x1024 像素）。
4.  **設定有效的 OAuth 重新導向 URL：**
    *   在「Facebook 登入」的設定中，找到「有效的 OAuth 重新導向 URL」欄位。
    *   填入：`https://你的網址/customer/auth/facebook/callback`。
5.  **取得進階權限與驗證：**
    *   至「應用程式審查」>「權限和功能」，確保 `email` 和 `public_profile` 已取得授權。
    *   **商家驗證：** 自 2023 年 2 月起，若需進階層級存取權限，必須完成臉書的商家驗證。
6.  **串接資料至 CYBERBIZ：**
    *   複製應用程式的「**應用程式編號**」與「**應用程式密鑰**」。
    *   回到 CYBERBIZ 後台的 Facebook 設定頁面，將兩組編號貼入對應欄位並儲存。


## 後續操作

<div class="grid cards" markdown>

- :lucide-import:{ .lg }
  [____]()
  。

- :lucide-ban:{ .lg }
  [____]()
  。

</div>

## 常見異常解決辦法

1.  **應用程式不支援登入：** 通常與 FB 應用程式審核或 API 版本過舊有關。建議至 Facebook for Developers 查看是否有警示訊息或「年度資料檢查」未執行。
2.  **無法取得信箱權限：** 需確認應用程式的 `email` 權限是否設定為「Advanced Access」級別。
3.  **FB 登入功能停用：** 由於 Facebook 不再支援 Android 內嵌瀏覽器的登入驗證，若顧客遇到此問題，請引導其**下載並使用 Facebook APP** 開啟登入。

您是否需要我進一步說明，如何透過「Facebook 商業擴充套件」來設定 Facebook 像素 (Pixel) 以追蹤廣告轉換成效？

## 常見問題

??? quote "為什麼會出現「此應用程式目前不支援 Facebook 登入」的錯誤？"

    通常與 FB 應用程式審核或 API 版本過舊有關。建議至 Facebook for Developers 查看是否有警示訊息或「年度資料檢查」未執行。

??? quote "無法取得顧客的 Email 信箱該怎麼辦？"

    需確認應用程式的 `email` 權限是否設定為「Advanced Access」級別。

??? quote "為什麼在 Android 內嵌瀏覽器中無法使用 Facebook 登入？"

    由於 Facebook 不再支援 Android 內嵌瀏覽器的登入驗證，若顧客遇到此問題，請引導其**下載並使用 Facebook APP** 開啟登入。

