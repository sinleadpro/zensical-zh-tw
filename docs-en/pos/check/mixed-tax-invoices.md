---
title: "Mixed-Tax Invoices"
description: "Learn how to set products as taxable or tax-exempt, and how to automatically calculate and issue mixed-tax invoices that include both taxable and tax-exempt items at POS checkout."
created: 2026-04-16 11:15
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 適用版本待確認
  - EC POS 綁連結決定位置
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 商品
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 開通混稅發票功能
  - 設定商品應稅免稅
  - POS 結帳開立混稅發票
features:
  - 混稅發票
  - 商品稅別設定
prerequisites:
related:
  - ec/products/bulk-operations/excel-import-products/
tags:
  - "POS Mixed-Tax Invoices"
  - "Tax-Exempt Products"
  - "Invoice Settings"
  - "Tax Type Management"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 商品稅別
  - 客服視窗
  - 所有商品
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=37151
  - https://www.cyberbiz.io/support/?p=37500
permalink: "https://help.cyberbiz.io/pos/check/mixed-tax-invoices/"
comments: false
search:
  exclude: false
icon: lucide/receipt-text
hide: []
---

# Mixed-Tax Invoices
Learn how to set products as taxable or tax-exempt and automatically calculate and issue mixed-tax invoices that include both taxable and tax-exempt items at checkout.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Mixed-business merchants**: Merchants that sell both standard taxable products (such as household goods) and tax-exempt products (such as agricultural products).
    - **Compliant invoicing**: Process products with different tax types on a single invoice. This complies with Taiwan's e-invoice regulations and simplifies checkout.
    - **Automatic shipping tax classification**: The system automatically classifies shipping fees as taxable items to ensure accurate mixed-tax calculations.


## Usage Notes { #prerequisites-mixed-tax-invoices }

- **Checkout channel restriction**: This document applies only to **POS checkout**.
- **Feature activation**: This feature requires contacting customer service to enable backend permissions.
- **Return and exchange restriction**: Mixed-tax orders do not support exchanges.

## Procedure { #operate-mixed-tax-invoices }

### Step 1: Request Activation of Mixed-Tax Invoicing { #operate-mixed-tax-invoices-step-a-tax }

Before you set up products, contact the CYBERBIZ customer service team to enable the mixed-tax module.

1. Log in to the CYBERBIZ admin dashboard.
2. Click the **Customer Service Window** icon in the bottom-right corner of the screen.
3. Send a message to customer service to request activation of the POS mixed-tax invoice feature.

![](../../assets/images/EC-後台-總覽-前往線上客服01.en.png){ .screenshot }


### Step 2: Set Product Tax Types { #operate-mixed-tax-invoices-step-b-settings }

Set the taxable or tax-exempt status for products with different attributes.

1. Go to **Products > All Products**.
2. Click the product you want to configure to open its edit page.
3. In the product information, find the **Settings** section.
4. In the **Product Tax Type** field, select **Taxable** or **Tax-free** from the dropdown.
5. Click **Save** to complete the setup.

![](../../assets/images/EC-後台-商品-所有商品-設定應稅免稅01.en.png){ .screenshot }

!!! tip "Bulk Setup Tip"
    To set up multiple products, you can [export](../../ec/products/bulk-operations/excel-import-products.md#operate-excel-import-download) products, edit the **Product Tax Type** field in the Excel file, and then run an [import](../../ec/products/bulk-operations/excel-import-products.md#operate-excel-import-upload) to edit them in bulk.

## Calculation Logic { #specs-mixed-tax-invoices }

After the mixed-tax feature is enabled, the system processes invoices and discounts based on the following logic:

- **Invoice details**: The invoice lists **taxable sales** and **tax-exempt sales** separately.
- **Discount proportional allocation**: Discount amounts from marketing campaigns are automatically split into **taxable discounts** and **tax-exempt discounts** based on each product's share of the original amount.
- **Combined issuance**: The system issues only **one** mixed-tax invoice and does not issue separate tax-exempt and taxable invoices.
- **Shipping handling**: The system always classifies shipping fees as **taxable items**. Even if every product in an order is tax-exempt, the invoice is issued as a mixed-tax invoice when shipping fees apply.

    <div class="grid cards borderless two-columns" markdown>

    - ![Issue a taxable invoice](../../assets/images/發票-混稅發票01.en.png){ .small-image title="Issue a taxable invoice" }
    - ![Issue a mixed-tax invoice](../../assets/images/發票-混稅發票02.en.png){ .small-image title="Issue a mixed-tax invoice" }

    </div>

## Frequently Asked Questions { #faq-mixed-tax-invoices }

??? quote "How do I handle returns or allowances?"
    The return and allowance process for mixed-tax invoices is the same as for standard invoices. The system automatically processes the corresponding amounts based on the pricing, taxable discount, and tax-exempt discount fields on the original invoice. Merchants only need to follow the standard allowance process.


