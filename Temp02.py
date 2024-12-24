



import yfinance as yf

# Fetch historical stock data
symbol = 'AAPL'
stock_data = yf.download(symbol, start='2022-01-01', end='2023-01-01', progress=False)

# Display the first few rows of the dataset
print(stock_data.head())


#https://dev.to/bshadmehr/unveiling-financial-insights-visualizing-stock-data-with-matplotlib-and-seaborn-4l0j

import matplotlib.pyplot as plt



# Line plot of closing prices
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label=f'{symbol} Closing Price', linewidth=2)
plt.title(f'{symbol} Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.show()


a10 = stock_data.copy().reset_index()
a10['AdjClose'] = a10.Close.pct_change(1)

import seaborn as sns
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.histplot(a10['AdjClose'].pct_change().dropna(), bins=30, kde=True, color='blue')
plt.title(f'Distribution of {symbol} Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()



import plotly.graph_objects as go

# Candlestick chart
candlestick = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                              open=stock_data['Open'],
                                              high=stock_data['High'],
                                              low=stock_data['Low'],
                                              close=stock_data['Close'])])

candlestick.update_layout(title=f'{symbol} Candlestick Chart',
                          xaxis_title='Date',
                          yaxis_title='Stock Price (USD)',
                          xaxis_rangeslider_visible=False)

candlestick.show()





plt.figure(figsize=(12, 6))
stock_data['Close'].plot(label=f'{symbol} Closing Price', linewidth=2)
stock_data['Close'].mean().plot(label=f'{symbol} 30-Day Avg', linestyle='--', color='orange')
plt.title(f'{symbol} Closing Prices with 30-Day Moving Average')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.show()
#rolling(window=30).




# Moving Average Plot
plt.figure(figsize=(12, 6))
stock_data['Close'].plot(label=f'{symbol} Closing Price', linewidth=2)
stock_data['Close'].rolling(window=30).mean().plot(label=f'{symbol} 30-Day Avg', linestyle='--', color='orange')
plt.title(f'{symbol} Closing Prices with 30-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.show()


a4 = stock_data.reset_index()
a4['ave'] = a4['Close'].rolling(window=30).mean()

fig01 = plt.figure(figsize=(10, 5), dpi=100)
plt.plot(a4.Date, a4['Close'], '-g', label="Цена закрытия USD")
plt.plot(a4.Date, a4['Close'].rolling(window=30).mean(), ':r', label="Среднее за 30 дней")
plt.style.use('_mpl-gallery')
plt.title("Свадьбы и разводы на 1000 чел в США 1867 - 2011")
plt.xlabel("Дата")
plt.xticks(rotation=90)
plt.legend();
plt.show()





a2 = stock_data.reset_index()
plt.figure(figsize=(12, 6))
plt.bar(x = a2.Date, y = a2.Volume, color='green', alpha=0.7)
plt.title(f'{symbol} Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()


a2.head()
a2.Date
a2.columns[1] = 


plt.figure(figsize=(12, 6))
plt.bar(stock_data.index, int(stock_data['Volume']/1000000), color='green', alpha=0.7)
plt.title(f'{symbol} Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()


stock_data.dtypes
a2.dtypes

a2.columns = a2.columns.droplevel(-1)
a3 = a2[0:250]
a3 = a2.copy()


plt.figure(figsize=(6, 6), dpi=70)
plt.bar(a3.Date, a3['Volume'], color='green', alpha=0.7)
plt.title(f'{symbol} Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()








fig10, ax10 = plt.subplots(figsize=(7, 4), dpi=70)
barlist = plt.bar(stock_data.index, int(stock_data['Volume']/1000))
#barlist.patches[a1.index.get_indexer(['United Kingdom'])[0]].set_facecolor('r')

plt.xticks(rotation = "vertical" )
plt.style.use('_mpl-gallery')
plt.ylabel("Revenue, kEuro")
plt.xlabel("Country")
plt.title("Online retail : UK value in kEuro")
plt.show()






# Correlation Heatmap
correlation_matrix = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title(f'Correlation Heatmap for {symbol} Financial Metrics')
plt.show()





fig, ax = plt.subplots(figsize = ( 5 , 5 ), dpi=100) 
sns.heatmap(stock_data.corr(numeric_only=True), cmap="YlGnBu", annot=True)





import pandas as pd
prices = pd.DataFrame([1035.23, 1032.47, 1011.78, 1010.59, 1016.03, 1007.95,
          1022.75, 1021.52, 1026.11, 1027.04, 1030.58, 1030.42,
          1036.24, 1015.00, 1015.20])
daily_return = prices.pct_change(1) # 1 for ONE DAY lookback
monthly_return = prices.pct_change(21) # 21 for ONE MONTH lookback
annual_return = prices.pct_change(252) #


