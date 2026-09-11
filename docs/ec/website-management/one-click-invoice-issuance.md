---
title: 一鍵開立請款發票
description: 了解如何啟用並使用一鍵開立請款發票功能。企業版商家透過串接星益欣帳戶，即可在對帳中心一鍵完成發票開立，大幅提升請款與撥款效率。
created: 2026-06-09 18:45
last_modified: 2026-06-12 14:40
lang: zh-TW
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules: 
  - 管理中心
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - 企業
cyb_extensions: []
intents: 
  - 設定一鍵開立請款發票
  - 如何開立請款發票
  - 串接星益欣帳戶
features: 
  - 一鍵開立請款發票
  - 星益欣帳戶串接
  - 對帳中心
prerequisites: 
  - "需為企業版方案商家"
  - "需由 CYBERBIZ 代為開立發票"
related:
  - pos/third-party/wixtar-e-invoice/
  - ec/website-management/auto-deduction-of-arrears/
tags: 
  - 請款發票
  - 星益欣
  - 對帳中心
  - 撥款流程
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 對帳中心
  - 請款發票設定
paths:
  - 管理中心 > 對帳中心
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=2196
permalink: "https://help.cyberbiz.io/ec/website-management/one-click-invoice-issuance/"
comments: false
search:
  exclude: false
icon: lucide/receipt
hide: []
---

# 一鍵開立請款發票
了解如何啟用並使用一鍵開立請款發票功能。企業版商家透過串接星益欣帳戶，即可在對帳中心一鍵完成發票開立，大幅提升請款與撥款效率。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 企業
{ .doc-badge }

!!! warning "適用對象限制"
    此功能僅適用於 **企業版方案** 且 **由 CYBERBIZ 代開消費者發票** 的商家。若您的企業版站台「自行開立消費者發票」，則不適用本文件之設定指引。


## 使用須知

- **前置條件**：必須完成 **星益欣帳戶串接** 方可使用一鍵開立功能。
- **功能限制**：星益欣對帳發票帳戶僅限用於開立 **對帳發票**。若想開立多通路發票，可透過後台升級至吃到飽方案。

    !!! info "星益欣吃到飽方案內容"	
        購買吃到飽方案後，系統除了支援開立對帳發票外，您亦可開立以下情境發票：

        |開立情境|開立發票位置|注意事項|
        |---|---|---|
        |**線下 POS 系統**|CYBERBIZ EC 後台|購買帳戶後，支援 2 台 POS 機開立發票。多台 POS 可參考 [POS 教學文件](../../pos/third-party/wixtar-e-invoice.md#方案收費方式) 了解子機計價方式與申請流程 |
        |**其他通路（第三方平台）**|星益欣後台|商家可進入星益欣後台操作，CYBERBIZ 不支援該操作流程教學 |

        > **注意** :lucide-triangle-alert: 以上情境皆以相同統編開立，若需開立不同統編發票，請分別購買方案。


## 啟用流程

### 步驟一：取得星益欣帳戶

根據您的系統購買時間，請參考對應的串接方式：

=== "2026/05/01 前購買系統"

    1. 登入 CYBERBIZ 管理後台，前往 **管理中心 > 對帳中心 > 對帳發票設定**。
    2. 在 **統一編號** 欄位輸入統編。
        
        ![](https://www.cyberbiz.io/support/wp-content/uploads/電子發票-美麗科技13.png){ .screenshot }

    3. 若尚未購買星益欣方案，請完成購買。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/電子發票-美麗科技14.png){ .screenshot }


    !!! tip "舊方案商家想升級方案？"
        2026/05/01 前購買系統的商家，若想升級至包含星益欣帳戶的方案規格，請洽詢 CYBERBIZ 客服人員。

=== "2026/05/01 後購買系統"

    1. 商家購買 CYBERIZ 系統方案並開通後，CYBERBIZ 會代為申請星益欣帳戶。
    
      - **對帳發票設定** 頁籤，會自動填入商家聯絡人資訊。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-商家資訊欄位01.png){ .screenshot }

    2. 待星益欣進入申請流程，**對帳單列表** 會顯示 **對帳發票設定提醒**。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-尚未啟用請款發票01.png){ .screenshot }
      
    3. 待電子郵件信箱收到星益欣通知信件。

        - 信件標題：#{統編}-#{公司名稱} 串接電子發票
    
    4. 根據信件引導登入星益欣後台，取得 **金鑰串接資訊**。


