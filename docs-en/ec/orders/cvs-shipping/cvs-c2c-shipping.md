---
title: "Ship with Convenience Store C2C Store-to-Store"
description: "Pack products and send them through convenience store C2C store-to-store shipping to the store the shopper chose, including the full steps and notes."
created:
last_modified: 2026-06-30 11:11
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/cvs-shipping/cvs-c2c-shipping/"
type: guide
author: Jase
reviewers: []
notes:
  - add 儲值 CYBER 幣 doc link
  - add 熱感列印 doc link
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents:
  - 超商店到店出貨
  - 超商寄件
  - 列印託運單
  - 處理物流異常
  - 了解超商寄件規範
features:
  - 超商店到店 C2C
  - 7-ELEVEN 交貨便
  - 全家店到店
  - 萊爾富超商取貨
  - 貨到付款
  - 熱感列印
  - ibon 列印
  - FamiPort列印
prerequisites:
  - 開通CYBERBIZ PAYMENTS (貨到付款)
  - 一般版商家需儲值CYBER幣
  - 正確設定寄件人資訊
related:
  - ec/website-management/points-deposits/
  - ec/orders/basics/order-fulfillment-flow/
  - ec/orders/cvs-shipping/thermal-print-cvs-waybill/
  - ec/orders/references/cvs-waybill-expiration-reference/
  - ec/orders/renew-waybill-after-expiration/
  - ec/orders/cvs-shipping/family-mart-frozen-c2c/
  - ec/website-management/setup-store-basic-info/
tags:
  - "Convenience Store Store-to-Store"
  - C2C
  - "Convenience Store Drop-Off"
  - "Logistics Shipping"
  - "Shipping Labels"
  - "7-Eleven Store-to-Store"
  - "FamilyMart Store-to-Store"
  - Hi-Life
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
  - 訂單 > 訂單報表匯出
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=120
  - https://www.cyberbiz.io/helpcenter/?p=6856
  - https://www.cyberbiz.io/support/?p=980
comments: false
search:
  exclude: false
icon: lucide/store
hide:
---

![C2C download shipping labels](../../../assets/images/ec-訂單-店到店下載托運單.en.png){ title="C2C: Download Shipping Labels" .hero-page }

## About Convenience Store Store-to-Store Shipping { #intro-cvs-c2c }

Convenience store store-to-store (C2C) shipping means "from one convenience store to another": you drop off the package at a store, and the customer picks it up at their chosen store. Supported convenience store logistics services:

- **7-Eleven (Delivery Service)**
- **FamilyMart (Store-to-Store)**
- **Hi-Life (Convenience Store Pickup)**

Customers can choose **Pickup Without Payment** (pay at checkout) or **Pickup with Payment (COD, Cash on Delivery)** (pay at store pickup).

## Prerequisites and Limitations { #prerequisites-cvs-c2c }

Before shipping, make sure the following are set up:

