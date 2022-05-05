###  Functions, code blocks and While loops

###  6.1 Defining and calling python functions

def my_function():
    print("Hello") # Do action 1
    print("Bye") # Do action 2...n

my_function() #Calling the function => After is called it goes into the definition and executes

###  6.2 Reeborg challenge www.reeborg.ca

# def turn_arround():
#     turn_left()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

###  6.3 Hurdle challenge

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def sector():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for i in range (6):
#     sector()

### 6.3 With While loop in stead of For loop

# While not at_goal():
#   sector()
#
# ###  6.4 Reeborg conditions
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def sector():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         sector()
#     else:
#         move()

###  6.5 Reeborg hurdles race
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

###  6.6 Day 6 coding challenge - Reeborg's escape from the maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()

# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
