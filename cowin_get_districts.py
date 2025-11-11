import requests

url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/16"

res = requests.get(url)

districts = res.json()

print(districts)
