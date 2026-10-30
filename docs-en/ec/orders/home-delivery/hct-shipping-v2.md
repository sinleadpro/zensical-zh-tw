---
title: "Ship with HCT Logistics"
description: "Batch select orders in the order list, download HCT shipping labels, and update the shipment status to Shipped."
created: 2026-05-22 17:21
last_modified: 2026-08-20 16:00
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
  - 訂單
  - 金物流
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
  - 批次下載新竹物流託運單
  - 查詢新竹物流配送規範與限制
  - 了解新竹物流計費方式
features:
  - 新竹物流託運單
  - 補印託運單
  - 加印託運單
prerequisites:
  - ec/payments-and-logistics/setup-hct-waybill-v2/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/orders/basics/search-filter-orders/
tags:
  - "HCT Logistics"
  - "Shipping Labels"
  - "Batch Shipping"
  - "CYBER Coins"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
  - 金物流 > 新竹物流託運單
  - 金物流 > 新竹物流託運單 > 加印託運單
  - 金物流 > 新竹物流託運單 > 單號使用紀錄
  - 管理中心 > 儲值中心
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10646
  - https://www.cyberbiz.io/support/?p=46278
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/hct-shipping-v2/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

![Download HCT Logistics shipping labels](../../../assets/images/EC-訂單-所有訂單-下載新竹物流託運單-hero.en.png){ title="Download HCT Logistics Shipping Labels" .hero-page }

## About HCT Logistics Shipping { #intro-hct-shipping }

When your orders use **HCT Logistics** delivery, you can select orders in bulk in the order list, have the system generate tracking numbers, download shipping labels and related documents, and change the orders' delivery status to "Shipped" all at once. This article covers the batch shipping process in the order list, what the 5 downloaded documents are for, and what happens after the driver picks up.

## Prerequisites and Limitations { #prerequisites-hct-shipping }

### Activation Requirements { #prerequisites-hct-shipping-enable }

Before the "Download HCT Logistics Shipping Labels" option appears in the order list, complete the following:

- [x] **Set up HCT Logistics shipping labels**: Go to "Payment and Logistics" > "[HCT Logistics Shipping Labels](../../payments-and-logistics/setup-hct-waybill-v2.md){ title="Set Up HCT Logistics Shipping Labels" }" and fill in the sender information[^1].
- [x] **HCT Logistics sender address**: Set the sender address in "Payment and Logistics" > "[HCT Logistics Shipping Labels](../../payments-and-logistics/setup-hct-waybill-v2.md#operate-hct-setup-sender){ title="Set Up HCT Logistics Shipping Labels" }." Without it, you'll see an "Incomplete sender information" message when shipping.

!!! plan "Charges Depend on Your Plan"
    HCT Logistics shipping labels are charged in one of two ways. Check your plan before you start:

    - **Standard Plan**: **CYBER Coins are deducted immediately** when you print shipping labels, and printing is blocked if your balance is insufficient. Top up first in "Management Center" > "Top-Up Center."
    - **PLUS / Enterprise**: No top-up needed; fees are **included on each statement**.

[^1]: If this isn't set up, the download action doesn't appear in the order list.
[^2]: Changes also update the address on that logistics page. Addresses for different logistics services and the company logistics address don't affect each other.

---

### Order Requirements { #prerequisites-hct-shipping-order }

For batch downloads, the system checks whether the selected orders meet the following requirements. If any isn't met, this option doesn't appear in "More Actions":

