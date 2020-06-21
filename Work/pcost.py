# pcost.py
#
# Exercise 1.32
import csv

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

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')