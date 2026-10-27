---
title: "Cloudflare SSL Conflict"
description: "Cloudflare is a well-known DNS hosting and CDN provider. If your domain is hosted on Cloudflare, you must configure its Proxy feature in a specific way when you point the domain to CYBERBIZ. This makes sure your website loads correctly and the SSL certificate is applied properly."
created: 2026-03-10 00:00
last_modified: 2026-06-30 08:02
lang: en-US
type: reference
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 管理中心
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
  - 解決_Cloudflare_SSL_衝突
  - 關閉_Cloudflare_Proxy
features:
  - SSL 憑證
  - 網域管理
  - DNS 設定
prerequisites:
  - "需具備 Cloudflare 帳戶管理權限"
  - "網域已完成 Cloudflare 代管設定"
related: []
tags:
  - Troubleshooting
  - DNS
  - SSL
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 管理中心 > 網域管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4598
  - https://www.cyberbiz.io/support/?p=28727
permalink: "https://help.cyberbiz.io/ec/website-management/cloudflare-ssl-conflict/"
comments: false
search:
  exclude: false
icon: lucide/shield-alert
hide: []
---
# Cloudflare SSL Conflict

Cloudflare is a well-known DNS hosting and CDN provider. If your domain is hosted on Cloudflare, you must configure its Proxy feature in a specific way when you point the domain to CYBERBIZ. This makes sure your website loads correctly and the SSL certificate is applied properly.
{ .subtitle }


## Before You Start { #prerequisites-cf-ssl }

- **Avoid SSL conflicts**: CYBERBIZ provides and automatically maintains SSL certificates for all merchant websites. If Cloudflare's Proxy (orange cloud) feature is on, Cloudflare's certificate conflicts with the CYBERBIZ certificate. Common symptoms include: **a 521 error on the website, an endless redirect loop, or a website that can't be opened at all.**
- **Third-party updates**: The Cloudflare interface may change over time. If the button names and paths in this guide (such as DNS Records and Proxy status) differ slightly from what you see, follow Cloudflare's latest official documentation. CYBERBIZ mainly provides system integration and domain pointing services. If a third-party platform changes its interface and the steps change, CYBERBIZ is not obligated to update this guide to match. For detailed steps on the domain provider's side, contact that platform's customer service first.


## Turn off the Cloudflare Proxy { #operate-cf-ssl }

To point your domain to CYBERBIZ correctly and keep it running reliably, adjust your DNS settings as follows:

### 1. Open the DNS Management Page { #operate-cf-ssl-dns }

1. Log in to your **Cloudflare dashboard**.
2. Select the **domain** you want to set up.
3. In the left menu, click **DNS > Records**.

### 2. Edit the CNAME Record { #operate-cf-ssl-cname }

1. In the record list, find the **CNAME record** that points to CYBERBIZ (for example, the record named `www`).
2. Click **Edit** on the right side of the record.
3. Find the **Proxy status** field.
4. Switch it to **DNS only**.
    - The icon should change from an orange cloud to a **gray cloud**.
5. Click **Save**.

![](https://www.cyberbiz.io/support/wp-content/uploads/CloudFlare注意事項1.png){ .screenshot }



