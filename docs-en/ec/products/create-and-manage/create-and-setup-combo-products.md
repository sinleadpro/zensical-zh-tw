---
title: "Create and Set up Product Combos"
description: "Create fixed or mix-and-match product combos and set up their sub-products, prices, inventory, and sales rules."
created: 2026-01-08 00:00
last_modified: 2026-09-18 14:10
lang: en-US
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/create-and-setup-combo-products/"
type: guide
author: ""
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
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: 
  - optional
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 如何新增組合商品
  - 設定組合商品
features:
  - 組合商品
prerequisites: []
related:
  - ec/marketing/coupon/setup-promo-codes/
  - ec/marketing/coupon/setup-coupons/
  - ec/marketing/discounts/threshold-gifts-and-quantity-gifts/
  - ec/marketing/upsells/setup-product-upsell/
  - ec/products/shipping/setup-product-shipping-conditions/
  - ec/products/create-and-manage/create-update-products/
  - ec/products/create-and-manage/edit-product-slogan-and-description/
  - wms/processed-products/
tags:
  - "Combo Products"
  - "Fixed Product Combo"
  - "Mix-and-Match Product Combo"
  - "Sub-Product Inventory"
  - "Product Combo Price Difference"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 組合商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5717
  - https://www.cyberbiz.io/helpcenter/?p=8055
  - https://www.cyberbiz.io/support/?p=37330
  - https://www.cyberbiz.io/support/?p=9749
comments: false
search:
  exclude: false
icon: lucide/boxes
hide: []
---
# Create and Set up Product Combos
Create specified or optional combo products and set their sub-products, prices, inventory, and sales rules.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    On PLUS plans, "combo products" are part of the "Marketing A" add-on modules (choose 2 of 11), so make sure you've selected that module before using it. The Enterprise plan includes this feature.

![Add a combo product](../../../assets/images/ec-create-new-product-combo.zh-tw.en.png){ title="Add a Combo Product: Products > Add Combo Product" .hero-page }

## About Combo Products { #intro-combo-products }

=== "Standard, PLUS"

    A combo product combines two or more products into a single product for sale. You can set up a **Specified Quantity** combo with fixed contents, or an **Optional Quantity** combo whose contents customers choose themselves.
    
    - **Specified Quantity**: You fix the products and quantities in the section; customers can't change them.
    - **Optional Quantity**: You set the **total quantity to choose** for the section, and customers pick freely from the list.
    
    Common use cases:

    - Bundle deals: Package multiple products at a combo price to encourage purchases.
    - Promotions: For example, Christmas gift boxes or anniversary sale bundles.
    - Higher average order value: Encourage customers to buy several products at once to increase sales.
    - Inventory clearance: Bundle slower-selling products with best sellers to speed up inventory turnover.

=== "Enterprise"

	A combo product can mix multiple **Specified Quantity** and **Optional Quantity** sections. Its features:

	- **Fixed and optional together**: No longer limited to a single rule, a combo can include both **must-buy (specified combo)** and **free-choice (optional combo)** sections. You can easily create set meals such as "fixed main course + drink of choice" to maximize sales flexibility.

	!!! example "Mixed Combo Product Example"
		Back-to-School New Device Sale – Tablet + Official Accessories + Peripherals of Your Choice Value Bundle

		- **Structure**: Mixes a "specified combo section" and an "optional combo section".
    	- **Contents**:
			1.  **Section 1 (specified)**: 1 tablet and 1 official protective case.
			2.  **Section 2 (optional)**: Any 2 items from the accessory pool (screen protector, keyboard, stylus, and so on).
    	- **How customers buy**: Customers who buy this bundle always get a tablet and an official protective case (the must-buy combo), and can freely choose the accessories.

## Combo Product Limits { #prerequisites-combo-products }

Combo products have the following limits in the system:

### Conditionally Supported Attributes { #prerequisites-combo-products-attrs }

