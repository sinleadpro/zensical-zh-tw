---
title: "Store Assistant Performance Reports"
description: "Learn about the Recommender Report and Sales Attribution Report in Store Assistant, and track offline member linking and omnichannel sales attribution data."
created: 2026-06-22 11:15
last_modified: 2026-06-22 11:15
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - "Store Assistant"
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: 
  - STORE PAL
intents: 
  - 查看門市業績報表
  - 分析店員綁定成效
  - 掌握全通路業績歸因
features: 
  - 門市助理
  - "Performance Reports"
  - "Sales Attribution"
  - 推薦人綁定
prerequisites:
  - ec/app-market/storepal/install-and-setup-storepal/
related: []
tags: 
  - 門市助理
  - 績效報表
  - 業績歸因
  - OMO
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 績效報表
  - 推薦人報表
  - 業績歸因報表
paths:
  - 績效報表 > 推薦人報表/業績報表
  - 門市管理 > 匯出報表
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=41036
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/performance-reports/"
comments: false
search:
  exclude: false
icon: lucide/bar-chart-3
hide: []
---
# Store Assistant Performance Reports
Learn about the Recommender Report and Sales Attribution Report in Store Assistant, and track offline member linking and omnichannel sales attribution data.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表01.png){ .hero-page }


## Overview { #overview-performance }

- Store Assistant provides the two performance reports below. Use them to review purchases by members collected through offline channels and the online sales they bring after leaving the store, and use the data to push messages, recommend products, and run promotions for these members.



## Recommender Report { #reference-performance }


Use the Recommender Report to see **linking status for each store** and **links between members and store staff**.


- **Referrer Linking Overview**: Shows the total linked members for all store staff, by store.
- **Linked Member Details**: Shows all members linked to each staff member.
    - Linked staff, name, mobile number, email, linking time, and linking type.
![Recommender Report](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表02.png)

> Report content varies slightly depending on the attribution level.


## Sales Attribution Report { #reference-attribution-report }


Use the Sales Attribution Report to see omnichannel sales performance after members are linked to referrers. The report contains four worksheets:


1. **Store Sales**

    Total sales for all staff in all stores, broken down into total online and offline sales, in-store sales, and total online store sales, with amounts and percentages.

    - **Total Official Website Sales** is divided into **Online Store Purchase Attribution** and **Recommended Product Attribution** to separate online referral performance.
        -  **Online Store Purchase Attribution**: Sales attributed to purchases members make on their own on the online store during the valid linking period.
        -  **Recommended Product Attribution**: Sales attributed to purchases made through recommended product links during the specified period.

    ![Sales Attribution Report - Store Sales](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表03.png)



2. **Personal Sales**

    Sales for each staff member, broken down into total online and offline sales, in-store sales, and total online store sales, with amounts and percentages.

    !!! warning "Data Display Limitation"
        This report shows data only when the sales attribution level is set to **Staff**. If the attribution level is set to Store, it has no data.


    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表04.png)



3. **EC Referral Report (Online)**

    Records of linked members' online purchases that can be validly attributed, listing the attribution level, attribution type, attributed to, purchasing member, order total, order number, and order date.


    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表05.png)



4. **EC Referral Report (Offline)**

    In-store purchases entered manually by staff, listing the operator, purchasing member, entry date, entered amount, and attribution level.

    !!! warning "Data Display Limitation"
        This report shows data only when the sales attribution level is set to **Staff**. If the attribution level is set to Store, it has no data.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表06.png)


## Store Reports { #reference-store-report }

### Role Permissions { #reference-store-report-role-permissions }

The data you can export depends on your role:

- Headquarters admins: Export all stores, or select specific groups or stores
- Group admins: Export all stores in their group, or select specific stores in their group
- Store managers: Export only their own store


### All Store Reports { #reference-store-report-store-report }

1. Log in to the Store Assistant admin and go to **績效報表 > 推薦人報表/業績報表**.
2. Select the report to export and click **Export**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表07.png)

3. Select a time range. If you select **Specific Store Group**, also select specific groups or stores.
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表08.png)



### Specific Store Reports { #reference-store-report-section }

1. Log in to the Store Assistant admin and go to **門市管理 > 匯出報表**.
2. Select the report to export and click **Export**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表09.png)

3. Select a time range.
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表10.png)