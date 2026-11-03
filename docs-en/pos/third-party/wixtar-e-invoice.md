---
title: "Set up POS Wixtar E-Invoice"
description: "Learn how CYBERBIZ POS connects with Wixtar e-invoicing, including plan fee calculation, back-office invoice settings, and purchase and activation steps."
created: 2026-06-10 17:50
last_modified: 2026-06-30 21:55
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
  - 管理中心
  - POS 功能
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: branch
plans: 
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents: 
  - 串接 POS 電子發票
  - 購買 POS 發票子機
  - 設定星益欣發票
features: 
  - POS 電子發票
  - 星益欣串接
prerequisites: 
  - "需擁有星益欣電子發票帳戶"
  - "需為企業版方案商家"
related: []
tags: 
  - POS
  - e-invoice
  - Wixtar
  - "Meili Technology"
acoiv: activate
apis: []
devices: 
  - desktop
ui_components: 
  - 發票設定
  - POS 商店列表
paths:
  - 管理中心 > 發票設定 > POS
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=46379
permalink: "https://help.cyberbiz.io/pos/third-party/wixtar-e-invoice/"
search:
  exclude: false
icon: lucide/receipt
hide: []
---

# Set up POS Wixtar E-Invoice
Learn how CYBERBIZ POS connects with Wixtar e-invoicing. This covers plan fee calculation, back-office invoice settings, and purchase and activation steps.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }


## Usage Notes

- **Name change**: Meili Technology was renamed **Wixtar** in May 2024. The system interface and this document both use the new name.
- **Payment restriction**: Only **credit card payment** is supported.
- **Invoice range pre-fetching**: To prevent invoicing failures caused by unstable networks, the system pre-fetches invoice number ranges to each POS terminal based on average usage. Pre-fetched ranges cannot be transferred to other POS terminals or the EC storefront. For special requirements, contact customer support. Fees may apply depending on the adjustment.
- **Check before importing invoice ranges**: Before you import invoice number ranges, **be sure to confirm that the range is not already in use on another value-added center platform**. If an incorrect range causes **duplicate invoices**, the system cannot help with reissuing or voiding them. **Merchants must contact the National Taxation Bureau and handle the matter according to applicable regulations.**

## Plan Pricing

### Base Plan Details

  - A Wixtar account is created per Unified Business Number (UBN). After you purchase a plan with your company UBN, the system automatically activates the corresponding account, and you can use the invoicing feature.
  - One Wixtar account supports multiple EC storefronts, 2 POS terminals, and other sales channels.


### Add-On POS Terminal Fee Calculation

  Add-on POS terminals are billed by combining pricing tiers with remaining months until expiry. The basic rules are as follows:

  - **Pricing tier**: Every 2 terminals form one group.
  - **Terminals 1-2 (first tier)**: Tier fee × **remaining months until UBN expiry**
  - **Terminals 3-4 (second tier)**: Next tier fee × **remaining months until UBN expiry**
  - **Additional terminals**: The same logic applies. Every additional 2 terminals moves to the next tier fee calculation.

!!! info "Calculating Remaining Months Until UBN Expiry"
    - **Billing end date**: Billing always runs until the expiry date of the original verified UBN.
    - **No charge for partial months**: If a terminal is activated in the middle of a month and the month is not fully used (for example, activated mid-month or at month end), that month is not charged. Remaining months start counting from the first day of the next month.
    - **Example**: Suppose your UBN verification expires on **Dec 31**:

        - **Scenario A (activated mid-month)**:
          If you activate a terminal on **Aug 15**, August is not fully used, so the system will **not charge for August**. Billing starts on Sep 1 and runs through Dec 31. The remaining months are **4 months** (Sep, Oct, Nov, Dec).
        - **Scenario B (activated at the start of the month)**:
          If you activate a terminal on **Aug 1**, the full month of August is used, so billing starts in August. Billing runs from Aug 1 through Dec 31, and the remaining months are **5 months**.

### Checkout Amount Calculation

  - If you already purchased a Wixtar plan, the plan includes 2 POS terminals. If you need additional POS terminals, **you only need to pay the add-on POS terminal fee**.
  - If you have not purchased a Wixtar plan, you must purchase one. If you also need additional POS terminals, the total amount is **plan fee + add-on POS terminal fee**.


### Scenario Examples

