# pcost.py
#
# Exercise 1.33
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        try:
            shares = int(row[1])
            price = float(row[2].strip())
            cost = shares * price
            total_cost += cost
        except ValueError:
            print("Warning: couldn't parse", row)

    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')