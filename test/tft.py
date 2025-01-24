import requests
from bs4 import BeautifulSoup
import json
import re

# 定義一個函式來清理掉非法控制字元
def clean_control_characters(s):
    return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', s)

def line_name(data):
    line_name = []
    for line_up in data['lineup_list']:
        detail_cleaned = clean_control_characters(line_up['detail'])
        detail = json.loads(detail_cleaned)
        line_name.append(detail['line_name'])
    return line_name

# 雲頂之奕!!
url = r'https://game.gtimg.cn/images/lol/act/tftzlkauto/json/lineupJson/s11/6/lineup_detail_total.json'
r = requests.get(url)
data = r.json()
soup = BeautifulSoup(r.text, 'html.parser')

old_filename = 'data/old_lineup_detail_total.json'
new_filename = 'data/new_lineup_detail_total.json'
with open(new_filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open(old_filename, 'r', encoding='utf-8') as f:
    old_data = json.load(f)

with open(new_filename, 'r', encoding='utf-8') as f:
    new_data = json.load(f)

if old_data == new_data:
    print('沒更新')
else:
    print('更新了?!')
    old_line_up = line_name(old_data)
    new_line_up = line_name(new_data)

    # 排名
    ranking = []
    for new in new_line_up:
        if new in old_line_up:
            old_ranking = old_line_up.index(new)
            new_ranking = new_line_up.index(new)
            ranking_change = old_ranking - new_ranking
            ranking.append(ranking_change)
        else:
            ranking.append('NEW')
    
    rips = [old for old in old_line_up if old not in new_line_up]

    for i in range(len(new_line_up)):
        print(f'{ranking[i]}\t{new_line_up[i]}')
    
    for rip in rips:
        print(f'RIP\t{rip}')
