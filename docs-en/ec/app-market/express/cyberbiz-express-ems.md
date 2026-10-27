---
title: "CYBERBIZ EXPRESS Japan Post (EMS)"
description: "Connect Japan Post EMS to create consignment notes efficiently and handle international customs documents."
created: 2026-07-23 18:30
last_modified: 2026-07-23 18:30
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - APP MARKET
  - 訂單
sites:
  - JP
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - global_advanced
plan_options: []
cyb_extensions:
  - EXPRESS
intents: 
  - 設定 EMS 出貨
  - 批次列印 EMS 託運單
  - 串接日本郵局帳號
features: 
  - EMS 國際快捷
  - 自動化印單工具
  - Yubin Biz Card 整合
prerequisites: 
  - 需向開店顧問團隊申請開通服務
  - 需安裝 CYBERBIZ EXPRESS APP
  - 需具備商品英文名稱
related:
  - ec/app-market/express/product-info-setting/
  - ec/app-market/express/cyberbiz-express-japan-to-taiwan-delivery/
tags: 
  - EMS
  - "Japan Post"
  - "Cross-Border Logistics"
  - EXPRESS
acoiv: operation
apis: []
devices: []
ui_components: 
  - 建立託運單
  - 物流管理
paths: 
  - APP MARKET > 我的擴充服務 > CYBERBIZ EXPRESS
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/express/cyberbiz-express-ems/"
comments: false
search:
  exclude: false
icon: lucide/send
hide: []
---
# CYBERBIZ EXPRESS Japan Post (EMS)
Connect to Japan Post EMS to create consignment notes efficiently and handle international customs documents. You can also use your own Japan Post contract account to get discounted shipping rates.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (Japan to Taiwan)<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ EXPRESS
{ .doc-badge }


## Express Mail Service (EMS) { #intro-express-ems }

Express Mail Service (EMS) is a logistics option directly integrated between CYBERBIZ and Japan Post.

When you choose EMS as your logistics channel, you get these key features:

- **Lower Shipping Costs**: Use the discounted rates in your own contract with **Japan Post** to reduce cross-border logistics costs.
- **Label Printing in the Admin**: Generate consignment notes in the admin in one click and manage orders from placement to shipping in one place.
- **Easier Customs Clearance**: Customers **do not need EZWAY real-name verification**, making delivery more convenient and improving conversion.

### Before You Start { #intro-express-ems-requirements }

- **Product Information Settings**: Products sold cross-border **must include customs information** (such as JANCODE, ingredients, and country of origin). For field details, see [Product Information Settings for Japan-to-Taiwan Cross-Border Sales](product-info-setting.md).
- **Label Printing Service Fee**: The system deducts CYBER Coins in advance when you create a consignment note. On the last day of each month, billing is adjusted based on the number of parcels shipped that month.
- **Fee Settlement Limits**: If a consignment note is not actually used, for example because the order was canceled or the note expired, the label printing service fee already charged is not refunded.
- **Pickup**: Contact Japan Post yourself to arrange pickup. You can book in advance through [Japan Post Pickup Booking](https://mgr.post.japanpost.jp/C20P02Action.do) to ship on time.
- **Prohibited Items**: Make sure your products meet Japan Post's shipping restrictions. If a parcel is returned because of a violation, you are responsible for any losses. For details, see [Japan Post Prohibited Items](https://www.post.japanpost.jp/int/use/restriction/index_cn.html#airmail).


### Compare EXPRESS Home Delivery and Express Mail Service { #intro-express-ems-express-comparison }

| **Logistics Option** | **CYBERBIZ EXPRESS Home Delivery** | **Express Mail Service** |
| ----------- | ------------------------- | ----------------------- |
| **Carrier** | CYBERBIZ official logistics service | Japan Post |
| **Shipping Fee** | Deducted in advance by the platform (CYBER Coins) | Paid on pickup / monthly billing |
| **Taxes/Customs** | Follow the [EXPRESS home delivery shipping process](cyberbiz-express-japan-to-taiwan-delivery/#operate-express-japan) | Handled by you |
| **Logistics Disputes** | Handled by a single CYBERBIZ contact | Contact Japan Post |
| **Best For** | Merchants who want simpler cross-border customs procedures<br>Merchants who want to manage delivery through a single contact | Merchants with a discounted Japan Post contract account<br>Merchants used to shipping with EMS |



## Apply for Activation { #operate-express-ems }

1.  Apply for activation through your CYBERBIZ store consultant team. After activation, you can start setting it up in the admin.


2.  Log in to your online store admin, go to **APP MARKET > My Apps > CYBERBIZ EXPRESS**, and click **基本設定 > Express Mail Service**.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-EMS-開始設定01.en.png){ .screenshot }

3. Agree to the CYBERBIZ EXPRESS Cross-Border Shipping Service Agreement.

3.  Complete the basic settings.

    *   Select the account type:

        === "Regular Account (Pay Immediately)"

            - **Best For**: Merchants without a Japan Post contract
            - **Shipping Fees**: Paid when Japan Post picks up the parcel

        === "Japan Post Contract Account (Yubin Biz Card)"

            - **Best For**: Merchants with a Japan Post contract
            - **Shipping Fees**: Billed monthly at discounted rates
            - **Memo**: After selecting this option, fill in the deferred-payment customer fields. To apply, see [JP POST](https://www.post.japanpost.jp/send/fee/how_to_pay/deferred_pay/index.html)


    *   Enter the sender's identity information.

    *   Enter your shipping address in Japan.
        *   Without a shipping address in Japan, you cannot ship orders, so be sure to fill it in.
        *   **We recommend entering it in Chinese** to make Taiwan customs review easier. (English also works, but Chinese is preferred.)

    *   Choose your parcel mailing preferences.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-EMS-開始設定02.en.png){ .screenshot }




## Ship Orders { #operate-shipping }

1.  Go to **Orders > All Orders**, select the orders, and choose "Create Consignment Note".

    *   Make sure the orders meet these requirements:
        *   The payment status is "Payment Received"
        *   The delivery status is "Not Shipped" / "Preparing Shipment" / "Partially Shipped"
        *   The return status is "No Return Needed"

    *   After you create the consignment note, the order's delivery status changes to "Shipped" automatically.

    *   You can select multiple orders to create consignment notes in bulk.

    *   When selecting in bulk, make sure every order qualifies for Japan-to-Taiwan home delivery. If any order does not match the delivery method or order status, the "Create Consignment Note" option does not appear.

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單01.en.png){ .screenshot }


2.  **Choose the Delivery Method**: Select the delivery channel in the pop-up window.

    *   **Preview and Print Documents**: Based on what you selected (see the list below), the system opens a web preview. Check it and then print.
        *   Consignment notes
        *   Order details
        *   Picking lists
        *   Shipping details
    *   **Bulk Download**: You can download all of the documents above at the same time.
    *   **Automatic Sorting**: When you create notes in bulk, the system generates one PDF file with all order details, sorted by order number in ascending order.
    *   **Real-Time Data Validation**: The system checks the fields of products in the order. If the weight or required cross-border product fields are missing, fill them in before shipping.

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單06.en.png){ .small-image }



## Reprint Consignment Notes { #intro-reprint }


Go to **Orders > All Orders**, select the orders, and choose "Reprint Consignment Note".

Make sure the orders meet these requirements:

*   The payment status is "Payment Received"
*   The delivery status is "Shipped"
*   The return status is "No Return Needed"

![](../../../assets/images/EC-後台-訂單-所有訂單-補印EXPRESS託運單01.en.png){ .screenshot }


