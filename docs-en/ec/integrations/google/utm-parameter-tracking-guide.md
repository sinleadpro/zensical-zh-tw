---
title: "Track Marketing Traffic and Analyze Performance with UTM Parameters"
description: "Use UTM parameters to tag marketing links, track traffic sources, and analyze channel performance in GA4."
created: 2026-03-25 19:22
last_modified: 2026-07-03 11:44
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - 1st grid card pending, 推薦人分潤 doc missing content
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
  - 使用 UTM 追蹤流量
  - 分析行銷成效
  - 設定 GA4 流量來源
features:
  - UTM 參數
  - Campaign URL Builder
  - GA4 流量報表
prerequisites:
  - ec/integrations/google/ga/setup-google-analytics/
related:
  - ec/integrations/google/ga/setup-google-analytics/
  - ec/profit-sharing/referral-link-applications/
  - ec/orders/reports/export-order-report/
tags:
  - UTM
  - Traffic_Tracking
  - Marketing_Analytics
  - GA4
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > GA 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5156
  - https://www.cyberbiz.io/support/?p=6434
permalink: "https://help.cyberbiz.io/ec/integrations/google/utm-parameter-tracking-guide/"
comments: false
search:
  exclude: false
icon: lucide/snail
hide: []
---

![GA4 Traffic Acquisition](../../../assets/images/ec-第三方整合-google-ga4-流量開發.en.png){ .hero-page }

## UTM Overview

**UTM (Urchin Tracking Module)** is a small parameter appended to the end of a URL to tag traffic source information. With UTM, merchants can have Google Analytics (GA4) accurately record which ad, social platform, or email led users to the site. This is essential for analyzing marketing performance and attributing traffic.

## UTM URL Structure and Common Parameters

An example of a URL containing UTM is: `https://www.example.com/?utm_source=facebook&utm_medium=social`.  
The five most commonly used parameters are listed below:

|Parameter|Required|Description|Example|
|:---|:---:|---|---|
| `utm_source` | :lucide-check: | Identifies the platform or website that sends the traffic | `facebook`, `google`, `newsletter` |
| `utm_medium` |:lucide-check: | Identifies the marketing medium | `social` (social), `email`, `cpc` (paid click), `live` (live stream) |
| `utm_campaign` |:lucide-check: | Used to identify a specific promotion | `summer_sale`, `mothersday` |
| `utm_term` | - | Commonly used to tag keywords in paid search ads | `Running Shoes`, `iPhone15` |
| `utm_content` | - | Used for A/B testing<br>Distinguishes different creatives or link placements within the same campaign | `banner1`, `textlink_a` |


## Prerequisites and Guidelines

To ensure GA4 records your data accurately, be sure to follow these guidelines:

- [x] **Use consistent letter case**: GA4 is case-sensitive. If you use `Facebook` and `facebook` at the same time, the system treats them as two different sources.
- [x] **Avoid spaces and special characters**: Spaces cause garbled URLs. Use an **underscore (_)** or a **hyphen (-)** instead of spaces.
- [x] **Use English letters only**: Avoid Chinese characters to prevent encoding errors that cause garbled text.
- [x] **Create a UTM naming master list**: We recommend creating a master list that records all the names you have configured, so team members can follow consistent naming rules.

## Steps

### UTM Setup Tool <small>Campaign URL Builder</small>

Use the official Google [**Campaign URL Builder** :lucide-external-link:](https://ga-dev-tools.google/campaign-url-builder/) to quickly generate links:

1.  Go to the tool page and paste the website URL you want to track.
2.  Enter the parameter names above in order (English letters recommended).

    ![UTM URL Builder Fields](../../../assets/images/ec-第三方整合-utm-campaignurlbuilder-infofields.en.png)

3.  The system generates the full URL with UTM parameters below in real time. Copy it and use it directly.

    ![Generated UTM URL](../../../assets/images/ec-第三方整合-utm-campaignurlbuilder-generatedurl.en.png)

---

### View Data in GA4 Reports

!!! warning "First, complete the [GA4 integration with your website](ga/setup-google-analytics.md){ title="Set up and connect Google Analytics" } so you can view website traffic data in GA4."

After you publish your links, check their performance in the GA4 dashboard:

1.  **Path**: Sign in to the [GA4 Dashboard :lucide-external-link:](https://analytics.google.com/analytics/web/), then go to **Reports ** > **Business objectives ** > **Generate leads ** > **Traffic acquisition**.
2.  **Dimension**: In the report, switch the primary dimension to **Session source / medium**.
3.  **Analyze data**: View the clicks, user behavior, and conversion performance from each channel.
4. *Note: GA4 data processing takes about 24 to 48 hours, so data is not displayed in real time.*

![GA4 Traffic Acquisition Source / Medium](../../../assets/images/ec-第三方整合-ga4-流量開發-工作階段來源或媒介.en.gif)

## Next Steps

<div class="grid cards" markdown>

- :lucide-hand-coins:{ .lg }  
  [__Affiliate / Referral Links__](../../profit-sharing/referral-link-applications.md){ title="Using Referral Code Links" }  
  To manually add UTM parameters to a URL that includes a referral code (that is, one that includes `?rcode=...`), you must use **&** to separate each parameter after rcode.

- :lucide-file-spreadsheet:{ .lg }  
  [__Order Report Export__](../../orders/reports/export-order-report.md#步驟一選擇報表欄位){ title="Export Order Reports" }  
  In the admin, Order Report Export lets you select UTM-related fields (such as source, medium, and campaign name), so you can download an Excel file for offline analysis.

</div>

## Frequently Asked Questions

??? quote "Can UTM parameters use Chinese names?"
    We do not recommend using Chinese. UTM parameters should use English letters only to prevent encoding errors that cause garbled URLs, which can affect the accuracy of GA4 data statistics.

??? quote "How do I add UTM parameters to a referral code URL?"
    If the URL already includes a referral code (`?rcode=...`), separate the UTM parameters after the referral code parameter with **&**. Correct example: `https://...?rcode=xxx&utm_source=facebook&utm_medium=social`.

??? quote "How long does it take for UTM data to appear in GA4?"
    GA4 data processing takes about **24 to 48 hours**, so data is not displayed in real time. After you create UTM links, allow time for the data to come in.

