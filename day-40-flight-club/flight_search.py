# Import necessary modules
import os
import requests
from pprint import pprint
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from flight_data import FlightData

# Load environment variables
KIWI_API_KEY = os.environ["KIWI_API_KEY"]
KIWI_LOCATIONS_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
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
        self.date_in_six_months = (self.today + relativedelta(months=6)).strftime("%d/%m/%Y")

    def get_iata_code(self, city_name):
        # Get the IATA code for a city
        self.location_params = {"term": city_name}
        return self._make_request(KIWI_LOCATIONS_ENDPOINT, self.location_params)["locations"][0]["id"]

    def search_flights(self, destination_city, price_to):
        # Search for flights to a destination city
        self.search_params = {
            "fly_from": "city:TYO",
            "fly_to": f"city:{destination_city}",
            "date_from": self.date_tmr,
            "date_to": self.date_in_six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "max_stopovers": 0,
            "curr": "JPY",
            "price_to": price_to,
            "one_for_city": 1,
        }

        print(f"Check flights triggered for {destination_city}")

        # Try to get flight data
        try:
            data = self._make_request(KIWI_SEARCH_ENDPOINT, self.search_params)["data"][0]
            # pprint(data)
        except IndexError:
            # If no direct flights found, try to find flights with one stopover
            # Note: this means max_stopovers = 4, to account for inbound and outbound
            self.search_params["max_stopovers"] = 4
            try:
                data = self._make_request(KIWI_SEARCH_ENDPOINT, self.search_params)["data"][0]
                # pprint(data)
            except IndexError:
                return None
            pass
        
        return self._create_flight_data(data)

    def _make_request(self, url, params):
        try:
            r = requests.get(url, params=params, headers=self.headers)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError:
            print(f"HTTPError: {params['fly_to']} cannot be proceesed.")
            return None

    def _create_flight_data(self, data):
        # Find the index number of the first return flight
        for i, leg in enumerate(data["route"]):
            if leg['return'] == 1:
                return_flight_index = i

        # Count number of legs in entire journye
        stop_overs = len(data["route"]) / 2 - 1                
    
        # Create FlightData object
        return FlightData(
            price=data["price"],
            origin_city=data["cityCodeFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityCodeTo"],
            destination_airport=data["flyTo"],
            out_date=datetime.strptime(data["route"][0]["local_departure"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            return_date=datetime.strptime(data["route"][return_flight_index]["local_departure"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            stop_overs=stop_overs,
            via_city=data["route"][0]["cityCodeTo"] if stop_overs > 0 else None,
            via_airport=data["route"][0]["flyTo"] if stop_overs > 0 else None,
        )
        