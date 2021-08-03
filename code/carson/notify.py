

# import requests

# response = requests.get('https://www.americanmuscle.com/corsa-mustang-xtreme-cat-back-exhaust-black-tips-21040blk.html')
# data = response.json()
# print(data)



import json
from urllib.request import urlopen

f = urlopen("https://www.americanmuscle.com/corsa-mustang-xtreme-cat-back-exhaust-black-tips-21040blk.html")
j = json.load(f)