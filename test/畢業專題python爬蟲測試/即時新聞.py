import requests
from bs4 import BeautifulSoup

# 即時新聞
url = f'https://news.chu.edu.tw/p/403-1001-14-1.php?Lang=zh-tw'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# 圖片網址
img = soup.select('div.d-img img')
for i in img:
    print(f'https://news.chu.edu.tw/{i["src"]}')

# 日期
date = soup.select('div.d-txt i')
for d in date:
    print(d.text.strip())

# 標題 連結
aaa = soup.select('div.d-txt a')
for a in aaa:
    print(a['href'])
    print(a.text.strip())

# 簡介
mdetail = soup.select('div.mdetail')
for m in mdetail:
    print(m.text.strip())
