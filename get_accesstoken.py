import requests
import secret


def getAccessToken():
    URL = "https://restapimoonboard.ems-x.com/token"

    headers = {
        'accept-encoding': 'gzip, gzip',
        'content-type': 'application/x-www-form-urlencoded',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }
    data = {
        'refresh_token': getRefreshToken(),
        'grant_type': 'refresh_token',
        'client_id': 'com.moonclimbing.mb'
    }
    r = requests.get(URL, headers=headers, data=data)
    return r.json()['access_token']


def getRefreshToken():
    URL = "https://restapimoonboard.ems-x.com/token"

    headers = {
        'accept-encoding': 'gzip, gzip',
        'content-type': 'application/x-www-form-urlencoded',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }
    data = {
        'username': secret.username,
        'password': secret.password,
        'grant_type': 'password',
        'client_id': 'com.moonclimbing.mb'
    }
    r = requests.get(URL, headers=headers, data=data)
    return(r.json()['refresh_token'])
