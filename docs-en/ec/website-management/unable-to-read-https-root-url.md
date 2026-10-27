---
title: "Unable to Load the HTTPS Root URL"
description: "After you move your website from another platform to CYBERBIZ, http://your-domain may open normally while https://your-domain cannot be loaded. This is usually related to whether your domain registrar supports redirects for the root domain (naked domain)."
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
  - 診斷_HTTPS_連線問題
  - 執行網域移轉流程
features:
  - SSL 憑證
  - 根網域轉址
  - 網域移轉
prerequisites:
  - "需具備第三方網域商的管理權限"
  - "網域需已指向 CYBERBIZ"
related:
  - ec/website-management/domain-management/
tags:
  - Troubleshooting
  - HTTPS
  - SSL
  - "Domain Redirects"
  - "Root Domain"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 網域管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=29144
permalink: "https://help.cyberbiz.io/ec/website-management/unable-to-read-https-root-url/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---
# Unable to Load the HTTPS Root URL

After you move your website from another platform to CYBERBIZ, http://your-domain may open normally while https://your-domain cannot be loaded. This is usually related to whether your domain registrar supports redirects for the root domain (naked domain).
{ .subtitle }


## Diagnosis: Why Doesn't HTTPS Load? { #intro-https-root }

During a website migration, the root domain (`example.com`) is usually redirected automatically to a subdomain (`www.example.com`) to protect search engine ranking (SEO) and the user experience.

However, the basic redirect feature of some domain registrars (such as GoDaddy) only supports HTTP. When a user visits the root URL over HTTPS, the registrar can't complete the SSL handshake, so the page shows "Connection timed out" or "Unable to connect".

!!! tip "How to Tell "
    1.  Enter `http://example.com` → **successfully** redirects to `https://www.example.com`.
    2.  Enter `https://example.com` → **fails** and the page can't be loaded.
    - *If both of these are true, your domain registrar doesn't support HTTPS redirects for the root domain.*


## Solution: Transfer the Domain to a Registrar with Better Support { #operate-https-root }

The simplest and most stable solution right now is to transfer your domain to a registrar with better HTTPS redirect support (such as Gandi). **The example below transfers a domain from GoDaddy to Gandi:**

### Step 1: Request a Transfer out from Your Current Registrar { #operate-https-root-export }

1. Log in to the **GoDaddy dashboard** and open **Domain management**.
2. Find the domain you want to transfer and click **Transfer out**.
3. Follow the prompts and click **Continue with transfer**.
4. Click the link to **view the authorization code**, and copy the **authorization code** for later.

![](https://www.cyberbiz.io/support/wp-content/uploads/https開頭網址無法順利讀取1.png){ .screenshot }

### Step 2: Start the Transfer in at the New Registrar { #operate-https-root-import }

1. Log in to the **Gandi dashboard** and select **域名 > 移轉**.
2. Enter your domain and search for it.
3. During the transfer, enter the **authorization code** you got in step 1.
4. Complete checkout.
5. Follow Gandi's instructions to complete **email verification**.

![](https://www.cyberbiz.io/support/wp-content/uploads/https開頭網址無法順利讀取2.png){ .screenshot }

### Step 3: Set up DNS Again { #operate-https-root-dns }

After the domain transfer is complete, check and [set up your DNS records](domain-management.md) again to make sure the URL points to the CYBERBIZ servers.


## FAQ { #faq-https-root }

??? quote "Will transferring the domain take my website offline?"
    If DNS is set up correctly before the transfer and the TTL value is reasonable, the transfer usually doesn't take your website offline. However, domain record updates can take 24–48 hours to take effect.

??? quote "Who should I contact if I run into problems?"
    Domain DNS management is a third-party service and isn't directly managed by CYBERBIZ. If you run into technical problems during the transfer, contact your domain registrar's support first.


## Next Steps { #next-steps-https-root }

<div class="grid cards" markdown>

- :lucide-move-right:{ .lg }
  [__How to Transfer a Domain to Gandi (Official Guide)__](https://docs.gandi.net/zh-hant/domain_names/transfer/description.html)
  Technical documentation from Gandi that guides you through moving an existing domain to its platform.

</div>

