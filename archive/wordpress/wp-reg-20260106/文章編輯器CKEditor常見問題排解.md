---
title: "文章編輯器CKEditor常見問題排解"
last_modified: ""
categories: [商品>商品上架/管理,網站設定,訂單]
tags: []
permalink: "https://www.cyberbiz.io/helpcenter/?p=1330"
id: "1330"
---

CKEditor的使用TIP  
1.圖片上圖的方式  
step1. 點擊圖片按鈕  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor1.png) step2. 點擊瀏覽伺服器  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor2.png) step3. 點擊上傳按鈕，上傳圖片(圖片上傳限制:2mb/每次上傳量)  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor3.png)
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor4.png) step4.
點擊剛剛上傳的圖片，設定圖片寬度為100%，高度留白，對齊方式不用設定  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor5.png)
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor6.png) step5. 若要批量上傳圖片，請拖拉資料夾檔案至編輯器內部空白處。
![CKEditor](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/批量上傳.gif)

2.嵌入Youtube的方式  
step1. 點擊Youtube按鈕  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor8.png) step2. 貼上youtube的連結  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor9.png) 完成(前台畫面)  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor10.png) 3.Youtube影片後面要插入圖片的方式  
因youtube影片有自己的div語法，若直接enter鍵換行的話，下面加入的內容會帶到影片語法，有可能會有影片與圖片/內文中間有大間隔，或是圖片被影片語法包住...等問題。  
step1. 滑鼠移到youtube下方，編輯器底部，就會跑出紅色的虛線換行線，點擊右方換行鍵換行  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor11.png) 完成. 紅色虛線換行之後，下方加入的圖片或文字就不會被影片語法包住囉！  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor12.png)

_Q 1  _youtube嵌入的影片，後面的圖片及內文不見了？  
原因:因為圖片及內文被影片語法包住，導致下方內容無法顯示。  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor13.png)
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor14.png) _A 1  _  
點擊原始碼，將除了影片以外的<div>語法刪除  
※紅色框框刪除  
※藍色框框改成<p> 及 </p>  
只要是文字或是圖片，前面都使用p語法 注意:影片前面( < iframe >前面) 的< div > 語法不可以拿掉喔！
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor15.png)

_Q 2  _youtube嵌入的影片無法隨螢幕縮放，手機版會爆出去，或是顯示太小了  
原因:因為youtube嵌入的影片被圖片或是文字的語法 <p>包住了  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor16.png) _A 2  _  
1\. 請點擊原始碼  
2\. 將紅匡的 <p> 改成 <div class="embed-responsive embed-responsive-16by9">  
3\. 藍匡的 </p> 改成 </div>  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor17.png)
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor18.png)

_Q 3  _商品頁面跑版  
原因:因為商品頁編輯器中的 <style type="text/css">p, li { white-space: pre-wrap; } <
/style> 語法導致跑版  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor19.png) _A 3  _  
1\. 請點擊原始碼  
2\. 找到 <style type="text/css">p, li { white-space: pre-wrap; } < /style >
的語法，刪掉這段即可  
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor20.png)
![CKEditor](https://www.cyberbiz.co/helpcenter/wp-content/uploads/2019/10/CKEditor21.png)

