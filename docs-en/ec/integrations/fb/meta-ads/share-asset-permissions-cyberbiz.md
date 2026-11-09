---
title: "Manually Share Asset Permissions with CYBERBIZ"
description: "When Meta ad creation fails, manually share asset permissions (Facebook Page, pixel, and catalog) with the CYBERBIZ Business Manager to resolve the issue."
created: 2026-04-21 16:01
last_modified: 2026-06-26 10:05
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
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 解決廣告創建失敗
  - 手動分享資產權限
features:
  - Meta Ads
  - 資產權限
prerequisites:
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
related:
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/meta-ads/setup-meta-ad-campaign/
tags:
  - "Meta Ads"
  - "Asset Permissions"
  - Troubleshooting
  - "Facebook Ads"
acoiv: integration
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > Facebook 整合_廣告_註冊登入 > 廣告活動設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10681
  - https://www.cyberbiz.io/support/?p=44556
permalink: "https://help.cyberbiz.io/ec/integrations/fb/meta-ads/share-asset-permissions-cyberbiz/"
comments: false
search:
  exclude: false
icon: lucide/share-2
hide: []
---



![Manual asset sharing permissions](../../../../assets/images/ec-第三方整合-fb-mbs-手動分享權限.en.png){ .hero-page }

## Share Assets with CYBERBIZ

If you see **Ad Creation Failed** when you run Meta ads in the CYBERBIZ back office, you can fix the issue by manually sharing asset permissions with CYBERBIZ and then notifying customer service.

## Prerequisites

Before you manually share assets, confirm the following:

- [x] **Complete [Meta Ad Account Setup and Top-Up](create-meta-ad-account-top-up.md){ title="Create a Meta ad account and top up" }**: First, confirm that you have completed all steps in "Create a Meta ad account and top up."
- [x] **Complete [Pixel Setup](create-meta-ad-account-top-up.md#像素設定-pixel){ title="Create a Meta ad account and top up" }**: Make sure you have completed the Pixel Setup step during ad account creation.
- [x] **Share the correct assets**: First, complete [FBE Account Authorization and Asset Linking](../mbe/setup-fbe-authorization.md){ title="Set up FBE account authorization and asset linking" }, then confirm the specific assets you configured in "New Business Extensions" in the back office.

## Steps to Manually Share Asset Permissions

!!! warning "Verify Assets"
    Before assigning permissions, make sure the assets selected in Business Manager Settings match the details shown in [Business Extension Asset Linking](../mbe/setup-fbe-authorization.md){ title="Set up FBE account authorization and asset linking" }.

### Share Facebook Page Permissions

1. Log in to [Business Manager Settings](https://business.facebook.com/latest/settings), then in the left menu, click "Accounts" > **Fan Page**.
2. Click **Assign Partner** > select **Business Manager ID**, then enter **CYBERBIZ Business Manager ID: `481801283092517`**.
3. Under Partial Management Permissions, select **Ads** and **Insights**, then click "Continue" to finish.

![MBS-Facebook Page Sharing Permissions](../../../../assets/images/ec-第三方整合-fb-mbs-粉絲專頁分享權限.en.gif)

---

### Share Pixel Permissions

1. Log in to [Business Manager Settings](https://business.facebook.com/latest/settings), then in the left menu, click "Data Sources" > **Datasets and Pixels**.
2. Select the pixel you want to share, click **Assign Partner** > Select **Business Manager ID**, and enter **CYBERBIZ Business Manager ID: `481801283092517`**.
3. Under Partial Management Permissions, select **View pixel**, click **Continue** > select **(as an agency for my business)**.

![MBS-Pixel Sharing Permissions](../../../../assets/images/ec-第三方整合-fb-mbs-像素分享權限.en.png)

??? failure "Error "Partner Business Manager Relationship Already Established" appears"

    1. In the left menu, click "Users" > **Partners**.
    2. Find the **CYBERBIZ1** BM account.
    3. Click **Share Assets**.
    4. Under "Datasets" or "Pixels", find the matching pixel, select the **Use Event Datasets** permission, and click "Assign Assets".

    ![MBS-Partner-Share Assets](../../../../assets/images/ec-第三方整合-fb-mbs-合作夥伴-分享資產.en.png)

---

### Share Catalog Permissions

1. Log in to [Business Manager Settings](https://business.facebook.com/latest/settings), then in the left menu, click "Data Sources" > **Catalogs**.
2. Click **Assign Partner** > select **Business Manager ID**, then enter **CYBERBIZ Business Manager ID: `481801283092517`**.
3. Under the available partial management permissions, select **Create Ads**, then click "Continue".

![MBS-Catalog Sharing Permissions](../../../../assets/images/ec-第三方整合-fb-mbs-目錄-分享權限.en.gif)

## Complete Follow-Up Steps

1.  **Notify customer service**: After manual sharing is complete, make sure to **notify CYBERBIZ customer service**.
2.  **Wait for a response**: After CYBERBIZ completes the system-side follow-up and sends an official reply, you can try [Set Up a Meta Ad Campaign](setup-meta-ad-campaign.md){ title="Set up a Meta ad campaign" } again.

## FAQ

??? quote "What should I do if the error "Partner Business Manager Relationship Already Established" appears when sharing permissions?"

    Instead, in the left menu, click "Users" > "Partners", find the "Cyberbiz1" BM account, click "Share Assets", find the matching pixel in "Datasets" or "Pixels", select the "Use Event Datasets" permission, and click "Assign Assets".

??? quote "Do I still need to notify customer service after permission sharing is complete?"

    Yes. After manual sharing is complete, be sure to notify CYBERBIZ customer service. Once CYBERBIZ finishes the back-end follow-up and sends an official reply, you can try setting up the ad campaign again.