- **Admin product tags**

    1. Requirements

        - **Applicable plan**: Enterprise
        - **Not applicable**: Professional, Advanced, Expert, and all PLUS plans
        - **Details**: Only the Enterprise plan can set product tags on combo products. On other plans, this attribute isn't available when creating combo products.

    2. Use cases

        After you set **product tags** on a combo product, it counts as a product within that tag's scope and can take part in marketing campaigns that **target products by product tag**.

        **Compatible campaign types**:

        - [Promo codes](../../marketing/coupon/setup-promo-codes.md)/[coupon](../../marketing/coupon/setup-coupons.md): Use product tags to limit which products the discount applies to
        - [Product threshold/quantity gifts](../../marketing/discounts/threshold-gifts-and-quantity-gifts.md): Use product tags to limit which products count toward the gift threshold
        - [Product upsells](../../marketing/upsells/setup-product-upsell.md): Use product tags to limit the scope of main product conditions

    3. Where to set it

        Go to the **Settings** tab and specify **Tags**.

        ![](../../../assets/images/EC-後台-商品-組合商品-綁定商品標籤01.en.png)


### Unsupported Attributes { #prerequisites-combo-products-unsupported }
    
- Product type, product vendor  
- Google product category
- SEO settings  
- Fast delivery  
- Related product collections
        
### Bulk Operation Limits { #prerequisites-combo-products-batch }
    
- Bulk adding or bulk editing combo products isn't supported yet
        
### Weight Calculation { #specs-combo-products-weight }
    
- Combo products don't include sub-product weights; the system always treats them as 0 kg
- The checkout page checks against logistics volume limits

### Marketing Campaigns for Combo Products { #specs-combo-products-campaigns }

The following tables list the marketing campaigns combo products can take part in and their limits:

=== ":material-check-circle: Supported"
	| Marketing Campaign | Notes | Status |
	|-----------|-----------|-----------|	
	| Coupon, free shipping coupon |  | :material-check: |
	| Order amount free shipping threshold (convenience store + home delivery) |  | :material-check: |
	| First-purchase gift (campaign rule: spending threshold) |  | :material-check: |
	| Bonus for spending threshold (member bonus points) |  | :material-check: |
	| Commission sharing |  | :material-check: |
	| Referral commission discount code |  | :material-check: |
	| Bonus redemption |  | :material-check: |
	| Specified combo products: recurring orders, one-page campaign pages | | :material-check: |

=== ":material-alert: Conditionally Supported"
	| Marketing Campaign | Notes | Status |
	|-----------|-----------|-----------|
	| Order upsell | Combo products can't be used as *upsell items* | :material-alert-outline: |
	| Order threshold gift | Combo products can't be used as *threshold gifts* | :material-alert-outline: |

=== ":material-close-circle: Not Supported"
	| Marketing Campaign | Notes | Status |
	|-----------|-----------|-----------|
	| Buy X Get Y discount |  | :material-close: |
	| Mix and Match |  | :material-close: |
	| Single-product discount |  | :material-close: |
	| Product-linked coupon giveaway |  | :material-close: |
	| Product-linked bonus giveaway |  | :material-close: |
	| First-purchase gift (product tags) |  | :material-close: |
	| Multi-level category threshold discount |  | :material-close: |
	| Coupon for spending threshold (sitewide campaign – coupon) |  | :material-close: |
	| Bonus Mall |  | :material-close: |
	| Product purchase limit |  | :material-close: |
	| Sitewide campaign (amount/percentage) |  | :material-close: |
	| Product upsell |  | :material-close: |
	| Product threshold gift / product quantity gift |  | :material-close: |
	| Optional combo products | | :material-close: |


## Add a Combo Product { #operate-combo-products }

With combo products, you can package multiple sub-products for sale to increase sales flexibility and promotion efficiency.

### Step 1: Go to Combo Product Management { #operate-combo-products-enter }

1. Sign in to the CYBERBIZ admin and go to **Products > Product Combo**.
2. Click **Create New Combo Product**.

![Combo product management page](../../../assets/images/ec-product-combo-add-page.zh-tw.en.png)



### Step 2: Edit Combo Product Details { #operate-combo-products-info }

