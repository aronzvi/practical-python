# pcost.py
#
# Exercise 1.30

def portfolio_cost(filename):
    total_cost = 0

    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2].strip())
        cost = shares * price
        total_cost += cost

    f.close()
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')