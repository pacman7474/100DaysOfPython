def add(*args):
    total = 0
    for x in args:
        total += x
    return total

#print(add(1,2,3,4,5))

def calculate (n, **kwargs):
    #for key, value in kwargs.items():
    #    pass
    n += kwargs["add"]
    n *= kwargs["multiply"]
#    print(n)

calculate(2, add=3,multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Ford")
print(my_car.make, my_car.model)