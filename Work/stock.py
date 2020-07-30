# Exercise 5.8

class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def sell(self, nshares):
        self.shares -= nshares

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, val):
        if not isinstance(val, int):
            raise TypeError('Expected int')
        self._shares = val

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"