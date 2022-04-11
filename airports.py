from email.mime import base
import requests
import json
import pandas as pd

api_filename = 'api_key.json'

api_keys = {}
with open(api_filename, 'r') as f:
    api_secret = json.loads(f.read())

api_key = api_secret['AVIATION_STACK_SECRET']

base_url = 'http://api.aviationstack.com/v1/airports'

