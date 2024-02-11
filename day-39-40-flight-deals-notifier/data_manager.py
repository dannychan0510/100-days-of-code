import os
import requests

SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PW = os.environ["SHEETY_PW"]
SHEETY_ENDPOINT = 'https://api.sheety.co/2629490a2bce2089b8b8dd37ff5689f3/flightDeals/prices'

class DataManager:
    
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = SHEETY_USERNAME
        self.pw = SHEETY_PW
        self.endpoint = SHEETY_ENDPOINT
    
    def get_data(self):
        r = requests.get(url=self.endpoint, auth=(self.username, self.pw))
        return r.json()