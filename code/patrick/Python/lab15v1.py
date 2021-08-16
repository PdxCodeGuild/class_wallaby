import requests



response = requests.get('https://favqs.com/api/qotd')
#print(response.apparent_encoding)
dict_1 = response.json()
print(dict_1)
author = dict_1['quote']['author'] #it is a dictionary nested within another dictionary 
quote = dict_1['quote']['body']
print(f'Author: {author}\nQuote: {quote}')