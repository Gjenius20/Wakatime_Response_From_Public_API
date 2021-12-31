# wakatime api res in python
import requests
import json

# url = 'https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key=f4378b63-bdf0-41d9-993e-4c600e08aa62'
# r = requests.get(url)

r = requests.get('https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key=f4378b63-bdf0-41d9-993e-4c600e08aa62')

# print(json.loads(r.content))

print(r.json().get('data').get('best_day').get('created_at'))