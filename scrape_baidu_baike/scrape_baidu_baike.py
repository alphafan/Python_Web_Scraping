# Scrape Baidu Baike Website

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = 'https://baike.baidu.com'
# '/item/网络爬虫'
his = ['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB']

for i in range(20):

    url = base_url + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')

    # Find will return the first h1 tag
    print(i, soup.find('h1').get_text(), '\turl:', his[-1])

    # Find all sub urls
    sub_urls = soup.find_all('a', {'target': '_blank', 'href': re.compile('/item/(%.{2})+$')})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        his.pop()
