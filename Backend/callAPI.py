import requests

name = 'linh'

url = 'http://127.0.0.1:5000/redirect'.format(name)

response = requests.get(url)

print(response.status_code)
print(response.text)
print(response.json())
