---
title: Set VIP Member Exclusive Prices
description: Configure exclusive product prices for different VIP member groups.
product:
  - EC
module:
  - product
activ: ""
surfaces:
  - backend
devices: []
apis: []
type: tutorial
features: []
tasks: []
tnb: branch
plans:
  - Advanced
  - PLUS
  - Enterprise
lang: en
sites:
  - TW
status: doing
doc_next: ""
tags: []
difficulty: ""
notes:
  - doc-previous Set VIP Member Group link
---

# Set VIP Member Exclusive Prices :material-lock-outline:
Configure exclusive product prices for different VIP member groups.
{ .page-subtitle }

[:material-tag-text:](){ .badge-icon title="Available Plans" }[Advanced | PLUS | Enterprise](){ .badge-text }
[:material-arrow-left-circle:](){ .badge-icon title="Related Task"}[[Set VIP Member Group]]{ .badge-text }

---

## Overview
> Please make sure you have set up customer VIP groups before configuring member-exclusive prices.

=== ":material-information-outline: Notes"
	  - [ ] If a new VIP rule is published, make sure to reconfigure the member-exclusive prices to ensure the correct prices are applied.

=== ":material-lightbulb-outline: Use Cases"
	  - Set exclusive prices for different VIP groups.
	  - Manage VIP prices flexibly through single edit, bulk edit, or Excel import.
	  - Enable VIP promotion hints for non-logged-in visitors to encourage login for special offers.

---

## Operation Steps

### Set Member Exclusive Price (Single Product)
=== ":material-numeric-1-circle: Access the Settings Page"   
	  - [ ] Log in to your CYBERBIZ Admin Panel, then go to **Products → All Products**.
	  - [ ] Select the product you want to configure and go to the **Product Info** tab.  
	  - [ ] In the **Variant Management** section, click **Edit Member Price** to enter the “Edit Member Price” page.

	  <div class="grid cards two-columns" markdown>
	
	  - ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定01.png)
	
	  - ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定02.png)
	
	  </div>

=== ":material-numeric-2-circle: Select a Group"
	  - [ ] Choose the desired VIP group from the dropdown list.
	  - [ ] Click **Add Member Price** to add more group fields if you wish to set multiple group-specific prices for the same product.
	
	  ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定03.png)

=== ":material-numeric-3-circle: Edit Member Price"
	  - [ ] Click **Add Member Price**, select a VIP group, and click **Edit Price** to input the exclusive price.
	
	> Each variant can have a different price. If not specified, the system will use the product’s regular selling price by default.
	
	  ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定04.png)

=== ":material-numeric-4-circle: Delete Member Price"
	  - [ ] To remove a VIP group’s exclusive price, click **Remove** beside the field.
	  - [ ] Click **Delete** to confirm removal.
	
	  ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定05.png)

---

### Bulk Edit Member Exclusive Prices

=== ":material-numeric-1-circle: Select Products"
	  - [ ] Log in to your CYBERBIZ Admin Panel, then go to **Products → All Products**.
	  - [ ] Select the products you want to edit (single or multiple selection supported).
	  - [ ] Click the **Actions Menu** :material-arrow-down-drop-circle-outline:, then select **Edit Member Prices** to open the edit page.
	
	  ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定06.png){ .screenshot }

=== ":material-numeric-2-circle: Select Group"
	  - [ ] Choose the desired VIP group from the dropdown list.
	
	  ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定07.png){ .screenshot }
	
	=== ":material-numeric-3-circle: Edit Prices"
	  - [ ] Click **Add Member Price**, select the VIP group, and input the exclusive price.
	  - [ ] To delete a VIP group price field, click **Remove** beside the field.
  
    > Each variant can have a different price. If not specified, the system will use the product’s regular selling price by default.
	
	  ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定08.png){ .screenshot }

---

### Import or Edit Member Prices via Excel

