# Exercise 9.1

from .typedproperty import String, Integer, Float

class Stock:
    __slots__ = ('_name', '_shares', '_price')
    
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def sell(self, nshares):
        self.shares -= nshares

    @property
    def cost(self):
        return self.shares * self.price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"