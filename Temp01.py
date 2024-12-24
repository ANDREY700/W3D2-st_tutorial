
# file for functions testing


import yfinance as yf

# Define the ticker symbol
ticker_symbol = "AAPL"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data for the last 30 days
historical_data = ticker.history(period="1mo")  # data for the last month

# Display a summary of the fetched data
print(f"Summary of Historical Data for {ticker_symbol}:")
print(historical_data[['Open', 'High', 'Low', 'Close', 'Volume']])
#                                 Open        High  ...       Close    Volume
#Date                                               ...                      
#2024-11-21 00:00:00-05:00  419.500000  419.779999  ...  412.869995  20780200
#2024-11-22 00:00:00-05:00  411.369995  417.399994  ...  417.000000  24814600



df = yf.download(tickers, group_by="ticker")




import datetime
 
# Создание объекта datetime
date = datetime.datetime(2024, 12, 22)
# 0 = Monday
# 6 = Sunday

# Вывод дня недели
print(date.weekday())




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

d1 = yf.Ticker('AAPL')
    # data for the last month
d2 = d1.history(period="1y").reset_index()
#d2['Date']
    


# Line plot of closing prices
plt.figure(figsize=(12, 6))
plt.plot(d2['Close'], label=f'{symbol} Closing Price', linewidth=2)
plt.title(f'{symbol} Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.show()