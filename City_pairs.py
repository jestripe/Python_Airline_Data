from email.mime import base
import requests
import json
import pandas as pd

api_filename = 'api_key.json'

api_keys = {}
with open(api_filename, 'r') as f:
    api_secret = json.loads(f.read())

api_key = api_secret['AVIATION_STACK_SECRET']

base_url = 'http://api.aviationstack.com/v1/flights'

params = dict(access_key = api_key, dep_iata = 'DFW', ar_iata = 'MSP', status = 'active', airline_icao = 'aal')

# response.json()

# df = pd.DataFrame.from_dict(response.json()['data'])

# df.to_csv('test.csv')

response.json().keys()

t2 = response.json()['data']
df = pd.json_normalize(t2)