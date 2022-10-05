#default values in functions

def my_function(a=2, b=4):
    return a*b

print(my_function())
#return 8
print(my_function(b=5))
#retun 10


# Any number of args, (variable does not have to be args

def add(*args):
    for n in args:
        print(n)
    return sum(args)

print(add(2, 8, 9, 4))

## Kwards (key word arguments)  Two ** s

def calculate(n, **kwargs):
#    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add = 3, multiply = 5))
## Creates a dictionary in the function

#print(calculate(4, add = 20))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.style = kw.get("style")
## using get means keywords don't have to exist

my_car = Car(make="Chevy", color= "red")

print(my_car.color)
print(my_car.model)