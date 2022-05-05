### Day 18 graphics, modules, work with documentation

import turtle as t # from x import * => everything from the x module
import random
colors = ["red", "blue", "green", "yellow", "orange", "gray", "DarkOrchid"]
directions = [0, 90, 180, 270]

tim = t.Turtle()
tim.shape("turtle")
tim.pensize(2)
tim.speed("fastest")

# tim = Turtle()
# tim.shape("turtle")
# tim.color("MidnightBlue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)


# for _ in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
#
# def square():
#     for _ in range (4):
#         tim.forward(100)
#         tim.right(90)


# square()

### Drawing a N-tagon


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range (num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range (3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
#

### Drawing a random walk


# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


### Generating a random color

# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


### Drawing a spirograph

# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range (int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + 10)
#         tim.circle(100)


#draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()