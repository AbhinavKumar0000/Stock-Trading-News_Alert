# Stock-Trading-News_Alert

This project is a Stock Trading News Alert system built using Python, Twilio, Alpha Vantage API, and NewsAPI. It monitors stock price changes and sends SMS alerts with relevant news headlines if the price fluctuations exceed a certain threshold.

Features
-Fetches stock price data from Alpha Vantage API.
-Monitors the daily percentage changes in stock prices.
-Retrieves related news headlines from NewsAPI for significant price changes.
-Sends SMS alerts using Twilio API.
-Configurable price change threshold.
-Easy deployment on cloud platforms like PythonAnywhere or local environments using Anaconda.


APIs Used:
-Alpha Vantage API (for stock prices)
-NewsAPI (for fetching news headlines)
-Twilio (for sending SMS alerts)

Cloud Platform: Supports running on cloud environments such as PythonAnywhere and Anaconda environments.


API Key Configuration

To run the project, you need to have valid API keys for Alpha Vantage, NewsAPI, and Twilio. Replace the placeholders in the code with your keys:
STOCK_API_KEY = "<Your Alpha Vantage API Key>"
NEWS_API_KEY = "<Your NewsAPI Key>"
TWILIO_SID = "<Your Twilio SID>"
TWILIO_KEY = "<Your Twilio Auth Token>"





How It Works
-Fetches the daily closing prices for the specified stock from Alpha Vantage.
-Compares the current and previous day prices to calculate the percentage change.
-If the change exceeds 5% (configurable threshold), fetches three top news headlines from NewsAPI.
-Sends these news updates via SMS using Twilio.



Deployment on Cloud
-PythonAnywhere
-Upload the project files to your PythonAnywhere account.
-Set up a virtual environment and install the requirements.
-Schedule a daily task to execute the Python script.
