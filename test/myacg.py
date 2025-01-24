# myacg 商品標題

import requests
from bs4 import BeautifulSoup

count = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

for id in range(4430293, 4430300):

    url = f'https://www.myacg.com.tw/goods_detail.php?gid={id}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    h1 = soup.select('title')

    if h1:
        print(h1[0].text)
    else:
        print('無')
