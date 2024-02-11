# Import necessary modules
import os
import requests
from datetime import datetime

# Get environment variables
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PW = os.environ["SHEETY_PW"]

# Define API endpoints
nl_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/2629490a2bce2089b8b8dd37ff5689f3/workoutTracker/workoutTracker"

# Define headers for API requests
nutritionix_headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}

# Get user input
user_input = input("Tell me the exercise you did: ")

# Define parameters for Nutritionix API request
nl_exercise_parameters = {
    "query": user_input,
    "weight_kg": "81",
    "height_cm": "168",
    "age": "35",
}

# Make a POST request to the Nutritionix API
r = requests.post(
    url=nl_exercise_endpoint, json=nl_exercise_parameters, headers=nutritionix_headers
)
result = r.json()["exercises"]

# Get current date and time
today = datetime.now()

# Loop through the result list
for i in range(len(result)):
    # Define data for each row
    row_data = {
        "workoutTracker": {
            "date": today.strftime("%Y-%m-%d"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": result[i]["name"].title(),
            "duration": result[i]["duration_min"],
            "calories": result[i]["nf_calories"],
        }
    }

    # Make a POST request to the Sheety API
    r = requests.post(
        url=sheety_endpoint, json=row_data, auth=(SHEETY_USERNAME, SHEETY_PW)
    )
