### Day 24 - Working with local files and directories
# Updating the snake game project

# file = open("MY_FILE.txt")
# content = file.read()
# print(content)
# file.close()

# with open("MY_FILE.txt") as file:
#     content = file.read()
#     print(content)

# with open("MY_FILE.txt", mode="w") as file: #Clears the file and changes the text with the new one
#     file.write("New text")

# with open("MY_FILE.txt", mode="a") as file: #Appends the new text to the previous existing one in the file
#     file.write("\nNew text.")


    ### Relative and absolute file paths

# with open("/Users/Workstation/Desktop/MY_FILE.txt") as file: # Absolut
#     content = file.read()
#     print(content)

# with open("../../Desktop/my_file.txt") as file: # Relative to the current file directory
#     content = file.read()
#     print(content)


### READLINES() METHOD
#Returns all lines in the file, as a list. Each line is an item in the list
f = open("demo.txt", "r")
print(f.readlines())

### REPLACE() METHOD
#Replaces the string with another
txt = "I like bananas"
x = txt.replace("bananas", "strawberries")
print(x) #=> "I like strawberries

### STRIP() METHOD
#Removes the spaces at the beginning and the end of string
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favourite") #=> of all fruits, banana, is my favourite