---
title: 管理會員檔案
description: 當特定會員有資料與權限異動、點數與優惠券配置調整、或需要下單協助時，管理員可透過 會員明細頁 進行一站式的客服處理與資料維護。
created: 2026-02-11 00:00
last_modified: 2026-06-30 12:30
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 會員標籤的應用
  - 行銷活動內部連結
  - 詞彙表：會員列表頁、會員明細頁
  - 快速登入內部連結
  - 訊息推播內部連結
  - 測試搜尋能力與標籤關鍵字
  - 會員篩選器內部連結
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
tnb: trunk
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 編輯會員基本資料
  - 手動發送點數與優惠券
  - 調整會員帳號狀態與權限
  - 協助會員代客下單
features:
  - 會員明細管理
  - 代客下單
  - 紅利優惠券派發
  - 帳號權限控管
prerequisites:
  - [[需具備管理員權限以編輯會員敏感資訊]]
related: []
tags:
  - 會員明細
  - 代客下單
  - 紅利優惠券派發
  - 忘記密碼
  - 會員標籤
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > 所有會員 > [點擊會員姓名]
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=248
  - https://www.cyberbiz.io/helpcenter/?p=8497
  - https://www.cyberbiz.io/helpcenter/?p=8798
  - https://www.cyberbiz.io/support/?p=2289
  - https://www.cyberbiz.io/support/?p=2549
  - https://www.cyberbiz.io/support/?p=2635
permalink: https://help.cyberbiz.io/ec/members/manage-member-profiles
comments: false
search:
  exclude: false
icon: lucide/user-round-cog
hide: []
---

# Managing Membership files

When a specific Membership has changes to their data and Permissions, adjustments to points and Coupon configurations, or needs assistance placing an order, the administrator can provide Mon Call Center Process and data maintenance through the Membership Detailed page.
{ .subtitle }

![](../../assets/images/EC-Backend- Membership- All Customers- Membership Detailed Page Overview){ .hero-page }

!!! tip &quot;Application Context&quot;
    - **Routine Data Maintenance**: To modify it. incorrectly entered Name, Phone Number , or Birthday information by Membership .
    - **Customer Complaint Compensation and Rewards**: For specific Orders disputes, manually reissue Bonus Points or Coupon.
    - **Risk Management and Segmentation:** Suspend the Disabled of Membership who maliciously abandon orders, or manually label premium Membership with VIP Tags.
    - **Advanced Call Center Assistance:** Assist Membership who are not proficient in Operation web pages to Order as delegate, or guide them to Reset Password.


## Instructions for Use

Before Operation Membership information, please understand the less system logic:

- **Data Sync:** After Update customer information the Contact information on a member&#39;s Detailed page, **it will not** automatically Update the Shipping Information for **existing old Orders **.
- **Irreversible Operation **: Mon Bonus Points are Send or withdrawn, the system will immediately adjust the Membership assets. Please be sure to Enter the value and reason Hour Operation .



## Task Mon: View Membership behavior and asset data

Once you enter the Detailed page, You can quickly determine the Membership&#39;s spending power and current interaction Status:

| Data Metrics | Evaluation Dimensions | Calculation Formulas | 
| ------- | ------- | -------- | 
| **Cumulative Total spent ** | Loyalty Contribution | Total item price Amount of EC Orders+ POS Orders+ Orders from Other Channels |
| ** Number of ordrs** | Purchase Frequency | Total Number of ordrs : EC Valid Orders+ POS Orders+ Orders from Other Channels |
| **Average Valid Order Price** | Price per customer transaction Value | Total Cumulative Total spent ÷ Number of ordrs |
| ** Total Bonus Points** | Rebate Incentive | Total Bonuses Available to Membership| 
| ** Valid coupon available ** | Intent to make a purchase | Total number of Coupon available to Membership |

Data is not just a static record; it &#39;Yes a **navigator** for making marketing decisions. Less are examples of data application scenarios:

