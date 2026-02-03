---
title: "CKEditor 編輯器教學"
module:
  - 網站設定
tasks:
  - 文章編輯器
type: guide
product:
  - EC
plans:
  - 專業
  - 進階
  - 高手
  - 企業
surfaces:
  - 商品 > 所有商品 > 商品管理 > 商品描述
  - 網站設定 > 頁面管理 > 活動頁
  - 網站設定 > 頁面管理 > 其他頁面
  - 部落格 > 文章管理
system:
  - 後台
lang: zh-TW
lang_twin:
sites: 台灣
status: draft
activ: configure
note:
  - 檢查圖片連結
  - 調整圖片尺寸與上傳限制的呈現方式
  - 整合注意事項到相關內容
---

# CKEditor 編輯器教學

在 CYBERBIZ 後台，使用 CKEditor 快速建立商品銷售頁、活動著陸頁及內容頁面。支援文字、圖片與影片上傳與排版，並提供操作指引與建議規格，確保頁面專業、一致，提升可讀性。

## 功能概述

*   **內容設計**：使用 CKEditor 設計商品頁、商品群組、活動頁（一頁商店）、定期定額、部落格及其他自訂頁面。
*   **多媒體上傳**：支援文字、圖片及影片上傳，並提供建議規格與操作指引。
*   **應用範圍**：廣泛應用於商品描述、規格說明、運送方式等後台編輯區塊。

## 使用情境

*   **建立銷售頁面**：設計具備豐富圖文與影片的商品銷售頁，提升顧客購買意願。
*   **優化著陸頁**：製作高轉換率的活動著陸頁，有效收集潛在客戶資訊。
*   **撰寫部落格文章**：透過圖文並茂的內容，分享品牌故事或產品知識。
*   **編輯商品資訊**：為商品添加詳細描述、規格說明及運送方式，提供完整資訊。

## 操作流程

### :material-format-text: 文字編輯

在 CKEditor 中編輯文字，所見即所得，可直接預覽前台顯示效果。

1.  登入 CYBERBIZ 電商後台，前往「商品」→「所有商品」→「商品名稱」→「商品描述」。

    [![CKEITOR-文字編輯器01](https://www.cyberbiz.io/support/wp-content/uploads/2022/01/CKEITOR-文字編輯器01-1.png)](https://www.cyberbiz.io/support/wp-content/uploads/2022/01/CKEITOR-文字編輯器01-1.png)

2.  **文字輸入**：直接在編輯器中輸入或貼上文字。
    *   若從其他文字軟體（如 Office）匯入，請使用 **純文字貼上** 按鈕，避免帶入其他語法導致跑版。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/CKEITOR-文字編輯器02.png)
3.  **進階設定**：如有錨點設定需求，可參考 [錨點教學影片](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/錨點設定.mp4)。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/CKEITOR-文字編輯器03.png)

### :material-image-multiple: 圖片上傳

#### 圖片尺寸與上傳限制

| 項目     | 限制說明                                     |
| :------- | :------------------------------------------- |
| 上傳總量 | 單次不得超過 2MB                             |
| 圖片寬度 | 最大 5000px，超過 1110px 會自動壓縮至 1110px |
| 圖片長度 | 不得超過 7000px                              |
| SEO 設定 | 可參考 [SEO 優化教學](https://www.cyberbiz.io/helpcenter/?p=3512) 進行設定             |

#### 長幅產品圖製作建議

您可以依需求選擇以下兩種方式製作長條產品圖：

=== ":material-image-area: 單張圖片（推薦）"
    *   **優點**：可避免拼接空隙問題。
    *   請控制檔案大小。
    *   **建議尺寸**：寬度 1000px，長度不限。

=== ":material-image-multiple-outline: 多張拼接圖"
    *   **優點**：各圖檔較小，利於上傳。
    *   請統一尺寸以達成無縫拼接效果。
    *   **建議尺寸**：每張寬度 1000px × 長度 1000px。

#### 個別/批次上傳

1.  可選擇透過 CKEditor 圖片按鈕逐一上傳，也可透過資料夾一次上傳圖片。

    === ":material-image-outline: 個別上傳"

        * 適合少量圖片
        * 可精確控制每張圖片位置

        ![影片-CKEditor圖片個別上傳](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/%E5%96%AE%E7%AD%86%E4%B8%8A%E5%82%B3%E5%9C%96%E7%89%87.mp4)

    === ":material-folder-multiple-outline: 批次上傳"

        * 適合大量圖片
        * 系統會依序排列圖片

        ![影片-CKEditor圖片批次上傳](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/%E6%89%B9%E6%AC%A1%E4%B8%8A%E5%82%B3%E5%BD%B1%E7%89%87.mp4)

2.  **前台畫面顯示**：
    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/CKEITOR-文字編輯器07.png)

