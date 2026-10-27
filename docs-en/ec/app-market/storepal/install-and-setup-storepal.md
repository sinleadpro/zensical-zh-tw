---
title: "Install and Set up Store Assistant"
description: "Learn how to install Store Assistant and complete the prerequisites, including LINE certification, member registration rules, and store data preparation, so you can complete your OMO integration smoothly."
created: 2026-06-18 16:00
last_modified: 2026-07-01 12:00
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules:
  - "Store Assistant"
  - APP MARKET
  - 管理中心
  - 訊息推播
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions:
  - STORE PAL
intents: 
  - 安裝門市助理
  - 設定門市助理前置資料
  - 串接 LINE Certified Provider
features: 
  - 門市助理
  - LINE 整合
  - 會員綁定
prerequisites: 
  - "需為企業版方案商家"
  - "需啟用新版 VIP 制度"
related: []
tags: 
  - 門市助理
  - "Installation Guide"
  - "LINE Certification"
  - OMO
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 我的擴充服務
  - 顧客註冊設定
  - 簡訊通知樣板
paths:
  - APP MARKET > 我的擴充服務
  - 管理中心 > 顧客註冊設定
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=41626
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/install-and-setup-storepal/"
search:
  exclude: false
icon: lucide/store
hide: []
---

# Install and Set up Store Assistant
Learn how to install Store Assistant and complete the prerequisites, including LINE certification, member registration rules, and store data preparation, so you can complete your OMO integration smoothly.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

!!! tip "Use Cases"
	- **OMO Member Integration**: With a Store Assistant QR code, customers can add your LINE account as a friend, register on your online store, and link a referrer in one step in store.
	- **Store Sales Tracking**: Assign online store members to specific stores or staff to measure each store's contribution accurately.
	- **Real-Time Digital Service**: Store staff can view member assets on mobile devices and offer personalized service.


## Before You Start { #prerequisites-storepal-install }

- **How to Apply**: If you have not purchased Store Assistant yet, contact your CYBERBIZ customer service consultant or fill out the [application form](https://docs.google.com/forms/d/e/1FAIpQLScAzqU3OckpsS-XBy3yvioKksDBazronFTuEl_RBonxCATHaQ/viewform).
- **System Limitation**: Store Assistant supports only the **new VIP system**. Merchants on the old VIP system cannot use it.
- **LINE Certification Recommendation**: We strongly recommend applying for **LINE Certified Provider** status. With it, scanning the QR code opens a LIFF URL directly, greatly simplifying registration and linking.
- **SMS Reminder**: Turning on mobile verification sends SMS messages.



## Setup Steps { #operate-storepal-install }

### Step 1: Check the Installation Status { #operate-storepal-install-step-status }

After purchase, the CYBERBIZ consultant team helps with the initial installation.

1. Log in to the CYBERBIZ admin and go to **APP MARKET > My Apps**.
2. Make sure **Store Assistant** appears in the installed list.
3. Click **Settings** to open its management interface.

	![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置01.png){ .screenshot }

### Step 2: Set up LINE { #operate-storepal-install-step-line-settings }

To make QR code linking work smoothly, complete LINE certification and connections.

1. **LINE Developers Settings**: Go to [LINE Developers](https://developers.line.biz/) and make sure your LINE OA and LINE Login channel are connected.
2. **Turn On LINE Quick Login**: In the admin, complete the [quick login settings]() under **Third-Party Integration > LINE Login**.
3. **Official Account Verification**: Make sure your LINE Official Account is verified with a blue or green badge.
    - [LINE verified official account guide](https://tw.linebiz.com/column/line-lac-id-0418/)
4. **Apply for LINE Certified Provider Status**: Contact your [LINE partner](https://tw.linebiz.com/partner/sales-partner/), or follow the process in the document below to apply ([download the application file](https://drive.google.com/file/d/1S2OoIPlmlwzyqE3h1vQldLXrcgf1sCO5/view?usp=sharing)).
  - **Under LINE rules, each company can apply for only one Certified Provider. Duplicate applications are not approved.**
5. If you already have LINE Certified Provider status, turn on **Auto-Generate LIFF URL**.
  - **Use Case**: Later, when members register and link through Store Assistant (Renewal), they can scan a QR code to add your LINE Official Account as a friend, register on your online store, and link a Store Assistant referrer.
  - **Path**: Third-Party Integration > LINE Login.
      ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置05.png)
  - **Note**: **If you do not have LINE Certified Provider status yet, do not turn on "Auto-Generate LIFF Link".**
      Without "Auto-Generate LIFF Link", members who register and link through Store Assistant first scan a QR code to add your LINE Official Account as a friend. Then guide them to the mobile verification page to provide their mobile number, register on your online store, and link a Store Assistant referrer.



### Step 3: Set up Member Registration { #operate-storepal-install-step-member-settings }

Store Assistant uses the mobile number as each member's unique identifier.

1. Go to **Website Management > Member Registration Setting**.
2. **Registration Rules**: Set the registration method to **Fast checkout with registration**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置04.png){ .screenshot }

3. **Mobile Verification**: For the mobile field, select **Required**, **Verify**, and **Mobile verification while registration**.

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置02.png){ .screenshot }

### Step 4: Set up SMS Notifications { #operate-storepal-install-step-sms-notifications }

Make sure members can receive registration verification codes.

1. Go to **Push Notifications > 簡訊通知樣板**.
2. In the Customer category, turn on **Customer Verification Code Request Notification**.

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置03-1.png){ .screenshot }


## Data Preparation { #prerequisites-data-preparation }

Store Assistant accounts are set up per store. When your account is activated, CYBERBIZ asks for the following information and creates the stores and groups in advance. To make changes later, edit them in the Store Assistant admin.

| Category | Information | Notes |
| :--- | :--- | :--- |
| **Store Information** | **Store Name** | Names must be unique<br>This name is shown as the store name when members link |
| **Group Information** | **Group Name** | Names must be unique<br>This name is shown as the group name when members link |
|  | **Store Assignment** | Each store can belong to only one group |



