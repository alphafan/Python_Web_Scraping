# Scrape Baidu Baike Website

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = 'https://baike.baidu.com'
# '/item/网络爬虫' --> '/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
# https://www.url-encode-decode.com/
his = ['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB']
url = base_url + his[-1]
print(url)

html = urlopen(url).read().decode('utf-8')
print(html)
