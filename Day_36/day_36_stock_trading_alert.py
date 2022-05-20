### Day 36 - Stock trading news alert project

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "PV61VM6MEIOZ"
NEWS_API = "1j55x5j89c8g03cmg62pl"

TWILIO_SID = "ACeImei653kMeg9g7g67GRn65z"
TWILIO_AUTH = "48fk1mcc8afd0v42mbvy0"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}
news_params = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close = yesterday_data["4. close"]
day_before_yesterday_close = data_list[1]["4. close"]

abs_delta = round(abs(float(yesterday_close) - float(day_before_yesterday_close)))
delta_percent = (abs_delta / float(yesterday_close)) * 100

if delta_percent > 3:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    first_articles = articles[:3]  # first 3

    formatted_articles = [f"{STOCK_NAME}: Moved {delta_percent}%"
                          f"Headline: {articles['title']}.\n"
                          f"Brief {articles['description']}" for article in first_articles]
    for article in formatted_articles:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages.create(
            body=article,
            from_="+359887862498",
            to="+359889903652"
        )
