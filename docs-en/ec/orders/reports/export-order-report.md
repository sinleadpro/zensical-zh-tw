---
title: "Export Order Reports"
description: "Export an order report as an Excel file sent to the admin's email, so you can look up and analyze order data."
created: "2026-03-13 23:45"
last_modified: 2026-08-05 11:20
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 匯出訂單
  - 訂單篩選
  - 訂單查詢
features:
  - 訂單報表匯出
  - Excel 匯出
  - 篩選功能
prerequisites: []
related:
  - ec/orders/references/order-report-fields/
  - pos/inventory/pos-reports-list-guide/
  - ec/products/shipping/cvs-shipping-restrictions-exclusions/
  - ec/profit-sharing/export-profit-sharing-reports/
  - ec/orders/reports/export-subscription-forecast/
  - ec/website-management/add-admin-set-permissions/
tags:
  - Orders
  - Export
  - Reports
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 訂單報表匯出
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1266
  - https://www.cyberbiz.io/support/?p=25244
permalink: "https://help.cyberbiz.io/ec/orders/reports/export-order-report/"
comments: false
search:
  exclude: false
icon: lucide/file-spreadsheet
hide: []
---

![Export order report](../../../assets/images/ec-訂單-訂單報表匯出.en.png){ title="Export Order Report" .hero-page }

## About Order Report Export

**"Export Order Report"** lets you review and analyze order details. The report is sent in Excel format to the admin email of the person exporting it.

## Where to Find It

Sign in to the CYBERBIZ admin and click **Orders > Order Data Export** in the left menu.

After you complete the settings below, the system exports the order report as an Excel file and sends it to your admin email.

## Steps

### Step 1: Select Report Fields

