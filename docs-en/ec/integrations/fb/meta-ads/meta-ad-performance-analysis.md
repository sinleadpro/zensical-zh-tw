---
title: "Using Meta Ad Performance Analysis"
description: "Track ad performance data in the Meta Ads App, analyze key metrics, and use AI Insights to get data-driven insights and optimization suggestions."
created: 2026-04-21 11:29
last_modified: 2026-07-03 11:45
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
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 分析廣告成效
  - 查看 ROAS
  - 使用 AI Insights
features:
  - 成效總覽
  - AI Insights
  - 廣告活動列表
prerequisites:
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/meta-ads/setup-meta-ad-campaign/
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
tags:
  - Meta_Ads
  - ROAS
  - CPA
  - AI_Insights
  - Ad_Performance
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 成效總覽
  - 廣告活動列表
paths:
  - 第三方整合 > 臉書 Facebook 設定 > 廣告活動設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1737
  - https://www.cyberbiz.io/support/?p=48371
permalink: "https://help.cyberbiz.io/ec/integrations/fb/meta-ads/meta-ad-performance-analysis/"
comments: false
search:
  exclude: false
icon: lucide/chart-column
hide: []
---

![MAA-Ad Performance Analysis](../../../../assets/images/ec-maa-廣告成效分析.en.png){ .hero-page }

## Meta Ad Performance Analysis Guide { #overview-meta-performance }

**Meta Ad Performance Analysis** is an analysis tool designed for CYBERBIZ merchants. It helps you track the performance of Meta ads (such as Facebook and Instagram), identify which products are worth promoting further, and determine whether your ad strategy is profitable.

## Prerequisites and Limitations { #prerequisites-meta-performance }

Before you start analyzing performance, make sure you have completed the following preparation steps so that data is returned and displayed correctly:

- [x] **Complete ad campaign setup**: This feature generates data only after your ad campaign has officially started. If you have not created an ad yet, first refer to [Set Up Meta Ad Campaign](setup-meta-ad-campaign.md){ title="Set Up Meta Ad Campaign" }.
- [x] **Make sure assets are linked correctly**: Confirm that you have completed authorization through the [Facebook Business Extension (FBE)](../mbe/setup-fbe-authorization.md){ title="Set Up FBE Account Authorization and Asset Linking" }, and that the Meta Pixel and Conversions API (CAPI) are correctly installed.
- [x] **Check account balance**: Your ad account must have sufficient balance or a valid payment method. Otherwise, performance data will show as "Abnormal" or stop updating.

## Track Overall Performance <small>Overview Metrics</small> { #overview-meta-performance-summary }

On the Performance Overview page, you can quickly evaluate the quality of your Meta ad delivery across two dimensions: **Traffic Ads** and **Sales Ads**.

!!! info "Select Analysis Date Range"  

    To view data for a specific period, first click the **Time Filter Dropdown :lucide-calendar-days:** in the upper-left corner of the page, then select a range (for example, Last 7 Days or Last 14 Days). The system automatically compares the change against the "previous period" for the selected range and displays the percentage change below each metric:

    - **Positive (↑)**: The metric increased compared with the previous period.
    - **Negative (↓)**: The metric decreased compared with the previous period.
    - **Shown as "—"**: No data is available for the previous period to compare against (for example, the ad had not yet been running during that period).

![MAA-Performance Overview](../../../../assets/images/ec-maa-成效總覽-gen.en.png)

=== "Traffic Ads"

    This section shows whether your ad content successfully attracts audiences and how they behave before reaching your online store.

    | Metric Name | Definition and Calculation | Data Insights and Optimization Suggestions |
    | :--- | :--- | :--- |
    | **Clicks** | Total number of times users click the ad link. | **High value:** Creative and audience targeting are precise.<br>**Low value:** Creative is not compelling enough, or the audience targeting is too narrow. |
    | **Click-Through Rate (CTR)** | (Clicks ÷ Impressions) x 100% | **Average benchmark:** About 0.9% – 1.5% for e-commerce.<br>**Low CTR:** Adjust the ad image or headline, or change the audience. |
    | **Frequency** | Average number of times each user sees the ad. | **1–3 times:** Within the normal range and helps build awareness.<br>**> 5 times:** Audience fatigue. Consider expanding the audience or refreshing the creative. |

