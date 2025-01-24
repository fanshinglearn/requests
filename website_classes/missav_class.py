import re
import requests
from bs4 import BeautifulSoup

class Missav:
    def __init__(self, url):
        matchs = re.search(r'^https://missav.com/(.+)', url)
        if matchs:
            # 網址
            self.url = matchs.group(0)
            # 番號
            self.num = matchs.group(1)
            self._initialize_properties()
        else:
            raise ValueError('網址輸入錯誤')

    def _initialize_properties(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        r = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            # 縮圖網址
            self.thumbnail_url = f'https://cdn82.akamai-content-network.com/{self.num}/cover.jpg?class=normal'
            # 標題
            spans = soup.select('div.text-secondary span')
            self.num = spans[3].text.replace('-UNCENSORED-LEAK', '')
            self.title = spans[5].text
            # 女優 (有的話會在第四行)
            if len(spans) > 6 and spans[6].text == '女優:':
                    text_secondary = soup.select('div.text-secondary')
                    models = text_secondary[4].select('a')
                    self.model = [model.text for model in models]
                    self.model_url = [model['href'] for model in models]
            else:
                self.model = None
                self.model_url = None
            # 集數
            self.episode = None
            # 簡圖網址
            self.thumbnail_side_url = None
            # 頻道
            self.channel = None
            self.channel_url = None
            # 是否存在
            self.is_exist = True
        except Exception as e:
            # print(e)
            # 是否存在
            self.is_exist = False
            try:
                self.title = soup.select_one('h1').text.strip()
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
            print(f'縮圖網址： {self.thumbnail_url}')
            print(f'女優\t： {self.model}')
            print(f'女優網址： {self.model_url}')


if __name__ == '__main__':
    url = 'https://missav.com/fsog018'
    # url = 'https://missav.com/mizd-304'
    # url = input('請輸入 Missav 網址： ')
    video = Missav(url)
    video.print_all()
