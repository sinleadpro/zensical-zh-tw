---
title: 排程跑馬燈對照表
description: "說明排程跑馬燈版位的檔期狀態(預設、已上架、未上架、已下架)，由系統依目前時間自動判定。"
created: 2026-06-10 15:45
last_modified: 2026-06-10 15:49
lang: zh-TW
type: reference
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans:
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-appearance/references/scheduled-carousel-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


### 廣告檔期狀態對照表 { #reference-scheduled-carousel-statuses }

| 狀態 | 說明 |
| :-- | :-- |
| 預設 | 版位的常駐圖片，當該版位沒有其他正在上架的排程檔期時顯示。 |
| 已上架 | 目前前台正在顯示的排程檔期(已到開始時間、尚未過結束時間)。 |
| 未上架 | 已建立但尚未到達開始時間的排程檔期，時間到後會自動上架。 |
| 已下架 | 已過結束時間、排程結束的檔期，可隨時重新調整時間再次上架。 |

!!! note "註釋"
    * 狀態由系統依「目前時間」與檔期的開始／結束時間自動判定，無須手動切換。
    * 「預設」圖片不受時間限制，與其他排程檔期可並存於同一版位。
