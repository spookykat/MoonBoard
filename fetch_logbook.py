import requests
import json
import shutil
from get_accesstoken import getAccessToken
from secret import username


def request_data(n=0, access_kwargs={}):
    '''
    Request logbook from moonboard api

    Args:
      n (int): download 'startline'. Not used here. In case of >5000 lines?
      access_kwargs (dict): dict passed to getAccessToken as kwargs

    access_kwargs can be used to pass username and password as kwargs to
    getAccessToken/getRefreshToken
    '''
    URL = f"https://restapimoonboard.ems-x.com/v1/_moonapi/Logbook/{n}?v=8.3.4"

    headers = {
        'accept-encoding': 'gzip, gzip',
        'authorization': f'BEARER {getAccessToken(**access_kwargs)}',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }

    json = requests.get(URL, headers=headers).json()
    return json


def main():
    # Request data
    json_data = request_data()

    # Save to json file
    with open("logbook.json", 'w') as file:
        json.dump(json_data, file, indent=4)

    # Copy to file with username in it
    shutil.copy("logbook.json", f"logbook_{username}.json")


if __name__ == '__main__':
    main()
