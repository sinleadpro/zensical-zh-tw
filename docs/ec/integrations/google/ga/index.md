---
title: "Google Analytics"
description: "Google Analytics 4 (GA4) 完整教學，包含基礎串接設定與進階資料分析功能，協助商家追蹤網站流量與使用者行為。"
created: "2026-03-20 18:12"
last_modified: "2026-03-23 18:50"
lang: "zh-TW"
type: "guide"
status: ""
version: ""
author: "Jase"
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - "EC"
modules:
  - "第三方整合"
sites:
  - "TW"
audiences:
  - "admin"
difficulty: ""
tnb: "trunk"
plans:
  - "專業"
  - "進階"
  - "高手"
  - "專業 PLUS"
  - "進階 PLUS"
  - "高手 PLUS"
  - "企業"
cyb_extensions: []
intents:
  - "串接_GA4"
  - "流量分析"
  - "資料追蹤"
features:
  - "Google_Analytics_4"
  - "加強型評估"
  - "資料串流"
prerequisites: []
related:
  - "[[建立並串接 Google Analytics]]"
  - "[[設定 Google Analytics 進階追蹤與資料分析]]"
  - "[[設定 GA4 排除內部流量與第三方參照來源]]"
tags:
  - "GA4"
  - "Google Analytics"
  - "流量追蹤"
  - "數據分析"
  - "第三方整合"
acoiv: "configure"
apis: []
devices:
  - "desktop"
  - "mobile"
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "ga"
comments: false
search:
  exclude: false
icon: "lucide/chart-no-axes-column-increasing"
hide: []
---

# Google Analytics

Google Analytics 4 (GA4) 完整教學，包含基礎串接設定與進階資料分析功能，協助商家追蹤網站流量與使用者行為。
{ .subtitle }

{ .doc-badge }

{ .hero-page }


## 後續操作

<div class="grid cards" markdown>

- :lucide-link:{ .lg }   
  [__建立並串接 Google Analytics__](建立並串接 Google Analytics.md){ data-preview }     
  從零開始串接 GA4，包含 Google 端帳號建立與 CYBERBIZ 後台設定。

- :lucide-settings:{ .lg }     
  [__進階追蹤與資料分析__](設定 Google Analytics 進階追蹤與資料分析.md){ data-preview }  
  啟用加強型評估、Google 信號，調整資料保留期限。

- :lucide-funnel-x:{ .lg }     
  [__排除內部流量與參照連結__](設定 GA4 排除內部流量與第三方參照來源.md){ data-preview }  
  排除內部 IP 流量與第三方金物流網址，避免數據偏差。

</div>

## 常見問題

??? quote "為什麼需要使用 GA4 而非舊版 Universal Analytics？"

    Google 已於 2023 年 7 月正式停止 Universal Analytics (UA) 的資料收集，全面遷移至 GA4。GA4 採用嶄新的事件導向模型，能提供更靈活的追蹤與分析功能。

??? quote "GA4 與 CYBERBIZ 串接是否需要付費？"

    GA4 本身為免費工具，CYBERBIZ 後台亦提供免費的 GA4 串接功能，商家無需額外付費即可使用。

??? quote "如何驗證 GA4 是否成功串接？"

    可在商店前台執行任意操作（如加入購物車），再回到 GA4 後台查看「即時」報表是否有事件計數變化，即可確認串接是否成功。
