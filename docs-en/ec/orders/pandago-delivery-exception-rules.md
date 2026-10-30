---
title: "Pandago Delivery Exception Rules"
description: "Responsibility rules and steps for exceptions during Quick Delivery, such as wrong addresses, unreachable customers, and delivery delays."
created: 2026-02-06 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: troubleshooting
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
difficulty: intermediate
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
  - 處理配送異常
  - 判定運費責任
  - 申請配送補償
features:
  - CYBERBIZ NOW
  - 逆物流
  - 配送補償
prerequisites:
  - 訂單已進入「配送中」或「媒合成功」狀態
related: []
tags:
  - "Quick Delivery"
  - "Delivery Exceptions"
  - Pandago
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 訂單列表
  - 物流訊息
paths:
  - 訂單 > 門市訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=13253
permalink: "https://help.cyberbiz.io/ec/orders/pandago-delivery-exception-rules/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---
# Pandago Delivery Exception Rules

For exceptions during Quick Delivery (such as wrong addresses, unreachable customers, or delivery delays), this article explains who is responsible and what to do.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }




## Before You Start

- **Scope**: All exceptions in this article are cases where **the shopper didn't receive the order**.
- **Delivery address can't be changed**: Quick Delivery orders connect to the delivery system in real time and are limited by area, so **the address can't be changed after the order is placed**.
- **Cancellation**: If the delivery status shows **Order Canceled** and the return status is **No Return Needed**, the delivery platform canceled the order.
- **Shipping fee refunds**: The system charges the first-leg shipping fee in advance. If the platform is later found responsible and no fee is due, the delivery platform refunds CYBERBIZ in the next billing cycle, and CYBERBIZ then refunds you (shown on the Enterprise statement).
- **Reverse logistics cost**: If products return to the store because of the shopper (reverse logistics), you usually pay double shipping (original delivery fee + reverse logistics fee).
- **Compensation limit**: If products are damaged or lost because of the delivery platform, compensation is usually capped at **NT$5,000** per order (subject to each platform's final decision).
- **Monthly summary**: During monthly reconciliation, CYBERBIZ summarizes exception reasons and adjusts the charges on your statement.

!!! warning "Cancellation Reasons and Responsibility"
    If the detailed criteria for **cancellation reasons and responsibility** change, go by the latest announcement on the [Pandago official website](https://vendor.foodpanda.com.tw/pandago).



## Exception Responsibility and Shipping Fee Matrix

When the shopper doesn't receive the order, use the following table to determine who pays shipping and how to refund:

| Exception | Platform Charges Shipping | Products Returned to Store | Reverse Logistics Fee Paid By | Recommended Refund to Customer |
| :--- | :---: | :---: | :---: | :--- |
| **No driver available** | No | Not delivered | None | **Full refund** (including shipping) |
| **Driver called while store is closed** | Yes | Not delivered | None | **Full refund** (including shipping) |
| **Outside the area's delivery hours** | No | Not delivered | None | **Full refund** (including shipping) |
| **Weather or disaster prevents delivery after pickup** | No | Yes | No charge | **Full refund** (including shipping) |
| **Delivery delay (>30 min)** | No | Yes | Split between merchant and platform | **Full refund** (including shipping) |
| **Driver accident or unreachable** | No | No (compensated) | None | **Full refund** (including shipping) |
| **Out of delivery range found after pickup** | No | Yes (plus compensation) | None | **Full refund** (including shipping) |
| **Wrong recipient address** | Yes | Yes | **Merchant** | Refund product amount, **no shipping refund** |
| **Customer unreachable (>10 min)** | Yes | Yes | **Merchant** | Refund product amount, **no shipping refund** |
| **Delivery error** | Yes | Yes | **Merchant** |**Full refund** (including shipping) |
| **Spilled or damaged products** | No | No (compensated) | None | **Full refund** (including shipping) |
| **System technical issue** | No | Yes (plus compensation) | None | **Full refund** (including shipping) |


## Steps

### Task 1: Handle a "Wrong Address" or "Unreachable Recipient"

These are the most common exceptions. Handle them as follows:

1. **Confirm the exception**: Check **Logistics Messages** on the order details page to see whether it shows **Recipient Unreachable** or **Delivery Error**.
2. **Reach out**: Store staff should call the shopper to confirm the address or remind them to receive the order.
3. **Close out**: If the driver has brought the order back to the store, mark the order as **Returned**.


### Task 2: Handle "Damaged Products" or "Delivery Delays"

1. **Collect evidence**: If the shopper reports damaged products, ask for photos.
2. **Issue a full refund**: Because the delivery platform is responsible in these cases, give the shopper a **full order refund** (including shipping).
3. **Report to the platform**: Record the tracking number and the damage.

---

## FAQ

??? quote "Can the address of a Quick Delivery order really not be changed at all?"
    That's right. The admin doesn't support editing the address. For a minor change (such as from the 3rd floor to the 5th floor), if the store agrees, record it in "Admin Notes" and have the store call the driver directly. If the new address is in a different area, cancel the order and order again.

??? quote "What is the "reverse logistics fee"? Why do I pay twice?"
    Quick Delivery uses an on-demand delivery service. The driver taking products from the store to the customer counts as one trip. If the order can't be delivered and must go back to the original store, the driver spends the same time and effort, so the delivery platform charges for the return trip (the reverse logistics fee).

??? quote "How do I know if I'll get order compensation?"
    If the driver becomes unreachable, spills the order, or has an accident, the delivery platform sends a specific status code to the admin. You can see the details in "Activity Log" or "Logistics Messages" on the order details page. Compensation appears on your monthly statement rather than being paid out immediately.