=== ":material-numeric-1-circle: Export Products"
	  - [ ] Log in to your CYBERBIZ Admin Panel, then go to **Products → All Products**.
	  - [ ] Click the **Actions Menu** :material-arrow-down-drop-circle-outline:, then select **Export Member Prices**.
	
	  ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定09.png){ .screenshot }

=== ":material-numeric-2-circle: Edit Excel File"
	  - [ ] The system will send an Excel file to your registered email address.
	  - [ ] Download and open the Excel file, then fill in the exclusive prices in the corresponding columns. Save the file after editing.

	  ![[圖示-會員專屬價格設定11.png]]

=== ":material-numeric-3-circle: Import Excel File"
	  - [ ] Return to **Products → All Products** in the Admin Panel.
	  - [ ] Click the **Actions Menu** :material-arrow-down-drop-circle-outline:, then select **Import Member Prices**.
	  - [ ] Upload the edited Excel file and click **Confirm**.

	  ![[圖示-會員專屬價格設定12.png]]

=== ":material-numeric-4-circle: Confirm Import Success"
	  - [ ] Once the upload is successful, the system will send a confirmation email to your inbox.
	
	  ![[圖示-會員專屬價格設定13.png]]

---

## Advanced Settings

#### Show VIP Tag for Non-Logged-in Visitors
This feature reminds unregistered or logged-out users that logging in as a VIP member can grant them access to special pricing.

- [ ] Log in to your CYBERBIZ Admin Panel, then go to **Website Appearance → Theme Management → Website Settings**.
- [ ] Switch to the **Product Page** tab and find the **Basic Settings** section.
- [ ] Enable **Show Member Price Tag**.  
  If disabled, non-logged-in visitors will not see any tag hint on the product page.
- [ ] In the **VIP Tag Link** field, you can set a URL leading to the login or sign-up page to guide users to register.

![Member Price Tag Setting](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定14.png){ .screenshot }

---

### Display for Logged-in Members
When a logged-in customer belongs to a VIP group with an exclusive price set for a product, the product page will display the special price along with the member’s VIP group name.

=== "Feature Disabled"
	  ![[圖示-會員專屬價格設定-未開啟功能.png]]

=== "Feature Enabled - User Not Logged In"
	  The product page displays a login/register link.
	
	  ![[圖示-會員專屬價格設定未登入畫面.png]]

=== "Feature Enabled - User Logged In"
	  The product page shows the member’s group level.
	
	  ![[圖示-會員專屬價格設定開啟功能登入畫面.png]]

---

## FAQs

??? question "How will the product page display after setting member-exclusive prices?"
    === ":material-alert-circle-outline: Cause"
        When a member logs in, if their VIP group has a special price set, the product page will display that exclusive price.  
        If not logged in, the regular price is shown by default.  
        You can enable the **Non-logged-in VIP Tag Display** feature to hint customers to log in for discounts.
    === ":material-lightbulb-on-outline: Solution"
        - **Logged-in members:** The system automatically displays the VIP price.  
        - **Non-logged-in visitors:** Enable the **Non-logged-in VIP Tag Display** and link it to the login/register page.

??? question "If a product has multiple VIP group prices, how does the system decide which one to display?"
    === ":material-alert-circle-outline: Cause"
        The system usually prioritizes the highest VIP level or follows an internal hierarchy to determine which price is shown.
    === ":material-lightbulb-on-outline: Solution"
        Please refer to official CYBERBIZ documentation or contact customer support to confirm the price priority logic among multiple VIP groups.

---

## Related Resources
=== ":material-page-previous-outline: Linked Documents"

=== ":material-page-next-outline: Navigation"
	  - [[Set VIP Member Group]]

=== ":material-update: Related Updates"

=== ":material-book-outline: Related Terms"

=== ":material-map-outline: Related Diagrams"

- [[Set Multi-level Product Categories]]
- [[Product Group: Limited-time Discount for Single Items]]
