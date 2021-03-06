import requests
import time

ticker = "TSLA"

api_key = "e0284e629a65479eb7f9ee7242f46155"

def get_stock_price(ticker_symbol, apikey):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={apikey}" #f = format url
    response = requests.get(url).json()
    price = response['price'][:-2] #Chop 2 decimal places
    return price 

def get_stock_quote(ticker_symbol, apikey):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={apikey}"     # f = format url
    response = requests.get(url).json()
    return response

stockdata = get_stock_quote(ticker, api_key) #Get stock data array

stock_name = stockdata['name']
stock_currency = "(" + stockdata['currency'] + ")"
if (stock_currency == "(USD)"):
    stock_price = get_stock_price(ticker, api_key) + " $" #Get stock real time price
else:
    stock_price = get_stock_price(ticker, api_key) #Get stock real time price

stock_change_percent = stockdata['percent_change'] + " %"

result = stock_name + "\n" + stock_price + " " + stock_currency + "\n" + stock_change_percent

print(result)
    
