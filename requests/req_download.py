# Download Requests

from urllib.request import urlretrieve
import requests

# The link to download random image
img_width = 640
img_height = 480
img_url = 'http://lorempixel.com/{}/{}/'.format(img_width, img_height)

# Method 1: Download with url retrieve
urlretrieve(img_url, 'img_1.png')

# Method 2: Use requests
r = requests.get(img_url)
with open('img_2.png', 'wb') as f:
    f.write(r.content)

# Method 3: Download chunk by chunk
r = requests.get(img_url, stream=True)
with open('img_3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
