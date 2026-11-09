---
title: "Set up LINE Rich Menu"
description: "Create and configure a LINE rich menu so customers can quickly browse products, the member center, and shopping pages from your official account."
created:
last_modified: 2026-07-02 10:17
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 第三方整合
sites: []
audiences:
  - merchant
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定 LINE 圖文選單
  - 配置 LINE 官方帳號選單
  - 透過圖文選單引導顧客行動
  - 經由 LINE 推廣產品
  - 整合 LINE 官方帳號與電子商務
features:
  - 圖文選單配置
  - 客製化選單版面
  - 外部連結整合
  - 關鍵字搜尋整合
  - 會員帳號綁定
  - 會員條碼顯示 (OMO)
  - 自動化訊息通知
prerequisites:
  - LINE 官方帳號 API 支援
  - LINE Messaging API 設定
  - 圖文選單連結禁用短網址
related:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
  - pos/integrations/line/line-member-barcode-pos-checkout/
  - ec/integrations/line/account-integration/setup-liff-auto-login-member-binding/
tags:
  - LINE
  - "Rich Menu"
  - Integration
  - Marketing
  - "Shopping Links"
  - Members
  - OMO
  - "LINE OA"
acoiv:
apis:
  - LINE Messaging API
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5858
  - https://www.cyberbiz.io/support/?p=855
permalink: "https://help.cyberbiz.io/ec/integrations/line/marketing/setup-line-rich-menu/"
comments: false
search:
  exclude: false
icon: lucide/layout-panel-top
hide: []
---

![LINE Rich Menu Setup](../../../../assets/images/ec-第三方整合-line 圖文選單.en.png){ title="LINE Rich Menu Setup" .hero-page }

## What Is a LINE Rich Menu?

 **LINE Rich Menu** is an important tool for promoting products and helping customers quickly find information. You can set up features in the menu, such as keyword product search, member profile viewing, or shopping links.

## Prerequisites

Before you start, make sure you complete the following:

- [x] **Confirm your plan**: Check that your current LINE OA plan **supports API integration**.
- [x] **API integration**: First, complete  [**LINE Messaging API** integration](../account-integration/connect-line-messaging-api.md){ title="Connect LINE Messaging API" }  setup.
- [x] **Link rules**: Rich menu links **must not use short URLs**, which can cause the code to stop working.

## Steps to Create a Rich Menu

