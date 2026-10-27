---
title: "Buy X Get Y Discount"
description: "Create a Buy X Get Y Discount group. Set the item-count threshold and the pricing method (fixed amount, percentage of list price, or fixed amount off), and manage the products and valid period."
created: 2026-01-21 00:00
last_modified: 2026-06-30 10:56
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
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 設定任選折扣
features:
  - 任選折扣
prerequisites: []
related: []
tags:
  - Multi-Country
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 任選折扣
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1004
  - https://www.cyberbiz.io/helpcenter/?p=1065
  - https://www.cyberbiz.io/helpcenter/?p=1069
  - https://www.cyberbiz.io/helpcenter/?p=1072
  - https://www.cyberbiz.io/support/?p=1304
  - https://www.cyberbiz.io/support/?p=1335
  - https://www.cyberbiz.io/support/?p=1357
  - https://www.cyberbiz.io/support/?p=1380
  - https://www.cyberbiz.io/support/?p=7316
permalink: "https://help.cyberbiz.io/ec/marketing/discounts/mix-and-match-discounts.en/"
comments: false
search:
  exclude: false
icon: lucide/tags
hide: []
---
# Buy X Get Y Discount

Create a Buy X Get Y Discount group. Set the item-count threshold and the pricing method (fixed amount, percentage of list price, or fixed amount off), and manage the products and valid period.
{ .subtitle }

![](../../../assets/images/EC-後台-行銷活動-任選折扣-畫面總覽01.png){ .hero-page }

## About Buy X Get Y Discount

Buy X Get Y Discount lets you set tiered "buy N items, get a deal" rules for a group of products, such as "3 for NT$599" or "3 items at 70% of list price." At checkout, the system checks and applies these rules first. Use it for end-of-season clearance or cross-category bundle promotions.

!!! tip "Use Cases"
    - **End-of-season clearance**: Set "2 for NT$500, 3 for NT$699" to move low- and mid-priced products faster.
    - **Pair new and older items**: Bundle new and older products with "2 items at 80% of list price" to boost overall visibility and sales.
    - **Multi-category promotions**: Mix high-, mid-, and low-priced products with "3 for NT$999" to raise average order value.

## Before You Start

- **Product limit**: A product can be in only one Buy X Get Y Discount group.
- **Thresholds**: You can set multiple tiers (such as 2 for NT$699 and 3 for NT$599). The system applies the best tier automatically.

## Steps

### Step 1: Create A Buy X Get Y Discount Group

1. Log in to the CYBERBIZ admin and go to **Marketing > Buy X get Y Discount**.
2. Enter a group name and click **Create a collection** to open the settings page.

### Step 2: Set Basic Information And The Promotion Period

1. In the **Basic Information** section, fill in these fields:
    - **Collection name**: A name to identify the group in the admin.
    - **Collection URL:**: The URL path of the storefront promotion page (letters, numbers, and hyphens `-` only).
2. Set the **Start/End Date** to control when the promotion is active.

### Step 3: Set Pricing Rules And Thresholds

In the group list, click the group to expand it and set these fields:

1. **Choose a rule type**:
    - **Fixed price**: Set a fixed total price for the items during the promotion.
      > Example: 3 for NT$599.
    - **Fixed percentage**: Set a fixed discount rate for the items during the promotion.
      > Example: 3 items at 70% (that is, 70% of list price).
    - **Discount fixed amount**: Set a fixed discount amount for the items during the promotion.
      > Example: NT$100 off 3 items.
    - **Discount fixed amount per item**: Set a fixed discount amount per item during the promotion.
      > Example: NT$50 off each item when buying 3.

    **:lucide-info: Plan Availability**

    | Rule Type | Professional/PLUS | Advanced/PLUS | Expert/PLUS | Enterprise |
    |----------|-------------|-----------|-----------|------|
    | Fixed price | ✓ | ✓ | ✓ | ✓ |
    | Fixed percentage | ✓ | ✓ | ✓ | ✓ |
    | Fixed amount off | ✕ | ✕ | ✓ | ✓ |
    | Fixed amount off each item | ✕ | ✕ | ✓ | ✓ |

2. **Add tiers**:
    - Click **Create a new rule condition** to set multiple item-count tiers (for example, 2, 3, and 5 items).

    **:lucide-info: Plan Availability**

    | Rule Type | Professional/PLUS | Advanced/PLUS | Expert/PLUS | Enterprise |
    |----------|-------------|-----------|-------------|--------|
    | Single tier | ✓ | ✓ | ✓ | ✓ |
    | Multiple tiers | ✕ | ✕ | ✓ | ✓ |


3. **Set pricing for remaining items**: With the **Fixed percentage** or **Discount fixed amount per item** rule types, you can choose whether remaining items also get the deal.
    - **Use promotional price**: Remaining items below the threshold are charged the per-item promotional price.
    - **Use original price**: Remaining items below the threshold are charged the original price.

    !!! example "Pricing Example: 3 for NT$599"

        - With "Use promotional price": When buying 4 items, the first 3 cost NT$599 in total, and the 4th costs the per-item promotional price of NT$199.67.
        - With "Use original price": When buying 4 items, the first 3 cost NT$599 in total, and the 4th is charged its original price.

![](../../../assets/images/EC-後台-行銷活動-任選折扣-選擇計價規則01.png)

### Step 4: Add Products To The Group

There are two ways to add products to the discount group:

=== "Add Manually"

    1. Expand the discount group.
    2. In the product list on the left, click **Add** to add products or variants to the group.
    3. Check the product list and order in the group.


=== "Bulk Import"

    1. Download **Buy X Get Y Discount Group Template.xlsx**.
    2. Fill in the product details using the template, including product name, variant, and discount settings.
    3. Upload the completed Excel file. The system imports the products into the group automatically.

    !!! warning "Import Notes"

        - Keep the Excel file in the same format as the template to avoid import errors.
        - The group name must exactly match an existing discount group name.

## Multi-Language Settings

Set multi-language names for Buy X Get Y Discount groups so the storefront can Display the right text for each language.

!!! warning "Notes"
	- To edit the English version, **switch to English** first.
	- Only fields that Display a **language tag** change text when the storefront language changes (Display per language). For example: **Collection name** Buy X Get Y Discount `繁體中文`.
	- If a language field is empty, the storefront uses the **繁體中文** content by default (Display / Display).

### Steps

1. Log in to the CYBERBIZ admin and go to **Marketing > Buy X get Y Discount**
2. In the language menu, switch to the language you want to edit (for example, Traditional Chinese or English).
3. Expand the group, click the group name field to edit it, and press ++enter++ to save.

![](../../../assets/images/EC-後台-行銷活動-任選折扣-設定多國01.png)
