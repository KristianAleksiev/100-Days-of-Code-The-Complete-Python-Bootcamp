### Day 26 - List and dictionaries comprehension

#new_list = [new_item for item in list]

### Python sequences (specific order)
#list
#range
#string
#tuple

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Kristian"
# new_list = [letter for letter in name]
# print(new_list)

# numbers = [1, 2, 3]
# new_numbers = [number * 2 for number in range(1, 5)]
# print(new_numbers)

### Conditional list comprehension

## new_list = [new_item FOR item IN list IF test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]

### 26.1 List comprehension - exercise

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
#
# print(squared_numbers)

### 26.2 List comprehension - exercise

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
#
# print(result)

### 26.3 List comprehension - exercise

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num in file_2_data]

### 26.4 Dictionary comprehension
## new_dict = {new_key: new_value for item in list}
## new_dict = {new_key: new_value for (key,value) in dict.items()}
## new_dict = {new_key: new_value for (key,value) in dict.items() if test}

# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_score = {student:random.randint(1, 100) for student in names}
# passed_students = {student: score for(student, score) in student_score.items() if score >= 60}
# print(passed_students)

### 26.5 Dictionary comprehension - exercise

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word) for word in sentence.split(" ")}
# print(result)

### 26.6 Dictionary comprehension - exercise

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

### 26.7 Iterating overa Pandas Data Frame

import pandas

student_dict = {
    "student": ["George", "James", "Lily"],
    "score": [56, 76, 98],
}
student_dataframe = pandas.DataFrame(student_dict)

#Looping through a row in a data frame

for (index, row) in student_dataframe.iterrows():
    #print(row.score)
    if row.student == "James":
        print(row.score)
