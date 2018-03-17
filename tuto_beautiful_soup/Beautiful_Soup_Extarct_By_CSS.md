## Beautiful Soup Extract By CSS Class

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.github.io').read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

# Find all tags with specific class 'full-size'
images = soup.find_all('img', {'class': 'full-size'})
for image in images:
    print(image)
```