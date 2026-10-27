---
title: "One-Click Invoice Issuance"
description: "Learn how to turn on and use one-click billing invoice issuance. Enterprise merchants who connect a Wixtar account can issue invoices with one click in the Reconciliation Center, which makes billing and payouts much faster."
created: 2026-06-09 18:45
last_modified: 2026-06-12 14:40
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules: 
  - 管理中心
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - Enterprise
plan_options: []
cyb_extensions: []
intents: 
  - 設定一鍵開立請款發票
  - 如何開立請款發票
  - 串接星益欣帳戶
features: 
  - 一鍵開立請款發票
  - 星益欣帳戶串接
  - "Reconciliation Center"
prerequisites: 
  - "需為企業版方案商家"
  - "需由 CYBERBIZ 代為開立發票"
related:
  - pos/third-party/wixtar-e-invoice/
  - ec/website-management/auto-deduction-of-arrears/
tags: 
  - "Billing Invoice"
  - Wixtar
  - 對帳中心
  - "Payout Process"
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 對帳中心
  - 請款發票設定
paths:
  - 管理中心 > 對帳中心
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=2196
permalink: "https://help.cyberbiz.io/ec/website-management/one-click-invoice-issuance/"
comments: false
search:
  exclude: false
icon: lucide/receipt
hide: []
---

# One-Click Invoice Issuance
Learn how to turn on and use one-click billing invoice issuance. Enterprise merchants who connect a Wixtar account can issue invoices with one click in the Reconciliation Center, which makes billing and payouts much faster.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Enterprise
{ .doc-badge }

!!! warning "Who This Applies To"
    This feature only applies to merchants on the **Enterprise plan** whose **consumer invoices are issued by CYBERBIZ**. If your Enterprise store issues its own consumer invoices, this guide does not apply.


## Before You Start { #prerequisites-one-click-invoice }

- **Prerequisite**: You must finish **connecting your Wixtar account** before you can use one-click issuance.
- **Limits**: The Wixtar reconciliation invoice account can only issue **reconciliation invoices**. To issue invoices for multiple channels, upgrade to the unlimited plan in the admin panel.

    !!! info "What the Wixtar Unlimited Plan Includes"
        After you buy the unlimited plan, you can issue invoices in the following cases in addition to reconciliation invoices:

        |Case|Where to issue|Notes|
        |---|---|---|
        |**Offline POS system**|CYBERBIZ EC admin panel|The account supports issuing invoices from 2 POS devices. For more POS devices, see the [POS guide](../../pos/third-party/wixtar-e-invoice.md#specs-wixtar-einvoice-fees) for sub-device pricing and how to apply |
        |**Other channels (third-party platforms)**|Wixtar admin panel|Merchants can work in the Wixtar admin panel. CYBERBIZ does not provide a guide for that process |

        > **Note** :lucide-triangle-alert: All of the cases above use the same tax ID number. To issue invoices under a different tax ID number, buy a separate plan for each.


## How to Turn It On { #operate-one-click-invoice }

### Step 1: Get a Wixtar Account { #operate-one-click-invoice-account }

Follow the connection method that matches when you bought your system:

=== "System Bought Before 2026/05/01"

    1. Log in to the CYBERBIZ admin panel and go to **Website Management > Reconciliation Center > 對帳發票設定**.
    2. Enter your tax ID number in the **VAT Number** field.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/電子發票-美麗科技13.png){ .screenshot }

    3. If you have not bought a Wixtar plan yet, complete the purchase.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/電子發票-美麗科技14.png){ .screenshot }


    !!! tip "On an Older Plan and Want to Upgrade?"
        If you bought your system before 2026/05/01 and want to upgrade to a plan that includes a Wixtar account, contact CYBERBIZ Customer Service.

=== "System Bought After 2026/05/01"

    1. After you buy and activate a CYBERBIZ system plan, CYBERBIZ applies for a Wixtar account on your behalf.

      - The **Statements E-Invoice** tab fills in your contact information automatically.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-商家資訊欄位01.png){ .screenshot }

    2. When Wixtar starts processing the application, the **statement list** shows a **reconciliation invoice setup reminder**.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-尚未啟用請款發票01.png){ .screenshot }

    3. Wait for the notification email from Wixtar.

        - Email subject: #{統編}-#{公司名稱} E-Invoice Integration

    4. Follow the email to log in to the Wixtar admin panel and get the **key integration information**.


