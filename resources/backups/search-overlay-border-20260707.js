// docs/javascripts/search-overlay-style.js

window.addEventListener("load", () => {

  document.querySelectorAll("*").forEach(el => {

    if (!el.shadowRoot) return;

    const style = document.createElement("style");

    style.textContent = `

      /* OUTER SEARCH OVERLAY BOX */
      .n {

        border: 1px solid rgba(255,255,255,0.08) !important;

        border-radius: 24px !important;

        box-shadow:
          0 24px 80px rgba(0,0,0,0.55),
          0 0 0 1px rgba(255,255,255,0.03) !important;

        overflow: hidden !important;

      }

    `;

    el.shadowRoot.appendChild(style);

  });

});
