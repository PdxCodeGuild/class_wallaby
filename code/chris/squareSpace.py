from keys import squareSpace_API_key as key
import requests, json

headers = {
  'Authorization': f'Bearer {key}',
  'User-Agent': 'Chrish',
  'Content-Type': 'application/json'
}
payload = {}

def view_product(id):
  url = f"https://api.squarespace.com/1.0/commerce/products/{id}"
  http_method = 'GET'
  response = requests.request(http_method, url, headers=headers)
  return response.json()

def create_product_data():
  product_name = input('input product name: ')
  product_desc = input('input product description: ')
  sku = input('input product sku: ')
  price = input('product currency value: ')

  data = json.dumps({
  "type": "PHYSICAL",
  "storePageId": "6100bd69c9f97105f4fc7fd6",
  "name": product_name,
  "description": product_desc,

  "tags": [
    "artisanal",
    "steak"
  ],
  "isVisible": True,
  "variantAttributes": [
    "flavor"
  ],
  "variants": [
    {
      "sku": sku,
      "pricing": {
        "basePrice": {
          "currency": "USD",
          "value": price
        },
      },
      "stock": {
        "quantity": 10,
        "unlimited": False
      },
      "attributes": {
        "flavor": "Habanero"
      },
      "shippingMeasurements": {
        "weight": {
          "unit": "POUND",
          "value": 2
        },
        "dimensions": {
          "unit": "INCH",
          "length": 7,
          "width": 5,
          "height": 5
        }
      }
    }
  ]
})
  return data


while True:
  payload = {}
  main_input = input('''
    1)Show all products
    2)View a product
    3)Update a product
    4)Add a new product
    5)Delete a product
  ''')

  if main_input == '1':
    url = "https://api.squarespace.com/1.0/commerce/products"
    http_method = 'GET'
  elif main_input == '2':
    prod_id = input('\nEnter product ID ')
    url = f"https://api.squarespace.com/1.0/commerce/products/{prod_id}"
    http_method = 'GET'
  elif main_input == '3':
    prod_id = input('\nEnter product ID ')
    data = view_product(prod_id)
    print(data['products'][0]['name'])
    update_input = input('''
      1)Update product name

    ''')
    if update_input == '1':
      name_attr = data['products'][0]['name']
      new_product_name = input('\nEnter new product name: ')
      http_method = 'POST'
      url = f"https://api.squarespace.com/1.0/commerce/products/{prod_id}"
      payload = json.dumps({
        "name": new_product_name
      })

  elif main_input == '4':
    http_method = 'POST'
    url = 'https://api.squarespace.com/1.0/commerce/products/'
    payload = create_product_data()
    print(payload)
  elif main_input == '5':
    prod_id = input('\nEnter product ID ')
    http_method = 'DELETE'
    url = f"https://api.squarespace.com/1.0/commerce/products/{prod_id}"


  response = requests.request(http_method, url, headers=headers, data=payload)
  print(response.text)
  if response.status_code >= 200 or response.status_code <= 299:
    print('\noperation successful!')
