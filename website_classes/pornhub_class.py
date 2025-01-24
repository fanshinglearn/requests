import re
import requests
from bs4 import BeautifulSoup

class Pornhub:
    def __init__(self, url):
        matchs = re.search(r'^https://cn.pornhub.com/view_video.php\?viewkey=(.+)', url)
        if matchs:
            # 網址
            self.url = matchs.group(0)
            # 番號
            self.num = matchs.group(1)
            self._initialize_properties()
        else:
            raise ValueError('網址輸入錯誤')

    def _initialize_properties(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            # 標題
            self.title = soup.select_one('h1').text.strip()
            # 有時候有 有時候沒有 ._.?
            for count in range(1, 11):
                try:
                    # 縮圖網址
                    regex = r'"thumbnailUrl": "(https://di.phncdn.com/videos/.+\.jpg)",'
                    url_list = re.search(regex, str(soup))
                    self.thumbnail_url = url_list.group(1)
                    # 頻道
                    span = soup.select_one('span a.bolded')
                    self.channel = span.text
                    self.channel_url = f'https://cn.pornhub.com{span["href"]}'
                    break
                except:
                    print(f'找不到 pornhub 縮圖網址 重試第 {count} 次')
                    if count < 10:
                        r = requests.get(self.url)
                        soup = BeautifulSoup(r.text, 'html.parser')
                    else:
                        raise Exception('找不到縮圖')
            # 集數
            self.episode = None
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
            print(f'頻道\t： {self.channel}')
            print(f'頻道網址： {self.channel_url}')


if __name__ == '__main__':
    url = 'https://cn.pornhub.com/view_video.php?viewkey=ph617ec7501d933'
    # url = input('請輸入 Pornhub 網址： ')
    video = Pornhub(url)
    video.print_all()
