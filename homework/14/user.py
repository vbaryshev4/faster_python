import requests

text = 'Hello+world.+Has+the+sun+risen+on+you+today%3F'

r = requests.post('http://127.0.0.1:5000/{}'.format(text))
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.text)

