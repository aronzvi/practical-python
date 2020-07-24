# pcost.py
#
# Exercise 3.15

import csv
import sys
import report

def portfolio_cost(filename):
    total_cost = 0
    portfolio = report.read_portfolio(filename)
    for record in portfolio:
        total_cost += record['shares'] * record['price']
    return total_cost

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'
    
    cost = portfolio_cost(filename)
    print(f'Total cost {cost}')
