---
title: 排除未收到商家通知信件
description: 若 CYBERBIZ 寄出的訂單通知、系統公告等信件被誤歸類至「垃圾郵件」，本篇指南將協助您透過設定，確保能準時接收重要通知。
created: 2026-06-01 15:25
last_modified: 2026-06-01 15:25
lang: zh-TW
type: troubleshooting
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: []
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 解決收不到系統信問題
  - 設定 Gmail 篩選器
  - 避免信件進入垃圾桶
features: 
  - 系統通知信
  - Gmail 篩選器
prerequisites: []
related: []
tags: 
  - 通知信
  - 垃圾郵件
  - Gmail
  - 漏信排解
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - Gmail 設定
  - 篩選器
paths: 
  - Gmail > 設定 > 篩選器和封鎖的地址
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=4964
  - https://www.cyberbiz.io/support/?p=31664
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/mail-x
hide: []
---

# 排除未收到商家通知信件
若 CYBERBIZ 寄出的訂單通知、系統公告等信件被誤歸類至「垃圾郵件」，本篇指南將協助您透過設定，確保能準時接收重要通知。
{ .subtitle }

## 使用須知

- 此教學文件僅提供初步設定，詳情可參考 Google 官方文件 [在 Gmail 中回報垃圾郵件](https://support.google.com/mail/answer/1366858) 。


## 方法一：回報為非垃圾郵件

當您在「垃圾郵件」資料夾中發現來自 CYBERBIZ 的信件時，請執行以下操作：

1. 開啟該封信件。
2. 點擊上方的 **回報為非垃圾郵件** 按鈕。
3. 系統會將該信件移回收件匣，並協助 Gmail 學習該寄件者為安全來源。

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件08.jpg){ .screenshot }



## 方法二：設置 Gmail 篩選器（推薦）

透過建立篩選器，您可以強制系統 **永不** 將特定信箱的信件移至垃圾桶。

### 1. 進入 Gmail 設定

登入 Gmail 網頁版，點擊右上角的 **設定（齒輪圖示） > 查看所有設定**。

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件02.png){ .screenshot }

### 2. 建立新篩選器

切換至 **篩選器和封鎖的地址** 頁籤，點擊 **建立新篩選器**。

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件03.png){ .screenshot }

### 3. 填入寄件者清單

在 **寄件者** 欄位中，填入以下 CYBERBIZ 官方信箱：

（建議全部填入，信箱之間請用分號 `;` 分隔）

- **support@cyberbiz.io**
- **noreply@cyberbiz.co**
- **support@cyberbiz.co**

填寫完畢後，點擊 **建立篩選器**。

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件04.png){ .screenshot }

### 4. 設定排除條件

勾選以下三個關鍵選項，確保信件能正確呈現：

- **套用標籤**：選擇或新增一個標籤（如：CYBERBIZ），方便在左側選單統一查看。
- **永不移至垃圾桶**：這是最重要的設定，確保信件不會被攔截。
- **永遠將其標示為重要**：確保信件會出現在優先收件匣。

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件05.png){ .screenshot }

### 5. 前往篩選器

設定完畢後，可至 **篩選器和封鎖的地址**，查看所有篩選器。

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件06.png){ .screenshot }

至 **CYBERBIZ** 標籤收件夾查看篩選的所有信件。

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件07.png){ .screenshot }

