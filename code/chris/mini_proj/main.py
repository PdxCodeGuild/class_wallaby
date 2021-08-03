import requests
import re

# search_input = input('What recipe would you like? ')
# search_input = search_input.split(' ')
# search_input = '+'.join(search_input)
search_input = 'roasted corn'


response = requests.get(f'https://www.google.com/search?q={search_input}+recipe')

data = response.text

data = re.split('(https://)|(&amp)|(\\x26)', data)

# print(type(data) is list)
# print(type(data[0]) is str)
# print(data[0])
# print(data[1])
# if data[0].startswith('<'):
#   print(data.pop(0))

for idx, item in reversed(list(enumerate(data))):

  if type(item) == str:
    if len(item) < 20 or item.startswith('<!') or item.startswith('maps.google') or item.startswith('www.google.com') or item.startswith('support') or item.startswith('www.google.com') or item.startswith('www.google.com') or item.startswith('accounts') or item.startswith('policies') or item.startswith('accounts') or item.startswith('https://') or item.startswith('en.wikipedia') or item.startswith('/&amp') or item.startswith(';') or item.startswith('&') or item.startswith('/') or item.startswith('(') or item.startswith('ime') or item.startswith('goog') or item.startswith('window.') or item.startswith('ei=') or item.startswith('a.') or item.startswith('b') or item.startswith('document') or item.startswith('c.') or item.startswith('f.') or item.startswith('V(') or item.startswith('null') or item.startswith('"') or item.startswith('0') or item.startswith('Number') or item.startswith('C;') or item.startswith('conn') or item.startswith('nbsp') or item.startswith('gt;') or item.startswith('#') or item.startswith('rt') or item.startswith('ima') or item.startswith('+') or item.startswith('W(') or item.startswith('Array') or item.startswith('!') or item.startswith('a[') or item.startswith('d.') or item.startswith('a!') or item.startswith('f<') or item.startswith('g.') or item.startswith('zx') or item.startswith('r(') or item.startswith('-1') or item.startswith('r.') or item.startswith('h.') or item.startswith('F.') or item.startswith('32') or item.startswith('13'):
      data.pop(idx)
  elif item == None:
    data.pop(idx)


google_results = {}
for item in data:
  google_results[item] = item

for item in google_results:
  print(item)
  print()
# with open('google_query.txt', 'wb') as file:
#   data = str(data)
#   data = data.encode('utf-8')
#   file.write(data)
#   file.close()


