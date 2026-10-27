---
title: "Wixtar E-Invoice Setup"
description: "Learn how to buy Wixtar e-invoices, connect and turn on the service, share it across multiple stores, and set up reconciliation invoices in the CYBERBIZ admin panel."
created: 2025-11-19 15:07
last_modified: 2026-07-03 11:44
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify FAQ
  - update internal links
  - add doc link [一鍵開立請款發票](https://www.cyberbiz.io/support/?p=2196)
  - add doc link [POS – 星益欣(美麗科技)電子發票(https://www.cyberbiz.io/support/?p=46379)
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 管理中心
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: advanced
tnb: branch
plans:
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 購買電子發票方案
  - 串接星益欣發票服務
  - 管理多站台發票共用
  - 設定企業版對帳請款發票
features:
  - 星益欣電子發票
  - 自動開立發票
  - 多站台共用帳戶
  - 對帳發票設定
prerequisites:
  - 需準備公司統一編號
related:
  - ec/website-management/one-click-invoice-issuance/
  - pos/third-party/wixtar-e-invoice/
tags:
  - "Information Security"
  - Payments
  - Invoices
  - Wixtar
  - "Meili Technology"
  - E-Invoice
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
paths:
  - 管理中心 > 發票設定
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4068
  - https://www.cyberbiz.io/support/?p=2693
permalink: "https://help.cyberbiz.io/ec/website-management/wixtar-e-invoice-setup/"
comments: ""
search:
  exclude: false
icon: lucide/receipt
hide:
---
# Wixtar E-Invoice Setup

Learn how to buy Wixtar e-invoices, connect and turn on the service, share it across multiple stores, and set up reconciliation invoices in the CYBERBIZ admin panel.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Advanced / Expert / all PLUS plans / Enterprise
{ .doc-badge }

## About Wixtar E-Invoices { #intro-wixtar-invoice }

This guide shows you how to set up Wixtar e-invoices in the CYBERBIZ admin panel, including buying a plan, connecting and turning on the service, sharing it across multiple stores, setting up reconciliation invoices, and renewing your account.

!!! info "Meili Technology Has Merged with Wixtar"
	Meili Technology has merged with Wixtar, so this guide refers to the related services as Wixtar. For Wixtar settings, follow the [announcements on the Wixtar website :lucide-external-link:](https://www.wixtar.com/product/e-invoice), or call 02-2711-9528 ext. 240. To import invoice tracks into the Wixtar admin panel, see the [invoice track import guide](https://www.cyberbiz.io/helpcenter/wp-content/uploads/美麗科技-增加字軌數量_匯入教學使用手冊-20230511.pdf).

## Requirements and Limits { #prerequisites-wixtar-invoice }

After you buy a plan, the system creates a Wixtar account automatically based on your tax ID number. **The account is bound to that tax ID number, and all invoices are issued under it.** The account supports the following invoicing cases:

- [x] Invoices for multiple EC websites
- [x] Invoices for offline POS systems
- [x] Billing invoices for Enterprise EC websites
- [x] Invoices for other channels (third-party platforms)

??? note "Invoicing Cases in Detail"
	|Case|Where to issue|Notes|
	|---|---|---|
	|**Multiple EC websites**|CYBERBIZ EC admin panel|See the section on sharing an account across stores to learn how to connect an existing Wixtar account.|
	|**Offline POS system**|CYBERBIZ EC admin panel|The account supports issuing invoices from 2 POS devices. For more POS devices, see the [POS guide](../../pos/third-party/wixtar-e-invoice.md){ title="Set Up Wixtar E-Invoices for POS" } for sub-device pricing and how to apply.|
	|**Billing invoices for Enterprise EC websites**|CYBERBIZ EC admin panel|Enterprise merchants whose consumer invoices are issued by CYBERBIZ can issue the billing invoices needed for reconciliation. See the section on connecting and turning on reconciliation invoices.|
	|**Other channels (third-party platforms)**|Wixtar admin panel|Merchants can work in the Wixtar admin panel. CYBERBIZ does not provide a guide for that process.|

!!! warning "All of the cases above use the same tax ID number. To issue invoices under a different tax ID number, buy a separate plan for each."

## Steps { #operate-wixtar-invoice }

### Buy a Wixtar Plan { #operate-wixtar-invoice-buy }

1. In the CYBERBIZ e-commerce admin panel, go to **Website Management > Invoices**.
2. Enter your tax ID number to verify the account.

	![Enter the tax ID number](../../assets/images/ec-e-invoices-wixtar.zh-tw.en.png){ title="Enter the Tax ID Number" }

3. Choose a plan and fill in the purchase information (plan, contact person, and company invoice information).

	![Choose a plan and buy](../../assets/images/ec-e-invoice-wixtar-02-buy-plan.en.png){ title="Choose a Plan and Buy" .screenshot }

4. After you pay, CYBERBIZ sends your contact information to a Wixtar specialist, who helps activate your account.

    <div class="grid cards" markdown>

    - ![System notification email](../../assets/images/ec-e-invoice-wixtar-03-email-notification.en.png){ title="System Notification Email" }
    - ![Information shown in the admin panel](../../assets/images/ec-e-invoice-wixtar-04-backend-info.en.png){ title="Information Shown in the Admin Panel" }

    </div>

    !!! tip "The system sends a notification email with the contact information, and the related information appears in the admin panel."

5. After your account is activated, fill in the connection information to turn on the service.

---

### Connect and Turn on the Service { #operate-wixtar-invoice-bind }

1. Log in to the Wixtar admin panel and go to **營業人資訊 > 選擇 POS 機 > 下載**.

    ![Download POS device information](../../assets/images/ec-e-invoice-wixtar-07-download-pos-info.en.png){ title="Download POS Device Information" .screenshot }

2. Copy the following information:

    - Store code
    - POS device code
    - POS serial number (PID)
    - Authentication code (RID)
    - Product name (PNAME)
    - AES KEY

    ![Copy the connection information](../../assets/images/ec-e-invoice-wixtar-08-copy-credentials.en.png){ title="Copy the Connection Information" .screenshot }

3. Paste it into the matching fields in the CYBERBIZ admin panel: **Website Management > Invoices > 星益欣電子發票設定**.

    ![Paste the connection information](../../assets/images/ec-e-invoice-wixtar-06-paste-credentials.en.png){ title="Paste the Connection Information" .screenshot }

4. In the **Checkout page invoice settings** section, turn on **Show invoice on checkout page** :lucide-toggle-right:. For **Invoice issuing vendor**, select **WiXtar E-Invoice**.

    ![Turn on checkout page invoices](../../assets/images/ec-e-invoice-wixtar-09-enable-invoice.en.png){ title="Turn On Checkout Page Invoices" .screenshot }

5. In the **Invoice issuance time** section, select one or more invoice issuance times. For the trigger conditions and limits of each option, see [Invoice issuance times](#specs-invoice-issuance-timing).

6. In the Wixtar admin panel, upload an image of your company invoice stamp. The stamp is then added to issued invoices automatically.

    ![Set up the company invoice stamp](../../assets/images/ec-e-invoice-wixtar-11-invoice-stamp.en.png){ title="Set Up the Company Invoice Stamp" .screenshot }

### Invoice Issuance Times { #specs-invoice-issuance-timing }

Choose **When paying**, **When shipping**, or **When picking up the goods** as the invoice issuance time, and the system issues e-invoices automatically based on the order status. The table below shows the trigger conditions and how the system handles each option.


| Invoice issuance time | Trigger condition | How the system handles it |
| :--- | :--- | :--- |
| **When paying** | The order payment status is **Payment received** | The system issues the invoice automatically |
| **When shipping (recommended)** | The order delivery status is **Partially shipped** or **Shipped** | As soon as the order is **shipped**, the system automatically issues an e-invoice for the whole order |
| **When picking up the goods** | The order delivery status is **Received** | The system issues the invoice automatically<br>**Only for shipping methods whose delivery status is connected to CYBERBIZ** |

**Option details**

=== "When Shipping"

    - **Recommendation**: Choose **When shipping** as the invoice issuance time. This prevents invoices from having to be voided when customers cancel orders before shipping.
    - **Returning the remaining items after a partial shipment**: If the unshipped items are returned after a **partial shipment**, the system automatically issues a partial allowance for the invoice.
    - **Example of issuing an invoice for a partial shipment**:

        1. An order ships in two parts: the first shipment on 9/11 at 18:00, and the remaining 3 items on 9/14 at 13:00.
        2. The system issues the e-invoice for the whole order at the first shipment (9/11 at 18:00), without waiting for all items to ship.

=== "When Picking Up the Goods"

    - **Recommendation**: With custom shipping, the system can't track delivery status, so the delivery status stays at **Shipped**. If you only select **When picking up the goods**, the system can't issue invoices automatically. We recommend also selecting **When shipping**.



---

### Share an Account Across Multiple EC Stores { #operate-wixtar-invoice-multi }

!!! warning "When stores share one Wixtar account, invoices for all of them are issued **under that account's tax ID number**."

If you have several EC stores and want to issue invoices with one Wixtar account, first buy a plan and finish connecting and turning on the service in one of the stores.

1. In that store, finish [buying a plan](#operate-wixtar-invoice-buy) and [connecting and turning on the service](#operate-wixtar-invoice-bind).
2. Go to each other EC store, enter the same tax ID number and connection information as the main store, and turn on the checkout page invoice settings.

    ![Shared multi-store settings](../../assets/images/ec-e-invoice-wixtar-12-multi-site-creds.en.png){ title="Shared Multi-Store Settings" .screenshot }

3. After you finish the checkout page invoice settings, you can issue invoices.

---

### Issue Invoices Under Different Tax ID Numbers { #operate-wixtar-invoice-tax-id }

If each store needs to issue invoices under a different tax ID number, do the following:

1. Enter a different tax ID number in each store, *buy a separate plan*, and complete a *separate connection* for each.
2. The system automatically creates a Wixtar account for each tax ID number.

!!! example "Examples"
    - Several EC stores each issue invoices under a different tax ID number → Each store buys its own plan and completes its own connection.
    - You run both EC and POS → Set a different tax ID number for each channel, buy separate plans, and complete each connection.

---

### Renew the Plan { #operate-wixtar-invoice-renew }

1. In the CYBERBIZ e-commerce admin panel, go to **Website Management > Invoices**.
2. Click **Renew** and fill in the checkout information to extend the service period.

    ![Renew the plan](../../assets/images/ec-e-invoice-wixtar-15-renewal.en.png){ title="Renew the Plan" .screenshot }

3. Choose a payment method: virtual ATM or credit card.

## FAQ { #faq-wixtar-invoice }

??? quote "Can one Wixtar account issue invoices under different tax ID numbers?"
    No. Each account is bound to one tax ID number. Buy a separate plan for each.

## Next Steps { #next-steps-wixtar-invoice }

<div class="grid cards" markdown>

-   :lucide-file-check:{ .lg .middle }
    [__One-Click Invoice Issuance__](one-click-invoice-issuance.md)
    Enterprise merchants who connect a Wixtar account can issue invoices with one click in the Reconciliation Center.

-   :lucide-store:{ .lg .middle }
    [__POS Guide__](../../pos/third-party/wixtar-e-invoice.md)
    Learn about sub-device pricing and how to apply for Wixtar e-invoices on POS.

-   :lucide-file-input:{ .lg .middle }
    [__Invoice Track Import Guide__](https://www.cyberbiz.io/helpcenter/wp-content/uploads/美麗科技-增加字軌數量_匯入教學使用手冊-20230511.pdf)
    A guide to importing invoice tracks into the Wixtar admin panel.

</div>

## References { #reference-wixtar-invoice }

- [Wixtar website](https://www.wixtar.com/product/e-invoice)
