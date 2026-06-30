---
title: EPSON TM-M30III 發票機安裝教學 (Wi-Fi 連接)
description: 透過 Wi-Fi 無線連接方式安裝 EPSON TM-M30III 發票機，無須安裝驅動程式即可於平板設備使用。
created: 2026-05-27 12:20
last_modified: 2026-05-27 12:20
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結
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
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents: 
  - 安裝發票機
  - EPSON_TM-m30III_安裝
  - Wi-Fi_連接發票機
features: 
  - 發票機安裝
  - Wi-Fi_設定
prerequisites: []
related: 
  - "[[EPSON TM-T82III 發票機安裝教學]]"
tags: 
  - EPSON
  - 發票機
  - POS_硬體
  - TM-m30III
  - Wi-Fi
acoiv: activate
apis: []
devices: 
  - tablet
  - mobile
ui_components: 
  - 發票機
  - 進紙按鈕
paths: 
  - POS 功能 > 所有 POS 商店 > 修改 POS 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=53134
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/printer
hide: []
---

# EPSON TM-M30III 發票機安裝教學 (Wi-Fi 連接)
透過 Wi-Fi 無線連接方式安裝 EPSON TM-M30III 發票機，無須安裝驅動程式即可於平板設備使用。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 智能 POS
{ .doc-badge }


!!! tip "應用情境"
	- **無線櫃台環境**：櫃台空間有限，希望減少實線連接以保持整潔。
	- **行動結帳**：使用平板電腦在店內各處進行結帳並遠端列印發票。
	- **多設備共享**：多台平板設備共用同一台發票列印機。

---

## 使用須知

- **適用型號**：EPSON TM-M30III。
- **連接方式**：本教學採用 Wi-Fi 連接（無須驅動程式）。
    - 若需使用 USB 連接，則須安裝驅動程式，請參考 [EPSON TM-T82III 安裝教學](epson-tm-t82iii-invoice-printer.md)。
- **環境要求**：發票機與結帳平板須連接至同一個 Wi-Fi 網域。

## 操作流程

### 1. 硬體準備與開機

1. 打開上蓋，放入電子發票證明聯專用感熱紙捲。
2. 按壓 **電源鍵**，直到介面燈源閃爍完成開機。

### 2. 啟動 Wi-Fi 配對模式

1. 打開上蓋，按壓電源鍵下方的 **進紙按鈕** 約 3-5 秒。
2. 下方左側第三個訊號燈開始閃爍。
3. 將發票紙稍微拉出並蓋上上蓋，發票機會自動吐出一段紙張。

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用01-scaled.jpg){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用02-scaled.jpg){ .screenshot }

    </div>

### 3. 取得 Wi-Fi 設定 QR Code

1. 連續點擊 **進紙按鈕** 5 下，接著再點擊 1 下。
2. 發票機將吐出一張包含 **QR Code** 的設定紙。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用03-scaled.jpg){ .screenshot }

### 4. 執行 Wi-Fi 連線設定

1. 使用結帳平板掃描上述 QR Code。
2. 於平板上同意發票機加入目前的 Wi-Fi 網域。
3. 此時發票機會再吐出第二個 QR Code，請使用平板再掃描一次。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用04-scaled.jpg){ .screenshot }

4. 平板將出現 Wi-Fi 設定介面，點擊 **Wi-Fi**。
5. 找到步驟 3 取得的明細紙，將明細紙上 SSID 欄位 `DIRECT-TM-m30III-` 後方的英數字，填入平板介面的 **Current Password** 欄位。

    <div class="grid cards borderless two-columns" markdown>

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用05.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用07-scaled.jpg){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用06.png){ .screenshot }

    </div>

6. 於平板上輸入目前 Wi-Fi 的密碼，等待 Setup 完成。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用08.png){ .screenshot }

### 5. 取得 IP 位址並授權連線

1. 設定完成後，發票機會自動吐出一張包含 **IP 位址 (IP Address)** 的紙張。
2. 開啟平板瀏覽器，於網址列輸入該 IP 位址。
3. 若出現「您的連線不是私人連線」，請點擊 **進階**，再點擊 **繼續前往** 以允許連線。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用09-scaled.jpg){ .screenshot }

### 6. POS 前台連線測試

1. 使用相同瀏覽器登入 POS 前台。
2. 點擊 **進行連接**，輸入剛才取得的 IP 位址。
3. 點擊 **進行連接與測試**。若發票機吐出測試紙，即代表連線成功。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用10.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用11.png){ .screenshot }




