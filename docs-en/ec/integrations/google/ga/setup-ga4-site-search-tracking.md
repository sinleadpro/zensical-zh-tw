---
title: "Set up GA4 Site Search Tracking"
description: "Use GA4 Enhanced Measurement to track site searches on your storefront and analyze consumers' information needs and search intent."
created: 2026-03-24 20:05
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
  - 設定 GA4 站內搜尋追蹤
  - 查看網站搜尋關鍵字
  - 分析消費者搜尋行為
features:
  - GA4 加強型評估
  - 站內搜尋追蹤
  - view search results 事件
  - search term 參數
prerequisites:
  - ec/integrations/google/ga/setup-google-analytics/
related:
  - ec/integrations/google/ga/setup-google-analytics/
tags:
  - GA4
  - "Site Search"
  - "Search Tracking"
  - "Enhanced Measurement"
  - "Consumer Behavior"
  - "Third-Party Integration"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - GA4 後台 > 管理 > 資源設定 > 資料收集和修改 > 資料串流
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12099
  - https://www.cyberbiz.io/support/?p=28483
permalink: "https://help.cyberbiz.io/ec/integrations/google/ga/setup-ga4-site-search-tracking/"
search:
  exclude: false
icon: lucide/search-code
hide: []
comments: false
---

![GA4 site search tracking](../../../../assets/images/ec-第三方整合-google-ga4-加強型評估-站內搜尋.en.png){ title="GA4 Site Search Tracking" .hero-page }

## GA4 Site Search Tracking Guide

Turn on site search tracking for **Google Analytics 4 (GA4)**. This helps merchants see the keywords users enter on the website and understand consumers' information needs and search intent.

## Prerequisites and Restrictions

- [x] Confirm [your website is connected to GA4](setup-google-analytics.md){ title="Set up and connect Google Analytics" }.

## Setup Steps

Sign in to your Google Analytics dashboard and follow this path:

1.  **Go to Settings**: In the lower-left corner, click **Admin** > **Property Settings** > **Data Collection and Modification** > **Data streams**, and select the stream bound to your website.
2.  **Turn on Enhanced measurement**: In the "Events" section, find "**Enhanced measurement**", and click the gear icon :lucide-cog: on the right to open its settings.
3.  **Enable site search**: Find the "**Site search**" item and turn on the toggle.
4.  **Set query parameters**: Click "**Show advanced settings**", and in the "Search term query parameters" field, enter: `q,s,search,query,keyword` (separate with half-width commas), then save the settings.

![Enable site search settings](../../../../assets/images/ec-第三方整合-google-ga4-加強型評估-開啟站內搜尋.en.gif){ title="Enable site search settings" }

!!! warning "Data Delay"

    After setup, GA4 needs some time to start collecting search data (data is not backfilled). If no one runs a search in a short period, the event may not show data. You can test by running a search on your storefront.

## How to View Tracking Results

After setup (and once a user runs a search), you can view the results in GA4 reports:

1.  In the **Realtime report view**: go to **Reports** > **Realtime** (or **Realtime overview**), and in the **Event count** section, find the `view_search_results` event.

    ![GA4 search results event](../../../../assets/images/ec-第三方整合-google-ga4-報表-view_search_results.en.png){ title="GA4 search results event" }

2.  **View keyword details**: Click the `view_search_results` event, then click the `search_term` parameter to view the **keyword records** and search counts for terms users have searched on your website.

    ![Search keyword records](../../../../assets/images/ec-第三方整合-google-ga4-報表-search_term.en.png){ title="Search keyword records" }

!!! info "For more information about GA4 tracking events, see the [official documentation :lucide-external-link:](https://support.google.com/analytics/answer/9322688?hl=zh-Hant#zippy=%2C%E5%8D%B3%E6%99%82%E5%A0%B1%E8%A1%A8%2Cdebugview-%E5%A0%B1%E8%A1%A8)."

## FAQ

??? quote "How long after setup can I see search data?"

    GA4 site search data does not appear immediately. It usually takes some time for the system to collect data. If no users run a search in a short period, the event may not show data. You can speed up testing by running searches on your storefront.

??? quote "Why can't I see search keyword data?"

    Possible causes include:

    - The storefront is not correctly connected to the GA4 code (Measurement ID)
    - The feature was just set up, and data collection has not started yet (data is not backfilled)
    - No users ran a search during that period

??? quote "Which search keywords can be tracked?"

    Any search keyword entered on your storefront is recorded. You can click the `view_search_results` event in your GA4 reports, then view the `search_term` parameter to browse all keyword records and search counts.

