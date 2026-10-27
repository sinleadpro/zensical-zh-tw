---
title: "Domain Management"
description: "After you buy a custom domain from a third-party provider, point the domain to your CYBERBIZ store with DNS settings, and then finish binding it in the CYBERBIZ admin panel."
created: 2026-03-02 00:00
last_modified: 2026-06-30 08:02
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 遠傳e管家已終止服務，下架對應內容
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
  - CNAME 設定
  - 根網域轉址
features:
  - 網域管理
  - DNS 設定
  - CNAME
prerequisites: []
related: []
tags:
  - "Domain Settings"
  - DNS
  - CNAME
  - HiNet
  - "Chunghwa Telecom"
  - PChome
  - GoDaddy
  - Gandi
  - TWNIC
  - Net-Chinese
  - "Taiwan Mobile"
  - Yuanzhen
  - Pumeng
  - "Far EasTone e-Manager"
  - "Far EasTone"
acoiv: activate
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 管理中心 > 網域管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10419
  - https://www.cyberbiz.io/helpcenter/?p=10433
  - https://www.cyberbiz.io/helpcenter/?p=295
  - https://www.cyberbiz.io/helpcenter/?p=305
  - https://www.cyberbiz.io/helpcenter/?p=314
  - https://www.cyberbiz.io/helpcenter/?p=3201
  - https://www.cyberbiz.io/helpcenter/?p=550
  - https://www.cyberbiz.io/helpcenter/?p=6867
  - https://www.cyberbiz.io/helpcenter/?p=7280
  - https://www.cyberbiz.io/helpcenter/?p=9050
  - https://www.cyberbiz.io/helpcenter/?p=9083
  - https://www.cyberbiz.io/support/?p=1
  - https://www.cyberbiz.io/support/?p=106
  - https://www.cyberbiz.io/support/?p=13235
  - https://www.cyberbiz.io/support/?p=140
  - https://www.cyberbiz.io/support/?p=24717
  - https://www.cyberbiz.io/support/?p=3445
  - https://www.cyberbiz.io/support/?p=36655
  - https://www.cyberbiz.io/support/?p=37604
  - https://www.cyberbiz.io/support/?p=43182
  - https://www.cyberbiz.io/support/?p=43442
  - https://www.cyberbiz.io/support/?p=4540
permalink: "https://help.cyberbiz.io/ec/website-management/domain-management/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---
# Domain Management

After you buy a custom domain from a third-party provider, point the domain to your CYBERBIZ store with DNS settings, and then finish binding it in the CYBERBIZ admin panel.
{ .subtitle }

![](../../assets/images/EC-後台-管理中心-網域管理-新增網域01.en.png){ .hero-page }

## Before You Start { #prerequisites-domain-mgmt }

Depending on your domain provider, setup usually involves these two key settings:

1.  **CNAME setting (required)**: Point the URL that starts with `www` (such as `www.yourshop.com`) to the CYBERBIZ servers.
2.  **Root domain redirect (depends on the provider)**: Makes sure customers who enter the URL without `www` (such as `yourshop.com`) are also redirected to your store.




## DNS Setup Guides for Major Providers { #operate-domain-mgmt-dns }

Find your domain registrar below and follow its setup instructions:

