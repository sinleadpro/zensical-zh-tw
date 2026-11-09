---
title: "Australia Local Payment Services"
description: "Set up Australia Local payment services through Airwallex, from account application and website compliance review to backend API integration."
created: 2026-03-03 00:00
last_modified: 2026-10-13 10:20
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：建立商品、頁腳、購物車相關設定、訂單相關設定
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - AU
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 申請_Airwallex_帳戶
  - 激活收單功能
  - 串接_API_密鑰
features:
  - 澳洲落地版
  - 跨境金流
  - Airwallex 收單
prerequisites:
  - 需為澳洲落地版商家
  - 需先聯繫開店顧問取得申請連結
related: []
tags:
  - "Cross-Border E-Commerce"
  - Airwallex
acoiv: integration
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=51285
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/australia-local-payment-services/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# Australia Local Payment Services

Australia Local partners with Airwallex to provide merchants with stable and diverse local payment services. This guide walks you through the full process, from account application and website compliance review to backend API integration.
{ .subtitle }


[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用方案) | Cross-Border E-Commerce (Australia Local)
{ .doc-badge }

![](../../assets/images/澳洲站-後台-金物流-金流設定-畫面總覽01.en.png){ .hero-page }

## Usage Notes { #prerequisites-au-payments }

- **Fee Policy**: For account monthly fees, payment processing fees, and settlement mechanisms, see the [Airwallex official pricing details](https://www.airwallex.com/au/pricing).



## Step 1: Apply for and Activate Your Airwallex Account { #operate-au-payments-airwallex }

### 1. Submit Account Application { #operate-au-payments-apply }

Contact your CYBERBIZ store consultant to get your dedicated **Airwallex application link**.

- **Account Setup**:
    - **Company Location**: Select the location where your company is registered.
        ![](../../assets/images/Airwallex-前台-會員註冊頁-建立會員01.en.png)
    - **Account Plan**: You must select the **Explore** plan.
        ![](../../assets/images/Airwallex-前台-會員註冊頁-選擇公司所在地01.en.png)
- **Required Documents**: Account opening requirements vary by region. See the [Airwallex account opening document checklist by region](https://help.airwallex.com/hc/zh-cn/sections/8352632554767).



### 2. Activate Account Eligibility { #operate-au-payments-activate }

1. After you complete registration and enter the Airwallex dashboard, click the **Activate Account** button on the home page.
    ![](../../assets/images/Airwallex-前台-首頁-激活帳戶01.en.png)
2. Complete email verification as instructed.
    ![](../../assets/images/Airwallex-前台-首頁-激活帳戶02.en.png)

## Step 2: Activate Acquiring Services { #operate-au-payments-acquire }

### 1. Set up Compliance Information on Your Website { #operate-au-payments-compliance }

Make sure your website has the following basic structure for review by the Airwallex team:

- **Brand Identity**: Website logo.
- **Product Display**: Create at least one product and display the correct price.
- **Required Footer Pages**:
    - **Contact Information**: Provide customer service contact details.
    - **About Us**: Must include the company name and unified business number (or local business registration number).
    - **Privacy Policy**.
    - **Terms of Service**.

### 2. Submit for Review and Enable Acquiring { #operate-au-payments-submit }

1. Provide your website link to the Airwallex service team for evaluation.
2. After the evaluation is complete, go to the **Acquiring** page in the Airwallex dashboard.
3. Follow the Airwallex instructions to [add payment methods](https://www.airwallex.com/docs/payments/get-started/payment-method-activation), and select the payment methods supported by the CYBERBIZ platform.

    - **Payment methods supported by CYBERBIZ**: Credit cards, Apple Pay, Google Pay, and Afterpay.

4. [Turn payment methods on or off](https://help.airwallex.com/hc/en-gb/articles/5898028587279-How-do-I-enable-or-disable-a-payment-method) as needed.

![](../../assets/images/Airwallex-前台-會員頁-收單-開啟收單功能01.en.png)


## Step 3: Connect to the CYBERBIZ Backend { #operate-au-payments-bind }

After you activate your account on the Airwallex side, the final step is to connect the two systems.

### 1. Get API Keys { #operate-au-payments-api-key }

Go to the Airwallex dashboard, **Account > Developer > API Keys**, and copy your **CLIENT ID** and **API key**.

![](../../assets/images/Airwallex-前台-帳戶-開發者-複製API密鑰01.en.png)

### 2. Enable Payments in CYBERBIZ { #operate-au-payments-enable }

1. Log in to the CYBERBIZ admin panel and go to **Payment and Logistics > Payment Settings**.
2. Find the **Airwallex** option and click Edit.
    ![](../../assets/images/澳洲站-後台-金物流-金流設定-啟用金流01.en.png)
3. In the **Enable Settings** section, enter the **CLIENT ID** and **API key** you just copied.
    ![](../../assets/images/澳洲站-後台-金物流-金流設定-串接API密鑰01.en.png)
4. Select the payment methods you want to enable on your website.
    ![](../../assets/images/澳洲站-後台-金物流-金流設定-開啟付款方式01.en.png)
5. Click Save to complete payment activation.



## Frequently Asked Questions { #faq-au-payments }

??? quote "Who should I contact about billing questions?"
    For questions about settlement timing, fee reconciliation, or failed transactions, we recommend contacting the [Airwallex Customer Support Center](https://www.airwallex.com/contact-us) directly for the fastest technical support.

