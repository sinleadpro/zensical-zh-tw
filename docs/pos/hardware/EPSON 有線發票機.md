---
title: EPSON 有線發票機
description: 了解如何安裝 EPSON TM-T82III 發票機，包含硬體整備、Virtual Port Driver 驅動安裝、COM Port 指派以及紙張寬度調整。
created: 2026-03-25 20:45
last_modified: 2026-05-28 14:48
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結：POS驅動程式
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - POS 功能
sites:
  - TW
audiences:
  - admin
  - clerk
difficulty: intermediate
tnb: branch
plans:
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents:
  - 如何安裝EPSON發票機
  - TM-T82III驅動程式下載
  - 解決EPSON發票機COM_Port衝突
  - 調整發票列印寬度
features:
  - 發票機串接
  - TM_Virtual_Port_Driver
  - 58mm發票列印
  - 自動裁刀
prerequisites: []
related: []
tags:
  - EPSON
  - 發票機
  - TM-T82III
  - POS_硬體
  - 驅動程式
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - POS 驅動程式
  - Port Assignment Tool
  - TM-T82III Utility
paths:
  - POS 功能 > 所有 POS 商店 > 修改 POS 設定
layouts: []
wp_url: []
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/printer
hide: []
---

# EPSON 有線發票機
透過正確安裝 EPSON TM-T82III 專業發票機並配置虛擬 COM Port，商家可實現穩定、快速的電子發票列印作業。本文將引導您完成從硬體安裝到驅動程式設定的完整流程。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 進階 PLUS / 高手 PLUS / 企業
{ .doc-badge }

!!! tip "應用情境"
    - **門市高效收銀**：利用 EPSON 高速列印特性，縮短顧客在櫃檯等待發票產出的時間。
    - **節省空間配置**：TM-T82III 的精巧設計適合空間有限的結帳櫃檯。
    - **稅務合規自動化**：結帳完成立即產出符合財政部規範的電子發票證明聯。


## 使用須知

- **適用型號**：本教學專針對 **EPSON TM-T82III** 型號撰寫。
- **耗材規格**：預設使用 **58mm** 電子發票感熱紙，安裝時需確認隔板已正確放置。


## 操作流程

### 步驟一：下載與安裝 POS 驅動程式

在設定硬體前，請先確保電腦具備通訊基礎。

1. 前往下載 [CYBERBIZ POS 驅動程式]()。
2. 完成安裝後開啟程式，靜待自動更新至最新版本。



### 步驟二：硬體整備與紙捲安裝

參考發票機箱附的說明手冊或 [產品說明書清單](https://support.epson.net/setupnavi/?PINF=bsmanual&OSC=IOS&LG2=ZH&MKN=TM-T82III) 的 [User’s Guide](https://download4.epson.biz/sec_pubs/bs/pdf/TM-T82III_ug_asia_04.pdf) 執行以下動作：

1. **安裝隔板**：打開發票機上蓋，確認已安裝箱內附帶的「隔板」，以固定 58mm 規格的紙捲。
2. **放置感熱紙**：放入電子發票證明聯專用感熱紙，確認感應面朝上。
3. **連接電源**：將發票機接通電源並開啟開關。


### 步驟三：安裝 Virtual Port Driver 並指派 COM Port

此步驟為連線成功的關鍵，請務必按照順序操作。

1. **下載驅動**：前往 [EPSON 軟體列表](https://support.epson.net/setupnavi/?PINF=swlist&OSC=IOS&LG2=ZH&MKN=TM-T82III) 下載 [TM Virtual Port Driver](https://download3.ebz.epson.net/dsc/f/03/00/16/59/59/37c78fb33341c071dbfc05bdbe456ca853037eaf/TMVirtualPortDriver870c.zip)。
2. **執行安裝**：完成安裝後，**強烈建議重新啟動電腦**。
3. **實體連線**：使用 USB 線將發票機連接至 Windows 電腦。
4. **指派 COM Port**：
    - 開啟 **EPSON TM Virtual Port Driver Port Assignment Tool** 軟體。
    - 參考 `C:\Program Files (x86)\EPSON\TMCOMUSB\TMVirtualPortDriver_User'sManual.pdf` 的 `手動設備設定 - USB` 設定指引，將偵測到的發票機指派至一個目前 **未被佔用** 的 COM Port（如 COM3 或 COM4）。

![type:video](../../assets/videos/POS-安裝-EPSON發票機軟體安裝設定01.mp4)


### 步驟四：校對紙張寬度設定

若發生發票文字跑版或裁切不全，請檢查此項設定。出貨時通常已預設完成，商家僅需在異常時進行確認。

1. 安裝 [TM-T82III Utility](https://download3.ebz.epson.net/dsc/f/03/00/15/59/89/e13530028b241ec0d281f763e894ce21988975cb/TM-T82IIIUtility111_e2.exe)。 [EPSON官方下載點](https://support.epson.net/setupnavi/?PINF=swlist&OSC=IOS&LG2=ZH&MKN=TM-T82III)。
2. 進入 **Basic Settings > Printing Control**。
3. 確認 **Paper width - Number of columns** 設定為 `58mm - 35 columns`。



### 步驟五：連線與測試列印

1. 回到 **CYBERBIZ POS 驅動程式**。
2. 在裝置清單中選擇已指派 COM Port 的 **EPSON 發票機**。
3. 點擊 **測試列印**，若成功印出測試明細，即代表安裝完成。