=== "Standard, PLUS"

    - **Combo Product Name**: Avoid special characters (such as `|` or `”`). HTML isn't allowed.
    - **Product URL**: We recommend English for SEO and GA analysis. If not set, the system uses the **product name** as the URL.
    - **Product slogan**: Short text shown on the product page to highlight the combo product's features.
    - **Product brief**: We recommend 1–3 sentences; avoid long paragraphs. A short description shown on the product page.
    - **Sell status**: Set when the product is launched and taken off market. If left blank, the product stays launched permanently; outside the launch period, the page shows 404.

    ![](../../../assets/images/EC-後台-商品-組合商品-建立v2組合品01.en.png){ .screenshot }

=== "Enterprise"

    - **Combo Product Name**: Avoid special characters (such as `|` or `”`). HTML isn't allowed.
    - **Product URL**: We recommend English for SEO and GA analysis. If not set, the system uses the **product name** as the URL.
    - **Product slogan**: Short text shown on the product page to highlight the combo product's features.
    - **Product brief**: We recommend 1–3 sentences; avoid long paragraphs. A short description shown on the product page.
    - **Sell status**: Set when the product is launched and taken off market. If left blank, the product stays launched permanently; outside the launch period, the page shows 404.
    - **Compare-at price/price**: The **compare-at price** is the product's original price, and the **Price** is the sale price customers actually pay at checkout.
    - **Bonus redemption**: Set the maximum amount of bonus points members can redeem on this combo product.
    - **Vendor number**: Enter the vendor ID code used for internal management or communication with suppliers.
    - **Product Number(SKU)**: Set a unique stock keeping unit number for the combo product. We recommend keeping it distinct from sub-product numbers to make order management easier.

    ![](../../../assets/images/EC-後台-商品-組合商品-建立組合品01.en.png){ .screenshot }


!!! tip "Describe What's in the Combo Product"  
	To avoid customer confusion, clearly list the sub-products and quantities included in the combo product in the **product brief** or **product slogan**.

??? info-clean "Storefront Display Example"

    - Product name: Super Value Combo
    - Product brief:  
      Includes  
      Cake ×1  
      Curtain ×1  
      Quilt ×1
    - Product slogan: A super value combo product

    !!! quote ""
      ![Combo product on the storefront](../../../assets/images/ec-product-combo-basic-setting-frontend.zh-tw.en.png){ title="Combo Product on the Storefront" }


### Step 3: Upload Product Images { #operate-combo-products-images }

We recommend uploading images that show the contents of the combo product so the bundle is clear.

![Upload combo product images](../../../assets/images/ec-product-combo-image.zh-tw.en.png)



### Step 4: Set up Combo Product Contents { #operate-combo-products-content }

=== "Standard, PLUS"

    1. **Choose the combo product type**:

        === "Specified Combo"

            For **Combo Product Type**, select **Specified Quantity**.

            ![](../../../assets/images/EC-後台-商品-組合商品-建立v2組合品02.en.png){ .screenshot }

        === "Optional Combo"

            For **Combo Product Type**, select **Optional Quantity** and specify the total quantity to choose for the combo.

            ![](../../../assets/images/EC-後台-商品-組合商品-建立v2組合品03.en.png){ .screenshot }

        !!! warning "The Combo Type Can't Be Changed After the Combo Product Is Created"
    
    2. **Add products**: In the section, click **Select Product** and select products in the pop-up window.

        - **Quick search**: Enter a product name or SKU to find a specific product.
        - **Bulk filter**: Click **Advanced Search** to open the filter and find products that match your conditions.


    3. **Set prices and identifiers**:

        - **Compare-at price/price**: The **compare-at price** is the product's original price, and the **Price** is the sale price customers actually pay at checkout.
        - **Bonus redemption**: Set the maximum amount of bonus points members can redeem on this combo product.
        - **Vendor number**: Enter the vendor ID code used for internal management or communication with suppliers.
        - **Product Number(SKU)**: Set a unique stock keeping unit number for the combo product. We recommend keeping it distinct from sub-product numbers to make order management easier.


    !!! info "For how inventory quantity is calculated, see 'Product Combo C' in [Inventory Management](#operate-combo-products-stock)."