- [x] **Company sender name and mobile number**: Set the sender's correct legal name and mobile number in the admin. If the customer doesn't pick up the package and it's returned, store staff check the sender's ID before releasing the package.
- [x] **Top up CYBER Coins (Standard Plan)**: Standard Plan merchants must [top up CYBER Coins](../../website-management/points-deposits.md#operate-cyber-coin-deposit) in "Management Center > Top-Up Center" before printing shipping labels. Labels can't be printed with an insufficient balance. PLUS / Enterprise plans don't need manual top-ups; fees are charged on each statement.
- [x] **Turn on CYBERBIZ PAYMENTS (for Cash on Delivery)**: Convenience store "Cash on Delivery" is available only to merchants with CYBERBIZ PAYMENTS turned on. See the requirements below.

??? plan "Requirements for Convenience Store "Cash on Delivery""
    **Cash on Delivery (COD)** for convenience store store-to-store shipping is available only to merchants with **CYBERBIZ PAYMENTS** turned on. Once it's on, the system automatically adds a "Cash on Delivery" option to store-to-store delivery methods such as 7-Eleven and FamilyMart, and customers pay when they pick up at the store.

    ??? info-clean "What Is CYBERBIZ PAYMENTS?"
        **CYBERBIZ PAYMENTS** is CYBERBIZ's all-in-one payment and logistics service. It provides payment collection services so customers can pay quickly and securely. Features include:

        - **Very low transaction fees**
        - **All-in-one payment and logistics integration**
        - **PCI DSS security certification**

        How to turn it on depends on your plan:

        - **PLUS / Enterprise**: CYBERBIZ PAYMENTS is built in, so you can use convenience store Cash on Delivery directly.
        - **Standard Plan**: Apply for CYBERBIZ PAYMENTS in the admin and complete the individual account risk assessment form. It's turned on after approval.

---

## Steps { #operate-cvs-c2c }

### Step 1: Check Shipping Conditions { #operate-cvs-c2c-check }

Depending on the customer's payment method, make sure the order status meets the shipping conditions:

- **Pickup Without Payment (prepaid)**: The order's payment status must be "**Payment Received**" before you can ship.
- **Pickup with Payment (COD)**: You can ship when the order's delivery status shows "**Cash on Delivery**"[^cod-plan].

[^cod-plan]: Cash on Delivery (COD) is available only to merchants with CYBERBIZ PAYMENTS turned on. See [Prerequisites and Limitations](#prerequisites-cvs-c2c) for the requirements.

---

### Step 2: Get Tracking Numbers and Download Shipping Labels { #operate-cvs-c2c-download }

1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders**.
2. Select orders with the same delivery method (such as Hi-Life Cash on Delivery).
3. Click **Actions...** > **Download Store-to-Store Shipping Labels and Change to Shipped** in the upper right. We recommend selecting up to **20 orders** at a time to avoid tracking number failures on the convenience store side.

    !!! warning "Once the delivery status is "Shipped," the delivery information and order statuses can't be changed."

4. The system generates a shipping label archive (ZIP) with shipping labels, packing slips, order details, and a pick list. For details, see [Shipping Label Archive Contents](../basics/order-fulfillment-flow.md#operate-fulfillment-zip){ data-preview }.

    ??? example-clean "Shipping Label Archive Contents"
        ![Shipping label archive contents](../../../assets/images/ec-訂單-所有訂單-託運單壓縮檔內容.en.png)

    !!! warning "If the archive won't download, check whether the browser is blocking pop-ups."

![C2C download shipping labels](../../../assets/images/ec-訂單-所有訂單-c2c下載託運單.en.png)

---

### Step 3: Print and Attach Labels { #operate-cvs-c2c-print }

!!! tip "We recommend a laser printer so labels are easier to read."

!!! warning "Special Characters in Vendor Names on 7-Eleven Shipping Labels"
	Special characters in the vendor name on 7-Eleven shipping labels cause order creation to fail, so the system automatically converts them to "_" (transactions aren't affected). If special characters prevent the buyer from picking up the package, it's returned by home delivery and you're charged the return shipping fee.

#### Regular Printing

- Use A4 paper or label stickers, up to 4 labels per page (2x2 format).
- [Example of commercial A4 label stickers :lucide-external-link:](https://shopee.tw/%E3%80%90A4%E3%80%91A4%E7%A9%BA%E7%99%BD%E8%B2%BC%E7%B4%99-2%C3%972-%E8%B2%BC%E7%B4%99-A6%E8%87%AA%E9%BB%8F%E6%A8%99%E7%B1%A4%E8%B2%BC%E7%B4%99-A4%E6%A8%A1%E9%80%A0%E8%B2%BC%E7%B4%99-%E9%9B%BB%E8%85%A6%E6%A8%99%E7%B1%A4%E8%B2%BC%E7%B4%99-%E5%8F%AF%E9%9B%B7%E5%B0%84-%E5%99%B4%E5%A2%A8-1%E5%8C%85100%E5%BC%B5-10%E5%8C%85%E5%85%8D%E9%81%8B-i.24728499.2550119685), for reference only.

??? example-clean "Example"
    ![](../../../assets/images/ec-訂單-超商托運單-一般列印.en.png)

---

#### Thermal Printing <small>A6</small>

- Supports 7-Eleven and FamilyMart C2C, and only from the "new order list." Learn [how to thermal print convenience store shipping labels](thermal-print-cvs-waybill.md){ title="Thermal Print Convenience Store Shipping Labels" }.

!!! plan "Thermal printing is available only on PLUS and Enterprise plans."



---

#### Print at the Convenience Store

- Print the service slip at the store's kiosk (ibon / FamiPort).
- You need the tracking number (Delivery Service code).

=== "ibon"

    1. **Look up the tracking number**

        - Sign in to the CYBERBIZ admin and go to **Orders > Order Data Export**.
        - Click **Tracking Number** to add it to the selected fields.
        - Click **Save** to apply the change, then export.
        - Open the exported file to find the tracking number (Delivery Service code) in the **Tracking Number** column.

        ![](../../../assets/images/ec-訂單-訂單報表匯出-托運單號.en.gif)

    2. **Use the ibon kiosk**

        - On the ibon home screen, tap **Services** > **Delivery Service** > **Ship**.
        - Choose to enter the Delivery Service code manually.
        - Confirm the sender and recipient information.

    3. **Print the slip**: After confirming, wait for the kiosk to print the payment slip.

    4. **Send the package**

        - Take the slip to the counter to get a "Delivery Service plastic sleeve," put the slip in it, and stick it on the package.
        - If you sell through 7-Eleven's seller service, you can batch-generate QR codes in the app to print multiple orders quickly.


=== "FamiPort"

    1. **Look up the pickup number**

        - Sign in to the CYBERBIZ admin and go to **Orders > Order Data Export**.
        - Click **Pickup Number** to add it to the selected fields.
        - Click **Save** to apply the change, then export.
        - Open the exported file to find the shipment number in the **Pickup Number** column.

        ![](../../../assets/images/ec-訂單-訂單報表匯出-超取編號.en.gif)

    2. **Use the FamiPort kiosk**

        - On the home screen, tap **Services/Shipping > Store-to-Store > FamilyMart Platform Shipping > Ship**.
        - Enter the "shipping code/number" provided by the platform.
        - Enter the order amount: For Cash on Delivery, the store collects payment, so enter the order amount. For Pickup Without Payment, the store collects nothing, so enter 0.
        - Enter the "last three digits of the sender's mobile number" to verify.
        - After checking the shipping information, tap "Confirm" and print the payment slip.

    3. **Pay and attach the label**: Take the slip and package to the counter, pay, and stick the shipping label on the package.

    !!! info "Recommendations"

        - Make sure the sender and recipient information (address / name) is correct; it can't be changed after printing.
        - Stick the printed label in the most visible spot on the package.

---

### Step 4: Drop Off at the Store { #operate-cvs-c2c-dropoff }

If you drop off a package and the store's logistics truck hasn't collected that day, the customer can usually pick it up two days later (drop-off day + 2). Some stores are excluded; see the [7-Eleven excluded store list :lucide-external-link:](https://www.7-11.com.tw/form/store.pdf). FamilyMart has no exclusions.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Validity by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See each convenience store's reprint deadline and expiration rules.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label has expired or is past the reprint deadline, get a new tracking number and download a new shipping label.

</div>

---

### Step 5: Arrival SMS Notifications { #operate-cvs-c2c-notify }

- When the item arrives at the store, the CYBERBIZ delivery status changes to "Arrived at Store," and a pickup SMS is sent to the "customer."
- CYBERBIZ pickup SMS notifications:

    - 7-Eleven: one on day 1 and one on day 4 after arrival.
    - FamilyMart: one on day 1 and one on day 3 after arrival.
    - Hi-Life: one on day 1 and one on day 3 after arrival.

- If the customer doesn't pick up the package and it's returned to the original sending store, an SMS is sent to the "sender."

!!! note "Convenience Store Tracking Systems"

    - 7-Eleven tracking [link :lucide-external-link:](https://eservice.7-11.com.tw/e-tracking/search.aspx).
    - FamilyMart tracking [link :lucide-external-link:](https://fmec.famiport.com.tw/FP_Entrance/QueryBox).
    - Hi-Life tracking [link :lucide-external-link:](https://www.hilife.com.tw/serviceInfo_search.aspx).

---

## Important Rules and Limitations { #specs-cvs-c2c }

!!! info "7-Eleven and FamilyMart provide official shipping procedures and sell packaging materials. See their official websites."

### Size and Weight { #specs-cvs-c2c-size }

- The sum of the package's three sides must be ≤ 105 cm, with the longest side ≤ 45 cm.
- Weight limit: generally ≤ 5 kg; 7-Eleven C2C ≤ 10 kg.
- When limits are exceeded, convenience store options are hidden on the checkout page automatically.

---

### Packaging Rules { #specs-cvs-c2c-packaging }

- Items must be fully packaged, not exposed.
- Don't use PP bags, drawstrings, or Styrofoam packaging.
- Stick barcode labels flat on a wide side. **Don't fold or resize them**, or scanning may fail.
- Don't ship fragile items; you're responsible for any breakage. If the item damages or stains other merchants' items, you're fully liable for compensation.

![](../../../assets/images/ec-訂單-超商店到店包裹異常範例.en.png)

---

### Prohibited Items { #specs-cvs-c2c-prohibited }

- Dangerous or prohibited items (firearms, explosives, knives, toxic substances)
- Cash, negotiable instruments, precious metals, jewelry, antiques
- Credit cards, ATM cards, ID documents
- Live animals and plants, pets
- Blood, urine, specimens
- Fragile items or electronics (computers, phones, cameras)
- Strong-smelling items such as durian or salted fish

---

## Handle Exceptions { #operate-cvs-c2c-exception }

### Reprint Shipping Labels { #operate-cvs-b2c-shipping-reprint }

If a label is lost or damaged, you can reprint it in the admin before the deadline.

1. Select the orders to reprint in the order list.
2. Open the **Actions...** drop-down and select **Reprint Shipping Label**.
3. The system downloads the PDF with the same tracking number again. **Shipping fees aren't charged again**, and the order status doesn't change.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Validity by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See each convenience store's reprint deadline and expiration rules.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label has expired or is past the reprint deadline, get a new tracking number and download a new shipping label.

</div>

### Customer Doesn't Pick Up in Time { #operate-cvs-c2c-exception-overdue }

- The package is returned to the original sending store at no extra cost to you.
- The system sends an SMS asking the sender to collect it.
- The sender must show ID to collect it, so **the company sender name must be correct**.
- If it isn't collected within 7 days, the package goes to the logistics center and is sent back to your address by "**home delivery, freight collect**."

!!! note-clean "Unclaimed Package Process"

    ```mermaid
    graph LR
      A[1. Initial hold<br>Not picked up for 7 days] --> B;
      B[2. Return shipping starts<br>Package sent to<br>original sending store<br>(1-3 days)] --> C;
      C[3. Merchant pickup<br>Go to the<br>original sending store<br>to collect the package] --> D;
      D[4. Pickup deadline<br>applies] --> E;
      E{Did the merchant<br>collect it<br>in time?};
      E -- Yes --> F(Process ends<br>Package<br>collected)
      E -- No --> G(Package destroyed)

      style E fill:#fff

    ```

---

### Store Closures <small>Closed</small> { #operate-cvs-c2c-exception-store-closed }

- **7-Eleven**: The CYBERBIZ system sends a notification email. Within 2 days of receiving it, contact the customer, find the order in the admin, and choose a new 7-Eleven store on the order details page.
- **FamilyMart**: The CYBERBIZ system sends a notification email. Within 6 days of receiving it, contact the customer, find the order in the admin, and choose a new FamilyMart store on the order details page.
- **Hi-Life**: The CYBERBIZ system sends a notification email. Within 2 days of receiving it, contact the customer, find the order in the admin, and choose a new Hi-Life store on the order details page.

---

### Partial Shipment { #operate-cvs-c2c-exception-partial }

- If an order ships in batches, **the second shipment can't use convenience store delivery** and must use home delivery.
- For Cash on Delivery orders, the customer pays **the full order amount** when receiving the first package.

---

## Related Tasks { #next-steps-cvs-c2c }

<div class="grid cards" markdown>

- :lucide-printer:{ .lg }  
  [__Convenience Store Thermal Printing__](thermal-print-cvs-waybill.md){ title="Thermal Print Convenience Store Shipping Labels" }  
  Print convenience store shipping labels with a thermal printer.

- :lucide-snowflake:{ .lg }  
  [__FamilyMart Frozen Store-to-Store__](family-mart-frozen-c2c){ title="Ship with FamilyMart Frozen C2C Store-to-Store" }  
  Set product delivery conditions to limit which logistics methods are shown and used at checkout.

</div>

## FAQ { #faq-cvs-c2c }

??? quote "My orders don't have a "Convenience Store Cash on Delivery" option. How do I turn it on?"
    [](){ #faq-cvs-c2c-cod-enable }
    Convenience store store-to-store Cash on Delivery requires the **CYBERBIZ PAYMENTS** payment service:

    - **PLUS / Enterprise**: Built into the plan; no separate application needed.
    - **Standard Plan**: Apply for CYBERBIZ PAYMENTS in the admin and complete the individual account risk assessment form. After approval, a "Cash on Delivery" option is automatically added to store-to-store delivery methods.

??? quote "What happens if the customer doesn't pick up the package in time?"
    [](){ #faq-cvs-c2c-overdue }
    If the customer doesn't pick up the package within the specified time, the system handles it automatically:

    1. The package is returned to the original sending store at no extra cost to you.
    2. The system sends an SMS asking the sender to collect it.
    3. The sender must show ID to collect it, so **the company sender name must be correct**.
    4. If it isn't collected within 7 days, the package goes to the Uni-President Logistics / Ri Yi / Hi-Life logistics center and is sent back to you by "home delivery, freight collect."
    5. The "home delivery, freight collect" address is set in EC admin > General Settings > [Company Logistics Address](../../website-management/setup-store-basic-info.md#operate-general-preferences-return-address){ title="Set Up Basic Website Information" }. Make sure it's set and complete.

??? quote "Can I keep using convenience store delivery if an order ships in batches?"
    [](){ #faq-cvs-c2c-partial }
    If an order ships in batches, note these convenience store delivery limits:

    - The second shipment can't use convenience store delivery and must use home delivery.
    - For Cash on Delivery orders, the customer must pay **the full order amount** when receiving the first package.

??? quote "What if printing shipping labels fails?"
    [](){ #faq-cvs-c2c-print-failed }
    If printing shipping labels fails, check the following:

    1. Check whether the browser is blocking pop-ups.
    2. Standard Plan merchants: make sure you've topped up CYBER Coins.
    3. If you still can't download or print, try another browser or contact customer service.

    !!! tip "The latest version of Chrome or Edge usually reduces printing issues."

## References { #reference-cvs-c2c }

- [7-Eleven tracking :lucide-external-link:](https://eservice.7-11.com.tw/e-tracking/search.aspx)
- [FamilyMart tracking :lucide-external-link:](https://fmec.famiport.com.tw/FP_Entrance/QueryBox)
- [Hi-Life tracking :lucide-external-link:](https://www.hilife.com.tw/serviceInfo_search.aspx)
- [7-Eleven excluded store list :lucide-external-link:](https://www.7-11.com.tw/form/store.pdf)

