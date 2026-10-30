---
title: "Member Return Request Feature"
description: "Learn how to turn on storefront return requests, including full and partial return settings and return deadline control."
created: 2026-02-23 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 會員
  - 金物流
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 開啟前台退貨申請開關
  - 設定退貨有效期限
  - 處理會員退貨申請
features:
  - 會員退貨申請
  - 部分退貨
prerequisites: []
related:
  - ec/orders/order-return-process/
  - ec/notifications/manage-email-templates/
tags:
  - "Member Return Process"
  - "After-Sales Service"
  - "Partial Return Requests"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 結帳頁 & 物流設定
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=51897
  - https://www.cyberbiz.io/support/?p=47627
permalink: "https://help.cyberbiz.io/ec/orders/member-return-request-feature/"
comments: false
search:
  exclude: false
icon: lucide/undo-2
hide: []
---
# Member Return Request Feature

Learn how to turn on storefront return requests, including full and partial return settings and return deadlines.
{ .subtitle }


!!! info "Scope and Limitations"
    - **Order types**: Supports regular orders and subscription orders.
    - **Return path**: After the return period set in the system passes, members can't request returns themselves and need to contact you to handle it manually in the admin.



## Task 1: Set Up the Feature in the Admin

Turn on the switch in the admin first so members can see the request button in the storefront order center.

### 1. Turn On Return Requests
Go to **Payment and Logistics > Checkout Page & Logistics**:

=== "Full Return"

    To let members return only **the whole order** at once:

    1. Scroll to the **Order Settings** section.
    2. Expand the **Customer Order Cancellation and Return Request Settings** drop-down menu.
    3. Turn on **Customers Can Request Returns**.

    ![](../../assets/images/EC-金物流-結帳頁物流設定-開啟會員申請取消與退貨功能01.en.png)

=== "Partial Return"

    To let members return **some items** in an order:

    1. **Complete the full return settings.**
    2. Scroll to the **Logistics Settings** section.
    3. Expand the **Storefront Return Settings** drop-down menu.
    4. Turn on **Storefront Partial Return Requests**.

    !!! info "Plan Limits"
        - **Plan limit**: Storefront partial return requests are currently available only on the **Enterprise Plan**.

    ![](../../assets/images/EC-金物流-結帳頁物流設定-開啟會員申請部分退貨功能01.en.png)

### 2. Set the Return Deadline

You can set how many days after an order is complete members can request a return, based on the delivery type:

- **System shipping label orders**: For orders with shipping labels created in CYBERBIZ, set the return deadline within **10 days**.
- **Custom logistics orders**: For orders you ship yourself, set the return deadline within **14 days**.

![](../../assets/images/EC-金物流-結帳頁物流設定-設定會員申請退貨期限01.en.png)

## Task 2: Handle Returns on the Storefront and in the Admin

### 1. Request and Accept Returns

=== "Member Request Steps"

    1. The member signs in to your website and goes to **Order Lookup > Regular Orders**.
    2. Next to an order within the allowed days, the member clicks **Request Return**.

        ![](../../assets/images/EC-前台-會員中心-訂單查詢-申請退貨01.en.png)

    3. The member enters the return reason and refund information.

        ![](../../assets/images/EC-前台-會員中心-訂單查詢-申請退貨02.en.png)

    4. The member clicks **Submit Request**.
    5. After the request succeeds, the member can see the **Return Status** in the order details.

        ![](../../assets/images/EC-前台-會員中心-訂單查詢-申請退貨03.en.png)

    !!! Flexible Partial Item Returns
        If you allow **storefront partial returns**, members can select the items and quantities to return.


=== "Merchant Steps"

    1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders**.
    2. Find orders whose return status is **Return Requested**.
    3. Open the order details, and in the **Order Activity Log** section, click **Customer Requested Return** to see the details and reason the member entered.

    !!! Flexible Partial Item Returns
        If you allow **storefront partial returns**, after members select the items and quantities to return, you can see the requested items and quantities.

    ![](../../assets/images/EC-後台-訂單-所有訂單-查看訂單退貨理由與數量01.en.png)

### 2. Review Returns and Confirm Results

=== "Member Views Results"

    After you receive the package and finish the review, the member can see the **refund amount**.

    !!! Flexible Partial Item Returns
        If you allow **storefront partial returns**, after you finish the return review, members can also see the **successfully returned quantity** of each item.

    ![](../../assets/images/EC-前台-會員中心-訂單查詢-查看退款金額01.en.png)


=== "Merchant Review Steps"

    - For full returns, the system automatically refunds the full amount.
    - For partial returns, you decide the return quantity and refund amount based on your store policy when issuing the partial refund.

    !!! Flexible Partial Item Returns
        If you allow **storefront partial returns**, you can see the items and quantities the member requested during the return review.


## Task 3: Return Status Notifications

=== "Notify Members"

    Go to **Push Notifications > Email Notification Template** and turn on **Order Return Request Reminder** manually.

=== "Notify Merchants"

    By default, the system sends you an email.



## How the System Works

### 1. Partial Return Selection Rules

The system has different selection rules for different product types:

| Product Type | Selection Rule |
| :--- | :--- |
| **Regular products** | Can be selected individually with a quantity |
| **Bundles** | Treated as a single item; must be returned as a whole set and can't be split |
| **Add-ons/gifts** | Can be selected for return individually |

!!! tip "Return Tips"
    This feature offers flexible return options, but every store has different refund rules (such as gift recovery and bundle discount calculations). We recommend stating your rules clearly in your shopping policy and contacting shoppers to confirm.

### 2. How Refund Amounts Are Calculated

The system adds up the **original prices** of the products the member selects. When you actually issue the refund in the admin, you can adjust the final refund total as needed.

- **Not included**: Automatic discounts from marketing campaigns (such as coupon and spend-threshold discounts).




## FAQ

??? quote "Why can't members find the **Request Return** button in the order center?"
    Check the following settings:

    1. Whether the order is past the **return period** set in the admin.
    2. Whether you turned on **Customers Can Request Returns**.


??? quote "Can I change a member's partial return request?"
    Yes. When you process the return in the admin, you still have final control over the items and amounts. The member's request is only a reference.


## Next Steps

<div class="grid cards" markdown>

- :lucide-package-check:{ .lg }  
  [__Merchant Return Process__](order-return-process.md)  
  Learn how to process returns and refunds in the admin after receiving a member's request.

- :lucide-mail:{ .lg }  
  [__Edit Email Notification Templates__](../notifications/manage-email-template/)  
  Adjust return notifications to give more detailed return shipping instructions.

</div>
