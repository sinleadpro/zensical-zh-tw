---
title: "Convenience Store Pickup Name Rules"
description: "Learn the recipient name rules for convenience store pickup (such as 7-Eleven), including length, special characters, numbers, and spaces, to avoid shipment submission failures."
created: 2026-06-12 16:20
last_modified: 2026-06-12 16:20
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
  - customer
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents: 
  - 了解超商取貨姓名規則
  - 解決超商出貨姓名錯誤
  - 設定結帳頁姓名驗證
features: 
  - 超商取貨
  - 姓名驗證
prerequisites: []
related: []
tags: 
  - "Convenience Store Pickup"
  - "Name Rules"
  - "Validation Rules"
acoiv: operation
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 結帳頁面
paths: 
  - 金物流 > 結帳頁 & 物流設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/cvs-pickup-name-rules/"
search:
  exclude: false
icon: lucide/user-check
hide: []
---

# Convenience Store Pickup Name Rules
Learn the recipient name rules for convenience store pickup (such as 7-Eleven), including length, special characters, numbers, and spaces, to avoid shipment submission failures caused by invalid formats.
{ .subtitle }


!!! tip "Use Cases"
	- **Real-time checkout validation**: When customers enter the recipient name on the checkout page, the system checks it against these rules in real time.
	- **Shipping troubleshooting**: When an order shows "Shipment Failed" for a name-related reason, use these rules to check and fix the recipient information.


## Before You Start

- **Purpose**: To make sure order information is accepted by convenience store logistics systems (such as 7-Eleven order submission), the system strictly limits the recipient name format.


## Name Rules

### 1. Length Limits

The system counts **Chinese** and **English** characters separately.

| Type | Maximum Length | Minimum Length (Meet Any One) |
| :--- | :--- | :--- |
| **Chinese characters** | Up to **5** characters | At least **2** Chinese characters |
| **English letters** | Up to **10** letters | At least **4** English letters |
| **Mixed Chinese and English** | - | At least **1 Chinese character + 2 English letters** |

!!! example "Examples"
    - **Pass**: `王小明` (3 Chinese), `John` (4 English), `王Aa` (1 Chinese + 2 English).
    - **Fail**: `王` (too short), `王小明張李陳` (more than 5 Chinese characters).

### 2. Prohibited Characters

To avoid parsing errors in logistics systems, the name field can't contain any of the following:

- **Half-width/full-width special symbols**: Such as `!`, `@`, `#`, `$`, `。`, `、`, `「`, `」`, and so on.
- **Emoji**: Such as 😀, ❤️, 🎉, and so on.
- **Zhuyin symbols**: Including Zhuyin letters (ㄅㄆㄇ) and tone marks (ˇˋˊ˙).

### 3. Number Limits

Whether numbers are allowed depends on the order's **payment method**:

| Payment Method | Numbers Allowed | Reason |
| :--- | :--- | :--- |
| **Cash on delivery** | **Allowed** | Pickup doesn't require checking an ID, so the rules are looser |
| **Not cash on delivery** | **Not allowed** | Pickup requires checking an ID, and numbers usually aren't part of a legal name |


### 4. Space Handling

The system automatically handles spaces in the name field:

- **Leading and trailing spaces**: Removed automatically.
- **Spaces in the middle**: Removed automatically. For example, if you enter `王 小明`, the system saves it as `王小明`.



## Examples to Reference

If you or customer service need to help a customer troubleshoot a name issue, refer to the validation results below:

| Input | Result | Error Message |
| :--- | :--- | :--- |
| `賴.` | Fail | Can't contain special characters |
| `王小明張李陳` | Fail | Invalid name length |
| `😀賴` | Fail | Can't contain emoji |
| `王` | Fail | Invalid name length |
| `王ㄇ明` | Fail | Can't contain Zhuyin symbols |
| `John123` (non-cash on delivery order) | Fail | Can't contain numbers |
| `Tony1` (cash on delivery order) | **Pass** | - |



