from datetime import date, timedelta
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "53706309f9c24e53a057fff1c164372c"
API_KEY_STOCK_DATA = "0MW9QA7YVE2O80CW"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters_daily_trade = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK_DATA,
}

parameters_news = {
    "q": STOCK,
    "apiKey": API_KEY,
}


yesterday = date.today() - timedelta(days=2)
yesterday = str(yesterday)
day_before_last = date.today() - timedelta(days=3)
day_before_last = str(day_before_last)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
response_stock = requests.get(STOCK_ENDPOINT, params=parameters_daily_trade)
response_stock.raise_for_status()
data_stock = response_stock.json()
data_stock_yesterday = float(data_stock["Time Series (Daily)"][yesterday]["4. close"])
data_stock_day_before_last = float(data_stock["Time Series (Daily)"][day_before_last]["4. close"])

data_percentage = ((data_stock_yesterday - data_stock_day_before_last) * 100) / data_stock_day_before_last
if data_percentage < 0:
    is_down = True
else:
    is_up = True

data_percentage = abs(data_percentage)
if data_percentage > 5:
    response = requests.get(NEWS_ENDPOINT, params=parameters_news)
    response.raise_for_status()
    data = response.json()["articles"]
    three_articles = data[:3]



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
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

