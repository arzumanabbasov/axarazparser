import requests
from bs4 import BeautifulSoup
import pandas as pd


class AxarAzParser:
    def __init__(self, base_dir):
        self.base_url = 'https://axar.az/'
        self.BASE_DIR = base_dir
        self.result = {'category': [], 'summary': [], 'article': []}

    def get_soup(self, url):
        request = requests.get(url)
        content = request.content
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def get_pages(self, url, n):
        res = [url + f'page{i}/' for i in range(2, n + 1)]
        res.insert(0, url)
        return res

    def get_news_urls(self, url):
        soup = self.get_soup(url)
        div = soup.find('div', {'class': 'newsPlace'})
        tables = div.find_all('table', {'id': 'catNews'})
        if not tables:
            return None, False
        news_urls = [table.find('a').get('href') for table in tables]
        return news_urls, True

    def get_news(self, url):
        soup = self.get_soup(url)
        span = soup.find('span', {"id": 'font_size', "class": 'article_body'})
        summary = span.find('strong').text
        article_text = ''.join([p.text for p in span.find_all('p')[1:]])
        return summary, article_text

    def scrape(self):
        soup = self.get_soup(self.base_url)
        menu_div = soup.find('div', {'class': 'menu1'})
        menu_li = menu_div.find_all('li')
        categories = {i.text: self.base_url + i.find('a').get('href') for i in menu_li}

        keys_to_remove = ['Gündəm', 'Yazarlar', 'Reportaj']
        for key in keys_to_remove:
            if key in categories:
                del categories[key]

        for category_name in categories.keys():
            print(category_name)
            category_url = categories[category_name]
            i = 1
            while True:
                page_url = category_url + f"page{i}/"
                news_urls, flag = self.get_news_urls(page_url)
                if not flag:
                    break
                for news_url in news_urls:
                    summary, article_text = self.get_news(news_url)
                    self.result['category'].append(category_name)
                    self.result['summary'].append(summary)
                    self.result['article'].append(article_text)
                i += 1

    def save_to_csv(self):
        df = pd.DataFrame(self.result)
        df.to_csv(self.BASE_DIR + "data.csv")

