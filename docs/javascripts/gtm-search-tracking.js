// docs/javascripts/gtm-search-tracking.js
//
// 監聽站內搜尋框（Zensical 以開放式 Shadow DOM 掛載，role="combobox"）的輸入內容，
// 於使用者停止輸入（防抖）或離開搜尋框時，將關鍵字推送至 dataLayer，
// 供 GTM 自訂事件觸發器 (event: "site_search") 擷取，作為優化站內搜尋的分析材料。
//
// 設計重點：
// 1. 監聽器掛在 document 層級並使用 capture 階段，搭配 event.composedPath()
//    取得跨越 Shadow DOM 邊界的真實來源元素，因此不受 navigation.instant
//    (SPA 式導覽) 替換 DOM 子樹影響，也不需要在 GTM 後台用選取器指向元素。
// 2. 僅在使用者已同意 Cookie 政策中的「分析 (analytics)」類別時才會蒐集，
//    與站內原生 Google Analytics 整合 (__md_analytics) 採用相同的同意機制。
// 3. 以防抖 (debounce) 方式蒐集完整關鍵字，避免每個按鍵都送出事件。
(function () {
  "use strict";

  var DEBOUNCE_MS = 500;
  var EVENT_NAME = "site_search";
  var lastValue = "";
  var debounceTimer = null;

  function isSearchInput(el) {
    return !!el && el.tagName === "INPUT" && el.getAttribute("role") === "combobox";
  }

  function getOriginElement(e) {
    if (typeof e.composedPath === "function") {
      var path = e.composedPath();
      return path && path.length ? path[0] : e.target;
    }
    return e.target;
  }

  function hasAnalyticsConsent() {
    try {
      if (typeof __md_get !== "function") return false;
      var consent = __md_get("__consent");
      return !!(consent && consent.analytics);
    } catch (err) {
      return false;
    }
  }

  function pushSearchTerm(term) {
    term = (term || "").trim();
    if (!term || term === lastValue) return;
    lastValue = term;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: EVENT_NAME,
      search_term: term,
      search_source: "docs_header_search"
    });
  }

  function handleInput(e) {
    if (!hasAnalyticsConsent()) return;
    var el = getOriginElement(e);
    if (!isSearchInput(el)) return;
    var value = el.value;
    window.clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(function () {
      pushSearchTerm(value);
    }, DEBOUNCE_MS);
  }

  function handleBlur(e) {
    if (!hasAnalyticsConsent()) return;
    var el = getOriginElement(e);
    if (!isSearchInput(el)) return;
    window.clearTimeout(debounceTimer);
    pushSearchTerm(el.value);
  }

  document.addEventListener("input", handleInput, true);
  document.addEventListener("blur", handleBlur, true);
})();
