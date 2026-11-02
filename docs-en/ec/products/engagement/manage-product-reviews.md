---
title: "Manage Product Reviews"
description: "Turn on and manage product reviews."
created: 2026-03-05 16:00
last_modified: 2026-10-07 17:10
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
  - 網站外觀
  - 會員
sites:
  - TW
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 設定商品評論功能
  - 審核顧客留言
  - 提升商品信任度
  - 評論獎勵設定
features:
  - 商品評論
  - 紅利點數贈送
  - Google reCAPTCHA
  - 樣板編輯器
prerequisites:
  - "Contact customer service to enable product reviews first"
related:
  - ec/website-appearance/customer-interaction/enable-comment-recaptcha/
tags:
  - "Product Reviews"
  - "Customer Feedback"
  - "Comment Management"
  - "Brand Trust"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 留言板
  - CSS/HTML編輯器
  - 彈跳視窗
paths:
  - 會員 > 商品待審核評論
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7894
  - https://www.cyberbiz.io/support/?p=30610
permalink: "https://help.cyberbiz.io/ec/products/engagement/manage-product-reviews/"
comments: false
search:
  exclude: false
icon: lucide/message-square-quote
hide: []
---
# Manage Product Reviews
Enable and manage product reviews.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

![Manage product reviews](../../../assets/images/ec-product-review-hero.zh-tw.en.png){ title="Manage Product Reviews" .hero-page }

## About Product Reviews

Product reviews let customers post star ratings and comments on product pages. You can approve, edit, or delete reviews in the admin and encourage customers to share their shopping experience with bonus points rewards. Together with [Google reCAPTCHA](../../website-appearance/customer-interaction/enable-comment-recaptcha.md){ title="Enable reCAPTCHA for Comments" }, you can effectively prevent spam, build trust in your products, increase conversions, and collect genuine customer feedback.


<div class="grid cards borderless two-columns" markdown>

