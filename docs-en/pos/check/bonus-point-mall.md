---
title: "Set up Bonus Mall (POS)"
description: "Create a dedicated online Bonus Mall where members can redeem products with points to boost repeat visits and brand loyalty."
created: 2026-04-10 10:00
last_modified: 2026-09-18 14:10
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：商品開賣時間
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 結帳
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: 
  - optional
cyb_extensions: []
intents:
  - 設定紅利商城
  - POS 紅利兌換
  - 建立紅利商品
features:
  - 紅利商城
  - 點數兌換
prerequisites: []
related:
  - ec/marketing/bonus-and-gifts/bonus-point-mall/
tags:
  - "Bonus Mall"
  - "POS Checkout"
  - "Points Marketing"
  - "Member Rewards"
acoiv: configure
apis: []
devices:
  - desktop
  - tablet
ui_components:
  - 紅利商城
  - 行銷活動
  - 小計
paths:
  - 行銷活動 > 紅利商城
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=35526
permalink: "https://help.cyberbiz.io/pos/check/bonus-point-mall/"
comments: false
search:
  exclude: false
icon: lucide/store
hide: []
---

# Set up Bonus Mall (POS)
Create a dedicated online Bonus Mall where members redeem products with points. Set the points required for each product, and use the points accumulation mechanism to increase repeat visits and brand loyalty.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

![](../../assets/images/POS-後台-行銷活動-紅利商城-畫面總覽01.en.png){ .hero-page }


!!! info "Version Differences"
    - **EC storefront (EC)** and **physical store (POS)** both support the Bonus Mall feature. This document applies only to the setup of **Smart POS** Bonus Mall.
    - Bonus Mall is an optional module under the "Marketing A" add-on in the PLUS plan (choose 2 of 11). Merchants must confirm that this module is selected before they use it. The Enterprise plan includes this feature by default.



## Bonus Mall Overview { #specs-bonus-mall }

**Bonus Mall** provides a standalone product showcase and redemption space, allowing members to turn the bonus points they accumulate from everyday purchases into physical products. Through this **Redeem Only** or **Points-Only Purchase** mechanism, members' point balances are put to use, which builds long-term brand loyalty.

The same product remains available for cash purchase in the regular store, while it can be redeemed with points in the Bonus Mall. Both share the same inventory.

!!! tip "Use Cases"
    - **Member Rewards Program**: Offer high-value products that can be redeemed only with bonus points, which encourages members to keep shopping and accumulate points.
    - **Points Usage Strategy**: For points that are about to expire, run a limited-time Bonus Mall campaign to drive members to the site to redeem them.
    - **New Product Trials**: Add trial products to Bonus Mall so that loyal members can try them first with points and provide product feedback.

## Usage Notes { #prerequisites-bonus-mall }

### Front-End Display and Visual Guidelines { #prerequisites-bonus-mall-frontend }
- **Listing Requirements**: Products must be **Listed** and **Published** to appear in the Bonus Mall.
- **Display Limit for Multi-Variant Products**: If a product added to the Bonus Mall has multiple variants (such as different colors or sizes), the storefront shows only the **first main image** of that product. Shoppers cannot switch to images for other variants on the mall page. We recommend selecting a single variant or making sure the main image is representative.
- **Color Scheme**: The Bonus Mall page does not support color swatches.

### Staff Permissions and Scope of Operation { #prerequisites-bonus-mall-section }

- **Admin Permissions**: Only **Site Administrators** can set up and edit the Bonus Mall in the back end.
- **Front-End Staff Permissions**:
    - **Product Lookup**: Search for bonus products by selecting them manually or by scanning the barcode directly.
    - **Real-Time Calculation**: Review the total price of bonus products and confirm the total bonus points used for the entire order, including regular redemptions and Bonus Mall redemptions.
    - **Eligibility Check**: At checkout, the system automatically checks whether the customer's remaining bonus points are enough to cover the transaction.

### After-Sales Return Policy { #prerequisites-bonus-mall-returns-rules }

- **Bonus Points Refund Policy**: Once a bonus product transaction is completed, the system **does not refund** the bonus points used in that transaction if a return occurs.

## Create a Mall in the Back Office { #operate-bonus-mall }

### Step 1: Create the Bonus Mall Basic Information { #operate-bonus-mall-step-a-create }

1. Log in to the CYBERBIZ admin back end, go to **Marketing > Bonus Mall**, and click the **POS Bonus Mall** tab.
2. Click **New Bonus Mall** in the top-right corner.
    ![](../../assets/images/POS-後台-行銷活動-紅利商城-新增商城01.en.png){ .screenshot }
