# 刷新個人資料

import requests

# 我哥id: 2KtkxfOatsf6pxMDNQoYeAjonaFOQd39UoO3q9Lt_jOQ9XdjpaklJ1Gj4w

# 哥
# url = "https://lol-web-api.op.gg/api/v1.0/internal/bypass/summoners/tw/2KtkxfOatsf6pxMDNQoYeAjonaFOQd39UoO3q9Lt_jOQ9XdjpaklJ1Gj4w/renewal"

# 毛
url = "https://lol-web-api.op.gg/api/v1.0/internal/bypass/summoners/tw/kAUMc-mNpagwXioYpaRRWtJu9JYxYymfy2kICeyxNMlqciMmK6ES9qq-Sw/renewal"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Length": "0",
    "Origin": "https://www.op.gg",
    "Referer": "https://www.op.gg/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.post(url, headers=headers)

if response.status_code == 200:
    print("成功！")
    print("響應文本：", response.text)
else:
    print("請求失敗，狀態碼：", response.status_code)
