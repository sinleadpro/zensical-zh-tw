---
title: Checkout
description: "Learn the complete CYBERBIZ Smart POS checkout workflow, including member login, product selection, applying promotions, and payment and invoicing."
created: 2026-04-17 12:30
last_modified: 2026-07-27 14:00
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - POS 前台
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - POS 結帳流程
  - 會員登入結帳
  - 套用行銷活動
  - 收款開立發票
features:
  - 智能 POS
  - 會員管理
  - 行銷活動
  - 發票管理
prerequisites: []
related:
  - pos/check/guest-checkout/
  - pos/check/offline-checkout-mode/
  - ec/profit-sharing/registrant-profit-sharing/
  - pos/check/low-stock-notifications/
  - ec/marketing/bonus-and-gifts/setup-bonus-points/
  - ec/marketing/coupon/setup-promo-codes/
  - ec/marketing/coupon/setup-coupons/
  - ec/marketing/coupon/multiple-coupons/
  - ec/profit-sharing/referrer-profit-sharing/
  - pos/check/storewide-order-discounts/
  - pos/check/pos-manager-price-override/
  - ec/marketing/upsells/setup-order-upsell/
  - ec/marketing/upsells/setup-product-upsell/
  - ec/marketing/discounts/threshold-gifts-and-quantity-gifts/
  - pos/check/bonus-point-mall/
  - pos/inventory/pos-reports-list-guide/
  - pos/check/payment-method/
  - pos/check/payment-method/multiple-payment-methods/
  - pos/orders/manage-general-orders/
  - pos/check/print-invoice-details/
  - pos/check/mixed-tax-invoices/
  - ec/orders/reports/export-order-report/
  - pos/inventory/
tags:
  - "Checkout Process"
  - "POS Front Desk"
  - "Member Login"
  - "Marketing Campaigns"
  - "Payment and Invoicing"
acoiv: operation
apis: []
devices:
  - tablet
  - desktop
ui_components:
  - 小計
  - 進行結帳
  - 行銷活動
  - 會員載具
paths:
  - 行銷活動 > 全館折扣 – 紅利 & 優惠券
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=5012
permalink: "https://help.cyberbiz.io/pos/check/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Checkout
From member identification to payment and invoicing, this guide walks you through each key step of in-store checkout to deliver a smooth customer experience.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Daily Sales**: Quickly add products and complete payment, with inventory synced in real time.
    - **Member Benefits**: Log in a member to apply tier-specific offers, redeem bonus points, or use coupon.

## Complete Checkout Process

```mermaid
graph LR
  A["Identify Member"]
  A1["Member Login"]
  A2["Quick Registration"]
  A3["Guest Checkout"]

  B1["Enter Products"]
  B2["Apply Promotions"]

  C1["Payment Processing"]
  C2["Issue Invoice"]

  subgraph memberLogin["Member Login"]
  A --> A1 & A2 & A3
  end

  subgraph cartSubtotal["Cart Subtotal"]
  A1 & A2 & A3 --> B1
  B1 --> B2
  end

  subgraph checkout["Checkout"]
  B2 --> C1
  C1 --> C2
  end
```

## Step 1: Member Login

Before checkout begins, identifying the customer ensures that member benefits are applied correctly and purchases are recorded.

=== "Interface Overview"

    ### Select Customer Identity on the Login Page

    1. **Start Checkout**: Click the **Checkout** button on the right side of the POS Front Desk.
    2. **Select Customer Checkout Identity**:
        - **Member Login**:
            - **Mobile Number**: The most common login method. Quickly enter the customer's phone number.
            - **Customer Barcode**: Scan the member barcode shown in the customer's mobile app.
            - **Email Search**: Enter an email address to search.
        - **Quick Member Registration**: If the customer is not a member but wants to join, enter their mobile number and click **Quick Registration**. The system automatically sends an **Account Activation Notice** SMS.
        - **Guest Checkout**: If the customer does not want to provide information, click **Guest Checkout** to go directly to the cart.
    3. **Bind Registrant Profit Sharing**: Specify a **Registrant Profit Sharing** code.

    ![](../../assets/images/POS-前台-結帳-選擇結帳身分01.en.png){ .screenshot }

    ### Add Member Details at Checkout

    === "Member Login"

        After logging in, you can view the customer's VIP tier, current bonus points, and purchase history. Click to view details.

        ![](../../assets/images/POS-前台-結帳-會員基本資訊01.en.png){ .screenshot }

    === "Quick Member Registration"

        To switch customers, click **Switch Member** to log in again.

        ![](../../assets/images/POS-前台-結帳-切換會員01.en.png){ .screenshot }

    === "Guest Checkout"

        In guest checkout mode, click **Member Login** to switch to member checkout. The order is automatically converted to a member order and receives the corresponding benefits.

        ![](../../assets/images/POS-前台-結帳-訪客登入會員01.en.png){ .screenshot }

