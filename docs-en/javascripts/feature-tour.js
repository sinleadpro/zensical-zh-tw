var driverObj = null
var tourResumed = false
var tourCompleted = false

function sendGA4Event(action, params) {
  if (typeof gtag === 'function') {
    gtag('event', action, Object.assign({ tour_name: 'help_center_intro' }, params))
  }
}

document$.subscribe(function () {
  var params = new URLSearchParams(location.search)
  if (params.get('tour') === '1' && !tourResumed) {
    tourResumed = true
    history.replaceState({}, '', location.pathname)
    setTimeout(startDocTour, 400)
  }
})

function tourLocale() {
  var lang = (document.documentElement.lang || 'zh-TW').toLowerCase()
  if (lang === 'en' || lang.indexOf('en-') === 0) return 'en'
  return 'zh-TW'
}

function tourCopy(locale) {
  if (locale === 'en') {
    return {
      buttons: null,
      steps: [
        {
          title: 'Welcome to the CYBERBIZ Help Center',
          description: 'This help center has been redesigned. Each guide includes steps, screenshots, and notes. Next, we will walk through the parts of a documentation page.',
        },
        {
          title: 'Search',
          description: 'Press Cmd+K (Mac) or Ctrl+K (Windows) to open full-text search, or click the search field.',
        },
        {
          title: 'Full-text search',
          description: 'The search overlay is open. Type a keyword to search across all product lines. Results appear in the left panel, and related tags in the right panel. Click a tag to narrow the results. For example, search for "product", then click the "settings" tag to show only product settings guides.',
        },
        {
          title: 'Product tabs',
          description: 'Use the tabs at the top to switch product lines: Online Store, Smart Warehousing, and Smart POS. Click a tab to browse that product\'s guides.',
        },
        {
          title: 'Chapter menu on the left',
          description: 'Feature categories for the current product line. Expand a topic to see its guides, then click a guide to open it.',
        },
        {
          title: 'Page outline on the right',
          description: 'The table of contents for this page. Click a heading to jump to that section.',
        },
        {
          title: 'FAQ shortcut',
          description: 'Each guide ends with an FAQ section. Open it from the outline on the right.',
        },
      ],
    }
  }
  return {
    buttons: {
      nextBtnText: '下一步',
      prevBtnText: '上一步',
      doneBtnText: '完成',
      progressText: '{{current}} / {{total}}',
    },
    steps: [
      {
        title: '歡迎來到 CYBERBIZ 幫助中心',
        description: '這是全新改版的幫助中心，每篇教學文件都包含完整的操作步驟、圖文範例與注意事項。接下來帶您認識文件頁面的各個區塊。',
      },
      {
        title: '搜尋',
        description: '按下 Cmd+K（Mac）或 Ctrl+K（Windows）可快速開啟全文搜尋，或直接點擊搜尋欄。',
      },
      {
        title: '全文搜尋',
        description: '搜尋覆層已開啟，輸入關鍵字即可跨所有產品線進行全文檢索。搜尋結果顯示在左側面板，右側面板則列出相關標籤；點擊任一標籤可進一步篩選結果，例如搜尋「商品」後點擊「設定」標籤，只顯示與商品設定有關的文件。',
      },
      {
        title: '產品分類分頁',
        description: '頂端分頁讓您在不同產品線之間快速切換：品牌官網（EC）、智慧倉儲（WMS）、智能 POS。點擊分頁即可瀏覽該產品的所有教學文件。',
      },
      {
        title: '左側章節選單',
        description: '目前產品線的完整功能分類。展開各主題即可看到所屬文件清單，點擊即可閱讀該篇詳細教學。',
      },
      {
        title: '右側頁面目次',
        description: '本頁文件的章節大綱（Table of Contents）。點擊任一標題即可快速跳轉至該段落，不需手動滾動頁面。',
      },
      {
        title: '常見問題快速入口',
        description: '每篇教學文件結尾都附有常見問題（FAQ）區塊，可從右側目次一鍵跳轉，快速找到解答。',
      },
    ],
  }
}

function findSearchInput() {
  var all = document.querySelectorAll('*')
  for (var i = 0; i < all.length; i++) {
    var el = all[i]
    if (el.shadowRoot) {
      var input = el.shadowRoot.querySelector('input[role="combobox"]')
      if (input) return input
    }
  }
  return null
}

