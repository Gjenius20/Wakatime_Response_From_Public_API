# wakatime api res in python

#this just like 3 line alternative if you cant using O2auth like sample from wakatime docs
import requests 
import json

user_API = 'Your_Api_Key' #You can get this key from your wakatime option Or you can visit //https://wakatime.com/settings/api-key then paste that key

# this api only get your current stats from last 7_days if you wanna to change you can visit //https://wakatime.com/developers
r = requests.get('https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key=' + user_API)

# and welldone your get your wakatime json api from last 7days
print(json.loads(r.content))

# if you want to get the Specific response from the json use the code below:
    # print(r.json().get('data').get('best_day').get('created_at'))