---
title: "Set up a Meta Ad Campaign"
description: "Manage Meta ad campaigns through the CYBERBIZ Meta Ads App, set budgets, audiences, and creative assets, and track ad performance."
created: 2026-04-20 14:54
last_modified: 2026-07-03 11:45
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - 確認 商品影片與圖片輪播功能版本限制
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
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions:
  - APP MARKET
intents:
  - 設定 Meta 廣告活動
  - 建立 Meta 廣告
  - 投放 Facebook 廣告
  - 投放 Instagram 廣告
features:
  - Meta Ads
  - 高效速成行銷活動
  - ASC
  - 目錄型廣告
  - 圖片型廣告
prerequisites:
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
  - ec/app-market/install-meta-ads-app/
related:
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
  - ec/app-market/install-meta-ads-app/
  - ec/integrations/fb/meta-ads/meta-ad-daily-budget-guide/
  - ec/products/create-and-manage/setup-product-videos/
  - ec/integrations/fb/meta-ads/sync-product-videos-meta-catalog/
  - ec/integrations/fb/meta-ads/setup-meta-ad-catalog-sets/
  - ec/integrations/fb/meta-ads/meta-ad-performance-analysis/
  - ec/integrations/fb/meta-ads/share-asset-permissions-cyberbiz/
tags:
  - "Meta Ads"
  - "FB Ads"
  - "IG Ads"
  - "Ad Delivery"
  - "Advantage+ Shopping"
acoiv: integration
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 臉書 Facebook 設定 > 廣告活動設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10374
  - https://www.cyberbiz.io/support/?p=1755
permalink: "https://help.cyberbiz.io/ec/integrations/fb/meta-ads/setup-meta-ad-campaign/"
comments: ""
search:
  exclude: false
icon: lucide/rocket
hide: []
---

![Create Meta ad campaign](../../../../assets/images/ec-第三方整合-fb-meta廣告-創建廣告活動.en.png){ .hero-page }

## Meta Ad Campaign Setup Guide { #operate-meta-campaign }

Set up your Meta ad campaign in the CYBERBIZ admin. With this integration, you can manage ad budgets, targets, and creative assets directly, without frequently switching to the Meta platform.

## Prerequisites and Limitations { #prerequisites-meta-campaign }

Before you begin, confirm that you have completed the following prerequisites:

- [x] **Reconnect [Facebook Business Extension](../mbe/setup-fbe-authorization.md){ title="Set up FBE account authorization and asset linking" }**: Due to Meta system updates, merchants should reconnect once to ensure data syncs correctly.
- [x] **Complete [Ad Account Creation and Top-Up](create-meta-ad-account-top-up.md){ title="Create a Meta ad account and add funds" }**: You must first apply for an ad account. Ads can run only after you add funds.

## Create Ad Campaign Workflow { #operate-meta-campaign-ads-flow }

1. **Open Meta Ads App**: Log in to the CYBERBIZ admin, then go to **Third-Party Integration > Facebook Settings > Campaign Settings**.

    - Not integrated yet: Click "Connect Now" (see [Install Meta Ads App](../../../app-market/install-meta-ads-app.md){ title="Install Meta Ads App" }).
    - Already integrated: Click "Go Now".

2. **Start editing**: In the left navigation, click Ad Campaigns > Campaign Settings > Create Ad Campaign.

    ![Create ad campaign in Meta Ads App](../../../../assets/images/ec-appmarket-maa-創建廣告活動.en.png)

