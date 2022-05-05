###  3.1 Conditional operator / Logical operator - Rollercoaster exercise

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:  # Comparisson operators
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are 12.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    
    if wants_photo == "Y":
        bill += 3
        # add 3$ to their bill
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

###  3.2 Odd or even exercise

number = int(input("Which number do you want to choose?"))
if number % 2 ==0:
    print("This is an even number.")
else:
    print("This is an odd number.")

###  3.3 BMI Calculator 2.0 Exercise

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / float(height) ** 2

if bmi <18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi <25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi <30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi <35:
    print(f"Your BMI is {round(bmi)}, you are slightly obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")

###  3.4 Leap year exercise

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    print("Leap year")
else:
    print("Not leap year.")

###  3.5 - Pizza order - Exercise

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni? Y, N")
extra_cheese = input("Do you want extra cheese? Y, N")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}.")

###  3.6 - Love Calculator - Exercise

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")

#   Day 3 Project - Treasure island game

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' \n")
left_or_right = left_or_right.lower()

if left_or_right != "left":
    print("You fell into a hole. Game over.")
else:
    swim_or_wait = input("You have come to a lake. There is an island in the middle of it. "
                         "Would you rather swim or wait for a boat? swim / wait \n")
    swim_or_wait = swim_or_wait.lower()
    if swim_or_wait != "wait":
        print("You have been attacked by trout. Game over.")
    else:
        door = input("Which door do you choose? red / blue / yellow \n")
        door = door.lower()
        if door == "red":
            print("You have been burned by fire. Game over.")
        elif door == "yellow":
            print("You win!")
        elif door == "blue":
            print("You have been eaten by beasts. Game over.")
        else:
            print("Game over.")
