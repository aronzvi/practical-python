# report.py
#
# Exercise 2.6

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
                holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
                portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Error: bad value for row')
                pass
    return prices