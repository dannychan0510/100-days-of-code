import os
import requests
import datetime as dt
from unidecode import unidecode
from twilio.rest import Client

# Define constants
STOCK = "GOOG"
COMPANY_NAME = "Google"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ["STOCK_API_KEY"]

NEWS_ENDPOINT = "https://api.marketaux.com/v1/news/all"
NEWS_API_KEY = os.environ["MARKETAUX_API_KEY"]

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
SENDER_PHONE_NUMBER = os.environ["SENDER_PHONE_NUMBER"]
RECIPIENT_PHONE_NUMBER = os.environ["RECIPIENT_PHONE_NUMBER"]

# Calculate dates
date_today = dt.datetime.now().strftime("%Y-%m-%d")
date_yesterday = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y-%m-%d")
date_two_days_ago = (dt.datetime.now() - dt.timedelta(days=2)).strftime("%Y-%m-%d")

# Define parameters for API requests
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "api_token": NEWS_API_KEY,
    "symbols": STOCK,
    "search": COMPANY_NAME,
    "filter_entities": "true",
    "language": "en",
    "published_after": date_two_days_ago,
    "published_before": date_today,
    "sort": "entity_match_score",
}

# Fetch stock data
r = requests.get(STOCK_ENDPOINT, params=stock_params)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]

# Calculate percentage change in stock price
closing_price_yesterday = float(data[date_yesterday]["4. close"])
closing_price_two_days_ago = float(data[date_two_days_ago]["4. close"])
pct_change = (
    closing_price_yesterday - closing_price_two_days_ago
) / closing_price_two_days_ago

# Fetch news data
snippets = []
r = requests.get(NEWS_ENDPOINT, params=news_params)
r.raise_for_status()
articles = r.json()["data"]
for a in articles:
    cleaned_title = unidecode(a["title"])
    cleaned_description = unidecode(a["description"])
    snippets.append(f"Headline: {cleaned_title}\nBrief: {cleaned_description}")

# Send SMS for each news snippet if stock price change is significant (+/-2.5%)
if abs(pct_change) >= 0.025 and len(snippets) > 0:
    for s in snippets:
        # Format message
        price_snippet = (
            f'{STOCK}: {"🔺" if pct_change >= 0 else "🔻"}{abs(pct_change):.2%}'
        )
        message_text = f"{price_snippet}\n\n{s}"

        # Initialize the Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Create and send the message
        message = client.messages.create(
            body=message_text, from_=SENDER_PHONE_NUMBER, to=RECIPIENT_PHONE_NUMBER
        )

        # Print the message status
        print(message)
