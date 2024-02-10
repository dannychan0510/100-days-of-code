# Import necessary libraries
import os
import requests
from datetime import datetime

# Get username and token from environment variables
USERNAME = os.environ("USERNAME")
TOKEN = os.environ("TOKEN")

# Define graph ID
GRAPH = "graph1"

# Define Pixela endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# Define user parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment to create a new user
# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)

# Define graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Define graph configuration
graph_config = {
    "id": GRAPH,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu",
}

# Define headers
headers = {"X-USER-TOKEN": TOKEN}

# Uncomment to create a new graph
# r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)#
# print(r.text)

# Define pixel creation endpoint
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

# Get today's date
today = datetime.now().strftime("%Y%m%d")
print(today)

# Define pixel data
pixel_data = {"date": today, "quantity": "4.84"}

# Uncomment to create a new pixel
# r = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(r.text)

# Define day to update
DAY_TO_UPDATE = "20240209"

# Define pixel update endpoint
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{DAY_TO_UPDATE}"

# Define pixel update data
pixel_update_data = {"quantity": "5.1"}

# Uncomment to update a pixel
# r = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(r.text)

# Define day to delete
DAY_TO_DELETE = "20240209"

# Define pixel delete endpoint
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{DAY_TO_DELETE}"

# Uncomment to delete a pixel
# r = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(r.text)
