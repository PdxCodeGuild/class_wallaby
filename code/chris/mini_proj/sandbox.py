import requests

response = requests.request('GET', 'https://www.thechunkychef.com/family-favorite-baked-mac-and-cheese/')
data = response.text
data = data.split('Ingredients')

for idx, item in reversed(list(enumerate(data))):
  if item.startswith('<'):
    data.pop(idx)


with open('data.txt', 'wb') as file:
  data = str(data)
  data = data.encode('utf-8')
  file.write(data)
  file.close()