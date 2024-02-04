# ISS Overhead Notifier

This application is a simple Python script that uses the Open Notify API to get the current position of the International Space Station (ISS), and sends an email to a specified address if the ISS is overhead a specific location, and that it is dark.

## File

- `main.py`: This file contains the main script that makes a GET request to the Open Notify API and retrieves the current position of the ISS.
- `kanye-quotes-app`: This is a Python application that uses the Tkinter library to create a graphical user interface and the requests library to fetch quotes from the Kanye REST API. Used as a small practice to learn how to make API requests.

## How it Works

The script sends a GET request to the `http://api.open-notify.org/iss-now.json` endpoint of the Open Notify API. This endpoint returns a JSON object that contains the current latitude and longitude of the ISS.

The `response.raise_for_status()` line checks if the request was successful. If the request was not successful (i.e., if the HTTP status code is not in the 200-299 range), this line will raise an exception.

The `iss_position = response.json()["iss_position"]` line parses the JSON response and extracts the `iss_position` object, which is a dictionary that contains the `latitude` and `longitude` of the ISS.

## Requirements

- Python 3
- `requests` library

## Usage

To run the script, navigate to the directory containing the `main.py` file and run the following command:

```bash
python main.py
```

This will print the current latitude and longitude of the ISS to the console.