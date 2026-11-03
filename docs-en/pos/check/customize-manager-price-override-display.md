---
title: "Change the Display Name of Manager Price Override on the Order Details Page"
description: "Modify the code to rename the storefront order details label from Manager Price Override to Product Price Override to prevent customer confusion."
created: 2026-03-05 16:07
last_modified: 2026-07-03 11:44
lang: en-US
permalink: "https://help.cyberbiz.io/pos/check/customize-manager-price-override-display/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 網站外觀
  - 商品
sites:
  - TW
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - developer
difficulty: advanced
intents:
  - 修改店長改價顯示名稱
  - 隱藏店長改價權限字眼
features:
  - 店長改價
  - 訂單明細
  - Liquid 樣板編輯
prerequisites: []
related:
  - ec/website-appearance/code-customization/restore-code-theme-editor/
tags:
  - Manager_Price_Override
  - Order_Lookup
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - CSS/HTML 編輯器
paths:
  - 網站外觀 > 套版主題管理 > CSS/HTML 編輯器
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=26950
comments: false
search:
  exclude: false
icon: lucide/code-2
hide:
---

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

![Template editor screen](../../assets/images/ec-customers-order-liquid-hero.en.png){ title="Template editor screen" .hero-page }

## Change the Manager Price Override Name

The POS system supports the "Manager Price Override" feature, but consumers also see this discount detail when they look up orders online. **To prevent consumers from misunderstanding that manager permissions are high and demanding a discount, merchants can change the storefront display name by modifying the code (for example, to "Product Price Override").**

## Prerequisites and Limitations

-   **Responsibility**: CYBERBIZ provides public template code for merchants to modify on their own, but **does not provide syntax tutorials beyond this document or code writing services**. We recommend engaging a professional engineer.
-   **Recovery**: The template editor includes a "**View Previous Versions**" feature. [Revert to a previous version](../../ec/website-appearance/code-customization/restore-code-theme-editor.md#操作步驟){ title="Restore page code with the template editor " }.

## Steps

### Change the Path and File

1.  **Access the back office**: Go to **Website Appearance > Theme Setting > CSS/HTML Editor**.
2.  **Open the file**: In the editor, search for and click the **`customers/order.liquid`** file.

---

###  Change the Code Syntax

1. Find the syntax that displays the original name in the file:`<div class="text">{{type.name}}</div>`

2. Change it to the following conditional statement (using "Product Price Override" as an example):

	```liquid 
	if type.name == '店長改價' %}
	  <div class="text">商品改價</div>
	{% else %}
	  <div class="text">{{type.name}}</div>
	{% endif %}
	```

3. Screen after the change:

	``` liquid title="customers/order.liquid" hl_lines="7-11"
	<!-- 所有折扣 -->
	{% if order.discounts_info %}
	{% for type in line_item_discount.types %}
	  {% assign key = type.code %}
	  {% if order.discounts_info[key] %}
		<div class="price_item">
		  {% if type.name == '店長改價' %}
			<div class="text">商品改價</div>
		  {% else %}
			<div class="text">{{type.name}}</div>
		  {% endif %}
		  <div class="value">{{ order.discounts_info[key] | floor | money_without_currency_with_sign: negative: true}}</div>
		</div>
	  {% endif %}
	{% endfor %}
	{% endif %}
	```

---

## Result After the Change

1.  **Save the settings**: After the change is complete, click **Save**.
2.  **Storefront display**: When a consumer views order details through the "Order Lookup" page on the storefront, the original "Manager Price Override" discount item will be renamed to "**Product Price Override**".

![Storefront display after change](../../assets/images/pos-manager-price-override-frontend-result.en.png){ title="Storefront display after change" }


## Frequently Asked Questions

??? quote "What should I do if the storefront name does not change after the change?"

	This is usually caused by caching or syntax errors. Check the following items in order:

	- **Confirm the save**: After you edit in the CSS/HTML editor, make sure you click **Save** in the top-right corner.

	- **Cache impact**: Try opening an incognito window in your browser and viewing the order details page again.

	- **String matching**: Make sure the `'店長改價'` string in the code exactly matches the back office system's default characters, including full-width and half-width symbols.

??? quote "If I have both "Manager Price Override" and a regular discount, will this code affect other discounts?"

	**No.** This code uses an `{% if %}` conditional statement. It only replaces the name when the discount name exactly matches "Manager Price Override". Other discounts (such as spend-threshold discounts and promo codes) go through the `{% else %}` logic and keep displaying their original `{{type.name}}` content.

??? quote "Will modifying this file affect the display of POS checkout receipts (details)?"

	**No.** This tutorial modifies the `customers/order.liquid` file, which only affects the consumer order lookup page on the storefront. The POS interface and printed receipt formats are not affected by changes to this Liquid file.

??? quote "What if I accidentally break the code and the page goes blank? How do I fix it?"

	Don't worry. The CYBERBIZ template editor provides version management:

	1. In the top-right corner of the `customers/order.liquid` file, click **View Previous Versions**.
	2. Select a time point before the change and revert to it.
	3. Save again to restore normal functionality.
