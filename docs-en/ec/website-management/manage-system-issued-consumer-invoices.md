---
title: "Manage System-Issued Consumer Invoices"
description: "Learn about the CYBERBIZ service that issues consumer invoices on your behalf, including how invoices are issued, how customers and merchants look them up, and the request deadlines and fees for changing invoice information."
created: 2026-06-10 16:30
last_modified: 2026-09-18 10:50
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
  - 訂單
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
  - 了解系統代開發票服務
  - 查詢電子發票資訊
  - 修改發票統編資訊
features: 
  - 系統代開消費者發票
  - 電子發票載具
  - 發票修改申請
prerequisites: 
  - "需為企業版方案商家"
related: []
tags: 
  - E-Invoice
  - "Invoices Issued on Your Behalf"
  - "Tax ID Number Changes"
  - "Invoice Lookup"
acoiv: operation
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 訂單詳情
  - 會員中心
  - 簡訊通知樣板
paths: 
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=2319
  - https://www.cyberbiz.io/support/?p=5769
permalink: "https://help.cyberbiz.io/ec/website-management/manage-system-issued-consumer-invoices/"
comments: false
search:
  exclude: false
icon: lucide/file-text
hide: []
---

# Manage System-Issued Consumer Invoices
Learn about the CYBERBIZ service that issues consumer invoices on your behalf, including how invoices are issued, how customers and merchants look them up, and the request deadlines and fees for changing invoice information.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Enterprise
{ .doc-badge }

!!! warning "Who This Applies To"
    This feature only applies to merchants on the **Enterprise plan** whose **consumer invoices are issued by CYBERBIZ**. If your Enterprise store issues its own consumer invoices, this guide does not apply.


## Before You Start { #prerequisites-consumer-invoice }

- **Invoice format**: All invoices are issued as **e-invoices**. Paper invoices are not available.
- **Change limits**: Once an invoice is issued, customers can't ask to change the carrier type or switch between personal and company invoices, except to correct wrong information.

## How Invoices Are Issued { #operate-consumer-invoice-method }

Customers can choose one of the following invoice types at checkout, and the system issues the invoice automatically based on the payment status:

1. **Member carrier (personal)**

    - **How it is issued**: A cloud invoice is issued, and the system sends an email notification. No paper or electronic file is provided.
    - **Uniform invoice rules**:
        - Once a personal invoice is issued, it can't be changed or reissued as a company invoice.
        - To include a tax ID number, choose the **Company (tax ID)** invoice type instead.
        - Make sure the e-invoice carrier type is correct. It can't be changed after the invoice is issued.

2. **Company (tax ID)**

    - **How it is issued**: The e-invoice is sent to the customer's email as a PDF.
    - **Uniform invoice rules**:
        - Once a company invoice is issued, it can't be changed to a personal invoice.
        - Make sure the company tax ID number is correct. It can't be changed after the invoice is issued.

3. **Mobile barcode carrier**

    - **How it is issued**: The customer enters their mobile barcode (for example, `/ABC1234`).
    - **Uniform invoice rules**: Make sure the e-invoice carrier code is correct. It can't be changed after the invoice is issued.

4. **Citizen digital certificate**

    - **How it is issued**: The customer enters their citizen digital certificate number.
    - **Uniform invoice rules**: Make sure the e-invoice carrier code is correct. It can't be changed after the invoice is issued.

5. **Donated invoice**

    - **How it is issued**: The customer enters a donation code. If the code is wrong, the system donates the invoice to a default charity.
    - **Uniform invoice rules**: Make sure the e-invoice carrier code is correct. It can't be changed after the invoice is issued.


## When Invoices Are Issued { #operate-consumer-invoice-timing }

| Order type | Status field | Trigger status | Invoice action | How the system handles it |
| :--- | :--- | :--- | :--- | :--- |
| Cash on delivery | Delivery status | **Partially shipped**<br>**Shipped** | **Issue invoice** | As soon as the order is **shipped**, the system automatically issues an e-invoice for the whole order |
| Not cash on delivery | Payment status | **Payment received** | **Issue invoice** | The system issues the e-invoice automatically |
| Not cash on delivery | Payment status | **Payment failed** | **No invoice** | The transaction is not complete, so no invoice is created |
| Any | Payment status | **Partially refunded**<br>**Refunded** | **Issue allowance** | After the refund is complete, the system creates an allowance automatically<br>A partial refund creates a partial allowance |

