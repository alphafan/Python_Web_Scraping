# Post Request

import requests

url = 'http://pythonscraping.com/files/processing.php'
data = {'firstname': 'Yufan', 'lastname': 'Zheng'}

r = requests.post(url, data)
print(r.text)