=== "Sales Ads"

    This section's metrics relate directly to order revenue and help you determine whether your ads are profitable.

    | Metric Name | Core Definition and Calculation | Data Insights and Optimization Suggestions |
    | :--- | :--- | :--- |
    | **Revenue** | Cumulative purchase amount attributed to the ad campaign. | **Data source:** Purchase records tracked through Meta Pixel and the Conversions API (CAPI).<br>**Attribution logic:** 7-day click, 1-day view.<br>**Note:** Due to iOS 14 privacy restrictions, figures may differ from actual orders. |
    | **Return on Ad Spend (ROAS)** | Ad revenue ÷ Ad spend | **Meaning:** The revenue returned for every NT$1 in ad spend.<br>**Assessment:** <br>- ROAS > 1: Revenue exceeds ad spend.<br>- ROAS < 1: Loss warning. Consider optimizing creative or audience.<br> * Gross margins vary by brand. Set your own "break-even ROAS" based on your cost structure. |
    | **Cost per Acquisition (CPA)** | Total ad spend ÷ Number of purchases | **Break-even key:** The average ad cost to acquire one order.<br>**Optimization:** Compare against the average gross profit per product. If `CPA > gross profit`, the ad campaign is running at a loss. |

## Ad Campaign List Field Descriptions { #reference-meta-performance }

In the ad campaign list below the metrics overview, you can view the detailed operating status of each campaign.

![MAA-Ad List Fields](../../../../assets/images/ec-maa-廣告列表欄位.en.png)

### Status and Basic Information { #reference-meta-performance-status }

