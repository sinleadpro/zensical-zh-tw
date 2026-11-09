---
title: "Set up and Manage LINE Tag"
description: "Set up your LINE Tag ID and track conversions from LINE OA message push notifications or LINE LAP ad campaigns."
created: 2026-03-10 15:13
last_modified: 2026-07-14 17:10
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 第三方整合
  - 行銷活動
sites:
  - TW
audiences:
  - developer
difficulty: advanced
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 如何設定 LINE_Tag
  - 如何取得 LINE_Tag_ID
  - 如何追蹤 LINE 廣告成效
  - 如何建立 LINE 網站流量受眾
features:
  - LINE Tag
  - LINE OA 整合
  - LINE LAP 廣告追蹤
  - 網站流量受眾
prerequisites:
  - 建立 LINE 官方帳號
related:
  - ec/website-management/add-admin-set-permissions/
  - ec/integrations/line/marketing/setup-line-oa-audience/
tags:
  - "LINE Tag"
  - "Ad Tracking"
  - "Conversion Tracking"
  - "LINE OA"
  - "LINE LAP"
  - Remarketing
  - "Audience Settings"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > LINE Tag 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4769
  - https://www.cyberbiz.io/support/?p=28602
permalink: "https://help.cyberbiz.io/ec/integrations/line/marketing/setup-manage-line-tag/"
search:
  exclude: false
icon: lucide/code
hide: []
comments: false
---

![LINE Tag Setup](../../../../assets/images/ec-第三方整合-linetag.en.png){ title="LINE Tag Setup" .hero-page }

## What Is LINE Tag

LINE Tag is a website tracking code provided by LINE. It works like the Facebook Pixel and can track:

- LINE OA message push conversions
- LINE LAP ad performance
- Website traffic audience creation

The following sections cover detailed setup steps and usage notes for LINE Tag:

## Notes

