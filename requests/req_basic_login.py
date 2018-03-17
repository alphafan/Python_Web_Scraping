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
