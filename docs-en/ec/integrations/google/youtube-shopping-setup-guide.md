---
title: "YouTube Shopping Setup Guide"
description: "Use YouTube Shopping to add product information and links to videos, live streams, and Shorts to boost product visibility and drive revenue."
created: 2026-03-27 10:49
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
difficulty: ""
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定 YouTube Shopping
  - 在 YouTube 銷售商品
  - YouTube 直播購物
features:
  - YouTube Shopping
  - Google Merchant Center
  - 產品動態饋給
  - YouTube 合作夥伴計畫
prerequisites:
  - ec/integrations/google/setup-google-merchant-center/
  - ec/integrations/google/ga/setup-google-analytics/
related:
  - ec/integrations/google/setup-google-merchant-center/
  - ec/integrations/google/ga/setup-google-analytics/
  - ec/integrations/google/setup-gmc-conversion-tracking/
tags:
  - "YouTube Shopping"
  - GMC
  - "Live Shopping"
  - "Product Feed"
  - YPP
  - "Third-Party Integration"
acoiv: integration
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 谷歌 Google 設定 > Google Merchant Center
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10552
  - https://www.cyberbiz.io/helpcenter/?p=10555
  - https://www.cyberbiz.io/helpcenter/?p=10556
  - https://www.cyberbiz.io/support/?p=1979
  - https://www.cyberbiz.io/support/?p=6118
  - https://www.cyberbiz.io/support/?p=6149
permalink: "https://help.cyberbiz.io/ec/integrations/google/youtube-shopping-setup-guide/"
comments: ""
search:
  exclude: false
icon: simple/youtube
hide: []
---

## What Is YouTube Shopping { #intro-youtube-shopping }

