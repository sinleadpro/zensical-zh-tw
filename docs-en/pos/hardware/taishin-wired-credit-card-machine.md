---
title: "Taishin Wired Credit Card Machine"
description: "Apply for and install a wired credit card machine, including adapter cable selection, CYBERBIZ driver installation, and front- and back-office integration setup and testing."
created: 2026-03-25 17:45
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：安裝驅動程式
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有 POS 商店
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 如何安裝有線刷卡機
  - 信用卡機串接教學
  - POS信用卡機設定步驟
  - RS232轉接線購買建議
features:
  - 信用卡機串接
  - 多元支付
  - 感應支付
  - 自動對帳
prerequisites:
  - "設定 POS 商店與機台"
related:
  - pos/software/drivers/
  - pos/hardware/mypay-wireless-credit-card-machine/
tags:
  - credit_card_machine
  - taishin_payment
  - RS232
  - POS_hardware
  - card_checkout
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - POS 驅動程式
  - 付款方式設定
  - 信用卡(信用卡機)
paths:
  - POS 功能 > 所有 POS 商店 > 商店設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=4518
  - https://www.cyberbiz.io/support/?p=21480
  - https://www.cyberbiz.io/support/?p=51450
permalink: "https://help.cyberbiz.io/pos/hardware/taishin-wired-credit-card-machine/"
comments: false
search:
  exclude: false
icon: lucide/credit-card
hide: []
---

# Taishin Wired Credit Card Machine
Apply for and install a wired credit card machine, including adapter cable selection, CYBERBIZ driver installation, and front- and back-office integration setup and testing.
{ .subtitle }


[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Faster Checkout**: The system automatically syncs the amount to the card machine. Staff only need to guide the customer to insert or tap their card, which avoids input errors.
    - **Accurate Reconciliation**: Every card transaction has a matching system order number, which makes back-office reconciliation easier.


## Usage Notes { #prerequisites-taishin-terminal }

- **Application Timeline**: The bank reviews credit card machine applications. Timing depends on the bank's processing schedule.
- **Payment Type**: The system distinguishes between "integrated card machines" and "non-integrated card machines". This tutorial covers **integrated credit card machines**.
- **Multi-Payment**: In addition to physical credit cards, integrated machines typically support Apple Pay, Google Pay, and Samsung Pay.
- **Cable Requirements**: Wired credit card machines **must** use a specific adapter cable to work properly.

!!! warning "Required Hardware Cables"
    Due to driver binding issues, be sure to purchase the **[SUNBOX brand USB to RS232 adapter cable](https://24h.pchome.com.tw/prod/DCAX1V-A9005MDWH)**. Do not buy adapter cables from other brands, as they may not be recognized or may fail to bind.

    ![](../../assets/images/POS-裝置-有線刷卡機限定傳輸線SUNBOX01.en.jpg){ .small-image }

## Application and Prerequisites { #prerequisites-preparation }

1. **Submit Application**: After you receive the **CYBERBIZ POS Multi-Payment Application Notification Email**, send the required business information to your onboarding consultant.

    ![](../../assets/images/POS-通知信件-有線信用卡機申請01.en.png){ .small-image }

2. **Purchase Cables**: Confirm that you have purchased the SUNBOX brand USB to RS232 adapter cable.
3. **Receive the Machine**: After the bank ships the card machine to your store, you can begin the installation process.


## Setup Procedure { #operate-taishin-terminal }

### Step 1: Download and Install the Hardware Driver { #operate-taishin-terminal-step-a-download }

Before connecting the hardware, install the communication driver on your computer.

1. Download the [CYBERBIZ hardware driver](../software/drivers.md).
2. Run the installer and open it.

    ![](../../assets/images/POS-安裝-有線信用卡機-啟用01.en.png){ .small-image }


### Step 2: Hardware Connection and Port Settings { #operate-taishin-terminal-step-b-hardware }

1. **Connect the cables**:
    - Insert the **USB connector** into the RS232 port on the back of the credit card machine.

        ![](../../assets/images/POS-安裝-有線信用卡機-啟用02.en.jpg){ .small-image }

    - Insert the **RS232 connector** into the computer where the POS system is installed.

        ![](../../assets/images/POS-安裝-有線信用卡機-啟用03.en.jpg){ .small-image }

2. **Software Detection**: In the open CYBERBIZ driver window, select **Taishin Credit Card Machine**.

    ![](../../assets/images/POS-驅動程式-綁定有線信用卡機01.en.png){ .small-image }

3. **Connection Complete**: The credit card machine status shows **Connected**.

    ![](../../assets/images/POS-驅動程式-綁定有線信用卡機02.en.png){ .small-image }

    > Tip: If a detection message appears, you can ignore it. Just make sure the correct item is selected in the menu.
        ![](../../assets/images/POS-驅動程式-綁定有線信用卡機03.en.png){ .small-image }

### Step 3: Quick Connection Test { #operate-taishin-terminal-step-c-connection }

1. Click the **Test** button in the driver.

    ![](../../assets/images/POS-驅動程式-綁定有線信用卡機04.en.png){ .small-image }

2. If the connection succeeds, the credit card machine automatically displays a test card-swipe screen.

    ![](../../assets/images/POS-安裝-有線信用卡機-測試01.en.png){ .small-image }

3. Once the screen appears, press the **Clear** key on the card machine to end the test.



### Step 4: Back Office Activation and Checkout Test { #operate-taishin-terminal-step-d-admin }

1. **Back Office Setup**:
    - Log in to the admin panel and go to **POS > POS Store List**.
    - Click the store name, then open the **Payment Method** tab.
    - Switch the **Credit Card (Credit Card Machine)** option to `開啟 (ON)` and save.

    ![](../../assets/images/POS-後台-所有POS商店-付款設定-新增有線信用卡機付款方式01.en.png){ .screenshot }

2. **Front Office Test**:
    - Go to the POS front end, select any products, and check out.
    - Select **Credit Card (Credit Card Machine)** as the payment method, then click **Collect**.
    - The card machine should automatically display the order amount. Complete the card payment process.

    ![](../../assets/images/POS-前台-結帳-有線信用卡機結帳1.en.png){ .screenshot }



## FAQ { #faq-taishin-terminal }


??? quote "Can I connect this wired card machine to a tablet (iPad)?"
    No. A wired card machine must connect to a computer through a USB adapter cable to run the driver. If you use a tablet, we recommend the [MYPAY wireless credit card machine](mypay-wireless-credit-card-machine.md).