| Field Name | Description | Technical Details / Notes |
| :--- | :--- | :--- |
| **On / Off (Status)** | Controls the manual delivery intent of the ad campaign. | **Takes effect immediately after switching:** Changes sync to the Meta backend. |
| **Campaign Name** | Displays the campaign name. Click it to open the edit page. | |
| **Effective Status** | Actual delivery status returned by Meta. | Considers review, balance, and on/off factors together. For details, see [Effective Status Breakdown](#reference-meta-performance-status-unlisted){ data-preview }. |
| **Schedule** | Displays the delivery period of the ad set. | **Display format:** `YYYY-MM-DD`.<br> If no end time is set, "Ongoing" is displayed. |

---

### Ad Performance Data Fields { #reference-meta-performance-fields }

Performance data (impressions, clicks, revenue, spend, ROAS) is displayed in the store's configured currency.

| Metric Field | Core Definition | Technical Notes |
| :--- | :--- | :--- |
| **Impressions** | Cumulative total number of times the ad was displayed in FB / IG placements. | — |
| **Clicks** | Cumulative number of times users actually clicked the ad link. | For example: clicking the Page name, liking, commenting, sharing, or expanding photos / videos. |
| **Click-Through Rate (CTR)** | (Clicks ÷ Impressions) × 100% | **Benchmark:** The e-commerce average is about `0.9%–1.5%`.<br>**Optimization:** Low CTR means the creative is not compelling enough; high CTR with low conversions means you should check the landing page. |
| **Frequency** | Average number of times each user sees the ad (estimated).<br>Impressions ÷ Reach | **Audience Fatigue Indicator:** <br>- **1–3 times**: within the normal range.<br>- **> 5 times**: High fatigue risk. CTR usually declines, so consider refreshing the creative. |
| **AD revenue** | Purchase amount attributed to this ad. | Uses Meta attribution logic (7-day click / 1-day view). |
| **Spend** | Total ad spend accumulated for this ad campaign. | — |
| **ROAS** | Ad-attributed revenue ÷ Ad spend |  |


---

### Refresh Mechanism and Pagination { #specs-meta-performance-pagination }

!!! warning "Data Refresh Notice"
    Non-real-time data: Performance data is updated approximately every 24 hours and cached in the system.

To ensure loading performance, each page displays 25 ad campaigns by default. Click the pagination below the list to switch pages.

- Adjust the number of rows: Click the **rows-per-page dropdown** below the list to show 25, 50, or 100 ads per page.
- Pagination: Click the page number or arrow icons in the lower-right corner to view activity records on other pages.

![MAA-Pagination Management](../../../../assets/images/ec-maa-廣告活動列表-分頁管理.en.png)

## AI Insights Feature { #intro-meta-performance }


Merchants can enable "AI Insights" to chat with the system and automatically generate data insights and optimization suggestions:

1.  **Go to Meta Ads App**: Log in to the CYBERBIZ admin backend and go to **Third-Party Integration > Facebook Settings > Campaign Settings**.

    - Not yet connected: Click **Connect Now** (see [Install Meta Ads App](../../../app-market/install-meta-ads-app.md){ title="Install Meta Ads App" }).
    - Already connected: Click **Go Now**.

2.  **Open the AI analysis window**: Switch to the **Campaign** tab, then click the **AI Analysis** button in the upper-right corner of the campaign list page to open the AI Insights page.

    ![MAA-aiinsights-Path](../../../../assets/images/ec-maa-廣告列表欄位-aiinsights-路徑.en.png)

2.  **Select a time range:** Choose the date range you want to analyze, then click **Apply**. The system automatically pulls ad data for that period from Meta.

    ![MAA-aiinsights-Select Range](../../../../assets/images/ec-maa-ai-insights-選取區間.en.png)

    !!! info "In line with Meta policy, AI Insights supports analysis of data from up to the past **35 months**."

3.  **Get insights:** AI provides suggestions based on model inference results. If you are unsure what to ask, select a **Popular Question Template** provided by the system (for example: How is my ROAS performing? Which ads are performing best?).

    ![MAA-aiinsights-Popular Topics](../../../../assets/images/ec-maa-ai-insights-熱門主題.en.png)

## Next Steps { #next-steps-meta-performance }

<div class="grid cards" markdown>

- :lucide-rocket:{ .lg }   
  [__Create Ad Campaign__](setup-meta-ad-campaign.md){ title="Set Up Meta Ad Campaign" }       
  After completing your performance analysis, you can create new Meta ad campaigns based on the data insights.

- :lucide-package-x:{ .lg }   
  [__Exclude Product Sync__](../mbe/exclude-products-fb-instagram-sync.md){ title="Exclude Products from Syncing to Facebook and Instagram Stores" }       
  If you do not want specific products synced to Meta, you can set an exclusion tag.

</div>

## Frequently Asked Questions { #faq-meta-performance }

??? quote "What is a good ROAS value?"

    There is no universal standard for a "good" ROAS. It depends on your product gross margin. General guidelines:

    - **ROAS > 1**: Revenue exceeds ad spend, but generally does not break even.
    - **ROAS > 2**: Considered the basic profitability threshold.

    - Gross margins vary by brand. We recommend setting your own "break-even ROAS" based on your cost structure.

??? quote "What should I do if an ad status shows "Abnormal"?"

    Common causes include:

    - **Insufficient ad account balance**: Go to **Third-Party Integration > Facebook Settings > Ad Account Settings** to check your balance, or [top up your account](create-meta-ad-account-top-up.md#operate-meta-account-steps-ads){ title="Create a Meta Ad Account and Complete Top-Up" }.
    - **Abnormal pixel setup**: Confirm that the Pixel is correctly connected.
    - **Creative review not passed**: Check whether your ad creative complies with Meta policies.

    See [Effective Status Breakdown](#reference-meta-performance-status-unlisted){ data-preview } for more status details.

??? quote "Why do ad data and actual orders differ?"

    Possible causes include:

    - **iOS privacy restrictions**: Due to Apple's iOS 14.5+ privacy policy, the data Facebook can collect may be incomplete. See [official documentation](https://zh-tw.facebook.com/business/help/1329822420714248?id=428636648170202&helpref=faq_content){ target="_blank" }.
    - **Attribution timing differences**: Data uses an attribution window of 7 days after click and 1 day after view, which may differ in timing from actual store orders.
    - **Pixel setup issues**: Confirm that you use the correct [Pixel setup](create-meta-ad-account-top-up.md#operate-meta-account-steps-settings-pixel){ title="Create a Meta Ad Account and Complete Top-Up" }, and connect through the CYBERBIZ Business Extension. **We do not recommend installing the Pixel through GTM**, as it can cause duplicate events, incorrect Pixel data, and other issues.

    To reconnect, see [Set Up FBE Account](../mbe/setup-fbe-authorization.md)link.md){ title="Set Up FBE Account Authorization and Asset Linking" }.

## References { #reference-meta-performance-references }

### Effective Status Breakdown { .unlisted } { #reference-meta-performance-status-unlisted }


| Status | Meaning | Display Color |
| :--- | :--- | :--- |
| **In Progress** | The ad is delivering normally and receiving traffic. | **Blue** |
| **In Process** | Meta is reviewing the creative, which usually completes within a few hours. | **Yellow** |
| **With Issues** | Delivery is interrupted. A common cause is **insufficient ad account balance**. | **Red** |
| **Paused** | Manually turned off by the merchant, or automatically paused due to account issues. | **Gray** |
| **Archived/Deleted** | The ad has been removed from the system or the Meta backend. | **Gray** |


