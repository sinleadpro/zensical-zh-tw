---
title: "CYBER Coins Topup Center Guide"
description: "A guide to the CYBER coins Topup Center, covering top-up steps, invoice information, payment methods, and usage history."
created: 2026-04-28 10:38
last_modified: 2026-07-22 15:51
lang: en-US
type: guide
author: Jase
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 儲值CYBER_幣
  - 填寫發票資訊
  - 查詢儲值紀錄
  - 匯出使用明細
features:
  - CYBER 幣儲值
  - 信用卡付款
  - 虛擬ATM轉帳
  - "SMS Billing"
  - EDM計費
prerequisites: []
related:
  - ec/notifications/manage-sms-templates-v2/
  - ec/notifications/send-edm-newsletters-v2/
tags:
  - "CYBER Coins"
  - "Topup Center"
  - "Top-Up Guide"
  - "Invoice Settings"
  - 簡訊計費
  - "EDM Billing"
acoiv: activate
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 儲值中心
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-management/points-deposits/"
comments: false
search:
  exclude: false
icon: lucide/wallet
hide:
---

![Topup Center](../../assets/images/ec-管理中心-儲值中心.en.png){ .hero-page }

## About CYBER Coins { #intro-cyber-coin }

CYBER coins are the CYBERBIZ platform's own points. You use them to pay for services on the platform, including:

- Sending SMS notifications
- Sending email newsletters (EDM)
- Other paid platform features

!!! warning "CYBER coins *can't be refunded* after purchase. Before you buy, confirm what you need and read the [CYBERBIZ Terms of Use](https://www.cyberbiz.io/terms-of-service/)."

## Page Overview { #overview-cyber-coin }

!!! path "Admin panel path: Website Management > Topup Center."

<div class="grid cards" markdown>

