# Day 27: Stock Price and News Alert

This Python application fetches stock price data and relevant news articles for a given company. It calculates the percentage change in the stock price over the past two days and fetches news articles related to the company from the past two days. If the stock price change is significant (more than 2.5%), it sends an SMS with the stock price change and the news articles.

## 🐍 Python Concepts Learned

During the development of this application, I learned and familiarised myself with the following Python concepts:

1. Importing and using the `requests` module to make HTTP requests.
2. Using the `os` module to access environment variables.
3. Using the `datetime` module to calculate dates.
4. Using the `unidecode` module to clean text data.
5. Using the `twilio` module to send SMS messages.
6. Defining and using functions to fetch data from APIs and calculate percentage changes.
7. Using conditional statements to control the flow of the program.

## 🚀 How to Run the Program

To run the Stock Price and News Alert application, follow these steps:

1. Make sure you have Python installed on your computer. This program is compatible with Python 3.6 or higher.
2. Save the `main.py` into your working directory.
3. Install the required Python packages with `pip install requests unidecode twilio`.
4. Set up environment variables for the Alpha Vantage API key, MarketAux API key, and Twilio account SID, auth token, sender phone number, and recipient phone number.
5. Run the program with `python main.py` (or `python3 main.py` on some systems). Make sure you use the `cd` command to change the working directory to where you saved the program.

## 🔮 Future Features
In the future, we aim to improve the relevancy of the news articles fetched by the application. Currently, the application fetches the three most relevant articles according to the MarketAux API. However, the relevancy of these articles can sometimes be questionable.

Ideally, we would like to use a Large Language Model (LLM) to summarize the news that is most relevant to understanding the stock price change. This would involve training a model to understand the context of the stock market and the specific company, and to summarize news articles in a way that highlights their relevance to the stock price change. This would provide a more accurate and useful summary of the news for the user.

---

Disclaimer: This README is generated with the help of GitHub Copilot.