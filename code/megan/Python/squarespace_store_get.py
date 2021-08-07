import requests

url = "https://api.squarespace.com/1.0/commerce/products?"

payload={}
headers = {
  'Authorization': 'Bearer 123abc',
  'User-Agent': 'Megan-postman'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
