---
title: "Set up GMC Important Event Source Tracking and Auto-Tagging"
description: "Set up Google Merchant Center important event source tracking and auto-tagging to monitor product purchase metrics."
created: 2026-03-30 10:00
last_modified: 2026-07-08 15:19
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
  - 設定重要事件來源追蹤
  - 開啟自動標記
features:
  - 重要事件來源追蹤
  - 自動標記
prerequisites:
  - ec/integrations/google/setup-google-merchant-center/
  - ec/integrations/google/ga/setup-google-analytics/
related:
  - ec/integrations/google/setup-google-merchant-center/
  - ec/integrations/google/ga/setup-google-analytics/
  - ec/integrations/google/youtube-shopping-setup-guide/
  - ec/integrations/google/setup-google-ads-conversion-tracking/
tags:
  - GMC
  - auto_tagging
  - event_source
  - GA4
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 谷歌 Google 設定 > Google Merchant Center
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/integrations/google/setup-gmc-conversion-tracking/"
comments: false
search:
  exclude: false
icon: lucide/settings-2
hide: []
---

![GMC Important Event Settings](../../../assets/images/ec-gmc-重要事件設定.en.png){ .hero-page }

## Important Event Source Tracking { #operate-gmc-conversions }

**Event Source** can track product purchases from specific sources (such as Google Analytics or your own website), providing actionable insights. [Learn more :lucide-external-link:](https://support.google.com/merchants/answer/14166401?hl=zh-Hant&sjid=15151417659935872406-NC)

## What Is Auto-Tagging { #intro-gmc-conversions }

**Auto-tagging** is essential for tracking product purchases. When turned on, Google automatically adds parameters to ad links when users click them, so the system can accurately match ad clicks to conversion events. [Learn more :lucide-external-link:](https://support.google.com/merchants/answer/15191080?hl=zh-Hant#%E5%95%9F%E7%94%A8%E6%88%96%E5%81%9C%E7%94%A8%E8%87%AA%E5%8B%95%E6%A8%99%E8%A8%98)
## Steps { #operate-gmc-conversions-steps }

### Auto-Tagging Settings { #operate-gmc-conversions-steps-settings }

1.  **Go to GMC settings**: Sign in to Google Merchant Center and click **Settings** > **General** > **Important Event Settings**
2.  **Find Auto-tagging**: On the settings page, find the **Auto-tagging** option
3.  **Turn on the feature**: Switch **Auto-tagging** to **On**

![GMC auto-tagging settings](../../../assets/images/ec-gmc-自動標記設定.en.png){ .screenshot }

---

### Link GA4 to Merchant Center { #operate-gmc-conversions-steps-ga4-merchant-cen }

!!! warning "Prerequisites"

    Before you begin, make sure you have completed the following:

    - [x] Completed [Google Merchant Center account setup](setup-google-merchant-center.md){ title="Set up Google Merchant Center and sync CYBERBIZ products" }
    - [x] Created a [Google Analytics 4 (GA4) property and obtained its measurement ID](ga/setup-google-analytics.md){ title="Create and connect Google Analytics" }

After you link GA4 to Merchant Center, you can track conversions from Google Search and Shopping ads and view purchase metrics under "Data Analysis" in Merchant Center.

1.  **Go to GMC settings**: In the left navigation menu of Merchant Center, click the **Settings** icon
2.  **Open Important Event Settings**: Click **Settings** > **General** > **Important Event Settings**
3.  **Turn on Auto-tagging**: If Auto-tagging is not yet on, turn it on first. This is required before you can link GA4.
4.  **Add an important event source**: Click **Add Important Event Source**
5.  **Select Google Analytics**: Choose **Google Analytics**
6.  **Complete the link**: Click **Go to Google Analytics** in the dialog and follow the steps to authorize access. After you finish, refresh the page to see the link in the list.

!!! info "After you link the accounts, data may take 24-48 hours to appear. For setup details, see the [official guide :lucide-external-link:](https://support.google.com/merchants/answer/13881610?hl=zh-Hant#zippy=%2C%E5%89%8D%E5%BE%80-merchant-center)."

![Link GA4 in GMC](../../../assets/images/ec-gmc-連結ga4.en.gif)

??? success "Verify the Link Status"

    After setup, you can confirm that GA4 is linked to Merchant Center in the following ways:

    - **GMC check: ** Go to GMC > **Settings** > **General** > **Important Event Settings** > **Source List**, and the GA4 status should show as **Active** or **Linked**

        ![GMC GA4 important event link](../../../assets/images/ec-gmc-重要事件來源列表-ga4.en.png)

    - **GA4 check:** Go to GA4 > **Admin** > **Product Links** > **Merchant Center Links**, and confirm that your GMC ID appears in the list

        ![GA4 GMC link](../../../assets/images/ec-ga4-gmc連結.en.png)

## Next Steps { #next-steps-gmc-conversions }

<div class="grid cards" markdown>

- :simple-youtube:{ .lg }   
  [__YouTube Shopping__](youtube-shopping-setup-guide.md){ title="YouTube Shopping Setup Guide" }       
  Track product purchase conversions by embedding your storefront product information in YouTube videos, live streams, and short-form videos.

- :lucide-trending-up:{ .lg }   
  [__Google Ads Conversion Tracking__](setup-google-ads-conversion-tracking.md){ title="Set up Google Ads conversion tracking" }    
  Accurately report the orders your ads generate to improve ad performance.

</div>

## FAQ { #faq-gmc-conversions }

??? quote "Why do I need to turn on Auto-tagging?"
    Auto-tagging lets Google automatically add tracking parameters to ad click links. Without it, you cannot accurately track ad conversions.

??? quote "How soon does Auto-tagging take effect after I turn it on?"
    Auto-tagging usually takes effect immediately, but some data may take 24-48 hours to appear in reports.

??? quote "What is the difference between event source tracking and Auto-tagging?"
    - **Auto-tagging**: Links Google ad clicks to their conversions
    - **Event source**: Tracks purchases from multiple sources, such as Google Analytics and your own website