| Requirement | Allowed status |
| :-- | :-- |
| Order status | Open, and all selected orders must have the same status |
| Delivery method | **All must be HCT Logistics** (doesn't appear when mixed with other logistics methods) |
| Payment method | Not EZCAT Cash on Delivery / Pelican Express Cash on Delivery |

---

### Billing Rules { #pricing-hct-shipping }

Charges depend on your plan:

- **Standard Plan**: Charged immediately when you confirm the download[^pricing-deposit]. If you don't have enough CYBER Coins, printing is blocked; top up in the "Top-Up Center" first.
- **PLUS / Enterprise**: Printing isn't blocked; fees are settled on each statement.

[^pricing-deposit]: If a package isn't actually shipped within 14 days after the shipping label is created, the system automatically refunds the CYBER Coins (see [Shipping Label Validity](#specs-hct-shipping-expiry)).

## Steps { #operate-hct-shipping }

### 1. Select Orders { #operate-hct-shipping-select }

Go to "Orders" > "All Orders" in the admin and select the [orders to ship together](#specs-hct-shipping-uniform) in the list.

!!! tip "Filter Before Selecting"
    In the new order list, filter by "Delivery Method = HCT Logistics" first, then select the whole page to speed up batch shipping. Learn [how to filter orders](../basics/search-filter-orders.md#orders-filter){ title="How to Search and Filter Orders" }

---

### 2. Choose the Download Action { #operate-hct-shipping-action }

Click the **Actions...** drop-down above the list and select **"Download HCT Logistics Shipping Labels and Change Delivery Status to 'Shipped'"**.

![Download HCT Logistics shipping labels](../../../assets/images/EC-訂單-所有訂單-下載新竹物流託運單.en.png){ title="Download HCT Logistics Shipping Labels" }

!!! info "Tip"
    To reprint shipping labels you've already downloaded (without being charged again), select **"Reprint Shipping Label."** The process is the same, but it **doesn't** deduct CYBER Coins again or generate new tracking numbers.

---

### 3. Set the Temperature Zone, Paper, and Sender Address { #operate-hct-shipping-modal }

After you click the action, the "Download HCT Logistics Shipping Labels" window opens. Set the following in order:

- **Temperature zone**: Choose one based on the package's actual temperature zone (only one temperature zone per batch)
    - **Room Temperature**
    - **Refrigerated**
    - **Frozen**

    ??? warning "Orders with Multiple Temperature Zones"
        If the selected orders cover different temperature zones, the window shows: "You have orders with different temperature zones. Check whether shipping them affects product quality." The system still creates shipping labels with the temperature zone you selected, so assess whether the items can ship together.

- **Paper size**:
    - **Standard Print (A4)**: For A4 six-label shipping label stickers
    - **Thermal Print (10cm x 10cm)**: For 10 cm × 10 cm thermal paper

    ??? info "Get Shipping Label Stickers"
        You can get them during the site inspection or at pickup, or by calling the HCT Logistics branch that handles your pickups. When you call, provide the following:

        - You're a CYBERBIZ merchant requesting shipping labels.
        - You need 10 cm × 10 cm thermal paper or A4 six-label shipping label stickers (choose one).
        - Your shipping location, phone number, and contact person.
        - Sender customer code: 0577349.

- **Sender Address**: Defaults to the sender address last used for this logistics service (the first time, it uses the address in [HCT Logistics settings](../../payments-and-logistics/setup-hct-waybill-v2.md#operate-hct-setup-sender){ title="Set Up HCT Logistics Shipping Labels" }). To change it, click **Change** in the window[^2].

![Download HCT Logistics shipping labels - pop-up](../../../assets/images/ec-orders-hct-waybill-download-popup.en.png){ title="Download HCT Logistics Shipping Labels: Pop-Up" }

---

### 4. Confirm the Download { #operate-hct-shipping-download }

After you click **"Confirm,"** the system:

- Generates HCT Logistics tracking numbers for the temperature zone you chose
- Deducts CYBER Coins immediately for the **Standard Plan**, or adds fees to the statement for **PLUS / Enterprise**
- Automatically downloads an archive with **5 PDF** documents
- Changes the order delivery status to **"Shipped (Awaiting Carrier Pickup)"**

The 5 downloaded documents are used as follows:

| File | Purpose |
| :-- | :-- |
| Shipping label - sender information | Stick on the box (be sure to print on HCT Logistics label paper). We recommend a laser printer to avoid shipping information errors. |
| HCT Logistics shipment manifest | **Important document**. Keep it safe and give it to the driver to check at pickup |
| Shipping details | For checking picked items when shipping |
| Order details | Sent to the customer with the package |
| Pick list | For warehouse staff to pick items |

!!! warning "No Changes After the Delivery Status Changes"
    Once an order's delivery status changes to "Shipped," **recipient information can't be changed**. Check the order information before downloading.

---

### 5. Driver Pickup { #operate-hct-shipping-pickup }

After you download the shipping labels, the system sends the order information to HCT Logistics. Pickup works as follows:

1. **Driver dispatch**:

    - Labels downloaded before 15:00: HCT Logistics creates the dispatch the same day and notifies the driver
    - Labels downloaded after 15:00: The dispatch is created the next day and the driver is notified
    - The driver picks up within 1–3 business days after being notified

2. **Driver pickup**: When the driver arrives, show the **HCT Logistics shipment manifest** (a PDF in the download) for the driver to check.
3. **Status update**: After the driver picks up, the order automatically changes to **"Shipped (In Transit)"**.

??? tip "If No One Picks Up for Several Days"
    Call your HCT Logistics branch, give sender customer code **0577349** and the information below, explain that you "already have printed shipping labels," and ask the branch to arrange a pickup.

## Important Rules and Limitations { #specs-hct-shipping }

### Size, Weight, and Unaccepted Items { #specs-hct-shipping-restrictions }

HCT Logistics size and weight limits vary by temperature zone. Packages over the limits can't be shipped:

| Temperature Zone | Max sum of three sides | Max single side | Max weight |
| :-- | :-- | :-- | :-- |
| Room temperature | 180cm | — | 20kg |
| Low temperature (refrigerated / frozen) | 120cm | 60cm | 20kg |

!!! info "Items Not Accepted for Low-Temperature Delivery"
    HCT Logistics **doesn't accept** the following items for low-temperature delivery:

    - Vaccines, blood / urine specimens, refrigerated medicines
    - Fresh cream cakes, breast milk, ice cream
    - Durian / salted fish not in sealed packaging
    - Products with a shelf life under 3 days

!!! warning "If a Package Is Returned"
    If HCT Logistics finds unaccepted items in a package, it may **return it to the sender** or refuse delivery, and CYBER Coins aren't refunded. Make sure your products comply before shipping.

---

### Shipping Label Validity (Expires After 14 Days) { #specs-hct-shipping-expiry }

If a package isn't actually shipped **within 14 days** after the shipping label is created, the tracking number expires:

- The system changes the shipping label status to **"Shipment Canceled."**
- For the **Standard Plan**, deducted CYBER Coins are fully refunded automatically (check "Tracking Number History" in "Payment and Logistics" > "HCT Logistics Shipping Labels").
- To ship after expiration, download a new tracking number from the order again; you're charged again.

--- 

### Delivery Methods Must Match { #specs-hct-shipping-uniform }

**All selected orders must use HCT Logistics as the delivery method**, or this option doesn't appear in "More Actions." If you've also selected orders with other logistics (such as EZCAT or Pelican Express), deselect them and select again.

---

### Use "Print Extra Shipping Labels" for Multi-Box Shipments { #specs-hct-shipping-extra-label }

If an order needs to **ship in multiple boxes** (for example, too many items for one box), first download the **original shipping label** from the order list, then use [Print Extra Shipping Labels](../../payments-and-logistics/setup-hct-waybill-v2.md#operate-hct-waybill-reprint){ title="Set Up HCT Logistics Shipping Labels" }: enter the same order number on the "HCT Logistics Shipping Labels" page to generate labels for the other packages.

!!! note "Labeling Recommendations"
    "Print Extra Shipping Labels" can print only **delivery-only** shipping labels, without payment collection. Put the **original shipping label** on the main package and the extra delivery-only labels on the other packages.


## Next Steps { #next-steps-hct-shipping }

<div class="grid cards" markdown>

- :lucide-printer:{ .lg }  
  [__HCT Logistics Shipping Label Management__](../../payments-and-logistics/setup-hct-waybill-v2.md){ title="Set Up HCT Logistics Shipping Labels" }  
  Sender information, extra shipping labels, and HCT reverse logistics settings.

- :lucide-package-open:{ .lg }  
  [__Partial Shipment for Orders__](partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }  
  How to ship one order in multiple shipments.

</div>

## FAQ { #faq-hct-shipping }

??? quote "Can't find the HCT Logistics download option in "More Actions"?"
    [](){ #faq-hct-shipping-action-missing }

    Check the following in order:

    - Whether **"HCT Logistics shipping label settings"** are complete (sender name, phone, and address all filled in). If not, the option doesn't appear in the order list.
    - Whether **all selected orders use HCT Logistics as the delivery method**. The option doesn't appear when mixed with other logistics.
    - Whether **the payment methods of selected orders include another carrier's Cash on Delivery** (EZCAT, Pelican Express, SF Express). If so, the option doesn't appear.
    - Whether all order statuses match and are "Open"

??? quote "Can I ship selected orders with different temperature zones at once?"
    [](){ #faq-hct-shipping-mixed-temperature }

    Yes. The system shows "You have orders with different temperature zones. Check whether shipping them affects product quality." and creates shipping labels with **the single temperature zone you selected**. When temperature zones are mixed, we recommend **downloading in batches** (room temperature orders first, then low-temperature orders) to protect product quality.

??? quote "What if I want to cancel a shipping label after downloading it?"
    [](){ #faq-hct-shipping-cancel }

    You **can't cancel** generated shipping labels yourself in the admin. To cancel, contact CYBERBIZ customer service.

    If you **don't actually ship**, the system automatically changes the tracking number to "Shipment Canceled" **14 days** after creation and refunds the CYBER Coins (Standard Plan only). No action is needed.

??? quote "How do I replace an expired shipping label?"
    [](){ #faq-hct-shipping-expired }

    After a shipping label expires, the system **refunds the CYBER Coins** to your Top-Up Center (Standard Plan only) and changes the tracking number status to "Shipment Canceled." To ship the order, go back to the order list and download the shipping label again. The system generates a new tracking number and charges you again.

??? quote "The download button doesn't respond or keeps loading?"
    [](){ #faq-hct-shipping-download-stuck }

    Check the following in order:

    - **Whether your CYBER Coin balance is sufficient** (Standard Plan only). If not, top up in the "Top-Up Center" first.
    - **Whether the sender address is complete**. Check that it's filled in under "Payment and Logistics" > "HCT Logistics Shipping Labels."
    - **Whether the browser is blocking the download pop-up**. Allow the site to download files and try again.

??? quote "What if one order needs to ship in multiple boxes?"
    [](){ #faq-hct-shipping-multi-box }

     Use **Print Extra Shipping Labels**: Go to "Payment and Logistics" > "HCT Logistics Shipping Labels" > "Print Extra Shipping Labels" and enter the same order number to generate a new tracking number and shipping label. Each [extra shipping label](../../payments-and-logistics/setup-hct-waybill-v2.md#operate-hct-waybill-reprint){ title="Set Up HCT Logistics Shipping Labels" }.

??? quote "How is reprinting shipping labels different from downloading them?"
    [](){ #faq-hct-shipping-reprint-vs-download }

    Downloading shipping labels generates new tracking numbers, deducts CYBER Coins based on your plan, and changes the delivery status to "Shipped." **Reprint Shipping Label** doesn't generate new tracking numbers or charge you again. The process is the same, and it's for reprinting when labels are damaged or lost.

??? quote "How do charges differ between the Standard Plan and PLUS / Enterprise?"
    [](){ #faq-hct-shipping-plan-pricing }

    - **Standard Plan**: **CYBER Coins are deducted immediately** when you download shipping labels, and printing is blocked if your balance is insufficient. If a package isn't actually shipped within 14 days, the system refunds them automatically.
    - **PLUS / Enterprise**: No top-up needed; fees are **included on each statement**, and printing isn't blocked.

??? quote "Can I change recipient information after the delivery status changes to "Shipped"?"
    [](){ #faq-hct-shipping-modify-recipient }

    No. Once an order's delivery status changes to "Shipped," **recipient information can't be changed**. Before downloading shipping labels, make sure the recipient's name, phone number, and address are correct.


