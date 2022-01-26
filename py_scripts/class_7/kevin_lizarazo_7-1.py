#!/usr/bin/env python

""" sort modification function, lambda """

stock_price_file = '../python_data/stock_prices.csv'
lines = open(stock_price_file).readlines()[1:]

for line in sorted(lines, key=lambda this_line: float(this_line.split(',')[5])-float(this_line.split(',')[2]), reverse=True)[0:5]:
    line = line.rstrip()
    ticker, date, opening, high, low, close, volume = line.split(',') 
    print '{} ({}): {} ({}->{})'.format(ticker,
                                       date, 
                                       (float(close)-float(opening)), 
                                       opening,
                                       close)

