---
description: "CYBERBIZ 智慧倉儲(WMS) 產品中心，提供申請開通、商品管理、進出倉作業與庫存管理說明。"
author: ""
reviewers: []
products: [WMS]
notes: []
title: 智慧倉儲 (WMS) 產品中心
lang: zh-TW
permalink: "https://help.cyberbiz.io/wms/"
hide:
  - description
  - path
  - toc
  - feedback
---

<div class="hero-wrapper" style="
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 2rem;
    flex-wrap: wrap;
    margin-top: -2.2rem;
    padding: 4rem 0rem;
">

  <!-- LEFT: Hero -->
  <div class="homepage-hero" style="
      flex: 1 1 380px;
      min-width: 360px;
      max-width: 680px;
  ">
    <h1>
      智慧 
      <span style="white-space: nowrap;">
        <span style="color: #03328e; font-size: 1.2em;">倉儲</span>
      </span>
    </h1>

    <p>
      <big><strong>專業的電商倉儲管理解決方案</strong></big><br>
      從入倉儲存到系統化出貨與退貨管理，為您打通物流最後一哩路，讓您專注品牌經營。
    </p>

    <div class="custom-button-group" style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1rem;
    ">
      <a href="merchant-inbound-operation-rules.md" class="md-button md-button--primary">商家進倉作業規範 ➜</a>
      <a href="application-process-and-activation.md" class="md-button">官網串倉整合指南</a>
    </div>
  </div>

  <!-- RIGHT: POS Callout -->
  <style>
	/* Light/Dark mode colors */
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
	
	/* Container */
	.hero-callout {
	  background-color: var(--callout-bg);
	  border-radius: 12px;
	  padding: 1rem 1.5rem;
	  border: 1px solid var(--border-color);
	  display: flex;
	  flex-direction: column;
	  gap: 1rem;
	  flex: 1 1 380px;
	  min-width: 360px;
	  max-width: 680px;
	}
	
	/* Tabs */
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
	
	/* Content list */
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
	
	/* Badge */
	.badge {
	  background-color: var(--badge-color);
	  color: white;
	  border-radius: 4px;
	  font-size: 0.65rem;
	  padding: 0.1rem 0.4rem;
	  font-weight: 600;
	  white-space: nowrap;
	}
	
	/* Mobile */
	@media (max-width: 640px) {
	  .tab-buttons {
	    flex-direction: column;
	  }
	  .tab-btn {
	    width: 100%;
	    text-align: center;
	  }
	}
  </style>

  <div class="hero-callout">
    <!-- Tabs -->
    <div role="tablist" class="tab-buttons">
      <button role="tab" aria-selected="true" class="tab-btn active"
        onclick="openTab(event, 'latest')">最新文件</button>
      <button role="tab" aria-selected="false" class="tab-btn"
        onclick="openTab(event, 'popular')">熱門文章</button>
    </div>

    <!-- Latest -->
    <div id="latest" role="tabpanel" class="tab-content" style="display:flex">
      <a href="processed-products.md"><span class="badge">更新</span>加工商品</a>
	  <a href="duplicate-order.md"><span class="badge">新增</span>複製訂單</a>
    </div>

    <!-- Popular -->
    <div id="popular" role="tabpanel" class="tab-content">
      <a href="returns-and-vehicle-dispatch.md"><span class="badge">更新</span>退貨與派車</a>
    </div>
  </div>

  <script>
    function openTab(evt, tabName) {
      document.querySelectorAll('.tab-content')
        .forEach(el => el.style.display = 'none');
    
      document.querySelectorAll('.tab-btn')
        .forEach(btn => {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
        });
    
      document.getElementById(tabName).style.display = 'flex';
      evt.currentTarget.classList.add('active');
      evt.currentTarget.setAttribute('aria-selected', 'true');
    }
  </script>

</div>

---

## 核心功能概覽

<div class="grid cards" markdown>

-   :lucide-package: __商品管理__
    
    ---
    支援單一品項、加工商品與季別群組管理
    
    [:octicons-arrow-right-24: 單一品項](single-items.md)<br>
    [:octicons-arrow-right-24: 加工商品](processed-products.md)

-   :lucide-arrow-right-left: __倉儲作業__
    
    ---
    完整的進倉、出倉與調倉單據流程
    
    [:octicons-arrow-right-24: 進倉管理](inbound-orders.md)<br>
    [:octicons-arrow-right-24: 調倉作業](transfer-orders.md)

-   :lucide-shopping-cart: __訂單處理__
    
    ---
    自動同步官網訂單，支援手動建單與 POD 追蹤
    
    [:octicons-arrow-right-24: 訂單列表](list.md)<br>
    [:octicons-arrow-right-24: 手動建單](manual-order-creation.md)

-   :lucide-settings: __系統設定__
    
    ---
    商店資訊、帳號權限與報表通知設定
    
    [:octicons-arrow-right-24: 權限設定](permission-settings.md)<br>
    [:octicons-arrow-right-24: 商店設定](store-settings.md)

</div>

---

## 核心營運場景

<div class="grid" markdown>

<div>
<big><strong>官網與倉儲自動化同步</strong></big><br>
實現庫存即時同步、自動拆單或混單處理。確保官網訂單能準確且快速地傳遞至倉儲系統進行出貨。
<br><br>


<a href="site-and-warehouse-sync-rules.md" class="md-button md-button--primary">官網與倉儲同步規則 ➜</a><br><br>
<a href="enable-partial-warehouse-integration-and-order-splitting.md" class="md-button">啟用部分串倉與拆單 ➜</a>&nbsp;&nbsp;
<a href="enable-partial-warehouse-integration-and-mixed-orders.md" class="md-button">啟用部分串倉與混單 ➜</a>
</div>

![](../assets/images/EC-後台-金物流-宅配物流-拆單畫面總覽01.png)

</div>

---

## 依角色探索

<div class="grid cards" markdown>

-   :lucide-user: __倉管人員__
    
    ---
    專注於現場作業與庫存異動
    
    [:octicons-arrow-right-24: 建立進倉單](inbound-orders.md)<br>
    [:octicons-arrow-right-24: 建立退貨單](return-orders.md)<br>
    [:octicons-arrow-right-24: 庫存紀錄查詢](inventory-records.md)

-   :lucide-user-cog: __營運管理者__
    
    ---
    專注於系統整合與數據監控
    
    [:octicons-arrow-right-24: 員工帳號建置](account-management.md)<br>
    [:octicons-arrow-right-24: 操作紀錄列表](operation-logs.md)<br>
    [:octicons-arrow-right-24: 報表通知設定](report-notification-settings.md)

</div>
