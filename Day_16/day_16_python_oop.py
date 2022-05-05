### Day 16 - Object oriented programming in python

#car = CarBlueprint() #Pascal case
#Object     #Class

### 6.1 Turtle

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.color("blue3")
# timmy.shape("turtle")
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)


# my_screen.exitonclick()

### 6.2 PrettyTable


from prettytable import PrettyTable
table = PrettyTable() #Creating an object called table from the class PrettyTable (blueprint)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) #Called method add_column
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)

### 6.3 OOP version of Coffee machine project


