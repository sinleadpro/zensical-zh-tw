---
title: 主頁
hide:
  - feedback
  - navigation
  - toc
---

<div style="display: flex; gap: 2rem; flex-wrap: wrap; padding: 3rem 0 2rem;" markdown>

<div style="flex: 1 1 380px; min-width: 0;" markdown>

<h1 style="margin-top: 0; font-size: 1.5rem;">
  輕鬆上手
  <span style="white-space: nowrap;">
    <span style="color: #03328e;">CYBERB</span>
    <span style="color: #ff7d00;">⋮</span>
    <span style="color: #03328e;">Z</span>
  </span>
</h1>

<p style="font-size: 0.95rem; line-height: 1.7;">
在這裡找到解答、探索功能，並精通 <strong>CYBERBIZ</strong> 平台。
我們隨時提供協助，讓您快速上手並善用每項工具。
</p>

[:lucide-arrow-right: 開始探索](ec/){ .md-button .md-button--primary }

</div>

<div style="flex: 1 1 380px; min-width: 0;">

<style>
[data-md-color-scheme="default"] {
  --callout-bg: #f2f6fc;
  --callout-hover: #FAFBFC;
  --badge-color: #6674c4;
  --text-color: #111;
  --divider-color: #e6e8ee;
  --border-color: #e6e8ee;
}
[data-md-color-scheme="slate"] {
  --callout-bg: #1e1e1e;
  --callout-hover: #2a2a2a;
  --badge-color: #6674c4;
  --text-color: #eee;
  --divider-color: #333;
  --border-color: #333;
}
.hero-callout {
  box-sizing: border-box;
  background-color: var(--callout-bg);
  border-radius: 12px;
  padding: 1rem 1.5rem;
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.tab-buttons {
  display: flex;
  gap: 0.5rem;
  border-bottom: 1px solid var(--divider-color);
  padding-bottom: 2px;
}
.tab-btn {
  flex: 1 1 auto;
  background: transparent;
  border: none;
  font-weight: 600;
  cursor: pointer;
  padding: 0.5rem 1rem;
  color: var(--text-color);
  position: relative;
  transition: color 0.2s;
}
.tab-btn:hover {
  color: var(--badge-color);
}
.tab-btn::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: transparent;
  transition: background 0.2s;
}
.tab-btn.active {
  color: var(--badge-color);
  font-weight: 700;
}
.tab-btn.active::after {
  background: var(--badge-color);
}
.tab-content {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
}
.tab-content a {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.3rem 0.5rem;
  font-size: 0.8rem;
  line-height: 1.4;
  color: var(--text-color);
  text-decoration: none;
  border-radius: 6px;
  transition: background 0.15s;
}
.tab-content a:hover {
  background-color: var(--callout-hover);
}
.badge {
  background-color: var(--badge-color);
  color: white;
  border-radius: 4px;
  font-size: 0.65rem;
  padding: 0.1rem 0.4rem;
  font-weight: 600;
  white-space: nowrap;
}
@media (max-width: 640px) {
  .hero-callout {
    padding: 0.75rem 1rem;
  }
  .tab-buttons {
    overflow-x: auto;
    flex-direction: row;
    flex-wrap: nowrap;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  .tab-buttons::-webkit-scrollbar {
    display: none;
  }
  .tab-btn {
    flex: 0 0 auto;
    white-space: nowrap;
    width: auto;
    text-align: center;
  }
  .tab-content a {
    padding: 0.5rem 0.5rem;
  }
}
</style>

<div class="hero-callout">

  <div role="tablist" class="tab-buttons">
    <button role="tab" aria-selected="true" class="tab-btn active"
      onclick="openTab(event, 'announcement')">最新公告</button>
    <button role="tab" aria-selected="false" class="tab-btn"
      onclick="openTab(event, 'latest')">最新文件</button>
    <button role="tab" aria-selected="false" class="tab-btn"
      onclick="openTab(event, 'popular')">熱門文章</button>
  </div>

  <div id="announcement" role="tabpanel" class="tab-content" style="display:flex">
    <a href="#"><span class="badge">重要</span>2026 年 6 月系統排程維護公告</a>
    <a href="#"><span class="badge">通知</span>CYBERBIZ 金流服務升級通知</a>
    <a href="#"><span class="badge">新功能</span>全通路庫存同步功能正式上線</a>
  </div>

  <div id="latest" role="tabpanel" class="tab-content">
    <a href="#"><span class="badge">新增</span>門市助理快速上手指南</a>
    <a href="#"><span class="badge">更新</span>EC 商品上架流程</a>
    <a href="#"><span class="badge">新增</span>全新金物流設定說明</a>
  </div>

  <div id="popular" role="tabpanel" class="tab-content">
    <a href="#"><span class="badge">FAQ</span>EC 付款流程 FAQ</a>
    <a href="#"><span class="badge">FAQ</span>商品管理常見問題整理</a>
    <a href="#"><span class="badge">指南</span>門市權限設定實務指南</a>
  </div>

</div>

<script>
function openTab(evt, tabName) {
  document.querySelectorAll('.tab-content').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('active');
    btn.setAttribute('aria-selected', 'false');
  });
  document.getElementById(tabName).style.display = 'flex';
  evt.currentTarget.classList.add('active');
  evt.currentTarget.setAttribute('aria-selected', 'true');
}
</script>

