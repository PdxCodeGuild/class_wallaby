#students = ('julio' ,'megan' , 'carson')
#f#or student in students:
    #print(student.capitalize())

#from random import choice 
# from colorama import init, Fore

# init()

# colors = [
# Fore.BLACK,
# Fore.RED,
# Fore.GREEN,
# Fore.YELLOW,
# Fore.BLUE
    
# ]
# def random_color():
#     return choice (colors)

# print(random_color())


import requests
import json

url = "https://api.squarespace.com/1.0/commerce/products/6100dcb594912f704504e291"

payload = json.dumps({
  "type": "PHYSICAL",
  "storePageId": "5d7ba084a63ee8bb410ce0b1",
  "name": "Artisanal Steak Dry Rub",
  "description": "Absolutly mouth watering expolosion of flavor that will make you slap your mama!",
  "isVisible": True,
  "variantAttributes": [
    "flavor"
  ],
  "variants": [
    {
      "sku": "SQ0557856",
      "pricing": {
        "basePrice": {
          "currency": "USD",
          "value": "12.95"
        }
      }
    },
    {
      "attributes": {
        "flavor": "Habanero"
      },
      "weight": {
        "unit": "POUND",
        "value": 2
      },
      "unit": "INCH",
      "length": 7,
      "width": 5,
      "height": 5
    }
  ]
})
headers = {
  'Authorization': 'Bearer edaa08c1-cca4-4193-a1e2-f114149e1b48',
  'User-Agent': 'Gamerboy',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
