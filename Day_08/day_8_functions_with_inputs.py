# ### Day 8 - Functions with inputs - Arguments and parameters


def greet():
    print("Hello")
    print("How do you do")
    print("Isn't the weather nice today?")


greet()

# ###Function with input


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Georgi")

# ###Functions with more than 1 input


def greet_with(name, location):  # - name, location - parameters
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Georgi", "Varna")  # inputs -> asigning the positional arguments to the parameters

### Keyword arguments


def greet_with(name, location):  # - name, location - parameters
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with(name="Georgi", location="Varna")

### 8.1 Paint area calculator - coding challenge

import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage_per_can = 5


def paint_calc (height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You will need {number_of_cans} cans of paint.")


paint_calc(height=test_h, width=test_w, cover=coverage_per_can)

### 8.2 Prime number checker - coding challenge

n = int(input("Check this number: "))


def prime_checker (number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(number = n)

### 8.3 Day 8 project - The Caeser cipher

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', \
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', \
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


### Solution with defining 1 function

def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # Fixed problem of bigger shift than the numbers in the alphabet
    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

### Solution with defining two functions


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text +=new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)