- [x] Create a LINE OA official account before you begin setup.
- [x] If your browser has **AdBlock (ad blocker)** installed, turn it off during setup or checks to avoid interfering with data tracking.
- [x] Operators need the **Settings** permission under **Website Management > User Account Settings** to complete integration setup.

    [Modify Admin Permissions](../../../website-management/add-admin-set-permissions/#管理者權限設定與修改){ data-preview }


## Get and Set up LINE Tag ID
Get the code from LINE OA Manager or LINE Ad Manager, then enter it in the CYBERBIZ backend.

### For Message Push Conversion Tracking <small>LINE OA Manager</small>

1.  **Access the backend**: Log in to [LINE OA Manager :lucide-external-link:](https://manager.line.biz/) and select the official account you want to set up.
2.  **Find the code**: In the left menu, click **Data Management > Tracking (LINE Tag)**, then copy the **Tag ID** on the page.

    ![Copy Tag ID](../../../../assets/images/ec-第三方整合-linetag-tagid複製.en.png){ title="Copy Tag ID" }

    !!! tip "Use ++ctrl+f++ to quickly locate the tagID."

3.  **Enter in the system**: Go to the CYBERBIZ backend **Third-Party Integration > LINE Tag Settings** and click **Add Tag ID**.
4.  **Set the type**: Select **`account`** as the type, then paste the Tag ID you just copied.

    ![Add Account Tag ID](../../../../assets/images/ec-第三方整合-linetag-新增tagid-account.en.png){ title="Add Account Tag ID" }

---

### For Ad Campaign Conversion Tracking <small>LINE Ad Manager</small>

1.  **Access the backend**: Log in to [LINE Ad Manager :lucide-external-link:](https://admanager.line.biz/) and select the ad account you want to set up.
2.  **Find the code**: In the left menu, select **Tracking (LINE Tag)**, then copy its **Tag ID**.


    ![Ad Manager Tag ID](../../../../assets/images/ec-第三方整合-lineadmanager-tagid畫面.en.gif){ title="Ad Manager Tag ID" }

    !!! tip "Use ++ctrl+f++ to quickly locate the tagID."

3.  **Enter in the system**: Go to the CYBERBIZ backend **Third-Party Integration > LINE Tag Settings** and click **Add Tag ID**.
4.  **Set the type**: Select **`lap`** as the type, then paste the Tag ID.

    ![Add LAP Tag ID](../../../../assets/images/ec-第三方整合-linetag-新增tagid-lap.en.png){ title="Add LAP Tag ID" }

---

## CYBERBIZ Supported Tracking Events

The system automatically embeds tracking code for the following actions, so you don't need to write any extra code:

| Event Name | Trigger Description |
| :--- | :--- |
| **CompleteRegistration** | Visitor completes registration |
| **Search** | Search for products |
| **PageView** | View any page on the storefront |
| **ViewContent** | View a product detail page |
| **AddToCart** | Add a product to the cart |
| **InitiateCheckout** | Enter the checkout page |
| **Purchase** | Order completed (purchase) |


---

## How to Check Whether Setup Is Successful

*   **Method 1 (manual check)**: Perform a specific action on the storefront, such as registering or adding a product to the cart. Then refresh the LINE Tag management page and check whether the event name appears in the status list.

    ![Tag Tracking Status](../../../../assets/images/ec-第三方整合-lineoa-linetag追蹤狀態.en.png){ title="Tag Tracking Status" }

*   **Method 2 (tool check)**: Download the Chrome extension [**LINE Tag Helper** :lucide-external-link:](https://chromewebstore.google.com/detail/line-tag-helper/jgnholagndjghcjedffhinifilbjmklg?hl=zh-TW) for real-time detection.

---

## Advanced LINE Tag Usage

### Create Audiences

The visitor data you collect can be packaged into a **Website Traffic Audience** in the LINE backend. Use it for precise ad targeting or remarketing.

#### LINE OA Manager

1.  **Access the backend**: Log in to [LINE OA Manager :lucide-external-link:](https://manager.line.biz/) and select the official account you want to set up.
2.  **Go to the page**: Click **Data Management > Audiences > Create Audience**.
3.  **Audience settings**:

    - **Audience type**: Select **Website Traffic**.
    - **Target settings**: Select the LINE Tag account you want to set up, and configure the related target settings.

![Create OA Audience](../../../../assets/images/ec-第三方整合-linetag-建立受眾-lineoa.en.png){ title="Create OA Audience" }

---

#### LINE Ad Manager

1.  **Access the backend**: Log in to [LINE Ad Manager :lucide-external-link:](https://admanager.line.biz/) and select the ad account you want to set up.
2.  **Go to the page**: Click the menu button :lucide-menu: in the upper-left corner, then select **Audiences > Create Audience > Website Traffic Audience**.
3.  **Audience settings**: Click **Events** and select the events you want to set up.

![Create Audience in Ad Manager](../../../../assets/images/ec-第三方整合-linetag-建立受眾-lineadmanager.en.png){ title="Create Audience in Ad Manager" }

### Conversion Analysis

In the analytics feature of LINE OA Manager, use Broadcast Message - Custom Conversion to analyze the actual conversion performance of specific messages.

1.  **Go to the page**: Click **Broadcast Messages > Custom Conversions > Create**.
2.  **Configure the conversion**:
    - **LINE Tag**: Select the LINE Tag you set up.
    - **Matching method**: Select **Conversion Event**.

![Conversion Analysis](../../../../assets/images/ec-第三方整合-linetag-轉換分析.en.png){ title="Conversion Analysis" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-split:{ .lg }   
  [__Audience Integration__](setup-line-oa-audience.md){ title="Set Up LINE OA Audience Integration" }  
  Filter storefront members and sync them to LINE to create audiences. Use these audiences for precise push messages or ad campaigns.

</div>

## Frequently Asked Questions

??? quote "Why does my LINE Tag status keep showing 'Waiting for data' or 'No activity'?"
    There are usually three possible causes:

    1. **No traffic yet**: Visit a few product pages on the storefront yourself and complete an **Add to Cart** action.
    2. **Ad blocker interference**: Make sure ad blockers such as AdBlock are turned off during the check.
    3. **Tag ID entered in the wrong place**: Make sure the IDs for `account` (OA) and `lap` (Ad) are not swapped.

??? quote "Does LINE Tag data differ from Google Analytics (GA4) data?"
    Yes, that is normal. The two use different **attribution models**. For example, LINE may count conversions within 30 days after a click, while GA4 uses its own definition. Also, if a shopper opens a link in the LINE in-app browser and then switches to Safari or Chrome to complete a purchase, tracking may be lost.

??? quote "Do I need to manually embed the `ViewContent` code on each product page?"
    No. CYBERBIZ is already fully integrated. As long as you enter the correct Tag ID in the backend, the system automatically sends the `ViewContent`, `AddToCart`, and `Purchase` events on the corresponding pages. The events include the amount and product information.

??? quote "If I have two LINE official accounts, can I enter two Account IDs?"
    Currently, the system supports one `account` type and one `lap` type. For special multi-account needs, we recommend adding extra tracking through Google Tag Manager (GTM).