=== "HiNet (Chunghwa Telecom)"

    1. Log in to the [HiNet dashboard](https://domain.hinet.net/#/dnlogin).
        ![](../../assets/images/HiNet-後台-網域資訊-新增CNAME01.en.png)
    2. **CNAME setting**: Go to **HiNet DNS 代管 > 更新 DNS 紀錄**. Delete the existing `A 紀錄`, and then add a new record.
        ![](../../assets/images/HiNet-後台-網域資訊-新增CNAME02.en.png)

        - **Ldata (host name/alias)**: `www`
        - **Record type**: `CNAME`
        - **Rdata (IP/host name)**: Enter the system default URL, for example: `xxx.cyberbiz.co`

            > **Do not add `.`** after the host URL.

            ![](../../assets/images/HiNet-後台-網域資訊-新增CNAME03.en.png)


    3. **Redirect setting**: Go to **轉址服務 > 設定轉址**.
        ![](../../assets/images/HiNet-後台-網域資訊-設定轉址01.en.png)

        - **Website title**: Enter a custom website title.
        - **Source URL**: Leave blank.
        - **Destination URL**: Enter the **Ldata (host name/alias)** from the CNAME record, for example: `www...`
        - **Address bar display**: `目的網址`

            ![](../../assets/images/HiNet-後台-網域資訊-設定轉址02.en.png)

    4. Copy the **host IP** shown in the **instructions**.
        ![](../../assets/images/HiNet-後台-網域資訊-設定轉址03.en.png)
    5. Go to **DNS代管 > 更新DNS紀錄** and click **Add a row**.

        - **Record type**: `A`
        - **Rdata (IP/host name)**: Paste the **host IP**.

        ![](../../assets/images/HiNet-後台-網域資訊-設定轉址04.en.png)

=== "PChome"

    1. Log in to the [PChome dashboard](https://myname.pchomebiz.com.tw/) and click **Manage My Domains**.
        ![](../../assets/images/PCHOME-後台-管理我的網址-新增CNAME01.en.png)
    2. **CNAME setting**: Click **Enter** in the **DNS settings and changes** column.
        ![](../../assets/images/PCHOME-後台-管理我的網址-新增CNAME02.en.png)

        - **Host**: `www`
        - **Address**: Enter the system default URL, for example: `xxx.cyberbiz.co.`

            > **Add `.`** after the host URL.

        - **Type**: `CNAME`

        ![](../../assets/images/PCHOME-後台-管理我的網址-新增CNAME03.en.png)

    3. **Redirect setting**:

        - **Address**: Enter your brand's custom URL, for example: `http://www...`
        - **Type**: `redirect`

        ![](../../assets/images/PCHOME-後台-管理我的網址-設定轉址01.en.jpg)


=== "GoDaddy"

    1. Log in to the [GoDaddy dashboard](https://www.godaddy.com/zh) and click **DNS** in the domain section.
        ![](../../assets/images/Godaddy-後台-網域-新增CNAME01.en.png)
    2. **CNAME setting**: Select the **DNS Records** tab, find the CNAME record for the domain, and click **Edit**.
        ![](../../assets/images/Godaddy-後台-網域-新增CNAME02.en.png)

        - **Type**: `CNAME`
        - **Name**: `www`
        - **Value**: Enter the system default URL, for example: `xxx.cyberbiz.co.`
        - **TTL**: `1天`

        ![](../../assets/images/Godaddy-後台-網域-新增CNAME03.en.png)

    3. **Redirect setting**: Go to the **Forwarding** tab and select **Add Forwarding** for the domain.
        ![](../../assets/images/Godaddy-後台-網域-設定轉址01.en.png)

        - **Enter the destination URL**: Enter your brand's custom URL, for example: `http://www...`

        ![](../../assets/images/Godaddy-後台-網域-設定轉址02.en.png)


=== "Gandi"

    1. Log in to the [Gandi dashboard](https://www.gandi.net/zh-Hant), go to **Domain names**, and click the domain you bought.
        ![](../../assets/images/GANDI-後台-域名-新增CNAME01.en.png)
    2. **CNAME setting**: Click **DNS Records**, and then click **Add record**.
        ![](../../assets/images/GANDI-後台-域名-新增CNAME02.en.png)

        - **Type**: `CNAME`
        - **TTL (cache time)**: `10800`
        - **Unit**: `秒`
        - **Name**: `www`
        - **Hostname**: Enter the system default URL, for example: `xxx.cyberbiz.co.`

            > **Add `.`** after the host URL.

        !!! info "Troubleshooting Domain Setup Errors"
            If an error message appears during setup, first delete the default CNAME record in your Gandi account, and then run the setup again.

        ![](../../assets/images/GANDI-後台-域名-新增CNAME03.en.png)

    3. **Redirect setting**: Go to **域名 > 網頁轉址** and click **Add web forwarding address**.
        ![](../../assets/images/GANDI-後台-域名-設定轉址01.en.png)
        ![](../../assets/images/GANDI-後台-域名-設定轉址02.en.png)

        - **Location**: Select `http:// + https://` and leave the field after it blank.
        - **Forward to**: Select ` http://` and enter your brand's custom URL, for example: `http://www...`
        ![](../../assets/images/GANDI-後台-域名-設定轉址03.en.png)

=== "TWNIC"

    1. Log in to the [TWNIC dashboard](https://rs.twnic.tw/cgi-bin/setupdns.cgi) and go to **DNS 設定服務 > DNS 設定/代管**.

        - **Domain name**: Enter the domain you want to add and select the domain suffix.
        - **Verification password**: Enter your password.

        ![](../../assets/images/TWNIC-後台-DNS設定代管-新增CNAME01.en.png)

    2. **CNAME setting**: Select **Host mode (hosted by TWNIC)**.

        - **Domain/host name**: Enter your brand's custom URL, for example: `www...com.tw`
        - **Record type**: `CNAME`
        - **IP address/host name**: Enter the system default URL, for example: `xxx.cyberbiz.co.`

            > **Add `.`** after the host URL.

        ![](../../assets/images/TWNIC-後台-DNS設定代管-新增CNAME02.en.png)

=== "Net-Chinese"

    1. Log in to the [Net-Chinese dashboard](https://www.net-chinese.com.tw/), go to **域名管理 > 域名總覽**, and click the domain you bought.
        ![](../../assets/images/網路中文-後台-域名管理-新增CNAME01.en.png)
    2. **CNAME setting**: In the left menu, select **DNS > DNS紀錄設定** and enter the following:

        - **Record type**: `CNAME`
        - **Host name/alias**: `www`
        - **IP/domain**: Enter the system default URL, for example: `xxx.cyberbiz.co.`

        ![](../../assets/images/網路中文-後台-域名管理-新增CNAME02.en.png)

=== "Taiwan Mobile"

    1. Log in to the [Taiwan Mobile dashboard](https://domains.tfn.net.tw/domains/session/showConsoleIndex.do) and go to **產品服務 > 域名申請服務 > 轉址設定**.
        ![](../../assets/images/台灣大哥大-後台-轉址設定-新增CNAME01.en.png)
    2. **CNAME setting**: Click **DNS hosting**.
        ![](../../assets/images/台灣大哥大-後台-轉址設定-新增CNAME02.en.png)

        - **Setting type**: `CNAME(別名)`
        - **Alias**: `www`
        - **Target host name**: Enter the system default URL, for example: `xxx.cyberbiz.co`

        ![](../../assets/images/台灣大哥大-後台-轉址設定-新增CNAME03.en.png)

=== "Yuanzhen"

    1. Log in to the [Yuanzhen dashboard](https://twnoc.net/whmcs/login) and go to **網域 > Manage DNS**.
        ![](../../assets/images/遠振-後台-ManageDNS-新增CNAME01.en.png)
    2. **CNAME setting**: Select the domain you bought, click :lucide-pencil:, and click **Add Record**.
        ![](../../assets/images/遠振-後台-ManageDNS-新增CNAME02.en.png)

        - **TYPE**: `CNAME`
        - **NAME**: `www`
        - **TTL**: `14400`
        - **Cname**: Enter the system default URL, for example: `xxx.cyberbiz.co.`
        ![](../../assets/images/遠振-後台-ManageDNS-新增CNAME03.en.png)

=== "Pumeng"

    1. Log in to the [Pumeng dashboard](https://www.pumo.com.tw/) and go to **Domain Management**.
        ![](../../assets/images/捕夢網-後台-網域管理-新增CNAME01.en.png)
    2. **CNAME setting**: Select the domain you bought, open the dropdown menu, and select **Set DNS records**.
        ![](../../assets/images/捕夢網-後台-網域管理-新增CNAME02.en.png)

        - **Record type to add**: `CNAME`
        - **Host name**: `www`
        - **CNAME alias**: Enter the system default URL, for example: `xxx.cyberbiz.co`

        ![](../../assets/images/捕夢網-後台-網域管理-新增CNAME03.en.png)




=== "Far EasTone"

    1. Log in to the [Far EasTone dashboard](https://rs.seed.net.tw/) and go to **My Domain Management**.
        ![](../../assets/images/遠傳-後台-我的域名管理-新增CNAME01.en.png)
    2. Enter your account information.

        - **Tax ID number/national ID number**: Enter the one that matches your account type.
        - **Password**: Enter the one that matches your account type.
        - **Domain name**: Enter the domain you want to add and select the domain suffix.
        ![](../../assets/images/遠傳-後台-我的域名管理-新增CNAME02.en.png)
    3. Select **DNS (Host / IP)**.
        ![](../../assets/images/遠傳-後台-我的域名管理-新增CNAME04.en.png)
    4. Select **Far EasTone DNS hosting mode**.
        ![](../../assets/images/遠傳-後台-我的域名管理-新增CNAME05.en.png)
    5. **CNAME setting**:
        - **Host**: `www`
        - **Record type**: `CNAME`
        - **IP/Domain/Content**: Enter the system default URL, for example: `xxx.cyberbiz.co`
        ![](../../assets/images/遠傳-後台-我的域名管理-新增CNAME06.en.png)
    6. When you finish, click **Hosting settings**.
        ![](../../assets/images/遠傳-後台-我的域名管理-新增CNAME07.en.png)


## Add the Domain in the CYBERBIZ Admin Panel { #operate-domain-mgmt-add }

After you finish the DNS settings with your provider, go back to CYBERBIZ to finish binding the domain:

1.  Log in to the CYBERBIZ admin panel and go to **Website Management > Domain**.
2.  Click **Add a domain you already own** and enter the full URL (for example, `www.yourshop.com`).
3.  Select **Always redirect customers here**.


!!! info "When Changes Take Effect"
    - DNS changes usually take **24 to 48 hours** to take effect.
    - About 1 hour after the change takes effect, you can enter the URL in the CYBERBIZ admin panel.
    - Use [DNS Checker](https://dnschecker.org/#CNAME/) to check whether your domain points to the right place.

![](../../assets/images/EC-後台-管理中心-網域管理-新增網域01.en.png)