### Step 2: Connect the Keys { #operate-one-click-invoice-keys }

1. In the Wixtar value-added center admin panel, go to **Business Information**, click the **POS device code** you want to set up invoicing for, and click **Download**.

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技07.png){ .screenshot }

2. Copy the following fields:

    - Store code
    - POS device code
    - POS serial number (PID)
    - Authentication code (RID)
    - Product name (PNAME)
    - AES KEY

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技08.png){ .screenshot }

3. Go to **Website Management > Reconciliation Center > 對帳發票設定** and paste the key information into the matching fields.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-請款發票串接欄位01.png){ .screenshot }



### Step 3: Set up the Company Invoice Stamp { #operate-one-click-invoice-stamp }

Log in to the Wixtar admin panel, go to **基本設定 > 圖片設定**, and upload an image of your company invoice stamp. The stamp is then added to issued invoice details automatically, so you don't need to stamp them by hand.

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技11.png){ .screenshot }


### Step 4: Turn on One-Click Issuance { #operate-one-click-invoice-enable }

=== "System Bought Before 2026/05/01"

    Go to **Website Management > Reconciliation Center** and click **Payment Request Invoice Settings** to turn on billing invoices.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票01.png){ .screenshot }


=== "System Bought After 2026/05/01"

    1. Go to **Website Management > Reconciliation Center** and click the **Payment Request Invoice Settings** tab.
    2. Switch **Enable billing invoices** to `開啟 (ON)`.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-開啟請款發票功能01.png){ .screenshot }

    #### Check the Setup Status { #operate-one-click-invoice-check }

    - **Setup complete / Enabled**

        The connection is successful when **Payment Request Invoice Settings** moves to the upper-left corner, and after you click it the feature is on and can't be turned off yourself.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-已啟用請款發票01.png){ .screenshot }

    - **Setup not complete**

        If the **Statements E-Invoice** reminder still appears in the statement list, check each connection step to make sure everything is set correctly.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-尚未啟用請款發票01.png){ .screenshot }

    !!! warning "Important"
        Make sure you finish connecting your Wixtar account. Otherwise, you can't see each period's payout amount or download statements.




## How to Issue Invoices { #operate-one-click-invoice-issue }

1. Before each period's payout, go to **Website Management > Reconciliation Center**.
2. After you check that the amount for the period is correct, click **Confirm Payment**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票02.png){ .screenshot }

3. The system automatically issues a billing invoice through your Wixtar account and starts the payout cycle.
4. Click the **Payment Invoice** button to view the details of the issued invoice.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票03.png){ .screenshot }



## Invoice Issuance Rules { #specs-one-click-invoice }

- **Invoice item**: Always listed as **Merchandise (one lot)**.
- **Invoice amount**: Equal to the **total amount to be invoiced** on the statement that doesn't require a credit note.
> Total amount to be invoiced = total of non-voucher order transactions where CYBERBIZ is the invoice issuer + total redeemed vouchers + refunds of voucher pick-any discount differences

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票04.png){ .screenshot }

- **Positive balance**: The system issues a **Payment Invoice**.
- **Negative balance**: The system issues a **Credit Note**.


    !!! info "How Credit Notes Are Issued"
        CYBERBIZ issues credit notes first. If the credit amount is larger than the total reconciliation invoices your store has accumulated, you must issue a paper credit note by hand for the excess. It can't be issued automatically in the admin panel.

        For example, if the current invoice total is negative NT$30,000 and your past reconciliation invoices add up to NT$20,000, you need to issue a NT$30,000 credit note by hand. It can't be issued in the admin panel.

## FAQ { #faq-one-click-invoice }

??? quote "How do I view credit note details?"
    Go to **Reconciliation Center** and click the **Credit Note** button to see the credit note details for that period.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票07.png){ .screenshot }

??? quote "What if the balance is negative?"
    If the reconciliation amount is negative, make sure you have turned on [automatic deduction of arrears](auto-deduction-of-arrears.md) and linked a credit card so that the system can deduct the arrears automatically.



