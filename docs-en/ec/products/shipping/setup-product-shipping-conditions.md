---
title: "Set up Product Shipping Conditions (Logistics, Temperature Zone, and Fulfillment Channel)"
description: "Set up a product's shipping temperature zone and logistics. Using standard home delivery and cash on delivery as examples, this guide explains shipping fee settings, product binding, and order splitting at checkout."
created: 2026-01-06 00:00
last_modified: 2026-07-22 17:40
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify FAQ
  - update internal links
  - wikilink to add 宅配物流：串接一般宅配物流
  - verify 修改物流運費設定的注意事項
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
  - 金物流
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
  - 如何設定物流運費
  - 如何建立自訂宅配物流
  - 如何設定商品配送溫層
  - 如何設定商品配送方式
  - 如何設定商品出貨通路
features:
  - 商品配送條件綁定
  - 配送物流綁定
  - 配送溫層綁定
  - 出貨通路綁定
  - 自訂物流設定
  - 貨到付款設定
prerequisites:
  - "Sign in to the CYBERBIZ admin"
related:
  - ec/products/checkout/checkout-split-multi-cart/
  - ec/products/bulk-operations/batch-update-product-descriptions-shipping/
tags:
  - "Shipping Temperature Zone"
  - "Logistics Settings"
  - "Home Delivery"
  - "Product Settings"
  - "Shipping Fee Settings"
  - "Shipping Condition Binding"
  - "Custom Logistics"
  - "Cash on Delivery"
  - "Product Channels"
  - "Cart Splitting"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 宅配物流
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2221
  - https://www.cyberbiz.io/helpcenter/?p=2249
  - https://www.cyberbiz.io/support/?p=2107
  - https://www.cyberbiz.io/support/?p=2131
permalink: "https://help.cyberbiz.io/ec/products/shipping/setup-product-shipping-conditions/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

![Product shipping condition settings](../../../assets/images/ec-product-temp-logistics-settings.zh-tw.en.png){ title="Product Shipping Condition Settings" .hero-page }

## About Binding Delivery Conditions

Binding delivery conditions means explicitly setting a product so that it "can use" or "can only use" specific logistics, delivery temperature zones, or fulfillment channels.
Based on these bindings, the system determines and displays the available delivery options when customers check out.

!!! example "Use Cases"

    - **Logistics binding**: When a product can only be delivered by specific logistics (such as T-Cat, Pelican Express, or Chunghwa Post), set the product to use only those logistics.
    - **Delivery temperature zone binding**: For products that need special temperature zone delivery (such as room temperature, refrigerated, or frozen), set one or more applicable temperature zones.
    - **Fulfillment channel binding**: When products ship from different locations (such as different warehouses, stores, or vendors), set the fulfillment channel each product belongs to.

## Set Shipping Fees by Temperature Zone

Before you set product delivery conditions, create each **logistics method** in the admin and set shipping fee rules for each **delivery temperature zone**.  
After setup, the logistics options appear on the product edit page for binding.

### Standard Home Delivery <small>Custom Logistics</small>

The following explains how to create a home delivery logistics method that charges by delivery temperature zone.

1. Log in to the CYBERBIZ admin and go to **Payment and Logistics > Delivery Settings**.
2. Click the "Custom Logistics" tab, then click "Add Custom Logistics".
3. Complete the following settings in order:

	- **Shipping Rule Name**: Enter the display name of the logistics method. Don't duplicate or change the name casually[^1][^2][^3].

	- **Shipping Regions**: Select the regions the logistics method can deliver to.
	    
	- **Shipping temperature zone**: Select the delivery temperature zone this logistics method applies to (room temperature by default).
	    
	- **Order Amount Based Shipping Fee Setting**:
	    
	    - Enter the "Order Amount" and the corresponding "Shipping Fee".
	    - To set multiple amount ranges, click **Create Setting** to add shipping fee thresholds.

4. Click **Save** to apply the settings.