=== "Detailed Instructions"

    <div class="grid cards" markdown>

    - :lucide-plug:{ .lg }
    [__Guest Checkout__](guest-checkout/)<br>
    For customers who do not provide information. Quickly go to the cart.

    - :lucide-plug:{ .lg }
    [__Offline Checkout__](offline-checkout-mode/)<br>
    Keeps transactions recorded without interruption when the network is unstable.

    - :lucide-plug:{ .lg }
    [__Registrant Profit Sharing__](../../ec/profit-sharing/registrant-profit-sharing/)<br>
    Set up promotional rewards to recognize people who refer new customers to register.

    </div>

## Step 2: Cart Subtotal

Enter the items the customer is buying into the system and confirm whether they qualify for marketing campaigns.

### Add Products

=== "Interface Overview"

    1. **Scan/Enter**: Use a barcode scanner to read the product barcode, or enter the SKU or vendor product number in the search bar.

    2. **Manual Search**: Click **Product Search** to open a pop-up window.

        - **Search Method**: Select **Starts With** or **Fuzzy Search**.
        - **Multi-Field Search**: Search by **Product**, **SKU**, or **Vendor Product Number**.
        - **Quick Select**: Click a product row to add it to the list. Click it again to remove it quickly.

        ![](../../assets/images/POS-前台-結帳-商品搜尋01.en.png){ .screenshot }

    3. **Adjust Quantity**: Click an added product row to change its quantity directly.

    4. **Notes**: Click the **Notes** button below to edit.

        - **Merchant Notes**: **Internal only**. This information is visible only to back-office administrators and is not visible to customers.
        - **Order Notes**: **Visible to both parties**. This information is shared with both the merchant and the member.

            > Member access path: Members can log in to the website, go to **Orders > All Orders**, and view this note on the order details page.

        ![](../../assets/images/POS-前台-結帳-建立備註01.en.png){ .screenshot }



=== "Detailed Instructions"

    <div class="grid cards" markdown>

    - :lucide-plug:{ .lg }
    [__Set Up Low-Stock Alert Method__](low-stock-notifications/)<br>
    Track inventory levels in real time to avoid overselling or running out of stock.

    </div>

### Apply Marketing Campaigns

=== "Interface Overview"

    1. **bonus points**: Manually enter the redemption amount (cannot exceed the cap) or select **Redeem All**.
    2. **Promo Code**: From the drop-down menu, select the **Promo Code** or **coupon** that applies to the customer.

        !!! info "Don't see the **Bonus Discount** or **Promo Code** field on the page?"
            If a field is missing, it is usually related to authentication settings. Go to the back-office and adjust the following:

            Go to **Marketing > Shop-wide Discount – Bonus & Coupons** and set **Require Barcode Authentication for POS coupon/bonus points** to **No** to display the field on the page.

    3. **Referral Code**: Enter a referral code to apply the **Referrer Profit Sharing** plan to this order.
    4. **Switch Checkout Profit Sharing Staff**: Assign a checkout staff member to apply the **Checkout Profit Sharing** plan to this order.

        ![](../../assets/images/POS-前台-結帳-小計行銷活動01.en.png){ .screenshot }

    5. **Add Order Discount**: **Store Managers** can adjust order prices.

        - **Order-Wide Discount**: Click **Add Order-Wide Discount** and enter the discount value.
        - **Override Product Price**: Click the target product, then enter the discount value in the drop-down menu.

        ![](../../assets/images/POS-前台-結帳-店長改價01.en.png){ .screenshot }

    6. Other marketing campaigns: Click **Marketing Campaigns** to open a pop-up window.
        - **Add-On Purchase**: The system displays eligible add-on products. Scan the barcode or select the add-on item.
        - **Spend/Quantity Gift**: View the remaining amount needed to qualify. If the threshold is met, the system automatically adds the gift.

            > If gift stock is insufficient, the system displays a pop-up alert and does not add the gift automatically.

        - **Bonus Mall**: Select and apply the bonus product the customer wants to redeem.

        ![](../../assets/images/POS-前台-結帳-小計行銷活動02.en.png){ .screenshot }

