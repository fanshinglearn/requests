import requests
from bs4 import BeautifulSoup

# 媒體報導
url = f'https://news.chu.edu.tw/p/403-1001-30-1.php?Lang=zh-tw'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# 日期
date = soup.select('div.d-txt i')
for d in date:
    print(d.text.strip())

# 標題 連結
aaa = soup.select('div.d-txt a')
for a in aaa:
    print(a.text.strip())
    print(a['href'])
