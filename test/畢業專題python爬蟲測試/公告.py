import requests
from bs4 import BeautifulSoup

# 全部公告
url = f'https://www1.chu.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_rcg_mstr&Nbr=273'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# 標題
titles = soup.select('div.mtitle a')
for title in titles:
    print(title.text.strip())

# 超連結
titles = soup.select('div.mtitle a')
for title in titles:
    print(title['href'])

# 日期
i = soup.select('i.mdate.after')
for j in i:
    print(j.text.strip())