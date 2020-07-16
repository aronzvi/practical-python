# report.py
#
# Exercise 3.1

import csv

headers = ('Name', 'Shares', 'Price', 'Change')

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
                record = dict(zip(headers, row))
                holding = {'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price'])}
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

def print_report(report):
    '''
    Output the report
    '''
    
    print('%10s %10s %10s %10s' % headers)
    print('%s ' % (10 * '-') * len(headers))
    for name, shares, price, change in report:
        price_with_symbol = '$%.2f' % price
        print(f'{name:>10s} {shares:>10d} {price_with_symbol:>10s} {change:>10.2f}')

#portfolio = read_portfolio('Data/portfolio.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)



