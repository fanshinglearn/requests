from bs4 import BeautifulSoup
import pandas as pd

# 設定你的HTML內容
import requests
from bs4 import BeautifulSoup

# 活動資訊
url = f'https://event.chu.edu.tw/ca/default.aspx'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table', {'id': 'GV1'})

output_rows = []

for table_row in table.findAll('tr'):
    row = []
    columns = table_row.findAll('td')
    
    for column in columns:
        row.append(column.text)
    output_rows.append(row)

del(output_rows[0])

for each_row in output_rows:
    time_text = each_row[2]
    
    time1 = time_text[2:18]
    print(time1)

    time2 = time_text[24:40]
    print(time2)

    print()
