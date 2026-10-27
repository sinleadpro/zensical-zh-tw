---
title: "CYBERBIZ APP Setup and Management"
description: "How to prepare the environment and pre-build your online store before you publish the CYBERBIZ APP, and how to set up the store map and push notifications in admin."
created: 2026-08-17 12:06
last_modified: 2026-08-17 12:06
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
  - POS
modules: 
  - APP 功能
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: 
  - "CYBERBIZ APP"
intents: 
  - 建置_CYBERBIZ_APP
  - 設定_APP_門市地圖
  - 設定_APP_推播通知
features: 
  - APP_門市列表
  - APP_推播通知
  - 通知樣板
  - 活動推播
prerequisites: 
  - ec/app/apply-apple-developer-account/
  - ec/app/cyberbiz-app-feature-overview/
  - ec/products/create-and-manage/create-update-products/
  - ec/marketing/
  - ec/website-appearance/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/payments-and-logistics/
  - ec/integrations/google/setup-google-quick-login/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/fb/setup-facebook-quick-login/
related:
  - ec/app/apply-apple-developer-account/
  - ec/products/create-and-manage/create-update-products/
  - ec/marketing/
  - ec/website-appearance/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/payments-and-logistics/
  - ec/integrations/google/setup-google-quick-login/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/fb/setup-facebook-quick-login/
tags: 
  - "Store Map"
  - "Push Notifications"
  - CYBERBIZ APP
acoiv: configure
apis: []
devices: []
ui_components: 
  - APP門市列表
  - 新增門市
  - 通知樣板
  - 活動推播列表
  - 新增推播
paths: 
  - APP 功能 > APP門市列表
  - APP 功能 > APP推播通知設定 > 通知樣板
  - APP 功能 > APP推播通知設定 > 活動推播列表
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app/setup-cyberbiz-app/"
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---

# CYBERBIZ APP Setup and Management
Learn how to prepare the environment and pre-build your online store before you publish the CYBERBIZ APP, and how to set up the store map and push notifications in admin.
{ .subtitle }

[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions.md#適用擴充) | CYBERBIZ APP
{ .doc-badge }

## Before You Start { #prerequisites-app-setup }

- Contact a CYBERBIZ store consultant to learn more about plans.

## App Environment Preparation { #prerequisites-app-environment }

The CYBERBIZ APP can be published on the App Store (iOS) and Google Play (Android). Set up the environment for the stores you plan to publish on.


- **Publish on the App Store**: [Apply for an Apple developer account and authorize CYBERBIZ](apply-apple-developer-account/).
- **Publish on Google Play**: CYBERBIZ provides the Google developer account, so you don't need to apply for one.


## Online Store Pre-Build { #prerequisites-app-site-prep }

The online store app fully inherits the visual settings and product data of your web store. Before you start building the app, make sure your website has the following core setup in place, so the app has full shopping features at launch:


- [x] **[Product Listings](../products/create-and-manage/create-update-products.md)**: Make sure your store has plenty of products for shoppers to choose from.
- [x] **[Marketing Tools](../marketing/index.md)**: Set up member benefits such as bonus points and coupon (codes).
- [x] **[Visual Design](../website-appearance/index.md)**: Build and review the storefront layout of your online store.
- [x] **Navigation Planning**: Complete your online store's [navigation bar settings](../website-appearance/navigation/setup-menus-navigation.md) so shoppers can move around easily.
- [x] **[Payment and Logistics Activation](../payments-and-logistics/index.md)**: Make sure your payment and shipping methods are connected and live.
- [x] **Social Login**: Set up [Google](../integrations/google/setup-google-quick-login.md), [LINE](../integrations/line/account-integration/setup-line-quick-login.md), and [Meta](../integrations/fb/setup-facebook-quick-login.md) quick login for a convenient member experience.


## Create the In-App Store Map { #operate-app-store-map }


Log in to your online store admin and go to **APP 功能 > APP門市列表** to show your physical store information in the app so customers can look it up.


1.  **Turn On the Feature**: Click the ON/OFF button.
2.  **Add Store**: Click **Add Store** in the upper-right corner.
3.  **Select a source**: Select **App Retail Store** or **POS Shop**.
    *   If you also use the CYBERBIZ POS system, select **POS Shop** to bring in store information with one click.
4.  **Enter Store Information:**
    *   **Store Phone Number**: Enter the store's contact phone number.
    *   **Store Address**: Enter the full address. This affects how accurately the store is located on the map.
    *   **Note**: Enter business hours or directions.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP門市列表-單筆新增門市01.png)

## Import Stores in Bulk { #operate-app-store-import }

1.  **Download the Excel Template**: Click **Download Excel Example**.
2.  **Enter Store Information**: Open the template file and add your store information.
3.  **Import the File**: Click **Import Custom Stores** and upload the file.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP門市列表-批次匯入門市01.png)


## Default App Notification Switches { #operate-app-notification-defaults }

Go to **APP 功能 > APP推播通知設定 > 通知樣板** to choose whether system-triggered notifications (such as order confirmation and shipping notifications) are turned on.


1.  **Toggle the Switch**: Click the ON/OFF button on the right. When the button shows a blue ON, the system automatically sends a push notification to customers when that event occurs.
    *   **Order-Related**: For example, **Order Confirmation Notification** and **Payment Success Notification**.
    *   **Shipping-Related**: For example, **Shipment Notification** and **Arrival at Store Notification**.
    *   **Customer-Related**: For example, **Member Birthday Bonus Notification** and **coupon Expiry Reminder**.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP推播通知設定-系統通知樣板01.png)



## Send App Push Messages { #operate-app-push }

Go to **APP 功能 > APP推播通知設定 > 活動推播列表** to create push campaigns, choose the target member groups and send time, and proactively send marketing messages or announcements to app users.

1.  **Add a Campaign**: Click **New Push**.
2.  **Basic Push Settings**
    *   **Push Title**: Enter an engaging title.
    *   **Push Content**: Enter the full message.
    *   **Push Image**: Click or drag to upload an image.
    *   **Landing Page**: Choose where users go after they tap the notification.
3.  **Select the Target Audience:**
    *   **All Members**: Sends the message to all registered members. Suitable for site-wide campaigns or major system announcements.
    *   **Member Group**: Sends the push to member segments you set up in advance, for targeted marketing.
    *   **Import Excel File**: For specific or one-off lists, upload an Excel file to specify which members receive the message.
4.  **Set the Send Time:**
    *   **Scheduled**: Specify a date and time.
    *   **Immediate**: Sends the push as soon as it's created.
5.  **Check the Preview**: Preview the push on the right.
    *   **System Push**: The pop-up notification on the phone's lock screen.
    *   **Notification List**: The news feed in the app's bell notifications.
    *   **Push Landing**: The landing page that opens when users tap the notification.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP推播通知設定-新增推播活動01.png)

From creating a campaign to managing it after it's sent, the system offers two core tools to streamline your workflow:

*   :lucide-send: **Style Preview**: Use **Send Test Push** to check how the message looks before the official push, so the content comes across exactly as intended.
*   :lucide-copy: **Campaign Copy**: Use **Copy** to duplicate an existing campaign in one click. Adjust the details and republish it quickly to save time.


![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP推播通知設定-複製與測試推播活動01.png)