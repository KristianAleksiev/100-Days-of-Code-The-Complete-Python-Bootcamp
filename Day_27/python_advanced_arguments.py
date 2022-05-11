###Python advanced arguments
##Arguments with Default values

# def my_function (a=1, b=2, c=3):
#     pass
# my_function() #Without Key or positional arguments, alreadY declared, can change value when calling

## Unlimited arguments
# def add(*args):
#     for n in args:
#         print(n)
# add(n1=5, n2=3)

# def add(*args):
#     print(args)
# add(3,5,6) #=> Tuple


# def add(*args):
#     print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

#print(add(3, 5, 6, 3, 2, 1))

### Unlimited keyword arguments - **kwargs

def calculate(n, **kwargs): #Creating unlimited keyword arguments
    print(kwargs) #=> Dictionary
    for key,value in kwargs.items():
        print(key)
        print(value)
        print(kwargs[1])
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)


calculate(2, add=3, multiply=5)

### Creating a class with unlimited arguments:


class Car:

    def __init__(self, **kwargs):
        self.__init__()
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make") # If value not inputed returns "None"
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R", colour="Red")
print(my_car.seats) # Returns "None"
