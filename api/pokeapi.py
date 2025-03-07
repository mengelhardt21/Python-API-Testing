import requests
from requests import *
import json
import pprint
from pathlib import Path

base_url = 'https://pokeapi.co/api/v2'

def get_pokemon (id):

    url = f"{base_url}/pokemon/{id}/"

    response = requests.get(url)

    pprint.pprint(url)

    if response.status_code == 200:
        return response.json()
    else:
        pprint.pprint(f'Error: {response.status_code}')

pprint.pprint(get_pokemon(1))