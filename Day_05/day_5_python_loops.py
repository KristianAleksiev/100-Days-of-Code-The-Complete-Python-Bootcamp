###  5-1 For loop with lists
fruits = ["Apple", "Peach", "Pear"]
for items in fruits:
    print(items)

###  5-2 "Average height" coding challenge

student_heights = input("Input a list of student heights ").split()
sum_heights = 0
total_height = 0

for height in student_heights:
    total_height += int(height)

number_of_students = 0

for students in student_heights:
    number_of_students +=1

avg_height = round(total_height / number_of_students)
print(avg_height)

### 5-3 "High score" coding challenge

import sys

student_scores = input("Input a list of student scores.").split(" ")
for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = -sys.maxsize

for highest in student_scores:
    if highest > max_score:
        max_score = highest

print(f"The highest score in the class is: {max_score}")

###  5-4 For loops in range()

total = 0
for number in range(1, 101):
    total += number
print(total)

###  5-5 Adding evens - coding challenge

sum_even = 0
for even in range(2, 101, 2):
    sum_even += even
print(sum_even)

###  5-6 TheFizzBuzz interview question.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

###  Day 5 Project - Random password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', \
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#####    #Solution number 1 - Without shuffle
print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
for sym in range (1, nr_symbols +1):
    random_sym = random.choice(symbols)
    password += random_sym
for sym in range (1, nr_numbers +1):
    random_num = random.choice(numbers)
    password +=random_num
print(password)

#####    #Solution number 2 - Completely random
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for sym in range (1, nr_symbols +1):
    password_list.append(random.choice(symbols))
for sym in range (1, nr_numbers +1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""

for char in password_list:
    password +=char
print(f"Your password is {password}")
