# pcost.py
#
# Exercise 9.1

import csv
import sys
from . import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'
    
    cost = portfolio_cost(filename)
    print(f'Total cost {cost}')

if __name__ == '__main__':
    main(sys.argv)