### 步驟二：串接金鑰

1. 進入星益欣加值中心後台，前往 **營業人資訊**，點選欲設定發票功能的 **POS機編碼**，點選 **下載**。

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技07.png){ .screenshot }

2. 複製以下欄位資訊：

    - 門市店碼
    - POS機碼
    - POS機序號(PID)
    - 認證碼(RID)
    - 產品名稱(PNAME)
    - AES KEY

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技08.png){ .screenshot }

3. 前往 **管理中心 > 對帳中心 > 對帳發票設定**，將金鑰資訊貼入對應欄位。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-請款發票串接欄位01.png){ .screenshot }



### 步驟三：設定公司發票章

登入星益欣後台，前往 **基本設定 > 圖片設定**，設定公司發票章的圖片。開立的發票明細上就會自動帶入發票章，不用手動蓋章。

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-美麗科技11.png){ .screenshot }


### 步驟四：開啟一鍵開立功能

=== "2026/05/01 前購買系統"

    前往 **管理中心 > 對帳中心**，點擊 **請款發票設定**，啟用請款發票。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票01.png){ .screenshot }


=== "2026/05/01 後購買系統"

    1. 前往 **管理中心 > 對帳中心**，點擊 **請款發票設定** 頁籤。
    2. 將 **啟用請款發票** 切換為 `開啟 (ON)`。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-開啟請款發票功能01.png){ .screenshot }

    #### 檢測功能設置狀態

    - **設置完成 / 已啟用**

        **請款發票設定** 自動移至左上角，點擊後功能為開啟狀態，且無法自行關閉，則串接成功。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-已啟用請款發票01.png){ .screenshot }

    - **尚未設置完成**

        當對帳單列表仍可看見 **對帳發票設定** 提醒，請檢查各項串接步驟，確保設定正確無誤。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-管理中心-對帳中心-尚未啟用請款發票01.png){ .screenshot }

    !!! warning "重要提醒"
        請務必完成星益欣帳戶串接，否則將無法查看每期撥款金額或下載對帳單。




## 發票開立流程

1. 每期帳款撥款前，前往 **管理中心 > 對帳中心**。
2. 確認該期帳款金額無誤後，點擊 **確認帳款**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票02.png){ .screenshot }

3. 系統將自動透過星益欣帳戶開立請款發票，並進入撥款週期。
4. 您可點擊 **請款發票** 按鈕，查看已開立的發票明細。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票03.png){ .screenshot }



## 發票開立規則

- **發票項目**：統一標示為 **商品一批**。
- **開立金額**：等同對帳單中不需折讓單之的 **應開立發票總額**。
> 應開立發票總額 = 發票開立方為 CYBERBIZ 之非票券訂單交易金額總和 + 票券核銷總金額 + 票券任選折扣價差退還

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票04.png){ .screenshot }

- **正值款項**：系統將開立 **請款發票**。
- **負值款項**：系統將開立 **折讓單**。


    !!! info "折讓單開立邏輯"
        折讓單將優先由 CYBERBIZ 開立。若折讓金額大於站台過往累積的對帳發票總額，則超出部分需由商家手動開立紙本折讓單，無法透過後台自動開立。

        如：當期發票總額為負 3 萬，過往對帳發票累計金額 2 萬，商家需要自行手開 3 萬的折讓單，恕無法透過後台開立折讓單。

## 常見問題

??? quote "如何查看折讓單明細？"
    前往 **對帳中心** 點擊 **折讓單** 按鈕，即可查看該期對應的折讓單詳細資訊。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自動開立請款發票07.png){ .screenshot }

??? quote "出現負值款項時如何處理？"
    若對帳金額為負值，請確保已開啟 [欠款自動扣繳](auto-deduction-of-arrears.md) 功能並綁定信用卡，系統方可自動扣繳欠款。



