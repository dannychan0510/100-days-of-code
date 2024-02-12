import os
from twilio.rest import Client
from flight_data import FlightData
from flight_search import FlightSearch

# Load environment variables
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
SENDER_PHONE_NUMBER = os.environ["SENDER_PHONE_NUMBER"]
RECIPIENT_PHONE_NUMBER = os.environ["RECIPIENT_PHONE_NUMBER"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        # Initialize with Twilio credentials and phone numbers
        self.account_sid = TWILIO_ACCOUNT_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.sender_phone_number = SENDER_PHONE_NUMBER
        self.recipient_phone_number = RECIPIENT_PHONE_NUMBER

        # Initialize FlightData and FlightSearch objects
        self.flight_data = FlightData()
        self.flight_search = FlightSearch()

    def send_message(self, data_df):
        # Check if there are any flights
        if len(data_df) > 0:
            # Find the cheapest flight
            self.flight_data.find_cheapest_flight(data_df)

            # Format the flight into a message
            message_text = self.format_message()

            # Send the message
            self.send_twilio_message(message_text)

    def format_message(self):
        # Format the flight data into a message
        message_text = "Low price alert!\n"
        message_text += (
            f"Cheapest flight from {self.flight_data.cheapest_flight['departure_city']} "
            f"({self.flight_data.cheapest_flight['departure_airport']}) to "
            f"{self.flight_data.cheapest_flight['arrival_city']} "
            f"({self.flight_data.cheapest_flight['arrival_airport']})\n"
            f"Outbound date and time: {self.flight_data.cheapest_flight['outbound_date'].strftime('%d %b %Y at %I:%M%p')}\n"
            f"Return date and time: {self.flight_data.cheapest_flight['inbound_date'].strftime('%d %b %Y at %I:%M%p')}\n"
            f"Price: ¥{self.flight_data.cheapest_flight['price']:,}\n"
        )
        if self.flight_data.total_flights > 1:
            message_text += (
                f"There are also {self.flight_data.total_flights} other cheap flights from "
                f"{self.flight_data.cheapest_flight['departure_city']} to {self.flight_data.cheapest_flight['arrival_city']} found between "
                f"{FlightSearch.date_tmr} to {FlightSearch.date_in_six_months}.\n"
            )
        return message_text

    def send_twilio_message(self, message_text):
        # Initialize the Twilio client
        client = Client(self.account_sid, self.auth_token)

        # Create and send the message
        message = client.messages.create(
            body=message_text,
            from_=self.sender_phone_number,
            to=self.recipient_phone_number,
        )

        # Print the message status
        print(message)
