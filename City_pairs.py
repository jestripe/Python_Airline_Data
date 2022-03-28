from email.mime import base
import requests
import json

base_url = 'http://api.aviationstack.com/v1/flights'
api_key = 'SECRET'

params = dict(access_key = api_key, dep_iata = 'DFW', arr_iata = 'MSP', status = 'active', airline_icao = 'aal')

response = requests.get(base_url, params)

print(response.text)