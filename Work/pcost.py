# pcost.py
#
# Exercise 1.27
total_cost = 0

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
for line in f:
    row = line.split(',')
    shares = int(row[1])
    price = float(row[2].strip())
    cost = shares * price
    total_cost += cost

f.close()
print(f'Total cost {total_cost}')