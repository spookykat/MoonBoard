import requests
import shutil
import json
from get_accesstoken import getAccessToken


def requestProblemsJson(n, json, holdset, angle):

    s_holdset, s_angle = holdset_angle_mapping(holdset, angle)
    URL = f"https://restapimoonboard.ems-x.com/v1/_moonapi/problems/v3/{s_holdset}/{s_angle}/{n}?v=8.3.4"

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
        return requestProblemsJson(json['data'][-1]['apiId'], json, holdset, angle)
    else:
        return json


def holdset_angle_mapping(holdset, angle):

    if holdset == "MoonBoard 2016" and angle == "":
        return "1", "0"
    elif holdset == "MoonBoard Masters 2017" and angle == "40":
        return "15", "1"
    elif holdset == "MoonBoard Masters 2017" and angle == "25":
        return "15", "2"
    elif holdset == "MoonBoard Masters 2019" and angle == "40":
        return "17", "1"
    elif holdset == "MoonBoard Masters 2019" and angle == "25":
        return "17", "2"
    elif holdset == "Mini MoonBoard 2020" and angle == "40":
        return "19", "1"
    else:
        raise ValueError(holdset, angle)

for holdset, angle in [
        ("MoonBoard 2016", ""),
        ("MoonBoard Masters 2017", "40"),
        ("MoonBoard Masters 2017", "25"),
        ("MoonBoard Masters 2019", "40"),
        ("MoonBoard Masters 2019", "25"),
        ("Mini MoonBoard 2020", "40"),
]:
    z = {}
    json_data = requestProblemsJson(0, z, holdset, angle)

    with open(f"problems {holdset} {angle}.json", 'w') as file:
        json.dump(json_data, file, indent=4)

# Copy the 2019 problems at 40 degrees to default location for webapp
shutil.copy("problems MoonBoard Masters 2019 40.json", "problems.json")
