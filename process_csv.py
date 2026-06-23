import csv
import re
import os

# Mapping of title to filepath from Grep output
title_to_path = {
    "Pandago 配送異常規範": "docs/ec/orders/pandago-delivery-exception-rules.md",
    "Step 3 官網與蝦皮商店庫存同步": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step3-sync-inventory-with-shopee.md",
    "Step 5 官網與蝦皮商品資訊同步": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step5-sync-product-info-with-shopee.md",
    "Step 4 官網商品建立為蝦皮商品": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step4-create-shopee-products-from-site.md",
    "Step 2 導入商品與建立關聯": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step2-import-products-and-link.md",
    "紅利商城 (EC)": "docs/ec/marketing/bonus-point-mall.md",
    "導購轉化": "docs/ec/app-market/storepal/sales-conversion.md",
    "Step 1 安裝與授權商店": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step1-install-and-activate.md",
    "指定商品送紅利": "docs/ec/marketing/send-bonus-points-for-specific-products.md",
    "一頁式商店": "docs/ec/marketing/one-page-store.md",
    "查看業績": "docs/ec/app-market/storepal/view-sales-performance.md",
    "缺貨訂單部分配送或取消流程": "docs/ec/orders/out-of-stock-partial-shipping-or-cancellation.md",
    "消費者購買流程": "docs/ec/orders/consumer-purchase-process.md",
    "期間限定首購禮": "docs/ec/marketing/limited-time-first-purchase-gift.md",
    "搜尋與建立會員": "docs/ec/app-market/storepal/search-and-create-members.md",
    "紅配綠多組合優惠": "docs/ec/marketing/red-and-green-bundle-discounts.md",
    "互動遊戲 (EC)": "docs/ec/marketing/interactive-games.md",
    "快速到貨運費計算與對帳規範": "docs/ec/orders/quick-delivery-shipping-fee-calculation-and-reconciliation.md",
    "開啟門市取貨服務": "docs/ec/payments-and-logistics/store-pickup/enable-store-pickup-service.md",
    "開啟門市快速到貨服務": "docs/ec/payments-and-logistics/cyberbiz-now/enable-cyberbiz-now-quick-delivery.md",
    "DHL 跨境物流": "docs/ec/payments-and-logistics/dhl-cross-border-logistics.md",
    "了解分潤功能": "docs/ec/profit-sharing/index.md",
    "註冊人分潤": "docs/ec/profit-sharing/registrant-profit-sharing.md",
    "複製商品到快速到貨門市": "docs/ec/products/copy-products-to-quick-delivery-stores.md",
    "啟用部分串倉與混單": "docs/wms/enable-partial-warehouse-integration-and-mixed-orders.md",
    "匯出分潤報表": "docs/ec/profit-sharing/export-profit-sharing-reports.md",
    "順豐海外物流": "docs/ec/payments-and-logistics/sf-express-overseas-logistics.md",
    "自動確認對帳帳款設定": "docs/ec/website-management/auto-confirm-reconciliation-accounts.md",
    "推薦人分潤": "docs/ec/profit-sharing/referrer-profit-sharing.md",
    "查詢分潤夥伴與代碼": "docs/ec/profit-sharing/query-profit-sharing-partners-and-codes.md",
    "推薦碼連結的應用": "docs/ec/profit-sharing/referral-link-applications.md",
    "LINEX 跨境物流": "docs/ec/payments-and-logistics/linex-cross-border-logistics.md",
    "快速到貨出貨與配送追蹤": "docs/ec/orders/quick-delivery-shipping-and-distribution.md",
    "快速到貨訂單接單準備": "docs/ec/orders/quick-delivery-order-preparation.md",
    "設定前台多國語言與多幣別": "docs/ec/website-management/setup-multi-language-and-multi-currency.md",
    "啟用部分串倉與拆單": "docs/wms/enable-partial-warehouse-integration-and-order-splitting.md",
    "LINE 訊息格式規範": "docs/ec/app-market/chatbox/line-message-format-spec.md",
    "Chat Box 訊息通": "docs/ec/app-market/chatbox/index.md",
    "Chat Box AI 建議回覆": "docs/ec/app-market/chatbox/chat-box-ai-suggested-replies.md",
    "Meta 訊息格式規範": "docs/ec/app-market/chatbox/meta-message-format-spec.md",
    "設定紅利點數": "docs/ec/marketing/setup-bonus-points.md",
    "結帳": "docs/pos/check/index.md",
    "開始使用": "docs/pos/get-started/index.md",
    "智能 POS 產品中心": "docs/pos/index.md",
    "設定 POS 多付款方式": "docs/pos/check/payment-method/multiple-payment-methods.md",
    "EPSON 有線發票機": "docs/pos/hardware/epson-tm-t82iii-invoice-printer.md",
    "Chat Box 串接 LINE 官方帳號": "docs/ec/app-market/chatbox/connect-chat-box-to-line-oa.md",
    "Chat Box 串接 Facebook 粉絲專頁": "docs/ec/app-market/chatbox/connect-chat-box-to-facebook-page.md",
    "門市助理安裝與導入": "docs/ec/app-market/storepal/install-and-setup-storepal.md",
    "全站功能與業績歸因設定": "docs/ec/app-market/storepal/configure-global-settings-and-attribution.md",
    "匯入顧客門市推薦人": "docs/ec/app-market/storepal/bulk-import-customer-referrers.md",
    "會員數據智庫": "docs/ec/app-market/storepal/member-data-warehouse.md",
    "門市助理": "docs/ec/app-market/storepal/index.md",
    "會員身份識別": "docs/ec/app-market/storepal/member-identification.md",
    "員工帳號與角色": "docs/ec/app-market/storepal/staff-accounts-and-role.md",
    "門市助理績效報表": "docs/ec/app-market/storepal/performance-reports.md",
    "篩選器與會員分群": "docs/ec/members/member-filters-and-groups.md",
    "滿額贈 / 滿件贈": "docs/ec/marketing/threshold-gifts-and-quantity-gifts.md",
    "設定 VIP 專屬優惠": "docs/ec/members/vip/setup-exclusive-vip-discounts.md",
    "官網與倉儲同步規則": "docs/wms/site-and-warehouse-sync-rules.md",
    "設定商品(現貨、限量、預購)": "docs/wms/setup-products-stock-limit-preorder.md",
    "退貨與派車": "docs/wms/returns-and-vehicle-dispatch.md",
    "商家自行驗收退貨": "docs/wms/merchant-self-inspection-of-returns.md",
    "手動確認收貨": "docs/wms/manually-confirm-receipt.md",
    "串倉申請流程與開通": "docs/wms/application-process-and-activation.md",
    "設定 POS 星益欣電子發票": "docs/pos/third-party/setup-pos-star-plus-e-invoice.md",
    "申請盟立電子發票": "docs/pos/third-party/monolith-e-invoice.md",
    "驅動程式": "docs/pos/software/drivers.md",
    "管理一般訂單": "docs/pos/orders/manage-general-orders.md",
    "使用 POS 前台管理會員": "docs/pos/member/index.md",
    "全通路庫存管理指南": "docs/pos/inventory/omnichannel-inventory-management.md",
    "混稅發票": "docs/pos/check/mixed-tax-invoices.md",
    "設定紅利商城 (POS)": "docs/pos/check/bonus-point-mall.md",
    "門市取貨：虛實整合營運導航": "docs/ec/payments-and-logistics/store-pickup/index.md",
    "門市取貨訂單出貨": "docs/ec/orders/store-pickup-orders.md",
    "訂單退貨流程": "docs/ec/orders/order-return-process.md",
    "訂單退款流程": "docs/ec/orders/order-refund-process.md",
    "管理會員檔案": "docs/ec/members/manage-member-profiles.md",
    "定期訂購活動頁": "docs/ec/marketing/subscription-campaign-page.md",
    "設定生日禮": "docs/ec/marketing/setup-birthday-gift.md",
    "設定優惠碼": "docs/ec/marketing/coupon/setup-promo-codes.md",
    "設定優惠券": "docs/ec/marketing/coupon/setup-coupons.md",
    "了解優惠券與優惠碼": "docs/ec/marketing/coupon/index.md",
    "API 與 Webhook 串接指南": "docs/ec/app-market/api-and-webhook-integration-guide.md",
    "調倉單": "docs/wms/transfer-orders.md",
    "供應商": "docs/wms/suppliers.md",
    "商店設定": "docs/wms/store-settings.md",
    "單一品項": "docs/wms/single-items.md",
    "季別群組": "docs/wms/seasonal-groups.md",
    "退貨單": "docs/wms/return-orders.md",
    "報表通知設定": "docs/wms/report-notification-settings.md",
    "加工商品": "docs/wms/processed-products.md",
    "POS 系統串倉庫存轉調": "docs/wms/pos-warehouse-inventory-transfer.md",
    "POD 列表": "docs/wms/pod-list.md",
    "權限設定": "docs/wms/permission-settings.md",
    "操作紀錄列表": "docs/wms/operation-logs.md",
    "商家進倉作業規範": "docs/wms/merchant-inbound-operation-rules.md",
    "手動建單": "docs/wms/manual-order-creation.md",
    "列表": "docs/wms/list.md",
    "庫存紀錄": "docs/wms/inventory-records.md",
    "智慧倉儲 (WMS) 產品中心": "docs/wms/index.md",
    "進倉單": "docs/wms/inbound-orders.md",
    "通路": "docs/wms/channels.md",
    "公告": "docs/wms/announcements.md",
    "帳號管理": "docs/wms/account-management.md",
    "員工帳號與權限管理": "docs/pos/store/staff-permissions-and-account-management.md",
    "登入 POS 前台系統": "docs/pos/store/staff-login.md",
    "設定前台自動登出時間": "docs/pos/store/setup-frontend-auto-logout-time.md",
    "安全性設定": "docs/pos/store/security-settings.md",
    "續購與加購方案": "docs/pos/store/renewal-and-add-on-plans.md",
    "POS 門市取貨店員分潤": "docs/pos/store/pos-store-pickup-staff-commission.md",
    "公告系統": "docs/pos/store/announcement-system.md",
    "人員權限欄位參考表": "docs/pos/reference/staff-permission-fields-reference.md",
    "秤重商品條碼": "docs/pos/others/scale-settings.md",
    "小結與關帳作業": "docs/pos/others/daily-closing.md",
    "修改訂單明細頁「店長改價」的顯示名稱": "docs/pos/orders/修改訂單明細頁「店長改價」的顯示名稱",
    "門市取貨訂單(入庫/取貨)": "docs/pos/orders/store-pickup-orders-inbound-and-pickup.md",
    "POS 報表列表與功能說明": "docs/pos/orders/POS 報表列表與功能說明.md",
    "調倉完整流程": "docs/pos/inventory/transfer-complete-process.md",
    "商品查詢": "docs/pos/inventory/product-query.md",
    "出倉單": "docs/pos/inventory/outbound-orders.md",
    "出倉完整流程": "docs/pos/inventory/outbound-complete-process.md",
    "庫存盤點": "docs/pos/inventory/inventory-count.md",
    "庫存調整": "docs/pos/inventory/inventory-adjustment.md",
    "進倉完整流程": "docs/pos/inventory/inbound-complete-process.md",
    "台新有線刷卡機": "docs/pos/hardware/taishin-wired-credit-card-machine.md",
    "平板裝置使用說明": "docs/pos/hardware/tablet-device-user-guide.md",
    "Posiflex 有線發票機": "docs/pos/hardware/posiflex-wired-invoice-printer.md",
    "網路連線異常與斷線提示": "docs/pos/hardware/network-connection-exception-and-disconnection-prompts.md",
    "MYPAY 無線刷卡機": "docs/pos/hardware/mypay-wireless-credit-card-machine.md",
    "標籤印表機": "docs/pos/hardware/label-printer.md",
    "系統硬體與環境需求": "docs/pos/hardware/index.md",
    "EPSON TM-M30III 發票機安裝教學 (Wi-Fi 連接)": "docs/pos/hardware/epson-tm-m30iii-invoice-printer.md",
    "客顯螢幕": "docs/pos/hardware/customer-display-screen.md",
    "使用「店長改價」在 POS 前台調整單品價格": "docs/pos/frontend/使用「店長改價」在 POS 前台調整單品價格.md",
    "子機結帳綁定": "docs/pos/check/sub-device-checkout-binding.md",
    "掃描槍掃描後找不到商品": "docs/pos/check/product-not-found-after-scanner-scan.md",
    "列印商品標籤": "docs/pos/check/print-product-labels.md",
    "列印發票明細": "docs/pos/check/print-invoice-details.md",
    "POS 前台選單設定": "docs/pos/check/pos-frontend-menu-settings.md",
    "POS 前台核銷電子票券": "docs/pos/check/pos-frontend-e-ticket-redemption.md",
    "付款方式": "docs/pos/check/payment-method/index.md",
    "離線結帳模式": "docs/pos/check/offline-checkout-mode.md",
    "庫存不足通知": "docs/pos/check/low-stock-notifications.md",
    "LINE Pay 掃碼支付": "docs/pos/check/line-pay-scan-payment.md",
    "訪客結帳": "docs/pos/check/guest-checkout.md",
    "客顯互動遊戲": "docs/pos/check/customer-display-interactive-games.md",
    "設定顧客 Email 與手機雙重驗證": "docs/ec/website-management/設定顧客 Email 與手機雙重驗證.md",
    "設定與管理二階段驗證": "docs/ec/website-management/設定與管理二階段驗證.md",
    "設定網站基本資訊": "docs/ec/website-management/設定網站基本資訊.md",
    "星益欣電子發票設定指南": "docs/ec/website-management/星益欣電子發票設定指南.md",
    "新增網站管理員並設定權限": "docs/ec/website-management/新增網站管理員並設定權限.md",
    "使用 Authy 啟用二階段驗證設定": "docs/ec/website-management/使用 Authy 啟用二階段驗證設定.md",
    "無法讀取 HTTPS 根網址": "docs/ec/website-management/unable-to-read-https-root-url.md",
    "排除未收到商家通知信件": "docs/ec/website-management/troubleshoot-not-receiving-merchant-notifications.md",
    "系統到期處理流程": "docs/ec/website-management/system-expiry-handling-process.md",
    "設定 301 重定向網站轉址": "docs/ec/website-management/seo/設定 301 重定向網站轉址.md",
    "將 Sitemap 提交至 Google Search Console": "docs/ec/website-management/seo/將 Sitemap 提交至 Google Search Console.md",
    "SEO 設定與優化指南": "docs/ec/website-management/seo/SEO 設定與優化指南.md",
    "保護後台帳號與顧客資料": "docs/ec/website-management/security-settings.md",
    "資安防護總覽與最佳實務": "docs/ec/website-management/security-best-practices.md",
    "續購與自動續約": "docs/ec/website-management/renewal-and-auto-subscription.md",
    "顧客註冊模式對照表": "docs/ec/website-management/references/顧客註冊模式對照表.md",
    "顧客欄位驗證模式對照表": "docs/ec/website-management/references/顧客欄位驗證模式對照表.md",
    "管理者權限與後台選單對照表": "docs/ec/website-management/references/管理者權限與後台選單對應表.md",
    "Cyber 幣儲值中心使用指南": "docs/ec/website-management/points-deposits.md",
    "一鍵開立請款發票": "docs/ec/website-management/one-click-invoice-issuance.md",
    "收不到後台登入 Email 驗證信": "docs/ec/website-management/not-receiving-backend-login-verification-email.md",
    "管理系統代開消費者發票": "docs/ec/website-management/manage-system-issued-consumer-invoices.md",
    "網域管理": "docs/ec/website-management/domain-management.md",
    "顧客註冊流程與欄位": "docs/ec/website-management/customer-registration-flow-and-fields.md",
    "Cloudflare SSL 衝突": "docs/ec/website-management/cloudflare-ssl-conflict.md",
    "欠款自動扣繳設定": "docs/ec/website-management/auto-deduction-of-arrears.md",
    "特定網域信箱套用會員標籤": "docs/ec/website-management/apply-member-tags-to-specific-email-domains.md",
    "關閉商品圖片放大預覽功能": "docs/ec/website-appearance/theme-and-layout/關閉商品圖片放大預覽功能.md",
    "調整首頁跑馬燈（輪播圖）的轉場停留時間": "docs/ec/website-appearance/theme-and-layout/調整首頁跑馬燈輪播圖的轉場停留時間.md",
    "拖拉版型網站設定": "docs/ec/website-appearance/theme-and-layout/theme-editor.md",
    "設定首頁商品群組排序": "docs/ec/website-appearance/theme-and-layout/storefront-collection-sorting.md",
    "建立與管理排程跑馬燈": "docs/ec/website-appearance/theme-and-layout/configure-scheduled-carousels.md",
    "設定轉貼連結縮圖 OG Image": "docs/ec/website-appearance/site-settings/設定轉貼連結縮圖 OG Image.md",
    "設定網頁鎖右鍵保護圖文版權": "docs/ec/website-appearance/site-settings/設定網頁鎖右鍵保護圖文版權.md",
    "設定網站標題與 SEO": "docs/ec/website-appearance/site-settings/設定網站標題與 SEO.md",
    "設定前台語系與文字自定義": "docs/ec/website-appearance/site-settings/設定前台語系與文字自定義.md",
    "日本站官網需建立特定商取引法頁面": "docs/ec/website-appearance/site-settings/日本站官網需建立特定商取引法頁面.md",
    "設定快速到貨前台入口與專區": "docs/ec/website-appearance/setup-quick-delivery-frontend-entry.md",
    # Manual mappings for notfound items
    "(門市取貨)複製商品到門市": "docs/ec/products/copy-products-to-quick-delivery-stores.md",
    "贈品券規格": "docs/ec/marketing/coupon/gift-coupon-spec.md",
    "免運券規格": "docs/ec/marketing/coupon/free-shipping-coupon-spec.md",
    "使用會員篩選器": "docs/ec/members/member-filters-and-groups.md",
    "優惠券（碼）與紅利點數到期通知": "docs/ec/marketing/coupon-and-bonus-points-expiry-notification.md",
    "設定註冊禮": "docs/ec/marketing/setup-registration-gift.md",
    "【無法登入】登入後台時收不到Email驗證信 / 【資安防護宣導】": "docs/ec/website-management/not-receiving-backend-login-verification-email.md",
    "跨境電商退款流程": "docs/ec/orders/cross-border-refund-process.md",
    "Amazon FBA 跨境物流": "docs/ec/payments-and-logistics/amazon-fba-cross-border-logistics.md",
    "查看門市與個人業績報表": "docs/ec/app-market/storepal/view-sales-performance.md",
    "建立門市": "docs/ec/payments-and-logistics/create-stores.md",
    "Cyberbiz POS系統需求": "docs/pos/hardware/index.md",
    "庫存不足提醒": "docs/pos/check/low-stock-notifications.md",
    "盟立發票": "docs/pos/third-party/monolith-e-invoice.md",
    "POS機綁定機制": "docs/pos/check/sub-device-checkout-binding.md",
    "POS前台-登入教學": "docs/pos/store/staff-login.md",
    "POS前台-訂單作業": "docs/pos/orders/manage-general-orders.md",
    "POS前台-會員管理": "docs/pos/member/index.md",
    "POS前台自動登出設定": "docs/pos/store/setup-frontend-auto-logout-time.md",
    "小結關帳": "docs/pos/others/daily-closing.md",
    "POS 離線模式": "docs/pos/check/offline-checkout-mode.md",
    "互動遊戲(POS)": "docs/pos/check/customer-display-interactive-games.md",
    "POS LINEPAY掃碼支付": "docs/pos/check/line-pay-scan-payment.md",
    "有線刷卡機安裝教學": "docs/pos/hardware/taishin-wired-credit-card-machine.md",
    "EPSON TM-T82III 發票機安裝教學": "docs/pos/hardware/epson-wired-invoice-printer.md",
    "Posiflex發票機安裝教學": "docs/pos/hardware/posiflex-wired-invoice-printer.md",
    "POS網路連線過慢/斷線提示": "docs/pos/hardware/network-connection-exception-and-disconnection-prompts.md",
    "現貨、限量、預購銷售": "docs/wms/setup-products-stock-limit-preorder.md",
    "商家進倉規範": "docs/wms/merchant-inbound-operation-rules.md",
    "串接Google Pay": "docs/ec/payments-and-logistics/setup-google-pay.md",
    "申請iPASS MONEY 一卡通": "docs/ec/payments-and-logistics/setup-ipass-money.md",
    "澳洲落地版金流設定": "docs/ec/payments-and-logistics/australia-local-payment-services.md",
    "日本站金流設定": "docs/ec/payments-and-logistics/japan-payment-services.md",
    "北美站金流設定": "docs/ec/payments-and-logistics/north-america-payment-services.md",
    "東南亞站金流設定": "docs/ec/payments-and-logistics/southeast-asia-payment-services.md",
    "CYBERBIZ EXPRESS": "docs/ec/app-market/express/cyberbiz-express-japan-to-taiwan-delivery.md",
    "串接宅配貨到不付款/自訂物流": "docs/ec/payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md",
    "Step4.官網商品建立為蝦皮商品": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step4-create-shopee-products-from-site.md",
    "Step3.官網與蝦皮商品庫存同步": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step3-sync-inventory-with-shopee.md",
    "Step2.導入商品與建立關聯": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step2-import-products-and-link.md",
    "Step1.安裝啟用": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step1-install-and-activate.md",
    "第三方支付 : 人工退款": "docs/ec/orders/manual-refund-for-third-party-payment-orders.md",
    "Step5.官網與蝦皮商品資訊同步": "docs/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step5-sync-product-info-with-shopee.md",
    "綠界後台訂單查詢": "docs/ec/orders/ecpay-backend-order-query.md",
    "(CYBERBIZ NOW快速到貨)快速到貨運費計算與對帳": "docs/ec/orders/quick-delivery-shipping-fee-calculation-and-reconciliation.md",
    "會員退貨申請功能": "docs/ec/orders/member-return-request-feature.md",
    "指定物流送紅利": "docs/ec/marketing/send-bonus-points-for-specific-logistics.md",
    "(宅配物流託運單)補印與加印託運單": "docs/ec/payments-and-logistics/reprint-waybills.md",
    "串接宅配貨到付款物流": "docs/ec/payments-and-logistics/home-delivery-cash-on-delivery.md",
    "申請ezship超商物流(C2C)": "docs/ec/payments-and-logistics/integrate-ezship-cvs-pickup-c2c.md",
    "申請綠界金流與超商取貨付款": "docs/ec/payments-and-logistics/apply-for-ecpay-payment-and-cvs-cod.md",
    "指定商品送活動序號": "docs/ec/marketing/send-event-serials-for-specific-products.md",
    "指定商品送優惠券": "docs/ec/marketing/send-coupons-for-specific-products.md",
    "任選折扣": "docs/ec/marketing/mix-and-match-discounts.md",
    "紅利商城(POS)": "docs/pos/check/bonus-point-mall.md",
    "指定金流送紅利": "docs/ec/marketing/send-bonus-points-for-specific-payment-methods.md",
    "建立專屬VIP群組": "docs/ec/members/vip/create-exclusive-vip-groups.md",
    "建立全館VIP制度": "docs/ec/members/vip/setup-store-wide-vip-system.md",
    "VIP 功能運作指南": "docs/ec/members/vip/index.md",
    "批次匯入與編輯會員": "docs/ec/members/batch-import-and-edit-members.md",
    "會員客服系統": "docs/ec/members/member-customer-service-system.md"
}

