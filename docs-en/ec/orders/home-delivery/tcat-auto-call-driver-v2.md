---
title: "Automatically Call an EZCAT Driver for Pickup"
description: "When you batch download EZCAT shipping labels, the system automatically asks EZCAT to send a driver for pickup, saving you the time of contacting them manually."
created: 2026-05-13 16:18
last_modified: 2026-07-09 12:30
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
plan_options: []
cyb_extensions: []
intents:
  - 自動呼叫黑貓司機取件
  - 批次出貨同步預約取件
  - 下載黑貓託運單
features:
  - 自動呼叫司機
  - 新版訂單列表
  - 黑貓宅配
  - 黑貓快速到店
prerequisites:
  - 使用新版訂單列表
  - 向 CYBERBIZ 客服申請開通「自動呼叫黑貓司機」
  - 至黑貓寄取件設定頁完整填寫寄件人姓名、地址、聯絡電話
related:
  - ec/orders/home-delivery/tcat-home-delivery-v2/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
tags:
  - "EZCAT TA-Q-BIN"
  - "Call a Driver"
  - Pickup
  - "Shipping Labels"
  - Shipping
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 更多操作
  - 下載黑貓託運單
  - 是否自動呼叫黑貓司機取件
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=11013
  - https://www.cyberbiz.io/support/?p=47125
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/tcat-auto-call-driver-v2/"
comments: false
search:
  exclude: false
icon: lucide/phone
hide: []
---

## About Automatic EZCAT Driver Requests { #intro-tcat-auto-call-driver }

Previously, after printing EZCAT shipping labels in the admin, you had to call EZCAT customer service to schedule a pickup. With "Automatic Driver Pickup Request," you can choose to have the system notify EZCAT to send a driver to your pickup location **at the same time** you download EZCAT shipping labels, saving time on manual contact.

