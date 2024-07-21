# NTU-COOL-comments-crawler
爬取 NTU COOL 課程投影片與影片底下的留言（助教專用）

下載相關 python 套件後，輸入 course_id、帳號密碼、存取目標(影片/投影片) 後，會將此課程的所有學生留言存到 csv 檔中。

註1：course_id 即為 COOL 網址的課程編號 (https://cool.ntu.edu.tw/courses/<course_id>)
註2：若 csv 出現亂碼，使用 excel utf-8 格式讀取即可解決

已知 issue：若留言包含圖片或數學式，無法成功解析
