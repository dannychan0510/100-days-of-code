import os
from twilio.rest import Client
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

        # Initialize FlightSearch objects
        self.flight_search = FlightSearch()

    def send_message(self, flight_data):
        # Check if there are any flights
        if flight_data is not None:

            # Format the flight into a message
            message_text = self.format_message(flight_data)

            # Send the message
            self.send_twilio_message(message_text)

    def format_message(self, flight_data):
        # Format the flight data into a message
        message_text = "Low price alert!\n"
        message_text += (
                f"Cheapest flight from {flight_data.origin_city} "
                f"({flight_data.origin_airport}) to "
                f"{flight_data.destination_city} "
                f"({flight_data.destination_airport})\n"
                f"Outbound date and time: {flight_data.out_date.strftime('%d %b %Y at %I:%M%p')}\n"
                f"Return date and time: {flight_data.return_date.strftime('%d %b %Y at %I:%M%p')}\n"
                f"Price: ¥{flight_data.price:,}\n"
            )        
        if flight_data.stop_overs > 0:
            message_text += (
                f"\nFlight has {flight_data.stop_overs} stop over, "
                f"via {flight_data.via_city}-{flight_data.via_airport}."
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