=== "Enterprise"


    1. **Add Section Block**: Click the button to create the first content section.
    2. **Choose the section type**:

        - **Fixed Combo**: You fix the products and quantities in the section; customers can't change them.
        - **Optional Combo**: You set the **total quantity to choose** for the section, and customers pick freely from the list.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-組合商品-建立組合品04.png){ .screenshot }

    3. **Add products**: In the section, click **Select Product** and select products in the pop-up window.

        - **Quick search**: Enter a product name or SKU to find a specific product.
        - **Bulk filter**: Click **Advanced Search** to open the filter and find products that match your conditions.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-組合商品-建立組合品06.png){ .screenshot }

    4. **Set purchase quantities**:

        === "Specified Combo"

            Specify the purchase quantity of each product.

            ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-組合商品-建立組合品10.png){ .screenshot }

        === "Optional Combo"

            Specify the total purchase quantity for products in the combo.

            ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-組合商品-建立組合品11.png){ .screenshot }


    5. **Build a mixed combo** (key step): Click **Add Section Block** again to create a second section.

        > Example: Set section A as a "fixed combo" for the main products, and section B as an "optional combo" for choosing gifts or accessories.

    6. **Customize section details**:

        - **Edit Section Name**: Click the section title (such as "Section 1") to customize its name. This name appears on the storefront to guide customers.
        - **Reorder sections**: Drag the icon on the left of a section to change the order sections appear on the storefront page.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-組合商品-建立組合品07.png){ .screenshot }

!!! warning "Check Applicable Temperature Zones and Logistics"
    When you set delivery options on the **Settings** tab, follow these rules:

    - **Publishing requirement**: All individual products in the combo must share **at least one common temperature zone and logistics option** before the combo product can be published.
    - **When there's a conflict**: If conflicts between individual products leave the combo product with no applicable temperature zone and logistics, the combo product can't be published, and its storefront product page shows a 404 error page.
    - **How to fix it**: Edit each individual product's logistics and temperature zone so they share a common temperature zone/logistics option, or remove products with special temperature zone/logistics from the combo product.

## Storefront Checkout and Cart Behavior { #specs-combo-products-checkout }

=== "Standard, PLUS"
    
    === "Specified Combo"

        Click **Add to Cart** on the product page.

        ![](../../../assets/images/EC-前台-商品頁-指定組合品01.en.png){ .screenshot }
        
    === "Optional Combo"

        Customers must select the **total optional combo quantity** set in the admin before they can add it to the cart.
        
        > When the selection limit is reached, the storefront shows **Limit reached**.
        
        ![Optional combo on the storefront](../../../assets/images/ec-product-combo-optional-quantity-frontend.zh-tw.en.png){ title="Optional Combo on the Storefront" }


=== "Enterprise"

    The storefront product page shows the **combo sections** in the order you set in the admin.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-商品頁-組合商品01.png){ .screenshot }

    === "Specified Combo Section"

        In a **specified combo section**, the items and quantities are fixed and customers can't edit them.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-商品頁-組合商品02.png){ .small-image }

    === "Optional Combo Section"

        In an **optional combo section**:

        1. **Selection progress**: The upper right of the section shows **0 / N selected** in real time. The number updates as customers add or remove products, and customers can't add the combo to the cart until the requirement is met.
        2. **Product list**: By default, the variant menu of the first product is expanded. Customers can also click the **down triangle** arrow on the right to collapse or expand other products.
        3. **Variant quantities**: Customers use the **+** and **-** buttons to adjust quantities of different variants until the section's total quantity requirement is met.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-商品頁-組合商品03.png){ .small-image }

- The cart and checkout page check whether the combo product meets logistics volume limits.  
- Combo products support only a single temperature zone and don't support [multi-channel cart splitting](../shipping/setup-product-shipping-conditions.md#specs-ship-conditions-split-cart){ title="Set Up Product Shipping Conditions (Logistics, Temperature Zone, and Fulfillment Channel)" }.

![Combo product in the cart](../../../assets/images/ec-product-combo-optional-quantity-cart.zh-tw.en.png){ title="Combo Product in the Cart" }
## Combo Product Shipping { #specs-combo-products-ship }

