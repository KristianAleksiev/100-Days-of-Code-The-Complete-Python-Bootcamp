### Day 14 - Higher lower game project

import random
from art import logo, vs
from game_data import data


def get_random_account():
    """Gets a random account from data"""
    return random.choice(data)


def format_data (account):
    """Takes the account data and returns printable format"""
    name = account["name"]
    descr = account["description"]
    country = account["country"]
    return f"{name}, a {descr}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks the number of followers against the guess and if it is right returns True"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    game_should_continue = True
    score = 0
    account_b = get_random_account()
    account_a = get_random_account()
    print(logo)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        guess = input("Who has more followers? Type 'A' or 'B'").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score +=1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry that's wrong. Final score {score}")


game()