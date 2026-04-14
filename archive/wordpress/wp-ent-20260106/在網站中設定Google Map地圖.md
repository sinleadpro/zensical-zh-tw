---
title: "在網站中設定Google Map地圖"
last_modified: ""
categories: [網站設定>前台介面,常見問題]
tags: []
permalink: "https://www.cyberbiz.io/support/?p=2801"
id: "2801"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/適用站別.png)
![](https://www.cyberbiz.io/support/wp-content/uploads/台灣站.png)
![](https://www.cyberbiz.io/support/wp-content/uploads/北美站.png)
**操作目錄：**

* 設定步驟
* 狀況題：前台預設文字為「公司地址」，若想改成「門市位置」或其他文字，要怎麼改？
* 狀況題：除了預設資訊外，想要顯示其他資訊要怎麼做？
注意事項:  

* 此功能**僅限預設版型** 使用。
* 此文件僅供參考， CYBERBIZ 恕不提供程式碼修改與教學服務，商家請謹慎操作。

📌 設定步驟

1. 先至Google Map上，打上想顯示的地址 → 點選「分享」→ 點選「嵌入地圖」→ 點選「複製 HTML」。  
![google map](https://www.cyberbiz.io/support/wp-content/uploads/2019/04/MAP2.png)

2. 進入 EC 後台，將複製的 HTML 碼貼上，並儲存設定，即可在前台顯示地圖。  
後台路徑 : 「網站外觀」→「套版主題管理」→「網站設定」→ 「客服中心」  

![google map](https://www.cyberbiz.io/support/wp-content/uploads/MAP11.png)  

3. 前台顯示畫面  
![google map](https://www.cyberbiz.io/support/wp-content/uploads/2019/04/MAP1.png)

* * *


📌 狀況題：前台預設文字為「公司地址」，若想改成「門市位置」或其他文字，要怎麼改？ 後台路徑 : 「網站外觀」→「套版主題管理」→「選擇操作」→
「CSS/HTML編輯器」  


1. 依畫面點選「CSS/HTML編輯器」。  
![google map](https://www.cyberbiz.io/support/wp-content/uploads/MAP12.png)  

2. 選擇「contact.liquid」，找到紅線顯示的此行，將紅框內的文字改為想顯示的文字，儲存設定後即可變更。  
![google map](https://www.cyberbiz.io/support/wp-content/uploads/MAP4.png)  

* * *


📌 狀況題：除了預設資訊外，想要顯示其他資訊要怎麼做？ 後台路徑 : 「網站外觀」→「套版主題管理」→「選擇操作」→ 「CSS/HTML編輯器」  


1. 依畫面點選「CSS/HTML編輯器」。  
![google map](https://www.cyberbiz.io/support/wp-content/uploads/MAP12.png)  

2. 選擇「contact.liquid」，找到標示的此行，將其中一段< li >至< /li >複製起來（反白部分）。  
![google map](https://www.cyberbiz.io/support/wp-content/uploads/MAP6.png)  

3. 將剛剛複製的段落，貼在< /ul >上方，並且將複製後的紅底線刪除（不要刪到原本紅底線的部分），直接填寫想要的資訊（如下方紅框處），儲存設定後即可變更。  
![google map](https://www.cyberbiz.io/support/wp-content/uploads/MAP7.png)  

* * *



