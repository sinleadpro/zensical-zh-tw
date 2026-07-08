document$.subscribe(function () {
  document.querySelectorAll('.headerlink').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var id = link.parentNode.id;
      var url = window.location.origin + window.location.pathname + '#' + id;
      navigator.clipboard.writeText(url).then(function () {
        var tip = document.createElement('span');
        tip.textContent = '已複製連結';
        tip.style.cssText =
          'position:absolute;inset:auto 0 auto auto;font-size:0.65rem;color:var(--md-accent-fg-color);background:var(--md-default-bg-color);padding:0 0.3rem;border-radius:4px;white-space:nowrap;pointer-events:none;z-index:1;animation:fadeInOut 1.5s ease forwards;';
        link.parentNode.style.position = 'relative';
        link.parentNode.appendChild(tip);
        setTimeout(function () {
          tip.remove();
        }, 1500);
      });
      return false;
    });
  });
});