After a combo product order is placed, when the system generates a convenience store or home delivery waybill, it also generates the following four documents. All of them include details of every sub-product in the combo product:

- **Order details**: Shows each product in the order and the contents of combo products.
- **Shipping details**: Lists the products and quantities to ship.
- **Pick list**: The basis for warehouse picking, including the sub-products in combo products.
- **Waybill**: The logistics shipping document, including details of all sub-products in the combo product.

## Sub-Product Inventory Management { #operate-combo-products-stock }

Whether a combo product can be purchased (has enough inventory) depends on the inventory quantity and settings of its sub-products. If any sub-product is out of stock and is set to **Stop selling** when out of stock, the combo product can't be purchased. Learn more about [product inventory settings](create-update-products.md#operate-product-create-inventory){ title="Add and Update Products" }.

!!! info "When a Sub-Product Is Taken Off Market or Discontinued"  
	- The **sell status** of sub-products in a combo product can be _Off Market_ or _Unlisted_.
	  - If a sub-product is discontinued, remove it from the combo product.

|**Sub-product A variant setting**|**Sub-product B variant setting**|**Purchasable quantity of Product Combo C (A + B)**|
|---|---|---|
|Stop selling when out of stock (inventory = 10)|Stop selling when out of stock (inventory = 20)|10|
|Continue selling when out of stock (inventory = 10)|Stop selling when out of stock (inventory = 20)|20|
|Unlimited (inventory not tracked)|Stop selling when out of stock (inventory = 20)|20|
|Continue selling when out of stock (inventory = 10)|Continue selling when out of stock (inventory = 10)|Unlimited|
|Unlimited (inventory not tracked)|Continue selling when out of stock (inventory = 10)|Unlimited|
|Stop selling when out of stock (inventory = 0)|Stop selling when out of stock (inventory = 20)|Out of stock|


## Combo Product Price Difference Calculation { #specs-combo-products-price-diff }

In order reports, Excel/CSV exports, and API responses, the system provides a **combo product price difference** field to help you reconcile accounts and analyze how discounts are allocated.

!!! info-clean "Calculation Logic"

    Combo product prices and price differences are calculated as follows:

    - **Combo product discount** = total price of sub-products − combo product price
    - **Discount allocation**: The combo product discount is allocated proportionally to each sub-product
    - **Combo product price difference** = sub-product original price − final price after allocation
        
    !!! warning "Note"
        The combo product price difference reflects each sub-product's share of the discount. It's for reconciliation and report analysis and doesn't affect the actual checkout amount.

??? example "Calculation Example"

    Suppose a combo product contains three sub-products:

    - Combo product price: NT$850
    - Total original price of sub-products: NT$900
    - Total discount: NT$50
        
    |Sub-product|Final Price|Combo Product Price Difference|
    |---|---|---|
    |A|94|6|
    |B|283|17|
    |C|473|27|

    **Explanation**:

    - "Final price" is the price after the discount is allocated proportionally to each sub-product
    - "Combo product price difference" is the original price minus the final price
    - The combo product price differences of the three sub-products add up to NT$50 (the same as the total discount)

## Next Steps { #next-steps-combo-products }

<div class="grid cards" markdown>

- :lucide-pencil:{ .lg }  
  [__Edit Product Descriptions and Product Settings__](edit-product-slogan-and-description.md){ title="Edit Product Descriptions and Product Settings" }  
  Import an edited product Excel file to update the product descriptions and delivery settings of multiple products at once.

- :lucide-boxes:{ .lg }  
  [__Combo Products (Bundle Products)__](../../../wms/processed-products.md){ title="Bundle Products" }  
  Map combo products to WMS bundle products so each sub-item's inventory is deducted automatically at shipping.  

</div>

## FAQ { #faq-combo-products }
??? quote "Can I change the combo type of a combo product?"
    Once a product is created, its combo type (specified or optional combo) can't be changed. To change it, we recommend creating a new product.

??? quote "Does a sub-product being out of stock affect sales of the combo product?"
    Yes. If any sub-product in the combo product is out of stock and is set to *stop selling when out of stock*, the whole combo product can't be purchased.
