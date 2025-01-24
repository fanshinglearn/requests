from wnacg_class import Wnacg
import json
import time


with open('wnacg_test_title_100.json', 'r', encoding='utf8') as jfile:
    title_data = json.load(jfile)

for num in range(10000, 10100):
    print(num)
    comic = Wnacg(num)
    comic_title = comic.title
    print(comic_title)
    title_data[num] = comic_title

    time.sleep(3)

with open('wnacg_test_title_100.json', 'w', encoding='utf8') as jfile:
    json.dump(title_data, jfile, ensure_ascii=False, indent=4)
    
