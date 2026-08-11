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
# Set Up VIP Exclusive Offers

Set up exclusive discounts, bonus rewards, and differentiated pricing for VIP members, and master the rules for their use in conjunction with store-wide marketing activities.

{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | Expert / All PLUS / Enterprise

{ .doc-badge }

![](../../../assets/images/EC-後台-會員-VIP設定-優惠設定01.en.png){ .hero-page }

The core appeal of the VIP system lies in its "sense of prestige" and "tangible rewards." The new VIP system offers a variety of offer combinations to help you design differentiated benefits that members will appreciate.

## VIP discounts and rules
When setting up VIP offers, please define the rules for combining the offer with "Designated Marketing Activities". The system provides three different strengths of stacking logic:

- **Unrestricted**

**3.** VIP offers can be directly stacked with all activities.

- **Combined with other activities (product-level exclusion)**

**4.** If a single product already enjoys a selected activity discount, that product will not enjoy the VIP offer; other products in the order that are not participating in the activity will not be affected.

- **No discount during activities (order-level exclusion)**

**5.** If the shopping cart contains any product that qualifies for a selected activity, the entire order will have its VIP offer completely canceled.

When setting up various offers, if you encounter a section on **Rules for combining with other marketing activities**, please refer to the explanations here to select the appropriate logic.

![](../../../assets/images/EC-後台-會員-VIP設定-與其他行銷活動的併用規則01.en.png){ .screenshot }

!!! info "Bonus Points Activation Switch"

     To award bonus points, please go to **Marketing Activities > store-wide Discounts - Bonuses & Coupons**, [Activate Bonus Points Function](../../marketing/bonus-and-gifts/setup-bonus-points/#操作流程).

## 1. Enjoy discounts
1. Enter the **specified discount**. This VIP member will enjoy a specified discount on their entire order.

**(3)** Set the discount value to 1-99. For example, 90 represents a 10% discount, and 70 represents a 30% discount.

2. **Set the rules for using this rule with other marketing activities**

**(4)**

**(5)** First, select [**Use logic**](0), then select the marketing activities from the list to which you want to apply this rule.

6. Marketing activities that can be linked and used with rules:

7.
8. Member-only pricing

9. Single item discounts

10. Red and green (combination discount)

11. Optional discounts

12. Multi-level product category discounts (advanced product category discounts)

13. store-wide discount

![](1)2

## 2. Free shipping on orders.
1. Enter the **Free Shipping Threshold**. VIP members who reach the threshold will enjoy free shipping on their entire order.

2. **Set Rules for Using with Other Marketing Activities**

3.
4. First, select [**Use Logic**](0), then select the marketing activities from the list to apply this rule to.

5. Marketing activities available for binding and using rules:

6.
7. - Member Exclusive Price

8. - Single Item Discount

9. - Red & Green (Combination Discount)

10. - Optional Discount

11. - Multi-level Product Category Discount (Advanced Product Category Discount)

12. - store-wide Discount

![](1)2.

## 3. Bonus multiplier setting

### Instructions for Use
* **Stacked Bonus:** If you have set up both "store-wide Bonus" and "VIP Extra Bonus" simultaneously, members will **receive both** when placing an order.

### Setting method
Enter the **spending threshold, bonus amount, and validity period**. This VIP member will receive extra bonus points after placing an order.

![](https://www.cyberbiz.io/support/wp-content/uploads/VIP優惠03.png){ .screenshot }

## 4. Birthday Gift Setup

### Send Schedule
- **Sending Time**: The system defaults to sending the monthly birthday gift on the 1st of each month.

- **Early Sending**: You can customize to send the birthday gift **N days in advance**.

**0**
**1** Sending is based on the member's current level. If the sending time is earlier than the member's Upgrade date, the member will not receive the birthday gift for levels after Upgrade. You can manually send the birthday gift to the member according to the store's VIP policy.

**2**!!! example "Scenario Example"

**3** Customer A's birthday is in May, and they Upgrade to VIP1 on April 27th.

**4** The system is set to send the monthly birthday gift 5 days in advance, so the sending time for VIP1's May birthday gift is April 26th.

5. The system sent out May birthday gifts on April 26th. Customer A did not yet have Upgrade at that time and therefore could not receive the VIP1 birthday gift.

- **Check Time**: The system began checking eligible members at 5:00 AM that day and sent gifts in order.

6. The exact time a member receives their birthday gift may vary slightly depending on system processing time.

- **Notification Sending Time**: If birthday gift notifications have been enabled in **Push Notifications > Email Notification Template** or **SMS Notification Template**, the system will send a notification to the member at 12:00 PM that day.

### Membership Claiming Rules
- **Register during your birthday month:** If the initial VIP level threshold is 0 yuan, the birthday person will be automatically granted that level and receive a birthday gift upon registration, without being subject to the **birthday gift sent N days in advance** restriction.

- **Single Claim Policy:** During the birthday gift sending period (from the date of advance issuance to the end of the birthday month), each member is limited to **one VIP birthday gift**, and it will not be sent repeatedly due to Upgrade during this period.

### Related operations
- **Stacked Gifts**: If you set up an store-wide member birthday gift in **Marketing Activities > store-wide Discount - Bonuses & Coupons**, the consumer will **receive both**. Please plan your birthday gift distribution policy carefully.

- **Delete Birthday Gift**: Please go to **Members > All Members**, select your personal page, and [Manually Reclaim] (0 points) coupons or bonus points.

### Setting method
1. Enter the **Birthday Gift Name and Number of Days to Receive in Advance**. VIP members will receive their birthday gift on the specified date.

    ![](../../../assets/images/EC-後台-會員-VIP設定-設定生日禮01.en.png){ .screenshot }

2. Select the Birthday Gift Type (all can be selected):

    === "Bonus"

        
         Enter the **Number of Bonus Points to Receive and Validity Period**.

        ![](../../../assets/images/EC-後台-會員-VIP設定-設定生日禮02.en.png){ .screenshot }

    === "Coupon"

        1. Click **Add Coupon**.

            > Multiple coupons can be added.

16.2. Select Coupon Type:

17. - Amount

18. - Percentage

19. - Gift **(Enterprise Edition Only)**

20. !!! info "VIP Gift Coupon Usage Rules"

21.1. Product Binding Rules: Each gift coupon can only be bound to one product, and the style cannot be specified.

22.2. Multiple Gift Setting Method: If you wish to give away multiple different items at once, please create multiple gift coupons.

23.3. Sending Mechanism: The system will send all bound gift coupons. Consumers cannot choose one to receive on the front end.

24. → Learn about [Complete Gift Coupon Specifications](2).

25.
26.3. Set Relevant Parameters.

27.4. **Setting Rules for Use with Other Marketing Activities**

28.
29. First, select [**Using Logic**](3), then check the marketing activities from the list to which you want to apply this rule.

30. Marketing activities that can be linked and used with rules:

31. Member-only pricing

32. Single item discounts

33. Red and green (combination discount)

35. Optional discounts

36. Multi-level product category discounts

37. store-wide discount

38. VIP discounts

39. Add-on purchases

40. Referral code discounts

41. ![](../../../assets/images/EC-後台-會員-VIP設定-設定生日禮03.en.png){ .screenshot }

## 5. Member Day Settings

### Instructions for Use
* **Valid Date Restriction**: If the set Member Day is outside the valid date range of the month, the Member Day feature will not be activated for that month.

**0** If you set the 30th of each month as Member Day, February will not automatically apply the Member Day activity because the longest possible date is the 29th (or 28th).

* **Exclusion of Other VIP Offers**: On Member Day, other VIP offers are not included in the calculation.

**1** If Member Day **Order Discounts** are enabled, the **Discount Offer** setting will not be effective on Member Day.

**2** If Member Day **Free Shipping** is enabled, the **Free Shipping** setting will not be effective on Member Day.

**3** If Member Day **Bonus** is enabled, the **Bonus Multiplier** setting will not be effective on Member Day.

### Setting method
1. Select Member Day.

14. !!! info "**Multiple Member Days per Month Functionality** Applicable Versions"

15. This function is exclusive to the **Enterprise Edition**. You can select multiple dates, and members will receive a member gift on each designated date within that month.

16. ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日01.en.png){ .screenshot }

2. Select Member Gift:

17. === "Order Discount"

18. 1. Enter the **Specified Discount**. VIP members will enjoy a specified discount on their entire order.

19. > Please set the discount value from 1 to 99. For example, 90 represents a 10% discount, and 70 represents a 30% discount.

20. **Setting Rules for Use with Other Marketing Activities**
21.
22. First, select [**Using Logic**](1), then select the marketing activities from the list to which you want to apply this rule.

23. Marketing activities that can be bound to and used with rules:
24.
25. - Member Exclusive Price
26. - Single Item Discount
27. - Red and Green (Combination Discount)
28. - Optional Discount
29. - Multi-level Product Category Discount (Advanced Product Category Discount)
30. - store-wide Discount
31. ![](2)10

32. === "Free Shipping"

33. 1. Enter the **Free Shipping Threshold**. Once this VIP tier member reaches the threshold, the entire order will receive free shipping.

34. 2. **Setting Rules for Use with Other Marketing Campaigns**

35.
36. First, select [**Using Logic**](3), then check the marketing campaigns from the list to which you want to apply this rule.

37. Marketing activities that can be linked and used with rules:

38.
39. - Member-exclusive pricing

40. - Single item discounts

41. - Red and green (combination discount)

42. - Optional discounts

43. - Multi-level product category discounts (advanced product category discounts)

44. - store-wide discount

45. ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日03.en.png){ .screenshot }

46. === "Bonus"

47. Set **spending threshold, bonus reward, validity period, and cumulative reward rules**. Bonus points are awarded based on the order amount for purchases made on Member Day.

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

                    3. Sending Mechanism: The system will send all bound gift coupons. Consumers cannot choose one to receive on the front end.

59 → Learn about the [Complete Specifications of the Gift Certificate] (6).

60
61 → 3. Set the relevant parameters.

62 → 4. **Set the rules for using this rule with other marketing activities**

63
64 → First, select [**Use Logic**] (7), then select the marketing activities from the list to which you want to apply this rule.

65. Marketing activities that can be linked and used with rules:

66.
67. - Member-only pricing

68. - Single item discount

69. - Red and green (combination discount)

70. - Optional discount

71. - Multi-level product category discount (advanced product category discount)

72. - store-wide discount

73. - VIP discount

74. - Add-on purchase

75. - Referral code discount

76.
77. ![](../../../assets/images/EC-後台-會員-VIP設定-設定會員日05.en.png){ .screenshot }

## 6. Upgrade Gift Settings

### Instructions for Use
* **Number of Gifts Sent:** Each Upgrade gift can only be sent once per membership tier during the membership period.

* **Version Switching:** Switching from the old VIP version to the new VIP version will not trigger the sending of the Upgrade gift.

### Setting method
1. Choose whether to accumulate Upgrade gifts across different Upgrade levels.

2. Select Upgrade Gifts

4. === "Bonus"

5. Set **Bonus Gift and Validity Period**. Bonus points will be awarded after purchasing Upgrade on Member Day.

6. === "Coupons"

7. 1. Click **Add Coupon**.

8. > Multiple coupons can be added.

9. 2. Select Coupon Type:

10. - Amount

11. - Percentage

12. - Gift **(Enterprise Edition Only)**

13. !!! info "VIP Gift Coupon Usage Rules"

14. 1. Product Binding Rules: Each gift coupon can only be bound to one product, and the style cannot be specified.

15. 2. Multiple Gift Item Setup: To give away multiple different items at once, please create multiple gift vouchers.

16. 3. Distribution Mechanism: The system will distribute all bound gift vouchers. Consumers cannot choose one to claim on the front end.

17. → Learn about [Full Gift Voucher Specifications](0).

18.
19. 3. Set Relevant Parameters.

20. 4. **Setting Rules for Use with Other Marketing Activities**

21.
22. First, select [**Using Logic**](1), then check the marketing activities from the list to which you want to apply this rule.

23. Marketing activities that can be linked and used with rules:

24.
25. Member-only pricing

26. Single item discounts

27. Red and green (combination discount)

28. Optional discounts

29. Multi-level product category discounts (advanced product category discounts)

30. store-wide discount

31. VIP discounts

32. Add-on purchases

33. Referral code discounts

![](2)3
