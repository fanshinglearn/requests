# BUG 有些網址完全空白
import re
import requests
from bs4 import BeautifulSoup

class Xvideos:
    def __init__(self, url):
        matchs = re.search(r'^https://www.xvideos.com/video(\d+)/', url)
        if matchs:
            # 網址
            self.url = f'{matchs.group(0)}_'
            # 番號
            self.num = int(matchs.group(1))
            self._initialize_properties()
        else:
            raise ValueError('網址輸入錯誤')

    def _initialize_properties(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            # 標題
            h2 = soup.select_one('h2')
            matchs = re.search(r'(.*)\s(\d+\s(s|m|h))', h2.text)
            self.title = matchs.group(1)
            # 時長
            # self.length = matchs.group(2)
            # 縮圖網址
            regex = r"setThumb(?:Url169|Slide)\('(https://)(.+)(\.xvideos-cdn\.com/videos/thumbs169)(lll|poster|)(.+\.jpg)'\);"
            url_list = re.findall(regex, str(soup))
            ## 大到小 poster > lll > ll > l > None
            thumbnail_url = url_list[0]
            self.thumbnail_url = f'{thumbnail_url[0]}img-egc{thumbnail_url[2]}lll{thumbnail_url[4]}'
            # 簡圖網址
            thumbnail_side_url = url_list[1]
            self.thumbnail_side_url = f'{thumbnail_side_url[0]}img-egc{thumbnail_side_url[2]}{thumbnail_side_url[4]}'
            # 頻道
            spans = soup.select('span.name')
            if len(spans) >= 1:
                self.channel = spans[0].text
                channel_href = soup.select_one('a.btn.btn-default.label.main.uploader-tag')['href']
                self.channel_url = f'https://www.xvideos.com{channel_href}'
            else:
                self.channel = None
                self.channel_url = None
            # 女優
            if len(spans) >= 2:
                self.model = [span.text for span in spans]
                self.model.pop(0)
                model_hrefs = soup.select('a.btn.btn-default.label.profile.is-pornstar')
                self.model_url = [f'https://www.xvideos.com{model_href["href"]}' for model_href in model_hrefs]
            else:
                self.model = None
                self.model_url = None
            # 集數
            self.episode = None
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
            print(f'簡圖網址： {self.thumbnail_side_url}')
            print(f'頻道\t： {self.channel}')
            print(f'頻道網址： {self.channel_url}')
            print(f'女優\t： {self.model}')
            print(f'女優網址： {self.model_url}')


if __name__ == '__main__':
    url = 'https://www.xvideos.com/video67241501/tifa_tit_fuck_-_final_fantasy_7'
    # url = 'https://www.xvideos.com/video28349679/stepdaughter_karlie_brooks_wakes_her_stepdad_up_for_fucking_while_stepmom_naps'
    # url = input('請輸入 Xvideos 網址： ')
    video = Xvideos(url)
    video.print_all()