| Data Metrics | Operational Insights | Practical Application Reference |
| ------- | ------- | ----------- |
| **Cumulative Total spent ** | Determines the priority of resource allocation | 1. Send gift certificates to Membership who are about to upgrade to guide them to place additional orders.<br> 2. Provide dedicated human intervention to win back high-value Lost member.
| ** Number of ordrs** | Assess Membership&#39; Brand Dependence and Repurchase Motivation | 1. Predict Replenishment Date Based on Order Cycle<br> 2. Differentiate between &quot;large-amount stockpiling&quot;or&quot;frequent Free Shipping sensitive&quot; customer groups and implement different Push Notification strategies.
| **Average Valid Order Price ** | Determines the Amount of Products combinations and the Free Shipping Threshold| 1. Push Notification Products prices that match the customer&#39;s spending level<br> 2. Refer to this indicator to Setting the threshold for &quot;gift upon purchase&quot; | 
| ** Total Bonus Points** | Measures asset value and attractiveness of return | High points indicate that purchasing power has not yet been channeled back; points Add Buy Discount Event can be Push Notification to stimulate redemption.
| ** Valid coupon available** | The final driving force for Orders completion | Limited-time reminder for Membership who have claimed coupons but haven&#39;t purchased | 

!!! Tip: &quot;From Data Insights To Precision Marketing&quot;
    In addition to View detailed data for individual Membership, you can also use the Membership Filter to filter in times based on specific indicators, enabling more precise mass Push Notification and promotion strategies.

![](../../assets/images/EC - Backend- Membership- All Customers- View )

## Task Tues.: Basic information and Account Maintenance

### 1. Edit Membership Basic information

1. Go to ** Membership&gt; All Customers**, Search for and click on the Membership Name to enter the Detailed page.
2. In the ** Basic information** Sections, click ** Edit** in the upper right corner.
3. You can Update information such as Name, Email Address, Phone Number, Birthday(Gregorian format only), and Address 1.
4. Click ** Save**.

### 2. Manage Account Permissions and Page publish status

In the ** Account Setting** Sections, You can manage access Permissions for Membership behaviors:

- ** Account status**:
    - Disable account: This Membership will be unable to Login in(applicable to malicious users).
    - Set as warning account: Membership can still place orders, but a prominent mark will appear in the Orders List in the background for the Shipping staff to notice.
- ** Account Type:**:
    - **Identify Registered Source**: View if Membership quickly Sign Up through Third Party platforms (such as LINE, Google, Facebook ).
    - **Quick Login Support**: The system records Order source Contains LINE, Google, and Facebook; if a Show fields is **left blank**, it means the Account was Sign Up using a regular Email Address address.
- **Logistics Restrictions**:
    - ** View Unclaimed Goods Records**: View the Membership past **number of Cash on delivery**, as a reference for delivery Permissions assessment.
    - **Control CVS pickup Permissions **: For Membership who have times failed to pick up their orders, the option to **disable** &#39; CVS pickup&#39; or&#39; CVS COD&#39; can be switched to ** Disable**.
- **Notifications and Push Notification:**
    - **Manage Marketing Subscription Page publish status**: Enter whether Membership are willing to receive promotional information and newsletters from Store .
    - ** Setting System Permissions**: Enter whether Membership are willing to Send automatic Email Address regarding order status, Return , and logistics progress.
    
    !!! info &quot;Notice Regarding Update of Notification and Push Notifications&quot;
        The initial preferences for ** Subscribed to Marketing** and **receiving System emails** are Setting by the Membership . If a Store needs to manually change these preferences, they must first reach a consensus with the Membership and obtain Agree to avoid any disputes regarding email receipt.

- ** Registrant Referral Code**: Show the Profit Sharing Sign Up bound to this Membership .

    !!! info &quot;Plan Support Explanation&quot;
        The Registrants Fee feature is not available in the Boss ; this field will Do not display in the backend interface of this Plan .

![](../../assets/images/EC-Backstage- Membership- All Customers - Edit )

