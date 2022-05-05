### Day 12 - Scope and Number guessing game

# Defining a variable -> Global or local scope - Namespace

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"Inside function enemies =>{enemies}") #Defined within the function (Local scope)


# increase_enemies()
# print(f"enemies outside function: {enemies}") #Defined outside of the function (Global scope)

### No Block Scope in python

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]


# def create_enemy():
#     if game_level <5:
#         new_enemy = enemies[0]
# print(new_enemy) ## Error, outside the function, NameError

### Modifying global variable inside the function

# enemies = 1


# def increase_enemies():
#     """Takes a variable defined outside of the function and modifies it"""
#     global enemies
#     enemies +=1


# increase_enemies()

### Global constants
#Always uppercase
PI = 3.14159

### Day 12 Project - The number guessing game

#Choosing a random number between 1 and 100
#Difficulty function
#User guess
#Comparing user's guess and the actual answer
#Track the number of user guesses +/-
#Repeating the guess functionality

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0

    while guess != answer:
      print(f"You have {turns} attempts remaining to guess the number.")

      #Let the user guess a number.
      guess = int(input("Make a guess: "))

      #Track the number of turns and reduce by 1 if they get it wrong.
      turns = check_answer(guess, answer, turns)
      if turns == 0:
        print("You've run out of guesses, you lose.")
        return
      elif guess != answer:
        print("Guess again.")


game()