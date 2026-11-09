---
title: "Set up Google Shopping Ads"
author: ""
reviewers: []
last_modified: 2026-03-11 12:18
description: "Connect Google Merchant Center and sync product data to Google Search and Shopping ads."
products:
  - EC
modules:
  - 第三方整合
acoiv: configure
paths:
  - 第三方整合 > 谷歌 Google 設定 > Google Merchant Center
  - 商品 > 所有商品 > 設定
devices:
  - desktop
  - mobile
apis: []
type: guide
intents:
  - 串接 Google Merchant Center
  - 同步商品資料至 Google 搜尋
  - 投放 Google 購物廣告
features:
  - 商品動態饋給 (Product Feed)
  - Google 產品類別設定
  - GMC 與 Google Ads 帳戶關聯
tnb: ""
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
prerequisites:
  - 擁有 Google 帳戶
  - 商品圖片符合 Google 規範
lang: en-US
sites:
  - TW
tags:
  - Google
  - GMC
  - "Shopping ads"
difficulty: intermediate
audiences:
  - merchant
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=718
  - https://www.cyberbiz.io/support/?p=230
notes:
  - verify FAQ
  - update internal links
comments: ""
search:
  exclude: false
icon: lucide/shopping-cart
permalink: "https://help.cyberbiz.io/resources/backups/articles/設定 Google 購物廣告/"
---


# Set up Google Shopping Ads
Connect Google Merchant Center (GMC) and sync product data to Google Search and Shopping ads.
{ .subtitle }

![](../../../assets/images/ec-integrations-gmc.zh-tw.en.png){ title="Connect GMC: Integrations > Google > Google Merchant Center" .hero-page }


## Benefits of Connecting GMC

Google Merchant Center (GMC) is Google's product-data upload and management platform. It connects your catalog to the Google ecosystem (such as Google Search and Google Shopping ads) to improve product reach, ad performance, and conversion efficiency, with automated management.

- **More product reach**: Products appear in the Shopping section of Google Search results and get more potential shopper views.
- **Precise ads**: Promote products with Google Ads, target the right audience, and improve conversion.
- **Automated management**: Sync inventory, price, and images automatically to cut manual upkeep.
- **Tracking and optimization**: Collect engagement and ad performance data for later analysis and tuning.

## Set Product Data Sync Options

Before connecting Google Merchant Center, set the related fields in the CYBERBIZ admin so product data reaches GMC correctly.

