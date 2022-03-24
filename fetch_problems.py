import requests
import json
from get_accesstoken import getAccessToken


def requestProblemsJson(n, json):

    URL = f"https://restapimoonboard.ems-x.com/v1/_moonapi/problems/v3/17/1/{n}?v=8.3.4"

    headers = {
        'accept-encoding': 'gzip, gzip',
        'authorization': f'BEARER {getAccessToken()}',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }

    jsontemp = requests.get(URL, headers=headers).json()
    if(n == 0):
        json = requests.get(URL, headers=headers).json()
    else:
        for data in jsontemp['data']:
            json['data'].append(data)

    if len(jsontemp['data']) == 5000:
        return requestProblemsJson(json['data'][-1]['apiId'], json)
    else:
        return json


z = {}
json_data = requestProblemsJson(0, z)

with open("problems.json", 'w') as file:
    json.dump(json_data, file, indent=4)
