---
title: "Advertising Analysis"
description: "See impressions, clicks, conversions, and ROAS for your Google Shopping ads in CYBERBIZ without signing in to Google Ads."
created: 2026-06-15 00:00
last_modified: 2026-07-12 19:51
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
  - 分析報表
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
intents:
  - 查看 Google 購物廣告成效
  - 分析廣告 ROAS 與轉換數據
features:
  - 廣告分析
  - Google 購物廣告成效
  - 廣告數據總覽
  - 每日趨勢圖
prerequisites:
  - 已開通「自動化廣告系統」並完成 Google 購物廣告開通
  - 已建立 Google Ads 自動化帳戶
devices:
  - desktop
  - mobile
apis: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/business-intelligence/ad-analytics-guide/"
comments: ""
search:
  exclude: false
icon: lucide/megaphone
hide:
---

![Advertising Analysis page](../../assets/images/ec-bi-advertising-analytics-hero.en.png){ title="Advertising Analysis Page" .hero-page }

## About Advertising Analysis { #intro-advertising-analytics }

"Advertising Analysis" turns the performance of the **Google Shopping ads** you run through the "Automated Advertising System" into data cards and a daily trend chart. From how much you spent and how many impressions and clicks you got, to how much order revenue came back, you can see it all on one page and decide whether your ads are worth it or need adjusting.

!!! path "Admin path: In the left menu of the admin, go to "Charts" > "Advertising Analysis.""

!!! info "Tip"
    This page currently shows only **Google Shopping ads** performance and does not include data from other ad channels.

## Prerequisites and Limitations { #prerequisites-advertising-analytics }

- [x] **["Automated Advertising System"](../integrations/google/automated-ads-system.md#operate-automated-ads-apply){ title="Apply for Activation and Make Your First Top-Up" } is activated**: "Advertising Analysis" appears in the left menu only after Google Shopping ads are activated.
- [x] **A [Google Ads automated account](../integrations/google/automated-ads-system.md#operate-automated-ads-gmc){ title="Choose a GMC Connection Method" } has been created**: If you have not created the account yet, the page shows the message "Google Ads automated account not created," and you cannot query data for now.

!!! plan "Activation Requirements"
    "Advertising Analysis" works with the "Automated Advertising System." You set it up under "Third-Party Integration" > "Automated Advertising System" in the admin. This page appears in the menu and loads data only after you activate Google Shopping ads and set up the account.

## Page Overview { #overview-advertising-analytics }

| Section | Contents | Purpose |
| :-- | :-- | :-- |
| Filter bar | [Date range](#operate-advertising-analytics-date-range), [device type](#operate-advertising-analytics-device) | Set the time range and devices to view |
| [Data Overview](#operate-advertising-analytics-overview) | 11 performance data cards | See totals and averages for each metric in the period at a glance |
| [Daily Trend Chart](#operate-advertising-analytics-trend) | Line chart with metric switching | See how a single metric changes day by day |

The data overview and the trend chart share the same 11 metrics. For full definitions, see [Advertising Analysis Metrics](references/advertising-analytics-metrics-reference.md#reference-advertising-analytics-metrics){ title="Advertising Analysis Metrics Reference" data-preview }.

## Steps { #operate-advertising-analytics }

### View the Ad Performance Overview { #operate-advertising-analytics-overview }

1. In the admin, go to "Charts" > "Advertising Analysis."
2. The "Google Shopping Ads Analysis" section at the top of the page shows 11 metrics for the selected period as data cards (Cost, Impressions, Clicks, ROAS, and more).
3. Hover next to the name of any card to see how the metric is calculated. For what each metric means, see [Metrics Reference](references/advertising-analytics-metrics-reference.md#reference-advertising-analytics-metrics){ title="Advertising Analysis Metrics Reference" data-preview }.

![View the ad performance overview](../../assets/images/ec-bi-ad-analytics-overview.zh-tw.en.png){ title="View the Ad Performance Overview" }

---

### Adjust the Query Date Range { #operate-advertising-analytics-date-range }

1. Click the **date range** picker in the upper-right corner.
2. Select the start and end dates you want to view[^date-limit].
3. The system automatically reloads the data cards and the daily trend chart for the new range.

[^date-limit]: A single query can cover up to 180 days. If you exceed this, the system shows a message. Shorten the range and query again.

![Adjust the query date range](../../assets/images/ec-bi-ad-analytics-date-range.zh-tw.en.png){ title="Adjust the Query Date Range" }

---

### Switch Device Type { #operate-advertising-analytics-device }

1. Click the **Device** drop-down menu above the data overview.
2. Select "All Devices," "Desktop," "Mobile," or "Tablet."
3. The data cards and trend chart recalculate right away for the selected device, so you can compare ad performance across devices.

![Switch device type](../../assets/images/ec-bi-ad-analytics-device.zh-tw.en.png){ title="Switch Device Type" }

---

### View the Daily Trend Chart { #operate-advertising-analytics-trend }

1. Scroll down to the **Daily Trend Chart** at the bottom of the page.
2. Click a metric tab above the chart to switch the metric you want to see. Choose "All Metrics" for an overview, or a single metric for details.
3. Hover over any point on a line to see the actual value for that date. Click an item name to hide or show its data.

![View the daily trend chart](../../assets/images/ec-bi-ad-analytics-trend.zh-tw.en.png){ title="View the Daily Trend Chart" }

## Important Rules and Limitations { #specs-advertising-analytics }

- A single query can cover up to 180 days.
- Data on this page covers only **Google Shopping ads**, not other ad channels.
- "Conversions" use 30-day post-click attribution, so conversion data may be incomplete when ads first start running or for the last few days.
- Data comes from Google Ads and is compiled daily. It may differ slightly from the Google Ads dashboard because of time zones and data sync timing.

## FAQ { #faq-advertising-analytics }

??? quote ""Advertising Analysis" is missing from the menu, or data won't load"
    [](){ #faq-advertising-analytics-not-available }
    "Advertising Analysis" works with the "Automated Advertising System." Check that:

    - Google Shopping ads are activated. The page appears in the menu only after activation.
    - A Google Ads automated account has been created. If you see the message "Google Ads automated account not created," first complete setup under "Third-Party Integration" > "Automated Advertising System."

??? quote "Why are conversions still 0 right after my ads started running?"
    [](){ #faq-advertising-analytics-no-conversion }
    "Conversions" count orders placed within 30 days after a customer clicks an ad. When ads first start running, customers may still be deciding and haven't ordered yet, so it takes some time for conversion data to appear.

??? quote "Can't query because the date range is too long?"
    [](){ #faq-advertising-analytics-date-range-limit }
    A single query can cover up to 180 days. To see trends over a longer period, query in segments.

??? quote "Data doesn't match the Google Ads dashboard?"
    [](){ #faq-advertising-analytics-data-diff }
    Data on this page comes from Google Ads and is compiled daily. Because of time zone calculations and data sync delays, numbers may differ slightly from the Google Ads dashboard in the short term. They will match once the data syncs.

## References { #reference-advertising-analytics }

- [Advertising Analysis Metrics](references/advertising-analytics-metrics-reference.md)
