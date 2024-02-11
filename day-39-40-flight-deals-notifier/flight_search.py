import os
import requests
from pprint import pprint

KIWI_API_KEY = os.environ["KIWI_API_KEY"]
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.api_key = KIWI_API_KEY
        self.headers = {
            'apikey': KIWI_API_KEY
        }

    def get_iata_code(self, city_name):
        self.params = {
            'term': city_name
        }
        r = requests.get(url=KIWI_ENDPOINT, params=self.params, headers=self.headers)
        r.raise_for_status()
        return r.json()['locations'][0]['code']
