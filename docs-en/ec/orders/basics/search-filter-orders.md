---
title: "How to Search and Filter Orders"
description: "Use keyword search, filters, view groups, and order tags to quickly find the orders you need."
created: 2026-05-07 11:23
last_modified: 2026-07-13 09:53
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 訂單
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
  - 搜尋訂單
  - 篩選訂單
  - 管理訂單
features:
  - 關鍵字搜尋
  - 條件篩選
  - 訂單檢視群組
  - 訂單標籤
  - 編輯列表欄位
  - 適應寬度
prerequisites: []
related:
  - ec/orders/references/order-filter-status-reference/
  - ec/orders/references/payment-statuses/
  - ec/orders/references/fulfillment-statuses/
  - ec/orders/references/shipping-methods/
  - ec/orders/references/order-list-columns/
  - ec/orders/reports/export-subscription-forecast/
  - pos/orders/manage-general-orders/
  - ec/members/manage-member-profiles/
  - ec/orders/basics/order-fulfillment-flow/
  - ec/orders/basics/edit-order-content/
  - ec/orders/reports/export-order-report/
tags:
  - "Order Search"
  - "Order Filters"
  - "Order Management"
  - "Order Tags"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=622
permalink: "https://help.cyberbiz.io/ec/orders/basics/search-filter-orders/"
comments: false
search:
  exclude: false
icon: lucide/search
hide: []
---


![Search and filter orders](../../../assets/images/EC-訂單-所有定單-搜尋與篩選-hero.en.png){ title="Search and Filter Orders" .hero-page }


## About Order Search and Filters

**"Order search and filters"** are on the order management page in the admin. They help you quickly find orders among many and improve efficiency with custom views.

## Open Order Management { #orders-path }

Sign in to the CYBERBIZ admin and click **"Orders"** > **"All Orders"** in the left menu.

![Open All Orders](../../../assets/images/EC-所有訂單-路徑.en.png){ title="Open All Orders" }

## Keyword Search { #orders-search }

