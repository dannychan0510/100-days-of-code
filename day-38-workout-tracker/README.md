# Day 38: Workout Tracker 📝

## Overview 🌐
This Python script is designed to help users track their daily exercises by leveraging the power of the Nutritionix API to interpret natural language inputs into structured exercise data and the Sheety API to log these exercises into a Google Sheets document for easy tracking and visualization.

## Features 🌟
- **Natural Language Processing:** Users can input their exercises in natural language (e.g., "ran 3 miles"), and the script will automatically identify the exercise, duration, and calories burned.
- **Automatic Logging:** The script logs each exercise session with the date, time, exercise name, duration, and calories burned directly into a Google Sheets document.
- **Ease of Use:** Simple command-line interface for inputting exercise data.

## Requirements 📋
Before running the script, ensure you have the following:
- Python 3.x installed on your system.
- Access to the internet to make API requests.
- An APP ID and API KEY from Nutritionix for exercise data interpretation.
- A Sheety account with a configured Google Sheets document for logging the exercises.
- The requests library installed (install via pip with `pip install requests`).

## Environment Variables 🔐
The script uses environment variables for sensitive information and API keys. Make sure to set the following variables in your environment:
- `APP_ID`: Your Nutritionix App ID.
- `API_KEY`: Your Nutritionix API Key.
- `SHEETY_USERNAME`: Your Sheety username.
- `SHEETY_PW`: Your Sheety password (or Bearer token for OAuth2).

## Usage 🚀
To use the script, follow these steps:
1. Open your terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using Python with the command `python main.py`.
4. When prompted, input the exercise you did in natural language.
5. The script will process your input, communicate with the APIs, and log your exercise in the Google Sheets document.

## API Endpoints 📡
- **Nutritionix:** Used for interpreting the natural language input into structured exercise data.
- **Sheety:** Used for logging the exercise data into a Google Sheets document.
