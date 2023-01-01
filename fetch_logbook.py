import requests
import json
import shutil
from get_accesstoken import getAccessToken
from secret import username


def request_data(n=0):
    URL = f"https://restapimoonboard.ems-x.com/v1/_moonapi/Logbook/{n}?v=8.3.4"

    headers = {
        'accept-encoding': 'gzip, gzip',
        'authorization': f'BEARER {getAccessToken()}',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }

    json = requests.get(URL, headers=headers).json()
    return json


# Request data
json_data = request_data()

# Save to json file
with open("logbook.json", 'w') as file:
    json.dump(json_data, file, indent=4)

# Copy to file with username in it
shutil.copy("logbook.json", f"logbook_{username}.json")