The search field supports many kinds of keywords, but note the [matching rules](../references/order-filter-status-reference.md#orders-match-mode){ title="Order Filters and Statuses Reference" data-preview }:

=== "New Order List"

    1. **Enter keywords**: Enter search terms (such as order number, name, or mobile number) in the search box and press ++enter++.
    2. **View results**: Matching orders appear in the list immediately.
    3. **Change rows per page**: Use the drop-down below the list to change rows per page (10 / 25 / 50 / 100 / 200).

    ![Order list: search](../../../assets/images/EC-所有訂單-搜尋操作.en.png){ title="Order List: Search" }

=== "Legacy Order List"

    1. **Enter keywords**: Enter search terms in the search box and press ++enter++.
    2. **View results**: Matching orders appear in the list below.
    3. **Change rows per page**: Use the drop-down in the **upper-right corner** of the list to change how many orders are shown per page.

    ![Order list: search (legacy)](../../../assets/images/EC-所有訂單-搜尋操作-舊版.en.png){ title="Order List: Search (Legacy)" }

## Filters { #orders-filter }

You can stack multiple filters and combine them with [keyword search](#orders-search) to narrow results further.

=== "New Order List"

    Filters are **stackable** and added with **"+ Add Filter."**  

    1.  **Add Filter**: Click **"+ Add Filter"** above the list and choose the [field to apply](../references/order-filter-status-reference.md#orders-v2-filters){ title="Order Filters and Statuses Reference" data-preview } from the drop-down. Added filters appear as tags.

        ![Order list: filter tags](../../../assets/images/EC-所有訂單-已新增篩選條件.en.png){ title="Order List: Filter Tags" }

    2.  **Set filter values**: Click a filter tag to open its drop-down and select one or more values. Multiple values in the same filter match "any of them."

        ![Order list: set filter values](../../../assets/images/EC-所有訂單-篩選條件值設定.en.png){ title="Order List: Set Filter Values" }

    3.  **Set a date range**: **Order date** and **order delivery date** support two modes:  

        - **Between**: Set specific start and end dates  
        - **Past**: Set a rolling range of "the past N days" (good for saving as a view group)

        ![Order list: date filter (between)](../../../assets/images/EC-所有訂單-篩選時區-介於.en.png){ title="Order List: Date Filter (Between)" .screenshot }  

    4.  **Clear filters**: To remove one filter, click the ✕ next to its tag. To clear all filters, click **"Clear All"**.  
    5.  **Save the filter results**: If you use this filter combination often, click "Save" to create an [order view group](#orders-groups-tabs) and switch to it with one click later.


    ??? plan "Filter Availability"
          If you don't see one of the filters below, your plan doesn't support it or the feature isn't turned on, and it won't appear in **"+ Add Filter"** either:  

          | Filter | Requires |
          | :-- | :-- |  
          | Online / offline store (filter by POS store) | POS system |
          | Delivery method (including store pickup options) | Store pickup |  
          | Product channel | Product channel settings |  
          | Delivery temperature zone | Product temperature zone binding |  
          | Return status (some options) | Logistics system |  
          | LINE group buy | LINE group buy |  
          | Merchant source / payee | Enterprise / PLUS plan, or "own payment gateway" not turned on |

=== "Legacy Order List"

    Filters are **fixed drop-down menus**, and each filter allows only one value. Orders must match all the filters.

    1.  **Status filters**: Four drop-down menus: "[Payment Status](../references/payment-statuses.md#payment-statuses){ title="Order Payment Status Reference" data-preview }," "[Delivery Status](../references/fulfillment-statuses.md#fulfillment-statuses-table){ title="Delivery Status Reference" data-preview }," "[Return Status](../references/order-filter-status-reference.md#orders-return-status){ title="Order Filters and Statuses Reference" data-preview }," and "[Order Status](../references/order-filter-status-reference.md#orders-status){ title="Order Filters and Statuses Reference" data-preview }."  

        ![Order filters (legacy)](../../../assets/images/EC-所有訂單-篩選條件-舊版.en.png){ title="Order Filters (Legacy)" }  

    2.  **Date filter**: Set a start and end range by **"order date."**

        ![Order date filter (legacy)](../../../assets/images/EC-所有訂單-篩選時間-舊版.en.png){ title="Order Date Filter (Legacy)" }  

        !!! info "If the POS system is turned on, an additional **"Confirmation Time"** filter appears so you can find POS orders by when staff checked out or confirmed them."
    1.  **Source and delivery filters**: Depending on the features you have, these filters may appear:

        - **"[Order Source](../references/order-filter-status-reference.md#orders-store){ title="Order Filters and Statuses Reference" data-preview }"**: Switch between the main EC site and each POS store  
        - **"[Delivery Method](../references/shipping-methods.md#shipping-methods){ title="Shipping Methods Reference" data-preview }"**: Filter by store pickup, convenience store, home delivery, and other channels  
        - **"[Order Type](../references/order-filter-status-reference.md#orders-line-group-buy){ title="Order Filters and Statuses Reference" data-preview }"**: Find LINE group buy orders on their own  
        - **"[Merchant Source/Payee](../references/order-filter-status-reference.md#orders-merchant-from){ title="Order Filters and Statuses Reference" data-preview }"**: Filter by payment payee  
        - **"[Warehouse Type](../references/order-filter-status-reference.md#orders-warehouse-type){ title="Order Filters and Statuses Reference" data-preview }"**: Stores with multiple warehouses can switch by shipping warehouse

    2.  **Advanced Search** (requires the "Advanced Order Search" feature): Above the search box, you'll see  

        - **Search type drop-down**: Search only in specific fields, such as order number, customer email, or product SKU  
        - **"Exact match" checkbox**: Select it for exact matching; fuzzy matching is the default  

### How Filters Combine { #orders-filter-logic }  

| Scenario | Logic | Example |
|---|---|---|
| **Multiple values in one filter** | Any value matches | Order status `In Progress` + `Completed` > <br> orders in both statuses appear |
| **Different filters combined** | All conditions must match | Payment status = `Payment Received` + delivery status = `Unshipped` > <br> only paid orders not yet shipped |
| **Keyword search + filters** | Narrows by filters first, then matches keywords | Filter `Unshipped`, then search `0912` > <br> mobile numbers are matched only in unshipped orders |

??? example "Common Combination Examples"  
    - **Find orders to ship today** → delivery status = `Unshipped` + order date = `Past 7 days`
    - **Find disputed orders pending refund** → payment status = `Pending Refund` + `Customer Service Processing`  
    - **A store's sales for the month** → order source = `A POS store` + order date = `Between 2026/05/01 ~ 05/31`  
    - **Shipping exceptions for frozen products** → delivery temperature zone = `Frozen` + delivery status = `Shipping Exception`

??? tip "Faster Filtering"

    With large amounts of data, set a **date range** first (such as the last 7 days) to narrow results, then add filters such as **Payment Status** and **Delivery Status** for faster searches.



## Order View Groups { #orders-groups-tabs }

"View groups" save complex [filter](../references/order-filter-status-reference.md#orders-v2-filters){ title="Order Filters and Statuses Reference" data-preview } combinations (such as specific carrier + paid + unshipped) as shortcut tabs at the top of the page, so you can switch with one click and process orders in bulk more efficiently.

**Steps**

1. **[Set filters](#orders-filter)**: Click "+ Add Filter" and select the fields and values to combine.
2. **Click Save**: When you're done, click Save on the right of the search bar.
3. **Choose how to save**: In the dialog, choose:
    - **Create New Group**: Enter a new name (such as "To Ship Today"). A new tab is created.
    - **Update Group**: Overwrite an existing tab with the current filters (appears only when you're adjusting an existing group).

    ![Order list: save order view group](../../../assets/images/EC-所有訂單-儲存訂單檢視群組.en.png){ title="Order List: Save Order View Group" }

4. **Manage tabs**: Hover over a custom tab and click the :lucide-chevron-down: icon next to its name to delete it.
5. **Search and jump**: If you have many groups, click "More View Groups" at the end of the tabs:
    - **Keyword search**: Enter a name in the drop-down search box to find a specific group.
    - **Jump with one click**: Click a search result to switch to that group's order list.

    ![Order list: more view groups](../../../assets/images/EC-訂單-所有訂單-更多檢視群組.en.png){ title="Order List: More View Groups" }

??? example "Common View Group Examples"

    | View Group Name | Suggested Filters |
    | :--- | :--- |
    | **Orders to ship** | **Delivery Status**: `Unshipped`, `Preparing`<br>**Payment Status**: `Cash on Delivery`, `Payment Received` |
    | **Specific carrier orders** | **Delivery method**: Select specific carriers (such as EZCAT or FamilyMart) |
    | **Returns in progress** | **Order Status**: `In Progress`<br>**Return Status**: `Return Requested`, `Returning`, `Reviewing Return` |

## Edit List Columns { #orders-edit-columns }

Depending on your needs, you can [choose which columns to show](#orders-columns-configure), change their order, or switch to [fit-to-width](#orders-list-adjust-width) mode when there are too many columns, so the table fits on the screen.

### Choose and Order Columns { #orders-columns-configure }

1. **Open the settings**: Click **Edit Columns** in the upper right of the list, and a settings panel opens on the right.
2. **Select columns**: Select the [columns](../references/order-list-columns.md#orders-columns){ title="Order List Columns Reference" data-preview } to show in the panel; clear one to hide it from the list.  
    - The **Order Number** column is the main identifier and is always shown.
    - Click **Select All / Clear All** at the bottom of the panel to toggle all columns at once.  
3. **Change the order**: Press and hold the :lucide-grip-vertical: icon on the left of a column and drag it up or down to change its left-to-right position in the list.  
4. **Save or reset**:  
    - Click **Save** to apply the changes, and the list updates immediately.  
    - Click **Reset** to restore the default layout.  
    - If you close the panel without saving, all changes are discarded.

![Order list: edit columns](../../../assets/images/EC-訂單-所有訂單-編輯欄位.en.gif){ title="Order List: Edit Columns" }

!!! tip "Track Subscriptions"
    If you sell subscriptions, turn on the **Recurring Order Number** and **Preorder Number** columns to quickly see which plan and period each sub-order belongs to.  

---

### Switch to Fit-to-Width { #orders-list-adjust-width }

When you show many columns and the list scrolls horizontally, use **Compact** to fit all columns on one screen.

1. Click :lucide-unfold-horizontal: **Compact** in the upper right of the list.  
2. Headers turn **vertical** and columns narrow automatically, so you can see the whole table without scrolling horizontally.  
3. Click the button again (now shown as **Default**) to restore the default width.  

![Order list: fit to width](../../../assets/images/EC-訂單-所有訂單-適應寬度.en.png){ title="Order List: Fit to Width" }

!!! tip "Compare Multiple Columns Quickly"  
    When you need to compare several status columns (such as "Payment Status," "Delivery Status," "Return Status," and "Invoice Status" together), fit-to-width avoids horizontal scrolling and speeds up review.

## Order Tags { #orders-tag-annotation }

"Order tags" are labels you add to orders **manually** to record internal information system statuses can't express, such as "Handwritten card needed," "VIP customer," or "Awaiting customer service reply." You can use tags as filters in the order list and save common combinations with [view groups](#orders-groups-tabs).

!!! example "When to Use Tags"

    * **Process notes**: Mark the order's current processing stage, such as "Confirmed by phone" or "Waiting for documents."
    * **Customer traits**: Mark the customer type, such as "Business customer," "Regular," or "Watch list."  
    * **Campaign**: Mark the marketing campaign or channel the order belongs to, such as "Double 11 sale" or "Department store pop-up."  
    * **Internal assignment**: Mark the responsible staff member or department so each role can quickly find their orders.  

**How to Use**

1. In the **Orders** > **All Orders** list, select the orders to tag (one or more).
2. Click **Actions...** > **Add Tags** above the list to open the tag settings dialog.  
3. In the input box:
    * Select an **existing tag** from the drop-down; or  
    * Enter a new name and click **Add** to create and apply a new tag.  
4. Confirm and submit, and the selected tags are added to all selected orders.  

To remove tags, go to **Actions...**, select **Remove Tags**, and choose the tags to remove in the dialog.  

![All orders: tag settings](../../../assets/images/EC-訂單-所有訂單-更多操作-訂單標籤設定.en.png){ title="All Orders: Tag Settings" }

## Other Search Paths

<div class="grid cards" markdown>

<!-- - :lucide-repeat:{ .lg } [__Subscription Orders__](../reports/export-subscription-forecast.md){ title="Export the Subscription Sub-Order Forecast Report" }   -->

- :material-point-of-sale:{ .lg } [__POS Orders__](../../../pos/orders/manage-general-orders.md#查詢訂單){ title="Manage Regular Orders" }  

- :lucide-user:{ .lg } [__Member Search__](../../members/manage-member-profiles.md){ title="Manage Member Profiles" }  

</div>

## Next Steps

<div class="grid cards" markdown>

- :lucide-package:{ .lg }  
  [__Bulk Shipping__](order-fulfillment-flow.md){ title="Order Fulfillment Flow" }  
  Select multiple orders and choose the matching carrier (EZCAT, FamilyMart, 7-Eleven, Pelican Express, and more) in "Bulk Actions" at the top to ship.

- :lucide-edit:{ .lg }  
  [__Change Order Status__](edit-order-content.md){ title="Edit Order Content" }  
  Open an order to edit it, or close/reopen orders with bulk actions (requires the "Manual Orders" permission).

- :lucide-download:{ .lg }  
  [__Export Reports__](../reports/export-order-report.md){ title="Export Order Reports" }  
  Click "Export" in the upper right of the page to download the current results as an Excel/CSV file for accounting or customer service.

</div>

## FAQ

??? quote "Why can't I find an order by product name?"

    Possible reasons:

    1. The product name at the time of the order differs from what you entered (for example, it was renamed later). The system records the item name **at the time of the order**.
    2. The product is a "gift" or "add-on" and is set to be excluded from search.
    3. The order was deleted (not closed). The list shows only orders that haven't been deleted.

??? quote "How do I save a filter combination I use often?"

    Follow these steps:

    1. Set filters in the order list (such as payment status = paid + delivery status = unshipped).
    2. Click "Save" on the right of the search bar.
    3. Select "**Create New Group**" and enter a name (such as "To Ship Today") to create a tab.
    4. After that, click the tab to switch to the order list for that filter combination with one click.

??? quote "What if there are too many results or the search is slow?"

    Try these in order:

    1. Use a date range first (such as the last 7 days) to narrow results.
    2. Add payment/delivery status filters, such as only "Paid + Unshipped."

