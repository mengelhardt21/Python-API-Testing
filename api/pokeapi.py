import requests
from requests import *
import json
import pprint
import urllib.parse
import sys
from pathlib import Path

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon (id):

    url = f"{base_url}/pokemon/{id}"

    