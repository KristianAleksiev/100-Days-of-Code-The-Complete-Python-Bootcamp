### 2.1 - Data types - Exercise 1

two_digit_number = input("Write a two digit number: ")
first_number = two_digit_number[0]
second_number = two_digit_number[1]
result = int(first_number) + int(second_number)
print(result)

### 2.2 - Mathematical operations - Exercise 2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / float(height) ** 2
print(round(bmi))

### 2.3 - Number manipulation and F-Strings in Python - Exercise 3

age = input("What is your current age? ")
years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# 2.4 Day 2 Project - Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percantage tip would you like to give? ")) / 100
total_people = int(input("How many people to split the bill? "))
bill_per_person = (bill + bill * tip_percentage) / total_people
print(f"Each person should pay: ${bill_per_person:.2f}")