1. **Go to the LINE admin console**: Log in to [LINE Official Account Manager :lucide-external-link:](https://manager.line.biz/), then select your official account.

2. **Create a menu item**: From the left menu, select **Chats > Rich Menu**, then click **Create Rich Menu**.

3. **Configure basic information**:

	- **Title**: Used for internal identification. Customers do not see it.

	- **Active period**: Set when the menu is displayed.

	- **Menu bar text**: The button text shown at the bottom of the chat (for example, "Tap for more").

	- **Default display**: Choose whether the menu is expanded or hidden by default.

4. **Configure layout and image**:

	- Choose a suitable **layout** for dividing the menu into areas.

	- Upload an image: Supports **JPG, JPEG, and PNG** files up to **1 MB**.

	- Recommended image sizes: Six sizes are available, such as 2500x1786, 1200x810, and 800x540 (in px).

!!! info "For detailed setup steps, see [LINE Official Documentation :lucide-external-link:](https://tw.linebiz.com/manual/line-official-account/oa-manager-richmenu/)."

![Rich menu setup steps](../../../../assets/images/ec-第三方整合-line-圖文選單設定.en.png){ title="Rich menu creation steps" }

## Configure Rich Menu Actions

When you configure actions for each area, select **Link** as the type.

- **Link URL:** Enter the full URL of the target page you want to direct customers to (must include `https://`).
- **Action label:** Provides accessibility support. Where supported, this text is read aloud. On unsupported devices, only the text is displayed.

![Rich menu action settings](../../../../assets/images/ec-第三方整合-line-圖文選單-連結.en.png){ title="Rich menu action settings" }

Select the links that match your needs:

### Common Feature Path Reference

Append the **path alias** below to your store domain to make it work (for example: `https://www.yourshop.com/account`).

|**Feature Name**|**Path Alias**|**Use Case and Notes**|
|---|---|---|
|**Store Homepage**|`/`|Leads to the brand homepage and drives brand traffic|
|**Member Profile Page**|`account`|Customers view their personal information, order history, and bonus points|
|**Blog Overview**|`blogs`|Leads to the list of content marketing articles|
|**All Products Page**|`collections/all`|Displays all published products in the store|
|**E-Tickets**|`account/eticket_orders`|Lets customers view purchased virtual tickets or redemption codes|
|**Member Card (Barcode)**|`account/id_barcode`|**OMO Application**: Lets offline stores scan and redeem codes (POS only)|
|**Specific Search Results**|`search?q=keyword`|Leads to search results for a specific keyword (replace "keyword" with the product keyword you want to promote)|

---

### Link Construction Rules and Examples

Choose the link format that matches your customers' browsing goals and authentication needs:

---

#### General Browsing Mode <small>No Forced Login</small>

If you want customers to browse pages directly without binding a LINE account, use the standard format.

- **Format**:`https://[your-domain]/[url-code]`

- **Example**:`https://testtest.co/collections/all`

---

#### Direct Link to a Specific Page

To direct customers to a specific product page, group page, or custom page, copy the full URL of that page directly.

- **Example**:`https://testtest.co/products/summer-sale`

---

#### OMO Physical Store Application

If you add a "Member Card" button to the menu so customers can show it at checkout in store, use the dedicated path.

- **Link URL**:`https://your-domain/account/id_barcode`

- **Prerequisites**: Confirm that your plan has **CYBERBIZ POS** enabled and that you have completed [LINE Member Binding Setup](../account-integration/bind-line-oa-store-members.md){ title="Bind LINE Official Account and Store Member" }  .

![Rich menu member card settings](../../../../assets/images/ec-第三方整合-line-圖文選單-會員卡.en.png){ title="Rich menu member card settings" }

!!! note "Related reading: Store-side operations"
	For POS barcode login, bonus redemption, and troubleshooting, see [How to Set Up and Use the LINE Member Barcode (POS Integration)](../../../../pos/integrations/line/line-member-barcode-pos-checkout.md){ title="Set Up and Use the LINE Member Barcode (Checkout via POS)" }  .

---

### Member Account Binding Mechanism <small>Recommended</small>

To ensure the system can send automated **order notifications** and **shipping status updates**, we recommend setting member-related areas in the menu (such as Member Center) to "Auto-Bind Link."

#### Setup Information

- **Binding link**:`https://[your-domain]/customer/auth/line?line_action=line_login`


#### How It Works

- **Customers not yet bound**: Tapping opens the LINE authorization screen. After authorization, the store member binding is completed automatically, and the customer is then directed to the logged-in status page.

- **Customers already bound**: Tapping goes directly to the target page in a logged-in state, for a smoother shopping experience.


!!! warning "Important Reminder"

	- Avoid repeated redirects: URLs with the `line_action=line_login` parameter keep triggering the verification flow. We recommend using this URL only for the "First-Time Binding" or "Log In / Sign Up" buttons. For other general shopping buttons, use a regular link.
	- LINE OA message billing: Before you enable automated notifications, be sure to assess operating costs. All messages sent from a LINE Official Account (including manual broadcasts, automated order notifications, and shipping updates) count toward the paid quota. For billing rates, see the official [LINE Official Account Add-On Message Pricing](https://tw.linebiz.com/service/account-solutions/line-official-account/).

!!! note "For more member binding methods, see [LINE Member Binding](../account-integration/bind-line-oa-store-members.md#商家後台設定方法){ title="Bind LINE Official Account and Store Member" }."

![Rich menu member binding settings](../../../../assets/images/ec-第三方整合-line-圖文選單-會員綁定.en.png){ title="Rich menu member binding settings" }



## How to Confirm the Rich Menu Is Displayed Successfully

After setup, open the LINE app on your phone and check the following:

- The rich menu appears at the bottom of the official account chat
- Tapping a menu item correctly leads to the specified page
- Menus with a set active period appear during the specified times


## Next Steps

<div class="grid cards" markdown>

- :lucide-link:{ .lg }   
  [__LIFF URL Optimization__](../account-integration/setup-liff-auto-login-member-binding.md){ title="Set Up LIFF Auto-Login and Member Binding" }       
  Switch to the **LIFF URL** generated in the EC admin. After tapping, customers can have their account information applied automatically within LINE, enabling "add friend, sign up, and bind in one tap" for a smoother experience.

- :lucide-search:{ .lg }     
  [__Keyword Product Search__](../account-integration/connect-line-messaging-api.md#line-關鍵字搜尋商品){ title="Connect LINE Messaging API" }    
  After you connect the webhook, customers can type a keyword in the LINE chat, and the system automatically replies with the matching product messages.

</div>

## FAQ

??? quote "Why does my rich menu show "Resolution Mismatch" after I upload an image?"

	LINE has strict image size requirements for rich menus. Make sure your image meets the following conditions:

	- **File format**: JPG, JPEG, PNG.
	- **File size**: Up to 1 MB.
	- **Pixel dimensions**: Must exactly match one of the six sizes specified by LINE (such as large: $2500 \times 1786$ px or $1200 \times 810$ px; small: $2500 \times 843$ px). Even a 1-pixel difference will cause the upload to fail.

??? quote "I set up "Auto-Bind Link," but users see an error page after tapping it"

	This is usually related to the Callback URL setting in **LINE Login**. Check the following:

	1. [LINE Developers Console](https://developers.line.biz/) — confirm the **LINE Login** channel status is "Published."

	2. Confirm that the **Callback URL** correctly matches your store URL.

	3. Confirm that the link includes the complete `https://`.

??? quote "Why does a message saying "Open in an external browser" appear when I tap a menu link?"

	This is usually because the link uses a **short URL** (such as bit.ly) or a non-secure link (http).

	- **Solution**: Be sure to use the **original long URL** generated by your store.

	- **Optimization tip**: To open pages directly within the LINE app without leaving it, switch the link to a **LIFF URL** for a smoother in-app web experience.

??? quote "I updated the rich menu, but the LINE app on my phone still shows the old one"

	This is because the phone has cached data. Try the following steps:

	1. Completely close the LINE app and reopen it.

	2. Unfollow the official account, then add it as a friend again.

	3. If you set an "active period," confirm that the current time falls within the set range.
