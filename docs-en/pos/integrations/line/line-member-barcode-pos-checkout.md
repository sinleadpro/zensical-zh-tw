---
title: "Set up and Use LINE Member Barcode Display (POS Checkout Integration)"
description: "Enable and set up the LINE Official Account member barcode so store staff can scan it on the POS to quickly identify members and apply bonus and coupon redemptions."
created:
last_modified: 2026-07-03 11:43
lang: en-US
permalink: "https://help.cyberbiz.io/pos/integrations/line/line-member-barcode-pos-checkout/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 第三方整合
  - 會員
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 顯示 LINE 會員條碼
  - 整合 LINE 與 POS
  - 優化線下結帳體驗
  - 會員紅利折抵
  - 門市優惠券折抵
features:
  - LINE 會員條碼顯示
  - POS 掃描會員登入
  - 紅利點數扣抵
  - 優惠券扣抵
  - LINE 圖文選單整合
prerequisites:
  - CYBERBIZ POS 系統
  - LINE Messaging API 串接
  - LINE 圖文選單設定
  - LINE OA 會員綁定（建議）
related:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
  - ec/integrations/line/marketing/setup-line-rich-menu/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
tags:
  - "bonus points"
  - "coupon Redemption"
  - "Store Checkout"
  - "Member Barcode"
  - LINE
  - OMO
  - POS
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=748
comments: false
search:
  exclude: false
icon: lucide/barcode
hide:
---

[:lucide-layers:{ title="Applicable Products" }](../../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

## LINE Member Barcode Display Overview

**LINE Member Barcode Display** is designed to improve the in-store checkout experience. Customers only need to show the member barcode from their LINE Official Account at the store, and staff can scan it with the POS terminal to verify the member and then apply bonus points or coupon redemption.

## Prerequisites and Restrictions

- **Applicable Merchants**: This feature is available only to merchants who use the **CYBERBIZ POS System**.
- **Prerequisite Setup**:
    - [x] Merchants must first complete the [LINE Messaging API Integration](../../../ec/integrations/line/account-integration/connect-line-messaging-api.md){ title="LINE Messaging API Integration" }, and set up the [LINE Rich Menu](../../../ec/integrations/line/marketing/setup-line-rich-menu.md){ title="Set Up the LINE Rich Menu" }.
    - [x] We recommend guiding customers to first complete [Link LINE Official Account to Website Member](../../../ec/integrations/line/account-integration/bind-line-oa-store-members.md){ title="Link LINE Official Account and Website Member" } so that member data is loaded directly after scanning.

## Operation Steps

### Back-End Setup Steps <small>Configure the Rich Menu</small>

To let consumers display their member barcode, the merchant must create a matching link in the LINE Official Account rich menu:

1. Go to the back end of [LINE Official Account Manager :lucide-external-link:](https://manager.line.biz/), then select **Chats > Rich Menu**.
2. Create or edit a menu item, and set one of its areas to **My Member Card**.
3. **Set Up the Action Link**: In the link field, enter the unique code:
    - Link URL: `https://您的網址/account/id_barcode`.
4. After saving the menu, customers tap this area to display their personal member barcode on their phone.

!!! info "For detailed LINE rich menu setup instructions, see [How to Set Up the LINE Rich Menu](../../../ec/integrations/line/marketing/setup-line-rich-menu.md){ title="Set Up the LINE Rich Menu" }."

---

### Front-End Operation Flow

#### Customer-Side Operation

- When consumers check out in store, they open the brand's LINE Official Account.
- Tap **My Member Card** in the rich menu, and the phone screen displays the **Member Barcode** and number.

![LINE member card screen](../../../assets/images/pos-line oa-會員卡.en.png){ title="LINE member card screen" }

---

#### Staff-Side Operation <small>POS Terminal</small>

1. Staff log in to the POS front end and click the **Checkout** key.
2. On the member login screen, scan the consumer's phone barcode with the barcode scanner, or manually enter the barcode number to log in.
3. Once the member information is confirmed, start scanning products.

![POS checkout screen](../../../assets/images/pos-結帳.en.png){ title="POS checkout screen" }

## Bonus and Coupon Redemption Methods

After all checkout products are scanned, redeem based on how the member logged in:

- **Scenario 1 (Phone or Email Login)**: If staff first search for the member by phone number, then scan the consumer's LINE member barcode again when redeeming. Once the **green checkmark** appears, apply the redemption.
- **Scenario 2 (Direct Login by Barcode Scanner)**: If the member logs in by scanning the barcode from the start, no second scan is needed. Click bonus points or coupon on the checkout screen to apply the deduction.

![bonus redemption screen](../../../assets/images/pos-紅利折抵.en.png){ title="bonus redemption screen" }

## Frequently Asked Questions

??? quote "Why can't the in-store barcode scanner read the member barcode?"
	If a scan fails, check the following troubleshooting steps in order:

	- **Refresh the Barcode Status**: Barcodes have a limited validity period. If a scan fails or the barcode shows as expired, guide the consumer to tap My Member Card in the rich menu again. The system automatically generates a new valid barcode number.
	- **Adjust Screen Brightness**: A dim or glare-prone phone screen can affect how the barcode scanner reads the code. Remind the consumer to set the phone screen brightness to maximum and try again.
	- **Check the Hardware Environment**: Confirm that the scanner lens is clean and maintain an appropriate scanning distance (about 5-10 cm).
