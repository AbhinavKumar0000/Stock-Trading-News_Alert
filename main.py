import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "" #Enter stock key here
NEWS_API_KEY = "" #Enter newsapi key here

TWILIO_SID = "" #Enter Twilio SID here
TWILIO_KEY = "" #Enter Twilio key here

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response =requests.get(STOCK_ENDPOINT, params=stock_params)
data =response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = round(float(yesterday_closing_data) - float(day_before_yesterday_closing_price))

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = (difference/ float(yesterday_closing_data))*100


if abs(diff_percent)> 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        }
    news_response = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{COMPANY_NAME}: {up_down}{diff_percent}% \n{article['title']}.\nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID,TWILIO_KEY)
    for article in formatted_articles:
        message = client.messages.create(
            body= article,
            from_= "+18596970391",
            to = "+918383951265",
        )



