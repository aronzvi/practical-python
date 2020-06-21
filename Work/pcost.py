# pcost.py
#
# Exercise 1.31

def portfolio_cost(filename):
    total_cost = 0

    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        try:
            row = line.split(',')
            shares = int(row[1])
            price = float(row[2].strip())
            cost = shares * price
            total_cost += cost
        except ValueError:
            print("Warning: couldn't parse", line, end='')

    f.close()
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')