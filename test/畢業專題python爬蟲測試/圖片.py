import requests
from bs4 import BeautifulSoup

# 圖片
# 沒整理過...
url = f'https://www1.chu.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_sz_mstr&Nbr=9'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup)
# 圖片網址
img = soup.select('img')
a = soup.select('a')
print(len(a))
# for i in img:
#     print(f'https://www1.chu.edu.tw{i["src"]}')

for j in a:
    print(j['href'])
#     print(f'https://news.chu.edu.tw/{i["src"]}')

# # 日期
# date = soup.select('div.d-txt i')
# for d in date:
#     print(d.text.strip())

# # 標題 連結
# aaa = soup.select('div.d-txt a')
# for a in aaa:
#     print(a['href'])
#     print(a.text.strip())

# # 簡介
# mdetail = soup.select('div.mdetail')
# for m in mdetail:
#     print(m.text.strip())