1.  **Select fields**: Click an item in "Available Fields" to add it to "Selected Fields" on the right; click it again to remove it.
2.  **Change the order**: Drag items in "Selected Fields" to change the order they appear in the report.
3.  **Advanced discount breakdown**: If you select the "Order Discount Breakdown" field, the report [shows each discount amount separately](../references/order-report-fields.md#訂單各項折扣拆分){ title="Order Report Fields" data-preview }, for example:

    - Mix-and-match product discount
    - VIP discount
    - Coupon discount
    - Bonus points discount
    - Manager price change (POS)

4. **Sales source**: Shows whether the order is a one-page store order.

    !!! info "One-Page Store Data Limits"

        * Compatibility: Only one-page stores created on or after 2025/07/02 are supported. For stores created before this date, the field can't show source information.
        * Data retention warning: If you "delete" the one-page store, the system can no longer show its source information. Before deleting a store, export the related reports to keep the order records.

5.  **Referral and UTM tracking**:

    *   [**Referral source**](../references/order-report-fields.md#導購來源){ title="Order Report Fields" data-preview }: Shows whether the order came from a referral platform such as LINE Shopping, Shop.com, or ShopBack.
    *   [**UTM parameters**](../references/order-report-fields.md#utm-參數){ title="Order Report Fields" data-preview } (Enterprise only): Export UTM source, medium, campaign name, and other data to track marketing performance (only for orders placed after 2025/12/17).

    !!! info "Each tool records UTM data and lookback periods differently. This feature uses data recorded by CYBERBIZ and may differ from GA4 or other tools."

6.  [**Bundle price difference**](../references/order-report-fields.md#組合品價差){ title="Order Report Fields" data-preview } (Enterprise only):

    - **Bundle price difference**: The total discount for a sub-product type in a bundle compared with selling it at its original single-item price (per product type).
    - **Bundle price difference details**: The discount actually allocated to each unit of that sub-product type (per unit).

![Export order report: select fields](../../../assets/images/ec-訂單-訂單報表匯出-選取欄位.en.gif){ title="Export Order Report: Select Fields" }

---

### Step 2: Filter the Export Range and Set Options

1.  **Filters**: Filter by order source, order status, payment status, delivery status, or return status.

    ![Export order report: filters](../../../assets/images/ec-訂單-訂單報表匯出-篩選項目.en.png){ title="Export Order Report: Filters" }

2. **Recipient email**: The email address the exported data is sent to.

    ![Export order report: recipient email](../../../assets/images/ec-訂單-訂單報表匯出-收信email.en.png){ title="Export Order Report: Recipient Email" }

    !!! info "Order Detail Export Limits"
        Because order details include sensitive personal data, the system doesn't offer direct downloads. After the report is generated, the system automatically sends it to the email of the account currently signed in, to keep the information secure.

3.  **How each order is shown**:
    *   **"Show Repeated" selected**: If an order has multiple products, it's split into multiple rows showing each product's subtotal.

        ![Export order report: show repeated selected](../../../assets/images/ec-訂單-訂單報表匯出-同筆訂單欄位重複顯示-勾選.en.png){ title="Export Order Report: Show Repeated Selected" }

    *   **"Show Repeated" not selected**: Each order is shown as a single row, and the amount is the order's total subtotal.

        ![Export order report: show repeated not selected](../../../assets/images/ec-訂單-訂單報表匯出-同筆訂單欄位重複顯示-未勾選.en.png){ title="Export Order Report: Show Repeated Not Selected" }

4. **Bundle breakdown**: Select "Show Bundle Information" to automatically expand the sub-product information inside "bundles" in the exported report.
5. **Date range**: Select the date range to export. New shortcuts are available, such as "Last 7 Days," "Last 30 Days," "This Month," and "Last Month."

    ![Export order report: date range](../../../assets/images/ec-訂單-訂單報表匯出-時間區間.en.png){ title="Export Order Report: Date Range" }

6.  **Export**: After confirming the settings, click the export button. The system sends the Excel report to **the email of the account currently signed in**.

## Reports for Other Scenarios

<div class="grid cards" markdown>

<!--
- :lucide-store:{ .lg }  
  [__POS Store Reports__](../../../pos/orders/pos-reports-list-guide.md){ title="POS Report List and Features" }  
  If you use the POS system, go to "POS Store List" > "Inventory Management" > "Reports" to download the "Order Summary Report" or "Daily Cash Report."

- :lucide-warehouse:{ .lg }  
  [__E-commerce Warehouse Reports__](../../products/shipping/cvs-shipping-restrictions-exclusions.md){ title="Set Up Convenience Store Delivery Restrictions and Logistics Exclusions" }  
  If you use Fengchao Logistics, go to "Orders" > "List" in the WMS admin and use "Export Report" with filters.
-->

- :lucide-hand-coins:{ .lg }  
  [__Commission Reports__](../../profit-sharing/export-profit-sharing-reports.md){ title="Export Referral Reports" }  
  If you set up referrer or employee commissions, go to "Commissions" > "Commission Reports" to export the summary or individual reports of completed referral commissions.

- :lucide-calendar-range:{ .lg }  
  [__Subscription Sub-Orders__](export-subscription-forecast.md){ title="Export the Subscription Sub-Order Forecast Report" }  
  Go to "Orders" > "Subscription Orders" to export the "Subscription Sub-Order Report" and check upcoming shipments.

</div>

## Important Notes

1.  **Check your inbox**: If you don't receive the report email, check your spam folder, or avoid HiNet email addresses, which have stricter blocking.
2.  **Export permissions**: The site owner can [restrict specific admins from "Order Export"](../../website-management/add-admin-set-permissions.md#權限分類與細節說明){ title="Add Website Admins and Set Permissions" } in "Site Permissions" to reduce security risks.

## FAQ

??? quote "Why didn't I receive the report email?"

    1. Check your "spam folder" first.
    2. Make sure the email of the account currently signed in is correct.
    3. If you use a company email, check whether your firewall blocks automated system emails from cyberbiz.io.

??? quote "Can I export orders from more than a year ago?"
    Yes. As long as the orders haven't been deleted, you can export them with a custom date range. Note that large amounts of data (over 10,000 orders) take longer to process.
