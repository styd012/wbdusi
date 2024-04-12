
import json
from sentinelsat import SentinelAPI

def initializeSentinelAPI():
    creds = {}
    with open('./credentials.json') as temp:
        creds = json.load(temp)
    
    user = creds['uid']
    passw = creds['pass']
    api = SentinelAPI(user, passw, 'https://scihub.copernicus.eu/dhus')
    
    return api


    
    