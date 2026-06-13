var driverObj = null
var tourResumed = false

document$.subscribe(function () {
  var params = new URLSearchParams(location.search)
  if (params.get('tour') === '1' && !tourResumed) {
    tourResumed = true
    history.replaceState({}, '', location.pathname)
    setTimeout(startDocTour, 400)
  }
})

function startDocTour() {
  var d = window.driver && window.driver.js && window.driver.js.driver
  if (!d) return

  var faqTocItem = findFaqTocItem()

  driverObj = d({
    showProgress: true,
    showButtons: ['next', 'previous', 'close'],
    steps: [
      {
        element: '.md-content',
        onHighlighted: function () {
          window.scrollTo({ top: 0, behavior: 'smooth' })
        },
        popover: {
          title: '歡迎來到 CYBERBIZ 幫助中心',
          description: '這是全新改版的幫助中心，每篇教學文件都包含完整的操作步驟、圖文範例與注意事項。接下來帶您認識文件頁面的各個區塊。',
          side: 'bottom',
        },
      },
      {
        element: '.md-search__button',
        popover: {
          title: '全文搜尋',
          description: '按下 Cmd+K（Mac）或 Ctrl+K（Windows）快速開啟搜尋覆層（search overlay），輸入關鍵字即可跨所有產品線進行全文檢索。搜尋結果右側的標籤列表可直接點選篩選，快速鎖定目標文件。',
          side: 'bottom',
        },
      },
      {
        element: '.md-tabs',
        popover: {
          title: '產品分類分頁',
          description: '頂端分頁讓您在不同產品線之間快速切換：品牌官網（EC）、智慧倉儲（WMS）、智能 POS。點擊分頁即可瀏覽該產品的所有教學文件。',
          side: 'bottom',
        },
      },
      {
        element: '.md-sidebar--primary .md-nav--primary',
        popover: {
          title: '左側章節選單',
          description: '目前產品線的完整功能分類。展開各主題即可看到所屬文件清單，點擊即可閱讀該篇詳細教學。',
          side: 'right',
        },
      },
      {
        element: '.md-sidebar--secondary .md-nav--secondary',
        popover: {
          title: '右側頁面目次',
          description: '本頁文件的章節大綱（Table of Contents）。點擊任一標題即可快速跳轉至該段落，不需手動滾動頁面。',
          side: 'left',
        },
      },
      {
        element: faqTocItem || '.md-sidebar--secondary .md-nav--secondary',
        popover: {
          title: '常見問題快速入口',
          description: '每篇教學文件結尾都附有常見問題（FAQ）區塊，可從右側目次一鍵跳轉，快速找到解答。',
          side: 'left',
        },
      },
    ],
    onDestroyed: function () {
      driverObj = null
      tourResumed = false
    },
  })

  driverObj.drive()
}

function findFaqTocItem() {
  var tocLinks = document.querySelectorAll(
    '.md-sidebar--secondary .md-nav__link'
  )
  for (var i = 0; i < tocLinks.length; i++) {
    if (tocLinks[i].textContent.trim().includes('常見問題')) {
      return tocLinks[i]
    }
  }
  return null
}
