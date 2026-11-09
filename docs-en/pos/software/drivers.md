---
title: Drivers
description: "The POS driver connects hardware devices such as invoice printers and barcode scanners, and must be installed and running before you open the POS front-end."
created: 2026-04-21 12:15
last_modified: 2026-08-05 19:00
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
  - 軟體安裝
sites:
  - TW
audiences:
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
  - 安裝 POS 驅動程式
  - 排除 POS 安裝錯誤
  - 下載 POS App
features:
  - POS 驅動程式
  - 硬體串接
prerequisites: []
related: []
tags:
  - Drivers
  - "POS App"
  - Installation
  - Troubleshooting
acoiv: activate
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=9556
permalink: "https://help.cyberbiz.io/pos/software/drivers/"
comments: false
search:
  exclude: false
icon: lucide/cable
hide: []
---

# Drivers
The POS driver is the key component that connects hardware devices (such as invoice printers and barcode scanners), ensuring it is properly installed and running before launching the POS front-end.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

## Usage Notes { #prerequisites-drivers }

- **Operating system**: Only **Windows** is supported. macOS and Linux are not supported.
- **Version requirement**: POS APP V.7.0.0 and later versions are only compatible with Windows 10 or later.
- **Startup order**: Before using the POS system, **start the driver first**, then open the POS front-end page.
- **Exception**: If you use the **MyPay credit card reader plan**, do not install this POS driver.

## Download and Install { #operate-drivers }

### Step 1: Download the Installation File { #operate-drivers-step-a-download }

Click the link below to download the latest driver:

- [**POS APP Download (V.7.9.98)**](https://drive.google.com/file/d/1RbtQz2CZ4aI7UP12LHygqx1HO7297sjy/view?usp=drive_link)

`備註：`

`- New feature in this release: interim closing receipt printing`


### Step 2: Run the Installer { #operate-drivers-step-b-run }

After the download completes, double-click `cyberbiz-pos-app Setup.exe` to complete the installation. If a security warning appears, see the **FAQ** below to troubleshoot.



## FAQ { #faq-drivers }

??? quote "How do I resolve the **Not commonly downloaded** warning during download?"

    When downloading with Edge or Chrome, Microsoft Defender SmartScreen may warn that the file is not commonly downloaded.

    **Warning message:**

    `[FILENAME].exe 不常下載。開啟前，請確認您信任 [FILENAME].exe`

    **Troubleshooting steps:**

    1. Click :lucide-move-down: and select **More options (⋯)** in the download menu.
    2. Select **Keep**.
    3. In the warning dialog, click **Show more** > **Keep anyway**.

    ![](../../assets/images/POS-安裝-驅動程式-下載出現警告訊息01.en.gif)

    !!! info "Security Mechanism Explanation"
        This warning comes from the Microsoft Defender SmartScreen security mechanism and does not mean the downloaded file is malicious. For details, see the [official FAQ](https://feedback.smartscreen.microsoft.com/smartscreenfaq.aspx#).


??? quote "What should I do if **Windows protected your PC** appears when opening the installer?"

    This is a Windows security feature that blocks unrecognized apps from starting.

    **Warning message:**

    `Windows protected your PC
    Microsoft Defender SmartScreen prevented an unrecognized app from starting. Running this app might put your PC at risk.`

    **Troubleshooting steps:**

    1. In the warning message, click **More info**.

        ![](../../assets/images/POS-安裝-驅動程式-Windows已保護您的電腦01.en.png){ .small-image }

    2. Click the **Run anyway** button.

        ![](../../assets/images/POS-安裝-驅動程式-Windows已保護您的電腦02.en.png){ .small-image }

??? quote "What should I do if the **A JavaScript error occurred in the main process** error message appears?"

    This error usually means your Windows is missing required system packages.

    **Troubleshooting steps:**

    1. Download and install the official Microsoft package: [**Visual C++ Redistributable**](https://docs.microsoft.com/zh-tw/cpp/windows/latest-supported-vc-redist?view=msvc-170).
    2. **Installation priority**:

        - Install the **x86 version** first.

            ![](../../assets/images/Microsoft-VisualC++套件-POS驅動程式-疑難排解01.en.png){ .screenshot }

        - If the error still appears after installation, try installing the **x64 version**.

            ![](../../assets/images/POS-安裝-驅動程式-錯誤提醒01.en.png){ .small-image }

    3. After installation, restart the POS driver.


