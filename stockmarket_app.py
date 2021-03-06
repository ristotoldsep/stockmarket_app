import requests
import time

ticker = "TSLA"

<<<<<<< HEAD
api_key = "<api key>"  # apikey from twelvedata
=======
api_key = "<api key>" #api_key from twelvedata
>>>>>>> f09a06682ded668da12c60e8c08e1f92afc53adc

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
    
