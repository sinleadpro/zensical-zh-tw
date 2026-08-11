---
title: 設定 VIP 專屬優惠
description: 設定 VIP 會員專屬折扣、紅利獎勵與差異化定價，並掌握與全館行銷活動的併用規則。
created: 2026-01-23 00:00
last_modified: 2026-07-14 17:10
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 會員
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: branch
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 如何設定 VIP 專屬優惠
  - VIP 會員優惠設定
features:
  - VIP 優惠
  - 會員專屬價格
  - 紅利倍數
prerequisites: []
related: []
tags:
  - VIP
  - 會員
  - 優惠
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > VIP 設定
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7498
  - https://www.cyberbiz.io/support/?p=12426
permalink: https://help.cyberbiz.io/ec/members/vip/setup-exclusive-vip-discounts
comments: false
search:
  exclude: false
icon: lucide/ticket
hide: []
---
# Set Up Exclusive VIP Benefits

Set up exclusive discounts, bonus rewards, and differentiated pricing for VIP members, and master the rules for using them in conjunction with store-wide marketing activities.

{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | Expert / All PLUS / Enterprise

{ .doc-badge }

![](../../../assets/images/EC-後台-會員-VIP設定-優惠設定01.en.png){ .hero-page }

The core appeal of the VIP system lies in its "sense of prestige" and "tangible rewards." The new VIP system offers a variety of benefit combinations to help you design differentiated benefits that members will appreciate.

## VIP discounts and rules
When setting up VIP offers, please define the rules for combining the offer with designated marketing activities. The system provides three different strengths of stacking logic:

- **Unrestricted**

     VIP offers can be directly stacked with all activities.

- **Combined with other activities (product-level exclusion)**

     If a single product already enjoys a selected activity discount, that product will not enjoy the VIP offer; other products in the order that are not participating in activities will not be affected.

- **No discount during activities (order-level exclusion)**

     If the shopping cart contains any product eligible for a selected activity, the entire order will have its VIP offer completely canceled.

When setting up various offers, if you encounter a section on **Rules for combining with other marketing activities**, please refer to the instructions here to select the appropriate logic.

![](../../../assets/images/EC-後台-會員-VIP設定-與其他行銷活動的併用規則01.en.png){ .screenshot }

!!! info "Bonus Points Enable Switch"

     To award bonus points, please go to **Marketing Activities > store-wide Discounts - Bonuses & Coupons**, and [Enable Bonus Points Function](../../marketing/bonus-and-gifts/setup-bonus-points/#操作流程).

## 1. Enjoy discounts
1. Enter the **specified discount**. This VIP member will enjoy a specified discount on their entire order.

    > Set the discount value to 1-99. For example, 90 represents a 10% discount, and 70 represents a 30% discount.

2. **Set the rules for using this rule with other marketing activities**
            
     First, select [**Use Logic**](#vip-優惠併用規則), then select the marketing activities from the list to which you want to apply this rule.

     supports the following marketing campaigns with matching rules:

    

     - Member Exclusive Pricing

     - Single Item Discount

     - Red & Green (Combination Discount)

     - Optional Discount

     - Multi-level Product Category Discount (Advanced Product Category Discount)

     - store-wide Discount

![](https://www.cyberbiz.io/support/wp-content/uploads/VIP優惠01.png){ .screenshot }

## 2. Free shipping on orders.
1. Enter the **Free Shipping Threshold**. VIP members who reach the threshold will enjoy free shipping on their entire order.

2. **Set Rules for Using with Other Marketing Activities**

            

     First, select [**Use Logic**](#vip-優惠併用規則), then select the marketing activities from the list to apply this rule to.

     Marketing activities that can be bound to use rules:

    

     - Member Exclusive Price

     - Single Item Discount

     - Red & Green (Combination Discount)

     - Optional Discount

     - Multi-level Product Category Discount (Advanced Product Category Discount)

     - store-wide Discount

![](https://www.cyberbiz.io/support/wp-content/uploads/VIP優惠02.png){ .screenshot }

## 3. Bonus multiplier setting

### Instructions for Use
* **Stacked Bonus:** If you have set up both "store-wide Bonus" and "VIP Extra Bonus" simultaneously, members will **receive both** when placing an order.

### Setting method
Enter the **spending threshold, bonus amount, and validity period**. This VIP tier member will receive extra bonus points after placing an order.

![](https://www.cyberbiz.io/support/wp-content/uploads/VIP優惠03.png){ .screenshot }

## 4. Birthday Gift Setup

### Send Schedule
- **Sending Time**: The system defaults to sending the monthly birthday gift on the 1st of each month.

- **Early Sending**: You can customize **sending the birthday gift N days in advance**.

    
    : Sending the gift depends on the member's current level. If the sending time is earlier than the member's Upgrade date, the member will not receive the birthday gift for levels after Upgrade. You can manually send the birthday gift to the member according to the store's VIP policy.

    !!! example "Scenario Example"
        : Customer A's birthday is in May, and they reached VIP1 on April 27th via Upgrade.

        : The system is set to send the monthly birthday gift 5 days in advance, so the sending time for VIP1's May birthday gift is April 26th.

The          system sent out May birthday gifts on April 26th. Customer A did not yet have an Upgrade at that time and therefore could not receive the VIP1 birthday gift.

- **Check Time**: The system began checking eligible members at 5:00 AM that day and sent gifts in sequence.

**    > The exact time members receive their birthday gifts may vary slightly depending on system processing time.

- **Notification Sending Time**: If birthday gift notifications have been enabled in **Push Notifications > Email Notification Template** or **SMS Notification Template**, the system will send a notification to members at 12:00 PM that day.

### Membership Claiming Rules
- **Register during your birthday month:** If the initial VIP level threshold is 0 yuan, the birthday person will be automatically granted that level and receive a birthday gift upon registration, without being subject to the **birthday gift sent N days in advance** restriction.

- **Single Claim Policy:** During the birthday gift sending period (from the date of advance issuance to the end of the birthday month), each member is limited to **one VIP birthday gift**, and it will not be sent repeatedly due to Upgrade during this period.

### Related operations
- **Stacked Gifts**: If you set up an store-wide member birthday gift in **Marketing Activities > store-wide Discount - Bonuses & Coupons**, the consumer will **receive both**. Please plan your birthday gift distribution policy carefully.

- **Delete Birthday Gift**: Please go to **Members > All Members**, select your personal page, and [Manually Reclaim] (../manage-member-profiles.md#任務四資產配置) coupons or bonus points.

### Setting method
1. Enter the **Birthday Gift Name and Number of Days to Receive in Advance**. This VIP member will receive the birthday gift on the specified date.

    ![](../../../assets/images/EC-後台-會員-VIP設定-設定生日禮01.en.png){ .screenshot }

2. Select the Birthday Gift Type (select all):

    === "Bonus"

        

         Enter the **Number of Bonus Points to Receive and Validity Period**.

        ![](../../../assets/images/EC-後台-會員-VIP設定-設定生日禮02.en.png){ .screenshot }

    === "Coupon"

        1. Click **Add Coupon**.

            > Multiple coupons can be added.

        2. Select Coupon Type:

             - Amount

             - Percentage

             - Gift **(Enterprise Edition Only)**

                !!! info "VIP Gift Coupon Usage Rules"

                    1. Product Binding Rules: Each gift coupon can only be bound to one product, and the style cannot be specified.

                    2. Multiple Gift Setting Method: If you want to give away multiple different items at once, please create multiple gift coupons.

                    3. Sending Mechanism: The system will send all bound gift coupons. Consumers cannot choose one to receive on the front end.

                     → Learn about [Complete Gift Coupon Specifications](../../marketing/coupon/gift-coupon-spec/#使用須知).

        
        3. Set Relevant Parameters.         4. **Setting Rules for Use with Other Marketing Campaigns**

            

             First, select [**Using Logic**](#vip-優惠併用規則), then select the marketing campaigns from the list to which you want to apply this rule.

             offers the following marketing activities that can be linked and used with the rules:

            

             - Member Exclusive Pricing

             - Single Item Discount

             - Red & Green (Combination Discount)

             - Optional Discount

             - Multi-level Product Category Discount

             - store-wide Discount

             - VIP Discount

             - Add-on Purchase

             - Referral Code Discount

        ![](../../../assets/images/EC-後台-會員-VIP設定-設定生日禮03.en.png){ .screenshot }

## 5. Member Day Settings

### Instructions for Use
* **Valid Date Restriction**: If the set Member Day is outside the valid date range of the month, the Member Day feature will not be activated for that month.


    > If you set the 30th of each month as Member Day, February will not automatically apply the Member Day activity because the longest possible date is the 29th (or 28th).


* **Exclusion of Other VIP Offers**: On Member Day, other VIP offers are not included in the calculation.


     - If Member Day **Order Discounts** are enabled, the **Discount Offer** setting will not be effective on Member Day.


     - If Member Day **Free Shipping** is enabled, the **Free Shipping** setting will not be effective on Member Day.


     - If Member Day **Bonus** is enabled, the **Bonus Multiplier** setting will not be effective on Member Day.


### Setting method
1. Select Member Day.

    !!! info "**Multiple Member Days per Month Functionality** Applicable Versions"

         This function is exclusive to the **Enterprise Edition**. You can select multiple dates, and members will receive a member gift on each designated date within that month.

    ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日01.en.png){ .screenshot }

2. Select Member Gift:

    === "Order Discount"

        1. Enter the **specified discount**. VIP members will enjoy a specified discount on their entire order.

            > Please set the discount value between 1 and 99. For example: 90 represents a 10% discount, and 70 represents a 30% discount.

        2. **Setting Rules for Use with Other Marketing Campaigns**
            
             First, select [**Using Logic**](#vip-優惠併用規則), then select the marketing campaigns from the list to which you want to apply this rule.

             offers the following marketing campaigns that can be linked and used with rules:

            

             - Member Exclusive Pricing

             - Single Item Discount

             - Red & Green (Combination Discount)

             - Optional Discount

             - Multi-level Product Category Discount (Advanced Product Category Discount)

             - store-wide Discount

          ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日02.en.png){ .screenshot }

    === "Free Shipping"

        1. Enter the **Free Shipping Threshold**. VIP members who reach the threshold will enjoy free shipping on their entire order.

        2. **Setting the Combination Rule with Other Marketing Activities**
            
             First, select [**Combination Logic**](#vip-優惠併用規則), then check the marketing activities you want to apply this rule to from the list.

             offers the following marketing activities that can be linked and used with the rules:

            

             - Member Exclusive Price

             - Single Item Discount

             - Red & Green (Combination Discount)

             - Optional Discount

             - Multi-level Product Category Discount (Advanced Product Category Discount)

             - store-wide Discount

          ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日03.en.png){ .screenshot }

    === "Bonus"

         sets **spending threshold, bonus rewards, validity period, and cumulative reward rules**. Bonus points are awarded based on the order amount for purchases made on Member Day.

        ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日04.en.png){ .screenshot }

    === "Coupon"

        1. Click **Add Coupon**.

        2. Select Coupon Type:

            - Amount

            - Percentage

            - Gift **(Enterprise Edition Only)**

                !!! info "VIP Gift Coupon Usage Rules"

                    1. Product Binding Rules: Each gift coupon can only be bound to one product, and the style cannot be specified.

                    2. Multiple Gift Setting Method: If you want to give away multiple different items at once, please create multiple gift coupons.

                    3. Distribution Mechanism: The system will send all bound gift vouchers; consumers cannot choose one to claim on the front end.

                     → Learn about [Complete Gift Voucher Specifications](../../marketing/coupon/gift-coupon-spec/#使用須知).

        
        3. Setting Relevant Parameters.

        4. **Setting the Combination Rule with Other Marketing Activities**

            
             First, select [**Combination Logic**](#vip-優惠併用規則), then check the marketing activities you want to apply this rule to from the list.

             offers the following marketing activities that can be linked and used with the rules:

            

             - Member Exclusive Pricing

             - Single Item Discount

             - Red & Green (Combination Discount)

             - Optional Discount

             - Multi-level Product Category Discount (Advanced Product Category Discount)

             - store-wide Discount

             - VIP Discount

             - Add-on Purchase

             - Referral Code Discount

        

          ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日05.en.png){ .screenshot }

## 6. Upgrade Gift Settings

### Instructions for Use
* **Number of Gifts Sent:** Each Upgrade gift can only be sent once per membership tier during the membership period.

* **Version Switching:** Switching from the old VIP version to the new VIP version will not trigger the sending of the Upgrade gift.

### Setting method
1. Choose whether to accumulate Upgrade gifts across different levels.

2. Select Upgrade Gifts

     === "Bonus"

         sets **bonus gift distribution and validity period**. Bonus points will be awarded after the Member's Day Upgrade.

     === "Coupons"

         1. Click **Add Coupon**.

             > Multiple coupons can be added.

        2. Select Coupon Type:

             - Amount

             - Percentage

             - Gift **(Enterprise Edition Only)**

                !!! info "VIP Gift Coupon Usage Rules"

                    1. Product Binding Rules: Each gift coupon can only be bound to one product, and the style cannot be specified.

                    2. Multiple Gift Setting Method: If you want to give away multiple different items at once, please create multiple gift coupons.

                    3. Sending Mechanism: The system will send all bound gift coupons. Consumers cannot choose one to receive on the front end.

                     → Learn about [Complete Gift Coupon Specifications](../../marketing/coupon/gift-coupon-spec/#使用須知).

        

        3. Set Relevant Parameters.

        4. **Setting Rules for Use with Other Marketing Campaigns**
            
             First, select [**Using Logic**](#vip-優惠併用規則), then select the marketing campaigns from the list to which you want to apply this rule.

             offers the following marketing activities that can be linked and used with the rules:

            

             - Member Exclusive Pricing

             - Single Item Discount

             - Red & Green (Combination Discount)

             - Optional Discount

             - Multi-level Product Category Discount (Advanced Product Category Discount)

             - store-wide Discount

             - VIP Discount (VIP Discount)

             - Add-on Purchase

             - Referral Code Discount

![](../../../assets/images/EC-後台-會員-VIP設定-設定Upgrade禮01.en.png){ .screenshot }
