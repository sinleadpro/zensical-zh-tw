---
title: "Shopper Purchase Flow"
description: "Guides shoppers to search for an address, choose a store, pick products, check out a Quick Delivery order, and verify receipt."
created: 2026-02-06 00:00
last_modified: 2026-07-06 17:00
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
  - 訂單
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options:
  - optional
cyb_extensions:
  - NOW!
intents:
  - 前台下單
  - 地址驗證
  - 收貨驗證
features:
  - CYBERBIZ NOW
  - 快速到貨
prerequisites:
  - 商家已完成 CYBERBIZ NOW 後台設定
  - 商家已開啟快速到貨專區
related: []
tags:
  - "Shopper Guide"
  - "Ordering Flow"
  - "PIN Code"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 快速到貨專區
  - 結帳頁面
paths:
  - 前台頁面
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=12978
  - https://www.cyberbiz.io/support/?p=13166
permalink: "https://help.cyberbiz.io/ec/orders/consumer-purchase-process/"
comments: false
search:
  exclude: false
icon: lucide/shopping-cart
hide: []
---
# Shopper Purchase Flow
This article explains how shoppers order in the **Quick Delivery section** of the storefront, how shipping fees are calculated, and how PIN verification works at delivery.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }


!!! tip "Use Cases"
	- **Customer education**: Use this article to create a shopper guide.
	- **Store inquiries**: Answer shoppers who ask how to use Quick Delivery or why they can't check out.


## Before You Start

- **Payment method limits**: Quick Delivery **doesn't support cash on delivery**. Shoppers must pay online first (status **Paid**) before you can accept and ship the order.
- **Address locked**: The recipient address at checkout defaults to the address entered when searching, and **can't be changed after checkout starts**.
- **Shipping fee**: Total shipping fee = platform shipping fee (Pandago/Uber Direct) + your shipping surcharge. If the order amount meets the free shipping threshold, the shopper doesn't pay shipping.
- **Service area limit**: Because of how Quick Delivery works, the maximum delivery distance is **5 km**.
---

## Ordering Steps

### Step 1: Enter the Delivery Address

1. On the storefront, click **CYBERBIZ NOW Quick Delivery**.

    === "Drag-and-Drop Theme"
        ![](../../assets/images/EC-前台-首頁-拖拉版型快速到貨入口01.en.png){ .screenshot }

    === "Default Theme"
        ![](../../assets/images/EC-前台-首頁-預設版型快速到貨入口01.en.png){ .screenshot }

2. Enter the full delivery address in the address search box.
    - Or click :lucide-send: on the right of the search box to use the current location.
3. The system shows all stores that can deliver, by distance.
    - If a store shows **Currently not accepting service**, it's currently outside its order-taking hours.
4. **Save frequent delivery addresses (optional)**: Click **Select Frequent Delivery Address** to add and save addresses (up to 5).
  ![](../../../assets/images/EC-前台-快速到貨-建立常用外送地址01.en.png){ .screenshot }

### Step 2: Shop the Store's Products

1. Click a store to browse its product list below.
2. Choose products and add them to the cart.

    > Note: Quick Delivery products open in a pop-up and don't have their own product pages.

3. **Checkout with multiple stores**:
    - If products from different stores are added, a **multiple carts** selection page appears before checkout.
    - Shoppers can check out only one store's cart at a time.

![](../../assets/images/EC-前台-首頁-快速到貨頁面01.en.png){ .screenshot }

### Step 3: Check Out and Add Notes

1. On the checkout page, confirm the recipient information and phone number.
2. In **Order Notes**, enter special instructions for the driver (such as "Leave it at the door" or "Call when you arrive").
3. Click **Checkout Now**. The shopper receives a **new order email**.

    > The order starts delivery only after the store accepts it. The store decides whether to accept the order. If the store rejects it, you'll be refunded.

---

## Receiving and Verification

### 1. Track Delivery Progress
After the order is placed and the store accepts it, once a driver is matched, the shopper receives a **store order acceptance email** from CYBERBIZ. The order can no longer be canceled at this point.

### 2. Track Delivery Progress

After a driver is matched, the delivery platform sends a **text message**. Tap the link in the message to see in real time:

- The driver's current location on the map.
- The estimated delivery time.

### 3. PIN Verification at Delivery (Uber Direct Only)
If the order is delivered by **Uber Direct**, the shopper must verify their identity at delivery for security:

- **How it works**: The shopper gives the courier the **last four digits of their phone number** as the PIN.
- **Purpose**: The order is completed only after the courier enters the correct PIN.

---

## FAQ

??? quote "Why does **Currently not accepting service** appear after I search an address?"
    It means the store is currently outside its **order-taking hours**. Note that **order-taking hours** are set by the merchant and may differ from the store's actual business hours.

??? quote "Can I change the delivery address at checkout?"
    No. Quick Delivery store coverage is based on the address entered when searching. To change the address, go back to the search page and enter it again, and the system matches the delivery stores again.

??? quote "Can shoppers cancel an order anytime after ordering?"
    Before the merchant clicks **Preparing**, the shopper can contact customer service to cancel. After the merchant clicks **Preparing** and sends the confirmation email, the shopper can't cancel it themselves, so delivery resources can be scheduled in real time.

??? quote "Can I change the order of delivery stores?"
    Yes. In **Payment and Logistics > Store Pickup Settings**, you can reorder stores manually, and the storefront shows them in that order.

