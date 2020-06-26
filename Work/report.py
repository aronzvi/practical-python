# report.py
#
# Exercise 2.7

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

stocks = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

orig_value = 0
current_value = 0
for s in stocks:
    orig_value += s['shares'] * s['price']
    current_value += s['shares'] * prices[s['name']]

print('original portfolio value', orig_value)
print('current portfolio value:', current_value)
print(f'gain/loss: {current_value - orig_value:0.3f}', )