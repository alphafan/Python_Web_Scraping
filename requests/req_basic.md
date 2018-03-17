## Python Requests Basic Usage

### Get

```python
# Get Request

import requests
import webbrowser

url = 'http://www.baidu.com/s'
params = {'wd': '网络爬虫'}

req = requests.get(url, params)
print(req.url)
webbrowser.open(req.url)
```

### POST

```python
# Post Request

import requests

url = 'http://pythonscraping.com/files/processing.php'
data = {'firstname': 'Yufan', 'lastname': 'Zheng'}

r = requests.post(url, data)
print(r.text)

```