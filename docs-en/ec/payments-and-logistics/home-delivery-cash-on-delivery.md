---
title: "Home Delivery Cash on Delivery Logistics (Black Cat / Pelican Express / Hsinchu Logistics)"
description: "Connect CYBERBIZ with Black Cat Express, Pelican Express, and Hsinchu Logistics for cash on delivery, and generate waybills directly in the back office to simplify reconciliation and shipping."
created: 2026-03-05 00:00
last_modified: 2026-06-30 08:52
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 使用新名詞？系統物流 vs 非系統物流
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
intents:
  - 申請新竹物流串接
  - 設定運費門檻
features:
  - 宅配貨到付款
  - 物流串接
  - 自動化產單
  - 新竹物流廠勘
prerequisites:
  - 站台需使用 CYBERBIZ PAYMENTS 金流服務
related:
  - ec/payments-and-logistics/setup-home-delivery-non-cod-custom-logistics/
tags:
  - Integrated_Logistics
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 宅配物流 > 串接物流 > 新竹物流貨到付款
  - 金物流 > 宅配物流 > 串接物流
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10629
  - https://www.cyberbiz.io/helpcenter/?p=10656
  - https://www.cyberbiz.io/support/?p=46272
  - https://www.cyberbiz.io/support/?p=5967
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/home-delivery-cash-on-delivery/"
comments: false
search:
  exclude: false
icon: lucide/banknote
hide: []
---
# Home Delivery Cash on Delivery Logistics (Black Cat / Pelican Express / Hsinchu Logistics)

Connect CYBERBIZ with Black Cat Express, Pelican Express, and Hsinchu Logistics for cash on delivery. Generate waybills directly in the back office to simplify reconciliation and shipping.
{ .subtitle }

[:lucide-toggle-right:{ title="Applicable Features" }](../../resources/conventions#適用功能) | CYBERBIZ PAYMENTS
{ .doc-badge }

!!! info "Integrated Logistics vs. Custom Logistics"
    - **Connect Logistics**: Refers to logistics services deeply integrated with the CYBERBIZ system. The system automatically generates waybills for the corresponding logistics provider and updates delivery status automatically.
    - **Custom Logistics**: If you use a home delivery service other than the three providers above (or one not connected through integration mode), see [Custom Logistics Settings](setup-home-delivery-non-cod-custom-logistics.md).

---

## Step 1: Request Activation

### 1. Black Cat Express and Pelican Express

These two services are usually ready to configure in the back office once the system is activated. No additional manual review is required.

### 2. Hsinchu Logistics

Hsinchu Logistics requires an on-site inspection and contract signing. The process is as follows:

1. Go to **Payment and Logistics > Delivery Settings > Connect Logistics > HCT Cash on Delivery**.
2. Check **Agree to Contract Terms**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/新竹物流串接01.png){ .screenshot }

3. Fill out the application form and submit it.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/新竹物流串接05.png){ .screenshot }

4. CYBERBIZ customer service will notify Hsinchu Logistics to schedule the on-site inspection. **After the inspection is complete**, system activation will be finished within approximately **7-10 business days**.
5. After activation succeeds, you will receive a notification email from the system.

!!! note "Update Information"
    If you need to change the account owner or contact information for Hsinchu Logistics after activation, contact CYBERBIZ customer service for help. Do not modify verified fields yourself.



## Step 2: Enable Logistics

Go to **Payment and Logistics > Delivery Settings > Connect Logistics** and select the corresponding logistics provider to edit.

### 1. Basic Activation Settings

- **Enable Service**: Turn the toggle to **ON**.
- **Outlying Island Delivery**: Choose whether to deliver to Taiwan's outlying islands.

![](https://www.cyberbiz.io/support/wp-content/uploads/新竹物流串接02.png){ .screenshot }

### 2. Shipping Fee and Free Shipping Settings

- **Free Shipping Settings**: When turned on, you can set a free shipping threshold (amount) for each order.
- **Show Free Shipping Threshold at Checkout**: When turned on, shoppers see a reminder in the cart and checkout pages, such as "Spend $XXX more for free shipping."
- **Shipping Fee Settings**: Based on your operating policies, set shipping fees separately for **room temperature, refrigerated, and frozen** items.
    - **Option Display Threshold**: The order amount must meet the minimum threshold you set. If it does not, the system automatically hides this logistics option on the checkout page.
    - **No Amount Limit Setting**: To allow this option for any order amount, set the **starting amount** of any condition range to NT$0.

![](https://www.cyberbiz.io/support/wp-content/uploads/新竹物流串接03.png){ .screenshot }

### 3. Payment Threshold Settings (PLUS and Above Plans)

- You can set a **maximum** or **minimum** checkout amount threshold for this logistics method to avoid collection amounts that are too high or not cost-effective.
  >   :lucide-lock: This feature is available only for PLUS and Enterprise plans.



## Frequently Asked Questions

??? quote "How is the free shipping threshold logic determined?"
    The system evaluates both **Free Shipping Settings** (logistics level) and **Shipping Fee Settings** (temperature zone level). If the order amount meets the free shipping condition of either setting, the checkout page displays free shipping, presenting the most favorable option to the shopper.
