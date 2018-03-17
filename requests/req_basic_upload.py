# Upload Requests

import requests

file = {'uploadFile': open('README.md', 'rb')}
resp = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
print(resp.text)
