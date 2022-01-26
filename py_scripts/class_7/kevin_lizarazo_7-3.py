#!/usr/bin/env python

""" stock prices sorted multi dimensional structures """ 

ticker_prices = dict()

fh = open('../python_data/stock_prices.csv')
lines = fh.readlines()[1:]

for line in lines:
    line = line.rstrip()
    ticker, date, opening, high, low, close, volume = line.split(',')
    if ticker not in ticker_prices:
        ticker_prices[ticker] = []
    ticker_prices[ticker].append(float(close))

sorted_keys = sorted(ticker_prices, key=lambda arg: max(ticker_prices[arg]) - min(ticker_prices[arg]), reverse=True)

for ticker in sorted_keys:
  print "{}: {} difference ({} - {})".format(ticker, max(ticker_prices[ticker]) - min(ticker_prices[ticker]), max(ticker_prices[ticker]), min(ticker_prices[ticker]))

