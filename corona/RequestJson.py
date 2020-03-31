import requests
from json import loads

from .Country import Country

class RequestJson:
    r = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/json/')
    json_request = loads(r.content)
    json_request = json_request['records']
