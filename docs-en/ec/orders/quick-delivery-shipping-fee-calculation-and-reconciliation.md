---
title: "Quick Delivery Shipping Fees and Reconciliation Rules"
description: "Explains how Quick Delivery shipping fees are calculated and the detailed rules for automatic reconciliation."
created: 2026-02-06 00:00
last_modified: 2026-07-15 14:20
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 以 CYBER 幣的方式收取；可在「CYBER 幣使用明細」查看->是否屬實
  - 不須儲值CYBER幣
  - 價格表
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
  - 金物流
  - 管理中心
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
plan_options: 
  - optional
cyb_extensions:
  - NOW!
intents:
  - 設定運費加價
  - 核對對帳單
features:
  - CYBERBIZ NOW
  - 運費計算
  - 自動對帳
prerequisites:
  - 已開通 CYBERBIZ NOW 快速到貨服務
related: []
tags:
  - "Shipping Fee Rules"
  - "Reconciliation Process"
  - Pandago
  - "Uber Direct"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 所有門市 > 快速到貨設定
  - 管理中心 > 網站權限
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=13847
permalink: "https://help.cyberbiz.io/ec/orders/quick-delivery-shipping-fee-calculation-and-reconciliation/"
comments: false
search:
  exclude: false
icon: lucide/calculator
hide: []
---
# Quick Delivery Shipping Fees and Reconciliation Rules

This article explains how Quick Delivery shipping fees are calculated and the detailed rules for automatic reconciliation.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }


!!! tip "Use Cases"
	- **Shipping cost planning**: Estimate Pandago and Uber Direct costs before you turn on the service.
	- **Promotion settings**: Set a free shipping threshold or a shipping surcharge for Quick Delivery to balance logistics costs.
	- **Financial reconciliation**: Each month, check CYBER Coin deduction details against actual shipping records.



## Before You Start

- **Distance rules**: The minimum unit is 1 km, and any part of a kilometer counts as a full kilometer (for example, 2.1 km counts as 3 km).
- **Fee changes**: Uber Direct fees vary with traffic, peak hours, and other factors. Go by the amount shown in the admin.
- **Special rates**: CYBERBIZ merchants get special program rates; the standard rates on the delivery platforms' official websites don't apply.
- **Changes**: Rates may change with partner programs. Go by what the admin shows or the latest announcement.


## Shipping Fee Calculation

Quick Delivery shipping fees have two parts: what you pay the platform and what customers pay you.

### 1. Shipping Fees You Pay the Platform (Cost)

#### Pandago

=== "Pricing"

    | Item | Distance Range | Rate |
    | :--- | :--- | :--- |
    | **Base fee** | 0–1 km | NT$85 |
    | **Additional per km** | Over 1 km | NT$10 per km |

=== "Distance Table"

    | Delivery Distance | Rate per Order |
    | :--- | :--- |
    | **0–1 km** | NT$85 per order |
    | **1–2 km** | NT$95 per order |
    | **2–3 km** | NT$105 per order |
    | **3–4 km** | NT$115 per order |
    | **4–5 km** | NT$125 per order |

#### Uber Direct


=== "Pricing"

    | Item | Distance Range | Rate |
    | :--- | :--- | :--- |
    | **Base fee** | - | NT$100 |
    | **First km surcharge** | 0–1 km | NT$5 for the first km |
    | **Additional per km** | 1.1–3 km | NT$10 per km |
    | | After 3.1 km | NT$15 per km |

=== "Distance Table"

    | Delivery Distance | Rate per Order |
    | :--- | :--- |
    | **0–1 km** | NT$105 per order |
    | **1–2 km** | NT$115 per order |
    | **2–3 km** | NT$125 per order |
    | **3–4 km** | NT$140 per order |
    | **4–5 km** | NT$155 per order |
    | **Over 5 km** | Increases following the same pattern |



### 2. Shipping Fees Customers Pay You (Shown on the Storefront)

The shipping fee customers see is calculated as follows:
**Platform base shipping fee ± your custom shipping surcharge or discount**


## Example Scenarios

Say you set the following:

- **Shipping surcharge**: NT$100 added per order
- **Free shipping threshold**: Free shipping on orders of NT$1,000 or more
- **Delivery distance**: 2.9 km (counted as 3 km)

### Example 1: Below the Free Shipping Threshold (Order Amount NT$450)

=== "With Pandago"

    - **You pay**: **NT$105**
    - **Customer pays**: NT$105 (platform fee) + NT$100 (your surcharge) = **NT$205**

=== "With Uber Direct"

    === "Before 2026/07/21"

        - **You pay**: **NT$103**
        - **Customer pays**: NT$103 (platform fee) + NT$100 (your surcharge) = **NT$203**

    === "After 2026/07/21"

        - **You pay**: **NT$125**
        - **Customer pays**: NT$125 (platform fee) + NT$100 (your surcharge) = **NT$225**

### Example 2: Meets the Free Shipping Threshold (Order Amount NT$1,680)

Whichever platform you use, the customer pays **NT$0** for shipping, and you cover the full shipping cost above.



## Reconciliation and Billing

### 1. When You're Charged
When the order status changes to **Shipped**, the system immediately calculates the shipping fee and charges you automatically.

### 2. Payment Method
Quick Delivery shipping fees are always deducted in **CYBER Coins**.

- You can download statements from **Website Management > Reconciliation Center** and see deduction records in **CYBER Coin Usage Details**.
- Example entry text: `pandago shipment, tracking number a-cb00-7715aa`.

### 3. Exception Adjustments
If an order is canceled or an exception occurs, the system creates the related adjustment:

- **Shipping fee refund**: When an order is canceled because of the platform, the deducted shipping fee is refunded.
- **Reverse logistics fee**: When a shopper returns an order for their own reasons, an extra fee is charged to bring the products back to the store.
- **Order compensation**: Compensation the platform pays for driver accidents or lost products.

!!! warning "When Adjustments Take Effect"
	These adjustments are added to the statement for the period and credited or deducted in CYBER Coins only after the delivery platform confirms the cancellation reason (usually the next month).


