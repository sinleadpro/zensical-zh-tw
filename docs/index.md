---
title: 主頁
hide:
  - feedback
  - navigation
  - toc
  - feedback
search:
  exclude: true
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
      輕鬆上手 
      <span style="white-space: nowrap;">
        <span style="color: #03328e; font-size: 1.2em;">CYBERB</span>
        <span style="color: #ff7d00; font-size: 1.2em;">⋮</span>
        <span style="color: #03328e; font-size: 1.2em;">Z</span>
      </span>
    </h1>

    <p>
      在這裡找到解答、探索功能，並精通 <strong>CYBERBIZ</strong> 平台。<br>
      我們隨時提供協助，讓您快速上手並善用每項工具。
    </p>

    <div class="custom-button-group" style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1rem;
    ">
      <a href="ec/" class="md-button md-button--primary">開始探索 ➜</a>
      <a href="resources/changelog/" class="md-button">最新消息</a>
    </div>
  </div>

  <!-- RIGHT: Zensical Callout -->
	  <style>
	/* Light/Dark mode colors */
	[data-md-color-scheme="default"] {
	  --callout-bg: #f2f6fc;
	  --callout-hover: #FAFBFC; 
/*	  --callout-hover: #f5f7fa;  */
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
	  border: 1px solid var(--border-color); /* light border */
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
	  border-bottom: 1px solid var(--divider-color); /* shared baseline */
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
    <a href="#"><span class="badge">新增</span>門市助理快速上手指南</a>
    <a href="#"><span class="badge">更新</span>EC 商品上架流程</a>
    <a href="#"><span class="badge">新增</span>全新金物流設定說明</a>
  </div>

  <!-- Popular -->
  <div id="popular" role="tabpanel" class="tab-content">
    <a href="#"><span class="badge">FAQ</span>EC 付款流程 FAQ</a>
    <a href="#"><span class="badge">FAQ</span>商品管理常見問題整理</a>
    <a href="#"><span class="badge">指南</span>門市權限設定實務指南</a>
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

## :lucide-shopping-bag: 品牌官網 


=== "商店設定"

	<div class= "grid cards" markdown>
	
	- [__新手上路__](品牌官網/get-started.md)
	- [__搬家到 CYBERBIZ__](#)
	- [__網站外觀__](#)
	
	</div>

=== "商品管理"

	<div class= "grid cards" markdown>
	
	- [__商品管理__]
	- [__庫存管理__]
	
	</div>

=== "訂單物流"

	<div class= "grid cards" markdown>
	
	- [__訂單流程__]
	- [__物流設定__]
	
	</div>

=== "支付金流"

	<div class= "grid cards" markdown>
	
	- [__付款方式__]
	- [__款項對帳__]
	
	</div>

=== "會員管理"

	<div class="grid cards" markdown>
	
	-   :material-clock-fast:{ .lg .middle } __快速上手__
	
	    ---
	
	    Install [`zensical`](#) with [`pip`](#) and get up
	    and running in minutes
	
	    [:octicons-arrow-right-24: Getting started](#)
	
	-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__
	
	    ---
	
	    Focus on your content and generate a responsive and searchable static site
	
	    [:octicons-arrow-right-24: Reference](#)
	
	-   :material-format-font:{ .lg .middle } __Made to measure__
	
	    ---
	
	    Change the colors, fonts, language, icons, logo and more with a few lines
	
	    [:octicons-arrow-right-24: Customization](#)
	
	-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__
	
	    ---
	
	    Zensical is licensed under MIT and available on [GitHub]
	
	    [:octicons-arrow-right-24: License](#)
	
	</div>

=== "行銷成長"

	<div class= "grid cards" markdown>
	
	- [__行銷工具__]
	- [__成長拓展__]
	
	</div>

=== "整合串接"

	<div class= "grid cards" markdown>
	
	- [__第三方服務整合__]
	- [__API 與自動化__]
	
	</div>

---

## :lucide-warehouse: 智慧倉儲

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`zensical`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

</div>


## :material-point-of-sale: 智能 POS

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`zensical`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

</div>
	
---

## :lucide-blocks: CYBERBIZ 擴充功能

<div class="grid cards" markdown>

- [:lucide-layout-grid:  __APP MARKET__](){ .md-button .extension-tag }     
<big>__擴充商店__</big>      
擴充服務市集    

- [:lucide-cog: __AUTOMATION__](){ .md-button .extension-tag }     
<big>__自動化功能__</big>      
自動化行銷 精準分眾省荷包  

- [:lucide-ticket: __TICKET__](){ .md-button .extension-tag }    
<big>[__電子票券__](ec/products/電子票券指南)</big>    
線上購票 線下體驗  

- [:lucide-zap: __NOW!__](){ .md-button .extension-tag }    
<big>__快速到貨__</big>    
整合機車外送系統  

- [:lucide-credit-card: __PAYMENTS__](){ .md-button .extension-tag }    
<big>__金流支付__</big>  
金物流一體的安全、多元支付  

- [:lucide-message-circle: __CHAT BOX__](){ .md-button .extension-tag }    
<big>__訊息通__</big>       
全通路訊息一站整合  

- [:lucide-link-2: __CHANNEL BRIDGE__](){ .md-button .extension-tag }  
<big>__全通路管理助手__</big>     
跨平台商品庫存整合    

- [:lucide-shopping-cart: __STORE PAL__](){ .md-button .extension-tag }    
<big>__門市助理__</big>    
OMO 整合  

- [:lucide-arrow-right-from-line: __EXPRESS__](){ .md-button .extension-tag }    
<big>__跨境通__</big>    
打通跨境商務的最後一哩  

</div>

---

## :lucide-newspaper: 最新消息

<div class="grid cards" markdown>

-   :lucide-megaphone: <big>[__功能報報__](#)</big>  
	了解最新動態與實用技巧，請持續關注我們的部落格。

-   :lucide-history: <big>[__更新紀錄__](#)</big>    
    關注我們的功能更新紀錄。

- :lucide-messages-square: <big>[__聯絡我們__](#) </big>  
  透過後台的線上客服與我們聯繫。

</div>
