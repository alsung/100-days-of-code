# Unlimited Arguments / Unlimited Positional Arguments
def add(*args): # args is a tuple of argument values
    sum = 0
    for n in args:
        sum += n
    return sum

add(3, 5, 6, 2, 1, 5, 7, 8)


# Unlimited Keyword Arguments
def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # get returns None if argument is not specified rather than crashing
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)
print(my_car.model)