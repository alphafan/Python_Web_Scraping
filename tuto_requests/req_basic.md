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
resp = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
print(resp.text)
```

### Login Request

```python
# Login Requests

import requests

# Login with data
data = {'username': 'Yufan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=data)
print(r.cookies.get_dict())

# Login with cookies
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

# Login with session (No need to pass cookies every time)
sess = requests.Session()
r = sess.post('http://pythonscraping.com/pages/cookies/welcome.php', data=data)
print(r.cookies.get_dict())
# !! No need to pass cookies here
r = sess.get('http://pythonscraping.com/pages/cookies/profile.php')
print(r.text)
```