1. Sign in to the CYBERBIZ admin and go to **Third-Party Integration > Google**。
2. In the **Google Merchant Center** block, set product sync options:
	- Expand by variant: choose whether every product variant is sent to GMC.  
    > On: best when every variant should appear on its own (for example, apparel or shoes in different colors or sizes).  
    > Off: best when only the main product image is needed (for example, electronics, appliances, or laptops).
	
		!!! tip "Best practice"
			If products have multiple variant attributes, turn on *Expand by variant* so each option appears separately on Google and gets more reach.
			
	- Product image selection: choose which image GMC uses as the product image (first or last).
	> To keep ads running, make sure product images meet [Google product data specifications](https://support.google.com/merchants/answer/6324350)。

		<div class="grid cards two-columns borderless" markdown>
		
		:material-check-circle: Compliant: no watermark
		![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC03-1.png){ .screenshot }

		:material-close-circle: Not compliant: has a watermark
		![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC02-1.png){ .screenshot }

		</div>
	
1. Click **Update catalog manually** to refresh now, or let the system update automatically daily at 1:30 AM.

## Set Google Product Categories

To place products in better search results, set Google product categories manually. Choosing the category yourself improves ad targeting and performance tracking.

1. Sign in to the CYBERBIZ admin and go to **Products > All Products**。
2. Open the product you want to edit, then click the **Settings** tab.
3. In **Google product category**, choose the matching category.
> If you skip manual setup, Google assigns a category automatically, which may not match the product well.  
> Pick from Google's existing category list. You cannot rename or add categories, and batch apply is not available yet.

    ![](../../../assets/images/ec-google-product-category.zh-tw.en.png)

4. After setup, check results under **Product feed link**.
	- In the CYBERBIZ admin, go to **Third-Party Integration > Google**。
	- In the Google Merchant Center block, find **Product feed link**, copy it, and paste it into the browser address bar to download the product feed file.

	![](docs/assets/images/ec-product-dynamic-feedback-link.zh-tw.en.png)

## Apply for a GMC Account

!!! warning "Notes"
    To run Google automated ads, create a [CYBERBIZ-managed GMC account](../../../ec/integrations/google/automated-ads-system.md#cyberbiz-代管適合新手) on the automated ads setup page and configure ads there. You do not need a separate GMC account. This avoids ad delivery issues from manual GMC permission changes.

1. Open [Google Merchant Center :material-open-in-new:](https://www.google.com/retail/) and click **Get started**.
> You need a Google account email and password to create a GMC account, and each email can create only one.

2. Set the following information in order.

    === "Add a business address"

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC03-1024x504.png){ .screenshot }

    === "Confirm your online store"

        1.  Enter your online store URL.
        2.  Choose **Add an HTML tag or file**.
        3.  Choose **Add an HTML tag**.
        4.  Copy the **HTML tag generated for your online store**.
        5.  Sign in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > 選擇操作「CSS/HTML 編輯器」>「theme.liquid」**。
        6.  Paste the HTML tag above `</head>`.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC06-1-1024x696.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/GOOGLE購物廣告設定GMC09-1-1024x508.png){ .screenshot }

    === "Add product shipping methods"

        Enter merchant shipping details as prompted.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC07-1024x486.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC08-1024x486.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC09-1-1024x485.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC10-1024x486.png){ .screenshot }

    === "Add a return policy"

        Enter the merchant return policy as prompted.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC11-1024x504.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC12-1024x504.png){ .screenshot }
        ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC13-1024x504.png){ .screenshot }

    === "Add products"

        1. Select country/region: choose where the products apply.

            ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC14-1024x504.png){ .screenshot }

        ２. Copy the product feed link.
        > In the CYBERBIZ admin, go to **Third-Party Integration > Google > Google Merchant Center** and copy **Product feed link**.

            ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC16-1024x490.png){ .screenshot }


        3. Paste the link.
	        - Return to the GMC admin and choose **Add products from a file**.
            - Paste **Product feed link** into **Enter a file URL**.

            ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC15-1024x504.png){ .screenshot }

3. After upload finishes, check the completion screen on the products page.
> Upload time depends on product count—wait a moment.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/串接GMC17-1024x486.png){ .screenshot }

## Products Excluded from GMC Upload

The system automatically excludes these three product types from Google Merchant Center.

| Product type      | Description                          | Upload to GMC          |
| --------- | --------------------------- | ---------------- |
| Private products    | Product visibility set to *eye closed* :material-eye-off:| :material-close: |
| Products past unpublish time | Unpublish time is set; product is excluded automatically            | :material-close: |
| Tag-excluded products    | Product tags set to `贈品` or `排除product feed`:lucide-asterisk:<br> :lucide-triangle-alert: Do not add a space between *exclude* and *product* | :material-close: |

!!! info "Products tagged `贈品` or `排除product feed` also do not appear in Google Search results. Learn more about [exclusion tag settings](../../../ec/products/categories-and-tags/manage-product-tags.md#operate-product-tags-exclude)。"

## Link GMC to a Google Ads Account

1. Sign in to your Google Merchant Center account.
2. In the left navigation, click **設定 > 存取權和服務 > 應用程式和服務**。
3. Click **Add service**, then select **Google Ads**.
4. Choose the Google Ads account to link.
5. Confirm the link details, then click **Link**.

![](../../../assets/images/ec-gmc-connect-google-ads.zh-tw.en.png)

## FAQ

??? quote "How does a CYBERBIZ-managed GMC account differ from one I create myself?"
    With a CYBERBIZ-managed GMC account, the system handles setup and maintenance so manual permission changes do not break ads. If you already created ads on the automated ads page with managed hosting, do not apply for a separate GMC account.

??? quote "Which products are not uploaded to the Google product feed?"
    The system excludes private products, products past unpublish time, and products tagged *gift* or *excludeproduct feed*.

??? quote "Can I batch-set Google product categories?"
    Google product categories must be set per product today; batch apply is not available.

## Further Reading

- [Exclusion tag settings](../../../ec/products/categories-and-tags/manage-product-tags.md#operate-product-tags-exclude)
