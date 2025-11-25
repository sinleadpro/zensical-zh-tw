---
title: 申請 CYBERBIZ PAYMENTS
description: 設定網站、提交商店資訊，並啟用 CYBERBIZ PAYMENTS。
product:
  - EC
module:
  - Payments
activ: activate
surfaces:
  - backend
devices: []
apis: []
type: tutorial
features:
  - Payment Gateway
tasks:
  - Prepare Application
  - Website Setup
  - Merchant Verification
  - Review Process
  - Activation
plans:
  - PLUS
lang: zh-TW
sites:
  - TW
status: new
tags:
  - Payments
  - Application
difficulty: medium
notes:
  - 一般用戶請參考 [CYBERBIZ PAYMENTS 申請流程](https://www.cyberbiz.io/helpcenter/?p=6174)
  - 補充審核所需的一般時長。
---

# 申請 CYBERBIZ PAYMENTS
:lucide-lock:{ title="適用方案" } | PLUS  
:lucide-sparkles:{ title="適用 CYBERBIZ 擴充功能" } | CYBERBIZ PAYMENTS


CYBERBIZ PAYMENTS 申請流程包含兩個階段：  

- 申請
	- [設定您的網站](#設定您的網站)
	- [填寫申請表](#填寫申請表)
- 審核
	- 風控部門審核商店網站與商店資料  
	- 系統通知審核結果並自動啟用服務
	
??? note "預估時程"
	- 簽署合約： 1–2 個工作天  
	- 審核流程： 5–15 個工作天  
	- 金流啟用： 審核通過後自動啟用
	
??? quote "為什麼要使用 CYBERBIZ PAYMENTS"
	CYBERBIZ PAYMENTS 提供信用卡及其他多元支付的收款與請款服務，並通過 **PCI DSS Level 1 國際安全認證**，協助商家安心收取款項。PLUS 方案用戶可直接線上申請。

## 申請流程

如果您的商店符合資格，系統將透過「後台彈窗通知」及「電子郵件」通知您。  

請依照跳窗指示申請，或依照以下步驟操作：

1. 登入您的 CYBERBIZ 後台，點擊 **金物流 > 金流設定**。
2. 在 CYBERBIZ PAYMENTS 開通區塊中，點擊 **立即申請** 進入申請頁面。
	
如果您尚未符合資格，請先依照[設定您的網站](#設定您的網站)完成網站設定後再進行申請。

### 設定網站
您的網站需要提供足夠識別「商店」和「商品類型」的完整資訊。請透過以下步驟完成：

#### 上傳網站 Logo
`網站外觀 > 套版主題管理 > 網站設定 > 導覽列 > 網站 Logo`

<iframe src="https://scribehow.com/embed/Upload_Website_Logo_Image__svlQbb-6QjSUi1gbYiSMZw" width="100%" height="800" allow="fullscreen" style="aspect-ratio: 1 / 1; border: 0; min-height: 480px"></iframe>

#### 填寫網站名稱
`管理中心 > 一般設定 > 網站名稱`  

1. 在您的 CYBERBIZ 後台，點擊 **網站管理 > 一般設定**。
2. 點擊 **網站名稱** 欄位輸入您的網站名稱。 
> 預設為網址中的英文名稱；請變更為您的品牌或公司名稱。

![](../assets/images/ec-enter-name-of-website.zh-tw.png)

#### 上架至少一件商品
`商品 > 所有商品 > 新增商品`

1. 在 CYBERBIZ 電商後台，點擊 **商品 > 所有商品**。
2. 點擊 **新增商品**。
3. 設定商品基本資訊。
> - [ ] 至少上傳一張商品圖片  
> - [ ] 填寫官方售價  
> - [ ] 建議填寫商品描述與規格

#### 設定聯絡資訊 
`網站外觀 > 套版主題管理 > 網站外觀 > 網站設定 > 頁腳 > 聯絡資訊`  

  <iframe src="https://scribehow.com/embed/Customize_Footer_Contact_Information_Display__O2xyYVgpSFm7ZFEIIeHprw" width="100%" height="800" allow="fullscreen" style="aspect-ratio: 1 / 1; border: 0; min-height: 480px"></iframe>

#### 編輯關於我們頁面
`網站外觀 > 自訂頁面管理 > 關於我們`  

1. 在您的 CYBERBIZ 後台，點擊 **網站外觀 > 自訂頁面管理**。
2. 點擊 **關於我們** 編輯現有頁面。或點擊 **新增頁面** 建立新頁面。  

![](../assets/images/ec-about-us-page-configure.zh-tw.png)

### 填寫申請表
當系統偵測到符合資格時，後台將會出現跳窗。請確認以下設定皆已完成：

- [ ] 設定網站 Logo 及名稱  
- [ ] 至少刊登一件商品  
- [ ] 設定聯絡資訊及關於我們頁面

完成後，請依照指示進入申請頁面，填寫相關資訊，並確認無誤後點擊**提交**，進入審核流程。

## 審核流程
![](../assets/images/cyb-payments-review-process.png)

| 審核狀態 | 說明 |
|---------------|-------------|
| 等待簽約 | 請完成合約簽署；未簽約前審核將不會進行。如有更新，請聯繫您的業務代表。 |
| 審核中 | 風控部門審核網站與商店資料，預計約需 **5–15 個工作天**。 |
| 未通過 | 系統將透過後台公告及電子郵件通知您。請依指示修正資料後重新提交。 [^1] |
| 已開通 | 審核通過後，系統將自動開通 CYBERBIZ PAYMENTS 服務，並透過後台公告及電子郵件通知您。 |

## 常見問題
??? quote "我如何知道金流服務是否已開通？"
	系統將透過**後台公告**及**電子郵件**通知您。
??? quote "如果我的申請被拒絕，是否需要重新填寫所有資料？"
	不需要。只需依照通知中的指示修正遺漏項目後重新提交即可。
	
	[^1]: 或在您的後台，點擊 **金物流 > 金流設定**。在相關區塊中，點擊 **立即申請**。