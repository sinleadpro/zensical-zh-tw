---
title: "Sync Product Videos to Meta Catalog"
description: "Sync CYBERBIZ product videos to the Meta catalog so that product videos and images rotate in catalog ads, making them more eye-catching."
created: 2026-04-21 14:27
last_modified: 2026-06-26 10:05
lang: en-US
type: guide
author: Jase
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
  - 同步商品影片
  - Meta 目錄同步
features:
  - 商品影片
  - Meta 目錄
  - CPV 廣告
prerequisites:
  - ec/products/create-and-manage/setup-product-videos/
  - ec/integrations/fb/mbe/setup-fbe-authorization/
related:
  - ec/integrations/fb/meta-ads/setup-meta-ad-campaign/
  - ec/products/create-and-manage/setup-product-videos/
  - ec/integrations/fb/mbe/setup-fbe-authorization/
tags:
  - "Meta Catalog"
  - "Product Videos"
  - "CPV Ads"
  - "Catalog Ads"
acoiv: integration
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 臉書 Facebook 設定
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7886
  - https://www.cyberbiz.io/support/?p=2175
permalink: "https://help.cyberbiz.io/ec/integrations/fb/meta-ads/sync-product-videos-meta-catalog/"
comments: ""
search:
  exclude: false
icon: lucide/play
hide:
---

![MBS-Data Sources-Catalog](../../../../assets/images/ec-第三方整合-mbs-資料來源-目錄.en.png){ .hero-page }

## Sync Product Videos to Meta Catalog Overview { #overview-meta-videos }

This feature lets merchants automatically sync product data on the CYBERBIZ platform (including information, inventory, prices, and, most importantly, **product videos**) to the Meta product catalog. After setup, when you create a Meta ad and select "[**Catalog Ads**](setup-meta-ad-campaign.md#intro-meta-campaign){ title="Set Up Meta Ad Campaign" data-preview }", product videos and product images rotate when the ad runs.

## Prerequisites and Feature Limitations { #prerequisites-meta-videos }

Before syncing, make sure you meet the following requirements and specifications:

- [x] **Product video upload:** Merchants must complete [Product Video Upload](../../../products/create-and-manage/setup-product-videos.md){ title="Set Up Product Videos" } in the CYBERBIZ admin.
- [x] **Extension integration:** Merchants must have integrated the "[Facebook New Business Extension](../mbe/setup-fbe-authorization.md){ title="Set Up FBE Account Authorization and Asset Linking" }" feature.
- [x] **Layout restriction:** The product video feature currently supports only the **drag-and-drop layout**. Stores using other layouts cannot upload or sync videos.

## Sync Setup Steps { #operate-meta-videos }

1.  **Enter the feature**: Log in to the CYBERBIZ admin dashboard, go to **Third-Party Integration > Facebook Settings (Ads/Registration Login)**, and click **Edit Asset** to open the setup window.

    ![FBE-Edit Assets](../../../../assets/images/ec-第三方整合-fb-基本設定-fbe-編輯資產.en.png)

2.  **Link assets:** This step is the same as the "Link Business Assets" process in [FBE Account Setup Tutorial](../mbe/setup-fbe-authorization.md#operate-fbe-authorization-operate-step){ title="Set Up FBE Account Authorization and Asset Linking" } (including logging in to Facebook, agreeing to authorization, and selecting assets).

3.  **Select a catalog asset:** Select **Catalog** as the asset type to sync, choose the product catalog from the list, and click **Confirm**.

    ![FBE-Link Catalog](../../../../assets/images/ec-第三方整合-fb-基本設定-fbe-連結目錄.en.png)

    !!! tip "We recommend clicking **Create New Asset** to create a brand-new catalog. If you use an existing catalog, conflicts with old product data can prevent video data from updating properly."

4.  **Finish the process:** Complete the remaining settings in the dialog and click **Finish**. The system then automatically returns you to the CYBERBIZ admin page.

## Verify the Sync Status in Meta { #specs-meta-videos }

1.  Go to the [Meta Business Manager :lucide-external-link:](https://business.facebook.com/latest/settings) admin, go to **Data Sources** > **Catalogs**, and select the catalog you just linked.
2.  Click **Open in Business Manager**.

    ![MBS-Data Sources-Catalog](../../../../assets/images/ec-第三方整合-mbs-資料來源-目錄-在商務管理工具中開啟.en.png)

3.  In **Catalogs** > **Data Sources**, you can check whether the catalog has automatically synced and updated the product data on your website.

    ![MBM-Catalogs-Data Sources](../../../../assets/images/ec-第三方整合-mbm-目錄-資料來源.en.png)

!!! warning "Notes"
    - If adding fails because multiple data sources exist, delete the old data source first, then update again.
    - Before **running ads**, Business Manager may not show video data. You can try creating an ad and pausing it during review. Meta then loads the video data.

## Next Steps { #next-steps-meta-videos }

<div class="grid cards" markdown>

- :lucide-rocket:{ .lg }   
  [__Launch a Meta Ad Campaign__](setup-meta-ad-campaign.md){ title="Set Up Meta Ad Campaign" }       
  After syncing, you can set up CPV ads (Catalog Product Video) to showcase product highlights with product videos.

</div>

## FAQ { #faq-meta-videos }

??? quote "How do I confirm that product videos have synced to the Meta catalog?"

    Follow these steps to confirm the sync status:

    1. Go to the [Meta Business Manager :lucide-external-link:](https://business.facebook.com/latest/settings) admin, then go to **Data Sources** > **Catalogs**
    2. Select the catalog you linked, then click **Open in Business Manager**
    3. Check **Catalogs** > **Data Sources** to see whether the product data on your website has been automatically synced and updated

??? quote "What are the format and specification requirements for product videos?"

    Videos must meet the following requirements:

    - Resolution: Must not exceed **1280 x 1280** (the recommended aspect ratio is **9:16**)
    - Format: Only **mp4** is supported
    - Length: Must not exceed **60 seconds**
    - File size: Must not exceed **30 MB**
    - Audio: The system **does not support audio output**

??? quote "Why can't I see video data in Meta Business Manager?"

    Possible causes include:

    - Before **running ads**, Business Manager may not show video data
    - If adding fails because multiple data sources exist, delete the old data source first, then update again
    - We recommend creating an ad and pausing it during review. Meta then loads the video data.

