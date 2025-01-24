import requests
from bs4 import BeautifulSoup

# 活動資訊
# 沒整理過...
url = f'https://event.chu.edu.tw/ca/default.aspx'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.text)

# 標題
titles = soup.select('td.border-end a.text-decoration-none.text-success.fw-bold')
for title in titles:
    print(title.text.strip())

# 活動地點
locations = soup.select('td.fw-bold.border-end')
for location in locations:
    print(location.text.strip())


# 活動時間
times = soup.select('td.d-none.d-sm-table-cell')
for time in times:
    print(time.text.strip())

# 超連結
titles = soup.select('div.mtitle a')
for title in titles:
    print(title['href'])

# 日期
i = soup.select('i.mdate.after')
for j in i:
    print(j.text.strip())