**YouTube Shopping** lets you embed product information and links from your storefront in YouTube videos, live streams, and Shorts. If you make videos, run a YouTube channel, or go live on YouTube, you can set up YouTube Shopping to increase product exposure and turn traffic into revenue. [Learn more :lucide-external-link:](https://support.google.com/youtube/answer/12257682?hl=zh-Hant)

!!! warning "Eligibility"
    YouTube Shopping is a feature of the **YouTube Partner Program (YPP)** for creators who have a YouTube channel that meets the monetization threshold (1,000 subscribers + 4,000 watch hours).

## YouTube Shopping Setup Process { #operate-youtube-shopping }

```mermaid
graph LR
    %% --- Phase 1 ---
    subgraph S1 [Phase 1: Account Setup]
        direction TD
        A1([Create and connect GMC]) --> A2([Create and connect GA4])
    end

    %% --- Phase 2 ---
    subgraph S2 [Phase 2: YPP Eligibility Application]
        direction TD
        B1([Check eligibility]) --> B2{Meets threshold}
        B2 -- Not met --> B3([Accumulate subscribers/views])
        B2 -- Met --> B4([Apply online directly])
        B4 --> B5([AdSense Verify])
    end

    %% --- Phase 3 ---
    subgraph S3 [Phase 3: Linking & Operations]
        direction TD
        C1([Link GMC and GA4])
        C1 --> C2([YouTube Link Store])
        C2 --> C3([Upload Product Feed])
        C3 --> C4([28-Day Update & Tracking])
    end

    %% Cross-phase link
    S1 --> S2
    S2 --> S3
```

### 1. Account Setup and Back-End Linking { #operate-youtube-shopping-account-create-backend }

Before applying for YouTube Shopping, you must first integrate the two Google tools.

<div class="grid cards" markdown>

-   :lucide-tags:{ .lg .middle } __Create and Verify a GMC Account__

    ---

    Go to Google Merchant Center (GMC), complete your basic merchant information, and verify store ownership.

    [:lucide-arrow-right: Setup Guide](setup-google-merchant-center.md){ title="Set Up Google Merchant Center and Sync CYBERBIZ Products" }    

-   :lucide-chart-no-axes-column-increasing:{ .lg .middle } __Create and Connect a GA4 Account__

    ---

    In Google Analytics admin, get the "Measurement ID," then go to the CYBERBIZ admin and enter the Measurement ID to complete the integration.

    [:lucide-arrow-right: Setup Guide](ga/setup-google-analytics.md){ title="Create and Connect Google Analytics" }

</div>

---

### 2. YPP Eligibility Application { #operate-youtube-shopping-ypp-apply }

Your merchant channel must meet the monetization eligibility requirements of the [**YouTube Partner Program (YPP)** :lucide-external-link:](https://support.google.com/youtube/answer/72851?hl=zh-Hant&ref_topic=9153642) before you can turn on shopping features.

1.  **Check eligibility**: Sign in to [YouTube Studio :lucide-external-link:](https://studio.youtube.com/) and click **Monetization** in the left menu. If a green star appears, you are not yet eligible.

    ![YouTube Studio Monetization page](../../../assets/images/yt-ypp-營利頁面-blurred.en.png){ .screenshot }

2.  **Apply online**: When your channel reaches 1,000 subscribers and 4,000 watch hours (or 10 million Shorts views), you can apply for YPP eligibility directly through YouTube Studio. For eligibility and application details, see the [official documentation :lucide-external-link:](https://support.google.com/youtube/answer/72851?hl=zh-hk&co=GENIE.Platform%3DDesktop).


---

### 3. Apply and Connect Your Store { #operate-youtube-shopping-apply }

Once the accounts above and eligibility are ready, you can complete the final linking steps.

1.  **Apply for eligibility**: Fill in the [YouTube Shopping eligibility application form](https://docs.google.com/forms/d/e/1FAIpQLSeC92YTZOl0E-SO03SAv-QF_rRaWXNWdYLABZXEFwnfeXhzdQ/viewform), and CYBERBIZ will submit it to YouTube.
    - After your application is approved, CYBERBIZ will send an activation notice to the email address you provided on the application form. Continue with the next steps only after you receive the email.
2.  **Link GMC and GA4**: Enable auto-tagging in Merchant Center settings, and [link GA4 to Merchant Center](setup-gmc-conversion-tracking.md#operate-gmc-conversions-steps-ga4-merchant-cen){ title="Set up GMC key event source tracking and auto-tagging" }.
3.  **Link your YouTube channel and online store**: Go to [YouTube Studio :lucide-external-link:](https://studio.youtube.com/), open the **Monetization** > **Shopping** tab, click **Link store**, select **Other store**, and then specify your GMC account. For details, see the [official documentation :lucide-external-link:](https://support.google.com/youtube/answer/12258186?sjid=15941351074417695736-NC#)

    ![YouTube Studio Link Store GIF](../../../assets/images/yt-第三階段-連結Youtube商店.en.gif){ .screenshot }

4.  **Upload Product Feed**:
    - **Get the link**: Sign in to the CYBERBIZ admin, go to Third-Party Integration > Google Settings > Google Merchant Center, and copy the "Product Feed Link."

        ![GMC CYB Product Feed](../../../assets/images/ec-第三方整合-google-gmcproductfeed.en.png)

    - **Import into GMC**: Go to the GMC admin, click **Products** > **All products** > **Add products** > **Add other product sources**, and paste the link you just copied.

        ![GMC Add Product Source](../../../assets/images/ec-gmc-新增產品來源.en.gif)

    - **Enable the YouTube destination**: In the **Marketing method** settings, be sure to select **YouTube Shopping**, and click **Save** to make sure products sync to the YouTube platform.

        ![GMC Product Marketing Method YouTube Shopping](../../../assets/images/ec-gmc-產品行銷方式-youtube商店.en.png)

    - **Finish and Manually Update**: Click **Continue** to finish setup. On the source detail page, click **Update** to force the system to fetch the latest product information.

        ![GMC Product Source Details](../../../assets/images/ec-gmc-來源詳情.en.png)

        !!! warning "Automatic Product Removal Mechanism"
            If product information in the feed has **not been updated in GMC for over 30 days**, products will be automatically removed from YouTube. We recommend updating **every 28 days** to keep products active.

## Track YouTube Shopping Performance { #operate-youtube-shopping-tracking }

Use the GA4 Explore feature to track the website conversions that YouTube Shopping drives.

1.  **Create a new report**: In the GA4 left menu, click **Explore**, then click **Blank**.

2.  **Add Total Revenue and Sessions metrics**: Click **Metrics** > **Monetization** > select **Total revenue** and **Sessions** > select **Sessions**, and then click **Confirm**.

    ![GA4 Metrics - Sessions and Total Revenue](../../../../assets/images/ec-ga4-探索-指標-工作階段與總收益.en.gif)

3.  **Add dimension**: Click **Dimensions** > **Traffic source** > select **Session manual term**, and then click **Confirm**.

    ![GA4 Dimension - Session Manual Term](../../../../assets/images/ec-ga4-探索-維度-工作階段手動字詞.en.png)

4.  **Set filter conditions**:
    - Add **Session manual term** to **Rows**
    - Add **Sessions** to **Values**
    - Add **Total revenue** to **Values**
    - Add **Session manual term** to **Filters**, and set the condition to **Begins with** "UC"

    ![GA4 Explore - Filter Condition Settings](../../../../assets/images/ec-ga4-探索-篩選條件設定.en.gif)

6.  **Set date range**: Click the date menu to select a time range and view data for a specific period.

    ![GA4 Explore - Date Menu](../../../../assets/images/ec-ga4-探索-日期選單.en.gif)

## **Live Streaming Tip** { #intro-youtube-shopping-overview-youtube-shopping }

When you live stream on YouTube, you can schedule the stream in advance and generate a link to promote it. During the live stream, we recommend using the **Live Pinning** feature to pin the link to a pre-built product page (such as a one-page store) in the comments, so viewers can shop more easily.

## Next Steps { #next-steps-youtube-shopping }

<div class="grid cards" markdown>

- :lucide-play:{ .lg }   
  [__Tag Products in Video Content__:lucide-external-link:](https://support.google.com/youtube/answer/10191533)  
  Tag products in uploaded YouTube videos so viewers can click to buy directly.

- :lucide-video:{ .lg }   
  [__Tag Products in Live Streams__:lucide-external-link:](https://support.google.com/youtube/answer/12299016)  
  Tag products in real time during YouTube live streams to promote them instantly.

- :lucide-megaphone:{ .lg }   
  [__Live Shopping Promotion Tips__:lucide-external-link:](https://support.google.com/merchants/answer/12375318)  
  Best practices and tips for promoting products with YouTube live shopping.

</div>

## FAQ { #faq-youtube-shopping }

??? quote "What are the eligibility requirements for YouTube Shopping?"

    YouTube Shopping is a feature of the **YouTube Partner Program (YPP)**. Merchants must have a YouTube channel and meet the monetization threshold (1,000 subscribers + 4,000 watch hours, or 10 million Shorts views) before they can apply.

??? quote "How do I sync CYBERBIZ products to YouTube?"

    Follow these steps in order:

    1. Get the **Product Feed Link** in the CYBERBIZ admin (Third-Party Integration > Google Settings > Google Merchant Center).
    2. Go to the GMC admin, add a product source, and paste the link.
    3. In **Marketing method**, select **YouTube Shopping** and save.

??? quote "Why are products automatically removed from YouTube?"

    If product information in the feed has **not been updated in GMC for over 30 days**, products will be automatically removed from YouTube. We recommend updating **every 28 days** to keep products active.

