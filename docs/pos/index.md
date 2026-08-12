---
description: "CYBERBIZ 智能 POS 產品中心，提供硬體安裝、結帳功能與庫存管理等操作說明。"
author: ""
reviewers: []
products: [POS]
notes: []
title: 智能 POS 產品中心
lang: zh-TW
hide:
  - description
  - path
  - toc
  - feedback
permalink: "https://help.cyberbiz.io/pos/"
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
      智能 
      <span style="white-space: nowrap;">
        <span style="color: #03328e; font-size: 1.2em;">POS</span>
      </span>
    </h1>

    <p>
      <big><strong>一站式全通路零售管理解決方案</strong></big><br>
      從基礎收銀到全通路會員整合，提供您最完整的一站式零售解決方案。<br>
      協助商家累積會員資產並精準行銷，讓線上線下經營從此無縫銜接。
    </p>

    <div class="custom-button-group" style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1rem;
    ">
      <a href="get-started/index.md" class="md-button md-button--primary">新手上路 ➜</a>
      <a href="hardware/index.md" class="md-button">硬體安裝</a>
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
      <a href="hardware/epson-tm-m30iii-invoice-printer.md"><span class="badge">新增</span>EPSON TM-M30III 發票機安裝教學 (Wi-Fi 連接)</a>
      <a href="others/daily-closing.md"><span class="badge">更新</span>小結關帳可列印紙本帳條</a>
	  <a href="../ec/marketing/coupon/multiple-coupons.md"><span class="badge">新增</span>POS 多優惠券結帳功能</a>
    </div>

    <!-- Popular -->
    <div id="popular" role="tabpanel" class="tab-content">
      <a href="software/drivers.md"><span class="badge">更新</span>安裝驅動程式</a>
      <a href="store/renewal-and-add-on-plans.md"><span class="badge">更新</span>續購與加購方案</a>
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

-   :lucide-credit-card: __流暢結帳__
    
    ---
    支援多種支付方式與電子發票開立

    [:octicons-arrow-right-24: 建立支付工具](check/payment-method/index.md)<br>
    [:octicons-arrow-right-24: 盟立電子發票](third-party/monolith-e-invoice.md)<br>
    [:octicons-arrow-right-24: 星益欣電子發票](third-party/wixtar-e-invoice.md)<br>


-   :lucide-package-check: __精準庫存__
    
    ---
    即時掌握門市與電商全通路庫存
    
    [:octicons-arrow-right-24: 庫存管理](inventory/index.md)

-   :lucide-users: __會員經營__
    
    ---
    整合紅利商城、客顯互動遊戲與線下分潤
    
    [:octicons-arrow-right-24: 紅利商城](check/bonus-point-mall.md)<br>
    [:octicons-arrow-right-24: 客顯互動遊戲](check/customer-display-interactive-games.md)<br>
    [:octicons-arrow-right-24: 推薦人分潤](../ec/profit-sharing/referrer-profit-sharing.md)<br>
    [:octicons-arrow-right-24: 註冊人分潤](../ec/profit-sharing/registrant-profit-sharing.md)<br>
    [:octicons-arrow-right-24: 門市取貨店員分潤](store/pos-store-pickup-staff-commission.md)

-   :lucide-bar-chart-3: __營運分析__
    
    ---
    多維度報表助您掌握銷售脈絡
    
    [:octicons-arrow-right-24: 報表分析](store/business-intelligence/pos-revenue-analysis/)

</div>

---

## 核心營運場景

<div class="grid" markdown>
 
<div>
<br>  
<big><strong>櫃檯營運一站式流程</strong></big><br>
確保您的收銀台運作無虞。包含刷卡機、發票機安裝，以及離線結帳、子機綁定等進階功能說明。 
<br><br>

<a href="check/index.md" class="md-button md-button--primary">查看結帳功能全指南 ➜</a>
</div>


![](../assets/images/POS-前台-結帳-付款方式01.png)

</div>

---

## 依角色探索

<div class="grid cards" markdown>

-   :lucide-user: __門市店員__
    
    ---
    專注於日常銷售與顧客服務
    
    [:octicons-arrow-right-24: 前台人員登入](store/staff-login.md)<br>
    [:octicons-arrow-right-24: 一般訂單管理](orders/manage-general-orders.md)<br>
    [:octicons-arrow-right-24: 建立前台商品選單](check/pos-frontend-menu-settings.md)<br>
    [:octicons-arrow-right-24: 磅秤商品結帳](others/scale-settings.md)


-   :lucide-user-cog: __店長與管理者__
    
    ---
    專注於門市效能與資源調度
    
    [:octicons-arrow-right-24: 員工權限管理](store/staff-permissions-and-account-management.md)<br>
    [:octicons-arrow-right-24: 建立公告](store/announcement-system.md)<br>
    [:octicons-arrow-right-24: 安全性與系統設定](store/pos-security-settings.md)<b>

</div>