3. **Complete the configuration**: After you open the editor, complete the following settings in order:

    <div class="grid cards" markdown>

    - :lucide-goal: [Campaign Objective Settings](#operate-meta-campaign-ads-flow-settings){data-preview }
    - :lucide-calendar: [Campaign Content Settings](#operate-meta-campaign-ads-flow-content-settings){ data-preview }
    - :lucide-image-play: [Ad Creative Settings](#operate-meta-campaign-ads-flow-ads-settings){ data-preview }

    </div>

4. **Save settings**: Click the **Save** button at the bottom of the page to complete the configuration.

---

### Campaign Objective Settings { #operate-meta-campaign-ads-flow-settings }

Choose a campaign objective based on your brand's current stage and marketing needs:

*   **Traffic ads**: Designed to direct customers to specific pages on your website, such as the homepage or brand introduction page. Especially suited to **early-stage brands** or **new product launches**, where they help collect early data and build an audience base.
*   **Sales ads**: Link ads to a product group on your website. Suited to merchants with **steady traffic**, these ads raise purchase likelihood and conversions for specific products.

![Campaign objective settings](../../../../assets/images/ec-appmarket-maa-活動目標設定.en.png)

??? example "Objective Differences and Budget Guidelines"

    | Item | Traffic ads | Sales ads |
    | :--- | :--- | :--- |
    | **Primary goal** | Direct traffic to a specific page | Boost product sales conversions |
    | **Daily Budget** | **Must be greater than NT$150** | **Must be greater than NT$50** |
    | **Key steps** | Select the landing page | Link a product catalog or product set |
    | **Recommended use** | New product launches, brand introductions | Best-selling product pages, promotion pages |

---

### Campaign Content Settings { #operate-meta-campaign-ads-flow-content-settings }

Set the ad name, daily budget, and delivery start and end times.

| Field name | Description | Notes |
| :--- | :--- | :--- |
| **Campaign Name** | We recommend including the date and product name for easy reference later. | Required |
| **Daily Budget** | - [Beginners: never run ads](meta-ad-daily-budget-guide.md#intro-meta-budget-ads){ title="Meta Ad Daily Budget Guide" }<br>- [Merchants with a known average CPA](meta-ad-daily-budget-guide.md#intro-meta-budget-ads-cpa){ title="Meta Ad Daily Budget Guide" }. | Required |
| **Start Time** | Starts immediately by default. You can also schedule a start time. | — |
| **End Time** | Runs continuously by default. You can also set an estimated end date. | — |


=== "Traffic Objective"

    ![Campaign content settings - traffic](../../../../assets/images/ec-appmarket-maa-活動內容設定-流量.en.png)

=== "Sales Objective"

    ![Campaign content settings - sales](../../../../assets/images/ec-appmarket-maa-活動內容設定-銷售量.en.png)

---

### Ad Creative Settings { #operate-meta-campaign-ads-flow-ads-settings }

Set up ad assets and copy. A single campaign can have up to 20 ad creatives.


| Field name | Setting description | Notes / Related features |
| :--- | :--- | :--- |
| **Ad name** | Enter the ad creative name. | For internal management |
| **Creative source** | Options depend on the selected **Campaign Objective**:<br>- **Sales ads**: Choose **Catalog** or **Single image**.<br>- **Traffic ads**: Default is **Image**.<br> [See differences in ad display](#intro-meta-campaign){ data-preview } | **Catalog**: Pulls data from [Pixel Settings](create-meta-ad-account-top-up.md#operate-meta-account-steps-settings-pixel){ title="Pixel Settings" }.<br>**PLUS/Enterprise** For merchants who have [uploaded product videos](../../../products/create-and-manage/setup-product-videos.md){ title="Set product videos" } and [synced the catalog](sync-product-videos-meta-catalog.md){ title="Sync product videos to the Meta catalog" }, ads rotate videos and product images in a carousel. |
| **Enter Ad Copy** | Enter **Primary Text**, **Headline**, and **Description**. |  |
| **Call to Action** | Set the button text on the ad (for example, Buy Now, Shop Now, or Learn More). | We recommend choosing based on your marketing goal |
| **Catalog product set** | Select the [catalog product set](setup-meta-ad-catalog-sets.md){ title="Set the Meta ad catalog product set" } for the ads to run. You can use pre-created product collections for precise targeting. | ※ Only products with a status of Public and that are Listed are supported.<br>※ Products tagged "Gift" or "Exclude product feed" cannot be selected. |
| **UTM parameters** | Set Source, Medium, and Campaign name. | Used to track performance in third-party tools |


=== "Traffic Objective"

    ![Ad creative settings - traffic objective](../../../../assets/images/ec-appmarket-maa-廣告創意設定-流量目標.en.png)

=== "Sales Objective"

    ![Ad creative settings - sales objective](../../../../assets/images/ec-appmarket-maa-廣告創意設定-銷售量目標.en.png)

## Ad Display Effects { #intro-meta-campaign }

=== "Catalog Type"

    ![Meta Ads App campaign results - catalog type](../../../../assets/images/ec-appmarket-maa-廣告活動設定-成果畫面-目錄型.en.png)

=== "Image Type"

    <div class="grid cards" markdown>

    - ![Meta Ads App campaign results - image type 01](../../../../assets/images/ec-appmarket-maa-廣告活動設定-成果畫面-圖片型-01.en.png)
    - ![Meta Ads App campaign results - image type 02](../../../../assets/images/ec-appmarket-maa-廣告活動設定-成果畫面-圖片型-02.en.png)

    </div>

## Manage Ad Campaigns { #operate-meta-campaign-manage-ads }

After you finish [creating](#operate-meta-campaign-ads-flow){ data-preview }, view all created campaigns in the list under **Campaign Settings** and manage them day to day.

![MAA - Ad campaign list](../../../../assets/images/ec-maa-廣告活動列表.en.png)

### Adjust Delivery Status { #operate-meta-campaign-manage-ads-status }

You can turn ad delivery on or off at any time with the toggle on the far left of the list:

* **On (ACTIVE)**: The ad runs on its schedule.
* **Off (PAUSED)**: Delivery stops immediately, and billing stops.

!!! tip "Difference Between Intended and Actual Status"
    The toggle reflects your "intended action." To confirm whether an ad is actually live, check the **Effective Status** field. For example, if the account balance is insufficient, the effective status shows "Abnormal" even when the toggle is on.

![MAA - Adjust delivery status](../../../../assets/images/ec-maa-廣告活動設定-調整投放狀態.en.png)

---

### Edit and View Details { #operate-meta-campaign-manage-ads-edit-view }

Click **Campaign Name** to reopen the editor and adjust the budget, schedule, or ad creative copy.

![MAA - Ad name](../../../../assets/images/ec-maa-廣告活動列表-廣告名稱.en.png)

!!! info "More Ad List Field Information"
    For detailed definitions and data interpretation of list metrics (such as ROAS, CTR, and frequency), see [Ad Campaign List Field Descriptions](meta-ad-performance-analysis.md#reference-meta-performance){ title="Meta Ad Performance Analysis" } documentation.

## Troubleshooting { #intro-meta-campaign-overview-meta-campaign }

<div class="grid cards" markdown>

- :lucide-wrench:{ .lg }   
  [__Manually Share Assets with CYBERBIZ__](share-asset-permissions-cyberbiz.md){ title="Manually Share Asset Permissions with CYBERBIZ" }       
  If ad creation fails, you can resolve the issue by manually sharing asset permissions (Facebook Pages, Pixels, and Catalogs) with CYBERBIZ Business Manager.

</div>

## Next Steps { #next-steps-meta-campaign }

<div class="grid cards" markdown>


- :lucide-chart-line:{ .lg }   
  [__Use Meta Ad Performance Analysis__](meta-ad-performance-analysis.md){ title="Meta Ad Performance Analysis" }       
  Track ad performance by reviewing key metrics such as ROAS, revenue generated, and ad spend. You can also use AI Insights to get data-driven insights and optimization recommendations.

</div>

## FAQ { #faq-meta-campaign }

??? quote "Who is the ad audience?"

    The system works with Meta's [Advantage+ Shopping Campaign (ASC) :lucide-external-link:](https://zh-tw.facebook.com/business/help/1362234537597370){ target="_blank" }, which uses AI to automatically narrow the audience down to the lowest CPA and highest ROAS. Merchants do not need to set parameters manually.

??? quote "Where are ad placements?"

    AI automatically selects the placements with the highest conversion rates, including Facebook posts, Instagram Stories, Reels, and Messenger.

??? quote "Can I run ads on Instagram?"

    Yes. You first need to link your Facebook Page and Instagram account. To link them, go to the [Business Manager backend](https://business.facebook.com/latest/settings), select "Pages" under "Accounts", click "Connect assets", click "Instagram accounts", and select the Instagram account you want to link. The link is then complete.

    ![Business Manager - Pages - Connect assets](../../../../assets/images/ec-第三方整合-meta企業管理平台-fb粉絲專頁-連結資產.en.png)

??? quote "What is the difference between traffic ads and sales ads?"

    - Traffic ads direct customers to specific pages on your website (such as the homepage or brand introduction page), and are suited to early-stage brands or new product launches.
    - Sales ads link ads to a product group on your website. They are suited to merchants with steady traffic and help increase purchase opportunities for specific products.
    - For daily budgets, we recommend more than 150 TWD for traffic ads and more than 50 TWD for sales ads.

??? quote "How many ad creatives can a single ad campaign have?"

    A single campaign can have up to 20 ad creatives.

??? quote "How do I resolve ad creation failures?"

    Ad creation failures are usually permission issues. See [Manually Share Asset Permissions with CYBERBIZ](share-asset-permissions-cyberbiz.md){ title="Manually Share Asset Permissions with CYBERBIZ" } for instructions, share the asset permissions with **CYBERBIZ Business Manager**, and contact customer support for troubleshooting.
