# 神魔之塔新聞稿爬蟲測試

import requests
from bs4 import BeautifulSoup

url = f'https://towerofsaviors.com/category/新聞稿/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# 標題
h2s = soup.select('section.entry.entry-archive h2 a')
for h2 in h2s:
    print(h2.text.strip())

# 網址
for h2 in h2s:
    print(h2['href'])

# 縮圖網址
imgs = soup.select('article img')
for img in imgs:
    print(img['src'])