- ![Product reviews section on the product page](https://www.cyberbiz.io/support/wp-content/uploads/商品評論00.png){ title="Product Reviews Section on the Product Page" }
- ![Product review prompt](https://www.cyberbiz.io/support/wp-content/uploads/商品評論00-1.png){ title="Product Review Prompt" }

</div>


??? info-clean "Product Review Flow"

    ```mermaid { data-search-exclude }

    %%{init: {
      "logLevel": "debug",
      "theme": "base",
      "gitGraph": {
      "showBranches": true,
      "showCommitLabel": true,
      "mainBranchName": "Merchant"
      }
    }}%%
    gitGraph
      commit id: "Launch products"
      commit id: "Enable product reviews" tag: "Contact customer service" type: HIGHLIGHT
      commit id: "Set up reviews" 
      branch "Customer"
      checkout "Customer"
      commit id: "Customer posts a review"
      checkout "Merchant"
      merge "Customer" id: "Review product reviews"
      commit id: "Edit"
      commit id: "Approve"
      checkout "Customer"
      merge "Merchant" id: "Show reviews on storefront"
      checkout "Merchant"
      merge "Customer" id: "Delete" type: REVERSE

    ```

## Prerequisites and Limits

- [x] Contact customer service to enable product reviews first.
- [x] FB sharing: Available only after you fill in "Third-Party Integration" → "Facebook Settings" → "Set the App ID and App Secret".


## Steps

### Set up Product Reviews { #manage-product-reviews }

After you go to **Website Appearance > Product Reviews Management**, the top of the page has two separate sections, [System Setting](#System-Setting) and [Give After Approval](#Give-After-Approval). Each has its own **Update** button, so save each section separately after making changes.

#### System Setting

1. Log in to the CYBERBIZ e-commerce admin and go to **Website Appearance > Product Reviews Management**.
2. In the **System Setting** section, adjust the following as needed:
    - **Comment Needs Approval**: When on, reviews submitted by customers appear on the storefront only after you approve them manually[^1].
    - **Default Hide Partial Username**: When on, reviewer names are partially hidden on the storefront.
    - **Google reCAPTCHA**: Turn on security verification to block bots and spam, and enter the **reCAPTCHA sitekey** and **reCAPTCHA secretkey** below. Learn [how to set up reCAPTCHA for comments](../../website-appearance/customer-interaction/enable-comment-recaptcha.md){ title="Enable reCAPTCHA for Comments" }.
3. Click **Update** in the **System Setting** section to apply the changes.

[^1]: This setting applies only to comment boards created later and doesn't affect existing comment boards.

![System Setting](../../../assets/images/ec-product-review-system-settings.en.png)

---

#### Give After Approval

Set the reward given automatically to a customer after you approve their review in **Customer Management > Product Reviews**. You can give bonus points only, or add a coupon as well.

1. Set the **bonus points** to give:
    - **Bonus points**: Enter the points to give after approval. Enter 0 to give no bonus points.
    - **Bonus points validity period**: The number of days each set of bonus points is valid. Enter 0 for no expiration.
2. To add a coupon as well, turn on the **Coupon** toggle and complete the following settings:
    - **Coupon name (required)**: The name customers see in their coupon list.
    - **Discount Type**: Select **Price** or **Percentage**[^2].
    - **Coupon discount (amount/percentage)**: Enter the discount amount (NT$) or discount percentage.
    - **Spending Threshold**: The order amount (NT$) must reach this threshold for this coupon to be used.
    - **Usage Limit per Account**: Select **Unlimited**, or select **Specific Number of Uses** and enter how many times each account can use it.
    - **Validity Period**: Select **Unlimited**, **Valid Days** (counted from the date received), or **Valid Date Range** (a specified start and end date).
    - **Link to product tags**: Limit the product tags the coupon can be used for. If none is selected, products are not limited.
    - **Campaign Combination Restrictions**: Select **Unrestricted**, **Combine coupon with campaigns other than the specified ones**, or **Do not use this coupon with specified campaigns**. If you select one of the last two, specify the campaigns to restrict.


3. Click **Update** in the **Give After Approval** section to apply the changes.

[^2]: Enter percentages as 2 digits. For example, 90% means 10% off, and 10% means 90% off.

![Give after approval settings](../../../assets/images/ec-product-review-reward-settings.en.png)

---

### View Comment Boards
You can configure every product's comment board in detail here. Click **View** to edit an individual comment board.

![Comment board list](../../../assets/images/ec-comment-board-list.zh-tw.en.png){ title="Comment Board List" }

---

### Set up a Comment Board
In the comment board list, click "View" on a comment board to open its edit page and configure it. Click the **trash can :material-trash-can-outline:** to delete a product review.

![Comment board settings](../../../assets/images/ec-comment-board.zh-tw.en.png){ title="Comment Board Settings" }

---

### Post a Product Review <small>Customer</small>

!!! info "Customers must log in as members to post reviews on product pages."

1. On the product page, the customer clicks **Write a Review**.
2. A pop-up window opens where the customer can enter a star rating and review.

![Post a review on the storefront](../../../assets/images/ec-product-review-frontend.zh-tw.en.png){ title="Post a Review on the Storefront" }

---

### Approve Product Reviews

You can approve product reviews submitted by customers in the admin.

1. Log in to the CYBERBIZ admin and go to **Customer Management > Product Reviews**.
2. Choose an approval action.
	- **Approve**: Show the review on the storefront. Approved reviews are published.
	- **Delete**: Delete the review.  
	- **Edit**: Change the review content to adjust or correct it.  

![Approve product reviews](../../../assets/images/ec-product-review-approval-pending.zh-tw.en.png){ title="Approve Product Reviews" }

---

### Hide Product Reviews

!!! warning "If you remove the code yourself, CYBERBIZ will not help restore it."

If you don't want to show product reviews for now, you can hide them with the Template Editor.

=== "Drag-and-Drop Theme"

	１. Log in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > Actions: CSS/HTML Editor**.
	2. In the "Sections" menu, click "Add Block". Name the new block `board_comments.liquid`.
	3. Click to open the new `board_comments.liquid` block file.  
    4. Leave the file content (the area on the right) empty to hide product reviews. To restore product reviews, click :material-trash-can-outline: to delete the `board_comments.liquid` file.

	![Hide product reviews](../../../assets/images/ec-template-editor-board_comments.liquid.zh-tw.en.png){ title="Hide Product Reviews" }

=== "Standard Theme"

	1. Log in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > Actions: CSS/HTML Editor**.

	2. Search for and open the `product.liquid` file, and find the `shop.plugins.board_comments` code.  
	3. Wrap the whole code block in the HTML comment markers `<!--` and `-->` to *comment out the code*. This disables and hides product reviews without deleting the code.

	4. Click **Save** to apply the update.

    ![Hide reviews in the standard theme](https://www.cyberbiz.io/support/wp-content/uploads/商品評論07.png){ title="Hide Reviews in the Standard Theme" .screenshot }

## Next Steps

<div class="grid cards" markdown>

- [__Enable reCAPTCHA for Comments__](../../website-appearance/customer-interaction/enable-comment-recaptcha.md){ title="Enable reCAPTCHA for Comments" }  
  Prevent bot messages and spam comments.

</div>

## FAQ

??? quote "Do customers need to log in to post reviews?"
    Yes. Customers must log in as members to post product reviews.

??? quote "If I remove code from the Template Editor myself, will CYBERBIZ help restore it?"
    If you remove code from the Template Editor yourself, CYBERBIZ does not provide restoration or similar help. Be sure to keep a backup of the code.
