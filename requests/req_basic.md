## Python Requests Basic Usage

### Get Request

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

### POST Request

```python
# Post Request

import requests

url = 'http://pythonscraping.com/files/processing.php'
data = {'firstname': 'Yufan', 'lastname': 'Zheng'}

r = requests.post(url, data)
print(r.text)
```

### Upload Request

```python
# Upload Requests

import requests

file = {'uploadFile': open('README.md', 'rb')}
resp = requests.post('http://pythonscraping.com/files/processing2.php', file)
print(resp.text)
```