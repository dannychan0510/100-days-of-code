# Import necessary modules
import os
import requests

# Load environment variables
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PW = os.environ["SHEETY_PW"]
SHEETY_ENDPOINT = (
    "https://api.sheety.co/2629490a2bce2089b8b8dd37ff5689f3/flightDeals/prices"
)


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """

    def __init__(self):
        # Initialize with Sheety credentials and endpoint
        self.username = SHEETY_USERNAME
        self.pw = SHEETY_PW
        self.endpoint = SHEETY_ENDPOINT

    def get_data(self):
        # Fetch data from the Google Sheet
        r = requests.get(url=self.endpoint, auth=(self.username, self.pw))
        r.raise_for_status()
        return r.json()

    def edit_row(self, id, row):
        # Edit a specific row in the Google Sheet
        edit_endpoint = f"{self.endpoint}/{id}"
        row_data = {"price": row}
        r = requests.put(
            url=edit_endpoint, json=row_data, auth=(self.username, self.pw)
        )
        r.raise_for_status()
