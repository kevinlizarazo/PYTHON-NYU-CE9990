#!/usr/bin/env python

""" sort modification function """

stock_price_file = '../py_data/stock_prices.csv'
lines = open(stock_price_file).readlines()[1:]


def by_closelessopen(line):
    line = line.rstrip()
    ticker, date, opening, high, low, close, volume = line.split(',') 
    return float(close) - float(opening)


for line in sorted(lines, key=by_closelessopen, reverse=True)[0:5]:
    line = line.rstrip()
    ticker, date, opening, high, low, close, volume = line.split(',') 
    print '{} ({}): {} ({}->{})'.format(ticker,
                                       date, 
                                       (float(close)-float(opening)), 
                                       opening,
                                       close)

