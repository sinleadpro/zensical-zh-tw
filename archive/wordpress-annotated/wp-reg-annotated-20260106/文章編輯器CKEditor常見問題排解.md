【文件標題】文章編輯器CKEditor常見問題排解
【適用版本】基本版
【來源連結】https://www.cyberbiz.io/helpcenter/?p=1330
【章節路徑】文章編輯器CKEditor常見問題排解

---

CKEditor的使用TIP
1.圖片上圖的方式
step1. 點擊圖片按鈕
[圖片說明：CKEditor] step2. 點擊瀏覽伺服器
[圖片說明：CKEditor] step3. 點擊上傳按鈕，上傳圖片(圖片上傳限制:2mb/每次上傳量)
[圖片說明：CKEditor]
[圖片說明：CKEditor] step4.
點擊剛剛上傳的圖片，設定圖片寬度為100%，高度留白，對齊方式不用設定
[圖片說明：CKEditor]
[圖片說明：CKEditor] step5. 若要批量上傳圖片，請拖拉資料夾檔案至編輯器內部空白處。
[圖片說明：CKEditor]

2.嵌入Youtube的方式
step1. 點擊Youtube按鈕
[圖片說明：CKEditor] step2. 貼上youtube的連結
[圖片說明：CKEditor] 完成(前台畫面)
[圖片說明：CKEditor] 3.Youtube影片後面要插入圖片的方式
因youtube影片有自己的div語法，若直接enter鍵換行的話，下面加入的內容會帶到影片語法，有可能會有影片與圖片/內文中間有大間隔，或是圖片被影片語法包住...等問題。
step1. 滑鼠移到youtube下方，編輯器底部，就會跑出紅色的虛線換行線，點擊右方換行鍵換行
[圖片說明：CKEditor] 完成. 紅色虛線換行之後，下方加入的圖片或文字就不會被影片語法包住囉！
[圖片說明：CKEditor]

_Q 1  _youtube嵌入的影片，後面的圖片及內文不見了？
原因:因為圖片及內文被影片語法包住，導致下方內容無法顯示。
[圖片說明：CKEditor]
[圖片說明：CKEditor] _A 1  _
點擊原始碼，將除了影片以外的語法刪除
※紅色框框刪除
※藍色框框改成 及
只要是文字或是圖片，前面都使用p語法 注意:影片前面( 前面) 的 語法不可以拿掉喔！
[圖片說明：CKEditor]

_Q 2  _youtube嵌入的影片無法隨螢幕縮放，手機版會爆出去，或是顯示太小了
原因:因為youtube嵌入的影片被圖片或是文字的語法 包住了
[圖片說明：CKEditor] _A 2  _
1\. 請點擊原始碼
2\. 將紅匡的  改成
3\. 藍匡的  改成
[圖片說明：CKEditor]
[圖片說明：CKEditor]

_Q 3  _商品頁面跑版
原因:因為商品頁編輯器中的 p, li { white-space: pre-wrap; }  語法導致跑版
[圖片說明：CKEditor] _A 3  _
1\. 請點擊原始碼
2\. 找到 p, li { white-space: pre-wrap; }
的語法，刪掉這段即可
[圖片說明：CKEditor]
[圖片說明：CKEditor]