!!! info &quot;Expand Custom Information&quot;
    - **Frequently Used Shipping address**: View the frequently used delivery lists Create by Membership themselves.
    - ** Custom fields**: View the Store[custom Sign Up fields](../website-management/customer-registration-flow-and-fields.md#Step-4- Create and manage Custom fields ) and the corresponding Value from Membership .
      This feature is only available to ** Master Plus and Enterprise** customers.

## Task We: Consumer Behavior and Order Management

To help Store accurately assess Membership value, the system integrates **real-time Orders from the Official Website and Stores ** with **manually added Orders from external sites**, providing comprehensive consumption data aggregation. This ensures that a Membership&#39;s VIP level and benefits calculations remain consistent regardless of where they make their purchases.

### 1. Official Website and in-Stores purchases

Scroll to the ** Orders Information** Sections. This Sections automatically aggregates the Total spent from the Official Website(EC) and POS Stores , serving as a primary basis for evaluating Membership contributions.

- **Use Case:** Click on the ** Order Number** to View the detailed Products list and Fulfillment Status of the transaction.
- **Data Update**: Once an Order Placed , it will be immediately added to the ** Total spent on the Official Website and in-Stores **.

! [ ](../../assets/images/EC - Backend- Membership- All Customers- View )

### 2. Orders from Other Channels

Scroll to the ** Price accumulated from other distributions**/** Orders from Other Channels** Sections. This Sections aims to integrate the consumption contributions from non-system-connected platforms (such as marketplaces and private community shopping guides). By **manually adding**, scattered external site data is incorporated into the system to complete the asset management of Membership throughout their entire lifecycle.

Depending on your Plan level, the less two management modes are available:

=== &quot;One-time supplement (professional, advanced)&quot;

    - **Applicable Scenarios**: Replenishing the total historical Total item price in one go.
    - ** Feature:** Quickly enter total assets and simplify the process of entering multiple data entries.
    - ** Operation Steps**:
        1. Scroll to the ** Price accumulated from other distributions** Sections and click ** Edit**.
        2. Enter the Membership total accumulated Total item price and the Order Date.
        3. Click ** Enter** to complete the data entry.
    - **Limitation**: Only the Total price is recorded; Order Details of orders orders cannot be traced.

    ! [ ](../../assets/images/EC-Backend- Membership- All Customers- View - Orders from Other Channels)


=== &quot;Precise Detailed Management (Advanced, PLUS, Enterprise)&quot;

    - **Applicable Scenarios**: Accurately record the Order source of orders external order (e.g., Taipei pop-up (Once you want to add more than one POS store, LINE Group Buy) for reconciliation purposes.
    - ** Feature **: Records specific Date Range, Order source, and Amount for orders , serving as evidence for Membership level progression.
    - ** Operation Steps**:
        1. Scroll to the ** Orders from Other Channels** Sections and click ** Create Orders**.
        2. Enter the ** Order Date**, ** Order source**, and ** Total spent** in that order.
        3. Click ** Enter** to generate a separate record.
    - **Limitations**: Supports Edit or Delete orders records; however, the ** Order source** cannot be changed once Enter.

    ! [ ](../../assets/images/EC - Backend- Membership- All Customers- View - Orders from Other Channels )


## Task Th: Asset Allocation


### 1. Bonus Points Distribution and Management

=== &quot;Orders Send or Recall&quot;

    #### Send

    1. Scroll to the ** Bonus Points** Sections and click ** Add Bonus Point**.
    2. Enter the ** points Name** (e.g., customer complaint compensation) and the ** point(s) value**.
    3. Setting the** Expire Date** (0 represents Forever validity).
    4. After clicking ** Enter**, the points will be immediately credited to your account.

    #### Reclaim

    1. Scroll to the ** Bonus Points** Sections and click:lucide-trash-2: to Remove a specific number of Number of records Points usage record.

    ![](../../assets/images/EC-Backend- Membership- All Customers- View Member Bonus Points (Vouchers) Points01.png)

=== &quot;Times Send&quot;

    1. To** Membership&gt; All Customers**.
    2. Select the Specify Membership in the List (multiple selections are allowed).
      You can use the Membership Filter to select All Customers who meet the Specify criteria, and select All of them with Mon click.
    3. In**More Operation** , Select** Send Bonus Points**.

    ![](../../assets/images/EC-backend- Membership- All Customers- times Send Member Bonus Points (Vouchers) points01.png)


### 2. Coupon Distribution and Management

=== &quot;Orders Send or Recall&quot;

    #### Send

    1. Scroll to the ** Member exclusive coupons** Sections and click ** Adding Member Exclusive Coupon**.
    2. Enter the ** Coupon name ** (e.g., customer complaint compensation) to complete the subsequent Setting of Send conditions and restrictions.
    3. After clicking ** Enter**, the Coupon will be immediately credited to your account.

    #### Reclaim

    1. Scroll to the ** Member exclusive coupons** Sections, click:lucide-trash-2:, and Remove a specific Number of records of Coupon records.

    ![](../../assets/images/EC - Backend- Membership- All Customers- View )

=== &quot;Times Send&quot;

    1. To** Membership&gt; All Customers**.
    2. Select the Specify Membership in the List (multiple selections are allowed).
      You can use the Membership Filter to select All Customers who meet the Specify criteria, and select All of them with Mon click.
    3. In**More Operation** , Select** Send Coupon**.

    ![](../../assets/images/EC-Backend- Membership- All Customers- Times Send Membership Coupon)


!!! info &quot;Plan Support Explanation&quot;
    The Coupon distribution and management feature is not sent in the Boss and Advance ; this interface will Do not display in the backend interface of these Plan .

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [Free Shipping Coupon Model](../marketing/coupon/free-shipping-coupon-spec.md)
    Understand the restrictions on Free Shipping coupons and the Checkout process.

- :lucide-hash:{ .lg }
    [Gift Coupon Model__](../marketing/coupon/gift-coupon-spec.md)
    Understand the restrictions and inventory rules for Gift vouchers.

</div>

## Task Fr: Marketing Tags and Audience Segmentation Management

With Tags, You can provide more detailed marking for individual Membership:

=== &quot;Orders Create or Remove&quot;

    1. Locate the ** Tags ** field on the Membership Detailed page.
    2. **Add a Create Tags:** Enter a new Tags Name and press Enter, or select it From the menu.
    3. ** Remove tags **: Click the `X` Picture # next to an existed!! Tags and Enter.
        When a Tags is no longer bound to Any Membership , the system will automatically Remove it From the Tags list.
    
    ![](../../assets/images/EC-backend- Membership- All Customers- orders transaction-binding Customer tag label01.png)

=== &quot;Times Create or Remove&quot;

    1. To** Membership&gt; All Customers**.
    2. Select the Specify Membership in the List (multiple selections are allowed).
      You can use the Membership Filter to select All Customers who meet the Specify criteria, and select All of them with Mon click.
    3. In**More Operation** , Select** Create Tags** or** Delete Tags**.

    ![](../../assets/images/EC-Backend- Membership- All Customers- Times Customer tag)


## Task Sat: Order as delegate

It is suitable for assisting Membership in Order has been placed or Process situations where shipping documents have expired and need to be reordered.

=== &quot;From Customer List Page&quot;

    To** Membership&gt; All Customers **, find the ` Operate as delegate section in the Customer List , and click ** Goto shop**.

    ![](../../assets/images/EC-Backend- Membership- All Customers- Operate as delegate)

=== &quot;From Membership Detailed Page&quot;

    Click the ** Order as delegate ** button in the upper right corner of the Membership Detailed page.

    

1. The system will Login in to the Membership&#39;s front-end interface.
2. Search for and add the Products you want to buy to Add To Cart.
3. Click the ** Cart Picture #** to complete the Checkout.
4. Setting the logistics Method(e.g., home delivery) and payment information.
5. (Optional) Fill in the Admin note for future tracking.
6. A payment link You can play again after from the backend and Send to Membership for Order Referral Online payment.

!!! info &quot;Plan Applicability Explanation&quot;
    The order placement feature on Order as delegate is not supported in the Boss.

## Task seventh: Membership forgets Password

Based on cybersecurity principles, administrators cannot directly View or Update customer information Password.

- **Onboarding Process**: Instruct Membership to goto shop to the Official Website Login page, click **Forgot Password**, and enter Email to receive an automatic Reset Password Send from the system.
- **Bulk Import Account **: If the Account is Import Excel with Password has been set, the Membership must also complete the initialization through the **Forgot Password** feature upon first Login .

!!! Warning: &quot;HiNet Email Email Retrieval Problem occurred Alert&quot;
    If a consumer Sign Up using a **HiNet Email **, they may not To the &quot;Forgot Password&quot; email due to obstruction by the telecom operator. It is recommended to guide them to use Other Email.

![](../../assets/images/EC-Front-end- User login-Forgot Password)

## Frequently Asked Questions

Why did the Shipping Information for old Orders not change even Update Membership Phone Number ?
    Update to Membership information only affect Orders placed in the **future**. For Orders that have already been placed, the Shipping Information is already stored in the Orders records.

Will Membership To a notification after the bonus is Send ?
    If the Store has Open the bonus change template in ** Email Notification** or**SMS Notification**, the system will automatically Send a notification to the Membership.

Can I use Membership account &#39;within Bonus discount Order as delegate ?
    Yes. On the Checkout Pages for orders Order as delegate in the backend, the administrator can manually select and enter the remaining bonuses in the Membership account for discount.


