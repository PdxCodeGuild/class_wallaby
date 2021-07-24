import requests
# from requests import api #https://realpython.com/python-requests/#getting-started-with-requests


from requests.exceptions import HTTPError 
for url in ['https://www.sec.gov/edgar/search-and-access']:
    try:
        #response.encoding = 'json'
        
        response = requests.get(url)
        # json_response = response.json()
        # repository = json_response['items'][0]
        # print(repository)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

print(response.apparent_encoding)
# print(response.url)

# api


#maybe building this out in Django would be better?