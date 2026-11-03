---
title: "Set up POS Order Auto-Close"
description: "Automatically close completed in-store POS orders based on your settings so the system can issue bonus points, activate the coupon given as gifts, and recognize profit-sharing bonuses."
created: 2026-06-25 10:00
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
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
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定 POS 訂單自動結案
  - 自動化訂單結案流程
  - 省下手動結案時間
features:
  - POS 訂單自動結案
  - 結帳後立即結案
  - 指定天數結案
prerequisites:
  - 已開通 POS 功能
  - 網站擁有者權限
related:
  - ec/payments-and-logistics/payments/order-settings/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/orders/references/payment-statuses/
tags:
  - POS_Orders
  - Auto_Close
  - Bonus_Issuance
  - coupon
  - Profit_Sharing
  - Closing_Settings
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 訂單相關設定
  - POS 訂單自動結案設定
paths:
  - 金物流 > 結帳頁 & 物流設定 > 訂單相關設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=23628
permalink: "https://help.cyberbiz.io/pos/orders/pos-order-auto-close/"
comments: false
search:
  exclude: false
icon: lucide/file-clock
hide: []
---

[:lucide-layers:{ title="Applies To" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

![POS Order Auto-Close Settings](../../assets/images/pos-auto-close-hero.en.png){ title="POS Order Auto-Close Settings" .hero-page }

## POS Order Auto-Close Overview{ #Intro-Pos-Auto-Close }

"POS Order Auto-Close" is an automation setting for **POS in-store orders**. After in-store checkout, an order stays in the "Not Closed" status. Only after an order enters **"Closed"** does the system perform the following actions:

- **Issue Shopping Bonus**: The bonus points that the customer earns on this order are officially credited to their account.
- **Activate Gifted coupon**: The coupon given for meeting a spend threshold become effective and usable only after the order is closed.
- **Recognize Profit-Sharing Bonuses**: Profit-sharing performance for store staff or referrers is calculated and recognized at this point.
- **Clean Up the Not Closed List**: After closing, the order is removed from the "Not Closed" list in the back office, keeping the order management interface tidy.

After you turn on auto-close, you no longer need to close orders one by one each day. The system completes the process above automatically at the scheduled time.

## Prerequisites and Limitations { #prerequisites-pos-auto-close }

- [x] **POS Feature Enabled**: This setting appears only in stores that have POS enabled. If POS is not enabled, this section does not appear.
- [x] **Site Owner Permission**: Only the **site owner** can change this setting. Other accounts cannot modify it.

## Step-by-Step Guide { #operate-pos-auto-close }

1. **Go to the settings page: ** Payment and Logistics > Checkout Page & Logistics Settings > Scroll to ** "Order Settings"** section, find **"POS Order Auto-Close Settings"**, and click to expand it.
2. **Turn on the feature:** Select **"Turn On POS Order Auto-Close"**. The closing method options appear below.

    ![Enable auto-close screen](../../assets/images/pos-auto-close-enable.en.png){ title="Turn On Auto-Close Screen" }

3. **Choose a closing method:** Select **one** of the following two methods[^mode].

    === "Close Immediately After Checkout"

        Select **"Close Immediately After Checkout"**. As soon as a customer finishes checkout in store, the order is closed automatically, so the bonus and coupon can be issued as quickly as possible.

        ![Immediate close settings screen](../../assets/images/pos-auto-close-immediate.en.png){ title="Immediate Close Settings Screen" }

        !!! tip "Recommended for Stores"
            Immediate closing lets customers receive their bonus or coupon right after checkout, which makes repeat purchases easier. It suits most physical stores.

    === "Close a Set Number of Days After Checkout"

        Do not select immediate closing. In the **"Auto-Close Orders ___ Days After Checkout"** field, enter the number of days (for example, `7`). The system closes the order automatically during the daily batch run once the specified number of days have passed since payment.

        ![Set-days auto-close settings screen](../../assets/images/pos-auto-close-delay.en.png){ title="Days-Based Close Settings Screen" }

4. **Save the settings:** When finished, click **Save**. The settings take effect immediately.

[^mode]: The two methods are mutually exclusive. After you select "Close Immediately After Checkout," the number-of-days field no longer appears.

## System Rules and Notes{ #Specs-Pos-Auto-Close }

### Differences Between the Two Closing Methods { #specs-pos-auto-close-modes }

| Closing Method | Closing Timing | Processes Existing Not Closed Orders from Before Setup |
| :-- | :-- | :-- |
| Close Immediately After Checkout | Closes the order as soon as payment is completed | No. Applies only to orders created after the setting is turned on |
| Close a Set Number of Days After Checkout | Closes during the daily batch run after N days have passed since payment | Yes. Also processes existing not closed orders from before the setting was enabled |

!!! note "Note"
    If you want the system to process not closed orders from before you turned on the setting, select the **Close a Set Number of Days After Checkout** method. Close Immediately only applies to orders created afterward.

---

### Closing Prerequisites and Timing { #specs-pos-auto-close-timing }

- **Orders must be paid**: Only orders that are **paid** are closed automatically. Unpaid orders are not closed automatically.
- **Canceled orders are not processed**: Canceled orders are not closed automatically.
- **Fixed daily batch time**: With the set-number-of-days method, the system runs one batch scan each morning at **06:15** to close orders. An order therefore does not close the moment its period ends. It closes at the next batch run.
- **Day count example**: For a setting of 7 days, an order checked out on **Jan 1** is closed automatically on **Jan 8**.

---

## Next Steps { #next-steps-pos-auto-close }

<div class="grid cards" markdown>

- :lucide-check-check:{ .lg }  
  [__Order Settings Overview__](../../ec/payments-and-logistics/payments/order-settings.md){ title="Order Settings" }  
  Review other order rules on the same page, such as auto-close, auto-cancel, and unpaid order reminders.

- :lucide-list-ordered:{ .lg }  
  [__Partial Order Shipment__](../../ec/orders/home-delivery/partial-shipment-v2.md){ title="Set Up Partial Order Shipment" }  
  Learn about order shipping and status flows so you can manage orders before they are closed.

</div>

## Frequently Asked Questions { #faq-pos-auto-close }

??? quote "Why were my earlier not closed orders not closed after I turned on auto-close?"
    [](){ #faq-pos-auto-close-existing-orders }
    It depends on the closing method you choose:

    - **Close Immediately After Checkout**: Applies only to orders created **after the setting is turned on**. It does not process older orders from before the setting.
    - **Close a Set Number of Days After Checkout**: Also processes not closed orders from before the setting. These orders close only after the specified number of days have passed since payment and the daily batch run has occurred.

    To close older orders from before the setting, use the set-number-of-days method or close them manually.

??? quote "Is it normal that orders are not closed right away after setup?"
    [](){ #faq-pos-auto-close-not-closed }
    If you use the **set-number-of-days** method, the system processes orders in a **fixed daily batch each morning**. Orders are not closed the instant their period ends, so a delay is expected and normal. Also confirm that the order has been **fully paid**. Unpaid orders are not closed automatically.

??? quote "Can't find the "POS Order Auto-Close Settings" section?"
    [](){ #faq-pos-auto-close-not-found }
    Check the following two items:

    - Your store has **POS enabled**. This setting appears only for stores with POS.
    - You are signed in as the **site owner**. Only the site owner can change this setting.

??? quote "How are bonus points and profit-sharing handled if an order is returned after it is closed?"
    [](){ #faq-pos-auto-close-return }
    Once an order is closed, its bonus points and profit-sharing are officially issued and recognized. If a return occurs later, how the related bonus points and profit-sharing are recovered depends on your store's **Return and Bonus Settings**. Check the actual status on the order or member page, and make adjustments if needed.

---

## References { #reference-pos-auto-close }

- [Payment Status Guide](../../ec/orders/references/payment-statuses.md)