function isSearchOpen() {
  var all = document.querySelectorAll('*')
  for (var i = 0; i < all.length; i++) {
    if (all[i].shadowRoot) {
      var p = all[i].shadowRoot.querySelector('.p')
      if (p && window.getComputedStyle(p).opacity !== '0') return true
    }
  }
  return false
}

function closeSearchIfNeeded() {
  if (isSearchOpen()) {
    var btn = document.querySelector('.md-search__button')
    if (btn) btn.click()
  }
}

function isFaqTocLink(link) {
  var text = link.textContent.replace(/\s+/g, ' ').trim()
  var href = link.getAttribute('href') || ''
  var hashIndex = href.indexOf('#')
  var hash = hashIndex === -1 ? '' : href.slice(hashIndex + 1)
  if (text.indexOf('常見問題') !== -1) return true
  if (/^faq\b/i.test(text)) return true
  try {
    hash = decodeURIComponent(hash)
  } catch (e) {}
  return /^faq(-|$)/i.test(hash)
}

function findFaqTocItem() {
  var tocLinks = document.querySelectorAll(
    '.md-sidebar--secondary .md-nav__link'
  )
  for (var i = 0; i < tocLinks.length; i++) {
    if (isFaqTocLink(tocLinks[i])) return tocLinks[i]
  }
  return null
}

function startDocTour() {
  var d = window.driver && window.driver.js && window.driver.js.driver
  if (!d) return

  var faqTocItem = findFaqTocItem()
  var searchInput = findSearchInput()
  var copy = tourCopy(tourLocale())
  var text = copy.steps

  var stepDefs = [
    {
      element: '.md-content',
      onHighlighted: function () {
        window.scrollTo({ top: 0, behavior: 'smooth' })
      },
      popover: {
        title: text[0].title,
        description: text[0].description,
        side: 'bottom',
        align: 'center',
      },
    },
    {
      element: '.md-search__button',
      onHighlighted: function () {
        closeSearchIfNeeded()
      },
      popover: {
        title: text[1].title,
        description: text[1].description,
        side: 'bottom',
      },
    },
    {
      element: searchInput || '.md-search__button',
      onHighlighted: function () {
        if (!isSearchOpen()) {
          var btn = document.querySelector('.md-search__button')
          if (btn) btn.click()
        }
      },
      popover: {
        title: text[2].title,
        description: text[2].description,
        side: 'bottom',
      },
    },
    {
      element: '.md-tabs',
      onHighlighted: function () {
        closeSearchIfNeeded()
      },
      popover: {
        title: text[3].title,
        description: text[3].description,
        side: 'bottom',
      },
    },
    {
      element: '.md-sidebar--primary .md-nav--primary',
      popover: {
        title: text[4].title,
        description: text[4].description,
        side: 'right',
      },
    },
    {
      element: '.md-sidebar--secondary .md-nav--secondary',
      popover: {
        title: text[5].title,
        description: text[5].description,
        side: 'left',
      },
    },
    {
      element: faqTocItem || '.md-sidebar--secondary .md-nav--secondary',
      popover: {
        title: text[6].title,
        description: text[6].description,
        side: 'left',
      },
    },
  ]

  var driverConfig = {
    showProgress: true,
    showButtons: ['next', 'previous', 'close'],
    onHighlightStarted: function (element, step, options) {
      sendGA4Event('tour_step_view', {
        step_index: options.state.activeIndex,
        step_title: step.popover.title
      })
      if (options.state.activeIndex === stepDefs.length - 1) {
        tourCompleted = true
      }
    },
    onNextClick: function () {
      sendGA4Event('tour_next')
      driverObj.moveNext()
    },
    onPrevClick: function () {
      sendGA4Event('tour_prev')
      driverObj.movePrevious()
    },
    steps: stepDefs,
    onDestroyed: function () {
      sendGA4Event('tour_ended', { completed: tourCompleted })
      closeSearchIfNeeded()
      driverObj = null
      tourResumed = false
      tourCompleted = false
    },
  }
  if (copy.buttons) {
    driverConfig.nextBtnText = copy.buttons.nextBtnText
    driverConfig.prevBtnText = copy.buttons.prevBtnText
    driverConfig.doneBtnText = copy.buttons.doneBtnText
    driverConfig.progressText = copy.buttons.progressText
  }

  driverObj = d(driverConfig)

  driverObj.drive()
}
