# CYB DOC (zh-TW)

Documentation site for the CYB patform. 

## Information Architecture

``` mermaid
graph TD
    %% Top level: Product lines
    A[品牌官網] --> B1[商品管理]
    A --> B2[支付金流]
    A --> B3[會員管理]

    C[智慧倉儲] --> D1[倉儲管理]
    E[智能 POS] --> F1[POS 管理]
    G[門市助理] --> H1[門市管理]
    I[資源中心] --> 1[更新紀錄]
    I[資源中心] --> J2[詞彙表] 
    I[資源中心] --> J3[慣例] 

    %% Docs container under each module
    B1 --> B1_docs[文件]
    B2 --> B2_docs[文件]
    B3 --> B3_docs[文件]
    D1 --> D1_docs[文件]
    F1 --> F1_docs[文件]
    H1 --> H1_docs[文件]

    %% Individual doc categories under Docs container
    B1_docs --> B1_doc1[使用須知]
    B1_docs --> B1_doc2[操作流程]
    B1_docs --> B1_doc3[常見問題]
    B1_docs --> B1_doc4[延伸閱讀]

```

