import requests
import json

url = "https://api.squarespace.com/1.0/commerce/products/"

payload = json.dumps({
  "type": "PHYSICAL",
  "storePageId": "6100bb8a421abe4707af1cbd",
  "name": "Artisanal Steak Dry Rub",
  "description": "<p>This can be a few words or even a few <i>paragraphs</i>.</p>",
  "urlSlug": "artisanal-steak-dry-rub",
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
      "sku": "SQ0557856",
      "pricing": {
        "basePrice": {
          "currency": "USD",
          "value": "12.95"
        },
        "onSale": False,
        "salePrice": {
          "currency": "USD",
          "value": "0.00"
        }
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
headers = {
  'Authorization': 'Bearer 123abc',
  'User-Agent': 'Megan-postman',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)