#### 常見問題：圖片之間有空白格

=== ":material-alert-circle-outline: 原因"
    若逐一上傳圖片並在照片之間按下 ++enter++ 鍵，網頁顯示會多一行空白格。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/CKEITOR-文字編輯器09.png)

=== ":material-lightbulb-on-outline: 解決方案"
    1.  進入後台點選「原始碼」。
    2.  刪除圖片之間多餘的 `<p>` 標籤即可移除空白格。
        *   此解法僅能解決圖片可自動換行的情況。
        *   **範例 A**：兩張圖片寬度皆為 300 px，則無法透過程式碼將空白格刪除，圖片之間必有空白。
        *   **範例 B**：兩張圖片寬度皆為 1000 px，若圖片之間按下 ++enter++ 後，可利用程式碼來將空白格刪除。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/2022/01/CKEITOR-文字編輯器10.png)
    3.  設定完成。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/CKEITOR-文字編輯器08.png)

### :material-video: 影片上傳

1.  **影片相關設定**：請參考 [影片自動播放+特定播放時間](https://www.cyberbiz.io/support/?p=19650) 設定教學。
    ![](https://www.cyberbiz.io/support/wp-content/uploads/2022/01/CKEITOR-文字編輯器11.png)
2.  **前台畫面顯示**：
    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/CKEITOR-文字編輯器12.png)

## 常見問題

??? question "YouTube 嵌入影片後，後面的圖片及內文不見了？"

    === ":material-alert-circle-outline: 原因"
        圖片及內文被影片語法包住，導致下方內容無法顯示。

        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor13.png)
        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor14.png)

    === ":material-lightbulb-on-outline: 解決方法"
        點擊原始碼，將除了影片以外的 `<div>` 語法刪除。

        *   紅色框框部分刪除。
        *   藍色框框部分改成 `<p>` 及 `</p>`。
        *   只要是文字或圖片，前面都使用 `<p>` 語法。
        *   **注意**：影片前面（`<iframe` 前面）的 `<div>` 語法不可以拿掉。

        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor15.png)

??? question "YouTube 嵌入影片無法隨螢幕縮放，手機版會爆出去，或是顯示太小了？"

    === ":material-alert-circle-outline: 原因"
        YouTube 嵌入的影片被圖片或文字的 `<p>` 語法包住了。

        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor16.png)

    === ":material-lightbulb-on-outline: 解決方法"

        1.  請點擊原始碼。
        2.  將紅色框框的 `<p>` 改成 `<div class="embed-responsive embed-responsive-16by9">`。
        3.  將藍色框框的 `</p>` 改成 `</div>`。

        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor17.png)
        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor18.png)

??? question "商品頁面跑版或是編輯器內容預覽看不到（前台顯示正常）？"

    === ":material-alert-circle-outline: 原因"
        商品頁編輯器中的 `<style type="text/css">p, li { white-space: pre-wrap; } </style>` 語法導致跑版。

        *   通常比較常發生在從其他網站複製內容貼到編輯器時，因為會帶到其他網站的語法。

        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor19.png)
        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor22.png)

    === ":material-lightbulb-on-outline: 解決方法"

        1.  請點擊原始碼。
        2.  找到 `<style type="text/css">p, li { white-space: pre-wrap; } </style>` 的語法，刪除這段即可。

        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor20.png)
        ![](https://www.cyberbiz.co/support/wp-content/uploads/2020/04/CKEditor21.png)

## 延伸閱讀

- [[SEO 優化教學]]
- [[影片自動播放+特定播放時間]]
