import re
import requests
from bs4 import BeautifulSoup

class Wnacg:
    def __init__(self, num):
        matchs = re.search(r'^\d+$', str(num))
        if matchs:
            # 番號
            self.num = num

            # 網址
            self.url = f'https://www.wnacg.com/photos-index-aid-{num}.html'
            self._initialize_properties()
        else:
            raise ValueError('番號輸入錯誤')

    def _initialize_properties(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            # 標題
            self.title = soup.select_one('h2').text

            # 縮圖網址
            self.thumbnail_url = f"https:{soup.select_one('div.asTBcell.uwthumb img')['src'][2:]}"

            # 分類
            # 語言
            label = soup.select('div.asTBcell.uwconn label')
            matchs = re.search(r'分類：(.+)(?:／| & )(.+)', label[0].text)

            if matchs.group(2) == 'CG畫集' or matchs.group(2) == 'Cosplay':
                self.classification = self.language
                self.language = None
            else:
                self.classification = matchs.group(1)
                self.language = matchs.group(2)

            # 長短篇
            self.length = '短篇' if '短篇' in self.classification else '單行本' if self.classification == '單行本' else None

            # 頁數
            matchs = re.search(r'頁數：(\d+)\w', label[1].text)
            self.page = int(matchs.group(1))
            
            # 標籤
            tags = soup.select('a.tagshow')
            self.tags = [int(tag.text) if tag.text.isdigit() else tag.text for tag in tags]
            
            # 是否存在
            self.is_exist = True

            # 格式化標題
            # self._title_teardown()

        except Exception:
            # 是否存在
            self.is_exist = False

            try:
                self.title = soup.select_one('div.title.title_c').text
            except Exception as e:
                raise Exception(f'預料之外的錯誤： {e}')
    
    def _title_teardown(self):
        # 格式化標題
        title_pattern = r'(?:\]|^)([^\[\(]{2,})'
        matchs = re.search(title_pattern, self.title)
        self.format_title = matchs.group(1).strip()

        # 無法處理 group(1) 最後的空格 都用 .strip()
        # 畫家
        artist_pattern = r'\[([^\]\(]+)\s?\(([^\)]+)\)\]'
        matchs = re.search(artist_pattern, self.title)
        self.artist = matchs.group(2).strip() if matchs else None
        self.artist_1 = matchs.group(1).strip() if matchs else None

        # 方括弧
        brackets_pattern = r'\[[^]\(]+\]'
        matchs = re.findall(brackets_pattern, self.title)
        self.brackets = [match.strip() for match in matchs] if matchs else None

        # 圓括弧
        parentheses_pattern = r'\(([^\)]*)\)[^]]'
        matchs = re.findall(parentheses_pattern, self.title)
        self.parentheses = [match.strip() for match in matchs] if matchs else None

    def __str__(self):
        return f'網址： {self.url}\n標題： {self.title}'

    def print_all(self):
        print(f'番號\t： {self.num}')
        print(f'網址\t： {self.url}')
        print(f'是否存在： {self.is_exist}')
        print(f'標題\t： {self.title}')
        if self.is_exist:
            print(f'縮圖網址： {self.thumbnail_url}')
            print(f'分類\t： {self.classification}')
            print(f'語言\t： {self.language}')
            print(f'長短篇\t： {self.length}')
            print(f'頁數\t： {self.page}')
            print(f'標籤\t： {self.tags}')

            # 格式化標題
            # print(f'新標題\t： {self.format_title}')
            # print(f'畫家\t： {self.artist}')
            # print(f'畫家_1\t： {self.artist_1}')
            # print(f'方括弧\t： {self.brackets}')
            # print(f'圓括弧\t： {self.parentheses}')


if __name__ == '__main__':
    # 沒有縮圖
    # comic = Wnacg(36708)

    comic = Wnacg(215120)
    comic.print_all()