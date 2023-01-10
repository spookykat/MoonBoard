import requests
import secret


def getAccessToken(**kwargs):
    ''' Get 'access token' '''
    URL = "https://restapimoonboard.ems-x.com/token"

    headers = {
        'accept-encoding': 'gzip, gzip',
        'content-type': 'application/x-www-form-urlencoded',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }
    data = {
        'refresh_token': getRefreshToken(**kwargs),
        'grant_type': 'refresh_token',
        'client_id': 'com.moonclimbing.mb'
    }
    r = requests.get(URL, headers=headers, data=data)
    return r.json()['access_token']


def getRefreshToken(username=secret.username, password=secret.password):
    ''' Get a 'refresh token', used to obtaion additional 'access tokens'

    Args:
      username (str): username, default from secret.username
      password (str): password, default from secret.password
    '''
    URL = "https://restapimoonboard.ems-x.com/token"

    headers = {
        'accept-encoding': 'gzip, gzip',
        'content-type': 'application/x-www-form-urlencoded',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }
    data = {
        'username': username,
        'password': password,
        'grant_type': 'password',
        'client_id': 'com.moonclimbing.mb'
    }
    r = requests.get(URL, headers=headers, data=data)
    return (r.json()['refresh_token'])
