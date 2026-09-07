---
title: 設定紅利點數
description: 透過紅利點數建立會員回饋機制，吸引新客首購並提升舊客回購率。
created: 2026-05-27 15:20
last_modified: 2026-06-30 10:56
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 行銷活動
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定紅利回饋
  - 手動發送紅利
  - 調整紅利兌換比例
  - 處理退貨紅利
features: 
  - 紅利點數
  - 消費回饋
  - 批次發送紅利
prerequisites: []
related: 
  - "[[設定註冊禮]]"
  - "[[設定生日禮]]"
  - "[[紅利商城設定]]"
tags: 
  - 紅利點數
  - 購物金
  - 行銷活動
  - 會員經營
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 紅利設定欄位
  - 會員列表
paths: 
  - 行銷活動 > 全館折扣-紅利 & 優惠券 > 會員紅利點數
  - 金物流 > 結帳頁 & 物流設定 > 訂單相關設定 > 訂單取消退貨相關紅利設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3805
  - https://www.cyberbiz.io/helpcenter/?p=3807
  - https://www.cyberbiz.io/helpcenter/?p=3812
  - https://www.cyberbiz.io/support/?p=42367
  - https://www.cyberbiz.io/support/?p=6103
permalink: https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-bonus-points
comments: false
search:
  exclude: false
icon: lucide/coins
hide: []
---

#  Set Bonus Points
Establish a membership reward mechanism through bonus points to attract new customers for their first purchase and increase the repurchase rate of existing customers.
{ .subtitle }

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-設定會員紅利點數01.png){ .hero-page }

!!! tip " Application Scenarios "
	-  **Enhance Loyalty**: Set up consumption rewards so that customers can get points after each purchase, increasing the incentive to return.
	-  **Holiday Promotions**: store-wide Send bonus points to create a sense of urgency for limited-time shopping.
	-  **Compensation or Rewards**: Manually send points to specific members as customer service compensation or exclusive event rewards.


## Instructions for Use

-  **Calculation Basis for Bonus Points Distribution**: Bonus points are calculated based on the checkout amount "excluding shipping costs".
-  **Effective Time**: Modifying the bonus distribution rules only applies to actions taken "after setting" and does not affect points already distributed.
-  **Import Restrictions**: Once bonus points are distributed or deleted, the system cannot automatically recall or restore them; please operate with caution.
-  **Account Settlement Time**: Bonus points will only be officially credited to the member's account for their use after the order status changes to "Closed".


## Operating procedures
Log in to the CYBERBIZ management backend (
> 1. ) and go to **Marketing Activities store-wide Discounts - Bonuses & Coupons**. Find the **Member Bonus Points (Vouchers)** section in the dropdown menu and switch the function to `開啟`. Set the core parameters: **Bonus Conversion**: Set `X 點 = NT 1` (default is 1:1). **Minimum Spending Threshold**: The minimum order amount required to use bonuses. **Bonus Distribution for Valid Orders from Other Channels**: Whether to send bonuses when manually adding [Valid Orders from Other Channels] (../../members/manage-member-profiles.en.md#2-其他通路訂單) to a member. **(Enterprise Edition Only)**
    -  **Single Order Discount Limit**: Can be set as a fixed amount or a percentage of the order amount. **(PLUS & Enterprise Edition Only)**
    -  **Bonus point is valid for:**: Sets the number of days points are valid (0 means never expires).
    >  This period setting also applies to "Registration Gift Bonuses".

   ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-store-wide折扣-設定會員紅利點數01.png){ .screenshot }

## Bonus delivery method

### A. Site-wide spending rewards (automatically sent)

sets a "spending threshold" and "bonus points" in the **Member Bonus Points (Vouchers)** section.

-  **Example**: Sets a bonus of 10 points for every 100 yuan spent.
-  **Logic**: The system accumulates points proportionally. Spending 1000 yuan earns 100 points; spending 999 yuan earns 90 points.

