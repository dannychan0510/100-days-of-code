# Import packages
import datetime as dt
import pytz
import requests
import smtplib
import time

# CONSTANTS
MY_LAT = 35.658257
MY_LONG = 139.723877

# E-mail account details
my_email = "dannychantesting@gmail.com"
password = "ighvhaupipfkbxcy"

# API parameters
sunrise_sunset_parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}


# Function to detect whether ISS is within proximity of my location
def is_iss_overhead(lat=MY_LAT, long=MY_LONG):
    """
    Check if the ISS (International Space Station) is within a certain proximity to a given location.

    Args:
        lat (float): The latitude of the location.
        long (float): The longitude of the location.

    Returns:
        bool: True if the ISS is within the specified proximity, False otherwise.
    """
    # Get ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_position = response.json()["iss_position"]

    iss_lat = float(iss_position["latitude"])
    iss_long = float(iss_position["longitude"])

    if abs(lat - iss_lat) <= 5 and abs(long - iss_long) <= 5:
        return True
    else:
        return False


# Function to check whether it is dark right now
def is_dark(parameters=sunrise_sunset_parameters):
    """
    Check if it is currently dark based on the sunrise and sunset times for a given location.

    Args:
        parameters (dict): Parameters for the sunrise-sunset API.

    Returns:
        bool: True if it is currently dark, False otherwise.
    """

    # Get sunrise/sunset times for location
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise_time_str = response.json()["results"]["sunrise"]
    sunset_time_str = response.json()["results"]["sunset"]

    # Convert to datetime object
    sunrise_time = dt.datetime.fromisoformat(sunrise_time_str)
    sunset_time = dt.datetime.fromisoformat(sunset_time_str)

    # Get today's date and time
    utc_now = dt.datetime.now(pytz.UTC)

    # Check whether it is after sunset, and before sunrise
    if sunset_time < utc_now < sunrise_time + dt.timedelta(days=1):
        return True
    else:
        return False


while True:
    # Check if the ISS is overhead and it is currently dark
    if is_iss_overhead() & is_dark:
        # Establish a secure connection with the SMTP server
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            # Login to the email account
            connection.login(user=my_email, password=password)
            # Send an email notification
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Look up!\n\nLook up! The ISS is above you.",
            )
    # Sleep for 60 secs before re-running
    time.sleep(60)