=== "Detailed Instructions"

    <div class="grid cards" markdown>

    - :lucide-plug:{ .lg }
    [__Send Member-Exclusive bonus points__](../../ec/marketing/bonus-and-gifts/setup-bonus-points.md)<br>
    Issue bonus rewards to increase repeat purchases and member loyalty.

    - :lucide-plug:{ .lg }
    [__Create Promo Codes__](../../ec/marketing/coupon/setup-promo-codes.md)<br>
    Create exclusive discount codes for customers to enter manually at checkout.

    - :lucide-plug:{ .lg }
    [__Create coupon__](../../ec/marketing/coupon/setup-coupons.md)<br>
    Manage coupon that apply automatically or let customers select them.

    - :lucide-plug:{ .lg }
    [__Set Up Multiple coupon__](../../ec/marketing/coupon/multiple-coupons.md)<br>
    Allow multiple coupon on a single order to add checkout flexibility.

    - :lucide-plug:{ .lg }
    [__Create Referrer Profit Sharing__](../../ec/profit-sharing/referrer-profit-sharing.md)<br>
    Set up referral commissions to reward existing customers, employees, and third parties who refer new customers.

    - :lucide-plug:{ .lg }
    [__Order-Wide Discount__](storewide-order-discounts/)<br>
    Motivate store staff by calculating bonuses based on checkout amounts.

    - :lucide-plug:{ .lg }
    [__Store Manager Price Override__](pos-manager-price-override/)<br>
    Authorized staff can manually adjust orders or prices.

    - :lucide-plug:{ .lg }
    __Create Add-On Purchase Campaign__<br>
    Increase average order value by recommending value add-on products at checkout.
        - [Order Add-On Purchase](../../ec/marketing/upsells/setup-order-upsell.md)
        - [Product Add-On Purchase](../../ec/marketing/upsells/setup-product-upsell.md)

    - :lucide-plug:{ .lg }
    [__Create Spend and Quantity Gift Campaigns__](../../ec/marketing/discounts/threshold-gifts-and-quantity-gifts.md)<br>
    Encourage customers to buy more. Gifts are automatically given once the threshold is met.

    - :lucide-plug:{ .lg }
    [__Set Up Low-Stock Alert Method__](low-stock-notifications/)<br>
    Track inventory in real time to keep sales running smoothly.

    - :lucide-plug:{ .lg }
    [__Create Bonus Mall__](bonus-point-mall/)<br>
    Offer varied redemption options to give bonus points real value.
        - [Bonus MallProduct Checkout](bonus-point-mall/#於前台結帳)

    </div>


## Step 3: Complete Checkout

The final stage of payment and receipt processing. Once complete, the order is officially placed.

=== "Interface Overview"

    ### Payment Processing

    1. **Proceed to Checkout**: Click **Proceed to Checkout** in the lower-right corner to open the payment page.
    2. **Select a Payment Method**:

        - **Single Payment**: For cash or credit card, select the method and enter the amount received.
        - **Multiple Payment Methods**: If the customer needs to split payment (for example, partly cash and partly 5x Vouchers), select **Multiple Payment Methods** and enter each amount in turn.

        ![](../../assets/images/POS-前台-結帳-付款方式01.en.png){ .screenshot }

    3. **Sales Recognition Date**: Defaults to today. To record sales under a different date, edit it manually.

        - This date field is the search basis when the system generates the [POS Product Sales Report](../inventory/pos-reports-list-guide/#商品銷售報表). The system assigns orders to the matching report period based on the date set here.

        ![](../../assets/images/POS-前台-結帳-收款作業02.en.png){ .screenshot }

=== "Detailed Instructions"

    <div class="grid cards" markdown>

    - :lucide-plug:{ .lg }
    [__Turn On Payment Methods__](payment-method/)<br>
    Manage in-store payment channels and set the most suitable checkout order.

    - :lucide-plug:{ .lg }
    [__Create Multiple Payment Methods__](payment-method/multiple-payment-methods/)<br>
    Supports split payments to meet diverse customer payment needs.

    </div>

### Issue Invoices

=== "Interface Overview"

    1. **Select Invoice Type**:

        ![](../../assets/images/POS-前台-結帳-開立發票01.en.png){ .screenshot }

        - **Member Carrier (Personal/Company)**: With an invoice machine, enter the Unified Business Number or carrier code to issue an e-invoice.
        - **Self-Issued (Manual Invoice)**: If no invoice machine is connected, select this option and fill in the invoice number and Unified Business Number after checkout.

            ![](../../assets/images/POS-前台-結帳-手開發票號碼01.en.png){ .screenshot }

            > You can also [issue an invoice later](../orders/manage-general-orders/#補開發票--列印明細) from the **Orders** page.

        - **Other Carriers**: Mobile barcode, Citizen Digital Certificate, or donation code.

    2. **Complete Checkout**: Confirm that the amount is correct, then click **Collect Payment**.



=== "Detailed Instructions"

    <div class="grid cards" markdown>

    - :lucide-plug:{ .lg }
    [__Automatically Print Invoices and Itemized Details__](print-invoice-details/)<br>
    Print automatically at checkout, or turn off automatic printing to save invoice paper.

    - :lucide-plug:{ .lg }
    [__Issue Mixed-Tax Invoices__](mixed-tax-invoices/)<br>
    Handle products with different tax rates and calculate and issue invoices accurately.

    - :lucide-plug:{ .lg }
    [__Export Order Reports__](../../ec/orders/reports/export-order-report.md)<br>
    Export invoice number and Unified Business Number fields for orders.

    - :lucide-plug:{ .lg }
    [__Omnichannel Inventory Management__](../inventory/index.md)<br>
    Manage inventory across all channels to ensure there are no gaps between online and offline stock.

    </div>