1. **First purchase** (apply for the base plan and add 1 terminal)

    - **Merchant scenario**: A new store is opening and needs 3 POS terminals in total.
    - **Billing logic**:
        - First 2 terminals: Included in the base plan and billed at the base plan rate.
        - Terminal 3: Exceeds the base plan allowance, so the system automatically triggers first-tier billing.
    - **Formula**: Checkout amount = base plan amount + terminal 3 POS fee (first-tier fee × remaining months until UBN expiry)
    - **Access granted**: Because terminals are unlocked in groups of 2, the merchant immediately gets installation and use rights for POS terminals 3 and 4.

2. **Expansion within the same tier** (adding terminal 4 within the invoice validity period)

    - **Merchant scenario**: After operating for a while, the store decides to officially activate POS terminal 4 for a holiday promotion.
    - **Billing logic**:
        - Because terminals 3 and 4 were bundled into the same pricing tier and unlocked during the first purchase, and the merchant already paid that tier's fee.
    - **Formula**: Checkout amount = NT$0
    - **Access granted**: The merchant does not need to pay extra. You can go directly to the back office to activate and bind POS terminal 4.

3. **Adding across tiers again** (later store expansion requires terminal 5)

    - **Merchant scenario**: The following year, business expands and the store needs to add POS terminal 5.
    - **Billing logic**:
        - Terminal 5 exceeds the capacity of the previous tier (terminals 3-4), so the system automatically moves up and triggers billing for the next tier.
    - **Formula**: Checkout amount = terminal 5 POS fee (second-tier fee × remaining months until UBN expiry)
    - **Access granted**: After payment, the system unlocks terminals 5 and 6 together, so the merchant gets access to both.


## Operating Procedure

### Step 1: Set up POS Invoice Settings in the Back Office

Before purchasing a plan, you must first complete the initial setup of the invoice machine and service provider on the designated POS host.

1. Log in to the CYBERBIZ admin panel and go to **POS > POS Store List**.
2. Click the store you want to set up, select the target POS host in the "POS System List," and click **Edit POS Settings**.
3. Go to the **POS Invoice Settings (Store Manager Only)** section, complete the following settings, and click **Save**:
    - **Invoice settings**: Select `星益欣(美麗科技)`.
    - **Invoice machine settings**: Select the invoice machine that matches your on-site hardware model.

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/POS美麗科技01.png){ .small-image }

### Step 2: Purchase Wixtar POS Terminal Licenses

After completing the initial setup, purchase the corresponding terminal licenses.

1. Go to **Website Management > Invoices** and click the **POS** tab.
2. Enter your **Company Unified Business Number** to verify.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS美麗科技02.png){ .screenshot }

3. On the **Select POS Terminal** page, check the POS terminals you want to purchase.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS美麗科技03.png){ .screenshot }

4. Go to the **Purchase Checkout** page and enter the contact and company invoice information.

    - **Plan selection**: Choose a 1-year or 2-year term (first purchase includes 2 extra months).
    - **Payment method**: Complete payment with a credit card.

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/POS美麗科技04.png){ .screenshot }

### Step 3: Connect and Activate

After payment, get the authentication information from Wixtar and enter it in the CYBERBIZ admin panel.

The system pre-fills the "Store Code," "POS Machine Code," "POS Serial Number (PID)," and "Product Name (PNAME)" fields.

![](https://www.cyberbiz.io/support/wp-content/uploads/POS美麗科技06.png){ .small-image }

1. Log in to the "Wixtar Value-Added Center Back Office" and go to **Business Information**.
2. Select the corresponding **Store Code** and **POS Machine Code**, then click **Download**.

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技07.png){ .screenshot }

3. In the downloaded file, copy the **Authentication Code (RID)** and **AES KEY**.

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技08.png){ .small-image }

4. Return to the CYBERBIZ admin panel, go to **Website Management > Invoices > POS**, paste the information into the matching fields, and save.
5. After the connection succeeds, the POS terminal status changes from "Applying" to **Active**.

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/POS美麗科技07.png){ .small-image }


## FAQ

??? quote "If the network is unstable, can POS still issue invoices?"
    Yes. The system pre-fetches invoice number ranges to each POS terminal so invoicing still works normally when offline or the network is unstable.

??? quote "How long after purchase is the service activated?"
    After payment, CYBERBIZ sends your information to Wixtar. A Wixtar representative will then contact you to help with activation. Processing usually takes about 3-5 business days.

??? quote "Can POS invoice number ranges be transferred to the EC storefront?"
    No. Pre-fetched invoice number ranges on a POS terminal can only be used on that terminal. They cannot be transferred to other POS terminals or the EC storefront.
