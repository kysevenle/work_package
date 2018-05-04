import api_creds
from urllib.request import urlopen, Request
import json

def fetch(api_key, endpoint):
    headers = {
        'Content-Type': 'application/json',
        'x-Auth-App-Key': api_key,
    }

    request = Request(api_creds.url + endpoint, headers=headers)

    response_body = urlopen(request).read()
    json_obj = response_body

    data = json.loads(json_obj)

    return data


def fetch_services():
    return fetch(api_creds.read_key, 'clients/services')