</div>

</div>


## :lucide-bot-message-square: AI 輔助檢索

<div class="grid cards" markdown>

-   :simple-notebooklm:{ .lg }
    __NotebookLM__

    ---

    使用 NotebookLM 檢索 CYBERBIZ 文件，進行 AI 輔助問答與分析。

    [:lucide-arrow-right: 開啟 NotebookLM](https://notebooklm.google.com/notebook/20277bb4-f8ae-4d7b-b2d9-3b8db845c761/preview){ target="_blank" }

-   :lucide-file-text:{ .lg }
    __LLM 可讀文件 (llms.txt)__

    ---

    針對大語言模型優化的 Markdown 格式，提升 RAG 檢索效率與上下文精準度。

    [:lucide-arrow-right: 標準版](llms.txt)

</div>

## :lucide-shopping-bag: 品牌官網

<div class="grid cards" markdown>

-   :lucide-rocket:{ .lg }
    __新手上路__

    ---

    從零開始建立您的品牌官網，快速掌握後台操作與基本設定。

    [:lucide-arrow-right: 開始使用](ec/)

-   :lucide-store:{ .lg }
    __商店設定__

    ---

    管理網站外觀、網域、SEO、發票與管理員權限。

    [:lucide-arrow-right: 前往設定](ec/website-management/)

-   :lucide-package:{ .lg }
    __商品管理__

    ---

    建立商品分類、上架商品、設定規格款式與銷售方式。

    [:lucide-arrow-right: 管理商品](ec/products/)

-   :lucide-truck:{ .lg }
    __訂單物流__

    ---

    處理訂單出貨、退貨退款、串接超商與宅配物流。

    [:lucide-arrow-right: 檢視訂單](ec/orders/)

-   :lucide-megaphone:{ .lg }
    __行銷活動__

    ---

    設定優惠活動、紅利商城、一頁式商店與互動遊戲。

    [:lucide-arrow-right: 建立活動](ec/marketing/)

-   :lucide-credit-card:{ .lg }
    __金流與物流__

    ---

    設定多元付款方式與配送方式，支援國內外金物流。

    [:lucide-arrow-right: 設定金物流](ec/payments-and-logistics/)

</div>

---

## :lucide-warehouse: 智慧倉儲

<div class="grid cards" markdown>

-   :lucide-log-in:{ .lg }
    __申請與開通__

    ---

    了解智慧倉儲的申請流程、開通設定與串倉規則。

    [:lucide-arrow-right: 了解詳情](wms/申請流程與開通.md)

-   :lucide-package:{ .lg }
    __商品管理__

    ---

    管理單一品項、加工商品與季節群組設定。

    [:lucide-arrow-right: 管理商品](wms/單一品項.md)

-   :lucide-arrow-right-left:{ .lg }
    __進出倉作業__

    ---

    建立進倉單、調倉單與退貨單，掌握庫存轉調流程。

    [:lucide-arrow-right: 檢視作業](wms/進倉單.md)

-   :lucide-bar-chart-3:{ .lg }
    __庫存管理__

    ---

    查詢庫存紀錄、操作紀錄與設定報表通知。

    [:lucide-arrow-right: 檢視庫存](wms/庫存紀錄.md)

</div>

---

## :material-point-of-sale: 智能 POS

<div class="grid cards" markdown>

-   :lucide-rocket:{ .lg }
    __開始使用__

    ---

    硬體安裝、軟體設定與快速上線指南。

    [:lucide-arrow-right: 開始使用](pos/get-started/)

-   :lucide-monitor:{ .lg }
    __硬體安裝__

    ---

    客顯螢幕、標籤印表機、發票機、刷卡機等設備設定。

    [:lucide-arrow-right: 安裝硬體](pos/hardware/)

-   :lucide-shopping-cart:{ .lg }
    __結帳功能__

    ---

    支援多種付款方式、離線結帳、訪客結帳與標籤列印。

    [:lucide-arrow-right: 了解結帳](pos/check/)

-   :lucide-bar-chart-3:{ .lg }
    __庫存管理__

    ---

    進出倉單、庫存調整、盤點作業與全通路庫存管理。

    [:lucide-arrow-right: 管理庫存](pos/inventory/)

</div>

---

## :lucide-grid-2x2-plus: CYBERBIZ 擴充功能

<div class="grid cards" markdown>

-   :lucide-layout-grid:{ .lg }
    __APP MARKET__

    ---

    擴充服務市集，探索更多功能與整合。

    [:lucide-arrow-right: 前往市集](ec/app-market/)

-   :lucide-cog:{ .lg }
    __自動化功能__

    ---

    自動化行銷、精準分眾，節省營運成本。

    [:lucide-arrow-right: 了解自動化](ec/app-market/automation/)

-   :lucide-ticket:{ .lg }
    __電子票券__

    ---

    線上購票、線下體驗，建立票券商品與設定。

    [:lucide-arrow-right: 設定票券](ec/e-ticket/設定指南.md)

-   :lucide-zap:{ .lg }
    __快速到貨__

    ---

    整合機車外送系統，提供即時配送服務。

    [:lucide-arrow-right: 了解詳情](#)

-   :lucide-credit-card:{ .lg }
    __金流支付__

    ---

    金物流一體的安全、多元支付方案。

    [:lucide-arrow-right: 檢視方案](ec/payments-and-logistics/)

-   :lucide-message-circle:{ .lg }
    __訊息通__

    ---

    全通路訊息一站整合，統一管理客服對話。

    [:lucide-arrow-right: 了解訊息通](ec/app-market/cyberbiz-extensions/chat-box/)

-   :lucide-link-2:{ .lg }
    __全通路管理助手__

    ---

    跨平台商品庫存整合，同步多通路銷售。

    [:lucide-arrow-right: 了解助手](ec/app-market/cyberbiz-channel-bridge/)

-   :lucide-shopping-cart:{ .lg }
    __門市助理__

    ---

    OMO 整合，串聯線上線下門市營運。

    [:lucide-arrow-right: 前往門市助理](storepal/)

-   :lucide-arrow-right-from-line:{ .lg }
    __代定__

    ---

    打通跨境商務的最後一哩，支援國際物流。

    [:lucide-arrow-right: 了解詳情](#)

</div>

---

## :lucide-newspaper: 最新消息

<div class="grid cards" markdown>

-   :lucide-megaphone: [__功能報報__](#)

    了解最新動態與實用技巧，請持續關注我們的部落格。

-   :lucide-history: [__更新紀錄__](resources/changelog/)

    關注我們的功能更新紀錄。

-   :lucide-messages-square: [__聯絡我們__](#)

    透過後台的線上客服與我們聯繫。

</div>
