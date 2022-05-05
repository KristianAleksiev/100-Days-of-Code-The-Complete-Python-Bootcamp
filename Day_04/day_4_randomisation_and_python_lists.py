###  4.1 Random module

import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() # * X For needed end of range  #From 0 to 1 excluded, (from, to)
print(random_float)

love_score = random.randint(0, 100)
print(f"Your love score is {love_score}")

###  4.2 Heads or tails coding challenge

import random

random_side = random.randint(0, 1)

if random_side ==1:
    print("Heads")
else:
    print("Tails")

###  4.3 Lists

state1 = "Delaware"
state2 = "Pensylvania"
states_of_america = ["Delaware", "Pensylvania", "Alaska", "Hawaii"] #List datastructure, Left to right order

print(states_of_america[0]) #Accessing the first item on the list - Shift from beginning of the first element
pensylvania = states_of_america[1] #Positive index - from beginning of list, Negative[-1] -> Last element
states_of_america.append("Additional element") #Adding one more item at the end of list
states_of_america.extend(["Element1", "Element2", "Element3"]) #Extending a list with another list(More than 1 element)

##
# Splitting an input string
# input = "Angela,John,Yu"
# name_list = input.split(",") # -> Splitting a string into elements and creating a list with them
# print(name_list)
##

#   4.4 Coding exercise - Banker roulette - Who will pay the bill?

import random

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")
number_of_names = len(names)
random_choice = random.randint(0,number_of_names-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay the meal today.")

###  4.5 Nested lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][2]) # [Nested list number] [ Element of chosen list]

###  4.6 - Treasure map challenge

row1 = ["*", "*", "*"]
row2 = ["*", "*", "*"]
row3 = ["*", "*", "*"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}")

###   4.7 - Day 4 Challenge - Rock, paper, scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
comp_choice = random.randint(0, 2)
sign = ""

if comp_choice == 0:
    sign = rock
elif comp_choice == 1:
    sign = paper
elif comp_choice == 2:
    sign = scissors

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice > 2 or player_choice < 0:
    print(f"You typed an invalid number, you lose!\n Computer chose:\n {sign}")
else:
    print(game_images[player_choice])
    if player_choice == 0 and comp_choice == 2:
        print(f"You win!\nComputer chose:\n {sign}")
    elif comp_choice == 0 and player_choice == 2:
        print(f"You lose!\nComputer chose:\n {sign}")
    elif comp_choice > player_choice:
        print(f"You lose!\nComputer chose:\n {sign}")
    elif player_choice > comp_choice:
        print(f"You win!\nComputer chose:\n {sign}")
    elif comp_choice == player_choice:
        print(f"It's a draw!\nComputer chose:\n {sign}")

