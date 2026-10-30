---
title: "Use 7-Eleven C2B Return Service"
description: "Set up and use 7-Eleven Return Service (C2B)"
created:
last_modified: 2026-07-02 21:42
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/returns-refunds/cvs-c2b-return/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 申請超商退貨便服務
  - 設定超商退貨便運費
  - 發送退貨便代碼給消費者
  - 協助消費者完成退貨寄件
  - 處理退貨包裹驗收與退款
features:
  - 7-11 超商退貨便 C2B
  - ibon 機台操作
  - 退貨便代碼
  - 退貨運費設定
prerequisites:
  - 已申請開通「超商大宗寄倉 (B2C)」服務
related:
  - ec/payments-and-logistics/setup-cvs-b2c-bulk-shipping/
  - ec/orders/order-return-process/
  - ec/orders/order-refund-process/
tags:
  - "Convenience Store Returns"
  - 7-Eleven
  - C2B
  - Returns
  - ibon
  - "Return Service"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=6178
  - https://www.cyberbiz.io/support/?p=34661
comments: false
search:
  exclude: false
icon: lucide/corner-down-left
hide:
---

![Convenience store Return Service C2B](../../../assets/images/ec-logistics-cvs-c2b-return.en.png){ title="Convenience Store Return Service C2B" .hero-page }

## About Convenience Store Pickup Return Service (C2B)

**Convenience store pickup Return Service (C2B)** lets shoppers send return packages back to you through **7-Eleven stores**.

!!! info-clean "Return Service Process Overview"

    ```mermaid
    graph LR
        subgraph Merchant
            A[Request return] --> B[Send return code]
        end
        subgraph Customer
            B --> C[Pack products]
            C --> D[Print shipping label at ibon]
            D --> E[Attach label and drop off at store]
        end
        subgraph System
            E --> F[Store ships to central warehouse<br>Merchant notified to collect and inspect]
        end
    ```

## Prerequisites and Limitations

- [x] **Plan limits:** This feature is mainly for **Enterprise** or **Expert PLUS** merchants.
- [x] **Requirements:** To use 7-Eleven C2B Return Service, you must first [apply for Convenience Store B2C Bulk Shipping](../../payments-and-logistics/setup-cvs-b2c-bulk-shipping.md).
- [x] **Original order:** The **original order doesn't need to have shipped by convenience store** to use Return Service. Whatever the original delivery type, you can use convenience store reverse logistics.
- [x] **Service fee:** Return Service currently costs a flat **NT$40** (whether you or the shopper pays). If you send the code by text message, an extra text message is sent.
- [x] **Code validity:** A Return Service code is valid for **the day it's requested plus six days (7 days total)**[^code-valid] and expires after that.

[^code-valid]: For example, if you create a Return Service code on July 1, it's valid through July 7 (7 days including the request day).

## Steps

### Step 1: Set Who Pays in the Admin

First decide who pays the return shipping fee. To set it:

1. Sign in to the CYBERBIZ admin and go to **Payment and Logistics > Convenience Store Logistics**.
2. In the **7-ELEVEN Convenience Store Return Service** section, click the edit :material-file-document-edit-outline: button to open the edit page.
3. Select **Merchant Pays** or **Shopper Pays**:
	- **Merchant Pays:** When you create a code, the system automatically deducts the fee from your **CYBER Coins**. If the code isn't used within 14 days, the coins are returned automatically.
	- **Shopper Pays:** The shopper pays the NT$40 shipping fee to the clerk when sending the package at a 7-Eleven store.

![Convenience store Return Service settings](../../../assets/images/ec-金物流-超商物流-超商退貨便-設定.en.gif){ title="Convenience Store Return Service Settings" }

---

### Step 2: Create and Send the Code in the Admin

After a customer requests a return, create a code as follows:

1. Go to **Orders > All Orders** in the admin and find the order.
2. Make sure the order's delivery status is **Received** (integrated logistics) or **Shipped** (custom logistics).
3. Select the order, click **More Actions** in the upper right, and select **Send Convenience Store Return Service Code and Change Delivery Status to Returning**.

    ![Send C2B convenience store Return Service code](../../../assets/images/ec-orders-cvs-c2b-return-send-code.en.png){ title="Send C2B Convenience Store Return Service Code" }

4. In the pop-up, choose whether to send the code to the shopper by **text message** or **email**, and then click **Confirm**.

    ![C2B convenience store Return Service send method pop-up](../../../assets/images/ec-orders-cvs-c2b-return-send-method-dialog.en.png){ title="C2B Convenience Store Return Service Send Method Pop-up" }

<!-- 5. You can see created Return Service codes in **Order Notes**. -->

---

### Step 3: Shopper Sends the Package

1. After receiving the Return Service code, the shopper packs the items.
2. At a 7-Eleven store, the shopper uses the **ibon kiosk** and enters the code to print the Return Service form (shipping label).
3. The shopper sticks the shipping label on the package and hands it to the store clerk.

!!! info "For details, see the [official Return Service guide :lucide-external-link:](https://www.7-11.com.tw/service/return.aspx)."

---

### Step 4: Inspect and Refund

• **Package return:** The convenience store sends the return package to the main warehouse, and the system sends a **CYBERBIZ 7-Eleven Return Service Arrival Notice** email telling you to pick it up.
• **Inspection:** After you receive the package, change the order's delivery status to **Reviewing Return** to inspect it.
• **Complete the return:** If everything checks out, change the status to **Returned**, and the system starts the automatic or manual refund process.

!!! info "To change the order's delivery status, see [Order Return Process](../order-return-process.md)."

## Next Steps

<div class="grid cards" markdown>

- :lucide-coins:{ .lg }  
  [__Refund Methods and Operations__](../order-refund-process.md)  
   Set your return and refund policy so customers understand the process and fees.

- :lucide-package-minus:{ .lg }  
  [__Order Return and Refund Process__](../order-return-process.md)  
   Process order returns and refunds.

</div>

## FAQ

??? quote "How do shoppers request convenience store Return Service?"  
	After the shopper requests a return from you, you create a Return Service code in the admin and notify the shopper.

??? quote "How long is a Return Service code valid?"  
	A Return Service code is valid for 7 days from the day it's created, and expires after that.

??? quote "Who pays the return shipping fee?"  
	You can choose **Merchant Pays** or **Shopper Pays** in the admin settings.

??? quote "What should I do after the package comes back?"  
	Receive the package > change the order's delivery status to **Reviewing Return** > after inspection, change it to **Returned** > the system starts the refund.

??? quote "Can I use Return Service if the original order didn't use convenience store logistics?"  
	Yes. Return Service doesn't restrict the original delivery type; you can use it to get any package back.