### B. store-wide sent (to all members)
On the same page, click **Send vouchers to every member** to expand the fields. Enter the points, duration, and sending name, then click **Confirm Add**. The system will automatically transfer the points to all registered member accounts.### C. Send manually (to specific members)

> Go to **Members All Members**.

=== " Send Single. "

     Go to a specific member's personal page, and select **Add Bonus Points** in the "Bonus Points" section.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數-4.png){ .screenshot }

=== " Send Filtered. "

     Use the filter to select a specific group (e.g., VIP members) and add points in batches.

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數-7.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數-8.png){ .screenshot }

    </div>


### D. Batch sending in Excel

!!! info " Usage Instructions "
    -  This function is only available for the **Enterprise Edition**.
    -  If the merchant has **enabled external bonuses**, batch bonus import cannot be used. If you need to send bonuses, please operate directly in your external middleware system.
    

1.  Download the template and fill in the fields according to the specifications provided in the template.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-紅利優惠券-批次發送紅利點數01.png){ .screenshot }

2.  Enter the member's email or mobile phone number, the specified activity name, the expected bonus to be sent, etc.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EXCEL範本-批次發送紅利點數01.png){ .screenshot }

3.  Upload Excel. The system will send an email notification of the import result, and immediately send the bonus to the designated member after successful import.



## Set a maximum discount limit for each product.

You can set a bonus redemption cap for individual products. **To enable bonus redemption for this product, please enter the number of points that can be redeemed.** **If this field is left blank with 0, it means that the product is not eligible for bonus redemption.**

> 1.  Go to **Products All Products** and select the desired product.
2.  Go to **Style Management** and enter the maximum number of points that can be redeemed for this style in the **Bonus Redemption** field.
>  **System Judgment Logic**: When both the "store-wide Redemption Cap" and the "Product Redemption Cap" exist, the system will apply the **stricter** (lower value) restriction. How to batch modify this field in

!!! tip "? You can [export a large number of product Excel spreadsheets](../../products/bulk-operations/batch-update-product-descriptions-shipping.en.md#匯出商品-excel-表格), edit the `商品款式紅利最高折抵` field, and then [import an Excel file](../../products/bulk-operations/batch-update-product-descriptions-shipping.en.md#上傳-excel-檔案) to complete the batch editing. Background settings screen "

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明02.png) { .screenshot }

=== " Front-end checkout screen "

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/設定紅利購物金說明03.png) { .screenshot }

## The checkout page automatically includes the bonus.

System default setting: **Enable** automatic display of member bonuses on the checkout page. Merchants can set whether the system automatically displays the member's current maximum available bonus points when the member enters the checkout page.

> 1.  Go to **Jin Logistics Checkout Page & Logistics Settings**.
2.  Expand the **Shopping Cart Settings** section and find **Auto-apply Member Bonus on Checkout**.
3.  Select the setting according to your needs:
    -  **Enable Auto-apply Member Bonus on Checkout** (System default): The checkout page will automatically display the member's maximum available bonus points, but members can still manually enter the bonus points they wish to use.
    -  **Disable Auto-apply Member Bonus on Checkout**: After closing the checkout page, the available member bonuses will not be automatically loaded. The "Please Enter Member Bonus Points" field will default to `0`, requiring members to manually enter the bonuses they wish to use.

=== " Backend Settings Screen "

    ![](../assets/images/EC-後台-金物流-結帳頁物流設定-結帳頁自動帶入紅利01.png){ .screenshot }

=== " Frontend Checkout Screen "

    ![](../assets/images/EC-前台-結帳頁-會員紅利折抵欄位01.png){ .screenshot }

## System Logic Description

### Discount application order

bonus points are deducted **after all other discounts and offers**. This means the system will calculate all promotions and coupons first, and then deduct bonus points last.

### Cancel processing

Merchants or consumers can cancel orders before they are shipped. The system's bonus processing rules for canceled orders are as follows:

