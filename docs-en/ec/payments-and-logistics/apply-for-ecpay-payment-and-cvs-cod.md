---
title: "Apply for ECPay Payments and CVS Cash on Delivery"
description: "This guide walks you through registering for ECPay, applying for its payment and CVS cash-on-delivery services, and integrating them with CYBERBIZ."
created: 2026-02-13 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：後續步驟於綠界後台看訂單
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - Professional
  - Advanced
  - Expert
plan_options: []
cyb_extensions: []
intents:
  - 註冊綠界帳號
  - 申請超商物流服務
  - 完成合約商議
  - 綁定 CYBERBIZ 後台
features:
  - 綠界金流
  - 綠界物流
  - 超商取貨付款
prerequisites:
  - "準備負責人證件影本"
  - "準備公司登記證照或變更事項登記表"
related:
  - ec/orders/ecpay-backend-order-query/
tags:
  - "Contracted Members"
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 金流設定 > 綠界金流
  - 金物流 > 宅配物流
  - 金物流 > 超商物流 > 綠界超商取貨
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4872
  - https://www.cyberbiz.io/helpcenter/?p=2430
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/apply-for-ecpay-payment-and-cvs-cod/"
comments: false
search:
  exclude: false
icon: lucide/file-signature
hide: []
---
# Apply for ECPay Payments and CVS Cash on Delivery

ECPay is a widely used third-party payment provider in Taiwan. It offers a range of payment methods, including credit cards, ATM transfers, and convenience store payment codes, along with convenient CVS cash-on-delivery (logistics) service. This guide walks you through account registration, service applications, and back-office integration.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Professional / Advanced / Expert
{ .doc-badge }

![](../../assets/images/綠界-後台-註冊綠界帳號01.en.png){ .hero-page }

!!! info "Plan Applicability"
    ECPay payment and CVS logistics integration is available only to merchants on the **Professional, Advanced, and Expert plans** who have **not enabled CYBERBIZ PAYMENTS**. If you already use CYBERBIZ PAYMENTS, its system includes full payment and CVS logistics features, so you do not need to connect ECPay separately.


## Usage Notes { #prerequisites-ecpay-cvs }

Before you start, choose the path that matches your service needs:

- **Online payments only (no CVS pickup)**: Skip step 2. Complete only step 1 and step 3-1.
- **Full payments and logistics (including CVS pickup)**: Complete all settings in steps 1 to 3, in order.
  > If your store needs both payment and CVS pickup services, we recommend that you **apply for both** when you register your account. Doing so avoids repeated document submissions or paper-based processes later and shortens the activation timeline.
- **Existing ECPay members (upgrading to a contracted merchant)**: See step 2-2 to complete the contract negotiation process.


## Step 1: Register an ECPay Account and Basic Information { #operate-ecpay-cvs-register }

Whether you need only payments or both payments and logistics services, the first step is to create an account on the ECPay website.

### 1. Account Registration and Member Category { #operate-ecpay-cvs-account }

