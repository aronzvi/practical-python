# pcost.py
#
# Exercise 2.15
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for rowno, row in enumerate(rows, start=1):
        try:
            shares = int(row[1])
            price = float(row[2].strip())
            cost = shares * price
            total_cost += cost
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')

    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')