| Scenario | Bonuses used in the order | Bonuses earned from consumption |
| :--- | :--- | :--- |
| **Order cancellation** | Automatically returned to the consumer's account | No reward sent if the order has not been closed <br> No deduction if the order has been closed and points have been used |


### Returns
Merchants can customize the bonus handling rules for returns:

| Scenario | Bonuses used in the order | Bonuses earned from purchases |
| ---- | -------------- | ------------- |
| **Returned Orders** | Option to refund (default: no refund) | Do not send bonuses upon settlement |
| **Partially Returned Orders** | Option to refund (default: no refund) | Option to send bonuses (default: no send) |

!!! info " Applicable Versions: "
    -  **Returned Orders** A switch can be set to indicate whether the order is returned; only available for **PLUS and Enterprise Editions**.
    -  **Partially Returned Orders** A switch can be set to indicate whether the order is returned; only available for **Enterprise Editions**.

> Please go to **Jin Logistics Checkout Page & Logistics Settings > Order Related Settings** to make the settings.

![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明17.png){ .screenshot }

### Return of goods will be processed after the case is closed.

If a return is made after the order has been closed, the bonus points earned from the purchase will **not be automatically deducted from the member's account**.

!!! tip " Recommended Operation "
    -  Merchants need to go to the member's personal page to [manually delete the bonus](../../members/manage-member-profiles.en.md#1-紅利點數派發與管理).
    -  It is recommended to wait until the order's return period has passed and confirm that there is no longer a need for a return before clicking **Close Order** to ensure the accuracy of bonus distribution.


!!! warning " Note for cross-warehouse merchants "
     This automatic return function is not supported for cross-warehouse merchants. When cross-warehouse orders are returned, the system will not automatically return or send bonus points.



## Management and Analysis

### Check bonus points
> Merchants can view, add, or delete individual members' bonus points in the backend. Go to **Members All Members**, search for and click on the specified member. View the **bonus points list** on that member's profile page.
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明08.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明09.png){ .screenshot }

=== " Member Terminal "

     Members can check their point records on the official website.

    > 1.  Go to **My Account Bonus Points**.
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/08/購買指定商品送紅利13.png){ .screenshot }

### Bonus Points Exchange Rate
The
system will automatically calculate and display the corresponding amount based on the set ratio:

#### Instructions for Use

-  This feature is only available for the **Enterprise Edition**.
-  The exchange rate only applies during "Bonus Credit".
-  If the merchant changes the conversion rate, it will directly affect the discounted value of existing bonuses in the consumer's account.

#### Front-end display example

-  **Member Center**: Displays available points and approximate equivalent value.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明10.png){ .screenshot }

-  **Product Page**: Displays the maximum points that can be redeemed for this product and its approximate equivalent value.

    >  When setting the "Bonus Points Redemption Limit" for a product in the backend, enter **points** instead of monetary value.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明11.png){ .screenshot }

-  **Checkout Page**: Displays the redeemed points and the actual amount deducted.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明12.png){ .screenshot }


#### Report export fields
When exporting orders (
), detailed fields for bonus discounts and amount conversions will be displayed simultaneously:

-  **Bonus Discount**: Unit is bonus points.
-  **Total Product Bonus Discount**: Actual discount amount after currency conversion of bonus points.

![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明13.png){ .screenshot }



### Query and export reports

> 1.  Go to **Analysis Reports Marketing Campaign Analysis > Bonus Analysis**.

2.  Click **Export Bonus Chart**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明14.png){ .screenshot }

3.  The system will send an Excel report to the administrator's email address.

    >  The export period cannot exceed 180 days.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/設定紅利購物金說明16.png){ .screenshot }


## More operations

<div class="grid cards" markdown>

- :lucide-bell-ring:{ .lg }
  [__Set Bonus Points Expiration Notification__](../purchase-restrictions/coupon-and-bonus-points-expiry-notification.en.md)
   Set bonus points expiration reminders to guide customers back to the official website to redeem points before they expire.

</div>
