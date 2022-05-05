### Day 9 - Dictionaries and nesting

# {Key: Value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",\
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing somethign over and over again."
}
print(programming_dictionary["Bug"])

# Adding a new entry to the dictionary

programming_dictionary["New key"] = "Value"
print(programming_dictionary)

###Defining a new empty dictionary

empty_dictionary = {}
empty_dictionary["Loop"] = "The action ... (Value)"
print(empty_dictionary)

###Clear an existing dictionary
# programming_dictionary = {}

###Editing an item in the dicitonary

#programming_dictionary["Bug"] = "New Value"

###Looping through the dictionary

for i in programming_dictionary:
    print(i) #=> Printing the "Keys" in the empty_dictionary

for value in programming_dictionary:
    print(programming_dictionary[value]) # Prints the Values of the keys in the dictionary

### 9.1 Grading program challenge

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Nevil": 62,
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        student_grades[student] = "Fail"
    elif score <= 80:
        student_grades[student] = "Acceptable"
    elif score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score <= 100:
        student_grades[student] = "Outstanding"
print(student_grades)

### Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

### Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"] #-> Multiple values on a key
    "Germany": ["Berlin", "Hamburg", "Stuttgar"]
}
### Nesting a dictionary in a dictionary

travel_log = {
"France":{"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12},
"Germany":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":12},
}

### Nesting a dictionary in a list

travel_log = [
    {
     "country": "France",
     "cities_visited":["Paris", "Lille", "Dijon"],
     "total_visits":12
     },
    {
    "country": "Germany",
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
    "total_visits":5},
]

### 9.2 Coding exercise

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country (country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

### Day 9 Challenge - The secret auction program

import art

print(art.logo)
bids = {}
is_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not is_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n $"))
    bids[name] = price
    should_countinue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_countinue == "no":
        is_finished = True
        find_highest_bidder(bids)


