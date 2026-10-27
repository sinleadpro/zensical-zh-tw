---
title: "Import Customer Store Recommenders"
description: "Headquarters admins can use bulk import to quickly link existing members to specific stores and staff, so sales are attributed accurately."
created: 2026-05-07 18:35
last_modified: 2026-06-18 18:35
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
  - APP MARKET
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
  - 批量綁定門市推薦人
  - 更換會員推薦人
  - 批次刪除綁定關係
features:
  - 門市助理
  - "Bulk Import"
  - "Referrer Linking"
  - "Sales Attribution"
prerequisites: []
related: []
tags:
  - 門市助理
  - 批量匯入
  - 推薦人綁定
  - 業績歸因
acoiv: configure
apis: []
devices: []
ui_components:
  - 匯入
  - 上傳檔案
  - 錯誤明細
paths:
  - 門市助理後台 > 門市管理 > 匯入 > 顧客門市推薦人
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=3865
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/bulk-import-customer-referrers/"
comments: false
search:
  exclude: false
icon: lucide/file-up
hide: []
---

# Import Customer Store Recommenders
Headquarters admins can use bulk import to quickly link existing members to specific stores and staff, so sales are attributed accurately.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }


## Overview { #overview-referrer-import }

Headquarters admins can use this feature to configure member and store referrer settings in bulk, including **changing the store referrer**, the **binding period**, and **removing the binding**.


## Before You Start { #prerequisites-referrer-import }

-  **Member Requirement**: You can only link members who have **already registered on your online store (EC)**. If a customer is not yet a member, go to **Customer Management > All Customers** and [import member data]() first.
-  **LINE Official Account Connection**: Members linked in bulk from the admin are **not** added as LINE Official Account friends automatically. We recommend asking these members to scan the staff member's QR code in store later to complete the LINE connection.
-  **Sales Calculation**: Orders from members with an imported customer store recommender appear in the **Sales Attribution Report**.
- **Permissions**: Only **headquarters admins** can use this feature in the Store Assistant admin.


## Setup Steps { #operate-referrer-import }

### Upload and Run the Import { #operate-referrer-import-upload-import }

1. Log in to the Store Assistant admin, go to **Store Management**, and click **匯入 > 顧客門市推薦人** in the top menu.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人01.png){ .screenshot }

2. Click **Download Template** and fill in the member's mobile number, store ID, staff ID, and other information in the template format.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人02.png){ .screenshot }

    !!! info "Limits"
        - Only `.xlsx` files are supported.
        - You can upload up to **3,000 records** at a time.
        - You must use the latest template provided by the system.

3. Click **Upload File** and select the completed `.xlsx` file.
4. The system starts the import. Check the status in real time in the **Upload Progress** section below.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人03.png){ .screenshot }

### Check Progress and Fix Errors { #operate-referrer-import-errors }

1. **Completed**: When the status shows **Completed**, the links take effect immediately.
2. **Error Handling**:
    - If the status shows **Failed** or **Partially Succeeded**, click **Error Details** on the right.
    - Fix the original file based on the messages (such as format errors, member not found, or store ID does not exist).
    - **After fixing, upload the whole file again**. No data is updated until the upload completes successfully.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-匯入顧客門市推薦人04.png){ .small-image }


## FAQ { #faq-referrer-import }

??? quote "After importing, are older orders attributed to the newly linked referrer automatically?"
    No. Sales attribution applies only to valid online store orders placed **after the link is created**. Closed or existing past orders are not attributed retroactively.

??? quote "Can I also use import to remove a member's link?"
    Yes. In the import template, use the specific command field (see the template instructions) to delete or remove the link, then upload again to update in bulk.

