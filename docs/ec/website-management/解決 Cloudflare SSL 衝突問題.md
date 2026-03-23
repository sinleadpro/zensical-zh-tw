---
title: "解決 Cloudflare SSL 衝突問題"
version: "1.1.1"
last_modified: "2026-03-10"
description: "Cloudflare 是全球知名的 DNS 代管與 CDN 加速服務商。若您的網域代管於 Cloudflare，在將網址指向 CYBERBIZ 時，必須針對 Proxy 功能進行特定設定，以確保網站能順利載入並正確套用 SSL 安全憑證。"
product:
  - EC
module: "管理中心"
activ: "Configure"
paths: "管理中心 > 網域管理"
surfaces: "Cloudflare DNS 管理頁面"
ends:
  - backend
  - frontend
devices:
  - desktop
apis: ""
type: troubleshooting
features: 
  - "SSL 憑證"
  - "網域管理"
  - "DNS 設定"
tasks: 
  - "關閉 Cloudflare Proxy"
  - "設定 CNAME 紀錄"
tnb: "trunk"
plans: ""
prerequisites: 
  - "需具備 Cloudflare 帳戶管理權限"
  - "網域已完成 Cloudflare 代管設定"
lang: zh-TW
sites: "TW"
status: ""
tags: 
  - "疑難排解"
  - "DNS"
  - "SSL"
difficulty: ""
audiences: ""
wp_url: "https://www.cyberbiz.io/support/?p=28727"
notes: ""
comments: ""
search: 
  exclude: ""
icon: ""
---

# 解決 Cloudflare SSL 衝突問題
Cloudflare 是全球知名的 DNS 代管與 CDN 加速服務商。若您的網域代管於 Cloudflare，在將網址指向 CYBERBIZ 時，必須針對 Proxy 功能進行特定設定，以確保網站能順利載入並正確套用 SSL 安全憑證。
{ .subtitle }


## 使用須知

- **避免 SSL 衝突**：CYBERBIZ 系統已為所有商家網站內建並自動維護 SSL 安全憑證。若 Cloudflare 的「Proxy (橘色雲朵)」功能開啟，將會導致 Cloudflare 的證書與 CYBERBIZ 的證書產生衝突，常見現象包含：**網站顯示 521 錯誤、產生無限重新導向循環、或網頁完全無法進入。**
- **第三方系統更新**： Cloudflare 介面可能隨時間更新。本指引所提及之按鈕名稱與路徑（如：DNS 記錄、Proxy 狀態）若與實際畫面略有出入，請依 Cloudflare 官方最新文件為準。CYBERBIZ 主要提供系統串接與網域指向服務，若因第三方平台介面更新導致操作流程變動，恕 CYBERBIZ 無比照同步更新教學之義務，網域商端的細部操作建議優先諮詢該平台客服。


## 關閉 Cloudflare Proxy 功能

為了讓網域正確指向 CYBERBIZ 並穩定運行，請依照以下步驟調整 DNS 設定：

### 1. 進入 DNS 管理頁面

1. 登入您的 **Cloudflare 管理後台**。
2. 選擇您要設定的 **網域**。
3. 在左側選單中點擊 **DNS > 記錄 (Records)**。

### 2. 修改 CNAME 記錄

1. 在記錄列表中找到指向 CYBERBIZ 的 **CNAME 記錄**（例如名稱為 `www` 的記錄）。
2. 點擊該記錄右側的 **編輯 (Edit)**。
3. 找到 **Proxy 狀態 (Proxy status)** 欄位。
4. 將開關切換為 **僅限 DNS (DNS only)**。
    - 此時圖示應由「橘色雲朵」變更為「**灰色雲朵**」。
5. 點擊 **儲存**。



