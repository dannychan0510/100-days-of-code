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
FlightData = FlightData()
NotificationManager = NotificationManager()

# Sample data for testing
data = DataManager.get_data()

# Loop through each city in the data
for row in data["prices"]:
    # If the city doesn't have an IATA code, fetch it
    if row["iataCode"] == "":
        row["iataCode"] = FlightSearch.get_iata_code(row["city"])
        DataManager.edit_row(row["id"], row)

    # Search for flights for the city
    flight_data = FlightSearch.search_flights(row["iataCode"], row["lowestPrice"])
    
    try:
        # Populate the DataFrame with the flight data
        data_df = FlightData.populate_flights_df(flight_data)

        # Send a notification with the flight data
        NotificationManager.send_message(data_df)
    except:
        pass
