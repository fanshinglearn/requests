import re
import requests
from bs4 import BeautifulSoup

class Hanime1:
    def __init__(self, url):
        matchs = re.search(r'^https://hanime1.me/watch\?v=(\d+)', url)
        if matchs:
            # 網址
            self.url = matchs.group(0)
            # 番號
            self.num = int(matchs.group(1))
            self._initialize_properties()
        else:
            raise ValueError('網址輸入錯誤')

    def _initialize_properties(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        r = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            # 標題
            self.title = soup.select_one('h3').text
            # 集數
            description = soup.select('div.video-description-panel.video-description-panel-hover.no-select div')
            self.episode = description[1].text
            # 縮圖網址
            self.thumbnail_url = soup.select_one('video')['poster']
            # 頻道
            a = soup.select('div.video-details-wrapper.desktop-inline-mobile-block a')   
            self.channel = a[1].text.strip()
            self.channel_url = a[1]['href']
            # 簡圖網址
            self.thumbnail_side_url = None
            # 女優
            self.model = None
            self.model_url = None
            # 是否存在
            self.is_exist = True
        except Exception as e:
            # print(e)
            # 是否存在
            self.is_exist = False
            try:
                self.title = soup.select_one('div.code').text.strip()
            except Exception:
                raise Exception(f'預料之外的錯誤： {e}')
    
    def __str__(self):
        return f'網址： {self.url}\n標題： {self.title}'

    def print_all(self):
        print(f'標題\t： {self.title}')
        print(f'是否存在： {self.is_exist}')
        print(f'網址\t： {self.url}')
        print(f'番號\t： {self.num}')
        if self.is_exist:
            print(f'集數\t： {self.episode}')
            print(f'縮圖網址： {self.thumbnail_url}')
            print(f'頻道\t： {self.channel}')
            print(f'頻道網址： {self.channel_url}')


if __name__ == '__main__':
    url = 'https://hanime1.me/watch?v=12985'
    # url = 'https://hanime1.me/watch?v=13779'
    # url = 'https://hanime1.me/watch?v=37908'
    # url = input('請輸入 Hanime1 網址： ')
    video = Hanime1(url)
    video.print_all()
