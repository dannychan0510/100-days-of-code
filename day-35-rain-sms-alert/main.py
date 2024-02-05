# Import necessary libraries
import requests
from twilio.rest import Client
import os

# Set your location latitude and longitude
MY_LAT = 56.49
MY_LONG = 5.6

# Get credentials from environmental variables
weather_api_key = os.environ['API_KEY']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
sender_phone_number = os.environ['SENDER_PHONE_NUMBER']
recipient_phone_number = os.environ['RECIPIENT_PHONE_NUMBER']

# Set the API endpoint
api_endpoint = f'https://api.openweathermap.org/data/2.5/forecast'

# Set the parameters for the API request
parameters = {'lat': MY_LAT, 'lon': MY_LONG, 'appid': weather_api_key, 'cnt': 4}

# Make the API request
response = requests.get(api_endpoint, params=parameters)
# Raise an exception if the request was unsuccessful
response.raise_for_status()
# Get the response data
data = response.json()

# Initialize an empty list to store weather IDs
weather_ids = []

# Loop through the forecast data and extract weather IDs
for forecast in data['list']:
    for i in forecast['weather']:
        weather_ids.append(i['id'])

# If any weather ID indicates rain, send a message
# https://openweathermap.org/weather-conditions
if any(id < 700 for id in weather_ids):
    # Initialize the Twilio client
    client = Client(twilio_account_sid, twilio_auth_token)

    # Create and send the message
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☂️.",
                        from_=sender_phone_number,
                        to=recipient_phone_number
                    )

    # Print the message status
    print(message.status)
