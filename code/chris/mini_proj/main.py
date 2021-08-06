import requests
import re

google_results = {}
url_list = []
current_scrape_url = ''
url_input = ''

search_input = input('\nWhat recipe would you like? ')
search_input = search_input.split(' ')
search_input = '+'.join(search_input)
print()

response = requests.get(f'https://www.google.com/search?q={search_input}+recipe')

data = response.text

data = re.split('(https://)|(&amp)|(\\x26)|(x26)', data)


for idx, item in reversed(list(enumerate(data))):

  if type(item) == str:
    if len(item) < 20 or len(item) > 500 or item.startswith('<!') or item.startswith('maps.google') or item.startswith('www.google.com') or item.startswith('support') or item.startswith('www.google.com') or item.startswith('www.google.com') or item.startswith('accounts') or item.startswith('policies') or item.startswith('accounts') or item.startswith('https://') or item.startswith('en.wikipedia') or item.startswith('/&amp') or item.startswith(';') or item.startswith('&') or item.startswith('/') or item.startswith('(') or item.startswith('ime') or item.startswith('goog') or item.startswith('window.') or item.startswith('ei=') or item.startswith('a.') or item.startswith('b') or item.startswith('document') or item.startswith('c.') or item.startswith('f.') or item.startswith('V(') or item.startswith('null') or item.startswith('"') or item.startswith('0') or item.startswith('Number') or item.startswith('C;') or item.startswith('conn') or item.startswith('nbsp') or item.startswith('gt;') or item.startswith('#') or item.startswith('rt') or item.startswith('ima') or item.startswith('+') or item.startswith('W(') or item.startswith('Array') or item.startswith('!') or item.startswith('a[') or item.startswith('d.') or item.startswith('a!') or item.startswith('f<') or item.startswith('g.') or item.startswith('zx') or item.startswith('r(') or item.startswith('-1') or item.startswith('r.') or item.startswith('h.') or item.startswith('F.') or item.startswith('32') or item.startswith('13') or item.startswith('amp;') or item.startswith('var') or item.startswith('www.youtube') or item.startswith('youtu.be') or item.startswith('13') or item.startswith('ust'):
      data.pop(idx)
    if item.endswith('.jpeg') or item.endswith('.jpg') or item.endswith('.gif') or item.endswith('.html'):
      data.pop(idx)
  elif item == None:
    data.pop(idx)

for url in data:
  google_results[url] = url

for idx, url in enumerate(google_results):
  print(f'{idx + 1}) ', url)
  print()
  url_list.append(url)

url_input = int(input('\nSelect which url to scrape from by entering URL: '))
url = url_list[url_input - 1]

if url.startswith('www.foodnetwork.com'):

  response = requests.get(f'https://{url}')
  print(url)

  data = response.text
  data = re.split('(<span class="o-Ingredients__a-Ingredient--CheckboxLabel">)|(</span>)', data)

  for idx, item in reversed(list(enumerate(data))):
    if item == None:
      data.pop(idx)
    else:
      data[idx] = item.strip()
      if len(item) > 500 or len(item) < 9 or '<span' in item or item.startswith('Deselect'):
        data.pop(idx)


  data = '#'.join(data)
  print(data)

  data = re.split('(<)|(#)', data)

  for idx, item in reversed(list(enumerate(data))):
    if item == None:
      data.pop(idx)
    elif item.startswith('/p') or item.startswith('/label') or len(item) < 7 or item.startswith('/') or item.startswith('p c') or item.startswith('label') or item.startswith('input ') or item.startswith('span'):
      data.pop(idx)
    # input('enter')



  with open('food_network_results.txt', 'wb') as file:
    fillstr = '\n'
    for idx, item in enumerate(data):
      file.write(item.encode('utf-8'))
      file.write(fillstr.encode('utf-8'))
  file.close()


else:
  print('\nScraping for that website does not exist')


# with open('google_query.txt', 'wb') as file:
#   google_results = str(google_results)
#   google_results = google_results.encode('utf-8')
#   file.write(google_results)
#   for item in google_results:
#     file.write(item.encode('utf-8'))
#     file.write(', '.encode('utf-8'))
#   file.close()


