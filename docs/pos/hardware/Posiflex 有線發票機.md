---
title: Posiflex 有線發票機
description: 安裝 Posiflex 發票機，包含驅動程式安裝、硬體連線、發票樣式測試及常見故障排除方法。
created: 2026-03-25 18:45
last_modified: 2026-03-25 18:45
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: ["確認：是否支援星益欣、常見問題1驅動程式檔案連結是否有效"]
ga_views: 0
feedback: 0
products: [POS]
modules: ["所有 POS 商店"]
sites: [TW]
audiences: [admin, clerk]
difficulty: intermediate
tnb: branch
plans: [進階 PLUS, 高手 PLUS, 企業]
cyb_extensions: []
intents: ["如何安裝Posiflex發票機", "發票機連線失敗排解", "發票印出來是空白怎麼辦", "發票機隔板安裝教學"]
features: ["發票機串接", "自動開立發票", "盟立加值中心整合", "硬體連線診斷"]
prerequisites: []
related: []
tags: ["Posiflex", "發票機", "盟立發票", "POS_硬體", "電子發票"]
acoiv: configure
apis: []
devices: [desktop]
ui_components: ["POS 驅動程式", "熱感應發票機", "快速測試", "自動開立發票"]
paths: ["POS 功能 > 所有 POS 商店 > 修改 POS 設定"]
layouts: []
wp_url: ["https://www.cyberbiz.io/support/?p=4225", "https://www.cyberbiz.io/support/?p=5064"]
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/file-text
hide: []
---

# Posiflex 有線發票機
安裝 Posiflex 發票機，包含驅動程式安裝、硬體連線、發票樣式測試及常見故障排除方法。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 進階 PLUS / 高手 PLUS / 企業
{ .doc-badge }


## 使用須知

- **系統限制**：系統僅支援 Posiflex 系列與盟立配合之發票機型號。
- **金鑰前提**：安裝前請確認已將 **盟立通道金鑰** 提供給 CYBERBIZ 客服人員。
- **軟體環境**：必須維持 CYBERBIZ POS 驅動程式開啟，**請勿關閉視窗**（可最小化）。
- **硬體時間**：發票開立時間將以商家 **POS 電腦硬體顯示時間** 為準，請確保電腦時區與時間正確。



## 操作流程

### 步驟一：安裝驅動程式與硬體整備

1. **安裝程式**：前往下載並安裝 [CYBERBIZ POS 驅動程式]()。
    ![](../../assets/images/POS-驅動程式-桌面圖示01.png)
2. **安裝紙捲**：將感熱紙捲放入機槽（感應面朝上）。

     <div class="grid cards borderless two-columns" markdown>

    - ![安裝紙捲01](../../assets/images/POS-安裝-Posiflex有線發票機-裝紙捲01.jpg){ title="安裝紙捲01" }
    - ![安裝紙捲02](../../assets/images/POS-安裝-Posiflex有線發票機-裝紙捲02.jpg){ title="安裝紙捲02" }
    - ![安裝紙捲03](../../assets/images/POS-安裝-Posiflex有線發票機-裝紙捲03.jpg){ title="安裝紙捲03" }

    </div>

    - **注意**：若使用 **PP-8800** 機型，必須安裝隨機附贈的「隔板」，以固定 58mm 規格的發票感熱紙。

    <div class="grid cards borderless two-columns" markdown>

    - ![安裝紙捲01](../../assets/images/POS-安裝-Posiflex有線發票機-裝隔板01.png){ title="安裝隔板01" }
    - ![安裝紙捲02](../../assets/images/POS-安裝-Posiflex有線發票機-裝隔板02.png){ title="安裝隔板02" }
    - ![安裝紙捲02](../../assets/images/POS-安裝-Posiflex有線發票機-裝隔板03.png){ title="安裝隔板03" }

    </div>

3. **開啟電源**：將發票機接上電源並開啟開關。
    ![](../../assets/images/POS-安裝-Posiflex有線發票機-開機01.jpg){ .screenshot }

### 步驟二：系統連線與綁定

1. **USB 連線**：將發票機透過 USB 線與電腦連接。
    ![](../../assets/images/POS-安裝-Posiflex有線發票機-啟用01.png){ .screenshot }
2. **啟動驅動程式**：開啟 CYBERBIZ 驅動程式，系統應自動偵測到裝置。
3. **選擇機型**：在程式介面中點選 **熱感應發票機**。

    <div class="grid cards borderless two-columns" markdown>

    - ![系統連線01](../../assets/images/POS-驅動程式-連線有線發票機01.jpg){ title="系統連線01" }
    - ![系統連線02](../../assets/images/POS-驅動程式-連線有線發票機03.png){ title="系統連線02" }

    </div>

4. **刷新前台**：若顯示「尚未綁定 POS 店」，請開啟或刷新瀏覽器中的 **POS 前台網頁**，並保持驅動程式開啟。
    ![](../../assets/images/POS-驅動程式-連線有線發票機02.png){ .screenshot }

