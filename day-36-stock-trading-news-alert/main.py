import os
import requests
import datetime as dt


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ['STOCK_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']

date_today = dt.datetime.now().strftime('%Y-%m-%d')
date_yesterday = (dt.datetime.now() - dt.timedelta(days=1)).strftime('%Y-%m-%d')
date_two_days_ago = (dt.datetime.now() - dt.timedelta(days=2)).strftime('%Y-%m-%d')

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}

news_params = {
    'q': COMPANY_NAME,
    'searchIn': 'title,description',
    'from': date_yesterday,
    'to': date_today,
    'language': 'en',
    'sortBy': 'relevancy',
    'apiKey': NEWS_API_KEY,
    'pageSize': 10,
    'page': 1
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price. 

# r = requests.get(STOCK_ENDPOINT, params=stock_params)
# r.raise_for_status()
# data = r.json()['Time Series (Daily)']


# closing_price_yesterday = float(data[date_yesterday]['4. close'])
# closing_price_two_days_ago = float(data[date_two_days_ago]['4. close'])

# pct_change = abs((closing_price_yesterday - closing_price_two_days_ago) / closing_price_two_days_ago)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

r = requests.get(NEWS_ENDPOINT, params=news_params)
r.raise_for_status()
data = r.json()

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's ca and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