This feature appears only in the lower part of the "Download EZCAT Shipping Label" dialog and works with the [batch shipping process](tcat-home-delivery-v2.md#tcat-home-shipping-label-batch){ title="Batch Download EZCAT Home Delivery Shipping Labels" data-preview }.

## Prerequisites and Limitations { #prerequisites-tact-auto-call-driver }

### Requirements { #prerequisites-tcat-auto-call-driver-dependencies }


| Requirement | Description |
| :-- | :-- |
| Admin version | You must use the **new order list**; the legacy order list doesn't support this feature |
| Feature activation | "Automatic EZCAT Driver Request" must be activated; contact **CYBERBIZ customer service** to apply |
| Sender information | First fill in the sender's name, address, and phone number completely on the **[EZCAT pickup settings page](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#configure-ezcat-shipping-note-sender-setup){ title="Set Sender Information" data-preview }** (Payment and Logistics > EZCAT Shipping Labels > EZCAT Settings), or the system won't accept the request |

!!! info "If the "Automatically request an EZCAT driver pickup?" section doesn't appear in the lower part of the dialog, the feature isn't turned on for your store."

---

### Supported Logistics { #tcat-auto-call-driver-applicable-logistics }

The download dialog applies settings automatically based on the EZCAT delivery type used by the order. You can request a driver when downloading for any of the following:

| Delivery Type | Description |
| :-- | :-- |
| EZCAT home delivery (ambient / refrigerated / frozen) | Includes Cash on Delivery and Pickup Without Payment |
| EZCAT Quick Store Delivery (ambient / refrigerated / frozen) | Customers pick up at a convenience store |

---

### Order Requirements { #tcat-auto-call-driver-order-conditions }

Selected orders must meet the standard conditions for "downloading EZCAT shipping labels" for the system to create the labels and send the pickup request to EZCAT. Common requirements:

* Order status is **In Progress**
* Delivery status is **Unshipped** or **Preparing**
* Payment status is **Payment Received**, or the order is **Cash on Delivery**
* At least one item in the order uses EZCAT logistics

If the batch includes orders that don't qualify, shipping labels can't be created. Go back to the order list and check each order first.

---

## Steps { #operate-tcat-auto-call-driver }

1. **Open the order list**: Sign in to the CYBERBIZ admin and go to "**Orders > All Orders**" (new order list).
2. **Select orders**: In the order list, select the EZCAT orders to ship together, and make sure they all meet the order requirements above.
3. **Open the download dialog**: Click **Actions...** in the upper-right corner of the list and select **Download EZCAT Shipping Labels and Change to Shipped** from the drop-down menu.
4. **Check the label settings**: In the **Download EZCAT Shipping Label** dialog, check the default temperature zone (ambient / refrigerated / frozen), whether items are fragile, the sender address, and other defaults.
5. **Set up the automatic driver request**: Scroll to the **Automatically request an EZCAT driver pickup?** section and select **Yes**[^1]. Three fields then appear:
    * **Call before pickup?**: If you select "Yes," the driver calls the phone number entered on the "[EZCAT pickup settings page](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#configure-ezcat-shipping-note-sender-setup){ title="Set Sender Information" }" to confirm before arriving.
    * **Does the EZCAT driver need to bring a cart?**: If you have many packages, you can ask the driver to bring a cart.
    * **Notes**: Enter special pickup instructions (such as building access or floor), up to **100 characters**.

    ![Automatic EZCAT driver request](../../../assets/images/ec-payments-and-logistics-ezcat-auto-call-driver.en.png){ title="EZCAT Automatic Driver Request Settings" }

6. **Accept the terms and submit**: Select the logistics agreement checkbox at the bottom of the page and click **Yes**. The system prints the shipping label PDF, changes the delivery status of the batch to "Shipped," and sends a driver pickup request to EZCAT ([how to avoid duplicate requests](#tcat-auto-call-driver-multiple-calls)).

!!! tip "Your Last Settings Are Saved"
    The dialog remembers your last driver request settings (whether to request, call ahead, or bring a cart) and applies them next time, saving repeated steps.

[^1]: After **16:30 each day**, the "Yes" option becomes unavailable. Complete the settings before the deadline. See [Request Deadline](#tcat-auto-call-driver-deadtime).

---

## Pickup Times and Important Notes { #tcat-auto-call-driver-pickup-timing }

### Request Deadline { #tcat-auto-call-driver-deadtime }

* The system stops accepting automatic driver requests for the day at **16:30 every day**.
* If you open the dialog **after 16:30**, the "Yes" option for "Automatically request an EZCAT driver pickup?" **becomes unavailable**. For same-day or next-day pickup, contact EZCAT customer service directly.

!!! warning "The system doesn't move requests made after the deadline to the next day. Complete the settings before 16:30 to avoid missed pickups."

---

### Avoid Duplicate Requests { #tcat-auto-call-driver-multiple-calls }

* If you print EZCAT shipping labels in several batches on the same day, **select automatic driver request only for the last batch**.
* Requesting too early may mean packages aren't packed when the driver arrives, or may cause duplicate dispatches that create problems for the carrier.

---

### Make Sure Sender Information Is Filled In

* The system sends the request using the sender name, address, and phone number on the **EZCAT pickup settings page**.
* If any of these fields is empty, the request is rejected. Fill in the information first.

## Next Steps { #after-action }

<div class="grid cards" markdown>

- :lucide-search:{ .lg }  
  [__Track Shipping Status__](tcat-home-delivery-v2.md#tcat-home-verify-status){ title="Check Status Changes" }  
  Go back to the order list to check that the batch is marked "Shipped" and that the tracking numbers were added to the orders.

- :lucide-printer:{ .lg }  
  __Print Shipping Label Stickers__  
  Print on EZCAT blank three-part shipping label stickers. If you don't have any, call EZCAT to get them.

- :lucide-package:{ .lg }  
  __Hand Over Packages__  
  Have the labeled packages ready at the pickup location at the agreed time and wait for the driver.

</div>

---

## FAQ { #faq-tcat-auto-call-driver }

??? quote "Can't find the "Automatically request an EZCAT driver pickup?" section in the dialog?"
    [](){ #faq-tcat-auto-call-driver-cannot-find-option }

    This feature requires activation. Check that:

    1. You're using the **new order list**.
    2. Your store has applied to CYBERBIZ customer service to activate "**Automatic EZCAT Driver Request**."

??? quote "I selected "Yes" and submitted, but the driver didn't come?"
    [](){ #faq-tcat-auto-call-driver-driver-not-arrive }

    Check the following in order:

     1. Whether you submitted **before the 16:30 [deadline](#tcat-auto-call-driver-deadtime)**.
     2. Whether the name, address, and phone number on the [EZCAT pickup settings page](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#configure-ezcat-shipping-note-sender-setup){ title="Set Sender Information" } are complete.
    3. If the problem continues, contact EZCAT customer service at **02-412-8888** to arrange pickup directly.

??? quote "Can I request a driver pickup at a specific time?"
    [](){ #faq-tcat-auto-call-driver-schedule-pickup-time }

    You can't choose a pickup time. EZCAT schedules pickup times based on its daily schedule, and you can't set them in the admin.

??? quote "What if I print shipping labels several times on the same day?"
    [](){ #faq-tcat-auto-call-driver-multiple-batches }

    Set **Automatically request an EZCAT driver pickup? = Yes** only for the **last print**, and select "No" for earlier prints. This avoids early arrivals or duplicate dispatches.

??? quote "Is there an extra charge for "Automatic Driver Request"?"
    [](){ #faq-tcat-auto-call-driver-extra-fee }

    This feature has no extra system fee, but actual logistics costs (including EZCAT peak season surcharges and cold-chain fee differences) still follow EZCAT's rules.

