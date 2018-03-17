# Get Request

import requests
import webbrowser

url = 'http://www.baidu.com/s'
params = {'wd': '网络爬虫'}

req = requests.get(url, params)
print(req.url)
webbrowser.open(req.url)
