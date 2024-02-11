# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

import requests
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# TODO read data

# Read in data from sheets
test = DataManager()
test2 = FlightSearch()

# data = test.get_data()
# print(data)

data = {
    "prices": [
        {"city": "Paris", "iataCode": "", "lowestPrice": 54, "id": 2},
        {"city": "Berlin", "iataCode": "", "lowestPrice": 42, "id": 3},
        {"city": "Tokyo", "iataCode": "", "lowestPrice": 485, "id": 4},
        {"city": "Sydney", "iataCode": "", "lowestPrice": 551, "id": 5},
        {"city": "Istanbul", "iataCode": "", "lowestPrice": 95, "id": 6},
        {"city": "Kuala Lumpur", "iataCode": "", "lowestPrice": 414, "id": 7},
        {"city": "New York", "iataCode": "", "lowestPrice": 240, "id": 8},
        {"city": "San Francisco", "iataCode": "", "lowestPrice": 260, "id": 9},
        {"city": "Cape Town", "iataCode": "", "lowestPrice": 378, "id": 10},
    ]
}

# pprint(data)

# TODO search IATA codes for from kiwi API
for row in data['prices']:
    if row['iataCode'] == '':
        row['iataCode'] = test2.get_iata_code(row['city'])

# TODO add IATA codes to data


# TODO write IATA codes back to sheet


# TODO search 

