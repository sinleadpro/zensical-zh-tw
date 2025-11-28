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
    padding: 4rem 2rem;
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
    [data-md-color-scheme="default"] {
      --callout-bg: #f5f5f5 !important; /* Light mode */
    }
    [data-md-color-scheme="slate"] {
      --callout-bg: #2a2a2a !important; /* Dark mode */
    }
  </style>

  <!-- Tab container -->
 <div class="hero-callout" style="flex: 1 1 320px;">
  <!-- Tab buttons -->
  <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
	<button class="tab-btn active" onclick="openTab(event, 'latest')">最新文件</button>
	<button class="tab-btn" onclick="openTab(event, 'popular')">熱門文章</button>
   </div>

  <!-- 最新文件 content -->
  <div id="latest" class="tab-content" style="display: block; background-color: var(--callout-bg); border-radius: 12px; padding: 1.5rem;">
    <a href="#">新增：門市助理快速上手指南</a><br>
    <a href="#">更新：EC 商品上架流程</a><br>
    <a href="#">新增：全新金物流設定說明</a><br>
  </div>

  <!-- 熱門文章 content -->
  <div id="popular" class="tab-content" style="display: none; background-color: var(--callout-bg); border-radius: 12px; padding: 1.5rem;">
    <a href="#">EC 付款流程 FAQ</a><br>
    <a href="#">商品管理常見問題整理</a><br>
    <a href="#">門市權限設定實務指南</a><br>
	</div>
   </div>

	<script>
	function openTab(evt, tabName) {
	  // Hide all tab contents
	  const contents = document.querySelectorAll('.tab-content');
	  contents.forEach(c => c.style.display = 'none');
	
	  // Remove active class from all buttons
	  const buttons = document.querySelectorAll('.tab-btn');
	  buttons.forEach(b => b.classList.remove('active'));
	
	  // Show the selected tab
	  document.getElementById(tabName).style.display = 'block';
	  evt.currentTarget.classList.add('active');
	}
	</script>
	
	<style>
	.tab-btn {
	  background: none;
	  border: none;
	  font-weight: bold;
	  cursor: pointer;
	  padding: 0.5rem 1rem;
	}
	.tab-btn.active {
	  border-bottom: 2px solid var(--color-primary);
	}
	</style>

</div>


## 品牌官網

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


## 智慧倉儲
=== "新手上路"
	<div class= "grid cards" markdown>
	
	- __新手上路__
	- ____
	
	</div>

### 智能 POS
=== "新手上路"
	<div class= "grid cards" markdown>
	
	- __新手上路__
	- ____
	
	</div>

### 門市助理
=== "新手上路"
	<div class= "grid cards" markdown>
	
	- __新手上路__
	- ____
	
	</div>


## CYBERBIZ 擴充功能


<div class="grid cards" markdown>

- :lucide-layout-grid:  __APP MARKET__   
  for content and structure
- :lucide-cog: __AUTOMATION__   
  for interactivity
- :lucide-ticket: __TICKETS__  
  for text running out of boxes
- :lucide-zap: __NOW!__  
  ... huh?
- :lucide-credit-card: __PAYMENTS__  
  ... huh?
- :lucide-message-circle: __CHAT BOX__  
  ... huh?
- :lucide-link-2: __CHANNEL BRIDGE__  
  ... huh?

</div>

## 最新消息

<div class="grid cards" markdown>

-   :lucide-rss: __功能報報__

    ---

    了解最新動態與實用技巧，請持續關注我們的部落格。


-   :lucide-history: __更新紀錄__

    ---

    我們不斷為 **CYBERBIZ** 帶來新功能與優化，請關注我們的功能更新紀錄。

</div>


## 聯絡我們

<div class="grid cards" markdown>

- :material-headset: [__需要協助嗎？__](#)  
  透過後台的線上客服與我們聯繫。

- :material-video-outline: [__使用 Jam 回報問題__](tags/types/how-to/使用 Jam 回報問題.md)  
  使用 Jam 擷取螢幕或錄影，提供完整資訊給客服與研發團隊，加快問題排解。

</div>

<br>