3. Enter the following fields:
    - **Bonus Mall Name**: **Specify the POS store to bind.**
        - **One-to-One Binding**: Each POS store can bind to only one Bonus Mall. Stores that are already bound to a mall automatically hide this option and cannot create a duplicate.
    - **Campaign Start and End Time**: Select the checkbox and set the effective period.
    ![](../../assets/images/POS-後台-行銷活動-紅利商城-新增商城02.en.png){ .screenshot }
6. Click **Save**.

### Step 2: Add Redeemable Products { #operate-bonus-mall-step-b-product }

=== "Manually Select and Add"

    1. On the mall edit page, switch to the **Select Products** tab.
    2. Search for the products you want to add by name, SKU, or product tag.
    3. Click the **Not In Mall** button to the right of the product. The button text changes to **Added** after the product is added.
    4. To add multiple products at once, select the checkboxes on the left, and then click **Add to Mall**.

    ![](../../assets/images/EC-後台-行銷活動-紅利商城-選擇EC商品01.en.png){ .screenshot }

=== "EXCEL Batch Import"

    1. To add a large number of products, edit in batches, or remove products, click **Import Products By Excel** in the top-right menu:
    2. Select the action, and then enter each product's **SKU** and its **Bonus Redemption Amount** in the required format.
        - Only **.xlsx** files are supported.
        - Each file must not exceed **2MB**.
        - Each upload is limited to **200 rows**. If you exceed this limit, upload the file in batches.
    3. The system runs the import in the background and sends an email notification when it finishes.

    ![](../../assets/images/POS-後台-行銷活動-紅利商城-批次匯入01.en.png){ .screenshot }


### Step 3: Set the Points Required for Redemption { #operate-bonus-mall-step-c-settings }

> If you add products by **manually selecting them**, complete this step.<br>
    If you use **EXCEL Batch Import**, enter the redemption amounts directly in the import template. You do not need to set them here.

1. On the **Select Products** tab, scroll down to the **Selected Products** section.
2. In the **Bonus** field, enter the number of points required to redeem the product. The system fills in the product's original price by default.
3. Press **Enter** or click an empty area. The system saves the setting automatically.

![](../../assets/images/EC-後台-行銷活動-紅利商城-設定EC商品紅利兌換值01.en.png){ .screenshot }



## Multi-Store Bonus Mall Management { #operate-multi-store-management }

### Copy a Mall { #operate-multi-store-management-mall }

- **One-Click Sync Setup**: The system uses a one-to-one binding model in which **one store** maps to **one mall**. When multiple stores need malls with the same specifications, use the copy feature to create them quickly.
- **Automatic Product Mapping**: Go to the edit page, click **Copy**, and select the **store** and **campaign period**. The system then automatically imports the matching product list, which greatly shortens listing time.

### Delete a Mall { #operate-multi-store-management-section-m }

- **Unbinding Mechanism**: Once Bonus Mall and a store are bound, the binding cannot be changed directly. If a store needs to switch to a new mall, you must first Delete the original mall to release the store's permissions. Then you can bind the store again.

![](../../assets/images/POS-後台-行銷活動-紅利商城-複製刪除商城01.en.png){ .screenshot }


## Check out at the Front Counter { #operate-bonus-mall-checkout }

When store staff check out a member at the POS front counter, they can add Bonus Mall products to the cart in one of two ways.

### Manually Select Redeemable Bonus Products { #operate-bonus-mall-checkout-points-product }

1. Follow the normal checkout process to add regular products to the cart.
2. Click **Subtotal** in the bottom-right corner to go to the checkout preparation page.
3. Click **Marketing Campaigns**.
4. In the marketing campaign list, select **Bonus Mall**.
5. In the pop-up Bonus Mall window, select the products you want to redeem.
    - **Restriction**: If a product is out of stock or the member's bonus points is insufficient, you cannot select it.
6. Click **Confirm**. The bonus products are added to the cart and marked with a **Bonus Product** tag.
7. Click **Proceed to Checkout**. The checkout page automatically calculates and displays the bonus points required for the redemption.

![](../../assets/images/POS-前台-結帳-新增紅利商城商品01.en.gif){ .screenshot }

### Scan a Redeemable Bonus Product at Checkout { #operate-bonus-mall-checkout-scan-points }

1. When the scanner reads a product that has already been added to the Bonus Mall, the system automatically detects it and displays a **Redeemable with Bonus Points** prompt.
2. Store staff can click the prompt to open the Bonus Mall selection window directly.
3. Select the product you want to redeem, and then click **Confirm**.
    - **Restriction**: If the product is out of stock or the member's bonus points is insufficient, you cannot select it.
4. The system automatically switches the item to bonus redemption mode and deducts the corresponding points.

![](../../assets/images/POS-前台-結帳-新增紅利商城商品02.en.gif){ .screenshot }

## More Actions { #next-steps-bonus-mall }

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__EC Bonus Mall__](../../ec/marketing/bonus-and-gifts/bonus-point-mall.md)
    Create an online Bonus Mall for the EC storefront.

</div>