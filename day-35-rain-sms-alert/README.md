# Weather Alert Application

This Python application uses the OpenWeatherMap API to check the weather forecast for a specific location. If the forecast indicates rain, it sends an SMS alert using the Twilio API.

## Dependencies

- `requests`: Used to make HTTP requests to the OpenWeatherMap API.
- `twilio`: Used to send SMS alerts.
- `os`: Used to access environment variables.

## Setup

1. Install the necessary Python packages:

    ```bash
    pip install requests twilio
    ```

2. Set the following environment variables:

    - `API_KEY`: Your OpenWeatherMap API key.
    - `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
    - `TWILIO_AUTH_TOKEN`: Your Twilio auth token.

    On Windows, use the following in the command prompt:

    ```cmd
    setx API_KEY "your_openweathermap_api_key"
    setx TWILIO_ACCOUNT_SID "your_twilio_account_sid"
    setx TWILIO_AUTH_TOKEN "your_twilio_auth_token"
    setx SENDER_PHONE_NUMBER "sender_phone_number"
    setx RECIPIENT_PHONE_NUMBER "recipient_phone_number"
    ```

    On macOS, add the following lines to your .bash_profile or .zshrc file:

    ```bash
    export API_KEY="your_openweathermap_api_key"
    export TWILIO_ACCOUNT_SID="your_twilio_account_sid"
    export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
    export SENDER_PHONE_NUMBER="sender_phone_number"
    export RECIPIENT_PHONE_NUMBER="recipient_phone_number"
    ```

    Remember to replace `"your_openweathermap_api_key"`, `"your_twilio_account_sid"`, and `"your_twilio_auth_token"` with your actual credentials. After setting the environment variables, you may need to restart your terminal or command prompt for the changes to take effect.

3. Update the `MY_LAT` and `MY_LONG` variables in `main.py` to your location's latitude and longitude.

4. Update the `from_` and `to` parameters in the `client.messages.create` function to your Twilio phone number and the phone number where you want to receive the alerts.

## Usage

Run the script with Python:

```bash
python main.py
```

If the forecast indicates rain, you will receive an SMS alert saying "It's going to rain today. Remember to bring an ☂️.".

## Note

The weather condition codes used by OpenWeatherMap can be found [here](https://openweathermap.org/weather-conditions). This script considers any code less than 700 as indicating rain.