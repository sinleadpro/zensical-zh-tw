---
title: 新功能報報
description: "CYBERBIZ 新功能報報，依月份彙整最新上線功能與功能優化內容。"
last_modified: 2026-09-21 11:15
type: hub
lang: zh-TW
author: Ann
reviewers: []
notes: []
related: []
permalink: "https://help.cyberbiz.io/resources/new-release/"
search:
  exclude: false
icon: lucide/megaphone
hide:
  - description
  - navigation
  - toc
  - feedback
  - path
---
<style>
  .release-index {
    --release-blue: #012e9e;
    --release-text: #111827;
    --release-muted: #697386;
    max-width: 1240px;
    margin: 0 auto;
    padding: 58px 40px 90px;
    color: var(--release-text);
  }

  .release-index,
  .release-index * {
    box-sizing: border-box;
  }

  .release-hero {
    display: flex;
    align-items: center;
    gap: 32px;
    margin-bottom: 38px;
  }

  .release-heading {
    min-width: 0;
  }

  .release-heading h1 {
    margin: 0;
    color: var(--release-text);
    font-size: 40px;
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1.2;
  }

  .release-heading p {
    margin: 14px 0 0;
    color: var(--release-muted);
    font-size: 17px;
    line-height: 1.8;
  }

  .release-timeline {
    display: grid;
    gap: 20px;
    margin-left: 0;
    width: 100%;
  }

  .release-month-card {
    display: grid;
    grid-template-columns: 265px 1px minmax(0, 1fr) 64px;
    column-gap: 28px;
    align-items: center;
    width: 100%;
    min-height: 156px;
    padding: 30px 28px;
    border: 1px solid rgba(1, 46, 158, .08);
    border-radius: 34px;
    background: rgba(255, 255, 255, .98);
    box-shadow: 0 16px 42px rgba(1, 46, 158, .07);
    color: inherit;
    text-align: left;
    text-decoration: none;
    transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
  }

  .release-month-card:hover {
    border-color: rgba(1, 46, 158, .28);
    box-shadow: 0 24px 60px rgba(1, 46, 158, .15);
    color: inherit;
    transform: translateY(-4px);
  }

  .release-month {
    color: var(--release-blue);
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 4px;
    line-height: 1.25;
    white-space: nowrap;
  }

  .release-divider {
    width: 1px;
    height: 104px;
    border-left: 4px dashed rgba(1, 46, 158, .14);
  }

  .release-features {
    min-width: 0;
    display: grid;
    gap: 14px;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .release-feature-row {
    display: flex;
    align-items: center;
    gap: 12px;
    /* 空間足夠時同行；不足時自然換行，不產生水平捲動。 */
    flex-wrap: wrap;
    min-width: 0;
    max-width: 100%;
  }

  .release-feature-name {
    flex: 0 1 auto;
    min-width: 0;
    max-width: 100%;
    white-space: normal;
    overflow-wrap: anywhere;
    color: var(--release-text);
    font-size: 17px;
    font-weight: 900;
    letter-spacing: .2px;
    line-height: 1.35;
  }

  .release-version-tag {
    flex: 0 0 auto;
    display: inline-flex;
    align-items: center;
    min-height: 28px;
    padding: 0 12px;
    border: 1px solid rgba(222, 130, 24, .20);
    border-radius: 999px;
    background: rgba(222, 130, 24, .08);
    color: #de8218;
    font-size: 13px;
    font-weight: 900;
    line-height: 1;
    white-space: nowrap;
  }

  .release-version-tag-2 {
    flex: 0 0 auto;
    display: inline-flex;
    align-items: center;
    min-height: 28px;
    padding: 0 12px;
    border: 1px solid rgba(1, 46, 158, .16);
    border-radius: 999px;
    background: rgba(1, 46, 158, .06);
    color: var(--release-blue);
    font-size: 13px;
    font-weight: 900;
    line-height: 1;
    white-space: nowrap;
  }

  .release-arrow {
    display: grid;
    place-items: center;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: rgba(1, 46, 158, .06);
    color: var(--release-blue);
    font-size: 38px;
    font-weight: 800;
    line-height: 1;
    transition: .22s ease;
  }

  .release-month-card:hover .release-arrow {
    background: var(--release-blue);
    color: #fff;
    transform: translateX(4px);
  }

  /* 文字裝飾：標題、說明、月份、功能名稱與版本標籤。 */
  .release-index .release-heading h1,
  .release-index .release-heading p,
  .release-index .release-month,
  .release-index .release-feature-name,
  .release-index .release-version-tag,
  .release-index .release-version-tag-2,
  .release-index .release-arrow {
    text-decoration: none;
  }

  /* 卡片本身為連結；底線必須在連結及互動狀態一併取消。 */
  .release-index .release-timeline a.release-month-card,
  .release-index .release-timeline a.release-month-card:link,
  .release-index .release-timeline a.release-month-card:visited,
  .release-index .release-timeline a.release-month-card:hover,
  .release-index .release-timeline a.release-month-card:focus,
  .release-index .release-timeline a.release-month-card:active {
    text-decoration: none;
  }
  @media (max-width: 760px) {
    .release-index {
      padding: 32px 16px 56px;
    }

  .release-hero {
      display: block;
      margin-bottom: 28px;
    }

    .release-heading h1 {
      font-size: 32px;
    }

    .release-heading p {
      font-size: 15px;
    }

    .release-month-card {
      grid-template-columns: 1fr 48px;
      gap: 20px;
      min-height: 0;
      padding: 24px;
      border-radius: 24px;
    }

    .release-month {
      grid-column: 1 / -1;
      font-size: 22px;
      letter-spacing: 3px;
    }

    .release-divider {
      display: none;
    }

    .release-features {
      grid-column: 1;
      gap: 12px;
    }

    .release-feature-name {
      font-size: 15px;
    }

    .release-version-tag {
      font-size: 12px;
    }

    .release-arrow {
      grid-column: 2;
      grid-row: 2;
      width: 48px;
      height: 48px;
      font-size: 30px;
    }
  }
</style>

<div class="release-index">
  <div class="release-hero">
    <div class="release-heading">
      <h1>新功能報報</h1>
      <p>快速掌握最新上線功能及優化，CYBERBIZ 陪您一同成長</p>
    </div>
  </div>

  <div>
    <div class="release-timeline">
      <a class="release-month-card" href="2026-08.md">
        <div class="release-month">2026 / 08 月更新</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">置頂公告｜多版位排程輪播功能</span>
            <span class="release-version-tag">#拖拉版型</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">CHAT BOX｜支援手機版後台檢視、自訂前台對話提示文字</span>
            <span class="release-version-tag">#企業版</span>
            <span class="release-version-tag">#PLUS版</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">超商逾期未取訂單可設定是否自動退款</span>
            <span class="release-version-tag">#企業版</span>
            <span class="release-version-tag">#PLUS版</span>
            <span class="release-version-tag-2">#CYBERBIZ PAYMENTS｜收款入帳</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">支援編輯進行中全館型優惠碼</span>
            <span class="release-version-tag">#企業版</span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-07.md">
        <div class="release-month">2026 / 07 月更新</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">CHAT BOX｜官網整合對話入口</span>
            <span class="release-version-tag">#企業版</span>
            <span class="release-version-tag">#PLUS版</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">消費者再次購買功能</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">自訂排版設計支援手機版多列並排顯示</span>
            <span class="release-version-tag">#拖拉版型</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">可編輯進行中的優惠碼</span>
            <span class="release-version-tag">#企業版</span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-06.md">
        <div class="release-month">2026 / 06 月更新</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">滿額／滿件贈支援限定會員分群</span>
            <span class="release-version-tag">#企業版</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">VIP 會員層級效期新增無期限設定</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">結帳頁自動帶入紅利點數開關</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">電腦版商品圖游標懸停效果：擴充適用頁面</span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-05.md">
        <div class="release-month">2026 / 05 月更新</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">CHAT BOX 訊息通</span>
            <span class="release-version-tag">#企業版</span>
            <span class="release-version-tag">#PLUS版</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">組合品可同時支援指定及任選情境</span>
            <span class="release-version-tag">#企業版</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">後台發動 7-11 C2C 退貨便功能</span>
            <span class="release-version-tag-2">#CYBERBIZ PAYMENTS</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">滿額/滿件贈可自選贈品款式</span>
            <span class="release-version-tag">#企業版</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">前台導覽列支援字體大小設定</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">前台商品圖圓角設定</span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>
    </div>
  </div>
</div>





