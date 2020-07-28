# Exercise 4.9

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def sell(self, nshares):
        self.shares -= nshares

    def cost(self):
        return self.shares * self.price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"