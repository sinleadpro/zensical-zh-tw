---
title: "Set up ECPay E-Invoices"
description: "Learn how to connect CYBERBIZ to the ECPay e-invoice service, set when invoices are issued automatically, and manage invoice void rules."
created: 2026-06-26 18:40
last_modified: 2026-09-18 17:50
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
  - 管理中心
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
plan_options: []
cyb_extensions: []
intents: 
  - 串接綠界電子發票
  - 設定發票自動開立
  - 解決發票開立失敗問題
features: 
  - E-Invoice
  - 綠界串接
  - 自動開立
prerequisites: 
  - "申請綠界科技帳戶"
related: []
tags: 
  - "Green World ECPay"
  - 電子發票
  - ECPay
  - "Payment Integration"
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 發票設定
  - 結帳發票設定
paths: 
  - 管理中心 > 發票設定
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=3274
permalink: "https://help.cyberbiz.io/ec/website-management/ecpay-invoice/"
search:
  exclude: false
icon: lucide/receipt-text
hide: []
---

# Set up ECPay E-Invoices
Learn how to connect CYBERBIZ to the ECPay e-invoice service, set when invoices are issued automatically, and manage invoice void rules.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Advanced / Expert / all PLUS plans
{ .doc-badge }

## Requirements { #prerequisites-ecpay-invoice }

- [X] You must have a valid business registration, and your ECPay account must be at the **Business Member** or **Contracted Member** level or higher.
- [X] Your company must have a valid **business registration** in Taiwan.
- [X] Your company must not owe any confirmed business tax, profit-seeking enterprise income tax, or related fines.

## Before You Start { #prerequisites-ecpay-notes }

- **Invoice number tracks**: Check the invoice number tracks in the ECPay dashboard regularly to make sure you have enough. If they run out, the system can't issue invoices automatically.
- **Customer support**: For questions about ECPay account permissions or uploading invoice number tracks, contact ECPay Customer Service: 02-2655-1775.



## How to Apply { #operate-ecpay-invoice-apply }


1. First [apply for the ECPay service](https://member.ecpay.com.tw/MemberReg/MerchantRegister). For the application process, see the [ECPay instructions](https://www.ecpay.com.tw/Business/einvoice_knowledge_flow).
2. After you register and confirm that e-invoicing is active, complete the following settings.

## How to Connect { #operate-ecpay-invoice }

### Step 1: Get Your ECPay Integration Information { #operate-ecpay-invoice-keys }

Before you start, have your ECPay key information ready.

1. Log in to the [ECPay merchant dashboard](https://vendor.ecpay.com.tw/).
2. Go to **系統開發管理 > 系統介接設定**.
3. Copy the **Merchant ID (MerchantID)** and the e-invoice **integration HashKey** and **integration HashIV** shown on the page.

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-綠界02.png){ .screenshot }

### Step 2: Enter the Integration Information in the Admin Panel { #operate-ecpay-invoice-bind }

Enter the information you got into CYBERBIZ.

1. Log in to the CYBERBIZ admin panel and go to **Website Management > Invoices**.
2. In the ECPay Invoice Settings section, enter the **ECPay vendor number**, **HashKey**, and **HashIV**.

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-綠界01.png){ .screenshot }

3. In the Checkout Invoice Settings section, switch **Show invoice on checkout page** to `開啟 (ON)`.
4. In the Invoice issuance method dropdown, select **ECPay E-Invoice**.

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-綠界03.png){ .small-image }

### Step 3: Set When Invoices Are Issued { #operate-ecpay-invoice-timing }

In the **Invoice issuance time** section, select one or more invoice issuance times. For the trigger conditions and limits of each option, see [About invoice issuance times](#specs-invoice-issuance-timing).

## How the System Works { #specs-ecpay-invoice }

### About Invoice Issuance Times { #specs-invoice-issuance-timing }

When you select **When paying**, **When shipping**, or **When picking up the goods** as the invoice issuance time, the system issues e-invoices automatically based on the order status. The table below shows the trigger conditions and how the system handles each option.


| Invoice issuance time | Trigger condition | System action |
| :--- | :--- | :--- |
| **When paying** | The order payment status is **Payment received** | The system issues the invoice automatically |
| **When shipping (recommended)** | The order delivery status is **Partially shipped** or **Shipped** | As soon as the order is **shipped**, the system automatically issues an e-invoice for the whole order |
| **When picking up the goods** | The order delivery status is **Received** | The system issues the invoice automatically<br>**Only for shipping methods whose delivery status is integrated with CYBERBIZ** |

**Option details**

=== "When Shipping"

    - **Recommended setting**: Select **When shipping** as the invoice issuance time. This prevents invoices from being voided when customers cancel orders before shipping.
    - **Returning the remaining items after a partial shipment**: If the unshipped items are returned after a **partial shipment**, the system automatically issues a partial allowance for the invoice.
    - **Example of issuing an invoice for a partial shipment**:

        1. An order ships in two parts: the first shipment on 9/11 at 18:00, and the remaining 3 items on 9/14 at 13:00.
        2. The system issues the e-invoice for the whole order at the first shipment (9/11 at 18:00), without waiting for all items to ship.

=== "When Picking Up"

    - **Recommended setting**: If you use a custom shipping method, the system can't track delivery status, so the delivery status stays at **Shipped**. If you select only **When picking up the goods**, the system can't issue invoices automatically. Select **When shipping** as well.


### Cancellations and Returns { #specs-ecpay-invoice-return }

The system automatically updates the invoice with ECPay based on the order status:

| Order change | Automatic system action |
| :--- | :--- |
| **Full cancellation / full return** | The system automatically sends a request to ECPay to mark the e-invoice as **Invalid**. |
| **Partial return** | The system automatically creates an **allowance** for the returned amount. |



## FAQ { #faq-ecpay-invoice }

??? quote "Why does the invoice show Issuance failed?"
    Go to the order page and check the **order activity log** in the lower-left corner.

    Common reasons:
    - **No invoice number track available**: Upload more invoice number tracks in the ECPay dashboard, and then go back to the CYBERBIZ order and issue the invoice manually.
    - **Incorrect keys**: Check and update the merchant ID and HashKey/IV entered in the admin panel.