1. Go to the [ECPay website](https://www.ecpay.com.tw/) and click **Register** in the upper-right corner.
2. Set a login account and password.
3. **Select a Member Type**: Companies should select **Business Member**.
4. **Select Services to Apply For**: Select **Payment** and **Logistics** services.

    > E-invoice service is charged separately. If you do not need it right now, leave it unchecked.

![](../../assets/images/綠界-後台-註冊綠界帳號02.en.png)

### 2. Fill in Company Information { #operate-ecpay-cvs-company }

Make sure the information matches your CYBERBIZ General Settings to speed up review:

- **Prepare the following documents**:
    1. A copy of the representative's ID.
    2. Business registration certificate or company change registration form.

    ![](../../assets/images/綠界-後台-註冊綠界帳號04.en.png)

- **Store Name**: This name appears on the payment page and the buyer's credit card statement. Keep it the same as the **Website Name** in **Website Management > General**.

    > To change the store name, each site can use 2 fee-free changes (NT$100). The change process takes about 5-7 business days.

    ![](../../assets/images/綠界-後台-註冊綠界帳號03.en.png)

### 3. Fill in Website Information { #operate-ecpay-cvs-site }

- **Contact Information**: Contact details such as **email, phone number, and address** must match the **Contact Information** shown on the storefront.
- **Website URL**: Enter your official CYBERBIZ domain. It must match the **Domain Name** in **Website Management > Domain**, and your website must have at least one product listed.

    > Do not set product text for items prohibited from online sale, such as circle lenses, pupil lenses, or EYES, etc.

    ![](../../assets/images/綠界-後台-註冊綠界帳號05.en.png)

- **Activate services**: We recommend selecting both **Credit Card** and **Overseas Credit Card**.
    ![](../../assets/images/綠界-後台-註冊綠界帳號06.en.png)

!!! warning "Review Timeline"
    After you submit your application, ECPay typically needs **3-5 business days** to review it. You will receive the result by email.


## Step 2: Apply for CVS Logistics Service (Optional) { #operate-ecpay-cvs-logistics }

If you need the "CVS cash on delivery" feature, complete logistics activation before the account is approved or before contract negotiations begin.

### 1. Apply for Logistics Service { #operate-ecpay-cvs-apply-logistics }

1. Go to the ECPay back office and go to [Apply for Logistics Shipping Service](https://www.ecpay.com.tw/IntroTransport).
2. **Select a Logistics Mode**:
    - **C2C (Store Drop-off and Pickup)**: Available for the Professional, Advanced, and Expert plans.
    - **B2C (Bulk Warehouse Consignment)**: Available only for the Expert plan.

![](../../assets/images/綠界-後台-申請超商物流01.en.png)

### 2. Contract Negotiation { #operate-ecpay-cvs-contract }

1. Go to the [ECPay back office](https://vendor.ecpay.com.tw/User/LogOn_Step1) and click **Contract Negotiation** in the upper-right corner.
    ![](../../assets/images/綠界-後台-申請超商物流-合約商議01.en.png)
2. Enter contact information.
  -  For **Sales Contact Information**, select **Same as Accounting Contact**.
      ![](../../assets/images/綠界-後台-申請超商物流-合約商議03.en.png)
  -  Enter `5468` in the **Sales Code** field, or enter `順立智慧` in the **Promoter** field.
      ![](../../assets/images/綠界-後台-申請超商物流-合約商議04.en.png)
3. Upload at least 3 images of your business premises.
    ![](../../assets/images/綠界-後台-申請超商物流-合約商議05.en.png)

### 3. Confirm the Review Is Complete { #operate-ecpay-cvs-check-review }

1. Go to the [ECPay back office](https://vendor.ecpay.com.tw/User/LogOn_Step1), then go to **Vendor Zone > Payment Review Information**.
2. Check the fields to make sure the review has passed.

    - The **Credit Card Review Status** field should show **Approved**.

        > If the review does not pass, first check whether any required supporting documents or related information were left out of your application.

        ![](../../assets/images/綠界-後台-檢核申請通過01.en.png)

    - **Service Fee Rate**: Should show the actual rate for your plan.
        ![](../../assets/images/綠界-後台-檢核申請通過02.en.png)
    - **CVS Pickup Service**: Should be **Activated**.

        > Complete the logistics application before contract negotiations. If you apply after negotiations, you must follow the paper application process.

        ![](../../assets/images/綠界-後台-檢核申請通過03.en.png)



## Step 3: Set up CYBERBIZ Back-Office Integration { #operate-ecpay-cvs-bind }

After you get your ECPay vendor number, you can complete the binding in the CYBERBIZ back office.

### 1. Enable the Payment Service { #operate-ecpay-cvs-enable-pay }

1. Go to **Payment and Logistics > Payment Settings > ECPay**.
2. In the **Vendor Number** field, paste the store code you got from the ECPay back office.
  > To find it, go to Vendor Area > Vendor Basic Information.
  ![](../../assets/images/綠界-後台-查看商店代號01.en.jpg)
3. Turn on the payment methods you want to offer customers (for example, credit card, ATM, or convenience store code).
4. **Key step**: Go to **Payment and Logistics > Delivery Settings**, select the matching logistics option, and select the newly added ECPay payment methods. Payment options appear on the storefront only when they are selected.

![](../../assets/images/EC-後台-金物流-金流設定-填寫綠界廠商代號01.en.png)

!!! info "Credit Card Installment Feature Overview"
    Credit card installment payments are usually available only to **ECPay contracted merchants**. Confirm that you have completed **Contract Negotiation** and that ECPay has approved the installment feature.

### 2. Enable the CVS Logistics Service (Optional) { #operate-ecpay-cvs-enable-logistics }

1. Go to **Payment and Logistics > Convenience Store Logistics > ECPay CVS**.
2. After you fill in the basic information, turn on the **Cash on Delivery / Pickup without Payment** toggles for **7-11/FamilyMart**, and set the amount threshold.



## Frequently Asked Questions { #faq-ecpay-cvs }

??? quote "Are the review processes for ECPay payments and CVS logistics separate?"
    Yes. After the basic account is approved, payment services usually activate first. Logistics services and contracted merchant negotiations require additional review time. We recommend submitting all information at once to speed up the process.

??? quote "Who should I contact if I run into problems during the application?"
    For questions about ECPay account review, rates, or contracts, contact ECPay customer service directly:

    - **Customer Service Hotline**: (02) 2655-1775 (24-hour service).
    - **Online Inquiry**: Use the customer service widget in the lower-right corner of the ECPay website.


## Next Steps { #next-steps-ecpay-cvs }

<div class="grid cards" markdown>

- :lucide-credit-card:{ .lg }   
  [__Look Up Orders in the ECPay Back Office__](../orders/ecpay-backend-order-query.md)       
  Learn how to check order status in real time in the ECPay back office and confirm when payments are credited.


</div>
