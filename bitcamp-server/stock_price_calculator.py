
import requests
import pandas as pd
import json
import datetime
import yfinance as yf

def stock_price_calculator(stock_ticker):
    end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    stock = yf.Ticker(stock_ticker)
    hist = stock.history()
    price_change = (hist['Close'][-1] - hist['Close'][0]) / hist['Close'][0] * 100
    return price_change


# def stock_price_calculator(stock_ticker):
#     # set the API key and the stock symbol
#     api_key = "21YBLJ5MCOC8723O"
#     symbol = stock_ticker 

#     # set the start and end dates for the time period
#     end_date = datetime.datetime.today().strftime('%Y-%m-%d')
#     start_date = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')

#     # make the API request
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={api_key}"
#     response = requests.get(url)

#     # parse the response and extract the daily closing prices
#     data = json.loads(response.text)
#     daily_data = data["Time Series (Daily)"]
#     closing_prices = [float(daily_data[date]["4. close"]) for date in daily_data if start_date <= date <= end_date]

#     # calculate the percentage change in the last month
#     price_change = (closing_prices[0] - closing_prices[-1]) / closing_prices[0] * 100
#     print(f"{symbol}: {price_change:.2f}%")

#     return price_change


def getTicker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name.strip(), "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code

# debugging purposes
# print(getTicker("First Republic Bank"))
# stock_price_calculator(getTicker("First Republic Bank"))