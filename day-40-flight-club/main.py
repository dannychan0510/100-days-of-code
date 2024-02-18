# Import necessary modules
import os
from pprint import pprint
import requests
import pandas as pd
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Instantiate classes
DataManager = DataManager()
FlightSearch = FlightSearch()
NotificationManager = NotificationManager()

# Sample data for testing
# data = DataManager.get_data()
data = {
    "prices": [
        # {"city": "New York", "iataCode": "NYC", "lowestPrice": 200000, "id": 1},
        {"city": "London", "iataCode": "LON", "lowestPrice": 150000, "id": 2},
        # {"city": "Hong Kong", "iataCode": "HKG", "lowestPrice": 50000, "id": 3},
        # {"city": "Bangkok", "iataCode": "BKK", "lowestPrice": 50000, "id": 4},
        # {"city": "Bali", "iataCode": "DPS", "lowestPrice": 600000, "id": 5},
    ]
}

# Loop through each city in the data
for row in data["prices"]:
    # If the city doesn't have an IATA code, fetch it
    if row["iataCode"] == "":
        row["iataCode"] = FlightSearch.get_iata_code(row["city"])
        DataManager.edit_row(row["id"], row)

    # Search for flights for the city
    flight_data = FlightSearch.search_flights(row["iataCode"], row["lowestPrice"])

    if flight_data == None:
        print("No flights found\n")
    else:
        NotificationManager.send_message(flight_data)
