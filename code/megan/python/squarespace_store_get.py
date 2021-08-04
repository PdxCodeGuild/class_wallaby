import requests

url = "https://api.squarespace.com/1.0/commerce/products?"

payload={}
headers = {
  'Authorization': 'Bearer 1e3d168a-4402-455e-a97e-1afdb94986a6',
  'User-Agent': 'Megan-postman'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
