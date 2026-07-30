---
title: 驅動程式
description: POS 驅動程式是串接硬體設備（如發票機、掃碼槍）的關鍵核心，確保在啟動 POS 前台前已正確安裝並執行。
created: 2026-04-21 12:15
last_modified: 2026-07-01 10:40
lang: zh-TW
type: tutorial
status: update
version: 1.1.1
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
  - admin
difficulty: intermediate
tnb: branch
plans:
  - 進階PLUS
  - 高手PLUS
  - 企業
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
  - 驅動程式
  - POS_App
  - 安裝教學
  - 故障排除
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

# 驅動程式
POS 驅動程式是串接硬體設備（如發票機、掃碼槍）的關鍵核心，確保在啟動 POS 前台前已正確安裝並執行。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 智能 POS
{ .doc-badge }

## 使用須知

- **作業系統**：僅支援 **Windows**，不支援 macOS 或 Linux。
- **更新版本**：POS APP V.7.0.0 及更新版本僅相容於 Windows 10 或更高版本作業系統。
- **啟動順序**：使用 POS 系統前，請務必 **先開啟驅動程式**，再開啟 POS 前台頁面。
- **例外狀況**：若您使用的是 **MyPay 刷卡機方案**，請勿安裝此 POS 驅動程式。

## 下載與安裝

### 步驟 1：下載安裝檔

請點擊下方連結下載最新版驅動程式：

- [**POS APP 下載 (V.7.9.96)**](https://drive.google.com/file/d/1SeLpr3mQifNvrbdic_RNVKcKZnkgGN1J/view?usp=sharing)

`備註：`

`- 支援寄存商品提領明細`


### 步驟 2：執行安裝程式

下載完成後，雙擊執行 `cyberbiz-pos-app Setup.exe`，完成安裝。若系統出現安全警告，請參考後續的 **常見問題** 進行排除。



## 常見問題

??? quote "下載時出現 **不常下載** 警告，該如何排除？"

    當使用 Edge 或 Chrome 下載時，Microsoft Defender SmartScreen 可能會提示檔案不常下載。

    **警告訊息：**
    
    `[FILENAME].exe 不常下載。開啟前，請確認您信任 [FILENAME].exe`

    **排除步驟：**

    1. 點擊 :lucide-move-down: 下載選單中的 **更多選項 (⋯)**。
    2. 選擇 **保留**。
    3. 在警示視窗中，點擊 **顯示更多** > **仍要保留**。

    ![](../../assets/images/POS-安裝-驅動程式-下載出現警告訊息01.gif)

    !!! info "安全機制說明"
        此警告訊息源自 Microsoft Defender SmartScreen 安全機制，並不代表所下載檔案即具有惡意性質。詳情請參考 [官方常見問答集](https://feedback.smartscreen.microsoft.com/smartscreenfaq.aspx#)。


??? quote "開啟安裝檔案時顯示 **Windows 已保護您的電腦**，該如何排除？"

    這是 Windows 的安全機制，阻止了未辨識應用程式的啟動。

    **警告訊息：**

    `Windows 已保護您的電腦 
    Microsoft Defender SmartScreen 已防止某個無法辨識的應用程式啟動。執行此應用程式可能會讓您的電腦暴露在風險中。`

    **排除步驟：**

    1. 在警示訊息中點擊 **其他資訊**。

        ![](../../assets/images/POS-安裝-驅動程式-Windows已保護您的電腦01.png){ .small-image }

    2. 點擊按鈕 **仍要執行**。

        ![](../../assets/images/POS-安裝-驅動程式-Windows已保護您的電腦02.png){ .small-image }

??? quote "出現 **A JavaScript error occurred in the main process** 錯誤訊息，該如何排除？"

    此錯誤通常代表您的 Windows 缺少必要的系統套件。

    **排除步驟：**

    1. 下載並安裝 Microsoft 官方提供的套件：[**Visual C++ 可轉散發套件**](https://docs.microsoft.com/zh-tw/cpp/windows/latest-supported-vc-redist?view=msvc-170)。
    2. **安裝優先順序**：

        - 請優先安裝 **x86 版本**。

            ![](../../assets/images/Microsoft-VisualC++套件-POS驅動程式-疑難排解01.png){ .screenshot }

        - 若安裝後仍出現錯誤，請再嘗試安裝 **x64 版本**。

            ![](../../assets/images/POS-安裝-驅動程式-錯誤提醒01.png){ .small-image }
            
    3. 安裝完成後，重新啟動 POS 驅動程式。

    
