# Exercise 1 : Built-In Functions
# Instructions:
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# 1 - Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# 2 - Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

from logging import exception


print("----- EX1 -----")

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def eli_funct() -> None:
    """
    proof that i know how to use the __doc__ ... 
    """

    pass

print(eli_funct.__doc__)

# Exercise 2: Currencies
# Instructions:

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

print("----- EX2 -----")

class Currency:

    def __init__(self:object, currency:str, amount:int):

        self.currency = currency
        self.amount = amount


    def __str__(self:object) -> str:
        return f"{self.amount}  {self.currency}"


    def __int__(self:object) -> int:
        return self.amount


    def __repr__(self:object) -> str:
        return self.__str__() 


    def __add__(self:object, other) -> int:
        if type(other) == int:
            return self.amount + other
        elif self.currency == other.currency:
            return self.amount + int(other)
        else:
            raise Exception (f"Cannot add between Currency type {self.currency} and {other.currency}")

    def __call__(self:object) -> str:
       return self.__repr__()
         
    def __iadd__(self:object, other):
        self.amount += int(other)
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1()) 
c1 += 5 
print(c1())
c1 += c2
print(c1())
c1 + c3