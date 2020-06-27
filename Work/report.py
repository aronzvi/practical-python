# report.py
#
# Exercise 2.11

import csv

headers = ('Name', 'Shares', 'Price', 'Change')

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

def make_report(portfolio, prices):
    report = []

    for s in portfolio:
        name = (s['name'])
        current_price = prices[name]
        change = current_price - s['price']
        r = (name, s['shares'], current_price, change)
        report.append(r)

    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

print('%10s %10s %10s %10s' % headers)
print('%s ' % (10 * '-') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
