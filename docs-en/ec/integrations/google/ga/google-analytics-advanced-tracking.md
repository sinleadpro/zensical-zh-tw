---
title: "Set up Google Analytics Advanced Tracking and Data Analysis"
description: "Configure Enhanced Measurement, Google Signals, data retention, and reporting identity to help merchants get more accurate traffic data and user profiles."
created: 2026-03-20 17:50
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 進階資料分析
  - 開啟加強型評估
  - 啟用_Google_信號
  - 調整資料保留期限
  - 報表識別資訊設定
features:
  - Google Analytics 4
  - 加強型評估
  - Google 信號
  - 資料保留
  - 報表識別資訊
prerequisites:
  - ec/integrations/google/ga/setup-google-analytics/
related:
  - ec/integrations/google/ga/ga4-exclude-internal-traffic-and-referrals/
  - ec/integrations/google/ga/setup-ga4-site-search-tracking/
tags:
  - GA4
  - Google_Analytics
  - Enhanced_Measurement
  - Google_Signals
  - Data_Retention
  - Traffic_Analysis
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7099
  - https://www.cyberbiz.io/support/?p=36980
permalink: "https://help.cyberbiz.io/ec/integrations/google/ga/google-analytics-advanced-tracking/"
search:
  exclude: false
icon: lucide/chart-column-increasing
hide: []
comments: false
---

![GA4 Advanced Data Analysis](../../../../assets/images/ec-第三方整合-google-ga-資料收集與修改.en.png){ .hero-page title="GA4 Advanced Data Analysis" }

## Google Analytics Advanced Data Analysis Guide

After you complete the basic connection between Google Analytics 4 (GA4) and your website, GA4 starts recording basic traffic data. To analyze your website traffic in more depth and build more accurate user profiles, follow the instructions below to configure advanced settings.

## <small>Enhanced Measurement</small>

This is GA4's built-in automatic tracking feature. Once turned on, the system records a range of user interactions on your website without requiring any additional tracking code.

*   **Tracked actions:** Includes page views, page scrolling, outbound link clicks, site search, form interactions, video views, and file downloads. For details on each tracked event, see the [official documentation :lucide-external-link:](https://support.google.com/analytics/answer/9216061?hl=zh-Hant&ref_topic=13367566&sjid=2617040479571463046-NC).
*   **Setup path:** In the GA4 admin, click "Admin" > "Data Collection and Modification" > "Data Streams" > select your stream > "Events" > turn on "Enhanced Measurement".

    ![Turn on Enhanced Measurement](../../../../assets/images/ec-第三整合-google-ga4-開啟加強型評估.en.gif){ title="Turn on Enhanced Measurement" }

*   **Advanced settings:** Click the gear icon :lucide-cog: to choose the specific events you want to measure.

    ![Configure Enhanced Measurement](../../../../assets/images/ec-第三方整合-ga4-設定加強型評估.en.png){ title="Configure Enhanced Measurement" }

## <small>Google Signals</small>

When a user signs in to a Google account and has Ads Personalization turned on, this feature helps the system collect cross-device and cross-platform usage data, giving a fuller view of the user across devices.

*   **Key features:** Builds target audience profiles by gender, age, and interests, and creates remarketing lists.
*   **Setup path:** In the GA4 admin, click "Admin" > "Property Settings" > "Data Collection and Modification" > "Data Collection". In the "Google Signals data collection" section, click "Enable".

![Enable Google Signals](../../../../assets/images/ec-第三方整合-google-ga4-google信號啟用.en.png){ title="Enable Google Signals" }

## <small>Data Retention</small>

The default data retention period in GA4 is only 2 months, which is not enough for merchants who need to track long-term trends or build remarketing lists.

*   **Recommended change:** Extend the data retention period to **14 months**.
*   **Setup path:** In the GA4 admin, click "Admin" > "Property Settings" > "Data Collection and Modification" > "Data Retention" to make the change.

![Data retention period settings](../../../../assets/images/ec-第三方整合-google-ga4-資料保留.en.png){ title="Data retention period settings" }

## <small>Reporting Identity</small>

This technology helps merchants avoid counting the same user more than once. For example, if a customer browses on their phone and then places an order on their computer, GA4 can recognize them as the same user.

*   **Common modes:**
    *   **Mixed:** Combines all available signals (User ID, Google Signals, device ID) for the most complete analysis.
    *   **Observed:** Uses only device information that was actually observed, so report results are more conservative and closer to the original records.
*   **Setup path:** In the GA4 admin, click "Admin" > "Property Settings" > "Data Display" > "Reporting Identity".

![Reporting identity settings](../../../../assets/images/ec-第三方整合-google-ga4-報表識別資訊.en.png){ title="Reporting identity settings" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-funnel-x:{ .lg }   
  [__Exclude Internal Traffic and Irrelevant Links__](ga4-exclude-internal-traffic-and-referrals.md){ title="Set up GA4 to exclude internal traffic and third-party referral sources" }     
  To avoid skewed data, we recommend excluding browsing activity from internal staff and interference from external payment and logistics URLs.

- :lucide-search-code:{ .lg }   
  [__Site Search Tracking__](setup-ga4-site-search-tracking.md){ title="Set up GA4 site search tracking" }       
  Track how users search your website to understand shoppers' information needs and search intent.

</div>

## Frequently Asked Questions

??? quote "What user actions does Enhanced Measurement track?"

    After you turn on Enhanced Measurement, the system automatically tracks the following actions:

    - Page views
    - Page scrolling
    - Outbound link clicks
    - Site search
    - Form interactions
    - Video views
    - File downloads

    None of these require additional tracking code. The system records them automatically.

??? quote "Do users need to sign in to a Google account for Google Signals?"

    Yes. Google Signals only collects cross-device data when the user is signed in to a Google account and has Ads Personalization turned on. If the user is not signed in or has turned off Ads Personalization, the system cannot track their cross-device behavior.

??? quote "What is the difference between Enhanced Measurement and Google Signals?"

    Although Enhanced Measurement and Google Signals both strengthen GA4 data collection, they serve different purposes, use different data sources, and fit different use cases:

    | Feature | Enhanced Measurement | Google Signals |
    |------|------------|-------------|
    | Data source | User interactions on the website itself | User activity while signed in to a Google account (cross-device) |
    | Audience | All visitors | Users signed in to Google with Ads Personalization turned on |
    | Data collected | Page views, scrolling, search, video interactions, and similar behavior | Gender, age, interests, device preferences, and cross-device interactions |
    | Use cases | Website content optimization and user engagement analysis | Cross-device conversion tracking, remarketing list creation, and audience profiling |

    You can turn on both at the same time, and they complement each other. Enhanced Measurement focuses on on-site interactions, while Google Signals adds a cross-platform, cross-device view of users. Merchants should decide whether to turn on Google Signals based on their marketing needs and privacy policy.

??? quote "What is the maximum data retention period in GA4?"

    The default data retention period in GA4 is 2 months. If you need to track long-term trends or build remarketing lists, we recommend extending it to 14 months.
