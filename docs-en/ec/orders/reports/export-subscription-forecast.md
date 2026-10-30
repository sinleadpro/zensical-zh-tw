---
title: "Export the Subscription Sub-Order Forecast Report"
description: "Export the subscription sub-order forecast report to check orders expected to ship and forecast how much stock to prepare."
created: "2026-03-16 00:15"
last_modified: 2026-09-29 18:00
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
  - 訂單
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
  - 匯出定期訂單
  - 子訂單預測
  - 備貨預測
features:
  - 定期定額子訂單匯出
  - Excel 匯出
  - 預測報表
prerequisites: []
related: []
tags:
  - Subscriptions
  - Sub-Orders
  - Forecast
  - Reports
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 定期定額訂單
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=6794
permalink: "https://help.cyberbiz.io/ec/orders/reports/export-subscription-forecast/"
comments: false
search:
  exclude: false
icon: lucide/calendar-clock
hide: []
---

![Subscription orders](../../../assets/images/ec-訂單-定期定額訂單.en.png){ title="Subscription Orders" .hero-page }

## About Exporting the Subscription Sub-Order Report

You can export the **sub-order report for subscription orders**, which helps you check orders expected to ship and forecast how much stock to prepare.

## Feature Overview

*   **Purpose**: Mainly used to check data for orders that will ship.
*   **Forecast data**: The system exports, for all subscription orders, **the next 3 sub-orders expected to be created** (projected data for orders not yet created).
*   **File format**: Excel report.

## Steps

1.  **Go to the page**: Sign in to the CYBERBIZ admin and click **Orders > Subscription Orders** in the left menu.
2.  **Export**: Click **Export Subscription Orders** on the page.
3.  **Get the report**: When the export finishes, the system automatically sends the Excel file to **the email of the admin currently signed in**. Check your inbox and download it.

![Export subscription orders](../../../assets/images/ec-訂單-定期定額訂單-匯出定期訂單.en.png){ title="Export Subscription Orders" }

## Report Fields

The downloaded report includes the following fields for detailed checking:

*   **Dates and cycles**: Expected ship date, subscription order number (parent order number), subscription cycle, and cumulative actual deliveries.
*   **Buyer information**: Buyer name, email, and phone.
*   **Recipient information**: Recipient name, phone, and shipping address.
*   **Product details**: Product name, SKU, quantity, and total.
*   **Other information**: Payment method, additional information, notes, subscription order admin notes, and whether the order was placed on behalf of the customer.

![Subscription sub-order report](../../../assets/images/ec-訂單-定期定額訂單-子訂單報表.en.png){ title="Subscription Sub-Order Report" }

## FAQ

??? quote "Why does my exported report show only 3 sub-orders?"
    To keep system performance and forecasts accurate, the system currently exports only the next 3 sub-orders "expected" for each parent order. If the subscription is close to its last cycle, it shows the actual number of remaining cycles.

??? quote "Do I export sub-orders that have already been created here too?"
    No. This feature is mainly for forecasting future stock. To look up sub-orders that have been created (with actual order numbers), go to Orders > All Orders and use the Subscription Orders filter to search and export.

??? quote "What if I don't receive the email after clicking Export?"
    Check the following first:

    * Check your spam folder: The mail server might have flagged the email as an ad.
    * Check the admin account: The report is sent to the email of the account currently signed in to the admin. Make sure that inbox works.
    * Wait a while: For large amounts of data, processing takes 3–5 minutes. Check again later.
