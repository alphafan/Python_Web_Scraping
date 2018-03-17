# Multi Processing Scraping (Acceleration)

import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re

BASE_URL = 'https://www.youtube.com'


def crawl(url):
    """ Crawl website content from url

    Args:
        url: (str) -- Link to the page

    Returns:
        html: Page content
    """
    resp = urlopen(url)
    time.sleep(.1)
    return resp.read().decode('utf-8')


def parse(html):
    """ From fetched website content extract information

    Args:
        html: Website content

    Returns:
        title: Video title
        url: Link of current page
        page_urls: List of links that will link to another video
    """
    soup = BeautifulSoup(html, features='lxml')
    title = soup.find('h1', {'class': 'watch-title-container'}).get_text().strip()
    links = soup.find_all('a', {'href': re.compile('^/watch\?.*$'), 'title': re.compile('^.+$')})
    page_urls = [BASE_URL+link.get('href', '') for link in links]
    url = soup.find('meta', {'property': 'og:url'})['content']
    print(url, title)
    return title, url, page_urls


if __name__ == '__main__':
    # 《奔跑吧兄弟1》第1期 完整版：邓超李晨PK战神金钟国 RunningManS1 20141010 【浙江卫视官方超清1080P】
    page = crawl('https://www.youtube.com/watch?v=qqzVIqsy_KY')
    _, _, urls = parse(page)
