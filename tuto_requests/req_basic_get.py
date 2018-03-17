# Get Request

import requests
import webbrowser

url = 'http://www.baidu.com/s'
params = {'wd': '网络爬虫'}

resp = requests.get(url, params)
print(resp.url)
webbrowser.open(resp.url)
