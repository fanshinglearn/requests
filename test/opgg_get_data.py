# 爬取對戰資訊

import requests
import json

# 哥
# url = "https://lol-web-api.op.gg/api/v1.0/internal/bypass/summoners/tw/2KtkxfOatsf6pxMDNQoYeAjonaFOQd39UoO3q9Lt_jOQ9XdjpaklJ1Gj4w/most-champions/rank?game_type=SOLORANKED"
# 毛
url = "https://lol-web-api.op.gg/api/v1.0/internal/bypass/summoners/tw/kAUMc-mNpagwXioYpaRRWtJu9JYxYymfy2kICeyxNMlqciMmK6ES9qq-Sw/most-champions/rank?game_type=SOLORANKED"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://www.op.gg/",
    "Origin": "https://www.op.gg",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # 將資料寫入到 JSON 檔案
    with open("data/soloranked_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print("資料已儲存到 soloranked_data.json")
else:
    print("請求失敗，狀態碼:", response.status_code)

# 讀取 JSON 檔案
with open("data/soloranked_data.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# 在這裡處理讀取到的資料
win = data['data']['win']
lose = data['data']['lose']
winning_rate = win / (win + lose) * 100

print()
print(f'win: {win}')
print(f'lose: {lose}')
print(f'winning rate: {winning_rate:.2f} %')