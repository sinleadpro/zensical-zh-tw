---
title: "Set up and Connect Google Analytics"
description: "Step-by-step guide to connecting Google Analytics 4 (GA4), including creating the Google account, getting the Measurement ID, and entering the tracking ID in the CYBERBIZ admin."
created: "2026-03-20 14:54"
last_modified: 2026-07-02 16:28
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
  - 如何串接 Google Analytics
  - GA4 串接步驟
  - Google Analytics 設定教學
features:
  - Google Analytics
  - GA4
  - 評估 ID
  - 加強型評估
  - 資料串流
prerequisites: []
related:
  - ec/integrations/google/ga/ga4-exclude-internal-traffic-and-referrals/
  - ec/integrations/google/ga/google-analytics-advanced-tracking/
tags:
  - "Google Analytics"
  - GA4
  - "Third-party Integrations"
  - "Traffic Tracking"
  - "Data Analytics"
acoiv: configure
apis: []
devices: 
  - desktop 
  - mobile
ui_components: []
paths:
  - 第三方整合 > Google 整合
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=678
  - https://www.cyberbiz.io/support/?p=165
permalink: "https://help.cyberbiz.io/ec/integrations/google/ga/setup-google-analytics/"
comments: false
search:
  exclude: false
icon: lucide/link
hide: []
---

![GA4 Setup](../../../../assets/images/ec-第三方整合-google-ga4設定.en.png){ .hero-page title="GA4 Setup" }

## Google Analytics Overview

Google Analytics (GA4) is essential for running a brand website. It helps marketing teams track traffic and user behavior. The integration has two main steps: **creating the Google Analytics account** and **entering the ID in the storefront admin**.

## Setup Steps

### Create a Google Analytics Account <small>Google-side Steps</small>

1.  **Sign in to the GA admin**: Go to [Google Analytics :lucide-external-link:](https://analytics.google.com/), then click "Start measuring".

2.  **Set up the account and resources**:
    *   Enter the account name, then the property name.
    *   Select the industry, business size, and business goals, then check the box to agree to the terms of service.

    ![Account and resources setup](../../../../assets/images/ec-第三方整合-google-ga-建立帳戶.en.gif){ .screenshot title="Set up the account and resources" }

3.  **Set up the data collection source**:
    *   In the data collection flow, select "**Web**".
    *   Enter your website URL and website name.
    *   We recommend turning on "Enhanced measurement," which automatically records scrolling, clicks, site searches, and other behaviors.

    ![Data stream setup](../../../../assets/images/ec-第三方整合-google-ga-資料串流.en.png){ .screenshot title="Set up the data stream" }

4. **Set up the Google tag**: Keep the default recommended option, "Use the Google tag found on your website."

5.  **Get the Measurement ID**:
    *   After setup, you will be taken to the "Web stream details" page. Copy the **Measurement ID** that starts with `G-`.

    ![Get Measurement ID](../../../../assets/images/ec-第三方整合-google-ga-評估ID-blurred.en.png){ .screenshot title="Get Measurement ID" }

!!! info "For detailed setup instructions, see [Official Documentation :lucide-external-link:](https://support.google.com/analytics/answer/9304153?hl=zh-Hant&ref_topic=14088998&sjid=385438859130631159-NC)."

---

### Connect the GA4 Account to Your Website <small>CYBERBIZ Admin Steps</small>

!!! warning "Notes"

    - Merchants activated before 2022/12/27 must request GA4 activation through the admin support chat window, then complete the setup by switching from Universal Analytics to GA4 in Google Analytics.
    - If your theme is outdated, GA4 features are not supported. Merchants who need GA4 should update their theme version.


1.  **Navigate to the settings**: Go to the admin dashboard, then click "**Third-party Integrations** > **Google Settings** > **Google Integration**".
2.  **Enter the ID**:
    *   In the "Google Analytics 4" section, click "Go to settings."
    *   Paste the Measurement ID you copied earlier into the "**GA4 tracking ID**" field, then save.
    *   *Note: If your theme is outdated or GA4 is not yet enabled, you must request activation through the admin support chat window.*

![Enter GA4 Measurement ID](../../../../assets/images/ec-第三方整合-google-ga串接-輸入id.en.gif){ title="Enter GA4 Measurement ID" }

## How to Verify the Installation

1.  **Test the behavior**: Open the storefront, click any product, and perform the "**Add to Cart**" action.

    ![Add to cart on storefront](../../../../assets/images/ec-商品-加入購物車-前台.en.png){ .screenshot title="Add to cart on storefront" }

2.  **Check the real-time report**: Go back to the GA4 admin, click "Reports" > "Realtime" or "Realtime overview" in the sidebar, and check the event count. If the data changes, the connection is successful.

    ![GA4 real-time report](../../../../assets/images/ec-第三方整合-google-ga-即時報表.en.png){ .screenshot title="GA4 real-time report" }

## Next Steps

To ensure data accuracy, we recommend making the following adjustments after the connection is complete:

<div class="grid cards" markdown>

- :lucide-funnel-x:{ .lg }   
  [__Exclude Internal Traffic__](ga4-exclude-internal-traffic-and-referrals.md){ title="Set up GA4 internal traffic and referral exclusions" }     
  In the GA4 admin interface, under "Data streams," define your company IP addresses to keep browsing by developers or marketing staff from interfering with your analytics.

- :lucide-list:{ .lg }     
  [__List Inapplicable Referral Links__](ga4-exclude-internal-traffic-and-referrals.md#列出不適用的參照連結網址-排除第三方網站){ title="Set up GA4 internal traffic and referral exclusions" }  
  Add your payment and logistics providers to the exclusion list so that conversion sources are not mistakenly identified as third-party payment pages.

- :lucide-clock:{ .lg }     
  [__Extend Data Retention Period__](google-analytics-advanced-tracking.md#資料保留-data-retention){ title="Set up Google Analytics advanced tracking and data analysis" }  
  GA4 keeps data for only 2 months by default. We recommend going to "Data collection and modification" > "Data retention" and manually changing the setting to **14 months**.

- :lucide-radio:{ .lg }     
  [__Enable Google Signals (Google Signals)__](google-analytics-advanced-tracking.md#google-信號-google-signals){ title="Set up Google Analytics advanced tracking and data analysis" }  
  Turning on this feature provides cross-device usage data and more precise user profiles.

</div>

## FAQ

??? quote "How do I confirm that GA4 is connected successfully?"

    After the connection is complete, verify it in the following ways:

    1. Perform any action on the storefront, such as adding a product to the cart.
    2. Return to the GA4 admin and click "Reports" → "Realtime" or "Realtime overview."
    3. If the event count changes, the connection is successful.

??? quote "Can merchants activated before 2022 still use GA4?"

    Merchants activated before 2022/12/27 must proactively request GA4 activation through the admin support chat window, then switch from Universal Analytics to GA4 in Google Analytics. If your theme is outdated, GA4 may not be supported either, so we recommend updating your theme version as well.

??? quote "What is Enhanced Measurement?"

    Enhanced measurement is a built-in GA4 feature that automatically tracks user actions such as scrolling, clicks, and site searches, with no extra code required. We recommend turning it on when you set up the data stream.

