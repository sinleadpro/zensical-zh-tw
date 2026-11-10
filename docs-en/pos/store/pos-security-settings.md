---
title: "Security Settings"
description: "Configure permissions for viewing cross-store orders and customer information, IP whitelist restrictions, and order source notifications to keep store operating data secure."
created: 2026-04-17 11:30
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有 POS 門市
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
  - 設定 POS 跨店權限
  - 配置 IP 白名單
  - 監控 POS 訂單來源
features:
  - POS 安全性設定
  - IP 白名單
  - 跨店資料權限
prerequisites: []
related: []
tags:
  - "POS Security"
  - "IP Whitelist"
  - "Permission Management"
  - "Cross-Store Access"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 安全性設定
  - 顯示 EC 網站、其他 POS 店訂單
  - 店長可查看他店顧客列表
  - 白名單
  - 訂單 IP 來源通知
paths:
  - POS 功能 > 所有 POS 商店
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=27199
  - https://www.cyberbiz.io/support/?p=5231
permalink: "https://help.cyberbiz.io/pos/store/pos-security-settings/"
comments: false
search:
  exclude: false
icon: lucide/shield-check
hide: []
---

# Security Settings
Configure permissions for viewing cross-store orders and customer information, IP whitelist restrictions, and order source notifications to keep store operating data secure.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

![](../../assets/images/POS-後台-所有POS商店-安全性設定01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Protect customer privacy**: Limit store managers to viewing customer data for their own store only. This prevents cross-store customer poaching and keeps brand operations stable.
    - **Strengthen login protection**: Set an IP whitelist so that only the store's fixed IP addresses can access the POS system, which eliminates the risk of unknown external access.
    - **Monitor logins from other IP addresses**: Turn on order IP source notifications to receive an immediate alert when a login from a different IP address occurs in the same store, which helps keep accounts secure.

## Before You Start { #prerequisites-pos-security }

- **Permission requirements**: Only the **Website Owner** can edit POS store security settings.


## Procedure { #operate-pos-security }

### Configure Store Permissions { #operate-pos-security-store }

Administrators can decide whether the POS front end displays orders from other stores, and whether store managers can view the customer lists of other stores.

1. Log in to the CYBERBIZ admin dashboard and go to **POS > POS Store List**.
2. In the **POS Store List**, click the **POS store name** you want to configure.
3. Scroll down to the **Security Settings** section, and turn the options on or off as needed.

    - **View orders from other stores**: Whether the POS order page displays cross-store orders.
    - **Store manager customer list access**: Whether store managers can look up customer information across stores.


### Configure IP Whitelist { #operate-pos-security-settings-ip-allowlist }

Use IP restrictions and notifications to strengthen network protection for the POS system.

1. Scroll down to the **Whitelist** section.
2. Turn the **Whitelist Feature** on.
3. Confirm the fixed IP address of each store device.
    - If you need to confirm the current device address in real time, you can use the [Online IP Lookup Tool](https://myip.com.tw/) to check it.
4. Enter the IP address, click **Add**, and create the complete IP whitelist.
5. After setup, logins from IP addresses that are not on the whitelist will show Forbidden.

!!! warning "IP Change Risk Notice"
    We recommend turning on this feature only for stores with a **fixed IP**. If a store uses a **dynamic IP**, we do not recommend enabling the whitelist, because an IP change may prevent the front end from logging in.

### Configure IP Source Notifications { #operate-pos-security-settings-ip-notifications }

1. Scroll down to the **Order IP Source Notifications** section.
2. Turn the **Notification Feature** on.
3. After setup, the system sends a notification when an order is placed from a different IP address within the same store.




