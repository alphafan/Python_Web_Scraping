# Beautiful Soup Extract By Regex

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen('http://morvanzhou.github.io/static/scraping/table.html').read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

# Find all tags with specific regex pattern (end with .jpg)
img_links = soup.find_all('img', {'src': re.compile('.*?\.jpg')})
for link in img_links:
    print(link)

# Find all website links with specific pattern (start with 'http')
web_links = soup.find_all('a', {'href': re.compile('http.*')})
for link in web_links:
    print(link)
