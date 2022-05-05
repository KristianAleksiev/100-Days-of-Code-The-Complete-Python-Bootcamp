###Printing exercise -

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


###String manipulation

print("Hello world!\nHello world!\nHello world!")

###Concatenation

print("Hello" + " " + "Kristian")

###    Debugging exercise 1-2

print("Day 1 - String Manipulation") #1. Missing double quotes before the word Day.
print("String Concatenation is done with the "+" sign.") #2. Outer double quotes changed to single quotes.
print('e.g. print("Hello " + "world"') #3. Extra indentation removed
print("New lines can be created with a backslash and n.") #4. Extra ( in print function removed.

###    Input function 1-3

print( len( input("What is your name? ") ) )

###    Variables 1-4

a = input("a: ")
c = a
b = input("b: ")
a = b
b = c
print(f"a:{a}")
print(f"b:{b}")

### Day 1 Project - Band name generator

print("Welcome to the Band Name Generator!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name could be " + city + " " + pet)
