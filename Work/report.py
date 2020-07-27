# report.py
#
# Exercise 4.7

import fileparse
import sys
import stock
import tableformat

headers = ('Name', 'Shares', 'Price', 'Change')

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        portdics = fileparse.parse_csv(f, select=['name','shares','price'], types=[str,int,float])
        portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdics]
        return portfolio

def read_prices(filename):
    with open(filename, 'rt') as f:
        prices = fileparse.parse_csv(f, types=[str,float], has_headers=False)
    return dict(prices)

def make_report(portfolio, prices):
    report = []

    for s in portfolio:
        name = (s.name)
        current_price = prices[name]
        change = current_price - s.price
        r = (name, s.shares, current_price, change)
        report.append(r)

    return report

def print_report(reportdata, formatter):
    '''
    Prints a nicely formated table from a list of (name, shares, price, change) tuples
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)

def main(argv):
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    main(sys.argv)