### 步驟三：連線與列印測試

1. **快速測試**：在驅動程式視窗 **點此** 快速測試，發票機應印出一小張測試明細。

    <div class="grid cards borderless two-columns" markdown>

    - ![測試01](../../assets/images/POS-驅動程式-有線發票機-列印測試01.png){ title="測試01" }
    - ![測試02](../../assets/images/POS-驅動程式-有線發票機-列印測試02.png){ title="測試02" }
    - ![測試03](../../assets/images/POS-安裝-Posiflex有線發票機-測試01.jpg){ title="測試03" }

    </div>

2. **真實交易測試**：
    - 進入 POS 前台進行一筆小額結帳。
    - 發票類型若 **僅顯示「自行開立」**，而沒有「紙本電子發票」、「公司統編」等其他選項，代表 **串接尚未生效**；請聯繫 CYBERBIZ 技術客服客服支援。
    ![](../../assets/images/POS-前台-結帳-開立發票選項01.png){ .screenshot }

3. **列印發票**：完成結帳，檢查發票機是否順利列印發票。
    ![](../../assets/images/POS-安裝-Posiflex有線發票機-測試02.jpg){ .screenshot }
4. **取消訂單**：取消訂單後，應可於前台 **訂單** 頁看到發票已成功註銷。

    <div class="grid cards borderless two-columns" markdown>

    - ![取消訂單01](../../assets/images/POS-前台-結帳-有線發票機取消測試訂單01.png){ title="取消訂單01" }
    - ![取消訂單02](../../assets/images/POS-前台-結帳-有線發票機取消測試訂單02.png){ title="取消訂單02" }
    - ![取消訂單03](../../assets/images/POS-前台-結帳-有線發票機取消測試訂單03.png){ title="取消訂單03" }

    </div>

### 步驟四：開立發票設定

前往 **POS 功能 > 所有 POS 商店**，選擇指定商店，點擊 **修改 POS 設定**，完成出單偏好配置。

![](../../assets/images/POS-後台-所有POS商店-修改POS子機設定01.png){ .screenshot }

- 自動開立發票：系統於結帳完成自動產生電子發票號碼，並向財政部上傳交易資料
- 自動列印發票：系統連動發票機自動產出紙本發票
- 自動列印明細：開啟後將自動列印交易明細表

![](../../assets/images/POS-後台-所有POS商店-修改POS子機發票設定01.png){ .screenshot }

## 紙捲與耗材資訊

若您從 CYBERBIZ 購買發票機，機器內附兩捲測試紙。後續請購買以下規格：

