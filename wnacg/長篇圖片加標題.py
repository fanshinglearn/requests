# 下載 wnacg 長篇漢化 n 頁 的 封面縮圖 存到 images/標題.jpg
# 檔名用標題命名

import requests
from bs4 import BeautifulSoup

# 每頁 20 本 page 頁
for page in range(1):

    # 長篇漫畫網址
    url = f'https://www.wnacg.com/albums-index-page-{page}-cate-9.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # 尋找title div 中德的 a 標籤
    titles = soup.select('div.title a')

    # 尋找圖片 div 中的 img 標籤
    sel = soup.select('div.pic_box img')

    for i in range(len(titles)):
        # 圖片標題
        title = titles[i]['title']

        # 圖片網址
        img_url = f'https:{sel[i]["src"]}'
        img = requests.get(img_url)

        # 按照標題存檔
        with open(f'images/{title}.jpg', 'wb') as file:
            file.write(img.content)