**Option details**

=== "Invoice Rules for Cash-on-Delivery Orders"

    - **Returning the remaining items after a partial shipment**: If the unshipped items are returned after a **partial shipment**, the system automatically issues a partial allowance for the invoice.
    - **Example of issuing an invoice for a partial shipment**:

        1. An order ships in two parts: the first shipment on 9/11 at 18:00, and the remaining 3 items on 9/14 at 13:00.
        2. The system issues the e-invoice for the whole order at the first shipment (9/11 at 18:00), without waiting for all items to ship.


## Look up Invoice Information { #operate-consumer-invoice-query }

### For Customers { #operate-consumer-invoice-customer }

=== "On the Storefront"

    After logging in as a member, customers go to **訂單查詢 > 查看詳情** to see the invoice number in the invoice information field.

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊07.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊08.png){ .screenshot }

    </div>


=== "By Email"

    After the system issues an invoice, it sends a notification email. Customers can click the **invoice details** link in the email to view and download the e-invoice.

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊12.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊13.png){ .screenshot }

    </div>


### For Merchants { #operate-consumer-invoice-admin }

1. Log in to the CYBERBIZ admin panel and go to **Orders > All Orders**.
2. In the order list, click the **invoice number** link to see the invoice details.

![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊16.png){ .screenshot }


## Change Invoice Information { #operate-consumer-invoice-edit }

If a customer needs to add a tax ID number or correct invoice information, you must submit a request to CYBERBIZ, and the platform asks the value-added service center (Wixtar) to make the change.

### Request Process and Deadline { #operate-consumer-invoice-apply }

- **How to request**: Contact Customer Service and provide the order and invoice information to change.
- **Deadline**: Submit the request **by the 7th of the month after the invoice was issued** (earlier if that day is a holiday).

    > Example: For a July invoice, submit the request by August 7 at the latest.

- **Processing time**: About 3–5 business days (excluding holidays).

### Fees { #specs-consumer-invoice-fees }

- **Manual processing fee**: **NT$100 (tax included)** per request.


## Invoice Prize Notifications { #operate-consumer-invoice-prize }

After the lottery is drawn on the 25th of each odd-numbered month, the system automatically checks for winning invoices and notifies the buyers.

### How Notifications Are Sent { #specs-consumer-invoice-notify }

The system chooses the notification channel and sender based on the contact information saved with the invoice:

| **Member information** | **Notification channel** | **Sender** |
| :--- | :--- | :--- |
| Email address on file | **Email** | Wixtar |
| Mobile number only | **SMS** | CYBERBIZ |

!!! tip "SMS Notification Settings"
    If your store requires a mobile number and makes email optional, go to **Push Notifications > 簡訊通知樣板** and turn on **Invoice issued notification**. The system then notifies customers by SMS when they win.


### Claiming Prizes and Printing { #operate-consumer-invoice-claim }

After receiving the notification, customers can take the winning information to a **FamilyMart** store and use a **FamiPort** kiosk to print the paper invoice and claim the prize.

> CYBERBIZ pays the convenience store fee for printing winning invoices.

### Notes { #prerequisites-consumer-invoice-prize }

- **No reprints**: Under [National Taxation Bureau rules](https://www.etax.nat.gov.tw/etwmain/tax-info/innotative-tax-e-reference/startup/invoice/r5wmN0W), if a printed winning invoice is lost or damaged, neither the system nor the convenience store kiosk can reprint it.
- **Accurate information**: If a customer can't be notified because their contact information is wrong, the system does not send another notification and can't help with follow-up.


## FAQ { #faq-consumer-invoice }

??? quote "How can customers get a paper invoice?"
    The system only issues e-invoices. Paper invoices are not available.



