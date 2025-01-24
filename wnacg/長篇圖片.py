# 下載 wnacg 長篇漢化 n 頁 的 封面縮圖 存到 images/count.jpg

import requests
from bs4 import BeautifulSoup

count = 1

# 每頁 20 本 page 頁
for page in range(1):

    # 長篇漫畫網址
    url = f'https://www.wnacg.com/albums-index-page-{page}-cate-9.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # 尋找圖片 div 中的 img 標籤
    sel = soup.select('div.pic_box img')
    
    for s in sel:
        # 圖片網址
        img_url = f'https:{s["src"]}'

        # 按照順序存檔
        img = requests.get(img_url)
        with open(f'images/{count}.jpg', 'wb') as file:
            file.write(img.content)
        count += 1
