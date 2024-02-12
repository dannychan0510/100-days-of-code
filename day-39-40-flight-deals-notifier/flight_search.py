import os
import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Load environment variables
KIWI_API_KEY = os.environ["KIWI_API_KEY"]
KIWI_LLOCATIONS_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        # Initialize with API key and headers
        self.api_key = KIWI_API_KEY
        self.headers = {"apikey": KIWI_API_KEY}

        # Calculate dates for flight search
        self.today = datetime.now()
        self.date_tmr = (self.today + timedelta(days=1)).strftime("%d/%m/%Y")
        self.date_in_six_months = (self.today + relativedelta(months=6)).strftime(
            "%d/%m/%Y"
        )

    def get_iata_code(self, city_name):
        # Get the IATA code for a city
        self.params = {"term": city_name}
        r = requests.get(
            url=KIWI_LLOCATIONS_ENDPOINT, params=self.params, headers=self.headers
        )
        r.raise_for_status()
        return r.json()["locations"][0]["code"]

    def search_flights(self, destination_city, price_to):
        # Search for flights to a destination city
        params = {
            "fly_from": "city:TYO",
            "fly_to": f"city:{destination_city}",
            "date_from": self.date_tmr,
            "date_to": self.date_in_six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "max_stopovers": 0,
            "curr": "JPY",
            "price_to": price_to,
        }

        r = requests.get(url=KIWI_SEARCH_ENDPOINT, params=params, headers=self.headers)
        r.raise_for_status()
        return r.json()
