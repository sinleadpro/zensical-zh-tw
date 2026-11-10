---
title: "Set up iPASS MONEY Payments"
description: "Guide merchants through applying for and connecting iPASS MONEY payment services, covering application requirements, required documents, the 2-4 week review timeline, and back-office key setup."
created: 2026-03-16 00:00
last_modified: 2026-06-30 08:52
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
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 提交_iPASS_MONEY_申請
  - 配置_Channel_ID_與_Secret
  - 綁定物流支付方式
features:
  - iPASS MONEY
  - 行動支付
  - 一卡通串接
prerequisites:
  - 需備妥公司登記證明與負責人證件影本
  - 需具備銀行存摺影本（戶名需與公司名一致）
related: []
tags:
  - "Mobile Payment"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 一卡通設定頁面
  - 自訂物流編輯頁面
paths:
  - 金物流 > 金流設定 > 一卡通
  - 金物流 > 自訂物流
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12633
  - https://www.cyberbiz.io/support/?p=51378
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/setup-ipass-money/"
comments: false
search:
  exclude: false
icon: lucide/wallet
hide: []
---
# Set up iPASS MONEY Payments
Guide merchants through applying for and integrating iPASS MONEY payment services. Covers application requirements, required documents, the 2-4 week review timeline, and back-office key setup.
{ .subtitle }


!!! warning "Important Notice: Changes to LINE Pay Features"
    Effective **January 1, 2026**, the iPASS MONEY feature has been fully removed from the LINE Pay wallet. If your storefront needs to offer iPASS MONEY, merchants must **apply separately and reconnect**. Legacy LINE Pay keys cannot be reused.


## Step 1: Prepare Application Documents { #operate-ipass-docs }

Prepare electronic copies (PDF or image format) of the following four documents:

1.  **Company registration documents** (choose one; all pages required)
    - The latest complete company incorporation or change registration form
    - Business registration transcript (not the legacy business registration certificate)
    - Tax registration certificate issued by the National Taxation Bureau
    - Commercial registration certificate issued by the Department of Commerce, Ministry of Economic Affairs
2.  **Owner's national ID card**: Front and back copies.
3.  **Bank passbook copy**: The account name for the payout account must exactly match the registered company name.
4.  **Homepage screenshot**: A screenshot of the storefront homepage after it goes officially live.

!!! tip "Data Security Recommendations"
    If the documents need to be marked for this application only, add the watermark `僅供申請 iPASS MONEY 一卡通使用` to the document.


## Step 2: Submit the Application and Await Review { #operate-ipass-apply }

1.  **Submit the form**: Once your documents are ready, complete the [CYBERBIZ x iPASS MONEY Integration Application Form](https://forms.gle/vHe3DdHZChcS43CUA).
2.  **Await review**: CYBERBIZ forwards your information to iPASS MONEY for review. This takes about **2 to 4 weeks**.
3.  **Create an account**: After registration is complete, the system sends a notification email containing your iPASS MONEY back-office login credentials.

    !!! info "Important Notes"
        If you receive an **account activation email** from iPASS MONEY, it only means your system account has been created. It **does not mean your application has been approved**. Be sure to wait for the CYBERBIZ key notification email before you integrate.




## Step 3: Configure the Back-Office Integration { #operate-ipass-bind }

After you receive the key notification email from CYBERBIZ, follow these steps to enable the service:

1.  Go to **Payment and Logistics > Payment Settings > iPASS MONEY**.
    ![](../../assets/images/EC-後台-金物流-金流設定-啟用一卡通01.en.png){ .screenshot }
2.  Fill in the key information: Use the keys provided in the notification email.
    -   **Channel ID**
    -   **Api Key**
    ![](../../assets/images/EC-後台-金物流-金流設定-啟用一卡通02.en.png){ .screenshot }
3. Set the **Payment Threshold Limit**.

    > :lucide-lock: **Payment Threshold Settings** is available only on the **Expert**, **PLUS Plan**, and Enterprise Plan plans. The Professional and Advanced plans are not supported.

4.  Click **Save**.

!!! warning "Entry Guidelines"
    When you enter the keys, make sure there are **no spaces** before or after them, including hidden spaces created when copying, to prevent validation failures.


## Step 4: Link Logistics Payment Methods { #operate-ipass-bind-logistics }

If your site uses **Custom Logistics** or **Home Delivery Cash on Delivery**, you must manually select the box to support iPASS MONEY:

1.  Go to **Payment and Logistics > Custom Logistics**.
2.  Click the logistics option you want to change.
3.  In **Payment Methods**, select **iPASS MONEY**.
4.  Click **Save**.

![](../../assets/images/EC-後台-金物流-宅配物流-自訂物流綁定付款方式01.en.png){ .screenshot }