- **規格**：70m 公版感熱紙捲
- **寬度**：5.7cm (58mm)
- **添購路徑**：可至 [財政部電子發票感熱紙平台](https://invoice.ppmof.gov.tw/PSJ_Web/) 或一般辦公用品店採購。

![](../../assets/images/POS-裝置-有線發票機紙捲01.png){ .screenshot }

## 常見問題

??? quote "為什麼驅動程式顯示「已註冊裝置為 0，1個問題待修正」？"
    ![](../../assets/images/POS-驅動程式-疑難排解1-1.png){ .screenshot }

    這代表電腦尚未正確識別發票機。請嘗試以下步驟：

    1. [下載並安裝驅動程式](https://drive.google.com/file/d/1_5E8MAY8fAAy5HDjuuX8cQ2hEcZBfiKQ/view?usp=sharing)。

    2. 進入 **電腦 > 管理**。
        ![](../../assets/images/POS-驅動程式-疑難排解1-2.png){ .screenshot }
    
    3. 於 **裝置管理員** 尋找「其他裝置」中帶有驚嘆號的項目。
        ![](../../assets/images/POS-驅動程式-疑難排解1-3.png){ .screenshot }
        
    4. 點擊右鍵選擇 **更新驅動程式**。
        ![](../../assets/images/POS-驅動程式-疑難排解1-4.png){ .screenshot }
    
    5. 點擊 **瀏覽電腦上的驅動程式軟體**。
        ![](../../assets/images/POS-驅動程式-疑難排解1-5.png){ .screenshot }

    6. 於瀏覽資料夾中選擇 **USBVCOM_Win_x64** 資料夾。
        ![](../../assets/images/POS-驅動程式-疑難排解1-7.png){ .screenshot }
    7. 點擊 **安裝**。
        ![](../../assets/images/POS-驅動程式-疑難排解1-8.png){ .screenshot }
    8. 排解成功後，裝置將不再帶有驚嘆號標誌。
        ![](../../assets/images/POS-驅動程式-疑難排解1-9.png){ .screenshot }

??? quote "顯示「安裝驅動程式軟體時發生錯誤」，該如何排解？"
    ![](../../assets/images/POS-驅動程式-疑難排解2-1.png){ .screenshot }

    1. [下載並安裝程式檔案](https://drive.google.com/file/d/1x1BPZeFaaAa8VjW3_pTiAqXP4OYCdE07/view)。

    2. 完成安裝後，點擊 **立即重新啟動**。
        ![](../../assets/images/POS-驅動程式-疑難排解2-2.png){ .screenshot }

    3. 進入 **電腦 > 管理**。
        ![](../../assets/images/POS-驅動程式-疑難排解2-3.png){ .screenshot }

    4. 於 **裝置管理員** 查看發票機裝置是否順利連接。
        ![](../../assets/images/POS-驅動程式-疑難排解2-4.png){ .screenshot }

    5. 裝置不帶有驚嘆號符號，表示有連接上裝置。
        ![](../../assets/images/POS-驅動程式-疑難排解2-5.png){ .screenshot }

??? quote "插入 USB 至 POS 主機後，卻找不到裝置？"
    請依照自身發票機型號選擇設置操作：

    === "型號 8800"
        開啟機器底部，調整 Jumper 設置，確認 Dip Switch 1、2、4、6 皆為 on，並重新開機。
        ![](../../assets/images/POS-驅動程式-疑難排解3-1.png){ .screenshot }

    === "型號 8802"
        此機型沒有實體開關，請下載軟體，並透過軟體進行檢查與調整。

        1. [下載軟體](https://drive.google.com/file/d/11OFommtgJWqYcZFmGWaQT4373BsJC9sO/view?usp=sharing)。
        2. 解壓縮檔案，於資料夾點選 Setup 應用程式檔案，完成安裝。
            ![](../../assets/images/POS-驅動程式-疑難排解3-2.png){ .screenshot }
        3. 安裝完成後，電腦桌面會新增以下捷徑。
            ![](../../assets/images/POS-驅動程式-疑難排解3-3.png){ .screenshot }
        4. 點擊捷徑，開啟軟體，檢查是否顯示以下畫面，若呈現畫面與下圖不符，請洽 CYBERBIZ 客服。
            ![](../../assets/images/POS-驅動程式-疑難排解3-4.png){ .screenshot }

??? quote "已完成所有基礎檢查，但硬體（發票機/刷卡機）仍無法成功串接怎麼辦？"
    1. **強制重啟驅動程式**：徹底關閉電腦工作列中的 **POS APP 驅動程式**，並重新執行程式。
    2. **重新觸發硬體偵測**：將設備的 **USB 傳輸線** 由電腦端拔除，等待 5 秒後重新插入。
    3. **執行系統重置 (Reset)**：
        - 在 **POS APP 驅動程式** 介面中，點擊 **重置 (Reset)** 按鈕。
        - 執行重置後，請重複上述步驟 1 與 2。
    4. **關鍵確認**：觀察驅動程式介面，確認是否有出現正確的裝置名稱或連線成功的綠色燈號。


??? quote "當系統出現「請先嘗試重開系統和裝置」警示，該如何處理？"
    ![](../../assets/images/POS-驅動程式-疑難排解5-1.jpg){ .screenshot }
    這類狀況通常源於 **硬體連線異常** 或 **驅動程式掛載失敗**，請依序執行以下初步排除步驟：

    1. 硬體實體檢查
        - 確認發票機（或刷卡機）的 **USB 傳輸線** 是否鬆脫，建議重新拔插。
        - 確認設備電源已開啟，且紙捲充足（無紅燈警示）。
    2. 重啟核心程式
        - 關閉並重新啟動電腦上的 **POS APP 驅動程式**。
        - 重新整理 POS 前台網頁。
    3. 重啟裝置
        - 若上述無效，請將電腦主機與發票機 **重新啟動**，通常可解決 90% 的暫時性連線衝突。

    !!! info "溫馨提醒"
        若完成上述「重開與拔插」動作後仍持續出現警示，可能是設備參數異動或硬體故障，請聯繫 **CYBERBIZ 客服人員** 協助排查。


??? quote "POS有發票號碼，EC訂單中卻無發票串聯紀錄？"
    結帳時若未選到 **自行開立**，後來才補輸入手開發票號碼，因此發票 **未標記** 為手動開立，則 EC 訂單無法串連及顯示。

??? quote "為什麼發票印出來是空白的？"
    通常是感熱紙捲 **放反了**。請確認紙捲拉出的方向是否能讓列印頭接觸到感熱面（通常是紙張較光滑的一面朝上）。
    ![](../../assets/images/POS-驅動程式-疑難排解4-1.png){ .screenshot }

??? quote "發票機發出異常噪音怎麼辦？"
    請檢查紙捲是否擺放平整，或是機蓋未完全扣緊。重新放置紙捲並用力壓下機蓋直至聽到「喀」聲即可解決。

    [發票機異音範例](https://drive.google.com/file/d/12Cnb5YsTSt5HSYQBYukbcjOugdm4QGQ4/view?usp=sharing)