# Add fuzzy matching
def find_match(name):
    if name in title_to_path:
        return title_to_path[name]
    
    # Try case-insensitive
    for title, path in title_to_path.items():
        if title.lower() == name.lower():
            return path
            
    # Try removing spaces
    name_no_space = name.replace(" ", "")
    for title, path in title_to_path.items():
        if title.replace(" ", "") == name_no_space:
            return path
            
    # Try partial match (if Name is in Title or vice versa)
    for title, path in title_to_path.items():
        if name in title or title in name:
            return path

    return None

notfound = []
updates = []

with open('workspace/wp-link/生產文件儀表板.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        if len(row) < 5: continue
        name = row[0]
        wp_reg_url = row[2]
        wp_ent_url = row[4]
        
        urls_from_csv = []
        if wp_reg_url:
            urls_from_csv.extend([u.strip() for u in wp_reg_url.split(',')])
        if wp_ent_url:
            urls_from_csv.extend([u.strip() for u in wp_ent_url.split(',')])
            
        # Filter out empty and non-url strings
        urls_from_csv = [u for u in urls_from_csv if u.startswith('http')]
        
        if not urls_from_csv:
            continue
            
        match_path = find_match(name)
        if not match_path:
            notfound.append(row)
            continue
            
        updates.append({
            'path': match_path,
            'urls': urls_from_csv
        })

# Write notfound.csv
with open('notfound.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(notfound)

# Print updates for the agent to process
import json
print(json.dumps(updates, ensure_ascii=False))
