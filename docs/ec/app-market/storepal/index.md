---
title: 門市助理
description: 專為線下門市設計的 OMO 銷售工具，整合官網會員數據與資產，協助店員實現精準識客、深度洞察與價值變現。
created: 2026-05-05 11:20
last_modified: 2026-05-28 14:48
lang: zh-TW
type: guide
status: ""
version: 1.0.0
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 門市助理
sites:
  - TW
audiences:
  - clerk
  - admin
difficulty: beginner
tnb: trunk
plans:
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents:
  - 了解門市助理功能
  - 開始使用門市助理
  - 導覽門市助理介面
features:
  - 門市助理
  - OMO 銷售
  - 會員數據
  - 資產核銷
prerequisites: []
related: []
tags:
  - 門市助理
  - OMO
  - 精準銷售
  - 導覽
acoiv: activate
apis: []
devices:
  - tablet
  - mobile
ui_components: []
paths:
  - APP MARKET > 我的擴充服務 > 門市助理
layouts:
  - classic
wp_url: []
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/users
hide: []
---

# 門市助理
專為線下門市設計的 OMO 銷售工具，整合官網會員數據與資產，協助店員實現精準識客、深度洞察與價值變現。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
{ .doc-badge }

門市助理是連接線下門市與線上官網的核心橋樑。透過平板或手機，門市人員可以即時調取會員在全通路的消費軌跡與優惠資產，將「過路客」轉化為「品牌鐵粉」，並透過導購連結確保每一筆努力都能獲得業績歸因。

---

## 介面切割導覽 (Interface Overview)

門市助理的前台介面設計遵循「由淺入深、由左至右」的銷售邏輯，分為三個核心操作區域：

```mermaid
graph LR
    subgraph ClerkUI [門市助理前台介面]
        direction LR
        Mod1["<b>左側/頂端：精準識客</b><br/>(身份識別、標籤標註)"]
        Mod2["<b>中段：深度洞察</b><br/>(等級權益、消費分析、註記)"]
        Mod3["<b>右側：價值變現</b><br/>(核銷、推薦商品、手動紀錄)"]
        
        Mod1 --> Mod2
        Mod2 --> Mod3
    end
```

1.  **精準識客 (左側/頂端)**：用於快速確認顧客是誰、有哪些特徵標籤。
2.  **深度洞察 (中段)**：提供數據支持，了解顧客的購買力、偏好以及目前擁有的權益。
3.  **價值變現 (右側)**：執行最終的成交動作，包含資產核銷、生成推薦連結或紀錄線下消費。

---

## 教學文件導覽

請根據您的操作需求，選擇對應的教學章節：

### 基礎建置與入會

<div class="grid cards" markdown>

- :lucide-user-plus:{ .lg }
  __註冊與綁定門市會員__
  引導顧客掃碼入會，並建立門市人員與顧客的推薦綁定關係。<br>
  [查看文件](搜尋與建立會員.md)

</div>

### 會員經營與數據應用

<div class="grid cards" markdown>

- :lucide-search:{ .lg }
  __01. 精準識客__
  身份識別與標籤應用。快速確認 VIP 等級，掌握顧客特徵。<br>
  [查看文件](會員身份識別.md)

- :lucide-bar-chart-3:{ .lg }
  __02. 數據洞察__
  消費概況與權益分析。分析歷史訂單與購物車，發掘潛在需求。<br>
  [查看文件](會員數據智庫.md)

- :lucide-shopping-cart:{ .lg }
  __03. 成交引導__
  資產核銷與商品推薦。執行點數/優惠券折抵，生成導購連結。<br>
  [查看文件](導購轉化.md)

</div>

### 績效追蹤與報表

<div class="grid cards" markdown>

- :lucide-file-text:{ .lg }
  __查看門市與個人業績報表__
  追蹤導購業績、線下消費紀錄與個人績效達成狀況。<br>
  [查看文件](查看業績.md)

</div>

---

!!! info "下一步建議"
    如果您是第一次使用，建議先閱讀 [搜尋與建立會員](搜尋與建立會員.md)，了解如何將顧客帶入您的 OMO 體系。
