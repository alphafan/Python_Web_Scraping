# Beautiful Soup Basic Usage Example

from bs4 import BeautifulSoup
from urllib.request import urlopen

# Use urlopen get web page content
# If Chinese, use decode 'UTF-8'
html = urlopen('http://www.github.io').read().decode('utf-8')
# print(html)

# Parsing the HTML to Beautiful Soup
soup = BeautifulSoup(html, features='lxml')

# To access the tag content
print('\nh1:', soup.h1)
print('\np:', soup.p)

# To access all tag content
all_link = soup.find_all('a')
print('\nLinks:', all_link)

# Access attribute of tag
all_href = [link['href'] for link in all_link]
print('\nHref:', all_href)