After that, the logistics method appears on the **Settings** tab of the product edit page, where you can set up [delivery temperature zone binding](#Set-Product-Delivery-Temperature-Zone) and [delivery method binding](#Set-Product-Delivery-Methods).

![Custom logistics settings](../../../assets/images/ec-product-custom-logistics-settings.zh-tw.en.png){ title="Custom Logistics Settings" }

!!! warning "Bind New Logistics Manually for Logistics-Restricted Products"
	If a product is set to "specific logistics only", logistics methods you add later **are not bound automatically** to it. Bind the product to the new logistics manually, or the logistics method **won't appear in the delivery options at checkout**. [Learn more](#Add-Logistics-After-Binding-Products).

[^1]: Don't use the same names as built-in system logistics (for example, T-Cat Cash on Delivery or Pelican Express Cash on Delivery), or checkout errors or logistics detection issues may occur.
[^2]: If you change a logistics name, products bound to the original name are unbound, and you must set their delivery methods again.
[^3]: Even for the same carrier, different delivery temperature zones **must use different logistics names**, for example: T-Cat (Room Temperature) / T-Cat (Refrigerated) / T-Cat (Frozen).

---

### Home Delivery Cash on Delivery

The following explains how to set cash on delivery and shipping fee rules for different delivery temperature zones on an existing home delivery logistics method.

1. Log in to the CYBERBIZ admin and go to **Payment and Logistics > Delivery Settings**.
2. Find the logistics option to set up and click :material-text-box-edit-outline: to open its edit page.

	![Edit home delivery logistics](../../../assets/images/ec-conntect-logistics-edit.zh-tw.en.png){ title="Edit Home Delivery Logistics" }
	
3. Set cash on delivery and free shipping conditions:

	- Turn on cash on delivery.
	- Turn on free shipping and set the free shipping amount.

	!!! warning "The Cash on Delivery Amount May Affect Free Shipping"  
		If the collected order amount reaches or exceeds the free shipping threshold, the system ignores the shipping fee settings and the order ships free.

	![Cash on delivery and free shipping settings](../../../assets/images/ec-conntect-logistics-settings.zh-tw.en.png){ title="Cash on Delivery and Free Shipping Settings" }

4. Set shipping fees for different delivery temperature zones:

	- Shipping fees can only be calculated based on the **collected order amount**.
	- Set the shipping fee for each delivery temperature zone separately.

	![Delivery temperature zone shipping fee settings](../../../assets/images/ec-conntect-logistics-temp-fees.zh-tw.en.png){ title="Delivery Temperature Zone Shipping Fee Settings" }

## Set Product Delivery Temperature Zone

After you complete the [logistics shipping fee settings](#Set-Shipping-Fees-by-Temperature-Zone), you can set the delivery temperature zone and corresponding logistics available to each product. To understand how binding works, see [What binding delivery conditions means](#About-Binding-Delivery-Conditions) first.

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click the product to set up to open its edit page.
3. Switch to the **Settings** tab.
4. In the **Temperature Zone Settings / Temperature Zone and Logistics Settings** section, select the delivery temperature zones that apply to this product (you can select more than one; the default is `常溫`, room temperature).

![Product delivery temperature zone settings](../../../assets/images/ec-product-temp-setting.zh-tw.en.png){ title="Product Delivery Temperature Zone Settings" }

## Set Product Delivery Methods

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions.md#conventions-plans){ title="Icon Conventions" } |
Expert / PLUS / Enterprise

You can set the delivery logistics methods available to each product. To understand how binding works, see [What binding delivery conditions means](#About-Binding-Delivery-Conditions) first.

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click the product to set up to open its edit page.
3. On the product edit page, find the **Temperature Zone and Logistics Settings** section and set the logistics methods the product can use.

    - **Logistics binding status**:
        - `ON`: This product *can* be delivered with that logistics method.
        - `OFF`: This product *cannot* be delivered with that logistics method.
    - **Default behavior**: When a product is created, the system binds all available logistics methods by default.  
    - **Requirement**: Each product *must be bound to at least one delivery logistics method*, or it can't be delivered.
        
    ![Logistics binding toggles](../../../assets/images/ec-logistics-toggle.zh-tw.en.png){ title="Logistics Binding Toggles" }
    
4. **Confirm the change reminder**: The first time you change a logistics binding, the system shows a reminder. Read the notes carefully, then check the box and click **Confirm**.
    !!! info "If you don't confirm, the system shows the reminder again every time you change a logistics binding."

### Notes on Changing Logistics Shipping Fee Settings
When you change logistics shipping fee settings, keep the following in mind:

**Changing the shipping fee calculation basis**  
If you change the basis for calculating shipping fees, you must reset the logistics temperature zone, the shipping fee rules, and the logistics bindings on product pages.

-   Products **apply to all delivery methods by default**. For products that need specific logistics, remember to set them individually.
-   The courier/logistics names on product pages also change to the items you created in "Logistics Shipping Fee Settings".

![Temperature zone and delivery logistics settings](https://www.cyberbiz.co/support/wp-content/uploads/2019/03/溫層配送物流設定-一般宅配5.png){ title="Temperature Zone Delivery Logistics Settings" .screenshot }
![Temperature zone and delivery logistics settings](https://www.cyberbiz.co/support/wp-content/uploads/2020/07/溫層配送物流設定-一般宅配6.png){ title="Temperature Zone Delivery Logistics Settings" .screenshot }

## Set Product Channels <small>Fulfillment Channel</small>

!!! info "What Product Channels Affect"
    Product channels specify where a product ships from, such as a store, warehouse, or supplier. The setting affects the following:

    - [Cart splitting](../checkout/checkout-split-multi-cart.md){ title="Set Up Automatic Checkout Splitting into Multiple Carts" }
    - Checkout
    - Order creation and fulfillment

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. In the product list, click the product to set up to open its edit page.
3. Switch to the **Settings** tab.
4. Select a channel in the **Product distribution channel** field:
    
    - The default is "Select a channel (no channel)", which means the product **applies to all channels**.  
    - Apart from "no channel", each product **can be bound to only one product channel**.  
    - If no matching channel is in the drop-down menu, type text to add a new channel name.
        
5. After entering the channel name, click **Add** to finish.
  
![Add a product channel](../../../assets/images/ec-product-distribution-channel-create-new.zh-tw.en.png){ title="Add a Product Channel" }

!!! warning "Product Channels Cannot Be Deleted Once Added"  
    A product channel cannot be deleted once added. Make sure the channel name is correct before adding it.

## Example Scenarios

### Cart Splitting Across Multiple Channels

**Example scenario**: Product channels are set to Taipei Store and Taichung Store

|Product|Product Channel|
|---|---|
|Product A|Taipei|
|Product B|Taichung|
|Product C|Taipei or Taichung|

---

**System behavior and checkout result**:

1. The customer adds all three products to the cart
    - The system splits the cart automatically by fulfillment channel:
        - **Taipei Store cart** → Product A, Product C
        - **Taichung Store cart** → Product B, Product C

2. The customer checks out the Taipei Store cart
	- A **Taipei Store order** is created
    - The quantity of Product C in the Taichung Store cart updates automatically to avoid duplicate shipments
3. The customer checks out the Taichung Store cart
	- A **Taichung Store order** is created

---

### Add Logistics After Binding Products

After products are bound to delivery logistics, *if you add a new delivery logistics method*, the system decides whether to apply it based on each product's existing logistics binding:

- Products set to "all delivery logistics" > The system **automatically applies and binds** the new delivery logistics.
- Products set to "specific delivery logistics only" > The system **does not automatically bind** the new delivery logistics. To use it, bind it manually on the product settings page.

Example

|Product|Existing Delivery Logistics|Original Product Logistics Setting|Result After Adding Delivery Logistics|
|---|---|---|---|
|Product A|T-Cat, Pelican Express|All delivery logistics|:material-check: Hsinchu Logistics bound automatically|
|Product B|T-Cat, Pelican Express|Specific delivery logistics only (T-Cat)|:material-close: Hsinchu Logistics not bound automatically (still T-Cat only)|

---

### How Different Logistics / Temperature Zone / Fulfillment Channels Work

This section explains the admin settings and storefront checkout behavior when products have different *delivery logistics, delivery temperature zones, and fulfillment channels*.

#### Admin Settings

Delivery settings in the admin have three levels, which together affect the delivery options available to products and how checkout is split.

- Logistics shipping fee settings: After setup, the corresponding logistics appear on the product settings page for binding.
   > For example, set up two logistics methods: *T-Cat home delivery* and *Pelican Express*.
    
- Delivery temperature zone settings: The system has three built-in delivery temperature zones: **room temperature, refrigerated, and frozen**. On the product settings page, select the temperature zones that apply to the product (you can select more than one).
- Product channel (fulfillment channel) settings: Different channels are treated as different shipping sources, which affects checkout and cart splitting.
  > For example, set two product channels (shipping locations), *Taipei Store* and *Taichung Store*, on the product edit page.

---

#### Storefront Display and Checkout Behavior

When a customer's cart contains products with different *delivery logistics, delivery temperature zones, or fulfillment channels*, storefront checkout works as follows:

1. The system groups the cart contents by **fulfillment channel**.
2. The customer first selects a fulfillment channel.
3. Under that channel, the customer selects an available **delivery temperature zone** and **delivery logistics** in turn and checks out.
4. Products not yet checked out stay in the cart for later checkout.
5. The customer must complete checkout for each cart separately, and the system creates multiple orders.

!!! info "If a cart doesn't reach the free shipping threshold, shipping fees are calculated and charged for each cart separately."

!!! tip "Simplify Delivery Conditions to Reduce Cart Abandonment"
	When products have multiple delivery conditions (product channel, delivery temperature zone, and delivery logistics), the system automatically splits them into multiple carts at checkout based on those conditions, *making checkout more complex and increasing shipping costs for customers*. Learn about [checkout with multiple carts](../checkout/checkout-split-multi-cart.md#About-Checkout-Splitting-into-Multiple-Carts){ title="Set Up Automatic Checkout Splitting into Multiple Carts" }.

## Next Steps

<div class="grid cards" markdown>

- :lucide-pencil:{ .lg }  
   [__Batch Edit Shipping Settings__](../bulk-operations/batch-update-product-descriptions-shipping.md){ title="Batch Edit Product Descriptions and Shipping Settings" }  
   Use Excel to edit the shipping settings of many products at once.
- :lucide-shopping-cart:{ .lg }  
   [__Split Checkout into Multiple Carts__](../checkout/checkout-split-multi-cart.md#About-Checkout-Splitting-into-Multiple-Carts){ title="Set Up Automatic Checkout Splitting into Multiple Carts" }  
   Learn how products' multiple delivery conditions create multiple carts at checkout.

</div>

## FAQ

??? quote "If I change a logistics name, will product bindings stop working?"
    Yes. If you change the name of a logistics method, products bound to it are unbound. Go to the product pages and bind the delivery logistics again.

??? quote "Can I set multiple temperature zones for one product?"
    Yes. On the "Settings" tab of the product edit page, you can select multiple temperature zones for the product.

??? quote "Why do customers see multiple carts at checkout?"
    When a customer buys products with different temperature zones, delivery logistics, or fulfillment channels, the system automatically splits them into multiple carts for checkout. Learn about [checkout with multiple carts](../checkout/checkout-split-multi-cart.md#About-Checkout-Splitting-into-Multiple-Carts){ title="Set Up Automatic Checkout Splitting into Multiple Carts" }.
