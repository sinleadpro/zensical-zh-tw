---
title: 設定會員安全與網站保護
description: 管理會員密碼強度、個資隱碼遮蔽與地區黑名單，並可為前台網站設定密碼保護，全方位守護顧客資料與網站存取安全。
created: 2026-08-12 10:59
last_modified: 2026-08-12 10:59
lang: zh-TW
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 管理中心
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 保護顧客隱私
  - 設定會員密碼規則
  - 網站密碼保護
  - 限制地區造訪
features:
  - 會員安全設定
  - 網站密碼
  - 會員密碼規則
  - 會員個資部分隱碼
  - 訪問限制地區黑名單
prerequisites:
  - 需具備「設置」權限
related:
  - ec/website-management/admin-security-settings/
  - ec/website-management/bot-protection-settings/
  - ec/website-management/add-admin-set-permissions/
tags:
  - 會員安全
  - 網站密碼
  - 個資隱碼
  - 黑名單
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 安全性設定 > 會員安全
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3214
comments: false
permalink: "https://help.cyberbiz.io/ec/website-management/member-security-settings/"
search:
  exclude: false
icon: lucide/user-check
hide: []
---

# 設定會員安全與網站保護

透過「會員安全」設定，您可以有效保護網站前台的存取權限，並加強顧客個資的隱私保護與密碼強度。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 全版本
{ .doc-badge }

![安全性設定頁面-hero](../../assets/images/ec-管理中心-安全性設定.png){ .hero-page }

## 安全性設定說明 { #intro-security }

「安全性設定」是 CYBERBIZ 後台的資安控制中心，協助你降低帳號被盜用、顧客個資外洩與惡意造訪的風險。頁面位於後台「管理中心」>「安全性設定」，並分為三個主要防護領域：

- **會員安全**：負責保護網站與顧客資料。
- **[管理員登入](admin-security-settings/)**：負責保護你與員工登入後台的安全。
- **[機器人防護](bot-protection-settings/)**：負責過濾惡意訪客，在簡訊發送前建立第一道防線。
    

## 使用前提與限制 { #prerequisites-security }

開始設定前，請先確認下列條件：

- [x] **「設置」權限**：本分頁區塊需要你的帳號在 **網站權限** 中具備 **設置** 權限，才能檢視與編輯。您可[修改管理員權限](add-admin-set-permissions/#管理者權限設定與修改)。
- [x] **方案／開通**：部分區塊需對應方案或開通功能才會出現。
- [x] **人員身分**：**分店人員** 帳號登入時預設不會顯示「會員安全」分頁。


## 操作步驟 { #operate-security }

前往後台 **管理中心 > 安全性設定** 後，點選上方 **會員安全** 分頁即可開始設定。

### 設定網站密碼 { #operate-security-website-password }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 全方案

為整個網站前台加上密碼，只有知道密碼的顧客才能瀏覽，適合尚未公開上線、或僅對特定客群開放的網站。

1. **進入區塊：** 在 **會員安全** 分頁，找到 **網站密碼** 區塊。
2. **啟用密碼保護：** 勾選 **網站密碼**。
3. **設定密碼：** 在 **密碼** 欄位輸入密碼（上限 64 個字元）。
4. **（選填）留言給顧客：** 在 **傳達顧客的訊息** 輸入提示文字（上限 255 個字元），顧客在輸入密碼的頁面會看到這段訊息。
5. **儲存設定：** 點擊 **儲存** 套用。

![](../../assets/images/ec-管理中心-安全性設定-網站密碼.gif)

!!! note "顧客造訪流程"
    啟用「網站密碼」後，顧客造訪任何前台頁面時，系統會先跳出密碼輸入頁。顧客必須正確輸入密碼，通過後方可瀏覽網站內容。
    若要切換為 **公開模式讓所有顧客自由瀏覽**，請 **取消** 此設定。


### 會員密碼規則 { #operate-security-customer-password-rule }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 選配

規範顧客註冊或設定會員密碼時的強度。

1. **進入區塊：** 在 **會員安全** 分頁找到 **會員密碼規則** 區塊。
2. **設定長度限制：長度限制** 為必填，輸入會員密碼的最小與最大字元數。
3. **加上組成要求：** 視需要勾選 **包含數字**、**包含大寫字母**、**包含小寫字母**、**包含特殊符號**。
4. **儲存設定：** 點擊 **儲存** 套用。

![](../../assets/images/ec-管理中心-安全性設定-會員密碼規則.png)


### 訂單明細會員個資隱碼 { #operate-security-pdpa }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 所有PLUS / 企業

將顧客的姓名、手機、地址等個資以隱碼（如星號）遮蔽。此功能僅針對訂單明細列印生效，且 **需開通** 後才會顯示。

1. **進入區塊：** 在 **會員安全** 分頁，找到 **會員個資部分隱碼** 區塊。
2. **啟用功能**：勾選 **訂單明細列印**。
3. **儲存設定：** 點擊 **儲存** 套用。

!!! info "遮罩規則"
    | 欄位 | 遮罩規則 | 範例 |
    | :-- | :-- | :-- |
    | 姓名 | 保留首字與末字 | 劉 \*\*\*\* 權 |
    | 手機 | 保留前三碼與末一碼 | 093 \*\*\*\*\* 3 |
    | 地址 | 保留郵遞區號、前段與末字 | 10001 台北市松山 \*\*\*\*\* 路 |

![](../../assets/images/ec-管理中心-安全性設定-會員個資部分隱碼.png)



### 訪問限制地區黑名單 { #operate-security-restricted-locations }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 企業 / 跨境

封鎖特定地區的顧客造訪網站前台，常用於跨境經營時排除特定市場。

1. **進入區塊：** 在 **會員安全** 分頁找到 **訪問限制地區黑名單** 區塊。
2. **選擇限制地區：** 點擊 **限制地區** 欄位，於選單中勾選要封鎖的國家或地區。
3. **儲存設定：** 點擊 **儲存** 套用。設定後，名單中地區的顧客將無法造訪你的網站前台。

![訪問限制地區黑名單](../../assets/images/ec-管理中心-安全性設定-會員登入-訪問限制地區黑名單.png)


