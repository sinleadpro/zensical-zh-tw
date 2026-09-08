---
title: "Export Profit Sharing Report"
description: "With the revenue sharing report, you can accurately calculate the performance and revenue sharing amount for various promotional targets. The system provides a formal report 'after project closure' as well as a real-time order overview 'before project closure'."
created: 2026-02-06 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 行銷活動
sites:
  - TW
audiences:
  - admin
difficulty: beginner
tnb: branch
plans:
  - Advanced
  - Expert
  - "Professional Plus"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 匯出分潤報表
  - 查詢分潤明細
  - 設定第三方查詢連結
features:
  - "Profit Sharing Report"
  - 分潤查詢
prerequisites: []
related: []
tags:
  - 分潤報表
  - "Bonus Settlement"
  - "Performance Inquiry"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 分潤 > 分潤報表
  - 分潤 > 分潤查詢
  - 訂單 > 訂單報表匯出
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=579
  - https://www.cyberbiz.io/helpcenter/?p=597
  - https://www.cyberbiz.io/helpcenter/?p=608
  - https://www.cyberbiz.io/support/?p=1833
  - https://www.cyberbiz.io/support/?p=1864
  - https://www.cyberbiz.io/support/?p=39234
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/file-up
hide: []
---
#  Export Profit Sharing Report

allows you to accurately calculate the performance and profit sharing amount for various promotional targets. The system provides a formal report "after project closure" and a real-time order overview "before project closure".
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | Brand Official Website / Smart POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Advanced / Expert / All PLUS / Enterprise
{ .doc-badge }


!!! tip " Application Scenarios "
	-  **Monthly Reconciliation and Settlement**: At the beginning of each month, a summary of the **closed cases** from the previous month is remitted for bonus distribution.
	-  **Third-Party Performance Tracking**: Provides a dedicated link to influencers or group leaders, allowing them to instantly view promotional order details.
	- **Real-time Performance Monitoring**: Before order completion, use order reports to anticipate potential profit-sharing expenses.


## Instructions For Use
**Permission Differences:** **Website Owner:** Can query profit-sharing data for all users on the site. **Collaborative Manager (Employee):** Can only query their own profit-sharing performance. **


**## Operating Procedures

### Task 1: Export The Official Profit Sharing Report

is applicable to the settlement of all profit-sharing schemes, including "referral, registration, checkout, and pickup".

1.  Log in to the CYBERBIZ management backend and go to **Profit Sharing > Referral Reports**.
2.  Select the desired report type from the **Report Type** dropdown menu.
3.  Select the specific report name:
    -  **Referral Profit Sharing**: You can choose **Referral Profit Sharing Summary Report** or **Individual Referral Profit Sharing Report**.
    -  **Registration Profit Sharing**: You can choose **Registration Profit Sharing Summary Report** or **Employee Registration Profit Sharing Report**.

    !!! note " Report Content Analysis "
        -  **Profit Sharing Summary Report**: Presents the total referral profit sharing amount for each of **all partners** within a specific month. Suitable for monthly financial settlement and large-scale data verification.
        -  **Individual Referral Profit Sharing Report/Employee Registration Profit Sharing Report**: Presents a list of all referral order details and profit sharing amounts for a **single partner** within a specific month. Suitable for providing partners with details of their earnings for each order.

    -  **Settlement Person/Pickup Profit Sharing**: Directly select the corresponding summary report or individual report.

4.  Select the **month** to be remitted.
5.  Set the **recipient's Email** and select **Remit Report**. The

    >  system will process the background and send a download link to your email address.

!!! note " Settlement and Output Specifications "
    -  **Settlement Criteria**: Formal profit-sharing reports only include **closed** orders. If an order is placed at the end of December but closed in January, the data will appear in the January report.
    -  **Data Scope**: Reports are exported in **single month** units and cannot be exported across months.

![](../assets/images/EC-後台-分潤-分潤報表-畫面總覽01.png){ .screenshot }

### Task 2: Export Real-time Profit Sharing Information
To preview the **Referrer Revenue Sharing** status before order closure, you can use the order report function. Go to **Orders > Order Data Export**. In the **Available Report Fields**, check the following revenue sharing related fields: **Use Referrer Revenue Sharing**, **Revenue Sharing Name**, **Revenue Sharing Percentage**, **Revenue Sharing Amount**, **Referrer Code**, and filter the order status you want to query. After setting the time range and email, click **Export**.## Frequently Asked Questions

??? quote " The referrer reports that a certain order cannot be found. What should be done? "
    1.  Confirm whether the customer actually entered the referral code or clicked the referral link when placing the order.
    2.  Check whether the order was placed within the **effective period** of the plan.
    3.  If it is a third-party query link, please confirm whether the order has appeared in the **revenue sharing query** in the backend.



