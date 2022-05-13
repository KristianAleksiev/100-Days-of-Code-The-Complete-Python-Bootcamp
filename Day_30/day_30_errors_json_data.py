### Day 30 - Errors, exceptions and saving JSON Data

#KeyError

# dictionary = {"key": "Value"}
# value = dictionary["non_existing_key"]

#IndexError
# list = ["Apple", "Banana"]
# fruit = list[3]

#TypeError
# text = "abc"
# print(text + 5)


#Try => except, else, finally

# try:
#     file = open("file.txt")
#     dictionary = {"key":"Value"}
#     print(dictionary["NoKey"])
# except FileNotFoundError:
#     open("file.txt", "w")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     raise KeyError

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 m.")

bmi = weight / height ** 2
print(bmi)
