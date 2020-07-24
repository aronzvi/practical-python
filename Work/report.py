# report.py
#
# Exercise 3.16

import fileparse
import sys

headers = ('Name', 'Shares', 'Price', 'Change')

def read_portfolio(filename):
    portfolio = fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
    prices = fileparse.parse_csv(filename, types=[str,float], has_headers=False)
    return dict(prices)

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

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    main(sys.argv)