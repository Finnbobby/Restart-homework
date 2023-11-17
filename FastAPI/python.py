import requests
import json

url = "http://127.0.0.1:8000/items/31231"

payload = json.dumps({
  "name": "Finn",
  "price": 312.5
})
headers = {
  'Content-Type': 'application/json',
  'ContentType': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)