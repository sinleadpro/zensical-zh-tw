---
title: "Set Up Payment Methods for EZCAT Quick Store Delivery"
description: "Set up payment methods for EZCAT Quick Store Delivery, including steps for cash on delivery and pickup without payment."
created:
last_modified: 2026-07-01 10:30
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/tcat-quick-store/tcat-express-payment-settings/"
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定黑貓快速到店付款方式
  - 設定貨到付款
  - 設定取貨不付款
  - 了解黑貓快速到店運作模式
  - 查詢物流運費
  - 遵守包裹規格限制
  - 處理逾期未取退貨
  - 確保低溫包裹預冷
features:
  - 黑貓快速到店
  - 7-11 門市配送
  - 貨到付款
  - 取貨不付款
  - 運費設定
  - 代收手續費
prerequisites:
  - 開通 CYBERBIZ PAYMENTS (若需使用貨到付款功能)
related:
  - ec/orders/tcat-quick-store/tcat-quick-store-shipping/
  - ec/products/shipping/cvs-shipping-restrictions-exclusions/
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 超商物流
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2655
  - https://www.cyberbiz.io/support/?p=8846
search:
  exclude: false
icon: lucide/wallet
hide:
comments: false
tags:
  - EC
  - "EZCAT Quick Store Delivery"
  - 7-Eleven
  - "Cash on Delivery"
  - "Pickup Without Payment"
  - "Convenience Store Logistics"
  - "Payment and Logistics"
---

![EZCAT Quick Store Delivery payment](../../../assets/images/ec-金物流-超商物流-黑貓快速到店.en.png){ title="EZCAT Quick Store Delivery Payment" .hero-page }

## About EZCAT Quick Store Delivery Payment

You can offer two options, "Cash on Delivery" and "Pickup Without Payment." An EZCAT driver picks up packages at your specified location and delivers them to the **7-Eleven store** the shopper chose.

## Step 1: Go to the Settings

1. Sign in to the admin and go to **Payment and Logistics > Convenience Store Logistics**.
2. In the **EZCAT Quick Store Delivery** section, click the edit button :material-file-document-edit-outline: to open the edit page.

![Edit EZCAT Quick Store Delivery](../../../assets/images/ec-金物流-超商物流-黑貓快速到店-編輯.en.png){ title="Edit EZCAT Quick Store Delivery" }

## Step 2: Set Up Payment Methods

### Set Up "Cash on Delivery" <small>COD</small>

!!! plan "This feature is **available only to merchants with CYBERBIZ PAYMENTS**."

1. Switch to the **Cash on Delivery** tab.
2. **Turn it on:** Switch "Cash on Delivery" to **"ON"**.

3. **Shipping and handling fees:**

	- Set shipping fee ranges and free shipping thresholds for each temperature zone (Ambient, Refrigerated, Frozen).
	- **Note:** With cash on delivery, EZCAT charges an extra collection fee based on the amount collected. The shipping fee is the same as the regular delivery fee.

4. Click **Save** to apply the changes.

![EZCAT Quick Store Delivery - cash on delivery](../../../assets/images/ec-金物流-超商物流-黑貓快速到店-貨到付款.en.png){ title="EZCAT Quick Store Delivery - Cash on Delivery" }

---

### Set Up "Pickup Without Payment" <small>No Payment on Delivery</small>

1. Switch to the **Pickup Without Payment** tab.
2. **Turn it on:** Switch "Pickup Without Payment" to **"ON"**.
3. **Shipping fee:** Set the base shipping fee and free shipping amount for each temperature zone. To not offer free shipping, select "Off."
4. Click **Save** to apply the changes.
5. **On the storefront:** Shoppers can choose this delivery type after paying online (such as by credit card) on the checkout page.

![EZCAT Quick Store Delivery - pickup without payment](../../../assets/images/ec-金物流-超商物流-黑貓快速到店-取貨不付款.en.png){ title="EZCAT Quick Store Delivery - Pickup Without Payment" }

## What Customers See

- On your website's checkout page, customers **don't see** the words "EZCAT Quick Store Delivery."

- The system shows a **7-Eleven store map** provided by EZCAT. After the shopper selects a store, you ship through EZCAT Quick Store Delivery.

- If you turn on both ambient and frozen delivery, customers see the matching 7-Eleven delivery options based on the temperature zone of the products they buy.

<div class="grid" markdown>

![EZCAT Quick Store Delivery ambient](../../../assets/images/ec-金物流-超商物流-黑貓快速到店-常溫.en.png){ title="EZCAT Quick Store Delivery Ambient" }
/// caption
Ambient
///

![EZCAT Quick Store Delivery frozen](../../../assets/images/ec-金物流-超商物流-黑貓快速到店-冷凍.en.png){ title="EZCAT Quick Store Delivery Frozen" }
/// caption
Frozen
///

</div>

## Key Rules and Important Notes

- **Shipping rates:** See detailed rates at **Website Management > Reconciliation Center > Other Logistics Shipping Fees** in the admin.

- **Package limits:**

	- **Weight:** Can't exceed **10 kg**.
	- **Size:** The sum of the three sides can't exceed **105 cm** (no limit on any single side).

- **Delivery area:** Delivers only to Taiwan's main island (**On shore of Taiwan**).

- **Return fees:** If the shopper doesn't pick up the package in time and it's returned to you, EZCAT charges **shipping twice** (outbound shipping + return shipping). For cash on delivery, the collection fee is charged separately.

- **Pre-chilling:** Before shipping chilled packages, pre-chill them (6+ hours for refrigerated, 12+ hours for frozen) to keep delivery quality.








## Next Steps

<div class="grid cards" markdown>

- :lucide-zap:{ .lg }  
  [__Ship with EZCAT Quick Store Delivery__](tcat-quick-store-shipping.md){ title="Ship with EZCAT Quick Store Delivery" }  
  Ship orders with EZCAT Quick Store Delivery.

- :lucide-ban:{ .lg }  
  [__Logistics Restrictions and Exclusions__](../../products/shipping/cvs-shipping-restrictions-exclusions.md){ title="Set Up Convenience Store Delivery Restrictions and Logistics Exclusions" }  
  Set product delivery conditions to limit which delivery types appear and can be used at checkout.

</div>


## FAQ

??? quote "Can I turn on both EZCAT Quick Store Delivery and 7-Eleven pickup with payment?"
	Yes. But customers see two 7-Eleven options on the checkout page. To avoid confusion, we recommend turning on only one delivery type per convenience store.

??? quote "How do customers choose EZCAT Quick Store Delivery at checkout?"
	Customers **don't see** a delivery option named **EZCAT Quick Store Delivery** on the storefront. They see the **7-Eleven store map** provided by EZCAT. For customers, the process is the same as regular convenience store pickup. The only difference is that you deliver products to the chosen store through EZCAT.

??? quote "Can I turn on both ambient and frozen EZCAT Quick Store Delivery?"
	Yes. If the customer buys products in both ambient and frozen temperature zones, the checkout page shows a separate EZCAT Quick Store Delivery option for each (both shown as 7-Eleven delivery), and customers choose based on the temperature zone.

??? quote "Are the store maps the same for ambient and frozen EZCAT Quick Store Delivery?"
	**Not necessarily**. The store map customers see at checkout is provided directly by EZCAT. Based on **ambient or frozen** delivery needs, the system automatically filters and shows stores that support delivery in that temperature zone.
