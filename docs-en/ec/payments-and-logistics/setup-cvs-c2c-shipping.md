---
title: "Set up CVS Store-to-Store C2C Logistics Integration"
description: "Enable the CVS store-to-store (C2C) logistics service so customers can choose a convenience store for pickup at checkout."
created:
last_modified: 2026-06-30 08:52
lang: en-US
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/setup-cvs-c2c-shipping/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents:
  - 設定超商物流串接
  - 開啟超商免運
  - 設定取貨不付款
features:
  - 超商店到店 C2C
  - 7-ELEVEN 交貨便
  - 全家店到店
  - 萊爾富超商取貨
prerequisites: []
related:
  - ec/payments-and-logistics/apply-cyberbiz-payments/
  - ec/orders/cvs-shipping/cvs-c2c-shipping/
  - ec/products/shipping/cvs-shipping-restrictions-exclusions/
tags:
  - CVS_Logistics
  - C2C
  - CVS_Pickup
  - Logistics_Integration
  - 7-11
  - FamilyMart
  - Hi-Life
acoiv:
apis:
  - 7-ELEVEN 交貨便
  - 全家店到店
  - 萊爾富超商取貨
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 超商物流
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5058
  - https://www.cyberbiz.io/helpcenter/?p=6850
  - https://www.cyberbiz.io/support/?p=5958
comments: false
search:
  exclude: false
icon: lucide/store
hide:
---

![CVS Shipping C2C](../../assets/images/ec-金物流-超商物流.en.png){ title="CVS Shipping C2C" .hero-page }

## Convenience Store Store-to-Store Shipping (C2C) Overview { #intro-cvs-c2c }

**CVS store-to-store (C2C)** is a shipping method in which the merchant packs the product and drops it off at a nearby convenience store. The package is then delivered to the store the customer selects for pickup.

!!! example "Use Cases"

    - Small or lightweight products
    - Merchants drop off shipments at a convenience store themselves.
    - Shipping scenarios that do not require a logistics provider to pick up from the merchant's location

!!! info "This service applies to the shipping model in which merchants drop off shipments at a convenience store themselves. If you use a logistics provider for home pickup, use a different shipping option."

### Supported Logistics Services { #intro-cvs-c2c-services }

CYBERBIZ currently supports the following convenience store store-to-store logistics services:

- [x] **7-ELEVEN 交貨便**
- [x] **FamilyMart Store-to-Store**
- [x] **Hi-Life Store Pickup**
- [x] **Black Cat Quick Store Pickup** (provides convenience store pickup, not traditional home delivery)

## Setup Steps { #operate-cvs-c2c }

### Step 1: Select a Logistics Service { #operate-cvs-c2c-select }

1. Log in to the **CYBERBIZ Admin Panel** and go to **Payment and Logistics > Convenience Store Logistics**.
2. Find the logistics service you want to enable, and click the edit button :material-file-document-edit-outline: to open its setup page.

![Select Logistics Service](../../assets/images/ec-logistics-cvs-c2c-select-service.en.png)

---

### Step 2: Fill In Basic Information { #operate-cvs-c2c-basic }

1. **Agree to the terms of service**: Select **I have read the logistics integration provider terms** before you can use the service.

2. **Company sender information**: Fill in the **sender name** and **mobile number**. Make sure they are accurate.

    !!! warning "If a customer requests a return, store staff will use the sender's **ID card information** to verify identity. Make sure it is entered correctly."

1. **Additional settings (enable as needed)**

    - **Free shipping settings**: Choose whether to offer free convenience store shipping.
    -  **No payment at pickup***: Customers do not need to pay when they pick up the order (online payment must be completed first).

	!!! info "CYBERBIZ PAYMENTS exclusive feature: COD (cash on delivery)"
	    - Only merchants who have activated **CYBERBIZ PAYMENTS** can use the cash on delivery feature.
	    - If not activated, the storefront only shows the "No payment at pickup" option.
	    - [Activate CYBERBIZ PAYMENTS](apply-cyberbiz-payments.md){ title="Apply for CYBERBIZ PAYMENTS" } to use this feature.

![CVS Logistics Settings](../../assets/images/ec-金物流-超商物流-設定.en.png){ title="CVS Logistics Settings" }


## How the Storefront Displays Convenience Store Pickup Options { #specs-cvs-c2c-storefront }

The following example uses **Hi-Life Store Pickup** to show what customers see when they select convenience store pickup at checkout:

![Storefront CVS Pickup Display](../../assets/images/ec-金物流-超商物流-萊爾富前台顯示.en.png){ title="Storefront CVS Pickup Display" }


## Next Steps { #next-steps-cvs-c2c }

<div class="grid cards" markdown>

- :lucide-package:{ .lg }   
  [__Ship Convenience Store Store-to-Store C2C Orders__](../orders/cvs-shipping/cvs-c2c-shipping.md){ title="Ship CVS Store-to-Store C2C Orders" }     
  After you create an order, go to the order management page to generate a shipping label and complete the convenience store shipping process.

- :lucide-ban:{ .lg }     
  [__Set Convenience Store Delivery Restrictions__](../products/shipping/cvs-shipping-restrictions-exclusions.md){ title="Set CVS Delivery Restrictions and Exclusions" }  
  Set product volume, weight, or type so the system automatically excludes products that are not eligible for convenience store delivery.

</div>