- :lucide-wallet:
  [__CYBER Coins Purchase Center__](#overview-cyber-coin-balance)

- :lucide-message-square:
  [__SMS Tracking Service__](#operate-points-sms)

- :lucide-mail:
  [__EDM Sending Service__](#operate-points-edm)

- :lucide-credit-card:
  [__Buy CYBER Coins Now__](#operate-cyber-coin-deposit)

- :lucide-receipt:
  [__Top-Up History__](#overview-cyber-coin-deposit)

- :lucide-file-text:
  [__Usage History__](#overview-cyber-coin-transactions)

- :lucide-download:
  [__Export Usage History__](#operate-cyber-coin-export)

</div>

## Check Your CYBER Coins Balance { #overview-cyber-coin-balance }

Shows your current balance and a link to top up.

![CYBER Coins Purchase Center](../../assets/images/ec-管理中心-儲值中心-CYBER幣購買中心.en.png)

??? plan "Plan Differences"
    If your account is on a PLUS or Enterprise plan, the system shows a "No top-up needed" message. Related fees are added to your statement automatically, so you don't need to top up manually.

## Service Pricing { #specs-cyber-coin-billing }

### SMS <small>SMS</small> { #operate-points-sms }

SMS messages are split into domestic and international messages based on the recipient, and each type costs a different number of CYBER coins.

!!! info "For SMS sending settings, see [How to Manage SMS Templates](../notifications/manage-sms-templates-v2.md){ title="Manage SMS Templates" }."

---

### Email Newsletters <small>EDM</small> { #operate-points-edm }

!!! info "For EDM sending settings, see [How to Send EDM Newsletters](../notifications/send-edm-newsletters-v2.md){ title="Set Up and Send EDM Newsletters" }."

## How to Top up CYBER Coins { #operate-cyber-coin-deposit }

!!! plan "Plan Differences"
    If your account is on a PLUS or Enterprise plan, the system shows a "No top-up needed" message. Related fees are added to your statement automatically, so you don't need to top up manually.

### Step 1: Enter the Top-Up Amount { #operate-cyber-coin-amount }

1. Log in to the CYBERBIZ admin panel, go to **Website Management > Topup Center**, and scroll down to the **Buy CYBER Coins Now** section.
2. Enter the amount you want to top up (in NTD) in the input box.
    - **Minimum top-up amount:** NT$1,200
    - **Maximum top-up amount:** NT$40,000
    - To buy more than 10,000 points at once, contact technical support at the bottom right, and they will prepare a quote based on your budget.
3. Click **Top Up** to open the purchase confirmation window.

---

### Step 2: Check the Top-Up Details { #operate-cyber-coin-confirm }

The purchase window shows:

- **Top-up amount:** The amount you entered
- **Tax**
- **Total:** Top-up amount + tax

---

### Step 3: Fill in the Invoice Information { #operate-cyber-coin-invoice }

Choose an invoice type and fill in the matching fields:

=== "Member Carrier (Personal)"

    ![Member carrier (personal)](../../assets/images/ec-管理中心-儲值中心-CYBER幣購買視窗-發票資訊-會員載具個人.en.png)

=== "Member Carrier (Company)"

    ![Member carrier (company)](../../assets/images/ec-管理中心-儲值中心-CYBER幣購買視窗-發票資訊-會員載具公司.en.png)

=== "Mobile Barcode Carrier"

    ![Mobile barcode carrier](../../assets/images/ec-管理中心-儲值中心-CYBER幣購買視窗-發票資訊-手機載具.en.png)

=== "Citizen Digital Certificate"

    ![Citizen digital certificate](../../assets/images/ec-管理中心-儲值中心-CYBER幣購買視窗-發票資訊-自然人憑證.en.png)

=== "Donation"

    ![Donation](../../assets/images/ec-管理中心-儲值中心-CYBER幣購買視窗-發票資訊-捐贈.en.png)

??? info "Required Fields"

    | Invoice type | Required fields |
    |----------|----------|
    | Member carrier (personal) | Email |
    | Member carrier (company) | Email, invoice title, tax ID number, company address, postal code |
    | Mobile barcode carrier | Email, mobile barcode |
    | Citizen digital certificate | Email, citizen digital certificate number |
    | Donation | Email, charity donation code |

!!! note "The e-invoice is sent to the email address you enter. The system **only provides e-invoices**. Duplicate or triplicate paper invoices are not available."

---

### Step 4: Choose a Payment Method { #operate-cyber-coin-pay }

=== ":lucide-credit-card: Credit Card"

    1. Select **Credit card payment**.
    2. Enter the card number, expiration date, and CVV in the credit card fields.
    3. Agree to the terms of service and click **Confirm**.
    4. The system takes you to a 3D Secure page to complete bank verification.
    5. After verification succeeds, the CYBER coins are **added to your account immediately**.

    ![Credit card payment](../../assets/images/ec-管理中心-儲值中心-CYBER幣購買視窗-付款方式-信用卡.en.png)

=== ":material-atm: Virtual ATM Transfer"

    1. Select **Virtual ATM transfer**.
    2. Agree to the terms of service and click **Confirm**.
    3. The system shows a page with your dedicated virtual account, including:
        - **Bank code**
        - **Transfer account number** (shown in red)
        - **Transfer amount**
        - **Payment deadline**

    !!! warning "ATM Transfer Notes"

        - Complete the transfer before the payment deadline (by default, **29 days** after you place the order). If you miss it, you need to place a new order.
        - **Transfer the full amount in one payment.** Don't split it into several transfers.
        - Don't set the transfer fee to be paid by the recipient.
        - You can pay by online banking, web ATM, a physical ATM, or a bank counter transfer.

            >  **Bank counter transfer**: You can pay at the counter of any financial institution except E.SUN Bank.

        - After the transfer, the CYBER coins are added automatically once the system confirms the payment.

## View Top-Up History { #overview-cyber-coin-deposit }

The **Top-Up History** table at the bottom of the page shows all of your past top-up transactions:

| Field | Description |
|------|------|
| Payment time | Date and time the transaction was completed |
| Amount | Actual amount paid (tax included) |
| CYBER coins | Points received from this top-up |
| Invoice number | E-invoice number (click to open the invoice link) |


!!! note "Search"

    The search box in the upper-right corner of the table does a **partial match** (not case-sensitive) across all fields on the **current page**. For example, enter `AB12` to find rows whose invoice number contains that string.
    *Search only covers the current page that has loaded. It doesn't search across pages.*

## View CYBER Coins Usage History { #overview-cyber-coin-transactions }

The **Usage History** table at the bottom of the page shows how your CYBER coins were spent:

| Field | Description |
|------|------|
| Type | Type of service used (such as SMS or EDM) |
| Time | When the charge occurred |
| CYBER coins | Number of points used |
| Details | Details of the charged item |

Use the pagination buttons below to see more records.

![Usage history](../../assets/images/ec-管理中心-儲值中心-明細紀錄.en.png)

## Export CYBER Coins Usage History { #operate-cyber-coin-export }

To download a report for reconciliation or analysis, use **Export Usage History**:

1. Choose a date range (click a shortcut: Last 7 days / Last 30 days / This month / Last month) or pick the start and end dates manually.
2. Click **Export**.
3. The system schedules the export and **sends an Excel (.xlsx) file to the email of the account that is logged in when it is done**.

!!! info "Only one export can run at a time. If you see "An export is already in progress," wait for the previous export to finish before you try again."

![Export usage history](../../assets/images/ec-管理中心-儲值中心-明細匯出.en.png)

## Next Steps { #next-steps-cyber-coin }

<div class="grid cards" markdown>

- :lucide-message-square-text:{ .lg }
  [__SMS Template Settings__](../notifications/manage-sms-templates-v2.md){ title="SMS Template Settings" }
   Set up the content and templates for automatic SMS messages.

- :lucide-mail:{ .lg }
  [__EDM Newsletter Settings__](../notifications/send-edm-newsletters-v2.md){ title="EDM Newsletter Settings" }
  Set up newsletter content and see how EDM is priced.

</div>

## FAQ { #faq-cyber-coin }

??? quote "How long does it take for CYBER coins to arrive after I top up?"

    With credit card payment, coins arrive **immediately** after verification. With ATM transfer, coins arrive after the system confirms the payment (usually within a few hours of the transfer).

??? quote "Can CYBER coins be refunded?"

    CYBER coins are **not refundable** after purchase. Confirm what you need before you buy.

??? quote "Can I change the invoice?"

    Invoice information can't be changed after payment is confirmed. Make sure it is correct before you buy.

??? quote "Why does a PLUS or Enterprise plan show "No top-up needed"?"

    If your account is on a PLUS or Enterprise plan, related fees are added to your statement automatically, so you don't need to top up manually. The system shows a "No top-up needed" message in the CYBER Coins Purchase Center section.

??? quote "What if I see "An export is already in progress" when exporting?"

    Only one export can run at a time. Wait for the previous export to finish before you try again. When it finishes, the system sends the Excel file to your email.

