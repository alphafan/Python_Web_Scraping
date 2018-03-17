# Post Request

import requests

url = 'http://pythonscraping.com/files/processing.php'
data = {'firstname': 'Yufan', 'lastname': 'Zheng'}

resp = requests.post(url, data)
print(resp.text)
