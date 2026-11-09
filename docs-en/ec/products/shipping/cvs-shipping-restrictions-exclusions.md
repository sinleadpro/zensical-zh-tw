---
title: "Set up Convenience Store Delivery Restrictions and Logistics Exclusions"
description: "Set product dimensions and weight so the system automatically checks whether an order meets the delivery limits of convenience store logistics (B2C/C2C)."
created: 2026-03-08 10:00
last_modified: 2026-07-22 17:24
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
  - 商品
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定超商物流限制
  - 排除超商物流
  - 設定商品材積
  - 設定商品重量
  - 指定商品無法使用超商物流
features:
  - 超商物流規格參考
  - 自動判斷物流條件
  - 手動設定材積與重量
  - 排除超商配送選項
  - 系統判斷邏輯說明
  - 情境範例
  - 常見問題
prerequisites:
  - "Sign in to the CYBERBIZ admin"
related: []
tags:
  - "Convenience Store Delivery"
  - "Logistics Restrictions"
  - "Product Settings"
  - Dimensions
  - Weight
  - "Volumetric Calculation"
  - "Weight Limits"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=950
  - https://www.cyberbiz.io/support/?p=2025
permalink: "https://help.cyberbiz.io/ec/products/shipping/cvs-shipping-restrictions-exclusions/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

![Convenience store shipping restrictions and logistics exclusions](../../../assets/images/ec-product-variants-volumn-weight.zh-tw.en.png){ title="Convenience Store Shipping Restrictions and Logistics Exclusions" .hero-page }

## About Convenience Store Shipping Restrictions { #intro-cvs-shipping-restrictions }

Convenience store logistics (B2C/C2C) have strict size and weight limits for parcels, and parcels over the limits cannot be delivered. At checkout, CYBERBIZ automatically calculates the total size and weight of all products in the order. If the total exceeds the convenience store limits, the checkout page does not show convenience store pickup options.

You can control whether a product can use convenience store logistics in the following ways:

- **Set size and weight:** Enter them in Manage Variants on the product edit page, and the system decides automatically.
- **Exclude convenience store shipping manually:** Set the size or weight above the limit to force the product not to use convenience store logistics.

??? info "Convenience Store Logistics Limits"

    The following table lists the size and weight limits for convenience store logistics:

    | Store Type           | Size Limit                               | Weight Limit             |
    |------------------|----------------------------------------|----------------------|
    | **B2C / C2C**    | Sum of three sides ≤ 105 cm, longest side ≤ 45 cm<br>(FamilyMart B2C: sum of three sides ≤ 120 cm, longest side ≤ 50 cm)      | C2C: weight ≤ 10 kg<br>B2C: weight ≤ 10 kg     |
    | **FamilyMart Frozen B2C / C2C** | Longest side ≤ 45 cm | S60[^1] box: weight ≤ 5 kg<br>S120[^2] box: weight ≤ 10 kg |

    !!! warning "Convenience store size and weight limits may change with carrier policies. For the actual limits, refer to each convenience store carrier's latest announcement."

??? tip "Exclude Shipping Options by Specification Conditions"
    You can adjust a product's size (sum of length, width, and height) or weight to exceed the convenience store limits, and the system automatically excludes the product from convenience store shipping options. Learn [how to prevent specific products from using convenience store logistics](#prerequisites-cvs-shipping-exclusion).

## Set Product Size and Weight { #operate-cvs-shipping-volume }

You can set size and weight information for each product so the system can automatically decide whether it meets convenience store shipping requirements.

1.  Log in to the CYBERBIZ admin and go to **Products > All Products**.
2.  Click the product you want to set up to open the product edit page.
3.  In **Manage Variants**, find the product's size and weight fields:
    -   In the "Size" field, enter the sum of the product's three sides (length, width, and height) in centimeters.
    -   In the "Weight" field, enter the product weight in kilograms.
    
    !!! tip "If the size or weight field is empty, the system uses `0` by default and treats the product as meeting all shipping requirements."

4.  Click **Save** to apply the changes.

![Product size and weight settings](../../../assets/images/ec-product-volume-weight-setting.zh-tw.en.png){ title="Product Size and Weight Settings" }

??? info "How the System Decides"
    When a customer opens the checkout page, the system automatically checks whether the order's **total size or weight** meets convenience store shipping requirements. If it exceeds the limits, the checkout page does not show convenience store options.
    
    | Condition | System Behavior | Result |
    |---|---|---|
    |Product size > 105 cm or weight > 10 kg|The system determines that the product does not meet convenience store shipping requirements|Convenience store logistics options are hidden on the checkout page|
    |Product size or weight is empty|The system treats it as 0|The product can still use convenience store shipping options|


## Prevent Specific Products from Using Convenience Store Logistics { #prerequisites-cvs-shipping-exclusion }

If you don't want specific products to use convenience store logistics, set them up manually as follows:

1.  Log in to the CYBERBIZ admin and go to **Products > All Products**.
2.  Click the product you want to set up to open the product edit page.
3.  In the **Manage Variants** section, set either of the following:
    -   **Size field**: Enter `106` cm (over the convenience store size limit of 105 cm).
    -   **Weight field**:
        -   For room-temperature products, enter `6` kg (over the convenience store weight limit of 5 kg).
        -   For refrigerated or frozen products, enter `11` kg (over the FamilyMart Frozen S120 weight limit of 10 kg).
4.  Click **Save** to finish.

!!! info "Result"
    When an order contains a specified product, the checkout page automatically hides convenience store pickup options, and customers cannot order with convenience store logistics.

## Example Scenarios { #specs-cvs-shipping-examples }

### 1. Total Product Size Exceeds the Limit { #specs-cvs-shipping-over-limit }

- Big Hamster product size: 30 cm each
- Little Piggy product size: 50 cm each

??? quote "If I buy 1 Big Hamster and 2 Little Piggies, can I use convenience store pickup?"
	The total product size is 30 + (50 * 2) = 130 cm. Because the total size exceeds the convenience store size limit of 105 cm, convenience store pickup with or without payment is not available.

### 2. Total Product Size Within the Limit <small>Including Empty Fields</small> { #specs-cvs-shipping-within-limit }

- Amethyst product size: 55 cm each
- Rose Quartz product size: 50 cm each
- Green Crystal product size: empty (the system uses 0 cm each by default)

??? quote "If I buy 1 Amethyst, 1 Rose Quartz, and 1 Green Crystal, can I use convenience store pickup?"
	The total product size is 55 + 50 + 0 = 105 cm. Because the total size equals the convenience store size limit of 105 cm, convenience store pickup with or without payment is available.

## FAQ { #faq-cvs-shipping-restrictions }

??? quote "How does the system decide if a product's size or weight is empty?"
    If the product's size or weight field is empty, the system uses `0` by default and treats the product as meeting all shipping requirements.

??? quote "Do convenience store logistics limits change over time?"
    Yes. Convenience store logistics specifications may change at any time. Follow each convenience store carrier's latest rules.

[^1]: Length + width + height = 60 cm
[^2]: Length + width + height = 120 cm
